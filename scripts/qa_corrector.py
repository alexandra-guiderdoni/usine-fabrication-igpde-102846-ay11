"""Correcteur conservateur PRD-119 pour les rapports QA PPTX.

Par défaut, le script ne modifie rien : il lit `.qa/qa-report.json` et écrit
des actions proposées. Seules les violations `accent_fr` peuvent être appliquées
avec `--apply`, et uniquement si la localisation source est univoque.
"""

from __future__ import annotations

import argparse
import io
import json
import re
import tokenize
from pathlib import Path
from typing import Any

DEFAULT_REPORT = Path(".qa/qa-report.json")
DEFAULT_OUTPUT_JSON = Path(".qa/qa-corrections.json")
DEFAULT_OUTPUT_MD = Path(".qa/qa-corrections.md")
WINDOW_RADIUS = 8


def load_report(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_corrections(project_root: Path, report: dict[str, Any], apply: bool = False) -> dict[str, Any]:
    """Construit les actions correctives pour les violations nouvelles."""
    project_root = project_root.resolve()
    actions = []
    new_violations = [
        violation for violation in report.get("violations", [])
        if violation.get("status") == "new"
    ]

    for violation in new_violations:
        if violation.get("type") == "accent_fr":
            actions.append(_handle_accent(project_root, violation, apply=apply))
        else:
            actions.append(_skip_non_accent(violation))

    summary = {
        "new_violations": len(new_violations),
        "patch_safe": sum(1 for action in actions if action["decision"] == "PATCH_SAFE"),
        "applied": sum(1 for action in actions if action.get("applied")),
        "skipped": sum(1 for action in actions if action["decision"].startswith("SKIP")),
    }
    return {
        "version": 1,
        "mode": "apply" if apply else "dry-run",
        "summary": summary,
        "actions": actions,
    }


def write_outputs(result: dict[str, Any], output_json: Path, output_md: Path) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    output_md.write_text(_markdown_report(result), encoding="utf-8")


def _handle_accent(project_root: Path, violation: dict[str, Any], apply: bool) -> dict[str, Any]:
    source = violation.get("source") or {}
    source_file = source.get("source_file")
    call_lineno = source.get("call_lineno")
    found = violation.get("found")
    expected = violation.get("expected")

    base = _base_action(violation)
    base.update({
        "action": "replace_accent",
        "found": found,
        "expected": expected,
    })

    if not source_file or not call_lineno:
        return _skip(base, "SKIP_NO_SOURCE", "source map absente ou incomplète")
    if not found or not expected:
        return _skip(base, "SKIP_BAD_DATA", "forme trouvée ou attendue absente du rapport")

    path = (project_root / source_file).resolve()
    try:
        path.relative_to(project_root)
    except ValueError:
        return _skip(base, "SKIP_OUTSIDE_PROJECT", f"chemin hors projet : {source_file}")
    if not path.exists():
        return _skip(base, "SKIP_MISSING_FILE", f"fichier introuvable : {source_file}")

    try:
        call_lineno_int = int(call_lineno)
    except (TypeError, ValueError):
        return _skip(base, "SKIP_BAD_SOURCE", f"ligne source invalide : {call_lineno}")

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    candidate = _find_unique_candidate(lines, call_lineno_int, str(found))
    if candidate is None:
        return _skip(base, "SKIP_AMBIGUOUS", "occurrence absente ou multiple dans la fenêtre source")

    line_index, start, end = candidate
    replacement = _match_case(str(found), str(expected))
    old_line = lines[line_index]
    new_line = old_line[:start] + replacement + old_line[end:]
    base.update({
        "decision": "PATCH_SAFE",
        "reason": "occurrence unique dans la fenêtre source",
        "source_file": source_file,
        "line": line_index + 1,
        "old": old_line.rstrip("\n"),
        "new": new_line.rstrip("\n"),
        "applied": False,
    })

    if apply:
        lines[line_index] = new_line
        path.write_text("".join(lines), encoding="utf-8")
        base["applied"] = True

    return base


def _find_unique_candidate(lines: list[str], call_lineno: int, found: str) -> tuple[int, int, int] | None:
    start_line = max(1, call_lineno - WINDOW_RADIUS)
    end_line = min(len(lines), call_lineno + WINDOW_RADIUS)
    pattern = re.compile(rf"\b{re.escape(found)}\b")
    candidates = []

    for line_no in range(start_line, end_line + 1):
        line = lines[line_no - 1]
        if _is_url_context(line):
            continue
        for match in pattern.finditer(line):
            if not _is_in_python_string(line, match.start(), match.end()):
                continue
            candidates.append((line_no - 1, match.start(), match.end()))

    if len(candidates) != 1:
        return None
    return candidates[0]


def _skip_non_accent(violation: dict[str, Any]) -> dict[str, Any]:
    action = _base_action(violation)
    violation_type = violation.get("type")
    if violation_type in {"footer", "overlap"}:
        return _skip(action, "SKIP_LAYOUT", "correction layout automatique interdite en v1")
    if violation_type == "alt_text":
        return _skip(action, "SKIP_ALT_TEXT", "alt-text à rédiger ou valider humainement")
    if violation_type == "font_size":
        return _skip(action, "SKIP_FONT_SIZE", "changement typographique à valider visuellement")
    return _skip(action, "SKIP_UNSUPPORTED", f"type non supporté : {violation_type}")


def _base_action(violation: dict[str, Any]) -> dict[str, Any]:
    source = violation.get("source") or {}
    return {
        "violation_type": violation.get("type"),
        "slide_index": violation.get("slide_index"),
        "shape_name": violation.get("shape_name"),
        "fingerprint": violation.get("fingerprint"),
        "message": violation.get("message"),
        "source": source,
    }


def _skip(action: dict[str, Any], decision: str, reason: str) -> dict[str, Any]:
    action.update({
        "decision": decision,
        "reason": reason,
        "applied": False,
    })
    return action


def _match_case(found: str, expected: str) -> str:
    if found.isupper():
        return expected.upper()
    if found[:1].isupper():
        return expected[:1].upper() + expected[1:]
    return expected


def _is_url_context(line: str) -> bool:
    lowered = line.lower()
    return "http://" in lowered or "https://" in lowered or "www." in lowered or "@" in lowered


def _is_in_python_string(line: str, start: int, end: int) -> bool:
    try:
        tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        for token in tokens:
            if token.type != tokenize.STRING:
                continue
            token_start = token.start[1]
            token_end = token.end[1]
            if token_start <= start and end <= token_end:
                return True
    except tokenize.TokenError:
        return False
    return False


def _markdown_report(result: dict[str, Any]) -> str:
    summary = result["summary"]
    lines = [
        "# Rapport correcteur QA PPTX",
        "",
        f"- Mode : `{result['mode']}`",
        f"- Violations nouvelles : {summary['new_violations']}",
        f"- Patchs sûrs : {summary['patch_safe']}",
        f"- Patchs appliqués : {summary['applied']}",
        f"- Skips : {summary['skipped']}",
        "",
        "## Actions",
        "",
    ]
    if not result["actions"]:
        lines.append("Aucune violation nouvelle à traiter.")
    for action in result["actions"]:
        source = action.get("source") or {}
        location = source.get("source_file", "source inconnue")
        if source.get("call_lineno"):
            location = f"{location}:{source['call_lineno']}"
        lines.extend([
            f"- `{action['decision']}` slide {action.get('slide_index')} - {action.get('violation_type')} - {location}",
            f"  - Raison : {action.get('reason')}",
        ])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--apply", action="store_true", help="Applique les patchs d'accents sûrs")
    args = parser.parse_args()

    project_root = Path.cwd()
    report_path = args.report if args.report.is_absolute() else project_root / args.report
    result = build_corrections(project_root, load_report(report_path), apply=args.apply)
    output_json = args.output_json if args.output_json.is_absolute() else project_root / args.output_json
    output_md = args.output_md if args.output_md.is_absolute() else project_root / args.output_md
    write_outputs(result, output_json, output_md)

    summary = result["summary"]
    print(
        "[QA-CORRECTOR] "
        f"mode={result['mode']} new={summary['new_violations']} "
        f"safe={summary['patch_safe']} applied={summary['applied']} "
        f"skipped={summary['skipped']}"
    )


if __name__ == "__main__":
    main()
