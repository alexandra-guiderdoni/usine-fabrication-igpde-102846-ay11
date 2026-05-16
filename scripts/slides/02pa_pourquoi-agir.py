"""Slide 02mc : pourquoi agir - droit + charte État (Martine 4+24)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_alert, add_callout, add_image, add_notes, add_tableau,
    estimate_callout_height,
    new_slide,
)

IMG_W = 1.5


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

    stack = Stack(top=2.20, gap=0.25)

    titre_droit = "Un droit, pas une faveur"
    bullets_droit = [
        "Droit fondamental d'acces a l'information",
        "Lutte contre la discrimination numérique",
        "Inclusion dans la vie professionnelle et citoyenne",
    ]
    col_h = estimate_callout_height(titre_droit, bullets_droit, CONTENT_W - IMG_W - 0.3, line_spacing=1.2)
    top_row1 = stack.push(col_h)
    add_callout(
        slide, titre_droit, bullets_droit,
        top=top_row1, left=MARGIN_L, width=CONTENT_W - IMG_W - 0.3,
        line_spacing=1.2,
    )
    add_image(
        slide,
        "scripts/images/charte-communication-etat.png",
        top=top_row1, left=MARGIN_L + CONTENT_W - IMG_W,
        width=IMG_W,
        alt_text="Couverture de la Charte d'accessibilité de la communication de l'État",
    )

    headers = ["Communication inaccessible", "Communication accessible"]
    rows = [
        ["Non compréhension", "Acces a l'information"],
        ["Frustration, enervement", "Confiance en soi"],
        ["Decrochage", "Autonomie"],
        ["Exclusion", "Inclusion sociale"],
    ]
    add_tableau(
        slide, headers, rows,
        top=stack.push(len(rows) * 0.40 + 0.40),
        col_widths=[6.0, 6.0],
    )

    add_notes(
        slide,
        "Le tableau gagnant-gagnant est tire de la Charte d'accessibilité "
        "de la communication de l'État (SIG, mars 2021). Cote gauche : "
        "ce que vit la personne face a un contenu inaccessible. Cote droit : "
        "ce qu'une communication accessible lui apporte. Pour le communicant, "
        "une communication accessible est une communication qui atteint son "
        "objectif. Montrer la couverture de la charte : c'est un document "
        "officiel du Premier Ministre.",
    )
    return slide
