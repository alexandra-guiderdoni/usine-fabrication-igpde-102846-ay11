"""Tests des garde-fous Git contre les verrous bureautiques."""

from __future__ import annotations

import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
HOOK = PROJECT_ROOT / ".githooks" / "pre-commit"


def test_gitignore_ignore_les_verrous_libreoffice():
    result = subprocess.run(
        ["git", "check-ignore", "--quiet", ".~lock.deck.pptx#"],
        cwd=PROJECT_ROOT,
        check=False,
    )

    assert result.returncode == 0


def test_hook_bloque_un_verrou_libreoffice_force_dans_l_index(tmp_path):
    subprocess.run(["git", "init", "--quiet"], cwd=tmp_path, check=True)
    lock = tmp_path / ".~lock.deck.pptx#"
    lock.write_text("verrou", encoding="utf-8")
    subprocess.run(["git", "add", "--force", lock.name], cwd=tmp_path, check=True)

    result = subprocess.run(
        ["bash", str(HOOK)],
        cwd=tmp_path,
        capture_output=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 1
    assert "fichier de verrou Office" in result.stderr
