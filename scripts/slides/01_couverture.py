"""Slide 1 : couverture de la formation."""

from igpde_dsfr_components import (
    BLEU_FRANCE,
    FONT,
    _apply_text,
    add_notes,
    new_slide,
)
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="couverture",
        titre="L'accessibilité numérique pour la bureautique et le web",
        footer_text="Institut de la Gestion publique et du Développement économique",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    sub_box = slide.shapes.add_textbox(
        Inches(5.8),
        Inches(5.95),
        Inches(7.1),
        Inches(0.35),
    )
    sub_box.name = "DSFR-couverture-soustitre"
    _apply_text(
        sub_box.text_frame,
        f"{ctx.footer_base} | Bureautique et web",
        font=FONT,
        size=14,
        bold=True,
        color=BLEU_FRANCE,
        align=PP_ALIGN.RIGHT,
    )

    add_notes(slide, "Slide de couverture - accueil des stagiaires et installation.")
    return slide
