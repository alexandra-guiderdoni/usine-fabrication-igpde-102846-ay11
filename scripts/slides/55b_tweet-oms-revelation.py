"""Slide rs_02 : révélation - ce que vous voyez vs ce que NVDA lit."""

from igpde_dsfr_components import (
    COL_W, COL_R, MARGIN_L, CONTENT_W,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)

TWEET_VU = (
    "Lavez-vous les \U0001f450 avec du \U0001f9fc & de l'\U0001f4a6."
)
TWEET_LU = (
    "Lavez-vous les mains ouvertes avec du savon"
    " et éclaboussures de sueur."
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Ce que vous voyez ≠ ce qui est lu",
        fil_ariane="4. Réseaux sociaux | Accroche",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30

    vu_titre = "Ce que vous voyez"
    vu_bullets = [
        "Lavez-vous les \U0001f450 avec du \U0001f9fc & de l'\U0001f4a6.",
        "Quand vous toussez ou \U0001f927 couvrez votre \U0001f444.",
        "Évitez de toucher les \U0001f440, le \U0001f443 & la \U0001f444.",
    ]
    vu_h = estimate_callout_height(vu_titre, vu_bullets, COL_W)

    lu_titre = "Ce que NVDA lit à voix haute"
    lu_bullets = [
        "Lavez-vous les mains ouvertes avec du savon et éclaboussures de sueur.",
        "Quand vous toussez ou visage qui éternue couvrez votre bouche.",
        "Évitez de toucher les yeux grand ouverts, le nez et la bouche.",
    ]
    lu_h = estimate_alert_height(lu_titre, lu_bullets, COL_W)

    col_h = max(vu_h, lu_h)

    add_callout(slide, vu_titre, vu_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h)
    add_alert(slide, lu_titre, lu_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="warning")

    accroche = "Chaque émoji a un nom officiel lu intégralement. Il interrompt le flux de lecture."
    hl_h = estimate_highlight_height(accroche, CONTENT_W)
    add_highlight(slide, accroche,
                  top=round(top + col_h + 0.25, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "Lire à voix haute la colonne de droite avec le ton d'un lecteur d'écran - monotone, sans pause. "
        "Silence après la lecture. Laisser l'absurdité s'installer. "
        "L'effet de surprise est la meilleure colle mémorielle ici. "
        "Ne pas commenter immédiatement - poser la question : 'Qui aurait pensé à ça en publiant ?'",
    )
    return slide
