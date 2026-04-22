"""Slide 02g : idée reçue 1 - ça ne concerne qu'une minorité de personnes."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_callout, add_highlight, add_notes, new_slide,
    estimate_card_height, estimate_callout_height, estimate_highlight_height,
)

URL_SOURCE = "https://ideance.net/blog/4602/idees-recues-a11y"
URL_LABEL = "ideance.net/blog/4602/idees-recues-a11y"
NUMERO = 1


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Idée reçue 1 / 6",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30
    idee_text = "« Ça ne concerne qu'une minorité de personnes »"

    decrypt_bullets = [
        "1 milliard+ de personnes dans le monde vivent avec un handicap (OMS)",
        "Soit 15 % de la population mondiale - 1 personne sur 6",
        "En France : 12 millions de personnes en situation de handicap",
        "Et chacun sera concerné un jour : âge, accident, maladie temporaire",
    ]

    callout_h = estimate_callout_height("Décryptage", decrypt_bullets, COL_W)
    card_h = estimate_card_height("Idée reçue", [idee_text], COL_W, numero=NUMERO)
    col_h = max(card_h, callout_h)

    add_card(
        slide, "Idée reçue", [idee_text],
        top=top_cols, left=MARGIN_L, width=COL_W, height=col_h, numero=NUMERO,
    )
    add_callout(
        slide, "Décryptage", decrypt_bullets,
        top=top_cols, left=COL_R, width=COL_W,
    )

    url_top = round(top_cols + col_h + 0.25, 2)
    hl_h = estimate_highlight_height(URL_LABEL, COL_W)
    add_highlight(slide, f"Source : {URL_LABEL}", top=url_top, left=MARGIN_L, width=COL_W, url=URL_SOURCE)
    add_card(slide, "QR code à insérer", [], top=url_top, left=COL_R, width=COL_W, height=hl_h)

    add_notes(
        slide,
        "Laisser le groupe répondre vrai/faux avant d'afficher le décryptage. "
        "Insister : le handicap permanent n'est qu'une fraction. Le handicap temporaire "
        "(bras cassé, conjonctivite) et situationnel (plein soleil sur téléphone) touchent tout le monde. "
        "Analogie : l'ascenseur est utile aux personnes en fauteuil, aux parents avec poussette, "
        "aux livreurs les mains prises. L'accessibilité profite à tous.",
    )
    return slide
