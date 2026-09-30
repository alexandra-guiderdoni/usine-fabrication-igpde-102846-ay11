"""Slide 02ma : c'est quoi l'accessibilité numérique ? (Martine 3+5+6)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, GAP, MARGIN_L,
    Stack,
    add_callout, add_highlight, add_notes,
    estimate_callout_height, estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="L'accessibilité numérique, c'est quoi ?",
        fil_ariane="1. Q1 - C'est quoi | Définition",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    definition = (
        "Rendre possible l'accès à l'information et aux fonctionnalités "
        "numériques aux personnes en situation de handicap, quels que soient "
        "leur matériel, leur logiciel ou leur situation."
    )
    add_highlight(
        slide, definition,
        top=stack.push(estimate_highlight_height(definition, CONTENT_W)),
    )

    titre_quoi = "Tous les contenus sont concernés"
    bullets_quoi = [
        "Sites web, applications, newsletters, courriels",
        "Vidéos, podcasts, visuels animés",
        "Documents bureautiques, PDF, formulaires",
        "Affiches, flyers, plans, QR codes",
    ]
    titre_qui = "Utile pour tous, indispensable pour certains"
    bullets_qui = [
        "Handicap permanent, temporaire ou situationnel",
        "Matériel ancien, connexion lente, écran petit",
        "Environnement bruyant, lumineux ou contraint",
        "Langue étrangère, faible littératie numérique",
    ]
    col_h = max(
        estimate_callout_height(titre_quoi, bullets_quoi, COL_W, line_spacing=1.2, compact=True),
        estimate_callout_height(titre_qui, bullets_qui, COL_W, line_spacing=1.2, compact=True),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_quoi, bullets_quoi,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.2,
        compact=True,
    )
    add_callout(
        slide, titre_qui, bullets_qui,
        top=top_cols, left=COL_R, width=COL_W,
        line_spacing=1.2,
        compact=True,
    )

    add_notes(
        slide,
        "Poser la définition avant tout. Insister sur le fait que l'accessibilité "
        "ne concerne pas que le web ni que le handicap lourd. Faire reformuler par "
        "le groupe : quels supports produisez-vous au quotidien ?",
    )
    return slide
