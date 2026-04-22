"""Slide 02f : icebreaker - introduction aux idées reçues sur l'accessibilité numérique."""

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
        titre="Ensemble, faisons tomber les préjugés !",
        footer_text=f"{ctx.footer_base} / Accueil",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.30)

    accroche = (
        "L'accessibilité numérique, ça fait peur... mais souvent pour de mauvaises raisons."
    )
    hl_h = estimate_highlight_height(accroche, CONTENT_W)
    add_highlight(slide, accroche, top=stack.push(hl_h), left=MARGIN_L, width=CONTENT_W)

    consigne_titre = "Activité : vrai ou faux ?"
    consigne_bullets = [
        "Vous avez chacun une carte avec une idée reçue",
        "Lisez-la, décidez : vrai ou faux ?",
        "On révèle ensemble le décryptage, carte par carte",
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
        "Les cartes ont été distribuées au moment du regroupement en binômes. "
        "Laisser 30 secondes de réflexion silencieuse, puis demander qui dit 'vrai' et qui dit 'faux' "
        "avant d'afficher la slide de décryptage. Ne pas corriger immédiatement - laisser le groupe débattre. "
        "Objectif : casser les freins avant même de commencer la théorie.",
    )
    return slide
