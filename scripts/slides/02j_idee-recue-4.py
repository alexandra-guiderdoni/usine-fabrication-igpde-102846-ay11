"""Slide 02j : idée reçue 4 - ce n'est pas de mon ressort."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_callout, add_qrcode, add_notes, new_slide,
    estimate_card_height, estimate_callout_height,
)

URL_SOURCE = "https://ideance.net/blog/4602/idees-recues-a11y"
NUMERO = 4


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        fil_ariane="1. Introduction | Idées reçues",
        titre="Idée reçue 4 / 6",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30
    idee_text = "« Ce n'est pas de mon ressort »"

    decrypt_bullets = [
        "L'accessibilité ne peut pas être portée par une seule équipe ou une seule personne",
        "Elle implique tous les producteurs de contenu : rédacteurs, communicants, designers ...",
        "Chaque document Word, chaque image publiée engage une responsabilité",
        "La loi de 2005 et la directive européenne 2016/2102 s'appliquent à tous les agents publics",
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
    add_qrcode(slide, "_assets/qrcode-ideance-idees-recues.png",
               url=URL_SOURCE, top=url_top, left=COL_R, size=0.95,
               label=URL_SOURCE, label_width=COL_W - 1.10)

    add_notes(
        slide,
        "Cette idée reçue est la plus difficile à déconstruire car elle repose sur une logique réelle : "
        "il y a des spécialistes. Répondre : oui, les développeurs et chefs de projet ont leurs responsabilités. "
        "Mais vous aussi - c'est précisément pourquoi vous êtes là aujourd'hui. "
        "Votre document Word mal structuré empêche un lecteur d'écran de lire. "
        "Votre image sans texte alternatif prive un non-voyant de l'information. Personne n'est exempté.",
    )
    return slide
