"""Slide 2 : objectifs pédagogiques - 3 objectifs du catalogue 102638."""

from igpde_dsfr_components import (
    add_callout, add_card, add_notes, new_slide,
    estimate_callout_height, MARGIN_L, COL_W, COL_R,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        titre="Objectifs pédagogiques",
        footer_text=f"{ctx.footer_base} / Objectifs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    callout_titre = "Cette formation vous permettra de :"
    callout_bullets = [
        "Expliquer les enjeux de l'accessibilité numérique et son cadre légal"
        " dans le contexte de la communication",
        "Identifier et évaluer les principales erreurs d'accessibilité",
        "Rendre des contenus numériques accessibles",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=2.30,
        left=MARGIN_L,
        width=COL_W,
    )

    add_card(
        slide,
        titre="Image à insérer",
        contenu=[],
        top=2.30,
        left=COL_R,
        width=COL_W,
        height=estimate_callout_height(callout_titre, callout_bullets, COL_W),
    )

    add_notes(
        slide,
        "Objectifs repris mot pour mot de la fiche catalogue 102638. "
        "Présenter les 3 objectifs, insister sur le caractère opérationnel : "
        "cette formation débouche sur des gestes concrets, pas seulement de la théorie.",
    )
    return slide
