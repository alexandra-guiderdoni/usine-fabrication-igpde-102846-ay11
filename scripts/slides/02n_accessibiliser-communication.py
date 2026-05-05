"""Slide 02n : cap du module 1 - accessibiliser sa communication.

Règles neuropédagogie appliquées :
- R3 : WIIFM - relier le cadre légal aux gestes de communication
- R5 : chunking - 3 questions et 4 familles de supports
- R21 : échafaudage - poser le cap avant les référentiels
"""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    CONTENT_W,
    MARGIN_L,
    Stack,
    add_alert,
    add_callout,
    add_highlight,
    add_notes,
    estimate_alert_height,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Accessibiliser sa communication : le cap",
        fil_ariane="1. Introduction | Communication accessible",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.18)

    message = (
        "But de la formation : transformer une intention d'inclusion en contenus "
        "que les publics peuvent lire, comprendre et utiliser."
    )
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    questions_titre = "3 questions à garder en tête"
    questions_bullets = [
        "Qui risque d'être empêché par ce support ?",
        "Quel autre chemin donne accès à la même information ?",
        "Quelle règle simple peut être appliquée dès maintenant ?",
    ]
    supports_titre = "Les supports concernés"
    supports_bullets = [
        "Web : site, application, newsletter, mails",
        "Médias : vidéo, podcast, visuel animé",
        "Documents : PDF, bureautique, formulaires",
        "Imprimés : affiche, flyer, plan, QR code",
    ]
    col_h = max(
        estimate_callout_height(questions_titre, questions_bullets, COL_W, line_spacing=1.05),
        estimate_alert_height(supports_titre, supports_bullets, COL_W, line_spacing=1.05),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide,
        questions_titre,
        questions_bullets,
        top=top_cols,
        left=MARGIN_L,
        width=COL_W,
        line_spacing=1.05,
    )
    add_alert(
        slide,
        supports_titre,
        supports_bullets,
        top=top_cols,
        left=COL_R,
        width=COL_W,
        alert_type="info",
        line_spacing=1.05,
    )

    add_notes(
        slide,
        "Cette slide sert de cadrage. Le guide source est une introduction utile, "
        "pas un référentiel complet ni un substitut à une formation. "
        "Faire reformuler par le groupe : accessibiliser une communication, "
        "ce n'est pas seulement corriger un site web, c'est penser le support final et l'usage réel.",
    )
    return slide
