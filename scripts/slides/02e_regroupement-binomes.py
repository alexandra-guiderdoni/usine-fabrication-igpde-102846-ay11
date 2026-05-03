"""Slide 02e : regroupement par binômes - constitution des paires de travail."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Regroupement par binômes",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30

    consigne_titre = "Comment ça marche ?"
    consigne_bullets = [
        "12 stagiaires - 6 binômes de 2 personnes",
        "Chaque binôme pioche 1 carte idée reçue : vous en êtes les gardiens",
        "Pendant la journée : les exercices pratiques se font en binôme",
    ]
    consigne_h = estimate_callout_height(consigne_titre, consigne_bullets, COL_W)

    pourquoi_titre = "Pourquoi en binôme ?"
    pourquoi_bullets = [
        "L'apprentissage est plus solide quand on explique à quelqu'un d'autre",
        "Deux regards valent mieux qu'un sur un document à corriger",
    ]
    pourquoi_h = estimate_alert_height(pourquoi_titre, pourquoi_bullets, COL_W)

    col_h = max(consigne_h, pourquoi_h)

    add_callout(
        slide, consigne_titre, consigne_bullets,
        top=top_cols, left=MARGIN_L, width=COL_W, height=col_h,
    )
    add_alert(
        slide, pourquoi_titre, pourquoi_bullets,
        top=top_cols, left=COL_R, width=COL_W,
        alert_type="info",
    )

    accroche = "Prenez 1 minute : échangez avec votre binôme ce que vous faites au quotidien."
    hl_h = estimate_highlight_height(accroche, CONTENT_W)
    add_highlight(
        slide, accroche,
        top=round(top_cols + col_h + 0.25, 2),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    add_notes(
        slide,
        "Constituer les binômes en mélangeant les directions si possible - éviter que deux "
        "personnes du même bureau soient ensemble (trop de connivence, moins d'échanges riches). "
        "Si nombre impair : un trinôme. Distribuer les cartes idées reçues maintenant : "
        "chaque binôme conserve sa carte comme support de l'engagement de fin de journée. "
        "Laisser 2 minutes d'échange avant de commencer le programme.",
    )
    return slide
