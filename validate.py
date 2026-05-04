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
        self.ids: set[str] = set()
        self.fragments: list[str] = []
        self.html_lang: str | None = None
        self.images_without_alt: list[str] = []
        self.local_refs: list[str] = []
        self.bad_refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if "id" in values and values["id"]:
            self.ids.add(values["id"])
        if tag == "html":
            self.html_lang = values.get("lang")
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src", "image sans src"))
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
            if value.startswith("#"):
                self.fragments.append(value[1:])
                continue
            if value.startswith(("mailto:", "tel:", "sms:")):
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

    accessible_errors: list[str] = []
    forbidden_accessible_markers = (
        "Contenu ministériel à produire",
        "Squelette de page",
        "demo-no-focus",
        "demo-fixed-cards",
        "demo-low-contrast",
        "demo-pale-link",
        "demo-pale-action",
        "demo-red-border",
    )
    for file in sorted((DOCS / "site-accessible").glob("*.html")):
        text = file.read_text(encoding="utf-8")
        parser = LinkParser(file)
        parser.feed(text)
        if parser.html_lang != "fr":
            accessible_errors.append(f"{file}: lang attendu fr, trouvé {parser.html_lang!r}")
        for fragment in parser.fragments:
            if fragment and fragment not in parser.ids:
                accessible_errors.append(f"{file}: ancre locale absente #{fragment}")
        for marker in forbidden_accessible_markers:
            if marker in text:
                accessible_errors.append(f"{file}: marqueur interdit en version accessible: {marker}")
        if parser.images_without_alt:
            accessible_errors.append(f"{file}: image(s) sans alt: {', '.join(parser.images_without_alt)}")
    if accessible_errors:
        details = "\n".join(accessible_errors[:30])
        raise ValueError(f"Contrôles version accessible en échec:\n{details}")

    help_errors: list[str] = []
    for file in sorted((DOCS / "site-aide-correction").glob("ec*.html")):
        text = file.read_text(encoding="utf-8")
        help_pos = text.find('id="help-title"')
        content_pos = text.find('id="content-title"')
        if help_pos == -1:
            help_errors.append(f"{file}: bloc Aide à la correction absent")
        elif content_pos == -1:
            help_errors.append(f"{file}: contenu principal de l'exercice absent")
        elif help_pos > content_pos:
            help_errors.append(f"{file}: l'aide doit être placée avant le contenu d'exercice")
    if help_errors:
        details = "\n".join(help_errors[:30])
        raise ValueError(f"Contrôles version aide à la correction en échec:\n{details}")


def main() -> None:
    validate_contract()
    validate_docs()
    print("OK validation Easy Checks")


if __name__ == "__main__":
    main()
