"""Slide 02pa : FALC et langage clair (Martine 27+28)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_alert, add_callout, add_highlight, add_image, add_notes,
    estimate_alert_height, estimate_callout_height, estimate_highlight_height,
    new_slide,
)

LOGO_FALC_W = 1.2


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="FALC et langage clair",
        fil_ariane="1. Q5 - Comment | FALC et langage clair",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "Simplifier ne veut pas dire appauvrir : "
        "c'est rendre le message accessible au plus grand nombre."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    titre_falc = "FALC - Facile à lire et à comprendre"
    bullets_falc = [
        "Règles européennes d'accessibilité cognitive",
        "Phrases courtes, mots simples, une idée par phrase",
        "Images explicatives, mise en page aérée",
        "Validation par des personnes concernées",
    ]
    titre_clair = "Langage clair"
    bullets_clair = [
        "Structurer : titres, listes, paragraphes courts",
        "Expliquer : sigles, jargon, termes techniques",
        "Guider : verbes d'action, consignes explicites",
        "Tester : relecture à voix haute, lisibilité",
    ]
    col_h = max(
        estimate_callout_height(titre_falc, bullets_falc, COL_W, line_spacing=1.2),
        estimate_alert_height(titre_clair, bullets_clair, COL_W, line_spacing=1.2),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_falc, bullets_falc,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.2,
    )
    add_alert(
        slide, titre_clair, bullets_clair,
        top=top_cols, left=COL_R, width=COL_W,
        alert_type="info",
        line_spacing=1.2,
    )

    add_image(
        slide,
        "images-coi/image17.jpeg",
        top=top_cols + col_h + 0.15,
        left=MARGIN_L + (CONTENT_W - LOGO_FALC_W) / 2,
        width=LOGO_FALC_W,
        alt_text="Logo FALC - Facile à lire et à comprendre",
    )

    add_notes(
        slide,
        "Le FALC est un cadre formel européen, le langage clair est une démarche "
        "applicable à tout contenu. Les deux se complètent. Ne pas confondre FALC "
        "et écriture simplifiée : le FALC suit des règles précises et implique "
        "une validation par des lecteurs en situation de handicap cognitif.",
    )
    return slide
