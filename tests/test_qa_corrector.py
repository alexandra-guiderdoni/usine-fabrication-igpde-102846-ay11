"""Tests du correcteur conservateur PRD-119 Phase 3."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from qa_corrector import build_corrections  # noqa: E402


def _write_source(project_root: Path, content: str) -> Path:
    source_path = project_root / "scripts/slides/99_test.py"
    source_path.parent.mkdir(parents=True)
    source_path.write_text(content, encoding="utf-8")
    return source_path


def _report(*violations):
    return {"violations": list(violations)}


def _accent_violation(found="methode", expected="méthode", call_lineno=4):
    return {
        "type": "accent_fr",
        "status": "new",
        "slide_index": 1,
        "shape_name": "DSFR-callout-body",
        "fingerprint": "accent-test",
        "message": f"{found} sans accent",
        "found": found,
        "expected": expected,
        "source": {
            "source_file": "scripts/slides/99_test.py",
            "call_lineno": call_lineno,
            "component_type": "add_callout",
        },
    }


def test_correcteur_propose_un_patch_accent_univoque_sans_modifier(tmp_path):
    source_path = _write_source(
        tmp_path,
        "\n".join([
            "def build(prs, layouts, ctx):",
            "    slide = None",
            "    add_callout(slide, \"Ma methode\", [\"Texte\"], top=2.3)",
            "",
        ]),
    )

    result = build_corrections(tmp_path, _report(_accent_violation(call_lineno=3)))

    assert result["summary"] == {
        "new_violations": 1,
        "patch_safe": 1,
        "applied": 0,
        "skipped": 0,
    }
    action = result["actions"][0]
    assert action["decision"] == "PATCH_SAFE"
    assert action["line"] == 3
    assert action["old"] == '    add_callout(slide, "Ma methode", ["Texte"], top=2.3)'
    assert action["new"] == '    add_callout(slide, "Ma méthode", ["Texte"], top=2.3)'
    assert "methode" in source_path.read_text(encoding="utf-8")


def test_correcteur_applique_un_patch_accent_univoque(tmp_path):
    source_path = _write_source(
        tmp_path,
        "\n".join([
            "def build(prs, layouts, ctx):",
            "    slide = None",
            "    add_callout(slide, \"Regle simple\", [\"Texte\"], top=2.3)",
            "",
        ]),
    )

    result = build_corrections(
        tmp_path,
        _report(_accent_violation(found="Regle", expected="règle", call_lineno=3)),
        apply=True,
    )

    assert result["summary"]["patch_safe"] == 1
    assert result["summary"]["applied"] == 1
    assert '    add_callout(slide, "Règle simple", ["Texte"], top=2.3)' in (
        source_path.read_text(encoding="utf-8")
    )


def test_correcteur_refuse_un_accent_ambigu(tmp_path):
    _write_source(
        tmp_path,
        "\n".join([
            "def build(prs, layouts, ctx):",
            "    texte = \"methode ou methode\"",
            "    add_callout(slide, texte, [\"Texte\"], top=2.3)",
            "",
        ]),
    )

    result = build_corrections(tmp_path, _report(_accent_violation(call_lineno=3)))

    assert result["summary"]["patch_safe"] == 0
    assert result["summary"]["skipped"] == 1
    assert result["actions"][0]["decision"] == "SKIP_AMBIGUOUS"


def test_correcteur_ne_modifie_pas_identifiant_ou_commentaire(tmp_path):
    _write_source(
        tmp_path,
        "\n".join([
            "def build(prs, layouts, ctx):",
            "    methode = \"déjà accentué\"  # methode de test",
            "    add_callout(slide, methode, [\"Texte\"], top=2.3)",
            "",
        ]),
    )

    result = build_corrections(tmp_path, _report(_accent_violation(call_lineno=3)))

    assert result["summary"]["patch_safe"] == 0
    assert result["summary"]["skipped"] == 1
    assert result["actions"][0]["decision"] == "SKIP_AMBIGUOUS"


def test_correcteur_skippe_layout_en_v1(tmp_path):
    violation = {
        "type": "footer",
        "status": "new",
        "slide_index": 12,
        "shape_name": "DSFR-box",
        "fingerprint": "footer-test",
        "message": "bottom > limit",
        "source": {
            "source_file": "scripts/slides/12_test.py",
            "call_lineno": 42,
            "component_type": "add_card",
        },
    }

    result = build_corrections(tmp_path, _report(violation))

    assert result["summary"] == {
        "new_violations": 1,
        "patch_safe": 0,
        "applied": 0,
        "skipped": 1,
    }
    assert result["actions"][0]["decision"] == "SKIP_LAYOUT"


def test_correcteur_ignore_les_violations_deja_connues(tmp_path):
    violation = _accent_violation()
    violation["status"] = "known"

    result = build_corrections(tmp_path, _report(violation))

    assert result["summary"] == {
        "new_violations": 0,
        "patch_safe": 0,
        "applied": 0,
        "skipped": 0,
    }
    assert result["actions"] == []
