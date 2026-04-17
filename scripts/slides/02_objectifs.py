"""Slide 2 : objectifs pédagogiques (callout 4 points)."""

from igpde_dsfr_components import add_callout, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        titre="Objectifs pédagogiques",
        footer_text=f"{ctx.footer_base} / Objectifs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_callout(
        slide,
        "À l\u2019issue de cette formation, les stagiaires sauront :",
        [
            "Identifier les critères RGAA 4.1.2 applicables",
            "Produire un document bureautique accessible",
            "Auditer une page web avec les outils standards",
            "Remédier aux non-conformités détectées",
        ],
        top=3.35, height=2.5,
    )

    add_notes(
        slide,
        "Présenter les 4 objectifs, insister sur le caractère opérationnel.",
    )
    return slide
