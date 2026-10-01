"""Tests de l'annonce et du plan de la partie IV."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import create_presentation
from slides import SlideContext, discover_slides, load_slide_module


SLIDE_FILE = "53_chapitre-reseaux-sociaux.py"
ETAPES = [
    "Comprendre les enjeux des réseaux sociaux",
    "Décrire les images et choisir les plateformes",
    "Rendre les textes et les caractères lisibles",
    "Représenter les publics et écrire clairement",
    "Vérifier avant de publier",
]


def test_plan_partie_4_occupe_la_slide_110_apres_la_mission_web():
    fichiers = [chemin.name for chemin in discover_slides()]

    assert fichiers[108] == "52_mission-13-checks.py"
    assert fichiers[109] == SLIDE_FILE
    assert len(fichiers) == 133


def test_plan_partie_4_annonce_les_cinq_sous_parties():
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=110,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )

    slide = load_slide_module(
        Path(__file__).parent.parent / "scripts" / "slides" / SLIDE_FILE
    ).build(prs, layouts, ctx)

    assert slide.shapes.title is not None
    assert slide.shapes.title.text == ("Partie IV - Réseaux sociaux accessibles - TP")

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
