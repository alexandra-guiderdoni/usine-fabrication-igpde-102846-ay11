"""Tests de régression du validateur du site d'exercice."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import validate  # noqa: E402


PAGE_IDS = [
    "ec01-images",
    "ec02-page-title",
    "ec03-headings",
    "ec04-contrast",
    "ec05-skiplinks",
    "ec06-keyboard-focus",
    "ec07-language",
    "ec08-zoom",
    "ec09-captions",
    "ec10-transcript",
    "ec11-audio-description",
    "ec12-form-labels",
    "ec13-required-errors",
]

EC06_TRAP_SNIPPETS = (
    'data-fr-opened="false" aria-expanded="false" aria-controls="publish-session-modal" class="fr-btn demo-modal-trigger" type="button" tabindex="0">Publier la session',
    'class="fr-link" href="ec12-form-labels.html" tabindex="-1">Vérifier le formulaire',
    'class="fr-link" href="#participants-notification" tabindex="-1">Prévenir les participants',
    'class="fr-modal demo-modal-keyboard-trap"',
    'class="fr-btn--close fr-btn" tabindex="-1">Fermer',
    'class="fr-btn demo-modal-trap-target">Confirmer la publication',
)


@pytest.fixture
def site_minimal(tmp_path, monkeypatch):
    """Construit un site minimal conforme aux règles déjà appliquées."""

    def build(*, include_nojekyll: bool = True) -> Path:
        docs = tmp_path / "docs"
        contract = tmp_path / "evaluation_contract.yml"
        contract.write_text(
            "pages:\n" + "".join(f'  - id: "{page_id}"\n' for page_id in PAGE_IDS),
            encoding="utf-8",
        )
        for relative_path in (
            "manifest.md",
            "corrige-easy-checks.md",
            "assets/dsfr/dsfr.min.css",
            "assets/dsfr/utility/utility.min.css",
            "assets/dsfr/dsfr.module.min.js",
            "assets/dsfr/dsfr.nomodule.min.js",
            "assets/downloads/grille-audit-easy-checks.xlsx",
        ):
            path = docs / relative_path
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        if include_nojekyll:
            (docs / ".nojekyll").touch()

        (docs / "index.html").write_text(
            '<html lang="fr"><body></body></html>', encoding="utf-8"
        )
        for number in range(8):
            (docs / f"annexe-{number}.html").write_text(
                '<html lang="fr"><body></body></html>', encoding="utf-8"
            )
        for variant in ("site-inaccessible", "site-aide-correction", "site-accessible"):
            for page_id in PAGE_IDS:
                path = docs / variant / f"{page_id}.html"
                path.parent.mkdir(parents=True, exist_ok=True)
                content = ['<html lang="fr"><body>']
                if variant == "site-aide-correction":
                    content.extend(
                        [
                            '<h2 id="help-title">Aide</h2>',
                            '<h1 id="content-title">Contenu</h1>',
                        ]
                    )
                elif page_id != "ec06-keyboard-focus" or variant == "site-accessible":
                    content.append('<h1 id="content-title">Contenu</h1>')
                if page_id == "ec06-keyboard-focus" and variant != "site-accessible":
                    content.extend(EC06_TRAP_SNIPPETS)
                content.append("</body></html>")
                path.write_text("\n".join(content), encoding="utf-8")

        monkeypatch.setattr(validate, "DOCS", docs)
        monkeypatch.setattr(validate, "CONTRACT", contract)
        return docs

    return build


def test_refuse_l_absence_de_nojekyll(site_minimal):
    site_minimal(include_nojekyll=False)

    with pytest.raises(FileNotFoundError, match=r"\.nojekyll"):
        validate.validate_docs()


def test_exige_chaque_page_du_contrat_dans_chaque_variante(site_minimal):
    docs = site_minimal()
    (docs / "site-accessible" / "ec13-required-errors.html").unlink()

    with pytest.raises(FileNotFoundError, match="ec13-required-errors.html"):
        validate.validate_docs()


def test_refuse_un_lien_local_qui_sort_de_docs(site_minimal):
    docs = site_minimal()
    (docs.parent / "hors-docs.html").write_text("hors publication", encoding="utf-8")
    page = docs / "site-accessible" / "ec01-images.html"
    page.write_text(
        page.read_text(encoding="utf-8").replace(
            "</body>", '<a href="../../hors-docs.html">Hors site</a></body>'
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="hors de docs"):
        validate.validate_docs()


def test_refuse_un_lien_markdown_absent_de_la_publication(site_minimal):
    docs = site_minimal()
    page = docs / "index.html"
    page.write_text(
        '<html lang="fr"><body><a href="manifest.md">Manifeste</a></body></html>',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Markdown non publié"):
        validate.validate_docs()


def test_verifie_l_action_locale_d_un_formulaire(site_minimal):
    docs = site_minimal()
    page = docs / "site-accessible" / "ec12-form-labels.html"
    page.write_text(
        page.read_text(encoding="utf-8").replace(
            "</body>", '<form action="traitement-inexistant.html"></form></body>'
        ),
        encoding="utf-8",
    )

    with pytest.raises(FileNotFoundError, match="traitement-inexistant.html"):
        validate.validate_docs()


def test_verifie_l_ancre_dans_une_autre_page(site_minimal):
    docs = site_minimal()
    page = docs / "site-accessible" / "ec01-images.html"
    page.write_text(
        page.read_text(encoding="utf-8").replace(
            "</body>",
            '<a href="ec02-page-title.html#ancre-inexistante">Suite</a></body>',
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="Ancres locales absentes"):
        validate.validate_docs()
