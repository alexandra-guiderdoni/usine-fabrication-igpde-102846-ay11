"""Slide 45 : Retour sur le document de Sami - Langue et Finalisation.

Règles neuropedagogie appliquees :
- R13 : Repetition espacee (retour sur un exercice deja fait)
- R10 : Effet Zeigarnik (exercice non termine revele)
- R16 : Interleaving (les 2 derniers thèmes appliques au même document)
"""

from igpde_dsfr_components import (
    add_card, add_callout, add_notes, new_slide,
    estimate_card_height, estimate_callout_height,
    MARGIN_L, CONTENT_W, COL_W, COL_R, Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Retour sur le document de Sami",
        fil_ariane="2. Documents accessibles | Retour exercice",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Retour exercice",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.20)

    card1_titre = "Vous vous souvenez ?"
    card1_contenu = (
        "Vous avez déjà travaillé la plupart des erreurs "
        "de Structure, Couleurs, Contenus et Lisibilité.\n\n"
        "Il restait 2 erreurs des thèmes Langue et Finalisation "
        "que vous n'aviez pas encore les outils pour détecter."
    )

    card2_titre = "Les 2 erreurs cachées"
    card2_contenu = [
        "Langue : un passage en anglais sans balisage de langue",
        "Finalisation : les propriétés du document (titre, auteur) sont vides",
    ]

    card_h = max(
        estimate_card_height(card1_titre, card1_contenu, COL_W),
        estimate_card_height(card2_titre, card2_contenu, COL_W),
    )
    cards_top = stack.push(card_h)

    add_card(slide, card1_titre, card1_contenu, top=cards_top,
             left=MARGIN_L, width=COL_W, height=card_h)
    add_card(slide, card2_titre, card2_contenu, top=cards_top,
             left=COL_R, width=COL_W, height=card_h)

    callout_titre = "Les corrections en 2 minutes"
    callout_bullets = [
        "Langue : sélectionner le passage anglais > Révision > Langue > Définir en anglais",
        "Finalisation : Fichier > Informations > renseigner Titre et Auteur",
    ]
    stack.gap = 0.30
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets,
                                               CONTENT_W)),
    )

    add_notes(
        slide,
        "Effet de surprise : les stagiaires pensaient avoir repéré toutes les "
        "catégories visibles à ce stade. Révéler les 2 derniers critères montre que "
        "l'accessibilité a des dimensions qu'on ne voit pas sans formation.\n\n"
        "Proposer aux stagiaires de rouvrir sami-doc-inaccessible.docx et de "
        "corriger ces 2 erreurs en 2 minutes. Le passage anglais est dans la "
        "section Contact. Les propriétés sont dans Fichier > Informations.",
    )
    return slide
