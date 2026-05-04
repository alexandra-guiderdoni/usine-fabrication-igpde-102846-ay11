"""Slide : Checklist exercice - Couleurs, langue, finalisation."""

from igpde_dsfr_components import (
    add_checklist, add_highlight, add_notes, new_slide,
    MARGIN_L, CONTENT_W,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist : pratiqué dans l'exercice (2/2)",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = "Couleurs, langue et finalisation."
    add_highlight(slide, accroche, top=2.3)

    items = [
        "Liens descriptifs (pas cliquez ici)",
        "Passages en langue étrangère balisés",
        "Contraste >= 4,5:1 texte standard, >= 3:1 grand texte",
        "Couleur doublée en texte",
        "Propriétés renseignées (Titre, Auteur)",
    ]

    add_checklist(
        slide, items,
        top=3.3, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Deuxième moitié des critères pratiqués. Liens, couleurs, langue "
        "et propriétés du document. Demander : « Levez la main si vous êtes "
        "capables de corriger ces 10 points sans aide. »",
    )
    return slide
