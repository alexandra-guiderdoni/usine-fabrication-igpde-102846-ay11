"""Slide 40 : Exercice cross-piliers - Les erreurs de Karine.

Règles neuropédagogie appliquées :
- R6 : Mise en situation pour engagement émotionnel
- R16 : Apprentissage intercalaire (discrimination entre piliers)
- R4 : Récupération active avant solution
"""

from igpde_dsfr_components import (
    add_card, add_callout, add_notes, new_slide,
    estimate_card_height, MARGIN_L, COL_W, COL_R,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Exercice : les erreurs de Karine",
        fil_ariane="2. Documents accessibles | Exercice cross-piliers",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Exercice",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    card1_titre = "Mise en situation"
    card1_contenu = [
        "Karine, chargée de communication, envoie son rapport trimestriel à 40 personnes.",
        "Quels piliers sont concernés ?",
        "Quelles corrections, dans quel ordre ?",
    ]

    card2_titre = "Le document contient"
    card2_contenu = [
        "un titre Introduction en gras Arial 16",
        "un graphique de résultats sans description",
        "la mention urgent écrite en gras et en rouge",
        "un lien cliquez ici pour les annexes",
    ]

    card_h = max(
        estimate_card_height(card1_titre, card1_contenu, COL_W),
        estimate_card_height(card2_titre, card2_contenu, COL_W),
    )

    add_card(slide, card1_titre, card1_contenu, top=2.3, left=MARGIN_L, width=COL_W, height=card_h)
    add_card(slide, card2_titre, card2_contenu, top=2.3, left=COL_R, width=COL_W, height=card_h)

    callout_bullets = [
        "Pilier 1 - Appliquer le style Titre 1 sur Introduction",
        "Pilier 2 - Doubler urgent en texte : urgent - Répondre avant le 15 mai",
        "Pilier 3 - Texte alt sur le graphique : Résultats T1 2025 : hausse de 12 %",
        "Pilier 3 - Renommer le lien : Consulter les annexes du rapport T1",
    ]
    add_callout(
        slide,
        "3 piliers, 4 corrections, 6 minutes",
        callout_bullets,
        top=round(2.3 + card_h + 0.25, 2),
    )

    add_notes(
        slide,
        "Laisser 3 minutes de réflexion individuelle avant de donner la réponse. "
        "Corriger dans l'ordre : structure d'abord (fondation), couleur ensuite, "
        "contenu en dernier. 3 piliers simultanément = exercice d'interleaving - "
        "force la discrimination entre les piliers. 6 minutes = temps réel, pas estime."
    )
    return slide
