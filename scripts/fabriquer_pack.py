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
import html
import json
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path
from xml.etree import ElementTree

import pack_supports

from config import load_formation_config

RACINE = Path(__file__).resolve().parent.parent
CONFIG = load_formation_config()
PACK = RACINE / CONFIG["livrables"]
STAGIAIRES = PACK / "Livrables-Stagiaires"
MD2PDF = RACINE / "vendor" / "accessible-pdf" / "scripts" / "md2pdf.py"
ALT_IGPDE = "République française - IGPDE"
BANDEAU_MEMO = RACINE / "fiche-pratique" / "bandeau-igpde-logos.jpg"
BANDEAU_FICHE = (
    STAGIAIRES / "fil-rouge-principes-wcag-igpde" / "assets" / "bandeau-igpde.jpg"
)

# (source Markdown, PDF produit, bandeau, options supplémentaires, copie éventuelle dans le pack)
PDFS = [
    (
        "fiche-pratique/memo-word.md",
        "fiche-pratique/memo-word-accessibilite.pdf",
        BANDEAU_MEMO,
        [
            "--header-text",
            "Mémo accessibilité - Microsoft Word",
            "--page-total-footer",
            "--subtitle",
            "Les 5 étapes du parcours Word :",
            "--subtitle-list-item",
            "Structurer et naviguer",
            "--subtitle-list-item",
            "Rendre les contenus et les liens compréhensibles",
            "--subtitle-list-item",
            "Sécuriser les couleurs, les graphiques et les tableaux",
            "--subtitle-list-item",
            "Régler les langues et la lisibilité",
            "--subtitle-list-item",
            "Finaliser, vérifier, exporter et contrôler",
        ],
        STAGIAIRES / "tp-word-igpde",
    ),
    (
        "fiche-pratique/memo-libreoffice-writer.md",
        "fiche-pratique/memo-libreoffice-writer-accessibilite.pdf",
        BANDEAU_MEMO,
        [
            "--header-text",
            "Mémo accessibilité - LibreOffice Writer",
            "--page-total-footer",
            "--subtitle",
            "Les 5 étapes du parcours Writer :",
            "--subtitle-list-item",
            "Structurer et naviguer",
            "--subtitle-list-item",
            "Rendre les contenus et les liens compréhensibles",
            "--subtitle-list-item",
            "Sécuriser les couleurs, les graphiques et les tableaux",
            "--subtitle-list-item",
            "Régler les langues et la lisibilité",
            "--subtitle-list-item",
            "Finaliser, vérifier, exporter et contrôler",
        ],
        STAGIAIRES / "tp-word-igpde",
    ),
    (
        "_source/checklist-accessibilite-bureautique.md",
        f"{CONFIG['livrables']}/Livrables-Stagiaires/tp-word-igpde/checklist-accessibilite-bureautique.pdf",
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
        "wcag/fiche-stagiaire-principes-wcag.md",
        f"{CONFIG['livrables']}/Livrables-Stagiaires/fil-rouge-principes-wcag-igpde/fiche-stagiaire-principes-wcag.pdf",
        BANDEAU_FICHE,
        [],
        None,
    ),
    (
        "liens-tp-en-ligne.md",
        f"{CONFIG['livrables']}/Livrables-Stagiaires/liens-pour-les-stagiaires.pdf",
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
    cible = STAGIAIRES / "supports-projections" / CONFIG["output"]
    if cible.exists() and contenu_deck(cible) == contenu_deck(source):
        print(f"[deck] {cible.relative_to(RACINE)} déjà à jour (contenu identique)")
        return
    cible.parent.mkdir(parents=True, exist_ok=True)
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


def contenu_favori_andi(url):
    return (
        '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n'
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n'
        '<TITLE>ANDI - favori à importer</TITLE>\n'
        '<H1>ANDI - favori à importer</H1>\n'
        '<DL><p>\n'
        f'    <DT><A HREF="{html.escape(url, quote=True)}">ANDI</A>\n'
        '</DL><p>\n'
    ).encode("utf-8")


def outils(telecharger=False):
    dossier = PACK / "outils"
    manifeste = json.loads((dossier / "outils.json").read_text(encoding="utf-8"))
    problemes = 0
    for outil in manifeste["outils"]:
        cible = dossier / outil["fichier"]
        if not cible.exists() and telecharger and outil.get("url"):
            print(f"[outils] téléchargement de {outil['fichier']}")
            cible.parent.mkdir(parents=True, exist_ok=True)
            temporaire = cible.with_suffix(cible.suffix + ".partiel")
            try:
                urllib.request.urlretrieve(outil["url"], temporaire)
            except Exception as erreur:
                temporaire.unlink(missing_ok=True)
                print(f"[outils] ÉCHEC {outil['fichier']} : {erreur}")
                problemes += 1
                continue
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
    favori = manifeste["favori_andi"]
    contenu = contenu_favori_andi(favori["url"])
    for fichier in favori["fichiers"]:
        cible = dossier / fichier
        if not cible.exists() and telecharger:
            cible.parent.mkdir(parents=True, exist_ok=True)
            cible.write_bytes(contenu)
        if not cible.exists():
            print(f"[outils] MANQUANT {fichier} (source : make outils-telecharger)")
            problemes += 1
        elif cible.stat().st_size != favori["taille"] or sha256(cible) != favori["sha256"]:
            print(f"[outils] INVALIDE {fichier} : taille ou empreinte différente du manifeste")
            problemes += 1
        else:
            print(f"[outils] OK {fichier}")
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
        pack_supports.tp_reseaux_sociaux(RACINE, STAGIAIRES)
        pack_supports.docx_sami(RACINE, STAGIAIRES)
    if args.commande in ("outils", "tout") and outils(args.telecharger):
        sys.exit(1)


if __name__ == "__main__":
    main()
