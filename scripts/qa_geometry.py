"""Collecte structurée des violations géométriques du deck PPTX.

Ce module fournit le signal exploité par les tests PRD-119 : mêmes règles
que les tests PRD-118, mais avec fingerprints stables et rapport JSON.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from igpde_dsfr_components import BOTTOM_CONTENT

NSMAP_A = "http://schemas.openxmlformats.org/drawingml/2006/main"

LAYOUT_PATTERNS = {"espace réservé", "placeholder", "title 1"}

DECORATIVE_PATTERNS = {
    "decorat", "accent", "logo", "ligne", "separator", "connecteur",
}

FOOTER_EXTRA_EXCL = {"qrcode", "qr-code"}
FONT_EXTRA_EXCL = {"qrcode", "qr-code", "url-visible"}

KNOWN_FOOTER_VIOLATIONS = 11
KNOWN_ALT_VIOLATIONS = 42
KNOWN_FONT_VIOLATIONS = 25

MIN_FONT_PT = 14
EMU_PER_INCH = 914400
EMU_TOLERANCE = 0.01

BASELINE_PATH = Path("tests/baselines/known-geometry-violations.json")
REPORT_PATH = Path(".qa/qa-report.json")

ACCENT_TERMS = {
    "accessibilite": "accessibilité",
    "amelioration": "amélioration",
    "conformite": "conformité",
    "critere": "critère",
    "criteres": "critères",
    "decrire": "décrire",
    "decrit": "décrit",
    "decrite": "décrite",
    "decrites": "décrites",
    "deficience": "déficience",
    "deficiences": "déficiences",
    "donnee": "donnée",
    "donnees": "données",
    "ecran": "écran",
    "ecrans": "écrans",
    "element": "élément",
    "elements": "éléments",
    "etiquette": "étiquette",
    "etiquettes": "étiquettes",
    "evitement": "évitement",
    "general": "général",
    "legale": "légale",
    "legales": "légales",
    "methode": "méthode",
    "methodes": "méthodes",
    "numerique": "numérique",
    "numeriques": "numériques",
    "redaction": "rédaction",
    "rediger": "rédiger",
    "referent": "référent",
    "referentiel": "référentiel",
    "regle": "règle",
    "regles": "règles",
    "schema": "schéma",
    "schemas": "schémas",
    "securite": "sécurité",
    "thematique": "thématique",
    "thematiques": "thématiques",
    "video": "vidéo",
    "videos": "vidéos",
}

ACCENT_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(term) for term in sorted(ACCENT_TERMS, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)


def _is_excluded(name: str | None, patterns: set[str]) -> bool:
    if not name:
        return False
    n = name.lower()
    return any(pattern in n for pattern in patterns)


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


def _rect_key(rect: dict[str, float]) -> str:
    return (
        f"t={rect['top']:.2f}:l={rect['left']:.2f}:"
        f"h={rect['height']:.2f}:w={rect['width']:.2f}"
    )


def _fingerprint(violation_type: str, slide_index: int, shape_name: str, rect: dict[str, float], detail: str) -> str:
    return (
        f"{violation_type}|slide={slide_index}|shape={shape_name}|"
        f"{_rect_key(rect)}|{detail}"
    )


def _shape_text(shape: Any) -> str:
    if not getattr(shape, "has_text_frame", False):
        return ""
    try:
        return "\n".join(paragraph.text for paragraph in shape.text_frame.paragraphs).strip()
    except Exception:
        return ""


def _text_excerpt(text: str, limit: int = 60) -> str:
    compact = " ".join(text.split())
    return compact[:limit]


def _is_url_context(line: str) -> bool:
    lowered = line.lower()
    return "http://" in lowered or "https://" in lowered or "www." in lowered or "@" in lowered


def _base_violation(
    violation_type: str,
    slide_index: int,
    shape: Any,
    rect: dict[str, float],
    detail: str,
    message: str,
    **extra: Any,
) -> dict[str, Any]:
    shape_name = shape.name or ""
    data = {
        "type": violation_type,
        "slide_index": slide_index,
        "shape_name": shape_name,
        "rect": rect,
        "detail": detail,
        "message": message,
        "fingerprint": _fingerprint(violation_type, slide_index, shape_name, rect, detail),
    }
    data.update(extra)
    return data


def _rects_overlap_2d(a: dict[str, float], b: dict[str, float], tol: float = 0.02) -> bool:
    v_overlap = (a["bottom"] > b["top"] + tol) and (b["bottom"] > a["top"] + tol)
    h_overlap = (a["right"] > b["left"] + tol) and (b["right"] > a["left"] + tol)
    return v_overlap and h_overlap


def _collect_footer(deck: Any) -> list[dict[str, Any]]:
    excl = LAYOUT_PATTERNS | DECORATIVE_PATTERNS | FOOTER_EXTRA_EXCL
    violations = []
    for slide_index, slide in enumerate(deck.slides, 1):
        for shape in slide.shapes:
            if _is_excluded(shape.name, excl):
                continue
            rect = _shape_rect(shape)
            if rect["bottom"] > BOTTOM_CONTENT + EMU_TOLERANCE:
                detail = f"bottom={rect['bottom']:.3f}>limit={BOTTOM_CONTENT:.2f}"
                violations.append(
                    _base_violation(
                        "footer",
                        slide_index,
                        shape,
                        rect,
                        detail,
                        f"Slide {slide_index}: \"{shape.name}\" bottom={rect['bottom']:.3f}\" > {BOTTOM_CONTENT}\"",
                    )
                )
    return violations


def _collect_overlaps(deck: Any) -> list[dict[str, Any]]:
    violations = []
    for slide_index, slide in enumerate(deck.slides, 1):
        boxes = []
        for shape in slide.shapes:
            if shape.name == "DSFR-box":
                boxes.append((shape, _shape_rect(shape)))
        for first in range(len(boxes)):
            for second in range(first + 1, len(boxes)):
                shape_a, rect_a = boxes[first]
                shape_b, rect_b = boxes[second]
                if not _rects_overlap_2d(rect_a, rect_b):
                    continue
                detail = f"{_rect_key(rect_a)}:vs:{_rect_key(rect_b)}"
                violations.append(
                    _base_violation(
                        "overlap",
                        slide_index,
                        shape_a,
                        rect_a,
                        detail,
                        (
                            f"Slide {slide_index}: box@({rect_a['top']:.2f}\","
                            f"{rect_a['left']:.2f}\") vs box@({rect_b['top']:.2f}\","
                            f"{rect_b['left']:.2f}\")"
                        ),
                        other_shape_name=shape_b.name or "",
                        other_rect=rect_b,
                    )
                )
    return violations


def _collect_alt_text(deck: Any) -> list[dict[str, Any]]:
    violations = []
    for slide_index, slide in enumerate(deck.slides, 1):
        for shape in slide.shapes:
            if shape.shape_type != 13:
                continue
            if _is_excluded(shape.name, DECORATIVE_PATTERNS):
                continue
            c_nv_pr = shape._element.find(f".//{{{NSMAP_A}}}cNvPr")
            descr = c_nv_pr.get("descr", "") if c_nv_pr is not None else ""
            if not descr:
                rect = _shape_rect(shape)
                violations.append(
                    _base_violation(
                        "alt_text",
                        slide_index,
                        shape,
                        rect,
                        "missing_descr",
                        f"Slide {slide_index}: image \"{shape.name}\" sans alt-text",
                    )
                )
    return violations


def _collect_font_size(deck: Any) -> list[dict[str, Any]]:
    excl = LAYOUT_PATTERNS | DECORATIVE_PATTERNS | FONT_EXTRA_EXCL
    violations = []
    for slide_index, slide in enumerate(deck.slides, 1):
        for shape in slide.shapes:
            if _is_excluded(shape.name, excl):
                continue
            if not getattr(shape, "has_text_frame", False):
                continue
            try:
                paragraphs = shape.text_frame.paragraphs
            except Exception:
                continue
            rect = _shape_rect(shape)
            for paragraph_index, paragraph in enumerate(paragraphs):
                for run_index, run in enumerate(paragraph.runs):
                    if run.font.size is None:
                        continue
                    size_pt = run.font.size.pt
                    if size_pt >= MIN_FONT_PT:
                        continue
                    txt = run.text[:30].replace("\n", " ")
                    detail = f"p={paragraph_index}:r={run_index}:size={size_pt:.1f}:text={txt}"
                    violations.append(
                        _base_violation(
                            "font_size",
                            slide_index,
                            shape,
                            rect,
                            detail,
                            f"Slide {slide_index}: \"{shape.name}\" \"{txt}\" = {size_pt}pt",
                            size_pt=round(size_pt, 2),
                            text=txt,
                        )
                    )
    return violations


def find_accent_issues(text: str) -> list[dict[str, str]]:
    """Retourne les formes françaises probablement non accentuées."""
    issues = []
    for line in text.splitlines():
        if _is_url_context(line):
            continue
        for match in ACCENT_PATTERN.finditer(line):
            found = match.group(0)
            expected = ACCENT_TERMS[found.lower()]
            issues.append({
                "found": found,
                "expected": expected,
                "context": _text_excerpt(line),
            })
    return issues


def _collect_accents(deck: Any) -> list[dict[str, Any]]:
    violations = []
    for slide_index, slide in enumerate(deck.slides, 1):
        for shape in slide.shapes:
            text = _shape_text(shape)
            if not text:
                continue
            rect = _shape_rect(shape)
            for issue in find_accent_issues(text):
                detail = f"{issue['found'].lower()}->{issue['expected']}:{issue['context']}"
                violations.append(
                    _base_violation(
                        "accent_fr",
                        slide_index,
                        shape,
                        rect,
                        detail,
                        (
                            f"Slide {slide_index}: \"{shape.name}\" contient "
                            f"\"{issue['found']}\" sans accent"
                        ),
                        found=issue["found"],
                        expected=issue["expected"],
                        context=issue["context"],
                    )
                )
    return violations


def collect_violations(deck: Any) -> list[dict[str, Any]]:
    """Collecte toutes les violations couvertes par PRD-118 + accents."""
    violations = []
    violations.extend(_collect_footer(deck))
    violations.extend(_collect_overlaps(deck))
    violations.extend(_collect_alt_text(deck))
    violations.extend(_collect_font_size(deck))
    violations.extend(_collect_accents(deck))
    return violations


def load_baseline(project_root: Path) -> set[str]:
    path = project_root / BASELINE_PATH
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    return set(data.get("fingerprints", []))


def build_report(deck: Any, project_root: Path) -> dict[str, Any]:
    """Construit le rapport QA sans l'écrire sur disque."""
    known_fingerprints = load_baseline(project_root)
    violations = collect_violations(deck)
    current_fingerprints = {violation["fingerprint"] for violation in violations}

    for violation in violations:
        violation["status"] = (
            "known" if violation["fingerprint"] in known_fingerprints else "new"
        )

    by_status = Counter(violation["status"] for violation in violations)
    by_type = Counter(violation["type"] for violation in violations)
    new_by_type = Counter(
        violation["type"] for violation in violations if violation["status"] == "new"
    )
    resolved = sorted(known_fingerprints - current_fingerprints)

    return {
        "version": 1,
        "baseline": str(BASELINE_PATH),
        "summary": {
            "total": len(violations),
            "known": by_status.get("known", 0),
            "new": by_status.get("new", 0),
            "resolved": len(resolved),
            "ignored": 0,
            "by_type": dict(sorted(by_type.items())),
            "new_by_type": dict(sorted(new_by_type.items())),
        },
        "violations": violations,
        "resolved": resolved,
        "ignored": [],
    }


def write_report(deck: Any, project_root: Path, report_path: Path | None = None) -> dict[str, Any]:
    """Écrit `.qa/qa-report.json` et retourne le rapport."""
    report = build_report(deck, project_root)
    output = project_root / (report_path or REPORT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return report
