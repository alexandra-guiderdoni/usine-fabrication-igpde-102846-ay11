"""Slide 53 : chapitre d'ouverture - Module 4 réseaux sociaux."""

from igpde_dsfr_components import add_notes, compose_chapitre, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="chapitre",
        titre="Module 4",
        footer_text=f"{ctx.footer_base} / Module 4",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    compose_chapitre(
        slide,
        numero="4",
        titre="Accessibilité sur les réseaux sociaux",
    )

    add_notes(
        slide,
        "Ouverture Module 4. Question d'accroche : "
        "Qui a déjà publié une photo sans texte alternatif ? "
        "Toutes les mains levées - c'est le problème qu'on va résoudre.",
    )
    return slide
