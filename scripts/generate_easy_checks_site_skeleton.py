#!/usr/bin/env python3
"""Generate the GitHub Pages skeleton for the points de contrôle rapides exercise.

The YAML contract is the source of truth for pages, expected findings,
correction help, manifest and correction draft.
"""

from __future__ import annotations

import html
import re
import shutil
import unicodedata
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "03-easy-checks" / "evaluation_contract.yml"
DOCS_DIR = ROOT / "docs"
GRID_SOURCE = ROOT / "03-easy-checks" / "grille-audit-easy-checks.xlsx"
GRID_TARGET = DOCS_DIR / "assets" / "downloads" / "grille-audit-easy-checks.xlsx"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def esc_text(value: object) -> str:
    return html.escape(str(value), quote=False)


def slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    normalized = re.sub(r"[^a-zA-Z0-9]+", "-", normalized).strip("-").lower()
    return normalized or "section"


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
    content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
    path.write_text(content, encoding="utf-8")


def asset_prefix(depth: int) -> str:
    return "/".join([".."] * depth + ["assets"])


def dsfr_head(title: str, depth: int) -> str:
    assets = asset_prefix(depth)
    return f"""<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc_text(title)}</title>
  <link rel="stylesheet" href="{assets}/dsfr/dsfr.min.css">
  <link rel="stylesheet" href="{assets}/dsfr/utility/utility.min.css">
  <link rel="stylesheet" href="{assets}/site.css">
</head>"""


def skiplinks(depth: int, variant: str = "default") -> str:
    first_target = "#contenu-principal" if variant == "broken-content-anchor" else "#contenu"
    return f"""<div class="fr-skiplinks">
  <nav role="navigation" class="fr-container" aria-label="Accès rapide">
    <ul class="fr-skiplinks__list">
      <li><a class="fr-link" href="{first_target}">Aller au contenu</a></li>
      <li><a class="fr-link" href="#navigation-principale">Aller au menu principal</a></li>
      <li><a class="fr-link" href="#footer">Aller au pied de page</a></li>
    </ul>
  </nav>
</div>"""


def header(contract: dict, depth: int, current: str = "", skiplinks_variant: str = "default") -> str:
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
    return f"""{skiplinks(depth, skiplinks_variant)}
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
        <p class="fr-footer__content-desc">Exercice pédagogique IGPDE sur les points de contrôle rapides du W3C.</p>
        <ul class="fr-footer__content-list">
          <li class="fr-footer__content-item"><a class="fr-footer__content-link" href="{home}">Accueil</a></li>
          <li class="fr-footer__content-item"><a class="fr-footer__content-link" href="{home}#apres-exercice">Après l'exercice</a></li>
        </ul>
      </div>
    </div>
    <div class="fr-footer__bottom">
      <ul class="fr-footer__bottom-list">
        <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="{plan}">Plan du site</a></li>
        <li class="fr-footer__bottom-item"><a class="fr-footer__bottom-link" href="{accessibility}">Accessibilité : non conforme</a></li>
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


def breadcrumb(links: list[tuple[str, str]], current_label: str, collapse_id: str) -> str:
    items = "\n".join(
        f"""        <li><a class="fr-breadcrumb__link" href="{esc(href)}">{esc_text(label)}</a></li>"""
        for label, href in links
    )
    return f"""<div class="fr-container">
  <nav role="navigation" class="fr-breadcrumb fr-mt-3w" aria-label="vous êtes ici :">
    <button type="button" class="fr-breadcrumb__button" aria-expanded="false" aria-controls="{esc(collapse_id)}">Voir le fil d'Ariane</button>
    <div class="fr-collapse" id="{esc(collapse_id)}">
      <ol class="fr-breadcrumb__list">
{items}
        <li><a class="fr-breadcrumb__link" aria-current="page">{esc_text(current_label)}</a></li>
      </ol>
    </div>
  </nav>
</div>"""


def page_shell(
    contract: dict,
    title: str,
    depth: int,
    main: str,
    current: str = "",
    html_lang: str = "fr",
    skiplinks_variant: str = "default",
) -> str:
    return f"""<!doctype html>
<html lang="{esc(html_lang)}">
{dsfr_head(title, depth)}
<body>
{header(contract, depth, current, skiplinks_variant)}
{main}
{footer(depth)}
{scripts(depth)}
</body>
</html>
"""


def content_column(content: str) -> str:
    return f"""<div class="fr-grid-row">
  <div class="fr-col-12 fr-col-md-8">
{content}
  </div>
</div>"""


def page_card(page: dict, href: str) -> str:
    return f"""<div class="fr-col-12 fr-col-md-6 fr-col-lg-4">
  <div class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
      <div class="fr-card__content">
        <h3 class="fr-card__title"><a href="{href}">{page['number']}. {esc(page['title'])}</a></h3>
        <p class="fr-card__desc">{esc(page['easy_check']['name'])}</p>
        <p class="fr-card__detail">Point de contrôle rapide {page['easy_check']['number']}</p>
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
        ("Aide à la correction", "site-aide-correction/index.html", "Même site avec indices en haut de page."),
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
    content = f"""  <h1>Exercice - Les 13 points de contrôle rapides du W3C</h1>
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
          <h3 class="fr-card__title"><a href="assets/downloads/grille-audit-easy-checks.xlsx" download>Télécharger la grille d'audit des points de contrôle rapides</a></h3>
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
      <li><a class="fr-link" href="corrige-easy-checks.md">Consulter le corrigé des points de contrôle rapides</a></li>
    </ul>
  </section>"""
    page_breadcrumb = breadcrumb([], "Accueil", "breadcrumb-accueil")
    main = f"""{page_breadcrumb}
<main id="contenu" class="fr-container fr-py-6w">
{content_column(content)}
</main>"""
    write_text(DOCS_DIR / "index.html", page_shell(contract, "Exercice points de contrôle rapides - Ministère de l'Accessibilité numérique", 0, main, "home"))


def generate_static_page(contract: dict, filename: str, title: str, body: str) -> None:
    content = f"""  <h1>{esc(title)}</h1>
  <p>{esc(body)}</p>"""
    page_breadcrumb = breadcrumb([("Accueil", "index.html")], title, f"breadcrumb-{slug(title)}")
    main = f"""{page_breadcrumb}
<main id="contenu" class="fr-container fr-py-6w">
{content_column(content)}
</main>"""
    write_text(DOCS_DIR / filename, page_shell(contract, f"{title} - {contract['site']['name']}", 0, main, ""))


