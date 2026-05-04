"""Slide : Exercice - Les erreurs de Sami."""

from igpde_dsfr_components import (
    add_card, add_highlight, add_notes, new_slide,
    estimate_card_height, estimate_highlight_height,
    MARGIN_L, CONTENT_W, COL_W, COL_R, Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Exercice : les erreurs de Sami",
        fil_ariane="2. Documents accessibles | Exercice",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Exercice",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.15, gap=0.15)

    card1_titre = "Mise en situation"
    card1_contenu = (
        "Sami, chargé de communication, envoie son rapport trimestriel "
        "à 40 personnes.\n\n"
        "1. Quels critères posent problème ?\n"
        "2. Quelles corrections proposez-vous ?"
    )

    card2_titre = "Le document contient"
    card2_contenu = [
        "Titres en gras, fausses listes, faux sommaire, tableaux sans en-tête",
        "Mention Urgent en rouge, note en gris insuffisant",
        "Graphique et organigramme sans alt, icône redondante",
        "Texte en image, lien cliquez ici, filigrane invisible",
        "Texte justifié, paragraphes vides, majuscules tapées",
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

    stack.gap = 0.30
    accroche = "30 minutes en binôme : repérez les problèmes, puis corrigez-les."
    add_highlight(slide, accroche,
                  top=stack.push(estimate_highlight_height(accroche, CONTENT_W)))

    add_notes(
        slide,
        "Distribuer sami-doc-inaccessible.docx aux binômes.\n\n"
        "Phase 1 - Identification (10 min) : « Identifiez les critères "
        "d'accessibilité qui posent problème. Notez-les sans corriger. » Pas de checklist.\n\n"
        "Phase 2 - Correction (15 min) : si le groupe a besoin d'un guidage, "
        "distribuer sami-doc-aide-correction.docx. Les commentaires Word "
        "expliquent le problème, l'impact et la méthode sans corriger à la "
        "place des stagiaires. "
        "Les binômes corrigent dans l'ordre structure > couleurs > contenus. "
        "Le vérificateur Word sert d'outil de découverte : « Que détecte-t-il ? "
        "Que rate-t-il ? »\n\n"
        "Phase 3 - Restitution (5 min) : débriefer l'erreur de contraste "
        "(gris #767676, ratio 4,48:1) avec le Colour Contrast Analyser. "
        "Question de transfert : « Sur votre dernier document, lequel de "
        "ces critères avez-vous probablement oublié ? » Tour de table rapide.",
    )
    return slide
