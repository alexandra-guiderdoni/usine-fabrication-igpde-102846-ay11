"""Slide clôture module 2 - Engagement personnel + progression J+7 / J+30 / 6 mois."""

from igpde_dsfr_components import (
    Stack, MARGIN_L, CONTENT_W, GAP,
    add_highlight, add_card, add_notes, new_slide,
    estimate_highlight_height, estimate_card_height,
)

CARD_W = (CONTENT_W - 2 * GAP) / 3


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="À vous de jouer",
        fil_ariane="2. Documents accessibles | Clôture",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Fin",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    engagement = "Je m'engage à vérifier les styles de titre et le texte alternatif sur mon prochain document."
    add_highlight(slide, engagement,
                  top=stack.push(estimate_highlight_height(engagement, CONTENT_W)),
                  left=MARGIN_L, width=CONTENT_W)

    c1 = ["Refaites le quiz final sans rouvrir ce support",
          "3-4/5 : relisez le thème correspondant aux erreurs"]
    c2 = ["Ouvrez un vrai document Word",
          "Appliquez la checklist de haut en bas"]
    c3 = ["Styles de titre, texte alt, vérificateur avant envoi",
          "Si c'est automatique : les réflexes sont installés"]

    card_h = max(
        estimate_card_height("J+7", c1, CARD_W),
        estimate_card_height("J+30", c2, CARD_W),
        estimate_card_height("6 mois", c3, CARD_W),
    )
    cards_top = stack.push(card_h)

    add_card(slide, "J+7", c1,
             top=cards_top, left=MARGIN_L, width=CARD_W, height=card_h)
    add_card(slide, "J+30", c2,
             top=cards_top, left=MARGIN_L + CARD_W + GAP, width=CARD_W, height=card_h)
    add_card(slide, "6 mois", c3,
             top=cards_top, left=MARGIN_L + 2 * (CARD_W + GAP), width=CARD_W, height=card_h)

    add_notes(
        slide,
        "L'engagement explicite crée une intention comportementale plus forte qu'une affirmation. "
        "Laisser chaque stagiaire écrire son engagement (physique ou mental). "
        "J+7 = pic de l'oubli selon la courbe d'Ebbinghaus - c'est le moment critique. "
        "J+30 = consolidation. À 6 mois, si les 3 gestes sont devenus automatiques, "
        "la formation a atteint son objectif.",
    )
    return slide
