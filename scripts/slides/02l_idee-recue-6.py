"""Slide 02l : idée reçue 6 - on s'en occupe à la fin."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_callout, add_highlight, add_notes, new_slide,
    estimate_card_height, estimate_callout_height, estimate_highlight_height,
)

URL_SOURCE = "https://ideance.net/blog/4602/idees-recues-a11y"
URL_LABEL = "ideance.net/blog/4602/idees-recues-a11y"
NUMERO = 6


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Idée reçue 6 / 6",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30
    idee_text = "« On s'en occupe à la fin ! »"

    decrypt_bullets = [
        "Prise en compte tardive = grosses corrections après coup",
        "Cela pèse sur l'efficacité des projets et génère de la frustration pour les équipes",
        "L'accessibilité « à la fin » est souvent l'accessibilité jamais faite",
        "Solution : intégrer les bons réflexes à chaque étape, pas les accumuler en sprint final",
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
        "Dernière idée reçue - transition naturelle vers la journée : "
        "« Aujourd'hui, on ne remet pas à la fin. On commence par les bons réflexes et on les ancre maintenant. » "
        "Demander au groupe : laquelle de ces 6 idées reçues vous parlait le plus ce matin ? "
        "Cette question fait le lien entre l'icebreaker et la suite du programme.",
    )
    return slide
