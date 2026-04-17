"""Slide 3 : chapitre d'ouverture du module Easy Checks.

Règles neuropédagogie appliquées :
- R1 : engagement immédiat par un chiffre d'impact (notes orateur)
- R2 : primauté - on annonce les 13 checks dès l'ouverture
- R3 : WIIFM - « en 20 min vous évaluerez n'importe quelle page »
"""

from igpde_dsfr_components import add_notes, compose_chapitre, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="chapitre",
        titre="",  # le titre est posé par compose_chapitre
        fil_ariane="3. Easy Checks",
        footer_text=f"{ctx.footer_base} / Easy Checks",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    compose_chapitre(slide, numero="3", titre="Les 13 Easy Checks du W3C")

    add_notes(
        slide,
        "Ouvrir par un chiffre : 97 % des pages web présentent au moins une violation WCAG détectable "
        "(source WebAIM Million 2024). "
        "Les Easy Checks sont la trousse de secours du W3C : 13 vérifications qu’un non-technicien peut faire "
        "en 20 minutes pour savoir si une page mérite un audit approfondi. "
        "Annoncer le plan : 13 checks, chacun traité sur 1 à 4 slides selon sa complexité. "
        "À la fin du module : mission d’audit groupé sur une page de votre choix.",
    )
    return slide
