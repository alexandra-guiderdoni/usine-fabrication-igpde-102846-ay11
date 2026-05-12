"""Slide 1 : couverture de la formation."""

from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

from igpde_dsfr_components import (
    BLEU_FRANCE, FONT,
    _apply_text, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="couverture",
        titre="Accessibilité numérique",
        footer_text="Institut de la Gestion publique et du Développement économique",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    sub_box = slide.shapes.add_textbox(
        Inches(5.8), Inches(5.3), Inches(7.1), Inches(0.35),
    )
    sub_box.name = "DSFR-couverture-soustitre"
    _apply_text(
        sub_box.text_frame,
        "Formation 102638 | Bureautique et web",
        font=FONT, size=14, bold=True, color=BLEU_FRANCE,
        align=PP_ALIGN.RIGHT,
    )

    add_notes(slide, "Slide de couverture - accueil des stagiaires, tour de table.")
    return slide
