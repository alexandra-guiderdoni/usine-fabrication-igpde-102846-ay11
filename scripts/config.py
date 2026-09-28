"""Lit la configuration de session de l'usine."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).parent.parent
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config.yml"
REQUIRED_FIELDS = ("code", "date", "footer", "output", "livrables", "site_url")


def load_formation_config(config_path: Path = DEFAULT_CONFIG_PATH) -> dict[str, str]:
    """Retourne les paramètres de session déclarés dans ``config.yml``."""
    try:
        config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        raise ValueError(f"YAML invalide : {config_path}") from error
    if not isinstance(config, dict) or not isinstance(config.get("formation"), dict):
        raise ValueError("Section obligatoire absente : formation")

    formation = config["formation"]
    for field in REQUIRED_FIELDS:
        value = formation.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Paramètre obligatoire invalide : {field}")
    return {field: formation[field] for field in REQUIRED_FIELDS}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Chemin du fichier de configuration",
    )
    parser.add_argument(
        "--value",
        choices=REQUIRED_FIELDS,
        required=True,
        help="Paramètre de session à afficher",
    )
    args = parser.parse_args()
    try:
        value = load_formation_config(args.config)[args.value]
    except (OSError, ValueError) as error:
        parser.exit(2, f"Configuration invalide : {error}\n")
    print(value)


if __name__ == "__main__":
    main()
