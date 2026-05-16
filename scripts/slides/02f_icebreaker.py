"""Slide 02f : icebreaker - lancement du debat idees recues en binomes."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    add_highlight, add_alert, add_notes, new_slide,
    estimate_highlight_height, estimate_alert_height,
    Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        fil_ariane="1. Introduction | Idées reçues",
        titre="Ensemble, faisons tomber les préjugés !",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.30)

    accroche = (
        "L'accessibilité numérique, ça fait peur ... mais souvent pour de mauvaises raisons."
    )
    hl_h = estimate_highlight_height(accroche, CONTENT_W)
    add_highlight(slide, accroche, top=stack.push(hl_h), left=MARGIN_L, width=CONTENT_W)

    consigne_titre = "Activité : vrai ou faux ?"
    consigne_bullets = [
        "En binôme, confrontez vos cartes : vrai ou faux ?",
        "Échangez vos arguments, préparez votre position",
        "Chaque binôme présente sa carte au groupe - débat ouvert",
    ]
    ah = estimate_alert_height(consigne_titre, consigne_bullets, CONTENT_W)
    add_alert(
        slide,
        consigne_titre,
        consigne_bullets,
        top=stack.push(ah),
        left=MARGIN_L,
        width=CONTENT_W,
        alert_type="info",
    )

    add_notes(
        slide,
        "Les cartes ont été piochées au moment de la constitution des binômes. "
        "Laisser 2-3 minutes aux binômes pour discuter entre eux de leurs cartes. "
        "Puis chaque binôme présente sa carte et dit ce qu'il en pense - le reste du groupe "
        "réagit librement. Ne pas corriger immédiatement - laisser le débat s'installer "
        "avant d'afficher la slide de décryptage. "
        "Objectif : casser les freins avant même de commencer la théorie.",
    )
    return slide
