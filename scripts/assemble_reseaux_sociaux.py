"""Assemble le module 4 Réseaux sociaux en PPTX autonome.

Les slides sont des fichiers `rs_NN_*.py` dans `scripts/slides/` -
ce préfixe les rend invisibles à l'assembleur principal.

Usage :
    python3 scripts/assemble_reseaux_sociaux.py
    python3 scripts/assemble_reseaux_sociaux.py -o mon-fichier.pptx
    python3 scripts/assemble_reseaux_sociaux.py --only rs_05
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

import yaml
from types import ModuleType

SCRIPTS_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPTS_DIR))

from igpde_dsfr_components import create_presentation, finalize_pptx  # noqa: E402
from slides import SlideContext  # noqa: E402

SLIDES_DIR = SCRIPTS_DIR / "slides"
RS_PATTERN = re.compile(r"^rs_\d+_.+\.py$")
OUTPUT_DEFAULT = SCRIPTS_DIR.parent / "04-reseaux-sociaux" / "module4-reseaux-sociaux.pptx"
_CONFIG = yaml.safe_load((SCRIPTS_DIR.parent / "config.yml").read_text(encoding="utf-8"))["formation"]
DATE_DEFAULT = _CONFIG["date"]
FOOTER_BASE_DEFAULT = _CONFIG["footer"]


def discover_rs_slides() -> list[Path]:
    files = [p for p in SLIDES_DIR.iterdir() if p.is_file() and RS_PATTERN.match(p.name)]
    return sorted(files, key=lambda p: p.name)


def load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(f"slides_rs.{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Impossible de charger {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if not hasattr(mod, "build"):
        raise AttributeError(f"{path.name} doit exposer build(prs, layouts, ctx)")
    return mod


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", help="Préfixe de slide à générer seule (ex. rs_05)")
    parser.add_argument("-o", "--output", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument("--date", default=DATE_DEFAULT)
    parser.add_argument("--footer-base", default=FOOTER_BASE_DEFAULT)
    args = parser.parse_args()

    all_slides = discover_rs_slides()
    if not all_slides:
        raise SystemExit("Aucun fichier rs_NN_*.py trouvé dans scripts/slides/")

    selected = [p for p in all_slides if p.stem.startswith(args.only)] if args.only else all_slides

    prs, layouts = create_presentation()
    for page_num, path in enumerate(selected, start=1):
        mod = load_module(path)
        ctx = SlideContext(page_num=page_num, date=args.date, footer_base=args.footer_base)
        mod.build(prs, layouts, ctx)
        print(f"  [{page_num:02d}] {path.name}")

    finalize_pptx(
        prs, str(args.output),
        title="Module 4 - Accessibilité réseaux sociaux",
        author="Alex Guiderdoni",
        subject=f"Formation {_CONFIG['code']} IGPDE - Module réseaux sociaux",
    )
    print(f"[OK] {args.output.name} généré ({len(selected)} slides)")


if __name__ == "__main__":
    main()
