"""Slide 02d : tour de table - template de présentation en 3 colonnes."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, GAP, BOTTOM_CONTENT,
    add_card, add_notes, new_slide,
)

CARD_W = (CONTENT_W - 2 * GAP) / 3
CARD_TOP = 2.30
CARD_H = BOTTOM_CONTENT - CARD_TOP - 0.05


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
    card1_contenu = (
        "Bonjour, je m'appelle [prénom]\n"
        "Je suis [métier / fonction]\n"
        "chez [direction / service]\n"
        "depuis [durée]"
    )

    card2_titre = "Mon rapport à l'accessibilité"
    card2_contenu = (
        "Quand j'entends « accessibilité numérique », je pense à [premier mot]\n\n"
        "Je me situe plutôt :\n"
        "[ ] Complet débutant\n"
        "[ ] J'en ai entendu parler\n"
        "[ ] J'ai déjà appliqué quelques règles"
    )

    card3_titre = "Ce que j'attends"
    card3_contenu = (
        "Je produis principalement [type de contenu]\n\n"
        "Pour un usage :\n"
        "[ ] Interne   [ ] Grand public\n\n"
        "Ce que j'espère retirer :\n"
        "J'aimerais [objectif personnel]"
    )

    add_card(slide, card1_titre, card1_contenu,
             top=CARD_TOP, left=MARGIN_L, width=CARD_W, height=CARD_H)
    add_card(slide, card2_titre, card2_contenu,
             top=CARD_TOP, left=MARGIN_L + CARD_W + GAP, width=CARD_W, height=CARD_H)
    add_card(slide, card3_titre, card3_contenu,
             top=CARD_TOP, left=MARGIN_L + 2 * (CARD_W + GAP), width=CARD_W, height=CARD_H)

    add_notes(
        slide,
        "Chaque stagiaire suit la grille à voix haute - 2 minutes maxi par personne. "
        "Colonne 1 : ancre les métiers présents dans la salle (utile pour choisir les exemples). "
        "Colonne 2 : révèle le niveau réel du groupe - adapter le rythme en conséquence. "
        "Colonne 3 : noter les attentes au tableau, y revenir en clôture pour montrer qu'elles ont été traitées.",
    )
    return slide
