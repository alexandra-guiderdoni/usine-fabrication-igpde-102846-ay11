#!/usr/bin/env python3
"""Validate the Easy Checks exercise skeleton."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, urldefrag

import yaml


ROOT = Path(__file__).resolve().parent
CONTRACT = ROOT / "03-easy-checks" / "evaluation_contract.yml"
DOCS = ROOT / "docs"
ALLOWED_EXTERNAL_HOSTS = {
    "www.youtube.com",
    "youtube.com",
    "www.youtube-nocookie.com",
    "youtube-nocookie.com",
}


class LinkParser(HTMLParser):
    def __init__(self, file: Path) -> None:
        super().__init__()
        self.file = file
        self.local_refs: list[str] = []
        self.bad_refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        href = values.get("href")
        src = values.get("src")
        for value in (href, src):
            if not value:
                continue
            if value == "#":
                self.bad_refs.append(value)
                continue
            if value.startswith(("http://", "https://", "//")):
                host = urlparse(value).netloc
                if host not in ALLOWED_EXTERNAL_HOSTS:
                    self.bad_refs.append(value)
                continue
            if value.startswith("cdn"):
                self.bad_refs.append(value)
                continue
            if value.startswith(("mailto:", "tel:", "#")):
                continue
            target, _ = urldefrag(value)
            if target:
                self.local_refs.append(target)


def validate_contract() -> None:
    with CONTRACT.open(encoding="utf-8") as handle:
        contract = yaml.safe_load(handle)
    pages = contract.get("pages", [])
    if len(pages) != 13:
        raise ValueError(f"Le contrat doit contenir 13 pages, trouvé: {len(pages)}")
    ids = [page.get("id") for page in pages]
    if len(set(ids)) != len(ids):
        raise ValueError("Les identifiants de pages ne sont pas uniques")
    required = {
        "id",
        "number",
        "title",
        "easy_check",
        "severity",
        "expected_minimal_finding",
        "minimal_proof",
        "detection",
        "inaccessible_errors",
        "accessible_correction",
        "help",
        "dsfr_components",
        "grid",
    }
    for page in pages:
        missing = sorted(required - set(page))
        if missing:
            raise ValueError(f"{page.get('id', 'page inconnue')}: champs manquants {missing}")
        for key in ("hint", "problem", "fix"):
            if key not in page["help"]:
                raise ValueError(f"{page['id']}: help.{key} manquant")


def validate_docs() -> None:
    required_files = [
        DOCS / "index.html",
        DOCS / "manifest.md",
        DOCS / "corrige-easy-checks.md",
        DOCS / "assets" / "dsfr" / "dsfr.min.css",
        DOCS / "assets" / "dsfr" / "utility" / "utility.min.css",
        DOCS / "assets" / "dsfr" / "dsfr.module.min.js",
        DOCS / "assets" / "dsfr" / "dsfr.nomodule.min.js",
        DOCS / "assets" / "downloads" / "grille-audit-easy-checks.xlsx",
    ]
    for file in required_files:
        if not file.exists():
            raise FileNotFoundError(file)

    html_files = sorted(DOCS.rglob("*.html"))
    if len(html_files) < 47:
        raise ValueError(f"Nombre de pages HTML inattendu: {len(html_files)}")

    missing: list[tuple[Path, str]] = []
    bad_refs: list[tuple[Path, str]] = []
    for file in html_files:
        parser = LinkParser(file)
        parser.feed(file.read_text(encoding="utf-8"))
        for value in parser.bad_refs:
            bad_refs.append((file, value))
        for value in parser.local_refs:
            path = (file.parent / value).resolve()
            if not path.exists():
                missing.append((file, value))
    if bad_refs:
        details = "\n".join(f"{file}: {value}" for file, value in bad_refs[:20])
        raise ValueError(f"Références interdites détectées:\n{details}")
    if missing:
        details = "\n".join(f"{file}: {value}" for file, value in missing[:20])
        raise FileNotFoundError(f"Liens ou assets locaux manquants:\n{details}")


def main() -> None:
    validate_contract()
    validate_docs()
    print("OK validation Easy Checks")


if __name__ == "__main__":
    main()
