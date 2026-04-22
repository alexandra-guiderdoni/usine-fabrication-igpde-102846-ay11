"""Slide 49 : Demain à 9h - Vos 3 réflexes.

Règles neuropédagogie appliquées :
- R2 : Réduction à 3 actions (limite cognitive = 3-4 éléments)
- R19 : Procédure détaillée + timing pour chaque réflexe
- R22 : Progression (install 1, puis 2, puis 3)
"""

from igpde_dsfr_components import (
    add_card, add_notes, new_slide,
    estimate_card_height, MARGIN_L, CONTENT_W, GAP
)

CARD_W = (CONTENT_W - 2 * GAP) / 3


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Demain à 9 h, vos 3 premiers réflexes",
        fil_ariane="2. Documents accessibles | Plan d'action",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Plan d'action",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    card1_contenu = [
        "Vérifier que tous les titres apparaissent dans le volet de navigation",
        "Si le volet est vide : appliquer les styles",
    ]
    card2_contenu = [
        "Décrire la fonction de chaque image",
        "Image décorative : cocher Marquer comme décoratif",
    ]
    card3_contenu = [
        "Corriger les erreurs avant d'envoyer",
        "Zéro erreur = premier filtre passé",
    ]

    # Calculate max card height
    heights = [
        estimate_card_height("Ctrl+F > onglet Titres", card1_contenu, CARD_W, numero="1"),
        estimate_card_height("Clic droit > Texte de remplacement", card2_contenu, CARD_W, numero="2"),
        estimate_card_height("Fichier > Vérifier l'accessibilité", card3_contenu, CARD_W, numero="3")
    ]
    card_height = max(heights)

    add_card(
        slide,
        titre="Ctrl+F > onglet Titres",
        contenu=card1_contenu,
        top=2.3,
        left=MARGIN_L,
        width=CARD_W,
        height=card_height,
        numero="1"
    )

    add_card(
        slide,
        titre="Clic droit > Texte de remplacement",
        contenu=card2_contenu,
        top=2.3,
        left=MARGIN_L + CARD_W + GAP,
        width=CARD_W,
        height=card_height,
        numero="2"
    )

    add_card(
        slide,
        titre="Fichier > Vérifier l'accessibilité",
        contenu=card3_contenu,
        top=2.3,
        left=MARGIN_L + 2 * (CARD_W + GAP),
        width=CARD_W,
        height=card_height,
        numero="3"
    )

    add_notes(
        slide,
        "Ces 3 gestes en 2 minutes sur chaque nouveau document. Pas besoin de tout "
        "maîtriser d'un coup : commencer par 1, installer le réflexe, ajouter le suivant. "
        "Dans 30 jours, c'est automatique."
    )
    return slide
