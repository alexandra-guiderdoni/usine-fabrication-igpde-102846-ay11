"""Slide 27 : mission finale - audit groupé avec les 13 points de contrôle rapides.

Règles neuropédagogie appliquées :
- R5 : chunking - 4 consignes courtes pour limiter la charge cognitive
- R20 : apprentissage social - audit et restitution en binômes
- R21 : échafaudage - répartition début/fin pour couvrir collectivement les 13 points
"""

from igpde_dsfr_components import add_callout, add_notes, add_stepper, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Votre mission : audit en binôme",
        fil_ariane="3. points de contrôle rapides | Mission finale",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Mission",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_callout(
        slide,
        "Le site d’exercice contient 13 pages : 1 page correspond à 1 point de contrôle.",
        [
            "Choisissez quelques points avec votre binôme : vous n’avez pas à tout couvrir",
            "Un seul écart correctement prouvé suffit à documenter le point",
            "Certains binômes commencent au début, d’autres par la fin",
            "Bonus si rencontré : lien ou PDF problématique à noter dans la grille",
        ],
        top=2.3, height=2.85,
    )

    étapes = [
        "Choisir vos points",
        "Prouver 1 écart",
        "Début / fin",
        "Restitution orale",
    ]
    add_stepper(
        slide,
        étapes,
        top=5.3, height=1.00,
    )

    add_notes(
        slide,
        "Distribuer la grille d’audit : grille-audit-easy-checks.xlsx, téléchargeable depuis la page d’accueil du site d’exercice. "
        "Expliquer la logique du site d’exercice : 13 pages, 13 points de contrôle, une page par point. "
        "Les binômes ne doivent pas tout auditer : ils choisissent quelques points ou pages. "
        "Répartir le groupe : certains binômes commencent par le début du site, d’autres par la fin, pour que les 13 points soient couverts à la restitution. "
        "Règle de diagnostic : un seul écart correctement prouvé suffit à documenter le point ; inutile de chercher toutes les occurrences possibles. "
        "Timing : 3 min cadrage, 15 min audit en binômes, 7 min restitution orale, 5 min comparaison avec l’aide ou le corrigé. "
        "Outils autorisés : DevTools, HeadingsMap, Colour Contrast Analyser, clavier + casque audio. "
        "Rappeler que l’exercice ne produit aucun taux de conformité. "
        "Restitution orale en binôme : point contrôlé, constat, preuve de l’écart et mise en conformité proposée. "
        "Si un binôme trouve un lien non explicite ou un PDF problématique, le traiter comme signal bonus utile à remonter. "
        "Clôture métacognitive (R25) : « Quel check vous a surpris ? Quel est le plus facile à faire adopter dans votre équipe ? ».",
    )
    return slide