def sitemap_items(pages: list[dict], prefix: str) -> str:
    return "\n".join(
        f"""      <li><a class="fr-link" href="{esc(prefix)}{page['id']}.html">{esc_text(page['title'])}</a></li>"""
        for page in pages
    )


def generate_sitemap_page(contract: dict) -> None:
    pages = contract["pages"]
    sections = [
        ("sitemap-inaccessible", "Site à auditer", "Accueil du site à auditer", "site-inaccessible/"),
        ("sitemap-help", "Site d'aide à la correction", "Accueil du site d'aide à la correction", "site-aide-correction/"),
        ("sitemap-accessible", "Site corrigé", "Accueil du site corrigé", "site-accessible/"),
    ]
    exercise_sections = "\n".join(
        f"""  <section class="fr-mb-5w" aria-labelledby="{section_id}">
    <h2 id="{section_id}">{esc_text(label)}</h2>
    <p><a class="fr-link" href="{esc(path)}index.html">{esc_text(home_label)}</a></p>
    <h3>Pages de l'exercice</h3>
    <ol>
{sitemap_items(pages, path)}
    </ol>
  </section>"""
        for section_id, label, home_label, path in sections
    )
    content = f"""  <h1 id="sitemap-title">Plan du site</h1>
  <p>Les pages sont regroupées selon les trois versions de l'exercice afin de retrouver rapidement la page à auditer, son aide ou sa version corrigée.</p>
  <nav aria-labelledby="sitemap-title">
    <section class="fr-mb-5w" aria-labelledby="sitemap-general">
      <h2 id="sitemap-general">Pages générales</h2>
      <ul>
        <li><a class="fr-link" href="index.html">Accueil</a></li>
        <li><a class="fr-link" href="plan-du-site.html">Plan du site</a></li>
        <li><a class="fr-link" href="assets/downloads/grille-audit-easy-checks.xlsx">Grille d'audit des points de contrôle rapides</a></li>
        <li><a class="fr-link" href="manifest.md">Manifeste des erreurs injectées</a></li>
        <li><a class="fr-link" href="corrige-easy-checks.md">Corrigé des points de contrôle rapides</a></li>
        <li><a class="fr-link" href="accessibilite.html">Accessibilité</a></li>
        <li><a class="fr-link" href="mentions-legales.html">Mentions légales</a></li>
        <li><a class="fr-link" href="donnees-personnelles.html">Données personnelles</a></li>
      </ul>
    </section>
{exercise_sections}
  </nav>"""
    page_breadcrumb = breadcrumb([("Accueil", "index.html")], "Plan du site", "breadcrumb-plan-du-site")
    main = f"""{page_breadcrumb}
<main id="contenu" class="fr-container fr-py-6w">
{content_column(content)}
</main>"""
    write_text(
        DOCS_DIR / "plan-du-site.html",
        page_shell(contract, f"Plan du site - {contract['site']['name']}", 0, main, ""),
    )


def generate_version_index(contract: dict, version_key: str, current: str) -> None:
    version = contract["versions"][version_key]
    pages = contract["pages"]
    cards = "\n".join(page_card(page, f"{page['id']}.html") for page in pages)
    content = f"""  <h1>{esc(version['role'])}</h1>
  <p>Index généré depuis le contrat d'évaluation. Chaque page cible un Point de contrôle rapide et une erreur principale.</p>
  <div class="fr-grid-row fr-grid-row--gutters">
{cards}
  </div>"""
    page_breadcrumb = breadcrumb([("Accueil", "../index.html")], version["role"], f"breadcrumb-{slug(version['role'])}")
    main = f"""{page_breadcrumb}
<main id="contenu" class="fr-container fr-py-6w">
{content_column(content)}
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
        findings = ""
        if title == "Ce qui pose problème" and page["help"].get("findings"):
            items = "\n".join(f"      <li>{esc(item)}</li>" for item in page["help"]["findings"])
            intro = page["help"].get("findings_intro", "Les erreurs à trouver sont :")
            findings = f"""
    <p>{esc(intro)}</p>
    <ul>
{items}
    </ul>"""
        fixes = ""
        if title == "Comment corriger" and page["help"].get("fixes"):
            items = "\n".join(f"      <li>{esc(item)}</li>" for item in page["help"]["fixes"])
            intro = page["help"].get("fixes_intro", "Messages de correction ciblés :")
            fixes = f"""
    <p>{esc(intro)}</p>
    <ul>
{items}
    </ul>"""
        extra = f"{findings}{fixes}"
        sections.append(
            f"""<section class="fr-accordion">
  <h3 class="fr-accordion__title">
    <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="{panel_id}">{esc(title)}</button>
  </h3>
  <div class="fr-collapse" id="{panel_id}">
    <p>{esc(text)}</p>{extra}
  </div>
</section>"""
        )
    return "\n".join(sections)


def youtube_media_block(source: dict, heading: str) -> str:
    title = source["title"]
    url = source["url"]
    embed_url = source.get("embed_url", url)
    role = source.get("role", "")
    heading_id = slug(heading)
    return f"""<section class="fr-mb-4w" aria-labelledby="{heading_id}">
  <h2 id="{heading_id}">{esc(heading)}</h2>
  <figure class="fr-content-media" role="group" aria-label="{esc(title)}">
    <div class="fr-content-media__img">
      <iframe class="fr-responsive-vid" src="{esc(embed_url)}" title="{esc(title)}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
    <figcaption class="fr-content-media__caption">
      {esc(role)}
      <br>
      <a class="fr-link" href="{esc(url)}" rel="external">Ouvrir la vidéo sur YouTube</a>
    </figcaption>
  </figure>
</section>"""


def card(title: str, href: str, desc: str, detail: str = "") -> str:
    detail_html = f'\n        <p class="fr-card__detail">{esc(detail)}</p>' if detail else ""
    return f"""<div class="fr-col-12 fr-col-md-6 fr-col-lg-4">
  <div class="fr-card fr-enlarge-link">
    <div class="fr-card__body">
      <div class="fr-card__content">
        <h3 class="fr-card__title"><a href="{esc(href)}">{esc(title)}</a></h3>
        <p class="fr-card__desc">{esc(desc)}</p>{detail_html}
      </div>
    </div>
  </div>
</div>"""


def callout(title: str, text: str, heading_level: int = 2) -> str:
    return f"""<div class="fr-callout fr-mb-4w">
  <h{heading_level} class="fr-callout__title">{esc(title)}</h{heading_level}>
  <p class="fr-callout__text">{esc(text)}</p>
