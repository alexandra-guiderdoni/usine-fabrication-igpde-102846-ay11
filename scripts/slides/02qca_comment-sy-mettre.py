"""Slide 02qca : comment s'y mettre - 4 étapes et offre de formation."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_callout, add_alert, add_highlight, add_notes,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Comment s'y mettre ?",
        fil_ariane="1. Q5 - Comment | Premiers pas",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "Des règles et bonnes pratiques simples permettent "
        "de garantir l'accessibilité à toutes et tous."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    titre_etapes = "4 étapes pour avancer"
    bullets_etapes = [
        "Être sensibilisé - c'est ce qu'on fait aujourd'hui",
        "Être à l'écoute des besoins spécifiques",
        "Connaître les matériels et logiciels adaptés",
        "Se former pour découvrir un nouvel univers",
    ]
    titre_formation = "Offre de formation"
    bullets_formation = [
        "Mentor (en ligne) : l'accessibilité numérique selon votre métier",
        "IGPDE : l'accessibilité numérique pour la bureautique et le web (réf. 102846)",
        "DINUM : sensibilisation, design inclusif, audit RGAA",
    ]

    col_h = max(
        estimate_callout_height(titre_etapes, bullets_etapes, COL_W, line_spacing=1.2),
        estimate_alert_height(titre_formation, bullets_formation, COL_W, line_spacing=1.2),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_etapes, bullets_etapes,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.2,
    )
    add_alert(
        slide, titre_formation, bullets_formation,
        top=top_cols, left=COL_R, width=COL_W,
        alert_type="success",
        line_spacing=1.2,
    )

    add_notes(
        slide,
        "Rassurer les stagiaires : ils ne partent pas de zéro. "
        "La sensibilisation d'aujourd'hui est la première étape. "
        "Mentor est un parcours en ligne gratuit. La formation IGPDE 102846 "
        "est le prolongement de cette journée. La DINUM propose des formats "
        "plus techniques pour ceux qui veulent aller plus loin.",
    )
    return slide
