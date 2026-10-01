"""Tests de l'annonce et du plan de la partie I."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import create_presentation
from slides import SlideContext, discover_slides, load_slide_module


SLIDE_FILE = "02la_plan-partie-1.py"
ETAPES = [
    "L'accessibilité numérique, c'est quoi ?",
    "L'accessibilité numérique, c'est pour qui ?",
    "L'accessibilité numérique, quel cadre légal ?",
    "L'accessibilité numérique, pourquoi ?",
    "L'accessibilité numérique, comment s'y mettre ?",
]


def test_plan_partie_1_remplace_la_synthese_de_fin_de_partie():
    fichiers = [path.name for path in discover_slides()]

    assert fichiers[14] == SLIDE_FILE
    assert "02t_module1-points-cles.py" not in fichiers
    assert len(fichiers) == 131


def test_plan_partie_1_annonce_les_cinq_sous_parties():
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=15,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )

    slide = load_slide_module(
        Path(__file__).parent.parent / "scripts" / "slides" / SLIDE_FILE
    ).build(prs, layouts, ctx)

    assert slide.shapes.title is not None
    assert slide.shapes.title.text == "Partie I - Accessibilité et cadre légal"

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
