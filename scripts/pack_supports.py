"""Étapes du pack qui ne passent pas par le générateur PDF.

- tp_reseaux_sociaux : variante hors ligne de la démo émojis (ressources DSFR
  locales, navigation du site en liens absolus vers le site publié)
- docx_sami : copie des trois documents de l'exercice Sami dans le pack
- pdf_deck : export PDF du deck pour les notes formateur (LibreOffice)
- generer_pdf : lance le générateur PDF avec des images résolues depuis l'usine
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SITE_PUBLIE = "https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/"
PAGES_DU_MENU = [
    "index.html",
    "site-inaccessible/index.html",
    "site-aide-correction/index.html",
    "site-accessible/index.html",
    "plan-du-site.html",
    "accessibilite.html",
    "mentions-legales.html",
    "donnees-personnelles.html",
]
DEMO = "demo-mauvaise-restitution-emojis.html"
DOCX_TP = [
    "tp-doc-accessible.docx",
    "tp-doc-aide-correction.docx",
    "tp-doc-inaccessible.docx",
]
SOFFICE = Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")


def tp_reseaux_sociaux(racine, formateur):
    docs = racine / "docs"
    cible = formateur / "tp-reseaux-sociaux-igpde"
    images = cible / "assets" / "shared" / "images"
    images.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        docs / "assets" / "dsfr",
        cible / "assets" / "dsfr",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".DS_Store"),
    )
    shutil.copy2(docs / "assets" / "site.css", cible / "assets" / "site.css")
    shutil.copy2(
        docs / "assets" / "shared" / "images" / "igpde-operator-logo.jpg", images
    )
    html = (docs / DEMO).read_text(encoding="utf-8")
    for page in PAGES_DU_MENU:
        html = html.replace(f'href="{page}"', f'href="{SITE_PUBLIE}{page}"')
    (cible / DEMO).write_text(html, encoding="utf-8")
    print(f"[supports] démo hors ligne : {(cible / DEMO).relative_to(racine)}")


def docx_sami(racine, formateur):
    cible = formateur / "tp-word-igpde"
    # Liste explicite : un document manquant fait échouer la copie.
    for nom in DOCX_TP:
        shutil.copy2(racine / "_source" / nom, cible / nom)
        print(f"[supports] {nom} copié dans {cible.relative_to(racine)}")


def pdf_deck(racine, formateur, nom_deck):
    """Exporte le deck en PDF dans _alex/. Retourne False si LibreOffice est absent."""
    if not SOFFICE.exists():
        print(f"[supports] LibreOffice absent ({SOFFICE}) : export PDF du deck ignoré")
        return False
    deck = racine / nom_deck
    with (
        tempfile.TemporaryDirectory() as profil,
        tempfile.TemporaryDirectory() as sortie,
    ):
        subprocess.run(
            [
                str(SOFFICE),
                "--headless",
                f"-env:UserInstallation=file://{profil}",
                "--convert-to",
                "pdf",
                "--outdir",
                sortie,
                str(deck),
            ],
            capture_output=True,
            check=True,
        )
        produit = Path(sortie) / (deck.stem + ".pdf")
        cible = formateur / "_alex" / produit.name
        shutil.move(str(produit), cible)
    print(f"[supports] export PDF du deck : {cible.relative_to(racine)}")
    return True


IMAGE_RELATIVE = re.compile(r"(!\[[^\]]*\]\()(?!https?:|/)([^)\s]+)")


def generer_pdf(md2pdf, source, sortie, bandeau, alt, options):
    """Le générateur résout les images depuis un dossier temporaire : on lui passe
    une copie de la source dont les chemins d'images relatifs sont rendus absolus."""
    texte = IMAGE_RELATIVE.sub(
        lambda m: m.group(1) + str((source.parent / m.group(2)).resolve()),
        source.read_text(encoding="utf-8"),
    )
    with tempfile.TemporaryDirectory() as dossier:
        copie = Path(dossier) / source.name
        copie.write_text(texte, encoding="utf-8")
        commande = [sys.executable, str(md2pdf), str(copie), "--template", "formation",
                    "--lang", "fr", "--logo", str(bandeau), "--logo-alt", alt,
                    "-o", str(sortie), *options]
        return subprocess.run(commande, capture_output=True, text=True, check=False)