</div>"""


def placeholder_media(label: str) -> str:
    return f"""<div class="demo-media-placeholder" aria-hidden="true">
  <span>{esc(label)}</span>
</div>"""


def transcript_component(identifier: str, title: str, paragraphs: list[str]) -> str:
    collapse_id = f"{identifier}-collapse"
    modal_id = f"{identifier}-modal"
    title_id = f"{identifier}-modal-title"
    body = "\n".join(f"              <p>{esc(paragraph)}</p>" for paragraph in paragraphs)
    return f"""<div class="fr-transcription fr-mt-3w">
  <button type="button" class="fr-transcription__btn" aria-expanded="false" aria-controls="{collapse_id}">Transcription</button>
  <div class="fr-collapse" id="{collapse_id}">
    <div class="fr-transcription__footer">
      <div class="fr-transcription__actions-group">
        <button aria-controls="{modal_id}" aria-label="Agrandir la transcription" data-fr-opened="false" type="button" class="fr-btn fr-btn--fullscreen">Agrandir</button>
      </div>
    </div>
    <dialog id="{modal_id}" class="fr-modal" aria-labelledby="{title_id}">
      <div class="fr-container fr-container--fluid fr-container-md">
        <div class="fr-grid-row fr-grid-row--center">
          <div class="fr-col-12 fr-col-md-10 fr-col-lg-8">
            <div class="fr-modal__body">
              <div class="fr-modal__header">
                <button aria-controls="{modal_id}" title="Fermer" type="button" class="fr-btn fr-btn--close">Fermer</button>
              </div>
              <div class="fr-modal__content">
                <h1 id="{title_id}" class="fr-modal__title">{esc(title)}</h1>
{body}
              </div>
            </div>
          </div>
        </div>
      </div>
    </dialog>
  </div>
</div>"""


def search_bar() -> str:
    return """<form class="demo-search-form fr-mb-4w" role="search" action="ec02-page-title.html" method="get" aria-labelledby="search-form-title">
  <h3 id="search-form-title">Modifier la recherche</h3>
  <div class="fr-search-bar fr-mb-3w">
    <label class="fr-label" for="search-rgaa">Rechercher une ressource RGAA</label>
    <input class="fr-input" placeholder="Exemple : contrastes" type="search" id="search-rgaa" name="q" value="RGAA">
    <button class="fr-btn" type="submit" title="Rechercher une ressource RGAA">Rechercher</button>
  </div>
  <div class="fr-grid-row fr-grid-row--gutters">
    <div class="fr-col-12 fr-col-md-6">
      <div class="fr-select-group">
        <label class="fr-label" for="search-sort">Trier les résultats</label>
        <select class="fr-select" id="search-sort" name="tri">
          <option value="pertinence" selected>Par pertinence</option>
          <option value="date">Par date de publication</option>
        </select>
      </div>
    </div>
  </div>
  <input type="hidden" name="page" value="1">
</form>"""


def form_label_content(accessible: bool) -> str:
    if not accessible:
        return """<section aria-labelledby="content-title">
  <h2 id="content-title">S'inscrire au webinaire RGAA</h2>
  <form action="ec12-form-labels.html" method="post" class="demo-form">
    <div class="fr-input-group">
      <input class="fr-input" type="text" name="nom" placeholder="Nom de famille">
    </div>
    <div class="fr-input-group">
      <label class="fr-label">Adresse électronique</label>
      <input class="fr-input" type="email" name="email">
    </div>
    <p class="fr-label">Format de participation</p>
    <div class="fr-radio-group">
      <input type="radio" id="format-distanciel" name="format" value="distanciel">
      <label class="fr-label" for="format-distanciel">À distance</label>
    </div>
    <div class="fr-radio-group">
      <input type="radio" id="format-presentiel" name="format" value="presentiel">
      <label class="fr-label" for="format-presentiel">Sur site</label>
    </div>
    <p class="fr-label">Thématiques souhaitées</p>
    <div class="fr-checkbox-group">
      <input type="checkbox" id="theme-images" name="theme" value="images">
      <label class="fr-label" for="theme-images">Images</label>
    </div>
    <div class="fr-checkbox-group">
      <input type="checkbox" id="theme-formulaires" name="theme" value="formulaires">
      <label class="fr-label" for="theme-formulaires">Formulaires</label>
    </div>
    <button class="fr-btn" type="submit">Confirmer l'inscription</button>
  </form>
</section>"""
    return """<section aria-labelledby="content-title">
  <h2 id="content-title">S'inscrire au webinaire RGAA</h2>
  <form action="ec12-form-labels.html" method="post" class="demo-form">
    <div class="fr-input-group">
      <label class="fr-label" for="nom">Nom de famille</label>
      <input class="fr-input" type="text" id="nom" name="nom" autocomplete="family-name">
    </div>
    <div class="fr-input-group">
      <label class="fr-label" for="email">Adresse électronique
        <span class="fr-hint-text">Format attendu : nom@domaine.fr</span>
      </label>
      <input class="fr-input" type="email" id="email" name="email" autocomplete="email" aria-describedby="email-hint">
      <p id="email-hint" class="fr-hint-text">Utilisée uniquement pour confirmer l'inscription.</p>
    </div>
    <fieldset class="fr-fieldset">
      <legend class="fr-fieldset__legend">Format de participation</legend>
      <div class="fr-fieldset__element">
        <div class="fr-radio-group">
          <input type="radio" id="format-distanciel" name="format" value="distanciel">
          <label class="fr-label" for="format-distanciel">À distance</label>
        </div>
      </div>
      <div class="fr-fieldset__element">
        <div class="fr-radio-group">
          <input type="radio" id="format-presentiel" name="format" value="presentiel">
          <label class="fr-label" for="format-presentiel">Sur site</label>
        </div>
      </div>
    </fieldset>
    <fieldset class="fr-fieldset">
      <legend class="fr-fieldset__legend">Thématiques souhaitées</legend>
      <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
          <input type="checkbox" id="theme-images" name="theme" value="images">
          <label class="fr-label" for="theme-images">Images</label>
        </div>
      </div>
      <div class="fr-fieldset__element">
        <div class="fr-checkbox-group">
          <input type="checkbox" id="theme-formulaires" name="theme" value="formulaires">
          <label class="fr-label" for="theme-formulaires">Formulaires</label>
        </div>
      </div>
    </fieldset>
    <button class="fr-btn" type="submit">Confirmer l'inscription au webinaire</button>
  </form>
