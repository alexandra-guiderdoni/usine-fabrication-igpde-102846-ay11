"""Slide rs_05 : vue synthétique - les 4 réflexes avant chaque publication."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, GAP,
    add_card, add_notes, new_slide,
    estimate_card_height,
)

CARD_W = (CONTENT_W - GAP) / 2
GAP_ROWS = 0.10


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="4 réflexes avant chaque publication",
        fil_ariane="4. Réseaux sociaux | Réflexes",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    modules = [
        ("Texte alternatif",
         ["Décrire chaque image en 1 à 2 phrases",
          "Mentionner « Image décorative » si elle ne porte pas de sens"],
         1, MARGIN_L),
        ("Émojis sobres",
         ["1 ou 2 maximum, en fin de message uniquement",
          "Le texte doit avoir du sens sans eux"],
         2, MARGIN_L + CARD_W + GAP),
        ("Hashtags CamelCase",
         ["#ServicePublic pas #servicepublic",
          "Rassembler en fin de post, 2 à 3 maximum"],
         3, MARGIN_L),
        ("Texte natif",
         ["Jamais de faux gras ou faux italique (InstaFont ...)",
          "Les caractères Unicode stylisés sont illisibles par les lecteurs d'écran"],
         4, MARGIN_L + CARD_W + GAP),
    ]

    card_h = max(estimate_card_height(t, c, CARD_W, numero=n) for t, c, n, _ in modules)
    max_card_h = (6.80 - 0.05 - 2.30 - GAP_ROWS) / 2
    card_h = min(card_h, max_card_h)
    row1_top = 2.30
    row2_top = row1_top + card_h + GAP_ROWS

    tops = [row1_top, row1_top, row2_top, row2_top]

    for (titre, contenu, numero, left), top in zip(modules, tops):
        add_card(slide, titre, contenu,
                 top=top, left=left, width=CARD_W, height=card_h, numero=numero)

    add_notes(
        slide,
        "Cette slide sert de boussole pour tout le module. Y revenir à la fin. "
        "Chaque réflexe sera détaillé dans les slides suivantes. "
        "Le message clé : 4 actions, 2 minutes par publication, zéro compétence technique requise.",
    )
    return slide
