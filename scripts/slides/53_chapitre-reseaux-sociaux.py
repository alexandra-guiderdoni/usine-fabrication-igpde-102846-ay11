"""Slide 53 : annonce et plan de la partie IV."""

from igpde_dsfr_components import add_notes, add_stepper, new_slide


ETAPES = [
    "Comprendre les enjeux des réseaux sociaux",
    "Décrire les images et choisir les plateformes",
    "Rendre les textes et les caractères lisibles",
    "Représenter les publics et écrire clairement",
    "Vérifier avant de publier",
]


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        fil_ariane="Partie IV | Plan",
        titre="Partie IV - Réseaux sociaux accessibles - TP",
        footer_text=f"{ctx.footer_base} / Partie IV",
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
        "Annoncer les cinq thèmes qui structurent la partie IV. "
        "Préciser que la progression va de l’analyse d’un post à la vérification "
        "complète avant publication. Question d'accroche : "
        "Qui a déjà publié une photo sans texte alternatif ? "
        "Toutes les mains levées - c'est le problème qu'on va résoudre.",
    )
    return slide
