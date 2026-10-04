"""Fabrique le pack livrable de la session à partir des sources de l'usine.

Commandes :
  deck    copie le deck généré (config.yml : output) dans le pack
  pdf     régénère les PDF accessibles (mémos, fiches WCAG, fiche des liens)
  supports démo réseaux sociaux hors ligne et documents Sami
  outils  vérifie les installeurs (taille et SHA-256), --telecharger pour les récupérer
  tout    deck + pdf + supports + outils
"""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path
from xml.etree import ElementTree

from config import load_formation_config
import pack_supports

RACINE = Path(__file__).resolve().parent.parent
CONFIG = load_formation_config()
PACK = RACINE / CONFIG["livrables"]
FORMATEUR = PACK / "Formateur"
MD2PDF = RACINE / "vendor" / "accessible-pdf" / "scripts" / "md2pdf.py"
ALT_IGPDE = "République française - IGPDE"
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
        ["--header-text", "Mémo accessibilité - Microsoft Word"],
        FORMATEUR / "tp-word-igpde",
    ),
    (
        "fiche-pratique/memo-libreoffice-writer.md",
        "fiche-pratique/memo-libreoffice-writer-accessibilite.pdf",
        BANDEAU_MEMO,
        ["--header-text", "Mémo accessibilité - LibreOffice Writer"],
        FORMATEUR / "tp-word-igpde",
    ),
    (
        "_source/checklist-accessibilite-bureautique.md",
        f"{CONFIG['livrables']}/Formateur/tp-word-igpde/checklist-accessibilite-bureautique.pdf",
        BANDEAU_MEMO,
        [
            "--header-text",
            "Checklist accessibilité des documents bureautiques",
            "--no-toc",
            "--subtitle",
            "Suivi progressif du TP Word accessible",
        ],
        None,
    ),
    (
        "wcag/fiche-formateur-principes-wcag.md",
        f"{CONFIG['livrables']}/Formateur/fil-rouge-principes-wcag-igpde/fiche-formateur-principes-wcag.pdf",
        BANDEAU_FICHE,
        [],
        None,
    ),
    (
        "wcag/fiche-stagiaire-principes-wcag.md",
        f"{CONFIG['livrables']}/Formateur/fil-rouge-principes-wcag-igpde/fiche-stagiaire-principes-wcag.pdf",
        BANDEAU_FICHE,
        [],
        None,
    ),
    (
        "liens-tp-en-ligne.md",
        f"{CONFIG['livrables']}/Formateur/liens-pour-les-stagiaires.pdf",
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


def nombre_modules():
    from slides import discover_slides

    return len(discover_slides())


def nombre_slides(pptx):
    with zipfile.ZipFile(pptx) as archive:
        return sum(
            1
            for nom in archive.namelist()
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", nom)
        )


def contenu_deck(pptx):
    # Compare les parties, pas les octets : l'archive date chaque régénération.
    with zipfile.ZipFile(pptx) as archive:
        parties = {}
        for nom in archive.namelist():
            contenu = archive.read(nom)
            if nom == "docProps/core.xml":
                racine = ElementTree.fromstring(contenu)
                date_modification = racine.find("{http://purl.org/dc/terms/}modified")
                if date_modification is not None:
                    date_modification.text = ""
                contenu = ElementTree.tostring(racine, encoding="utf-8")
            parties[nom] = contenu
        return parties


def deck():
    source = RACINE / CONFIG["output"]
    if not source.exists():
        sys.exit(f"Deck introuvable : {source}. Lancer d'abord : make deck")
    attendu, present = nombre_modules(), nombre_slides(source)
    if present < attendu:
        sys.exit(
            f"Deck partiel : {present} slides pour {attendu} modules (génération --only, "
            "--from ou --to). Livrable du pack inchangé ; lancer make deck pour un deck complet."
        )
    cible = FORMATEUR / CONFIG["output"]
    if cible.exists() and contenu_deck(cible) == contenu_deck(source):
        print(f"[deck] {cible.relative_to(RACINE)} déjà à jour (contenu identique)")
        return
    shutil.copy2(source, cible)
    retirer_quarantaine(cible)
    print(f"[deck] {source.name} copié dans {cible.relative_to(RACINE)}")


def est_pdf_ua(chemin):
    """Vrai si le PDF déclare PDF/UA-1 et porte un arbre de structure.

    Quand WeasyPrint refuse le mode PDF/UA-1, le générateur bascule sans échouer
    sur un PDF sans structure : on contrôle le fichier produit, pas son message."""
    import pikepdf

    with pikepdf.open(chemin) as document:
        return (
            document.open_metadata().get("pdfuaid:part") == "1"
            and "/StructTreeRoot" in document.Root
        )


def pdf():
    for source, sortie, bandeau, options, copie in PDFS:
        # Génération à côté du livrable : il n'est remplacé que par un PDF/UA-1.
        temporaire = RACINE / f"{sortie}.partiel"
        resultat = pack_supports.generer_pdf(
            MD2PDF, RACINE / source, temporaire, bandeau, ALT_IGPDE, options
        )
        standard = next(
            (
                ligne.strip()
                for ligne in resultat.stdout.splitlines()
                if "Standard" in ligne
            ),
            "?",
        )
        if resultat.returncode != 0:
            temporaire.unlink(missing_ok=True)
            sys.exit(
                f"[pdf] échec pour {source} :\n{resultat.stdout}\n{resultat.stderr}"
            )
        if not est_pdf_ua(temporaire):
            temporaire.unlink(missing_ok=True)
            sys.exit(
                f"[pdf] {source} n'est pas en PDF/UA-1 ({standard}) : {sortie} inchangé. "
                "Cause connue : tableau coupé entre deux pages (WeasyPrint, « Table wrapper "
                "without a table ») ; voir le contournement en tête des sources de wcag/."
            )
        temporaire.replace(RACINE / sortie)
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
    analyseur.add_argument(
        "commande", choices=["deck", "pdf", "supports", "outils", "tout"]
    )
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
    if args.commande in ("outils", "tout") and outils(args.telecharger):
        sys.exit(1)


if __name__ == "__main__":
    main()
