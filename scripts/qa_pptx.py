"""Orchestrateur PRD-119 pour la QA PPTX géométrique et textuelle.

Le script travaille sur une copie `.qa/formation-test-qa.pptx`, produit un
rapport structuré, lance le correcteur conservateur et reboucle uniquement si
des patchs d'accents sûrs sont explicitement appliqués.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import qa_corrector

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DECK = Path(".qa/formation-test-qa.pptx")
DEFAULT_RUN_JSON = Path(".qa/qa-pptx-run.json")
DEFAULT_RUN_MD = Path(".qa/qa-pptx-report.md")
QA_REPORT_PATH = Path(".qa/qa-report.json")
QA_CORRECTIONS_JSON = Path(".qa/qa-corrections.json")
QA_CORRECTIONS_MD = Path(".qa/qa-corrections.md")


@dataclass
class CommandResult:
    name: str
    command: list[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "command": self.command,
            "returncode": self.returncode,
            "stdout_tail": _tail(self.stdout),
            "stderr_tail": _tail(self.stderr),
        }


@dataclass
class Iteration:
    index: int
    report_summary: dict[str, Any]
    fingerprint_hash: str
    corrections_summary: dict[str, Any]
    decision: str
    commands: list[CommandResult] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "report_summary": self.report_summary,
            "fingerprint_hash": self.fingerprint_hash,
            "corrections_summary": self.corrections_summary,
            "decision": self.decision,
            "commands": [command.to_dict() for command in self.commands],
        }


def run_loop(
    project_root: Path = PROJECT_ROOT,
    deck_path: Path = DEFAULT_DECK,
    max_iterations: int = 5,
    apply_accents: bool = False,
    report_json: Path = DEFAULT_RUN_JSON,
    report_md: Path = DEFAULT_RUN_MD,
) -> dict[str, Any]:
    """Exécute la boucle QA et écrit les rapports finaux."""
    project_root = project_root.resolve()
    deck_path = _resolve(project_root, deck_path)
    report_json = _resolve(project_root, report_json)
    report_md = _resolve(project_root, report_md)
    deck_path.parent.mkdir(parents=True, exist_ok=True)

    seen_hashes: set[str] = set()
    iterations: list[Iteration] = []
    status = "MAX_ITERATIONS"
    best_new: int | None = None
    stale_iterations = 0
    pending_snapshots: dict[Path, str] = {}

    for index in range(1, max_iterations + 1):
        commands: list[CommandResult] = []
        commands.append(_assemble(project_root, deck_path))
        if not commands[-1].ok:
            status = "ASSEMBLE_FAILED"
            iterations.append(_failed_iteration(index, commands, status))
            break

        geometry = _run_geometry_tests(project_root, deck_path)
        commands.append(geometry)

        qa_report_path = project_root / QA_REPORT_PATH
        if not qa_report_path.exists():
            status = "TEST_FAILED_NO_REPORT"
            iterations.append(_failed_iteration(index, commands, status))
            break

        report = _load_json(qa_report_path)
        fingerprint_hash = new_fingerprint_hash(report)
        corrections = qa_corrector.build_corrections(project_root, report, apply=False)
        qa_corrector.write_outputs(
            corrections,
            project_root / QA_CORRECTIONS_JSON,
            project_root / QA_CORRECTIONS_MD,
        )
        decision = decide_next_action(report, corrections, apply_accents)
        iteration = Iteration(
            index=index,
            report_summary=report.get("summary", {}),
            fingerprint_hash=fingerprint_hash,
            corrections_summary=corrections.get("summary", {}),
            decision=decision,
            commands=commands,
        )
        iterations.append(iteration)

        new_count = int(report.get("summary", {}).get("new", 0))
        if new_count == 0:
            status = "CONVERGED"
            pending_snapshots = {}
            break

        if fingerprint_hash in seen_hashes:
            _restore_snapshots(pending_snapshots)
            status = "OSCILLATION"
            break
        seen_hashes.add(fingerprint_hash)

        if best_new is None or new_count < best_new:
            best_new = new_count
            stale_iterations = 0
            pending_snapshots = {}
        else:
            stale_iterations += 1
            if stale_iterations >= 3:
                _restore_snapshots(pending_snapshots)
                status = "NO_PROGRESS"
                break

        if decision == "DRY_RUN_PENDING":
            status = "DRY_RUN_PENDING"
            break
        if decision == "SKIPPED_UNSAFE":
            status = "SKIPPED_UNSAFE"
            break
        if decision != "APPLY_PATCHES":
            status = decision
            break

        pending_snapshots = _snapshot_patch_targets(project_root, corrections)
        applied = qa_corrector.build_corrections(project_root, report, apply=True)
        qa_corrector.write_outputs(
            applied,
            project_root / QA_CORRECTIONS_JSON,
            project_root / QA_CORRECTIONS_MD,
        )
        if int(applied.get("summary", {}).get("applied", 0)) == 0:
            status = "NO_PATCH_APPLIED"
            break

    result = {
        "version": 1,
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "project_root": str(project_root),
        "deck_path": str(deck_path.relative_to(project_root)),
        "max_iterations": max_iterations,
        "apply_accents": apply_accents,
        "status": status,
        "iterations": [iteration.to_dict() for iteration in iterations],
        "outputs": {
            "run_json": str(report_json.relative_to(project_root)),
            "run_md": str(report_md.relative_to(project_root)),
            "qa_report": str(QA_REPORT_PATH),
            "qa_corrections_json": str(QA_CORRECTIONS_JSON),
            "qa_corrections_md": str(QA_CORRECTIONS_MD),
        },
    }
    _write_json(report_json, result)
    report_md.write_text(_markdown_report(result), encoding="utf-8")
    return result


def decide_next_action(
    report: dict[str, Any],
    corrections: dict[str, Any],
    apply_accents: bool,
) -> str:
    summary = report.get("summary", {})
    corrections_summary = corrections.get("summary", {})
    new_count = int(summary.get("new", 0))
    patch_safe = int(corrections_summary.get("patch_safe", 0))

    if new_count == 0:
        return "CONVERGED"
    if not apply_accents:
        return "DRY_RUN_PENDING"
    if patch_safe > 0:
        return "APPLY_PATCHES"
    return "SKIPPED_UNSAFE"


def new_fingerprint_hash(report: dict[str, Any]) -> str:
    fingerprints = sorted(
        str(violation.get("fingerprint", ""))
        for violation in report.get("violations", [])
        if violation.get("status") == "new"
    )
    payload = json.dumps(fingerprints, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _assemble(project_root: Path, deck_path: Path) -> CommandResult:
    command = [
        sys.executable,
        "scripts/assemble.py",
        "--qa-map",
        "-o",
        str(deck_path),
    ]
    return _run_command("assemble", command, project_root)


def _run_geometry_tests(project_root: Path, deck_path: Path) -> CommandResult:
    report_path = project_root / QA_REPORT_PATH
    if report_path.exists():
        report_path.unlink()
    env = os.environ.copy()
    env["QA_PPTX_PATH"] = str(deck_path)
    command = [
        sys.executable,
        "-m",
        "pytest",
        "tests/test_deck_geometry.py",
        "-q",
    ]
    return _run_command("geometry-tests", command, project_root, env=env)


def _run_command(
    name: str,
    command: list[str],
    cwd: Path,
    env: dict[str, str] | None = None,
) -> CommandResult:
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    return CommandResult(
        name=name,
        command=command,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def _failed_iteration(index: int, commands: list[CommandResult], status: str) -> Iteration:
    return Iteration(
        index=index,
        report_summary={},
        fingerprint_hash="",
        corrections_summary={},
        decision=status,
        commands=commands,
    )


def _snapshot_patch_targets(project_root: Path, corrections: dict[str, Any]) -> dict[Path, str]:
    snapshots: dict[Path, str] = {}
    for action in corrections.get("actions", []):
        if action.get("decision") != "PATCH_SAFE":
            continue
        source_file = action.get("source_file")
        if not source_file:
            continue
        path = (project_root / source_file).resolve()
        try:
            path.relative_to(project_root)
        except ValueError:
            continue
        if path.exists() and path not in snapshots:
            snapshots[path] = path.read_text(encoding="utf-8")
    return snapshots


def _restore_snapshots(snapshots: dict[Path, str]) -> None:
    for path, content in snapshots.items():
        path.write_text(content, encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _resolve(project_root: Path, path: Path) -> Path:
    return path if path.is_absolute() else project_root / path


def _tail(text: str, max_lines: int = 30) -> str:
    lines = text.splitlines()
    return "\n".join(lines[-max_lines:])


def _markdown_report(result: dict[str, Any]) -> str:
    lines = [
        "# Rapport QA PPTX",
        "",
        f"- Statut : `{result['status']}`",
        f"- Projet : `{result['project_root']}`",
        f"- Deck testé : `{result['deck_path']}`",
        f"- Mode apply accents : `{result['apply_accents']}`",
        f"- Itérations : {len(result['iterations'])} / {result['max_iterations']}",
        "",
        "## Itérations",
        "",
        "| Itération | Statut | Nouvelles | Patchs sûrs | Appliqués | Skips | Hash |",
        "|-----------|--------|-----------|-------------|-----------|-------|------|",
    ]
    for iteration in result["iterations"]:
        summary = iteration.get("report_summary", {})
        corrections = iteration.get("corrections_summary", {})
        fingerprint_hash = iteration.get("fingerprint_hash", "")
        lines.append(
            "| {index} | `{decision}` | {new} | {safe} | {applied} | {skips} | `{hash}` |".format(
                index=iteration["index"],
                decision=iteration["decision"],
                new=summary.get("new", ""),
                safe=corrections.get("patch_safe", ""),
                applied=corrections.get("applied", ""),
                skips=corrections.get("skipped", ""),
                hash=fingerprint_hash[:12],
            )
        )
    lines.extend([
        "",
        "## Sorties",
        "",
        f"- Rapport QA : `{result['outputs']['qa_report']}`",
        f"- Correcteur JSON : `{result['outputs']['qa_corrections_json']}`",
        f"- Correcteur Markdown : `{result['outputs']['qa_corrections_md']}`",
        f"- Rapport boucle JSON : `{result['outputs']['run_json']}`",
        "",
        "## Commandes",
        "",
    ])
    for iteration in result["iterations"]:
        lines.append(f"### Itération {iteration['index']}")
        for command in iteration.get("commands", []):
            rendered = " ".join(command["command"])
            lines.append(f"- `{command['name']}` exit={command['returncode']} : `{rendered}`")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", type=Path, default=PROJECT_ROOT)
    parser.add_argument("--max-iterations", type=int, default=5)
    parser.add_argument("--deck-output", type=Path, default=DEFAULT_DECK)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_RUN_JSON)
    parser.add_argument("--report-md", type=Path, default=DEFAULT_RUN_MD)
    parser.add_argument(
        "--apply-accents",
        action="store_true",
        help="Applique uniquement les patchs d'accents classés sûrs",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Supprime .qa avant de lancer la boucle",
    )
    args = parser.parse_args()

    project_root = args.project.resolve()
    if args.clean and (project_root / ".qa").exists():
        shutil.rmtree(project_root / ".qa")

    result = run_loop(
        project_root=project_root,
        deck_path=args.deck_output,
        max_iterations=args.max_iterations,
        apply_accents=args.apply_accents,
        report_json=args.report_json,
        report_md=args.report_md,
    )
    print(
        "[QA-PPTX] "
        f"status={result['status']} iterations={len(result['iterations'])} "
        f"report={result['outputs']['run_md']}"
    )
    if result["iterations"]:
        last = result["iterations"][-1]
        summary = last.get("report_summary", {})
        print(
            "[QA-PPTX] "
            f"new={summary.get('new', '')} total={summary.get('total', '')} "
            f"by_type={summary.get('new_by_type', {})}"
        )


if __name__ == "__main__":
    main()
