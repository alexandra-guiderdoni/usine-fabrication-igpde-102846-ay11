"""Slide 03 : annonce et plan de la partie II."""

from igpde_dsfr_components import add_notes, add_stepper, new_slide


ETAPES = [
    "Structurer le document",
    "Rendre les couleurs accessibles",
    "Décrire les contenus visuels",
    "Améliorer la langue et la lisibilité",
    "Vérifier et finaliser",
]


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        fil_ariane="Partie II | Plan",
        titre="Partie II - Documents bureautiques accessibles - TP",
        footer_text=f"{ctx.footer_base} / Partie II",
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
        "Annoncer les cinq thèmes qui structurent la partie II. "
        "Préciser que la progression va de la structure du document à sa vérification finale.",
    )
    return slide
