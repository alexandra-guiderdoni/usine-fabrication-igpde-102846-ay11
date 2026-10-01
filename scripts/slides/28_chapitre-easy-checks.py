"""Slide 28 : annonce et plan de la partie III."""

from igpde_dsfr_components import add_notes, add_stepper, new_slide


ETAPES = [
    "Repérer les erreurs fréquentes",
    "Vérifier les images et les titres",
    "Contrôler les contrastes, les liens et le clavier",
    "Tester la langue, le zoom et les médias",
    "Examiner les formulaires et réaliser un audit rapide",
]


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        fil_ariane="Partie III | Plan",
        titre="Partie III - Web accessible - TP",
        footer_text=f"{ctx.footer_base} / Partie III",
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
        "Annoncer les cinq thèmes qui structurent la partie III consacrée au Web. "
        "Préciser que les points de contrôle rapides permettent de repérer les principaux "
        "signaux d’alerte avant un audit approfondi. "
        "À la fin de la partie : mission d’audit groupé sur une page de votre choix.",
    )
    return slide
