"""Slide 01a : Intervenante - Alexandra Guiderdoni."""

from igpde_dsfr_components import (
    add_callout, add_card, add_notes, new_slide,
    MARGIN_L, CONTENT_W,
)

PHOTO_W = 3.5
PHOTO_H = 4.2
BIO_LEFT = round(MARGIN_L + PHOTO_W + 0.28, 2)
BIO_W = round(CONTENT_W - PHOTO_W - 0.28, 2)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Alexandra Guiderdoni",
        fil_ariane="Intervenants",
        footer_text=f"{ctx.footer_base} / Intervenants",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_card(
        slide,
        titre="Photo à insérer",
        contenu=[],
        top=2.4,
        left=MARGIN_L,
        width=PHOTO_W,
        height=PHOTO_H,
    )

    add_callout(
        slide,
        "Chef de projet - Mission Ingénierie du Web, SG-SNUM",
        [
            "Spécialisée dans les technologies web et l'accessibilité numérique",
            "Expérience : Ministère des affaires étrangères, ESN",
            "DU-RAN (diplôme universitaire référent accessibilité numérique), 1re session 2024",
            "Formée à l'audit d'accessibilité numérique RGAA",
            "alexandra.guiderdoni@finances.gouv.fr",
        ],
        top=2.4,
        left=BIO_LEFT,
        width=BIO_W,
    )

    add_notes(slide, "Présentation d'Alexandra : parcours, spécialisation accessibilité, DU-RAN.")
    return slide
