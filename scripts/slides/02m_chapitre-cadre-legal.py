"""Slide 02m : chapitre d'ouverture - Module 1."""

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
        numero="1",
        titre="Mise en accessibilité de sa communication",
    )

    add_notes(
        slide,
        "Ouverture du module 1. Poser la question : "
        "Quand une communication est-elle vraiment accessible ? "
        "Laisser 30 secondes de silence avant de basculer vers les supports concernés.",
    )
    return slide
