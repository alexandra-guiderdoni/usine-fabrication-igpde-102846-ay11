"""Tests de la slide 7 - organisation des activités."""

import sys
from pathlib import Path

from pptx.util import Inches

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import create_presentation
from slides import SlideContext, load_slide_module


SLIDE_PATH = (
    Path(__file__).parent.parent / "scripts" / "slides" / "02e_regroupement-binomes.py"
)


def test_slide_7_cartes_alignees_sur_leur_contenu():
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=7,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )

    slide = load_slide_module(SLIDE_PATH).build(prs, layouts, ctx)

    cartes = [
        shape
        for shape in slide.shapes
        if shape.name == "DSFR-box" and shape.width < Inches(6)
    ]
    assert len(cartes) == 2
    assert all(shape.height == Inches(2.45) for shape in cartes)

    encadre_final = next(
        shape
        for shape in slide.shapes
        if shape.name == "DSFR-box" and shape.width >= Inches(12)
    )
    bas_cartes = cartes[0].top + cartes[0].height
    assert encadre_final.top - bas_cartes == Inches(0.45)
