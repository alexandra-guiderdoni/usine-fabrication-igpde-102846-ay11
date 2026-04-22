"""Slide 02d : tour de table - template de présentation en 3 colonnes."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, GAP,
    add_card, add_notes, new_slide,
    estimate_card_height,
)

CARD_W = (CONTENT_W - 2 * GAP) / 3


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Présentez-vous",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    card1_titre = "Qui êtes-vous ?"
    card1_contenu = [
        "Bonjour, je m'appelle [prénom]",
        "Je suis [métier / fonction]",
        "chez [direction / service]",
        "depuis [durée]",
    ]

    card2_titre = "Mon rapport à l'accessibilité"
    card2_contenu = [
        "Quand j'entends « accessibilité numérique », je pense à [premier mot]",
        "Je me situe plutôt :",
        "[ ] Complet débutant",
        "[ ] J'en ai entendu parler",
        "[ ] J'ai déjà appliqué quelques règles",
    ]

    card3_titre = "Ce que j'attends"
    card3_contenu = [
        "Je produis principalement [type de contenu]",
        "Pour un usage : [ ] Interne   [ ] Grand public",
        "Ce que j'espère retirer :",
        "J'aimerais [objectif personnel]",
    ]

    card_h = max(
        estimate_card_height(card1_titre, card1_contenu, CARD_W),
        estimate_card_height(card2_titre, card2_contenu, CARD_W),
        estimate_card_height(card3_titre, card3_contenu, CARD_W),
    )

    add_card(slide, card1_titre, card1_contenu,
             top=2.30, left=MARGIN_L, width=CARD_W, height=card_h)
    add_card(slide, card2_titre, card2_contenu,
             top=2.30, left=MARGIN_L + CARD_W + GAP, width=CARD_W, height=card_h)
    add_card(slide, card3_titre, card3_contenu,
             top=2.30, left=MARGIN_L + 2 * (CARD_W + GAP), width=CARD_W, height=card_h)

    add_notes(
        slide,
        "Chaque stagiaire suit la grille à voix haute - 2 minutes maxi par personne. "
        "Colonne 1 : ancre les métiers présents dans la salle (utile pour choisir les exemples). "
        "Colonne 2 : révèle le niveau réel du groupe - adapter le rythme en conséquence. "
        "Colonne 3 : noter les attentes au tableau, y revenir en clôture pour montrer qu'elles ont été traitées.",
    )
    return slide
