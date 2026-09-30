"""Slide 02e : organisation des activités - binomes idees recues + ateliers."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_card, add_highlight, add_notes, new_slide,
    estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        fil_ariane="1. Introduction",
        titre="Organisation des activités",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top_cols = 2.30

    consigne_titre = "Activité idées reçues"
    consigne_bullets = [
        "Mettez-vous par deux et piochez une carte idée reçue",
        "Présentez-vous et échangez sur votre quotidien",
        "Confrontez vos cartes : qu'en pensez-vous ?",
        "Présentez vos réflexions au groupe - débat ouvert",
    ]
    ateliers_titre = "Pour les ateliers Word et Web"
    ateliers_bullets = [
        "N'hésitez pas à travailler en binôme",
        "Deux regards repèrent ce qu'un seul ne voit pas",
        "Expliquer à quelqu'un consolide l'apprentissage",
    ]
    card_h = 2.45
    add_card(
        slide, consigne_titre, consigne_bullets,
        top=top_cols, left=MARGIN_L, width=COL_W, height=card_h, compact=True,
    )
    add_card(
        slide, ateliers_titre, ateliers_bullets,
        top=top_cols, left=COL_R, width=COL_W, height=card_h, compact=True,
    )

    accroche = "Première étape : trouvez votre binôme et piochez votre carte !"
    hl_h = estimate_highlight_height(accroche, CONTENT_W)
    add_highlight(
        slide, accroche,
        top=round(top_cols + card_h + 0.45, 2),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    add_notes(
        slide,
        "Constituer les binômes en mélangeant les directions si possible - éviter que deux "
        "personnes du même bureau soient ensemble (échanges plus riches entre services "
        "différents). Si nombre impair : un trinôme. Chaque binôme pioche une carte idée "
        "reçue puis prend 2-3 minutes pour se présenter et échanger sur leur quotidien. "
        "Ensuite ils confrontent leurs cartes et préparent une courte restitution au groupe. "
        "Lancer le débat ouvert après chaque présentation - laisser circuler la parole. "
        "Les binômes ne sont pas imposés pour les ateliers Word/Web mais encouragés : "
        "insister sur le bénéfice mutuel (relecture croisée, explication = ancrage).",
    )
    return slide