</section>"""


def required_errors_content(accessible: bool) -> str:
    if not accessible:
        return """<section aria-labelledby="content-title">
  <h2 id="content-title">Demander un accompagnement</h2>
  <p>Les champs avec une bordure rouge doivent être complétés.</p>
  <div class="fr-alert fr-alert--error fr-mb-3w">
    <h3 class="fr-alert__title">Erreur de saisie</h3>
    <p>Format invalide.</p>
  </div>
  <form action="ec13-required-errors.html" method="post" class="demo-form">
    <div class="fr-input-group">
      <label class="fr-label" for="service-ko">Service <span class="demo-red">*</span></label>
      <input class="fr-input demo-red-border" type="text" id="service-ko" name="service">
    </div>
    <div class="fr-input-group">
      <label class="fr-label" for="date-ko">Date souhaitée <span class="demo-red">*</span></label>
      <input class="fr-input demo-red-border" type="text" id="date-ko" name="date" value="32/14/2026">
      <p class="fr-error-text">Format invalide.</p>
    </div>
    <button class="fr-btn" type="submit">Envoyer</button>
  </form>
</section>"""
    return """<section aria-labelledby="content-title">
  <h2 id="content-title">Demander un accompagnement</h2>
  <p>Tous les champs sont obligatoires, sauf mention contraire.</p>
  <div class="fr-alert fr-alert--error fr-mb-3w" role="alert" tabindex="-1">
    <h3 class="fr-alert__title">Erreur : deux champs sont à corriger</h3>
    <ul>
      <li><a class="fr-link" href="#service">Indiquer le service demandeur</a></li>
      <li><a class="fr-link" href="#date">Saisir une date au format JJ/MM/AAAA</a></li>
    </ul>
  </div>
  <form action="ec13-required-errors.html" method="post" class="demo-form" novalidate>
    <div class="fr-input-group fr-input-group--error">
      <label class="fr-label" for="service">Service demandeur</label>
      <input class="fr-input" type="text" id="service" name="service" required aria-invalid="true" aria-describedby="service-error">
      <p id="service-error" class="fr-error-text">Erreur : le service demandeur est obligatoire.</p>
    </div>
    <div class="fr-input-group fr-input-group--error">
      <label class="fr-label" for="date">Date souhaitée
        <span class="fr-hint-text">Exemple : 15/06/2026.</span>
      </label>
      <input class="fr-input" type="text" id="date" name="date" required aria-invalid="true" aria-describedby="date-error" value="32/14/2026">
      <p id="date-error" class="fr-error-text">Erreur : la date doit respecter le format JJ/MM/AAAA.</p>
    </div>
    <button class="fr-btn" type="submit">Envoyer la demande d'accompagnement</button>
  </form>
</section>"""


def content_ec01(version_key: str) -> str:
    accessible = version_key == "accessible"
    if accessible:
        informative = '<img class="demo-informative-image" src="../assets/shared/images/schema-rgaa.svg" alt="Schéma : vérifier, corriger puis publier une ressource accessible.">'
        decorative = '<img src="../assets/shared/images/motif-hexagones.svg" alt="">'
        email_link = '<a class="fr-link demo-contact-link" href="mailto:contact@accessibilite-numerique.gouv.fr"><img src="../assets/shared/images/contact.svg" alt="Envoyer un courriel au ministère"></a>'
        sms_link = '<a class="fr-link demo-contact-link" href="sms:+33123456789"><img src="../assets/shared/images/sms.svg" alt=""> Envoyer un SMS</a>'
    else:
        informative = '<img class="demo-informative-image" src="../assets/shared/images/schema-rgaa.svg">'
        decorative = '<img src="../assets/shared/images/motif-hexagones.svg" alt="Long séparateur horizontal bleu composé de deux traits et d\'un losange central décoratif pour séparer la rubrique de contact du contenu précédent">'
        email_link = '<a class="fr-link demo-contact-link" href="mailto:contact@accessibilite-numerique.gouv.fr"><img src="../assets/shared/images/contact.svg" alt="Dessin d\'une enveloppe"></a>'
        sms_link = '<a class="fr-link demo-contact-link" href="sms:+33123456789"><img src="../assets/shared/images/sms.svg" alt="Dessin d\'un téléphone"> Envoyer un SMS</a>'
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Vérifier l'accessibilité d'une page avant publication</h2>
  <p>Le ministère publie une méthodologie courte fondée sur le RGAA (Référentiel général d'amélioration de l'accessibilité). Elle s'adresse aux équipes qui contrôlent une page avant publication. La page présente les repères utiles pour vérifier rapidement une ressource.</p>
  <div class="fr-grid-row fr-grid-row--gutters demo-image-check">
    <div class="fr-col-12 demo-image-check__item">
      <p>Le schéma ci-dessous présente les trois étapes proposées aux équipes éditoriales. Il sert à comprendre l'ordre des actions à mener. Chaque étape correspond à un moment concret du travail de publication.</p>
      {informative}
      <p>Cette démarche sert de repère pour vérifier une ressource avant publication. Elle aide l'équipe à passer de l'audit à la mise en ligne. Le visuel résume donc une information que le texte seul ne détaille pas entièrement.</p>
    </div>
    <div class="fr-col-12 demo-image-check__item">
      <p>La rubrique suivante présente le contact utile pour les questions sur la méthodologie. Un séparateur visuel introduit ce changement de sujet. Il ne porte pas d'information nécessaire à la compréhension du contenu.</p>
      <div class="demo-separator-image">{decorative}</div>
      <p>Le séparateur visuel marque le passage vers les informations de contact. Il donne simplement un rythme à la lecture de la page. La même information reste compréhensible si ce motif n'est pas restitué.</p>
    </div>
    <div class="fr-col-12 demo-image-check__contact">
      <h3>Nous contacter</h3>
      <p>Moyens pour nous contacter :</p>
      <ul class="demo-contact-list">
        <li>Par courriel : {email_link}</li>
        <li>Par SMS : {sms_link}</li>
      </ul>
      <p>Utilisez ces liens pour poser une question sur cette méthodologie. Le courriel illustre un lien image pur. Le SMS illustre un lien composite avec une icône et un texte visible.</p>
      <p>Une réponse est apportée par l'équipe chargée de la ressource. Les demandes sont traitées pendant les jours ouvrés. Les informations transmises permettent d'orienter la demande vers le bon interlocuteur.</p>
    </div>
  </div>
</section>"""


