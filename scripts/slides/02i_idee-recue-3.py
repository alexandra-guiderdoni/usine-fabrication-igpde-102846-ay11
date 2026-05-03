"""Slide 02i : idée reçue 3 - c'est juste du contraste et des images décrites."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_callout, add_highlight, add_image, add_notes, new_slide,
    estimate_card_height, estimate_callout_height, estimate_highlight_height,
)

URL_SOURCE = "https://ideance.net/blog/4602/idees-recues-a11y"
URL_LABEL = "ideance.net/blog/4602/idees-recues-a11y"
NUMERO = 3


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Idée reçue 3 / 6",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30
    idee_text = "« C'est juste du contraste et des images décrites »"

    decrypt_bullets = [
        "Le contraste et les textes alternatifs ne sont que 2 exigences sur des centaines",
        "Le RGAA compte 106 critères, les WCAG 2.1 en comptent 78",
        "Titres, liens, tableaux, formulaires, langue, ordre de lecture... autant de dimensions",
        "L'accessibilité touche toute la chaîne : rédaction, mise en forme, export, publication",
    ]

    callout_h = estimate_callout_height("Décryptage", decrypt_bullets, COL_W, line_spacing=1.0)
    card_h = estimate_card_height("Idée reçue", [idee_text], COL_W, numero=NUMERO)
    col_h = max(card_h, callout_h)

    add_card(
        slide, "Idée reçue", idee_text,
        top=top_cols, left=MARGIN_L, width=COL_W, height=col_h, numero=NUMERO,
    )
    add_callout(
        slide, "Décryptage", decrypt_bullets,
        top=top_cols, left=COL_R, width=COL_W, line_spacing=1.0,
    )

    url_top = round(top_cols + col_h + 0.10, 2)
    hl_h = estimate_highlight_height(URL_LABEL, COL_W)
    add_highlight(slide, f"Source : {URL_LABEL}", top=url_top, left=MARGIN_L, width=COL_W, url=URL_SOURCE)
    add_image(slide, "_assets/qrcode-ideance-idees-recues.png", top=url_top, left=COL_R + 2.0, width=hl_h, height=hl_h, alt_text=f"QR code : {URL_SOURCE}")

    add_notes(
        slide,
        "Bonne nouvelle pour les stagiaires : on ne peut pas tout apprendre en 1 jour. "
        "L'objectif de cette formation, c'est d'ouvrir les yeux sur l'étendue du sujet "
        "et d'acquérir les réflexes sur les points les plus fréquents. "
        "Le reste vient avec la pratique et les ressources (RGAA, Easy Checks W3C).",
    )
    return slide
