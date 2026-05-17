"""Tests de regression geometrique sur le deck PPTX assemble.

Verifie 4 familles de contraintes sur le PPTX final :
- Zone footer : aucun shape de contenu sous BOTTOM_CONTENT
- Chevauchements : aucun DSFR-box ne chevauche un autre (2D)
- Alt-text : images non decoratives avec description
- Police minimale : runs de contenu >= 14pt

Workflow : python3 scripts/assemble.py && pytest tests/test_deck_geometry.py -v
PRD-118.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import BOTTOM_CONTENT, MARGIN_L, CONTENT_W  # noqa: E402

NSMAP_A = "http://schemas.openxmlformats.org/drawingml/2006/main"

# ---------------------------------------------------------------------------
# Exclusions centralisees
# ---------------------------------------------------------------------------

LAYOUT_PATTERNS = {"espace réservé", "placeholder", "title 1"}

DECORATIVE_PATTERNS = {
    "decorat", "accent", "logo", "ligne", "separator", "connecteur",
}

FOOTER_EXTRA_EXCL = {"qrcode", "qr-code"}

FONT_EXTRA_EXCL = {"qrcode", "qr-code", "url-visible"}

# Seuils de regression : nombre de violations connues sur le deck actuel.
# Baisser ces seuils au fur et a mesure que les issues sont corrigees.
KNOWN_FOOTER_VIOLATIONS = 11
KNOWN_ALT_VIOLATIONS = 42
KNOWN_FONT_VIOLATIONS = 25

MIN_FONT_PT = 14
EMU_TOLERANCE = 0.01  # pouces, marge conversion EMU


def _is_excluded(name, patterns):
    """Vrai si le nom du shape matche un des patterns d'exclusion."""
    if not name:
        return False
    n = name.lower()
    return any(p in n for p in patterns)


def _shape_rect(shape):
    """Retourne (top, left, height, width) en pouces."""
    return (
        shape.top / 914400 if shape.top else 0,
        shape.left / 914400 if shape.left else 0,
        shape.height / 914400 if shape.height else 0,
        shape.width / 914400 if shape.width else 0,
    )


def _rects_overlap_2d(t1, l1, h1, w1, t2, l2, h2, w2, tol=0.02):
    """Vrai si deux rectangles se chevauchent en 2D."""
    v_overlap = (t1 + h1 > t2 + tol) and (t2 + h2 > t1 + tol)
    h_overlap = (l1 + w1 > l2 + tol) and (l2 + w2 > l1 + tol)
    return v_overlap and h_overlap


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestFooterZone:
    """Shapes de contenu ne doivent pas depasser BOTTOM_CONTENT (6.80")."""

    def test_aucun_shape_sous_bottom_content(self, deck):
        excl = LAYOUT_PATTERNS | DECORATIVE_PATTERNS | FOOTER_EXTRA_EXCL
        violations = []
        for i, slide in enumerate(deck.slides, 1):
            for shape in slide.shapes:
                if _is_excluded(shape.name, excl):
                    continue
                top, _, height, _ = _shape_rect(shape)
                bottom = top + height
                if bottom > BOTTOM_CONTENT + EMU_TOLERANCE:
                    violations.append(
                        f"Slide {i}: \"{shape.name}\" "
                        f"bottom={bottom:.3f}\" > {BOTTOM_CONTENT}\""
                    )
        assert len(violations) <= KNOWN_FOOTER_VIOLATIONS, (
            f"{len(violations)} violations footer (seuil={KNOWN_FOOTER_VIOLATIONS}). "
            f"Nouvelles violations :\n" + "\n".join(violations)
        )


class TestChevauchements:
    """Aucun DSFR-box ne doit chevaucher un autre DSFR-box en 2D."""

    def test_aucun_chevauchement_dsfr_box(self, deck):
        violations = []
        for i, slide in enumerate(deck.slides, 1):
            boxes = []
            for shape in slide.shapes:
                if shape.name == "DSFR-box":
                    boxes.append(_shape_rect(shape))
            for a in range(len(boxes)):
                for b in range(a + 1, len(boxes)):
                    t1, l1, h1, w1 = boxes[a]
                    t2, l2, h2, w2 = boxes[b]
                    if _rects_overlap_2d(t1, l1, h1, w1, t2, l2, h2, w2):
                        violations.append(
                            f"Slide {i}: box@({t1:.2f}\",{l1:.2f}\") "
                            f"vs box@({t2:.2f}\",{l2:.2f}\")"
                        )
        assert not violations, (
            f"{len(violations)} chevauchements DSFR-box :\n"
            + "\n".join(violations)
        )


class TestAltText:
    """Images non decoratives doivent avoir un alt-text."""

    def test_images_non_decoratives_ont_alt(self, deck):
        violations = []
        for i, slide in enumerate(deck.slides, 1):
            for shape in slide.shapes:
                if shape.shape_type != 13:  # MSO_SHAPE_TYPE.PICTURE
                    continue
                if _is_excluded(shape.name, DECORATIVE_PATTERNS):
                    continue
                cNvPr = shape._element.find(f".//{{{NSMAP_A}}}cNvPr")
                descr = cNvPr.get("descr", "") if cNvPr is not None else ""
                if not descr:
                    violations.append(
                        f"Slide {i}: image \"{shape.name}\" sans alt-text"
                    )
        assert len(violations) <= KNOWN_ALT_VIOLATIONS, (
            f"{len(violations)} images sans alt (seuil={KNOWN_ALT_VIOLATIONS}). "
            f"Nouvelles violations :\n" + "\n".join(violations)
        )


class TestPoliceMinimale:
    """Runs de contenu doivent avoir une taille >= 14pt."""

    def test_taille_police_minimum(self, deck):
        excl = LAYOUT_PATTERNS | DECORATIVE_PATTERNS | FONT_EXTRA_EXCL
        violations = []
        for i, slide in enumerate(deck.slides, 1):
            for shape in slide.shapes:
                if _is_excluded(shape.name, excl):
                    continue
                if not hasattr(shape, "text_frame"):
                    continue
                try:
                    tf = shape.text_frame
                except Exception:
                    continue
                for para in tf.paragraphs:
                    for run in para.runs:
                        if run.font.size is not None:
                            size_pt = run.font.size.pt
                            if size_pt < MIN_FONT_PT:
                                txt = run.text[:30].replace("\n", " ")
                                violations.append(
                                    f"Slide {i}: \"{shape.name}\" "
                                    f"\"{txt}\" = {size_pt}pt"
                                )
        assert len(violations) <= KNOWN_FONT_VIOLATIONS, (
            f"{len(violations)} runs < {MIN_FONT_PT}pt "
            f"(seuil={KNOWN_FONT_VIOLATIONS}). "
            f"Nouvelles violations :\n" + "\n".join(violations)
        )
