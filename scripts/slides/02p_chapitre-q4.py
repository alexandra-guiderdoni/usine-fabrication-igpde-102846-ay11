"""Slide 02p : chapitre Q4 - pourquoi ?"""

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
        numero="4",
        titre="L'accessibilité numérique, pourquoi ?",
    )

    add_notes(
        slide,
        "Au-delà du cadre légal, pourquoi s'investir ? "
        "Cette section passe du devoir à la conviction : "
        "droit fondamental, charte de l'État, bénéfice pour tous.",
    )
    return slide
