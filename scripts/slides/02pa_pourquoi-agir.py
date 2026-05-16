"""Slide 02mc : pourquoi agir - droit + charte État (Martine 4+24)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_alert, add_callout, add_notes,
    estimate_alert_height, estimate_callout_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pourquoi agir ?",
        fil_ariane="1. Q4 - Pourquoi | Droit et charte",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.25)

    titre_droit = "Un droit, pas une faveur"
    bullets_droit = [
        "Droit fondamental d'accès à l'information",
        "Lutte contre la discrimination numérique",
        "Inclusion dans la vie professionnelle et citoyenne",
    ]
    titre_charte = "Charte de communication de l'État"
    bullets_charte = [
        "Confiance : l'usager comprend et agit seul",
        "Autonomie : pas besoin d'aide tierce",
        "Inclusion : chaque canal atteint son public",
    ]

    col_h = max(
        estimate_callout_height(titre_droit, bullets_droit, COL_W, line_spacing=1.2),
        estimate_alert_height(titre_charte, bullets_charte, COL_W, line_spacing=1.2),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_droit, bullets_droit,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.2,
    )
    add_alert(
        slide, titre_charte, bullets_charte,
        top=top_cols, left=COL_R, width=COL_W,
        alert_type="success",
        line_spacing=1.2,
    )

    add_notes(
        slide,
        "Ne pas rester sur le registre moral : montrer le bénéfice concret. "
        "La charte de communication de l'État impose des engagements mesurables. "
        "Pour la personne qui publie : une communication accessible est une "
        "communication qui atteint son objectif.",
    )
    return slide
