"""Slide de cloture : questions et contacts formateurs."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_callout, add_highlight, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Des questions ?",
        fil_ariane="Cloture",
        footer_text=f"{ctx.footer_base}",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.50, gap=0.40)

    add_highlight(
        slide,
        "Merci pour votre participation !",
        top=stack.push(0.90), height=0.90,
    )

    add_callout(
        slide,
        "Vos contacts",
        [
            "Bertrand Matge - bertrand.matge@finances.gouv.fr",
            "Alexandra Guiderdoni - alexandra.guiderdoni@finances.gouv.fr",
        ],
        top=stack.push(1.60), height=1.60,
    )

    add_notes(
        slide,
        "Laisser un temps pour les questions. "
        "Rappeler que les stagiaires peuvent nous contacter par mail "
        "pour toute question post-formation.",
    )
    return slide
