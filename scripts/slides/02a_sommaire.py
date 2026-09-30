"""Slide 02a : sommaire - les 4 modules de la journée en grille 2x2."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_notes, new_slide,
)

CARD_H = 2.05
GAP_ROWS = 0.35
ROW1_TOP = 2.25


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
         ["Documents Word (LibreOffice)",
          "Export PDF accessible"],                              2, COL_R),
        ("Points de contrôle rapides W3C",
         ["13 vérifications rapides W3C WAI",
          "Démonstration et exercice pratique"],                 3, MARGIN_L),
        ("Réseaux sociaux",
         ["Enjeux et obligations",
          "Alt text, hashtags, émojis"],                        4, COL_R),
    ]

    row2_top = ROW1_TOP + CARD_H + GAP_ROWS
    tops = [ROW1_TOP, ROW1_TOP, row2_top, row2_top]

    for (titre_m, desc, numero, left), top in zip(modules, tops):
        add_card(
            slide,
            titre=titre_m,
            contenu=desc,
            top=top,
            left=left,
            width=COL_W,
            height=CARD_H,
            numero=numero,
            numero_en_ligne=True,
        )

    add_notes(
        slide,
        "Présenter les 4 modules, indiquer les horaires approximatifs. "
        "Signaler que chaque module se termine par un geste concret.",
    )
    return slide
