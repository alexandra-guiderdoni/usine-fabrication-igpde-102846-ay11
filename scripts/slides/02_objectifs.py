"""Slide 2 : objectifs pédagogiques - 3 objectifs du catalogue 102638."""

from igpde_dsfr_components import (
    add_callout, add_image, add_notes, new_slide,
    MARGIN_L, COL_W, COL_R,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        fil_ariane="1. Introduction",
        titre="Objectifs pédagogiques",
        footer_text=f"{ctx.footer_base} / Objectifs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_callout(
        slide,
        "Cette formation vous permettra de :",
        [
            "Expliquer les enjeux de l'accessibilité numérique et son cadre légal"
            " dans le contexte de la communication",
            "Identifier et évaluer les principales erreurs d'accessibilité",
            "Rendre des contenus numériques accessibles",
        ],
        top=2.30,
        left=MARGIN_L,
        width=COL_W,
        line_spacing=1.5,
    )

    add_image(
        slide,
        "_assets/affiche-sig-handicap.jpg",
        top=2.10, left=7.53, width=3.82,
        alt_text="Affiche du SIG pour les 20 ans de la loi handicap. Imaginez un quotidien où rien n'est vraiment pensé pour vous. Ordinateur avec un écran inversé.",
    )

    add_image(
        slide,
        "_assets/qrcode-info-gouv-accessibilite.png",
        top=5.30, left=9.50, width=1.30, height=1.30,
        alt_text="QR code : https://www.info.gouv.fr/accessibilite",
    )

    add_notes(
        slide,
        "Objectifs repris mot pour mot de la fiche catalogue 102638. "
        "Présenter les 3 objectifs, insister sur le caractère opérationnel : "
        "cette formation débouche sur des gestes concrets, pas seulement de la théorie.",
    )
    return slide
