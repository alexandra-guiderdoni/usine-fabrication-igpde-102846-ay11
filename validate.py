#!/usr/bin/env python3
"""Validation du site d'exercice points de controle rapides.

Vérifie le contrat YAML, les assets DSFR, les liens locaux et ancres,
la liste blanche d'hôtes externes, les attributs lang et alt, et des
cas specifiques (EC06, version accessible).
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, urldefrag

import yaml


ROOT = Path(__file__).resolve().parent
CONTRACT = ROOT / "03-easy-checks" / "evaluation_contract.yml"
DOCS = ROOT / "docs"
ALLOWED_EXTERNAL_HOSTS = {
    "accessibilite.numerique.gouv.fr",
    "addons.mozilla.org",
    "chromewebstore.google.com",
    "data.gouv.fr",
    "github.com",
    "info.gouv.fr",
    "legifrance.gouv.fr",
    "service-public.gouv.fr",
    "vispero.com",
    "www.data.gouv.fr",
    "www.defenseurdesdroits.fr",
    "www.legifrance.gouv.fr",
    "www.service-public.gouv.fr",
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
        self.local_refs: list[tuple[str, str]] = []
        self.bad_refs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if "id" in values and values["id"]:
            self.ids.add(values["id"])
        if tag == "html":
            self.html_lang = values.get("lang")
        if tag == "img" and "alt" not in values:
            self.images_without_alt.append(values.get("src", "image sans src"))
        for value in (values.get("href"), values.get("src"), values.get("action")):
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
            target, fragment = urldefrag(value)
            target = urlparse(target).path
            if target:
                self.local_refs.append((target, fragment))


def load_contract_pages() -> list[dict]:
    with CONTRACT.open(encoding="utf-8") as handle:
        contract = yaml.safe_load(handle)
    return contract.get("pages", [])


def validate_contract() -> list[dict]:
    pages = load_contract_pages()
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
    return pages


def validate_docs(contract_pages: list[dict] | None = None) -> None:
    if contract_pages is None:
        contract_pages = load_contract_pages()
    required_files = [
        DOCS / ".nojekyll",
        DOCS / "index.html",
        DOCS / "manifest.md",
        DOCS / "corrige-easy-checks.md",
        DOCS / "assets" / "dsfr" / "dsfr.min.css",
        DOCS / "assets" / "dsfr" / "utility" / "utility.min.css",
        DOCS / "assets" / "dsfr" / "dsfr.module.min.js",
        DOCS / "assets" / "dsfr" / "dsfr.nomodule.min.js",
        DOCS / "assets" / "downloads" / "grille-audit-easy-checks.xlsx",
    ]
    for variant in ("site-inaccessible", "site-aide-correction", "site-accessible"):
        required_files.extend(
            DOCS / variant / f"{page['id']}.html"
            for page in contract_pages
        )
    for file in required_files:
        if not file.exists():
            raise FileNotFoundError(file)

    html_files = sorted(DOCS.rglob("*.html"))
    if len(html_files) < 47:
        raise ValueError(f"Nombre de pages HTML inattendu: {len(html_files)}")

    docs_root = DOCS.resolve()
    missing: list[tuple[Path, str]] = []
    outside_docs: list[tuple[Path, str]] = []
    missing_anchors: list[tuple[Path, str]] = []
    target_ids: dict[Path, set[str]] = {}
    bad_refs: list[tuple[Path, str]] = []
    for file in html_files:
        parser = LinkParser(file)
        parser.feed(file.read_text(encoding="utf-8"))
        for value in parser.bad_refs:
            bad_refs.append((file, value))
        for value, fragment in parser.local_refs:
            path = (file.parent / value).resolve()
            if not path.is_relative_to(docs_root):
                outside_docs.append((file, value))
            elif not path.exists():
                missing.append((file, value))
            elif fragment and path.suffix == ".html":
                if path not in target_ids:
                    target_parser = LinkParser(path)
                    target_parser.feed(path.read_text(encoding="utf-8"))
                    target_ids[path] = target_parser.ids
                if fragment not in target_ids[path]:
                    missing_anchors.append((file, f"{value}#{fragment}"))
    if bad_refs:
        details = "\n".join(f"{file}: {value}" for file, value in bad_refs[:20])
        raise ValueError(f"Références interdites détectées:\n{details}")
    if outside_docs:
        details = "\n".join(f"{file}: {value}" for file, value in outside_docs[:20])
        raise ValueError(f"Références locales hors de docs détectées:\n{details}")
    if missing:
        details = "\n".join(f"{file}: {value}" for file, value in missing[:20])
        raise FileNotFoundError(f"Liens ou assets locaux manquants:\n{details}")
    if missing_anchors:
        details = "\n".join(f"{file}: {value}" for file, value in missing_anchors[:20])
        raise ValueError(f"Ancres locales absentes:\n{details}")

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

    ec06_errors: list[str] = []
    ec06_bad_snippets = (
        'data-fr-opened="false" aria-expanded="false" aria-controls="publish-session-modal" class="fr-btn demo-modal-trigger" type="button" tabindex="0">Publier la session',
        'class="fr-link" href="ec12-form-labels.html" tabindex="-1">Vérifier le formulaire',
        'class="fr-link" href="#participants-notification" tabindex="-1">Prévenir les participants',
        'class="fr-modal demo-modal-keyboard-trap"',
        'class="fr-btn--close fr-btn" tabindex="-1">Fermer',
        'class="fr-btn demo-modal-trap-target">Confirmer la publication',
    )
    for variant in ("site-inaccessible", "site-aide-correction"):
        text = (DOCS / variant / "ec06-keyboard-focus.html").read_text(encoding="utf-8")
        for snippet in ec06_bad_snippets:
            if snippet not in text:
                ec06_errors.append(f"{variant}/ec06-keyboard-focus.html: piège clavier attendu absent: {snippet}")

    accessible_ec06 = (DOCS / "site-accessible" / "ec06-keyboard-focus.html").read_text(encoding="utf-8")
    if 'tabindex="-1">Publier la session' in accessible_ec06:
        ec06_errors.append("site-accessible/ec06-keyboard-focus.html: le bouton Publier ne doit pas être retiré de l'ordre de tabulation")
    if 'href="ec12-form-labels.html" tabindex="-1"' in accessible_ec06:
        ec06_errors.append("site-accessible/ec06-keyboard-focus.html: le lien Vérifier le formulaire doit rester dans l'ordre de tabulation")
    if 'href="#participants-notification" tabindex="-1"' in accessible_ec06:
        ec06_errors.append("site-accessible/ec06-keyboard-focus.html: le lien Prévenir les participants doit rester dans l'ordre de tabulation")
    if "demo-modal-keyboard-trap" in accessible_ec06:
        ec06_errors.append("site-accessible/ec06-keyboard-focus.html: la modale corrigée ne doit pas contenir le piège clavier")
    if ec06_errors:
        details = "\n".join(ec06_errors[:30])
        raise ValueError(f"Contrôles spécifiques EC06 en échec:\n{details}")


def main() -> None:
    contract_pages = validate_contract()
    validate_docs(contract_pages)
    print("OK validation points de contrôle rapides")


if __name__ == "__main__":
    main()
