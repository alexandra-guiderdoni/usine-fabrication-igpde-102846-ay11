"""Tests de cohérence entre la grille d'audit et le deck courant."""

from __future__ import annotations

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from generate_grille_audit import EXERCICE_PAGES  # noqa: E402
from slides import discover_slides  # noqa: E402


def test_les_pages_d_exercice_pointent_vers_les_slides_du_deck_courant():
    positions = {
        path.name: index for index, path in enumerate(discover_slides(), start=1)
    }
    module_bounds = {
        "ec01-images": ("29_check01_alt-types.py", "31_check01_alt-exemples.py"),
        "ec02-page-title": ("32_check02_titre-page.py",),
        "ec03-headings": (
            "33_check03_titres-hierarchie.py",
            "34_check03_titres-outils.py",
        ),
        "ec04-contrast": (
            "35_check04_contraste-principe.py",
            "36_check04_contraste-outils.py",
        ),
        "ec05-skiplinks": ("37_check05_lien-evitement.py",),
        "ec06-keyboard-focus": (
            "38_navigation-clavier-ouverture.py",
            "41_mission-clavier.py",
        ),
        "ec07-language": ("42_check07_langue.py",),
        "ec08-zoom": ("43_check08_zoom.py",),
        "ec09-captions": (
            "44_check09_sous-titres-principe.py",
            "45_check09_sous-titres-auto.py",
        ),
        "ec10-transcript": ("46_check10_transcriptions.py",),
        "ec11-audio-description": ("47_check11_audiodescription.py",),
        "ec12-form-labels": (
            "48_check12_etiquettes-principe.py",
            "50_check12_etiquettes-groupes.py",
        ),
        "ec13-required-errors": ("51_check13_champs-obligatoires.py",),
    }
    expected = {}
    for page_id, bounds in module_bounds.items():
        first = positions[bounds[0]]
        last = positions[bounds[-1]]
        expected[page_id] = str(first) if first == last else f"{first}-{last}"

    assert {page["id"]: page["slides"] for page in EXERCICE_PAGES} == expected
