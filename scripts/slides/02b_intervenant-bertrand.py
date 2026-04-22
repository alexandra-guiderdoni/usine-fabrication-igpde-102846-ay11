"""Slide 01b : Intervenant - Bertrand Matge."""

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
        titre="Bertrand Matge",
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
        "Responsable pôle support web - Mission Ingénierie du Web, SG-SNUM",
        [
            "Service du numérique - 139 rue de Bercy, 75012 Paris",
            "Formateur Opquast certifié, référent Assurance Qualité Web",
            "Forme et sensibilise à l'accessibilité depuis plusieurs années",
            "Passionné par la conception inclusive et l'expérience utilisateur",
            "Formé à l'audit d'accessibilité numérique",
            "bertrand.matge@finances.gouv.fr",
        ],
        top=2.4,
        left=BIO_LEFT,
        width=BIO_W,
    )

    add_notes(slide, "Présentation de Bertrand : parcours SIRCOM, Opquast, sensibilisation accessibilité.")
    return slide
