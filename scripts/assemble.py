"""Assemble les slides de `scripts/slides/` en un PPTX unique.

Usage :

    python3 scripts/assemble.py                 # toutes les slides
    python3 scripts/assemble.py --only 02       # une seule slide (page_num=1)
    python3 scripts/assemble.py --from 02 --to 05
    python3 scripts/assemble.py -o autre.pptx   # sortie personnalisée

Convention :
  - Les modules `slides/NN_nom.py` sont découverts et triés par nom.
  - Chaque module expose `build(prs, layouts, ctx)` et reçoit dans `ctx`
    la date, le préfixe de pied de page et le numéro de page.
  - Le numéro de page est recalculé à chaque assemblage : insérer ou
    réordonner des slides ne casse pas la pagination.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from igpde_dsfr_components import create_presentation, finalize_pptx  # noqa: E402
import qa_source_map  # noqa: E402
from slides import (  # noqa: E402
    SlideContext, discover_slides, load_slide_module,
)

_config = yaml.safe_load((PROJECT_ROOT / "config.yml").read_text())["formation"]
DATE_DEFAULT = _config["date"]
FOOTER_BASE_DEFAULT = _config["footer"]
OUTPUT_DEFAULT = PROJECT_ROOT / _config["output"]


def _slide_number(path: Path) -> str:
    """Retourne le préfixe numérique d'un fichier de slide (ex. '05', '05a')."""
    stem = path.stem
    prefix = stem.split("_", 1)[0]
    return prefix


def _filter_slides(
    paths: list[Path],
    only: str | None,
    frm: str | None,
    to: str | None,
) -> list[Path]:
    if only:
        kept = [p for p in paths if _slide_number(p) == only]
        if not kept:
            raise SystemExit(f"Aucune slide avec le numéro « {only} »")
        return kept

    if frm is None and to is None:
        return paths

    start = frm or _slide_number(paths[0])
    end = to or _slide_number(paths[-1])
    kept = [p for p in paths if start <= _slide_number(p) <= end]
    if not kept:
        raise SystemExit(f"Aucune slide dans la plage {start}..{end}")
    return kept


def _slide_title(slide) -> str | None:
    """Retourne le premier titre visible trouvé sur la slide."""
    for shape in slide.shapes:
        name = (shape.name or "").lower()
        if "title" not in name and "titre" not in name:
            continue
        if not getattr(shape, "has_text_frame", False):
            continue
        text = shape.text_frame.text.strip()
        if text:
            return text
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", help="Numéro de slide à générer seule (ex. 05)")
    parser.add_argument("--from", dest="frm", help="Numéro de début de plage")
    parser.add_argument("--to", help="Numéro de fin de plage")
    parser.add_argument(
        "-o", "--output", type=Path, default=OUTPUT_DEFAULT,
        help=f"Fichier de sortie (défaut : {OUTPUT_DEFAULT.name})",
    )
    parser.add_argument(
        "--date", default=DATE_DEFAULT,
        help=f"Date affichée dans le footer (défaut : « {DATE_DEFAULT} »)",
    )
    parser.add_argument(
        "--footer-base", default=FOOTER_BASE_DEFAULT,
        help="Préfixe de pied de page transmis dans ctx.footer_base",
    )
    parser.add_argument(
        "--qa-map", action="store_true",
        help="Écrit .qa/source-map.json avec la provenance des composants DSFR",
    )
    args = parser.parse_args()

    all_slides = discover_slides()
    if not all_slides:
        raise SystemExit("Aucun module trouvé dans scripts/slides/ (NN_*.py)")

    selected = _filter_slides(all_slides, args.only, args.frm, args.to)

    prs, layouts = create_presentation()
    if args.qa_map:
        qa_source_map.enable(PROJECT_ROOT)
    try:
        for page_num, path in enumerate(selected, start=1):
            module = load_slide_module(path)
            ctx = SlideContext(
                page_num=page_num,
                date=args.date,
                footer_base=args.footer_base,
            )
            qa_source_map.start_slide(
                slide_index=page_num,
                slide_number=_slide_number(path),
                source_file=str(path.relative_to(PROJECT_ROOT)),
                page_num=page_num,
            )
            module.build(prs, layouts, ctx)
            if args.qa_map and prs.slides:
                qa_source_map.finish_slide(_slide_title(prs.slides[-1]))
            print(f"  [{page_num:02d}] {path.name}")

        finalize_pptx(
            prs, str(args.output),
            title="Formation 102638 - Accessibilité numérique",
            author="Alex Guiderdoni",
            subject="Support de formation IGPDE - DSFR accessible",
        )
        if args.qa_map:
            source_map_path = qa_source_map.write()
            print(f"[QA] Source map : {source_map_path.relative_to(PROJECT_ROOT)}")
    finally:
        qa_source_map.disable()
    print(f"[OK] {args.output.name} généré ({len(selected)} slides)")


if __name__ == "__main__":
    main()
