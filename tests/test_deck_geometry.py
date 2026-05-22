"""Tests de régression géométrique sur le deck PPTX assemblé.

Vérifie 5 familles de contraintes sur le PPTX final :
- Zone footer : aucun shape de contenu sous BOTTOM_CONTENT
- Chevauchements : aucun DSFR-box ne chevauche un autre (2D)
- Alt-text : images non décoratives avec description
- Police minimale : runs de contenu >= 14pt
- Accents français : formes fréquentes non accentuées signalées

Workflow : python3 scripts/assemble.py && pytest tests/test_deck_geometry.py -v
PRD-118 + PRD-119 Phase 1.
"""

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from qa_geometry import (  # noqa: E402
    KNOWN_ALT_VIOLATIONS,
    KNOWN_FONT_VIOLATIONS,
    KNOWN_FOOTER_VIOLATIONS,
    MIN_FONT_PT,
    find_accent_issues,
    write_report,
)


@pytest.fixture(scope="session")
def qa_report(deck):
    """Écrit le rapport JSON PRD-119 et le partage entre les tests."""
    return write_report(deck, PROJECT_ROOT)


def _violations_by_type(report, violation_type):
    return [
        violation for violation in report["violations"]
        if violation["type"] == violation_type
    ]


def _new_violations(report, violation_type):
    return [
        violation for violation in _violations_by_type(report, violation_type)
        if violation["status"] == "new"
    ]


def _format_messages(violations):
    return "\n".join(violation["message"] for violation in violations)


def _assert_no_new(report, violation_type):
    violations = _new_violations(report, violation_type)
    assert not violations, (
        f"{len(violations)} nouvelles violations {violation_type} :\n"
        + _format_messages(violations)
    )


class TestFooterZone:
    """Shapes de contenu ne doivent pas dépasser BOTTOM_CONTENT (6.80")."""

    def test_aucun_shape_sous_bottom_content(self, qa_report):
        violations = _violations_by_type(qa_report, "footer")
        _assert_no_new(qa_report, "footer")
        assert len(violations) <= KNOWN_FOOTER_VIOLATIONS, (
            f"{len(violations)} violations footer "
            f"(seuil={KNOWN_FOOTER_VIOLATIONS}).\n"
            + _format_messages(violations)
        )


class TestChevauchements:
    """Aucun DSFR-box ne doit chevaucher un autre DSFR-box en 2D."""

    def test_aucun_chevauchement_dsfr_box(self, qa_report):
        violations = _violations_by_type(qa_report, "overlap")
        _assert_no_new(qa_report, "overlap")
        assert not violations, (
            f"{len(violations)} chevauchements DSFR-box :\n"
            + _format_messages(violations)
        )


class TestAltText:
    """Images non décoratives doivent avoir un alt-text."""

    def test_images_non_decoratives_ont_alt(self, qa_report):
        violations = _violations_by_type(qa_report, "alt_text")
        _assert_no_new(qa_report, "alt_text")
        assert len(violations) <= KNOWN_ALT_VIOLATIONS, (
            f"{len(violations)} images sans alt "
            f"(seuil={KNOWN_ALT_VIOLATIONS}).\n"
            + _format_messages(violations)
        )


class TestPoliceMinimale:
    """Runs de contenu doivent avoir une taille >= 14pt."""

    def test_taille_police_minimum(self, qa_report):
        violations = _violations_by_type(qa_report, "font_size")
        _assert_no_new(qa_report, "font_size")
        assert len(violations) <= KNOWN_FONT_VIOLATIONS, (
            f"{len(violations)} runs < {MIN_FONT_PT}pt "
            f"(seuil={KNOWN_FONT_VIOLATIONS}).\n"
            + _format_messages(violations)
        )


class TestAccentsFrancais:
    """Les formes françaises fréquentes doivent être accentuées."""

    def test_aucune_forme_non_accentuee_nouvelle(self, qa_report):
        _assert_no_new(qa_report, "accent_fr")

    def test_detecte_formes_non_accentuees_sur_fixture(self):
        texte = (
            "methode accessibilite securite conformite critere regle "
            "donnees ecran numerique video"
        )
        issues = find_accent_issues(texte)
        formes = {issue["found"].lower() for issue in issues}
        assert formes == {
            "accessibilite",
            "conformite",
            "critere",
            "donnees",
            "ecran",
            "methode",
            "numerique",
            "regle",
            "securite",
            "video",
        }