def content_ec02(version_key: str) -> str:
    cards = "\n".join(
        [
            card("Guide RGAA pour les contributeurs", "ec03-headings.html", "Comprendre la structure d'une page avant publication.", "Résultat 4 sur 9"),
            card("Contrastes et charte éditoriale", "ec04-contrast.html", "Repérer les textes difficiles à lire.", "Résultat 5 sur 9"),
            card("Formulaires de contact", "ec12-form-labels.html", "Contrôler les étiquettes et les groupes de champs.", "Résultat 6 sur 9"),
        ]
    )
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Résultats de recherche pour « RGAA »</h2>
  {search_bar()}
  <p id="search-results-summary" role="status" aria-live="polite">9 résultats trouvés pour « RGAA ». Page 2 sur 3. 3 résultats affichés par page, résultats 4 à 6. Tri : pertinence.</p>
  <div class="fr-grid-row fr-grid-row--gutters">
{cards}
  </div>
  <nav role="navigation" class="fr-pagination fr-mt-4w" aria-label="Pagination des résultats de recherche">
    <ul class="fr-pagination__list">
      <li><a class="fr-pagination__link" href="ec02-page-title.html?q=RGAA&amp;tri=pertinence&amp;page=1">Page 1</a></li>
      <li><a class="fr-pagination__link" aria-current="page">Page 2</a></li>
      <li><a class="fr-pagination__link" href="ec02-page-title.html?q=RGAA&amp;tri=pertinence&amp;page=3">Page 3</a></li>
    </ul>
  </nav>
</section>"""


def content_ec03(version_key: str) -> str:
    if version_key == "accessible":
        return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Comprendre le RGAA</h2>
  <p>Le RGAA aide les équipes à vérifier qu'un service numérique reste utilisable par le plus grand nombre. Les titres structurent la page et permettent de parcourir rapidement ses grandes parties.</p>
  <h3>Utiliser les titres pour parcourir la page</h3>
  <p>Un texte qui introduit une nouvelle partie doit être balisé comme un vrai titre. Cette structuration sert autant aux lecteurs d'écran qu'aux outils qui affichent le plan de la page.</p>
  <h3>Prioriser une publication urgente</h3>
  <p><strong>Publication urgente avant vendredi :</strong> cette information est une mise en avant éditoriale. Elle reste dans un paragraphe, car elle ne titre pas une nouvelle rubrique.</p>
  <h2>Ressources</h2>
  <h3>Guides pratiques</h3>
  <p>Les ressources ci-dessous aident les contributeurs à vérifier les titres, les images et les formulaires avant publication.</p>
  <ul>
    <li><a class="fr-link" href="ec01-images.html">Images et alternatives</a></li>
    <li><a class="fr-link" href="ec12-form-labels.html">Formulaires accessibles</a></li>
  </ul>
  <h3>Points de vigilance</h3>
  <p>Le gabarit conserve ses repères de navigation : accès rapides, zones principales et fil d'Ariane. Ces éléments sont utiles, mais ils ne remplacent pas un plan de titres cohérent dans le contenu.</p>
  {callout("Point d'attention", "Un saut de niveau peut dégrader la lisibilité du plan sans constituer à lui seul la non-conformité principale de cet exercice.", 3)}
</section>"""
    return """<section aria-labelledby="content-title">
  <h2 id="content-title">Guide du RGAA</h2>
  <p class="demo-fake-heading">Comprendre le RGAA</p>
  <p>Le RGAA aide les équipes à vérifier qu'un service numérique reste utilisable par le plus grand nombre. Les contributeurs peuvent l'utiliser pour préparer une publication avant sa mise en ligne.</p>
  <p class="demo-fake-heading">Avant de publier</p>
  <p>Cette page rassemble les premiers repères à contrôler sur une ressource ministérielle. Elle sert aussi à orienter les demandes vers les bons interlocuteurs.</p>
  <h3 class="demo-heading-as-emphasis">Publication urgente avant vendredi</h3>
  <p>La ressource de référence doit être relue par l'équipe publication. Les remarques sont centralisées dans le tableau de suivi partagé.</p>
  <p>Les équipes éditoriales signalent les points bloquants avant l'envoi en validation. Les corrections mineures peuvent être intégrées dans la prochaine mise à jour.</p>
  <h2>Ressources</h2>
  <p class="demo-fake-heading">Ressources pour les contributeurs</p>
  <h4>Guides pratiques</h4>
  <p>Les guides pratiques décrivent les contrôles à réaliser avant publication. Ils présentent les points à vérifier sur les images, les formulaires et les contenus multimédias.</p>
  <h1>Repères déjà présents</h1>
  <p>La page propose des accès rapides, un fil d'Ariane, une navigation principale et un pied de page. Ces repères aident les utilisateurs à comprendre où ils se trouvent dans le site.</p>
  <p class="demo-fake-heading">À retenir pour l'équipe</p>
  <p>Les vérifications doivent rester simples à partager. Le responsable de publication conserve la trace des corrections effectuées avant la mise en ligne.</p>
</section>"""


def contrast_tools_links() -> str:
    return """<section aria-labelledby="contrast-tools-title" class="fr-mt-4w">
  <h3 id="contrast-tools-title">Outils pour vérifier les contrastes</h3>
  <p>Utilisez ces outils pour mesurer le ratio entre le texte et son arrière-plan. Pour ce test, cherchez en priorité les textes courants sous 4,5:1 et les gros textes, composants ou informations visuelles sous 3:1.</p>
  <ul>
    <li><a class="fr-link" href="https://addons.mozilla.org/en-US/firefox/addon/wcag-contrast-checker/" rel="external">WCAG Contrast Checker pour Firefox</a></li>
    <li><a class="fr-link" href="https://chromewebstore.google.com/detail/wcag-color-contrast-check/plnahcmalebffmaghcpcmpaciebdhgdf" rel="external">WCAG Color Contrast Check pour Chrome</a></li>
    <li><a class="fr-link" href="https://vispero.com/lp/color-contrast-checker/" rel="external">Color Contrast Checker de Vispero</a></li>
  </ul>
</section>"""


def content_ec04(version_key: str) -> str:
    if version_key == "accessible":
        return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Charte de publication</h2>
  <p>Les contenus publiés utilisent les couleurs et composants DSFR sans surcharge de contraste.</p>
  <div class="fr-alert fr-alert--success fr-mb-3w">
    <h3 class="fr-alert__title">Succès : charte validée</h3>
    <p>Le statut est indiqué par le texte et pas uniquement par la couleur.</p>
  </div>
  <p><a class="fr-link" href="ec03-headings.html">Consulter la structure des titres</a></p>
  <button class="fr-btn" type="button">Valider la publication</button>
  {contrast_tools_links()}
