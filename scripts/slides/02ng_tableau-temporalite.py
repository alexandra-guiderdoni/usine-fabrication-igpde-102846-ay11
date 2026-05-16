"""Slide 02ng : tableau handicap x temporalité (permanent, temporaire, situationnel, vieillissement)."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    Stack,
    add_highlight, add_image, add_notes,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Le spectre du handicap",
        fil_ariane="1. Q2 - Pour qui | Spectre du handicap",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.30)

    message = (
        "Le handicap n'est pas binaire. "
        "Il peut être permanent, temporaire, situationnel "
        "ou lié au vieillissement."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    img_w = 4.5
    img_h = img_w * 0.784
    add_image(
        slide,
        "scripts/images/image6.png",
        top=stack.push(img_h),
        left=MARGIN_L + (CONTENT_W - img_w) / 2,
        width=img_w,
        alt_text=(
            "Tableau à 5 colonnes (permanent, temporaire, situationnel, "
            "vieillissement) et 4 lignes (manipulation, vision, cognition, "
            "mobilité). Exemples : une seule main, bras cassé, bébé dans "
            "les bras, douleurs ; visibilité faible, oeil gonflé, lumière "
            "tamisée, vue qui baisse ; amnésie, fatigue, première "
            "utilisation, Alzheimer ; fauteuil roulant, jambe cassée, "
            "chaussures inconfortables, canne."
        ),
    )

    add_notes(
        slide,
        "Laisser les stagiaires découvrir le tableau. Demander : "
        "dans quelle colonne vous êtes-vous déjà retrouvés ? "
        "Tout le monde a déjà été en situation de handicap temporaire "
        "ou situationnel. C'est là que le déclic se produit : "
        "l'accessibilité concerne tout le monde.",
    )
    return slide
