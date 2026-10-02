"""Annonce et plan de la partie II."""

from igpde_dsfr_components import add_notes, add_stepper, new_slide
from sami_slide_data import station_blocks, tp_duration


def build(prs, layouts, ctx):
    blocks = station_blocks()
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        fil_ariane="Partie II | Plan",
        titre="Partie II - Documents bureautiques accessibles - TP",
        footer_text=f"{ctx.footer_base} / Partie II",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_stepper(
        slide,
        [block["titre"] for block in blocks],
        top=2.45,
        height=3.65,
    )

    add_notes(
        slide,
        f"Annoncer un TP guidé de {tp_duration()} minutes organisé en "
        f"{len(blocks)} stations. La théorie, la manipulation et la preuve avancent "
        "ensemble dans le document de Sami.",
        structure=True,
    )
    return slide
