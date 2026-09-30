"""Slide 02la : annonce et plan de la partie I."""

from igpde_dsfr_components import add_notes, add_stepper, new_slide


ETAPES = [
    "L'accessibilité numérique, c'est quoi ?",
    "L'accessibilité numérique, c'est pour qui ?",
    "L'accessibilité numérique, quel cadre légal ?",
    "L'accessibilité numérique, pourquoi ?",
    "L'accessibilité numérique, comment s'y mettre ?",
]


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        fil_ariane="Partie I | Plan",
        titre="Partie I - Accessibilité et cadre légal",
        footer_text=f"{ctx.footer_base} / Partie I",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_stepper(
        slide,
        ETAPES,
        top=2.45,
        height=3.65,
    )

    add_notes(
        slide,
        "Annoncer les cinq questions qui structurent la partie I. "
        "Préciser que la progression va de la définition aux premiers gestes concrets.",
    )
    return slide
