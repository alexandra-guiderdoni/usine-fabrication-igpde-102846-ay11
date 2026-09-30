"""Slide 02ra : cadre européen - 2 directives (Martine 30)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_alert, add_callout, add_highlight, add_notes,
    estimate_alert_height, estimate_callout_height, estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Le cadre européen",
        fil_ariane="1. Q3 - Cadre légal | Directives européennes",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "Deux directives européennes structurent l'obligation "
        "d'accessibilité numérique en France."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    titre_d1 = "Directive 2016/2102 - secteur public"
    bullets_d1 = [
        "Sites web et applications mobiles du secteur public",
        "Transposée en droit français par le décret 2019-768",
        "Obligation de déclaration d'accessibilité",
        "Base du RGAA actuel",
    ]
    titre_d2 = "Directive 2019/882 - secteur privé"
    bullets_d2 = [
        "Acte européen d'accessibilité (EAA)",
        "Applicable à partir du 28 juin 2025",
        "Commerce en ligne, banque, transport, télécom",
        "Élargit l'obligation au-delà du secteur public",
    ]
    col_h = max(
        estimate_callout_height(titre_d1, bullets_d1, COL_W, line_spacing=1.2, compact=True),
        estimate_alert_height(titre_d2, bullets_d2, COL_W, line_spacing=1.2, compact=True),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_d1, bullets_d1,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.2,
        compact=True,
    )
    add_alert(
        slide, titre_d2, bullets_d2,
        top=top_cols, left=COL_R, width=COL_W,
        alert_type="warning",
        line_spacing=1.2,
        compact=True,
    )

    add_notes(
        slide,
        "La directive 2016/2102 est déjà transposée et applicable. "
        "L'EAA (2019/882) étend l'obligation au secteur privé depuis juin 2025. "
        "Pointer que le mouvement est européen, pas seulement français : "
        "les obligations vont continuer à se renforcer.",
    )
    return slide
