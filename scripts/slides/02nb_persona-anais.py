"""Slide 02nb : persona Anaïs - malvoyance (DMLA précoce)."""

from igpde_dsfr_components import (
    BLEU_INFO, BLEU_INFO_CLAIR, CONTENT_W, GAP, MARGIN_L,
    add_callout, add_encadre, add_image, add_notes, new_slide,
)

PHOTO_W = 2.2
BIO_LEFT = round(MARGIN_L + PHOTO_W + 0.30, 2)
BIO_W = round(CONTENT_W - PHOTO_W - 0.30, 2)

def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Anaïs, gestionnaire RH - malvoyance",
        fil_ariane="1. Q2 - Pour qui | Anaïs",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_image(
        slide,
        "scripts/images/image10.png",
        top=2.20, left=MARGIN_L, width=PHOTO_W, height=PHOTO_W,
        alt_text="Portrait illustratif - Anaïs",
    )

    titre_besoin = "Ses besoins au quotidien"
    bullets_besoin = [
        "Agrandir la taille des textes et des interfaces",
        "Contraste suffisant entre texte et fond (ratio 4.5:1 minimum)",
        "Pouvoir naviguer sans dépendre uniquement des couleurs",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
        compact=True,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Percevoir",
        couleur_fond=BLEU_INFO_CLAIR, couleur_accent=BLEU_INFO,
    )

    outils_top = 5.05
    item_w = (CONTENT_W - GAP * 2) / 3

    outils = [
        "Agrandissement",
        "Contraste renforcé",
        "Synthèse vocale",
    ]
    for i, label in enumerate(outils):
        left = MARGIN_L + i * (item_w + GAP)
        add_encadre(
            slide, top=outils_top, left=left, width=item_w, height=1.35,
            titre=label,
            couleur_fond=BLEU_INFO_CLAIR, couleur_accent=BLEU_INFO,
        )

    add_notes(
        slide,
        "Anaïs a une DMLA précoce diagnostiquée il y a 10 ans. "
        "Ce profil illustre la déficience visuelle. Insister sur le fait "
        "que le contraste et la taille de texte sont des leviers que "
        "le communicant maîtrise directement dans ses documents.",
    )
    return slide
