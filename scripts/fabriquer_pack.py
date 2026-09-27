"""Fabrique le pack livrable de la session à partir des sources de l'usine.

Commandes :
  deck    copie le deck généré (config.yml : output) dans le pack
  pdf     régénère les PDF accessibles (mémos, fiches WCAG, fiche des liens)
  supports démo réseaux sociaux hors ligne, documents Sami, export PDF du deck
  outils  vérifie les installeurs (taille et SHA-256), --telecharger pour les récupérer
  tout    deck + pdf + supports + outils
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import pack_supports
import yaml

RACINE = Path(__file__).resolve().parent.parent
CONFIG = yaml.safe_load((RACINE / "config.yml").read_text(encoding="utf-8"))[
    "formation"
]
PACK = RACINE / CONFIG["livrables"]
FORMATEUR = PACK / "Formateur"
MD2PDF = RACINE / "vendor" / "accessible-pdf" / "scripts" / "md2pdf.py"
ALT_IGPDE = "IGPDE - Institut de la Gestion publique et du Développement économique"
BANDEAU_MEMO = RACINE / "fiche-pratique" / "bandeau-igpde-logos.jpg"
BANDEAU_FICHE = (
    FORMATEUR / "fil-rouge-principes-wcag-igpde" / "assets" / "bandeau-igpde.jpg"
)

# (source Markdown, PDF produit, bandeau, options supplémentaires, copie éventuelle dans le pack)
PDFS = [
    (
        "fiche-pratique/memo-word.md",
        "fiche-pratique/memo-word-accessibilite.pdf",
        BANDEAU_MEMO,
        [],
        FORMATEUR / "tp-word-igpde",
    ),
    (
        "fiche-pratique/memo-libreoffice-writer.md",
        "fiche-pratique/memo-libreoffice-writer-accessibilite.pdf",
        BANDEAU_MEMO,
        [],
        FORMATEUR / "tp-word-igpde",
    ),
    (
        "wcag/cadre-legal-principes-wcag-fiche-formateur.md",
        f"{CONFIG['livrables']}/Formateur/fil-rouge-principes-wcag-igpde/cadre-legal-principes-wcag-fiche-formateur.pdf",
        BANDEAU_FICHE,
        [],
        None,
    ),
    (
        "wcag/fiche-stagiaire-principes-wcag-a-garder-sous-la-main.md",
        f"{CONFIG['livrables']}/Formateur/fil-rouge-principes-wcag-igpde/fiche-stagiaire-principes-wcag-a-garder-sous-la-main.pdf",
        BANDEAU_FICHE,
        [],
        None,
    ),
    (
        "liens-tp-en-ligne.md",
        f"{CONFIG['livrables']}/Formateur/liens-tp-en-ligne.pdf",
        BANDEAU_FICHE,
        ["--no-toc"],
        None,
    ),
]


def retirer_quarantaine(chemin):
    if sys.platform == "darwin":
        subprocess.run(
            ["xattr", "-d", "com.apple.quarantine", str(chemin)],
            capture_output=True,
            check=False,
        )


def deck():
    source = RACINE / CONFIG["output"]
    if not source.exists():
        sys.exit(f"Deck introuvable : {source}. Lancer d'abord : make deck")
    cible = FORMATEUR / CONFIG["output"]
    shutil.copy2(source, cible)
    retirer_quarantaine(cible)
    print(f"[deck] {source.name} copié dans {cible.relative_to(RACINE)}")


def pdf():
    for source, sortie, bandeau, options, copie in PDFS:
        commande = [
            sys.executable,
            str(MD2PDF),
            str(RACINE / source),
            "--template",
            "formation",
            "--lang",
            "fr",
            "--logo",
            str(bandeau),
            "--logo-alt",
            ALT_IGPDE,
            "-o",
            str(RACINE / sortie),
            *options,
        ]
        resultat = subprocess.run(commande, capture_output=True, text=True, check=False)
        standard = next(
            (
                ligne.strip()
                for ligne in resultat.stdout.splitlines()
                if "Standard" in ligne
            ),
            "?",
        )
        if resultat.returncode != 0:
            sys.exit(
                f"[pdf] échec pour {source} :\n{resultat.stdout}\n{resultat.stderr}"
            )
        retirer_quarantaine(RACINE / sortie)
        print(f"[pdf] {sortie} ({standard})")
        if copie is not None:
            shutil.copy2(RACINE / sortie, copie / Path(sortie).name)
            print(f"      copié dans {copie.relative_to(RACINE)}")


def sha256(chemin):
    empreinte = hashlib.sha256()
    with open(chemin, "rb") as flux:
        for bloc in iter(lambda: flux.read(1 << 20), b""):
            empreinte.update(bloc)
    return empreinte.hexdigest()


def outils(telecharger=False):
    dossier = PACK / "outils"
    manifeste = json.loads((dossier / "outils.json").read_text(encoding="utf-8"))
    problemes = 0
    for outil in manifeste["outils"]:
        cible = dossier / outil["fichier"]
        if not cible.exists() and telecharger and outil.get("url"):
            print(f"[outils] téléchargement de {outil['fichier']}")
            temporaire = cible.with_suffix(cible.suffix + ".partiel")
            urllib.request.urlretrieve(outil["url"], temporaire)
            if sha256(temporaire) != outil["sha256"]:
                temporaire.unlink()
                print(
                    f"[outils] REFUSÉ {outil['fichier']} : empreinte différente du manifeste"
                )
                problemes += 1
                continue
            temporaire.rename(cible)
        if not cible.exists():
            ou = (
                outil.get("url") and "make outils-telecharger" or outil.get("page", "?")
            )
            print(f"[outils] MANQUANT {outil['fichier']} (source : {ou})")
            problemes += 1
        elif (
            cible.stat().st_size != outil["taille"] or sha256(cible) != outil["sha256"]
        ):
            print(
                f"[outils] INVALIDE {outil['fichier']} : taille ou empreinte différente du manifeste"
            )
            problemes += 1
        else:
            print(f"[outils] OK {outil['fichier']}")
    return problemes


def main():
    analyseur = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    analyseur.add_argument("commande", choices=["deck", "pdf", "supports", "outils", "tout"])
    analyseur.add_argument(
        "--telecharger", action="store_true", help="récupère les installeurs manquants"
    )
    args = analyseur.parse_args()
    if args.commande in ("deck", "tout"):
        deck()
    if args.commande in ("pdf", "tout"):
        pdf()
    if args.commande in ("supports", "tout"):
        pack_supports.tp_reseaux_sociaux(RACINE, FORMATEUR)
        pack_supports.docx_sami(RACINE, FORMATEUR)
        pack_supports.pdf_deck(RACINE, FORMATEUR, CONFIG["output"])
    if args.commande in ("outils", "tout") and outils(args.telecharger):
        sys.exit(1)


if __name__ == "__main__":
    main()