</section>"""
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Charte de publication</h2>
  <p class="demo-low-contrast">Les contenus doivent rester faciles à lire sur tous les écrans.</p>
  <p><a class="fr-link demo-pale-link" href="ec03-headings.html">Consulter la structure des titres</a></p>
  <p><button class="fr-btn demo-pale-action" type="button">Valider la publication</button></p>
  <p><span class="fr-badge demo-status-dot">Validé</span></p>
  {contrast_tools_links()}
</section>"""


def content_ec05(version_key: str) -> str:
    return """<section aria-labelledby="content-title">
  <h2 id="content-title">Accéder rapidement aux services</h2>
  <p>Cette page regroupe les accès les plus utilisés par les équipes de publication. Elle permet de rejoindre les ressources utiles, de consulter les contacts de référence et de retrouver les actions liées à la préparation d'une session.</p>
  <section aria-labelledby="services-title" class="fr-mt-4w">
    <h3 id="services-title">Services concernés</h3>
    <p>Les contenus sont préparés par plusieurs équipes avant leur mise en ligne. Chaque service conserve son périmètre, mais les informations doivent rester faciles à atteindre depuis une même page.</p>
    <ul>
      <li>Équipe éditoriale : vérification des contenus et des titres.</li>
      <li>Équipe formation : préparation des ressources à transmettre aux participants.</li>
      <li>Équipe support : réponse aux questions reçues après publication.</li>
    </ul>
  </section>
  <section aria-labelledby="resources-title" class="fr-mt-4w">
    <h3 id="resources-title">Ressources à consulter</h3>
    <p>Ces liens donnent accès aux ressources les plus fréquentes pendant la préparation. Les actions principales sont regroupées pour limiter les allers-retours entre l'en-tête, le contenu et le pied de page.</p>
    <div class="fr-grid-row fr-grid-row--gutters">
      <div class="fr-col-12 fr-col-md-4"><button class="fr-btn" type="button">Ouvrir les ressources</button></div>
      <div class="fr-col-12 fr-col-md-4"><a class="fr-link" href="ec06-keyboard-focus.html">Voir le parcours clavier</a></div>
      <div class="fr-col-12 fr-col-md-4"><a class="fr-link" href="#footer">Aller au pied de page</a></div>
    </div>
  </section>
  <section aria-labelledby="actions-title" class="fr-mt-4w">
    <h3 id="actions-title">Actions disponibles</h3>
    <p>Avant la diffusion, l'équipe peut relire la page, ouvrir les ressources associées et transmettre les corrections attendues. Les contributeurs doivent pouvoir rejoindre rapidement la zone utile sans relire l'ensemble de l'en-tête à chaque passage.</p>
  </section>
</section>"""


def content_ec06(version_key: str) -> str:
    class_attr = ' class="demo-no-focus"' if version_key != "accessible" else ""
    cards = "\n".join(
        [
            card("Guide des titres", "ec03-headings.html", "Repères pour structurer une page de publication."),
            card("Formulaire d'inscription", "ec12-form-labels.html", "Contrôle des champs et des libellés avant mise en ligne."),
            card("Accès rapides", "ec05-skiplinks.html", "Vérification des raccourcis placés en début de page."),
        ]
    )
    return f"""<section{class_attr} aria-labelledby="content-title">
  <h2 id="content-title">Préparer une session de formation</h2>
  <p>Cette page rassemble les actions utilisées par une équipe de publication avant l'ouverture d'une session. Les responsables doivent pouvoir vérifier les ressources, consulter les consignes et passer d'une action à l'autre sans perdre leur position dans la page.</p>
  <section aria-labelledby="actions-title" class="fr-mt-4w">
    <h3 id="actions-title">Actions prioritaires</h3>
    <p>Les actions ci-dessous couvrent les étapes les plus fréquentes : publier la session, contrôler le formulaire d'inscription et prévenir les personnes inscrites. Elles sont placées en premier pour éviter de chercher les commandes utiles dans le reste de la page.</p>
    <ul class="fr-btns-group fr-btns-group--inline-md">
      <li><button class="fr-btn" type="button">Publier la session</button></li>
      <li><a class="fr-btn fr-btn--secondary" href="ec12-form-labels.html">Vérifier le formulaire</a></li>
      <li><button class="fr-btn fr-btn--tertiary" type="button">Prévenir les participants</button></li>
    </ul>
  </section>
  <section aria-labelledby="resources-title" class="fr-mt-4w">
    <h3 id="resources-title">Ressources à consulter</h3>
    <p>Ces ressources servent de points de passage pendant la préparation. Une personne qui avance au clavier doit comprendre quel lien ou quelle carte est actif avant de valider son choix.</p>
    <div class="fr-grid-row fr-grid-row--gutters fr-mb-4w">
{cards}
    </div>
  </section>
  <section aria-labelledby="details-title" class="fr-mt-4w">
    <h3 id="details-title">Informations complémentaires</h3>
    <section class="fr-accordion">
      <h4 class="fr-accordion__title">
        <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="session-panel">Organisation de la salle</button>
      </h4>
      <div class="fr-collapse" id="session-panel">
        <p>La salle doit disposer d'un poste de démonstration, d'un accès réseau et d'un support de projection. Les consignes de circulation sont confirmées avec l'accueil avant l'arrivée des participants.</p>
      </div>
    </section>
    <section class="fr-accordion">
      <h4 class="fr-accordion__title">
        <button type="button" class="fr-accordion__btn" aria-expanded="false" aria-controls="materials-panel">Documents à préparer</button>
      </h4>
      <div class="fr-collapse" id="materials-panel">
        <p>Les supports de cours, la grille d'audit et les exemples corrigés sont mis à disposition dans l'espace documentaire. Chaque document doit être vérifié avant diffusion.</p>
      </div>
    </section>
    <p class="fr-mt-3w"><a class="fr-link" href="ec04-contrast.html">Consulter la charte de publication</a></p>
  </section>
</section>"""


def content_ec07(version_key: str) -> str:
    if version_key == "accessible":
        foreign = '<span lang="en">Fall / Winter accessibility workshop</span>'
    else:
        foreign = "Fall / Winter accessibility workshop"
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Atelier international</h2>
  <p>Le ministère invite les référents à participer au {foreign} consacré aux contrôles rapides.</p>
  <p>La séance alterne retours d'expérience français et exemples internationaux.</p>
