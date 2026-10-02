"""Contrats d'alignement des mémos et des notes formateur du TP Sami."""

from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from config import load_formation_config  # noqa: E402
from exercice_sami_matrice import load_sami_matrix  # noqa: E402


PACK = PROJECT_ROOT / load_formation_config()["livrables"]
MEMO_PATHS = (
    PROJECT_ROOT / "fiche-pratique" / "memo-word.md",
    PROJECT_ROOT / "fiche-pratique" / "memo-libreoffice-writer.md",
)
NOTES_PATH = (
    PACK / "Formateur" / "_alex" / "formation-102846-octobre-2026-bureautique.md"
)
LEGACY_CHECKLIST_PATH = PACK / "Formateur" / "_alex" / "checklist-bureautique.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _normalized_text(path: Path) -> str:
    return re.sub(r"\s+", " ", _read(path))


def _practiced_control_ids() -> list[str]:
    return [
        control["id"]
        for control in load_sami_matrix()["controles"]
        if control["niveau"] in {"P", "C"}
    ]


def test_les_memos_referencent_les_controles_pratiques_dans_l_ordre():
    expected_ids = _practiced_control_ids()

    for memo_path in MEMO_PATHS:
        content = _read(memo_path)
        positions = [content.index(control_id) for control_id in expected_ids]

        assert positions == sorted(positions), memo_path
        assert all(content.count(control_id) == 1 for control_id in expected_ids)
        assert not re.search(r"\bS-0[1-5]\b", content)


def test_les_notes_reprennent_les_sept_blocs_et_les_90_minutes():
    matrix = load_sami_matrix()
    notes = _read(NOTES_PATH)
    actual = [
        (title, int(duration))
        for title, duration in re.findall(
            r"^## (.+) - (\d+) minutes$", notes, flags=re.MULTILINE
        )
    ]
    expected = [
        (block["titre"], block["duree_minutes"]) for block in matrix["sequence"]
    ]

    assert actual == expected
    assert sum(duration for _, duration in actual) == 90


def test_les_notes_couvrent_tous_les_controles_sans_les_reclasser():
    matrix = load_sami_matrix()
    notes = _read(NOTES_PATH)

    for control in matrix["controles"]:
        assert control["id"] in notes
    for control_id in ("S-01", "S-02", "S-03", "S-04", "S-05"):
        assert f"{control_id} - signalé" in notes


def test_les_notes_decrivent_la_distribution_et_les_deux_formateurs():
    notes = _normalized_text(NOTES_PATH)

    expected_phrases = (
        "Word bureau sous Windows",
        "Writer sous Windows",
        "tp-doc-aide-correction.docx",
        "tp-doc-inaccessible.docx",
        "checklist-accessibilite-bureautique.docx",
        "cartes-criteres-wcag-2-2-a-imprimer.pdf",
        "tp-doc-accessible.docx",
        "Formateur 1",
        "Formateur 2",
        "synthèse commune",
        "remis seulement à la fin",
    )
    for phrase in expected_phrases:
        assert phrase in notes


def test_les_memos_couvrent_verification_export_et_controle_humain():
    word = _read(MEMO_PATHS[0])
    writer = _normalized_text(MEMO_PATHS[1])

    for content in (word, writer):
        assert "C-01" in content
        assert "P-20" in content
        assert "C-02" in content
        assert "PAC" in content
        assert "Acrobat Pro" in content
        assert "checklist humaine" in content
    assert "selon la version installée" in writer


def test_les_sources_actives_ecartent_les_anciens_contrats():
    active_sources = (*MEMO_PATHS, NOTES_PATH, LEGACY_CHECKLIST_PATH)
    forbidden_patterns = (
        "21 " + "critères",
        "25 " + "min",
        "25 " + "minutes",
        "30 min",
        "30 minutes",
        "sans " + "checklist",
        "diagnostic sans " + "checklist",
        "sans " + "filet",
        "rapport " + "trimestriel",
        "erreurs cachées",
        "#767676",
        "4,48",
        "quiz " + "final",
    )

    for source_path in active_sources:
        content = _read(source_path).casefold()
        for pattern in forbidden_patterns:
            assert pattern.casefold() not in content, (source_path, pattern)


def test_les_memos_conservent_les_seuils_de_contraste_valides():
    for memo_path in MEMO_PATHS:
        content = _read(memo_path)
        assert "4,5:1" in content
        assert "3:1" in content
