"""Tests de l'annonce et du plan de la partie III."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import create_presentation
from slides import SlideContext, discover_slides, load_slide_module


SLIDE_FILE = "28_chapitre-easy-checks.py"
ETAPES = [
    "Repérer les erreurs fréquentes",
    "Vérifier les images et les titres",
    "Contrôler les contrastes, les liens et le clavier",
    "Tester la langue, le zoom et les médias",
    "Examiner les formulaires et réaliser un audit rapide",
]
SLIDES_RETIREES = {
    "23_quiz-final.py",
    "24_faites-le-point.py",
    "24b_faites-le-point-reponses.py",
    "25_demain-9h.py",
    "27_revenez-7-jours.py",
    "23b_quiz-final-reponses.py",
}


def test_les_six_slides_demandees_sont_retirees_du_deck():
    fichiers = {chemin.name for chemin in discover_slides()}

    assert fichiers.isdisjoint(SLIDES_RETIREES)


def test_plan_partie_3_occupe_la_slide_79_dans_le_deck_complet():
    fichiers = [chemin.name for chemin in discover_slides()]

    assert fichiers[78] == SLIDE_FILE
    assert len(fichiers) == 131


def test_plan_partie_3_annonce_les_cinq_sous_parties():
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=79,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )

    slide = load_slide_module(
        Path(__file__).parent.parent / "scripts" / "slides" / SLIDE_FILE
    ).build(prs, layouts, ctx)

    assert slide.shapes.title is not None
    assert slide.shapes.title.text == "Partie III - Web accessible - TP"

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
