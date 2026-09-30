"""Slide 2 : objectifs pédagogiques - 3 objectifs du catalogue 102846."""

from igpde_dsfr_components import (
    COL_W,
    MARGIN_L,
    add_callout,
    add_image,
    add_notes,
    add_qrcode,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_soustitre",
        fil_ariane="1. Introduction",
        titre="Objectifs pédagogiques",
        footer_text=f"{ctx.footer_base} / Objectifs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_callout(
        slide,
        "",
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
        top=2.10,
        left=7.53,
        width=3.82,
        alt_text=(
            "Affiche du Service d'information du Gouvernement pour les 20 ans "
            "de la loi handicap. Un ordinateur à l'écran inversé illustre un "
            "outil inaccessible. L'affiche invite les agents publics à utiliser "
            "les outils disponibles sur accessibilite.gouv.fr."
        ),
    )

    add_qrcode(
        slide,
        "_assets/qrcode-info-gouv-accessibilite.png",
        url="https://www.info.gouv.fr/accessibilite",
        top=5.30,
        left=MARGIN_L,
        size=1.12,
        label_width=COL_W - 1.26,
        url_size=10,
    )

    add_notes(
        slide,
        "Objectifs repris mot pour mot de la fiche catalogue 102846. "
        "Présenter les 3 objectifs, insister sur le caractère opérationnel : "
        "cette formation débouche sur des gestes concrets, pas seulement de la théorie.",
    )
    return slide
