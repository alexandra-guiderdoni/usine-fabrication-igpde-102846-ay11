"""Tests de l'orchestrateur QA PPTX PRD-119 Phase 4."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from qa_pptx import decide_next_action, new_fingerprint_hash  # noqa: E402


def _report(new_count, violations=None):
    return {
        "summary": {"new": new_count},
        "violations": violations or [],
    }


def _corrections(patch_safe=0, skipped=0):
    return {
        "summary": {
            "patch_safe": patch_safe,
            "applied": 0,
            "skipped": skipped,
        }
    }


def test_hash_fingerprints_nouveaux_stable_malgre_ordre():
    first = _report(
        2,
        [
            {"status": "new", "fingerprint": "b"},
            {"status": "known", "fingerprint": "z"},
            {"status": "new", "fingerprint": "a"},
        ],
    )
    second = _report(
        2,
        [
            {"status": "new", "fingerprint": "a"},
            {"status": "new", "fingerprint": "b"},
            {"status": "known", "fingerprint": "z"},
        ],
    )

    assert new_fingerprint_hash(first) == new_fingerprint_hash(second)


def test_decision_converged_si_aucune_violation_nouvelle():
    assert decide_next_action(_report(0), _corrections(), apply_accents=False) == "CONVERGED"


def test_decision_dry_run_stoppe_si_nouvelles_violations():
    assert (
        decide_next_action(_report(2), _corrections(patch_safe=1), apply_accents=False)
        == "DRY_RUN_PENDING"
    )


def test_decision_apply_uniquement_si_patch_accent_sur():
    assert (
        decide_next_action(_report(1), _corrections(patch_safe=1), apply_accents=True)
        == "APPLY_PATCHES"
    )


def test_decision_skippe_si_aucun_patch_sur():
    assert (
        decide_next_action(_report(1), _corrections(patch_safe=0, skipped=1), apply_accents=True)
        == "SKIPPED_UNSAFE"
    )