</section>"""


def content_ec08(version_key: str) -> str:
    class_attr = ' class="demo-fixed-cards"' if version_key != "accessible" else ""
    cards = "\n".join(
        [
            card("Checklist de publication", "ec04-contrast.html", "Une ressource longue avec plusieurs points de contrôle à lire avant la mise en ligne.", "PDF"),
            card("Kit contribution RGAA", "ec03-headings.html", "Un kit détaillé pour vérifier les titres, les listes, les images, les liens et les formulaires.", "DOCX"),
            card("Grille de restitution", "ec13-required-errors.html", "Un modèle pour préparer la restitution collective après l'audit en binôme.", "XLSX"),
        ]
    )
    return f"""<section{class_attr} aria-labelledby="content-title">
  <h2 id="content-title">Ressources à zoomer</h2>
  <p>Tester cette page à 200 % de zoom et sur fenêtre étroite.</p>
  <div class="fr-grid-row fr-grid-row--gutters">
{cards}
  </div>
</section>"""


def content_ec09(version_key: str) -> str:
    if version_key == "accessible":
        track = '\n      <track kind="captions" src="../assets/shared/media/sous-titres-demo.vtt" srclang="fr" label="Français" default>'
        caption = "Vidéo de sensibilisation avec sous-titres français relus et synchronisés. Le fichier média final sera intégré ultérieurement."
    else:
        track = ""
        caption = "Vidéo de sensibilisation. Le fichier média final sera intégré ultérieurement."
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Vidéo de sensibilisation</h2>
  <figure class="fr-content-media" role="group" aria-label="Vidéo de sensibilisation à l'accessibilité numérique">
    <div class="fr-content-media__img">
      <video controls class="fr-responsive-vid" aria-describedby="video-caption">{track}
      </video>
      {placeholder_media("Vidéo à intégrer")}
    </div>
    <figcaption class="fr-content-media__caption" id="video-caption">{esc(caption)}</figcaption>
  </figure>
</section>"""


def content_ec10(version_key: str) -> str:
    transcription = ""
    if version_key == "accessible":
        transcription = transcript_component(
            "podcast-rgaa",
            "Transcription du podcast RGAA",
            [
                "Bienvenue dans ce court podcast consacré aux premiers contrôles RGAA.",
                "Nous commençons par vérifier le titre de page, les alternatives d'images, le clavier, puis les formulaires.",
                "La transcription finale reprendra mot pour mot le fichier audio fourni.",
            ],
        )
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">Podcast RGAA</h2>
  <figure class="fr-content-media" role="group" aria-label="Extrait audio sur une démarche RGAA">
    <figcaption class="fr-content-media__caption">Extrait audio présentant une démarche RGAA. Le fichier audio final sera intégré ultérieurement.</figcaption>
    <audio controls aria-label="Écouter le podcast RGAA"></audio>
  </figure>
  {transcription}
</section>"""


def content_ec11(page: dict, version_key: str) -> str:
    sources = page.get("assets", {}).get("external_sources", {})
    with_transcription = sources.get("with_transcription")
    audio_described = sources.get("audio_described")
    blocks: list[str] = []
    if version_key == "accessible":
        if audio_described:
            blocks.append(youtube_media_block(audio_described, "Vidéo audiodécrite"))
        if with_transcription:
            blocks.append(youtube_media_block(with_transcription, "Vidéo avec transcription"))
    elif version_key == "help":
        if with_transcription:
            blocks.append(youtube_media_block(with_transcription, "Vidéo avec transcription"))
        if audio_described:
            blocks.append(youtube_media_block(audio_described, "Vidéo audiodécrite"))
    else:
        if with_transcription:
            blocks.append(youtube_media_block(with_transcription, "Vidéo avec transcription"))
    return f"""<section aria-labelledby="content-title">
  <h2 id="content-title">CAPTCHA : le retour au Moyen Âge</h2>
  <p>Cette page présente une vidéo de sensibilisation aux difficultés posées par les CAPTCHA visuels.</p>
</section>
{'\n'.join(blocks)}"""


def page_content(page: dict, version_key: str) -> str:
    page_id = page["id"]
    if page_id == "ec01-images":
        return content_ec01(version_key)
    if page_id == "ec02-page-title":
        return content_ec02(version_key)
    if page_id == "ec03-headings":
        return content_ec03(version_key)
    if page_id == "ec04-contrast":
        return content_ec04(version_key)
    if page_id == "ec05-skiplinks":
        return content_ec05(version_key)
    if page_id == "ec06-keyboard-focus":
        return content_ec06(version_key)
    if page_id == "ec07-language":
        return content_ec07(version_key)
    if page_id == "ec08-zoom":
        return content_ec08(version_key)
    if page_id == "ec09-captions":
        return content_ec09(version_key)
    if page_id == "ec10-transcript":
        return content_ec10(version_key)
    if page_id == "ec11-audio-description":
        return content_ec11(page, version_key)
    if page_id == "ec12-form-labels":
        return form_label_content(version_key == "accessible")
    if page_id == "ec13-required-errors":
        return required_errors_content(version_key == "accessible")
    raise ValueError(f"Contenu non défini pour {page_id}")


def document_title(contract: dict, page: dict, version_key: str) -> str:
    if page["id"] == "ec02-page-title":
        if version_key == "accessible":
            return f'Recherche "RGAA" - Page 2/3 - {contract["site"]["name"]}'
        return "Sans titre"
    return f"{page['title']} - {contract['site']['name']}"


def html_lang(page: dict, version_key: str) -> str:
    if page["id"] == "ec07-language" and version_key != "accessible":
        return "francais"
    return "fr"


def skiplinks_variant(page: dict, version_key: str) -> str:
    if page["id"] == "ec05-skiplinks" and version_key != "accessible":
        return "broken-content-anchor"
    return "default"


def generate_exercise_page(contract: dict, page: dict, version_key: str, current: str) -> None:
    version = contract["versions"][version_key]
    title = document_title(contract, page, version_key)
    notice = ""
    if version_key == "help":
        notice = f"""<section class="fr-mb-6w" aria-labelledby="help-title">
  <h2 id="help-title">Aide à la correction</h2>
  <div class="fr-accordions-group">
{help_accordions(page)}
  </div>
</section>"""
    content = page_content(page, version_key)
    page_breadcrumb = breadcrumb(
        [("Accueil", "../index.html"), (version["role"], "index.html")],
        page["title"],
        f"breadcrumb-{version_key}-{page['id']}",
    )
    main_body = f"{notice}\n  {content}" if version_key == "help" else f"{content}\n  "
    exercise_content = f"""  <h1>{page['number']}. {esc(page['title'])}</h1>
  {main_body}"""
    main = f"""{page_breadcrumb}
