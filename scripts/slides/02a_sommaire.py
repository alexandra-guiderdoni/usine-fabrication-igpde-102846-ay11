"""Slide 02a : sommaire - les 4 modules de la journée en grille 2x2."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L, BOTTOM_CONTENT,
    add_card, add_notes, estimate_card_height, new_slide,
)

GAP_ROWS = 0.20
BOTTOM_SAFE = BOTTOM_CONTENT - 0.05


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        fil_ariane="1. Introduction",
        titre="Programme de la journée",
        footer_text=f"{ctx.footer_base} / Programme",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    # Contenu sous forme de listes (paragraphes séparés, rendu bullets •)
    modules = [
        ("Accessibilité et cadre légal",
         ["Enjeux et obligations des acteurs publics",
          "Déclaration d'accessibilité"],                        1, MARGIN_L),
        ("Bureautique accessible",
         ["Documents Word et LibreOffice",
          "Export PDF accessible"],                              2, COL_R),
        ("Easy Checks W3C",
         ["13 vérifications rapides W3C WAI",
          "Démonstration et exercice pratique"],                 3, MARGIN_L),
        ("Réseaux sociaux",
         ["Enjeux et obligations",
          "Alt text, hashtags, émojis"],                        4, COL_R),
    ]

    # Hauteur uniforme : toutes les cartes alignées sur la plus haute
    card_h = max(estimate_card_height(t, c, COL_W, n) for t, c, n, _ in modules)
    # row1_top le plus près possible du titre (2.20"), recalé vers le haut
    # si les deux rangées dépasseraient le footer
    row1_top = min(2.20, BOTTOM_SAFE - 2 * card_h - GAP_ROWS)
    row2_top = row1_top + card_h + GAP_ROWS
    tops = [row1_top, row1_top, row2_top, row2_top]

    for (titre_m, desc, numero, left), top in zip(modules, tops):
        add_card(
            slide,
            titre=titre_m,
            contenu=desc,
            top=top,
            left=left,
            width=COL_W,
            height=card_h,
            numero=numero,
        )

    add_notes(
        slide,
        "Présenter les 4 modules, indiquer les horaires approximatifs. "
        "Signaler que chaque module se termine par un geste concret.",
    )
    return slide
