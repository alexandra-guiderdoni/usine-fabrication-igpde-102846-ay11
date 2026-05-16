"""Slide 02q : chapitre Q5 - comment s'y mettre ?"""

from igpde_dsfr_components import add_notes, compose_chapitre, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="chapitre",
        titre="Module 1",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    compose_chapitre(
        slide,
        numero="5",
        titre="L'accessibilité numérique, comment s'y mettre ?",
    )

    add_notes(
        slide,
        "Dernière question du module : passer à l'action. "
        "Les slides suivantes donnent les premiers outils concrets "
        "avant d'entrer dans les modules pratiques (Word, web, réseaux sociaux).",
    )
    return slide
