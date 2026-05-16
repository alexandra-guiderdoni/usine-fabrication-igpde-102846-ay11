"""Slide 02h : idée reçue 2 - la créativité et l'UX seront dégradées."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_callout, add_qrcode, add_notes, new_slide,
    estimate_card_height, estimate_callout_height,
)

URL_SOURCE = "https://ideance.net/blog/4602/idees-recues-a11y"
NUMERO = 2


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        fil_ariane="1. Introduction | Idées reçues",
        titre="Idée reçue 2 / 6",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30
    idee_text = "« La créativité et l'UX seront dégradées »"

    decrypt_bullets = [
        "L'accessibilité n'impose pas un design archaïque, austère ou sans inspiration",
        "Les contraintes sont des leviers de créativité, pas des freins",
        "Les interfaces les plus accessibles sont souvent les plus claires et élégantes",
        "Exemple : le DSFR (Design System de l'État) est à la fois accessible et soigné",
    ]

    callout_h = estimate_callout_height("Décryptage", decrypt_bullets, COL_W, line_spacing=1.15)
    card_h = estimate_card_height("Idée reçue", [idee_text], COL_W, numero=NUMERO)
    col_h = max(card_h, callout_h)

    add_card(
        slide, "Idée reçue", idee_text,
        top=top_cols, left=MARGIN_L, width=COL_W, height=col_h, numero=NUMERO,
    )
    add_callout(
        slide, "Décryptage", decrypt_bullets,
        top=top_cols, left=COL_R, width=COL_W, line_spacing=1.15,
    )

    url_top = round(top_cols + col_h + 0.10, 2)
    add_qrcode(slide, "_assets/qrcode-ideance-idees-recues.png",
               url=URL_SOURCE, top=url_top, left=COL_R, size=0.95,
               label=URL_SOURCE, label_width=COL_W - 1.10)

    add_notes(
        slide,
        "Montrer un contre-exemple si possible : un site très accessible peut être très design. "
        "La contrainte de contraste 4,5:1 produit des palettes plus sereines, pas plus laides. "
        "Analogie : les normes de sécurité incendie n'ont pas empêché d'architecturer de beaux bâtiments.",
    )
    return slide
