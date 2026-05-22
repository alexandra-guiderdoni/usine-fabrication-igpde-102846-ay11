"""Source map QA pour relier les shapes PPTX aux scripts de slides.

Le module est inactif par défaut. `assemble.py --qa-map` active le registre,
les composants DSFR enregistrent alors les shapes créées par chaque appel.
"""

from __future__ import annotations

import inspect
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

EMU_PER_INCH = 914400


@dataclass
class _State:
    enabled: bool = False
    project_root: Path | None = None
    output_path: Path | None = None
    current_slide: dict[str, Any] | None = None
    slides: list[dict[str, Any]] = field(default_factory=list)
    components: list[dict[str, Any]] = field(default_factory=list)
    call_order: int = 0


_STATE = _State()


def enable(project_root: Path, output_path: Path | None = None) -> None:
    """Active la collecte source map pour l'assemblage courant."""
    reset()
    root = Path(project_root).resolve()
    _STATE.enabled = True
    _STATE.project_root = root
    _STATE.output_path = output_path or root / ".qa" / "source-map.json"


def disable() -> None:
    """Désactive la collecte sans effacer les données déjà écrites."""
    _STATE.enabled = False
    _STATE.current_slide = None


def reset() -> None:
    """Réinitialise entièrement le registre."""
    _STATE.enabled = False
    _STATE.project_root = None
    _STATE.output_path = None
    _STATE.current_slide = None
    _STATE.slides = []
    _STATE.components = []
    _STATE.call_order = 0


def is_enabled() -> bool:
    return _STATE.enabled


def start_slide(slide_index: int, slide_number: str, source_file: str, page_num: int) -> None:
    """Déclare la slide en cours de génération."""
    if not _STATE.enabled:
        return
    _STATE.call_order = 0
    _STATE.current_slide = {
        "slide_index": slide_index,
        "slide_number": slide_number,
        "source_file": source_file,
        "page_num": page_num,
        "title": None,
    }


def finish_slide(title: str | None = None) -> None:
    """Clôt la slide courante et mémorise ses métadonnées."""
    if not _STATE.enabled or _STATE.current_slide is None:
        return
    _STATE.current_slide["title"] = title
    _STATE.slides.append(dict(_STATE.current_slide))
    _STATE.current_slide = None


def shape_count(slide: Any) -> int | None:
    """Retourne l'index de départ pour capturer les shapes créées ensuite."""
    if not _STATE.enabled:
        return None
    return len(slide.shapes)


def record_component(
    component_type: str,
    slide: Any,
    start_index: int | None,
    metadata: dict[str, Any] | None = None,
) -> None:
    """Enregistre les shapes créées par un composant DSFR."""
    if not _STATE.enabled or _STATE.current_slide is None or start_index is None:
        return
    shapes = list(slide.shapes)[start_index:]
    if not shapes:
        return

    _STATE.call_order += 1
    source_file, call_lineno = _find_caller()
    slide_meta = _STATE.current_slide
    component_id = (
        f"{slide_meta['slide_number']}:{_STATE.call_order}:"
        f"{component_type}:{call_lineno or 'unknown'}"
    )
    entry = {
        "component_id": component_id,
        "component_type": component_type,
        "slide_index": slide_meta["slide_index"],
        "slide_number": slide_meta["slide_number"],
        "page_num": slide_meta["page_num"],
        "source_file": source_file or slide_meta["source_file"],
        "call_lineno": call_lineno,
        "call_order": _STATE.call_order,
        "metadata": metadata or {},
        "shapes": [_shape_payload(shape) for shape in shapes],
    }
    _STATE.components.append(entry)


def build_source_map() -> dict[str, Any]:
    """Retourne la source map en mémoire."""
    return {
        "version": 1,
        "slides": list(_STATE.slides),
        "components": list(_STATE.components),
    }


def write(output_path: Path | None = None) -> Path:
    """Écrit la source map JSON et retourne son chemin."""
    path = output_path or _STATE.output_path
    if path is None:
        raise RuntimeError("qa_source_map.write() appelé sans output_path")
    path = Path(path)
    if not path.is_absolute() and _STATE.project_root is not None:
        path = _STATE.project_root / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(build_source_map(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def _shape_payload(shape: Any) -> dict[str, Any]:
    return {
        "shape_id": getattr(shape, "shape_id", None),
        "name": shape.name or "",
        "shape_type": int(shape.shape_type) if getattr(shape, "shape_type", None) is not None else None,
        "rect": _shape_rect(shape),
    }


def _shape_rect(shape: Any) -> dict[str, float]:
    top = shape.top / EMU_PER_INCH if shape.top else 0
    left = shape.left / EMU_PER_INCH if shape.left else 0
    height = shape.height / EMU_PER_INCH if shape.height else 0
    width = shape.width / EMU_PER_INCH if shape.width else 0
    return {
        "top": round(top, 3),
        "left": round(left, 3),
        "height": round(height, 3),
        "width": round(width, 3),
        "bottom": round(top + height, 3),
        "right": round(left + width, 3),
    }


def _find_caller() -> tuple[str | None, int | None]:
    """Trouve la ligne d'appel dans le fichier source de slide."""
    current_source = None
    if _STATE.project_root and _STATE.current_slide:
        current_source = (_STATE.project_root / _STATE.current_slide["source_file"]).resolve()

    fallback: tuple[str | None, int | None] = (None, None)
    for frame in inspect.stack()[2:]:
        path = Path(frame.filename).resolve()
        if path.name in {"qa_source_map.py", "igpde_dsfr_components.py"}:
            continue
        rel = _relative_path(path)
        if fallback == (None, None):
            fallback = (rel, frame.lineno)
        if current_source is not None and path == current_source:
            return rel, frame.lineno
    return fallback


def _relative_path(path: Path) -> str:
    root = _STATE.project_root
    if root is None:
        return str(path)
    try:
        return str(path.resolve().relative_to(root))
    except ValueError:
        return str(path)
