"""Tests des slides 9 à 14 - série des idées reçues."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import create_presentation
from slides import SlideContext, load_slide_module


SLIDES_DIR = Path(__file__).parent.parent / "scripts" / "slides"
SLIDE_FILES = [
    "02g_idee-recue-1.py",
    "02h_idee-recue-2.py",
    "02i_idee-recue-3.py",
    "02j_idee-recue-4.py",
    "02k_idee-recue-5.py",
    "02l_idee-recue-6.py",
]


@pytest.mark.parametrize("filename", SLIDE_FILES)
def test_decryptage_des_idees_recues_est_aere(filename):
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=9,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )

    slide = load_slide_module(SLIDES_DIR / filename).build(prs, layouts, ctx)
    decryptage = next(
        shape for shape in slide.shapes if shape.name == "DSFR-callout-body"
    )

    assert decryptage.text_frame.paragraphs
    assert all(
        paragraph.line_spacing == 1.30 for paragraph in decryptage.text_frame.paragraphs
    )
