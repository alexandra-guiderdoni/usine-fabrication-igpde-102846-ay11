"""Slide 02n : chapitre Q2 - c'est pour qui ?"""

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
        numero="2",
        titre="L'accessibilité numérique, c'est pour qui ?",
    )

    add_notes(
        slide,
        "Transition vers les publics concernés. Avant de montrer les 4 familles, "
        "demander au groupe : à votre avis, combien de personnes "
        "sont concernées par l'accessibilité numérique en France ?",
    )
    return slide
