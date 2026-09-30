"""Tests de l'annonce et du plan de la partie II."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import create_presentation
from slides import SlideContext, discover_slides, load_slide_module


SLIDE_FILE = "03_chapitre-word.py"
ETAPES = [
    "Structurer le document",
    "Rendre les couleurs accessibles",
    "Décrire les contenus visuels",
    "Améliorer la langue et la lisibilité",
    "Vérifier et finaliser",
]


def test_plan_partie_2_occupe_la_slide_54_sans_changer_le_nombre_de_slides():
    fichiers = [chemin.name for chemin in discover_slides()]

    assert fichiers[53] == SLIDE_FILE
    assert len(fichiers) == 138


def test_plan_partie_2_annonce_les_cinq_sous_parties():
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=54,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )

    slide = load_slide_module(
        Path(__file__).parent.parent / "scripts" / "slides" / SLIDE_FILE
    ).build(prs, layouts, ctx)

    assert slide.shapes.title is not None
    assert slide.shapes.title.text == "Partie II - Documents bureautiques accessibles"

    etapes = [
        shape.text
        for shape in slide.shapes
        if shape.name.startswith("DSFR-stepper-texte-")
    ]
    numeros = [
        shape.text
        for shape in slide.shapes
        if shape.name.startswith("DSFR-stepper-pastille-")
    ]
    assert etapes == ETAPES
    assert numeros == ["1", "2", "3", "4", "5"]
    assert slide.notes_slide.notes_text_frame.text.strip()
