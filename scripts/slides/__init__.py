"""Modules de slides de la formation IGPDE (code dans config.yml).

Chaque module nommé `NN_nom.py` (où NN est un entier à 2 chiffres) expose :

    def build(prs, layouts, ctx):
        ...

Le `ctx` est un dataclass `SlideContext` injecté par `assemble.py` qui porte
le numéro de page, la date et le texte du pied de page. L'ordre d'exécution
suit le tri alphabétique des noms de fichiers, donc `01_*.py` puis `02_*.py`,
etc. Pour insérer une slide au milieu, renommer les suivantes ou utiliser
un numéro intermédiaire (`05a_*.py` est accepté).
"""

from __future__ import annotations

import importlib.util
import re
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType


SLIDES_DIR = Path(__file__).parent
SLIDE_PATTERN = re.compile(r"^(\d+)[a-z]*_.+\.py$")


@dataclass
class SlideContext:
    """Contexte injecté dans chaque slide au moment de l'assemblage."""

    page_num: int
    date: str
    footer_base: str  # préfixe commun, ex. « Formation 102846 »


def discover_slides() -> list[Path]:
    """Retourne les modules de slides triés par ordre de numérotation."""
    files = [
        p for p in SLIDES_DIR.iterdir()
        if p.is_file() and SLIDE_PATTERN.match(p.name)
    ]
    return sorted(files, key=lambda p: p.name)


def load_slide_module(path: Path) -> ModuleType:
    """Charge un fichier `.py` comme module Python sans passer par import."""
    name = f"slides.{path.stem}"
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Impossible de charger {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "build"):
        raise AttributeError(
            f"{path.name} doit exposer une fonction `build(prs, layouts, ctx)`"
        )
    return module