<main id="contenu" class="fr-container fr-py-6w">
{content_column(exercise_content)}
</main>"""
    write_text(
        DOCS_DIR / version["path"] / f"{page['id']}.html",
        page_shell(
            contract,
            title,
            1,
            main,
            current,
            html_lang=html_lang(page, version_key),
            skiplinks_variant=skiplinks_variant(page, version_key),
        ),
    )


def generate_manifest(contract: dict) -> None:
    rows = [
        "| Page | Point de contrôle rapide | Erreur injectée | Outil de détection | Correction attendue | Aide associée |",
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
    parts = ["# Corrigé points de contrôle rapides\n", "Généré depuis `03-easy-checks/evaluation_contract.yml`.\n"]
    for page in contract["pages"]:
        parts.append(f"## {page['number']}. {page['title']}\n")
        parts.append(f"- Point de contrôle rapide : {page['easy_check']['name']}")
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

.fr-content-media__img img {
  height: auto;
  max-width: 100%;
}

.demo-image-check {
  row-gap: 1.5rem;
}

.demo-image-check__item,
.demo-image-check__contact {
  padding-top: 0.5rem;
}

.demo-image-check__contact {
  border-top: 1px solid #dddddd;
}

.demo-informative-image {
  display: block;
  height: auto;
  margin: 0.75rem 0 1rem;
  max-width: 100%;
  width: 100%;
}

.demo-separator-image {
  margin: 0.75rem 0 1rem;
}

.demo-separator-image img {
  display: block;
  height: auto;
  max-width: 100%;
}

.demo-contact-link {
  align-items: center;
  display: inline-flex;
  gap: 0.35rem;
}

.demo-contact-link img {
  height: auto;
  max-width: 1.75rem;
}

.demo-contact-list {
  margin-top: 0;
}

.demo-contact-list li + li {
  margin-top: 0.5rem;
}

.demo-fake-heading {
  color: #161616;
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 2rem;
  margin: 2rem 0 1rem;
}

.demo-heading-as-emphasis {
  color: #c9191e;
}

.demo-low-contrast {
  color: #b8b8b8;
}

.demo-pale-link {
  color: #8f8fff;
}

.demo-pale-action {
  background-color: #ececff;
  color: #8f8fff;
}

.demo-status-dot {
  background-color: #e5fbef;
  color: #b8b8b8;
}

.demo-no-focus a:focus,
.demo-no-focus button:focus,
.demo-no-focus input:focus {
  outline: none !important;
  box-shadow: none !important;
}

.demo-fixed-cards .fr-card {
  height: 9rem;
  overflow: hidden;
}

.demo-media-placeholder {
  align-items: center;
  background: #eee;
  border: 1px solid #ddd;
  color: #666;
  display: flex;
  justify-content: center;
  min-height: 14rem;
}

.demo-form {
  max-width: 42rem;
}

.demo-red {
  color: #ce0500;
}

.demo-red-border {
  border: 2px solid #ce0500;
}
""",
    )


def copy_grid() -> None:
    if GRID_SOURCE.exists():
        GRID_TARGET.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(GRID_SOURCE, GRID_TARGET)


def generate_demo_assets() -> None:
    images = {
        "schema-rgaa.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="720" height="360" viewBox="0 0 720 360" role="img">
  <rect width="720" height="360" fill="#f6f6f6"/>
  <rect x="60" y="100" width="160" height="110" fill="#000091"/>
  <rect x="280" y="100" width="160" height="110" fill="#6e445a"/>
  <rect x="500" y="100" width="160" height="110" fill="#297254"/>
  <path d="M230 155h40M450 155h40" stroke="#161616" stroke-width="10"/>
  <text x="140" y="165" fill="#fff" font-family="Arial" font-size="28" text-anchor="middle">Vérifier</text>
  <text x="360" y="165" fill="#fff" font-family="Arial" font-size="28" text-anchor="middle">Corriger</text>
  <text x="580" y="165" fill="#fff" font-family="Arial" font-size="28" text-anchor="middle">Publier</text>
</svg>""",
        "motif-hexagones.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="720" height="72" viewBox="0 0 720 72" aria-hidden="true">
  <rect width="720" height="72" fill="#fff"/>
  <path d="M40 36h260M420 36h260" stroke="#000091" stroke-width="4" stroke-linecap="round"/>
  <path d="M360 18l18 18-18 18-18-18z" fill="#000091"/>
</svg>""",
        "contact.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="240" height="180" viewBox="0 0 240 180" role="img">
  <rect width="240" height="180" rx="8" fill="#f6f6f6"/>
  <rect x="42" y="48" width="156" height="96" rx="8" fill="#000091"/>
  <path d="M52 58l68 52 68-52" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M52 134l48-40M188 134l-48-40" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>
</svg>""",
        "sms.svg": """<svg xmlns="http://www.w3.org/2000/svg" width="240" height="180" viewBox="0 0 240 180" role="img">
  <rect width="240" height="180" rx="8" fill="#f6f6f6"/>
  <rect x="44" y="46" width="152" height="92" rx="12" fill="#000091"/>
  <path d="M78 78h84M78 102h58" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/>
  <path d="M92 138l-28 24v-36" fill="#000091"/>
</svg>""",
    }
    image_dir = DOCS_DIR / "assets" / "shared" / "images"
    for filename, content in images.items():
        write_text(image_dir / filename, content)
    write_text(
        DOCS_DIR / "assets" / "shared" / "media" / "sous-titres-demo.vtt",
        "WEBVTT\n\n00:00:00.000 --> 00:00:03.000\nBienvenue dans cette vidéo de sensibilisation.\n\n00:00:03.000 --> 00:00:06.000\nLes sous-titres finaux seront fournis avec la vidéo.\n",
    )
    write_text(
        DOCS_DIR / "assets" / "shared" / "media" / "audiodescription-demo.vtt",
        "WEBVTT\n\n00:00:00.000 --> 00:00:03.000\nDescription : l'interface affiche un formulaire avec une erreur mise en évidence.\n",
    )
    write_text(
        DOCS_DIR / "assets" / "shared" / "media" / "transcription-demo.html",
        "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\"><title>Transcription du podcast RGAA</title></head><body><main><h1>Transcription du podcast RGAA</h1><p>Transcription de démonstration à remplacer par la transcription finale.</p></main></body></html>\n",
    )


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
    generate_demo_assets()
    copy_grid()
    generate_media_readme(contract)
    generate_root(contract)
    generate_sitemap_page(contract)
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
