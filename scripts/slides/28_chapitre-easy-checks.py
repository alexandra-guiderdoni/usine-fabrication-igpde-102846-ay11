"""Slide 3 : chapitre d'ouverture du module points de contrôle rapides.

Règles neuropédagogie appliquées :
- R1 : engagement immédiat par un constat d'impact (notes orateur)
- R2 : primauté - on annonce les 13 points dès l'ouverture
- R3 : WIIFM - « en 20 min vous évaluerez n'importe quelle page »
"""

from igpde_dsfr_components import add_notes, compose_chapitre, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="chapitre",
        titre="",  # le titre est posé par compose_chapitre
        footer_text=f"{ctx.footer_base} / points de contrôle rapides",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    compose_chapitre(slide, numero="3", titre="Les 13 points de contrôle rapides du W3C")

    add_notes(
        slide,
        "Ouvrir par la source d’autorité : The WebAIM Million - Mise à jour 2026, "
        "https://webaim.org/projects/million/. "
        "WebAIM a évalué les pages d’accueil des 1 000 000 de sites web les plus visités avec l’API WAVE autonome "
        "et des outils complémentaires de collecte technique. "
        "Les points de contrôle rapides sont la trousse de secours du W3C : 13 vérifications qu’un non-spécialiste peut faire "
        "rapidement pour repérer les principaux signaux d’alerte avant un audit approfondi. "
        "Annoncer le plan : 13 points de contrôle rapides, chacun traité sur 1 à 4 slides selon sa complexité. "
        "À la fin du module : mission d’audit groupé sur une page de votre choix.",
    )
    return slide
