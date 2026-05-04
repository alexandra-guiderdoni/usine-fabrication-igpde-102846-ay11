#!/usr/bin/env python3
"""Generate the GitHub Pages skeleton for the Easy Checks exercise.

The YAML contract is the source of truth for pages, expected findings,
correction help, manifest and correction draft.
"""

from __future__ import annotations

import html
import shutil
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "03-easy-checks" / "evaluation_contract.yml"
DOCS_DIR = ROOT / "docs"
GRID_SOURCE = ROOT / "03-easy-checks" / "grille-audit-easy-checks.xlsx"
GRID_TARGET = DOCS_DIR / "assets" / "downloads" / "grille-audit-easy-checks.xlsx"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def load_contract() -> dict:
    with CONTRACT_PATH.open(encoding="utf-8") as handle:
        contract = yaml.safe_load(handle)
    pages = contract.get("pages", [])
    if len(pages) != 13:
        raise ValueError(f"Le contrat doit contenir 13 pages, trouvé: {len(pages)}")
    ids = [page["id"] for page in pages]
    if len(set(ids)) != len(ids):
        raise ValueError("Les identifiants de pages ne sont pas uniques")
    return contract


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def asset_prefix(depth: int) -> str:
    return "/".join([".."] * depth + ["assets"])


def dsfr_head(title: str, depth: int) -> str:
    assets = asset_prefix(depth)
    return f"""<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <link rel="stylesheet" href="{assets}/dsfr/dsfr.min.css">
  <link rel="stylesheet" href="{assets}/dsfr/utility/utility.min.css">
  <link rel="stylesheet" href="{assets}/site.css">
</head>"""


def skiplinks(depth: int) -> str:
    return f"""<div class="fr-skiplinks">
  <nav role="navigation" class="fr-container" aria-label="Accès rapide">
    <ul class="fr-skiplinks__list">
      <li><a class="fr-link" href="#contenu">Aller au contenu</a></li>
      <li><a class="fr-link" href="#navigation-principale">Aller au menu principal</a></li>
      <li><a class="fr-link" href="#footer">Aller au pied de page</a></li>
    </ul>
  </nav>
</div>"""


def header(contract: dict, depth: int, current: str = "") -> str:
    home = "../" * depth + "index.html"
    nav_items = [
        ("Accueil", home, "home"),
        ("Site à auditer", "../" * depth + "site-inaccessible/index.html", "inaccessible"),
        ("Aide à la correction", "../" * depth + "site-aide-correction/index.html", "help"),
        ("Site corrigé", "../" * depth + "site-accessible/index.html", "accessible"),
    ]
    links = "\n".join(
        f"""        <li class="fr-nav__item"><a class="fr-nav__link" href="{href}"{(' aria-current="page"' if key == current else '')}>{label}</a></li>"""
        for label, href, key in nav_items
    )
    return f"""{skiplinks(depth)}
<header role="banner" class="fr-header">
  <div class="fr-header__body">
    <div class="fr-container">
      <div class="fr-header__body-row">
        <div class="fr-header__brand fr-enlarge-link">
          <div class="fr-header__brand-top">
            <div class="fr-header__logo">
              <p class="fr-logo">République<br>Française</p>
            </div>
          </div>
          <div class="fr-header__service">
            <a href="{home}" title="Accueil - {esc(contract['site']['name'])}">
              <p class="fr-header__service-title">{esc(contract['site']['name'])}</p>
            </a>
            <p class="fr-header__service-tagline">{esc(contract['site']['baseline'])}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="fr-header__menu fr-modal" id="modal-menu">
    <div class="fr-container">
      <nav class="fr-nav" role="navigation" aria-label="Menu principal" id="navigation-principale">
        <ul class="fr-nav__list">
{links}
        </ul>
      </nav>
    </div>
  </div>
</header>"""


