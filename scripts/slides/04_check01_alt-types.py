"""Slide 4 : Easy Check 1 - Alt text, les 4 types d'images.

Règles neuropédagogie appliquées :
- R5 : chunking - 4 types exactement, pas plus
- R8 : analogie - l'alt text est le sous-titre de l'image
- R16 : visuel - 4 cards côte à côte pour comparer d'un coup d'œil
"""

from igpde_dsfr_components import (
    add_card, add_highlight, add_notes, estimate_card_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Alt text : 4 types d’images, 4 décisions",
        fil_ariane="3. Easy Checks | 1. Alternatives textuelles",
        footer_text=f"{ctx.footer_base} / Easy Checks - Alt text",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "L’alt text est le sous-titre de l’image - sans lui, 5 % des lecteurs voient une page muette.",
        top=2.3,
    )

    # 4 cartes côte à côte : 4 types. Hauteur = max des hauteurs auto.
    MARGIN = 0.52
    GAP = 0.28
    CARD_W = (12.28 - 3 * GAP) / 4  # ≈ 2.86
    TOP = 3.55

    cards = [
        ("Informative",  "Apporte une info : photo d’un bâtiment, graphique.\n→ alt descriptif court.",  1),
        ("Décorative",   "Pure ambiance : séparateur, icône floue.\n→ alt=\"\" (vide).",                 2),
        ("Fonctionnelle","Dans un lien ou un bouton : logo cliquable, picto.\n→ alt = action attendue.",3),
        ("Complexe",     "Diagramme, schéma, infographie.\n→ alt court + description longue à part.",    4),
    ]
    HEIGHT = max(estimate_card_height(t, c, CARD_W, n) for t, c, n in cards)

    for i, (titre_c, contenu, numero) in enumerate(cards):
        add_card(
            slide,
            titre=titre_c,
            contenu=contenu,
            top=TOP, left=MARGIN + i * (CARD_W + GAP),
            width=CARD_W, height=HEIGHT,
            numero=numero,
        )

    add_notes(
        slide,
        "Faire deviner : « Cette carte de métro, quel type ? » (complexe). "
        "Insister sur le décoratif - c’est le plus mal compris. "
        "Un séparateur graphique avec alt=\"ligne bleue\" pollue le lecteur d’écran. "
        "Règle mnémo : si je retire l’image, est-ce que je perds une info ? Si non → alt vide.",
    )
    return slide
