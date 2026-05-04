"""Slide : Checklist exercice - Structure et contenus."""

from igpde_dsfr_components import (
    add_checklist, add_highlight, add_notes, new_slide,
    MARGIN_L, CONTENT_W,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist : pratiqué dans l'exercice (1/2)",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = "Ces critères, vous savez déjà les corriger."
    add_highlight(slide, accroche, top=2.3)

    items = [
        "Titres avec styles intégrés (pas du gras manuel)",
        "Hiérarchie des titres cohérente (H1, H2, H3)",
        "Texte alternatif sur images / décoratifs marqués",
        "Tableaux de données avec ligne d'en-tête",
        "Listes natives (pas de tirets manuels)",
    ]

    add_checklist(
        slide, items,
        top=3.3, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Première moitié des critères pratiqués dans l'exercice de Sami. "
        "Ce sont les fondamentaux de structure et de contenu alternatif.",
    )
    return slide