def footer(depth: int) -> str:
    home = "../" * depth + "index.html"
    plan = "../" * depth + "plan-du-site.html"
    accessibility = "../" * depth + "accessibilite.html"
    legal = "../" * depth + "mentions-legales.html"
    privacy = "../" * depth + "donnees-personnelles.html"
    return f"""<footer class="fr-footer" role="contentinfo" id="footer">
  <div class="fr-container">
    <div class="fr-footer__body">
      <div class="fr-footer__brand fr-enlarge-link">
        <p class="fr-logo">République<br>Française</p>
      </div>
      <div class="fr-footer__content">
        <p class="fr-footer__content-desc">Exercice pédagogique IGPDE sur les Easy Checks du W3C.</p>
        <ul class="fr-footer__content-list">
          <li class="fr-footer__content-item"><a class="fr-footer__content-link" href="{home}">Accueil</a></li>
          <li class="fr-footer__content-item"><a class="fr-footer__content-link" href="{home}#apres-exercice">Après l'exercice</a></li>
        </ul>
      </div>
    </div>
    <div class="fr-footer__bottom">
      <ul class="fr-footer__bottom-list">
        <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="{plan}">Plan du site</a></li>
        <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="{accessibility}">Accessibilité : non applicable - site pédagogique</a></li>
        <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="{legal}">Mentions légales</a></li>
        <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="{privacy}">Données personnelles</a></li>
      </ul>
    </div>
  </div>
</footer>"""


def scripts(depth: int) -> str:
    assets = asset_prefix(depth)
    return f"""<script type="module" src="{assets}/dsfr/dsfr.module.min.js"></script>
<script nomodule src="{assets}/dsfr/dsfr.nomodule.min.js"></script>"""


def page_shell(contract: dict, title: str, depth: int, main: str, current: str = "") -> str:
    return f"""<!doctype html>
<html lang="fr">
{dsfr_head(title, depth)}
<body>
{header(contract, depth, current)}
{main}
{footer(depth)}
{scripts(depth)}
</body>
</html>
"""


def page_card(page: dict, href: str) -> str:
    return f"""<div class="fr-col-12 fr-col-md-6 fr-col-lg-4">
  <div class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
      <div class="fr-card__content">
        <h3 class="fr-card__title"><a href="{href}">{page['number']}. {esc(page['title'])}</a></h3>
        <p class="fr-card__desc">{esc(page['easy_check']['name'])}</p>
        <p class="fr-card__detail">Easy Check {page['easy_check']['number']}</p>
      </div>
    </div>
  </div>
</div>"""


def generate_root(contract: dict) -> None:
    pages = contract["pages"]
    grid_size = "poids à vérifier avant publication"
    if GRID_SOURCE.exists():
        grid_size = f"{round(GRID_SOURCE.stat().st_size / 1024)} Ko"
    cards = "\n".join(page_card(page, f"site-inaccessible/{page['id']}.html") for page in pages)
    versions = [
        ("Site à auditer", "site-inaccessible/index.html", "Version inaccessible utilisée pendant l'exercice."),
        ("Aide à la correction", "site-aide-correction/index.html", "Même site avec indices en bas de page."),
        ("Site corrigé", "site-accessible/index.html", "Version accessible sobre, sans pédagogie visible."),
    ]
    version_cards = "\n".join(
        f"""<div class="fr-col-12 fr-col-md-4">
  <div class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
      <div class="fr-card__content">
        <h3 class="fr-card__title"><a href="{href}">{label}</a></h3>
        <p class="fr-card__desc">{desc}</p>
      </div>
    </div>
  </div>
</div>"""
        for label, href, desc in versions
    )
    main = f"""<main id="contenu" class="fr-container fr-py-6w">
  <h1>Exercice - Les 13 Easy Checks du W3C</h1>
  <div class="fr-alert fr-alert--info fr-mb-4w">
    <h2 class="fr-alert__title">Pré-diagnostic pédagogique</h2>
    <p>Cet exercice ne constitue pas un audit RGAA et ne permet pas de publier un taux de conformité.</p>
  </div>
  <section class="fr-mb-6w" aria-labelledby="versions-title">
    <h2 id="versions-title">Choisir une version du site</h2>
    <div class="fr-grid-row fr-grid-row--gutters">
{version_cards}
    </div>
  </section>
  <section class="fr-mb-6w" aria-labelledby="grille-title">
    <h2 id="grille-title">Grille d'audit</h2>
    <div class="fr-card fr-card--download fr-enlarge-link">
      <div class="fr-card__body">
        <div class="fr-card__content">
          <h3 class="fr-card__title"><a href="assets/downloads/grille-audit-easy-checks.xlsx" download>Télécharger la grille d'audit Easy Checks</a></h3>
          <p class="fr-card__desc">Classeur à remplir pendant l'exercice.</p>
          <p class="fr-card__detail">XLSX - {grid_size}</p>
        </div>
      </div>
    </div>
  </section>
  <section aria-labelledby="pages-title">
    <h2 id="pages-title">Pages à auditer</h2>
    <div class="fr-grid-row fr-grid-row--gutters">
{cards}
    </div>
  </section>
  <section id="apres-exercice" class="fr-mt-6w" aria-labelledby="after-title">
    <h2 id="after-title">Après l'exercice</h2>
    <ul>
      <li><a class="fr-link" href="manifest.md">Consulter le manifeste des erreurs injectées</a></li>
      <li><a class="fr-link" href="corrige-easy-checks.md">Consulter le corrigé Easy Checks</a></li>
    </ul>
  </section>
</main>"""
    write_text(DOCS_DIR / "index.html", page_shell(contract, "Exercice Easy Checks - Ministère de l'Accessibilité numérique", 0, main, "home"))


