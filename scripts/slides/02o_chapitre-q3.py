"""Slide 02o : chapitre Q3 - quel cadre légal ?"""

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
        numero="3",
        titre="L'accessibilité numérique, quel cadre légal ?",
    )

    add_notes(
        slide,
        "Transition vers le cadre juridique. Rappeler que l'accessibilité "
        "n'est pas seulement une bonne pratique, c'est une obligation légale "
        "avec des sanctions.",
    )
    return slide
