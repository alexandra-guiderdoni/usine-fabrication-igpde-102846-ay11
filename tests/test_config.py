"""Tests du contrat de configuration de l'usine."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_CLI = PROJECT_ROOT / "scripts" / "config.py"
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from config import load_formation_config  # noqa: E402


def test_la_commande_publique_lit_le_dossier_de_livraison():
    result = subprocess.run(
        [sys.executable, str(CONFIG_CLI), "--value", "livrables"],
        capture_output=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "livrables-IGPDE-2026-102846\n"


def test_refuse_une_configuration_sans_cle_obligatoire(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text('formation:\n  code: "102846"\n', encoding="utf-8")

    with pytest.raises(ValueError, match="date"):
        load_formation_config(config_path)


def test_la_commande_lit_un_yaml_valide_independamment_de_sa_presentation(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text(
        """formation:
    code: "102846"
    date: 9 octobre 2026
    footer: Formation 102846
    output: support-formation-102846-2026-IGPDE.pptx
    livrables: pack-de-test
    site_url: https://example.test/site/
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(CONFIG_CLI),
            "--config",
            str(config_path),
            "--value",
            "livrables",
        ],
        capture_output=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "pack-de-test\n"


def test_make_lit_le_dossier_de_livraison_par_le_chargeur(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text(
        """formation:
    code: "102846"
    date: 9 octobre 2026
    footer: Formation 102846
    output: support-formation-102846-2026-IGPDE.pptx
    livrables: pack-de-test
    site_url: https://example.test/site/
""",
        encoding="utf-8",
    )

    result = subprocess.run(
        ["make", "-pn", f"CONFIG={config_path}"],
        capture_output=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "LIVRABLES := pack-de-test" in result.stdout


def test_make_propage_la_configuration_aux_generateurs(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text(
        """formation:
    code: "999999"
    date: 9 octobre 2026
    footer: Formation alternative
    output: deck-alternatif.pptx
    livrables: pack-alternatif
    site_url: https://example.test/alternative/
""",
        encoding="utf-8",
    )

    makefile = tmp_path / "Makefile"
    makefile.write_text(
        f"include {PROJECT_ROOT / 'Makefile'}\n"
        "afficher-config-test:\n"
        f"\t@$(PYTHON) {CONFIG_CLI} --value code\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            "make",
            "-s",
            "-f",
            str(makefile),
            f"CONFIG={config_path}",
            "afficher-config-test",
        ],
        capture_output=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "999999\n"


def test_make_installer_ne_depend_pas_du_chargeur_de_configuration():
    result = subprocess.run(
        ["make", "-n", "installer", "PYTHON=false"],
        capture_output=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "uv venv .venv" in result.stdout


def test_refuse_un_yaml_mal_forme_avec_un_message_explicite(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text("formation: [\n", encoding="utf-8")

    with pytest.raises(ValueError, match="YAML invalide"):
        load_formation_config(config_path)


def test_la_commande_signale_une_configuration_incomplete_sans_trace(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text('formation:\n  code: "102846"\n', encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(CONFIG_CLI),
            "--config",
            str(config_path),
            "--value",
            "livrables",
        ],
        capture_output=True,
        cwd=PROJECT_ROOT,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 2
    assert (
        "Configuration invalide : Paramètre obligatoire invalide : date"
        in result.stderr
    )
    assert "Traceback" not in result.stderr