def generate_static_page(contract: dict, filename: str, title: str, body: str) -> None:
    main = f"""<main id="contenu" class="fr-container fr-py-6w">
  <h1>{esc(title)}</h1>
  <p>{esc(body)}</p>
</main>"""
    write_text(DOCS_DIR / filename, page_shell(contract, f"{title} - {contract['site']['name']}", 0, main, ""))


def generate_version_index(contract: dict, version_key: str, current: str) -> None:
    version = contract["versions"][version_key]
    pages = contract["pages"]
    cards = "\n".join(page_card(page, f"{page['id']}.html") for page in pages)
    main = f"""<main id="contenu" class="fr-container fr-py-6w">
  <h1>{esc(version['role'])}</h1>
  <p>Index généré depuis le contrat d'évaluation. Les contenus définitifs des pages seront produits à l'étape suivante.</p>
  <div class="fr-grid-row fr-grid-row--gutters">
{cards}
  </div>
</main>"""
    write_text(DOCS_DIR / version["path"] / "index.html", page_shell(contract, version["role"], 1, main, current))


def help_accordions(page: dict) -> str:
    panels = [
        ("Indice", page["help"]["hint"]),
        ("Ce qui pose problème", page["help"]["problem"]),
        ("Comment corriger", page["help"]["fix"]),
    ]
    sections = []
    for index, (title, text) in enumerate(panels, start=1):
        panel_id = f"{page['id']}-help-{index}"
        sections.append(
            f"""<section class="fr-accordion">
  <h3 class="fr-accordion__title">
    <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="{panel_id}">{esc(title)}</button>
  </h3>
  <div class="fr-collapse" id="{panel_id}">
    <p>{esc(text)}</p>
  </div>
</section>"""
        )
    return "\n".join(sections)


def generate_exercise_page(contract: dict, page: dict, version_key: str, current: str) -> None:
    version = contract["versions"][version_key]
    title = f"{page['title']} - {contract['site']['name']}"
    notice = ""
    if version_key == "help":
        notice = f"""<section class="fr-mt-6w" aria-labelledby="help-title">
  <h2 id="help-title">Aide à la correction</h2>
  <div class="fr-accordions-group">
{help_accordions(page)}
  </div>
</section>"""
    elif version_key == "inaccessible":
        notice = """<div class="fr-alert fr-alert--warning fr-mb-4w">
  <h2 class="fr-alert__title">Squelette de page</h2>
  <p>Le contenu inaccessible définitif sera produit à l'étape de fabrication de l'exercice.</p>
</div>"""
    main = f"""<main id="contenu" class="fr-container fr-py-6w">
  <nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">
    <button type="button" class="fr-breadcrumb__button" aria-expanded="false" aria-controls="breadcrumb">Voir le fil d'Ariane</button>
    <div class="fr-collapse" id="breadcrumb">
      <ol class="fr-breadcrumb__list">
        <li><a class="fr-breadcrumb__link" href="../index.html">Accueil</a></li>
        <li><a class="fr-breadcrumb__link" href="index.html">{esc(version['role'])}</a></li>
        <li><a class="fr-breadcrumb__link" aria-current="page">{esc(page['title'])}</a></li>
      </ol>
    </div>
  </nav>
  <h1>{page['number']}. {esc(page['title'])}</h1>
  {notice}
  <section aria-labelledby="content-title">
    <h2 id="content-title">Contenu ministériel à produire</h2>
    <p>{esc(page['realistic_context'])}</p>
  </section>
</main>"""
    write_text(DOCS_DIR / version["path"] / f"{page['id']}.html", page_shell(contract, title, 1, main, current))


def generate_manifest(contract: dict) -> None:
    rows = [
        "| Page | Easy Check | Erreur injectée | Outil de détection | Correction attendue | Aide associée |",
        "|---|---|---|---|---|---|",
    ]
    for page in contract["pages"]:
        rows.append(
            "| {number}. {title} | {easy} | {errors} | {tools} | {correction} | {help_text} |".format(
                number=page["number"],
                title=page["title"],
                easy=page["easy_check"]["name"],
                errors="<br>".join(page["inaccessible_errors"]),
                tools=", ".join(page["detection"]),
                correction=page["accessible_correction"],
                help_text="Indice / Problème / Comment corriger",
            )
        )
    content = "# Manifeste des erreurs injectées\n\nGénéré depuis `03-easy-checks/evaluation_contract.yml`.\n\n" + "\n".join(rows) + "\n"
    write_text(DOCS_DIR / "manifest.md", content)


def generate_correction(contract: dict) -> None:
    parts = ["# Corrigé Easy Checks\n", "Généré depuis `03-easy-checks/evaluation_contract.yml`.\n"]
    for page in contract["pages"]:
        parts.append(f"## {page['number']}. {page['title']}\n")
        parts.append(f"- Easy Check : {page['easy_check']['name']}")
        parts.append(f"- Constat minimal attendu : {page['expected_minimal_finding']}")
        parts.append(f"- Sévérité indicative : {page['severity']}")
        parts.append(f"- Preuve possible : {page['minimal_proof']}")
        parts.append(f"- Correction : {page['accessible_correction']}")
        parts.append(f"- Occurrences bonus : {' ; '.join(page['bonus_occurrences'])}")
        parts.append(f"- À ne pas pénaliser : {' ; '.join(page['do_not_penalize'])}\n")
    write_text(DOCS_DIR / "corrige-easy-checks.md", "\n".join(parts))


def generate_site_css() -> None:
    write_text(
        DOCS_DIR / "assets" / "site.css",
        """body {
  min-height: 100vh;
}

.fr-card__detail {
  word-break: normal;
}

.fr-breadcrumb {
  margin-bottom: 2rem;
}
""",
    )


def copy_grid() -> None:
    if GRID_SOURCE.exists():
        GRID_TARGET.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(GRID_SOURCE, GRID_TARGET)


def generate_media_readme(contract: dict) -> None:
    placeholders: list[str] = []
    external_sources: list[tuple[int, str, str, str, str]] = []
    for page in contract["pages"]:
        assets = page.get("assets", {})
        placeholders.extend(assets.get("placeholders", []))
        for key, source in assets.get("external_sources", {}).items():
            external_sources.append((page["number"], page["title"], key, source["title"], source["url"]))
    lines = ["# Médias à fournir", "", "Les vrais fichiers vidéo/audio remplaceront ces placeholders déclaratifs.", ""]
    for item in sorted(set(placeholders)):
        lines.append(f"- `{item}`")
    if external_sources:
        lines.extend(["", "## Sources externes de référence", ""])
        for number, page_title, key, source_title, url in external_sources:
            lines.append(f"- Page {number} - {page_title} - {key} : [{source_title}]({url})")
        lines.extend(
            [
                "",
                "Ne pas télécharger ni réhéberger ces sources sans vérification des droits.",
                "Elles servent de références pédagogiques ou seront remplacées par des fichiers locaux autorisés.",
            ]
        )
    write_text(DOCS_DIR / "assets" / "shared" / "media" / "README.md", "\n".join(lines) + "\n")


def main() -> None:
    contract = load_contract()
    generate_site_css()
    copy_grid()
    generate_media_readme(contract)
    generate_root(contract)
    generate_static_page(contract, "plan-du-site.html", "Plan du site", "Cette page liste les accès principaux de l'exercice.")
    generate_static_page(contract, "accessibilite.html", "Accessibilité", "Ce site est un support pédagogique. La version accessible de l'exercice vise la conformité des composants utilisés.")
    generate_static_page(contract, "mentions-legales.html", "Mentions légales", "Site fictif créé pour une formation IGPDE.")
    generate_static_page(contract, "donnees-personnelles.html", "Données personnelles", "Aucune donnée personnelle réelle n'est collectée dans cet exercice.")
    for key, current in (("inaccessible", "inaccessible"), ("help", "help"), ("accessible", "accessible")):
        generate_version_index(contract, key, current)
        for page in contract["pages"]:
            generate_exercise_page(contract, page, key, current)
    generate_manifest(contract)
    generate_correction(contract)
    print("OK docs skeleton generated from evaluation_contract.yml")


if __name__ == "__main__":
    main()
