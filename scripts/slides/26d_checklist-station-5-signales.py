"""Checklist de la station 5 et contrôles signalés."""

from igpde_dsfr_components import COL_R, COL_W, MARGIN_L, add_card, add_notes, new_slide
from sami_slide_data import (
    checklist_item,
    sequence_block,
    signalled_controls,
    station_controls,
)


def build(prs, layouts, ctx):
    station = sequence_block("station-5")
    groups = (
        (station["titre"], station_controls(station["id"]), MARGIN_L),
        ("Contrôles signalés", signalled_controls(), COL_R),
    )
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Checklist progressive - Station 5 et points signalés",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    for title, controls, left in groups:
        add_card(
            slide,
            title,
            [checklist_item(control) for control in controls],
            top=2.30,
            left=left,
            width=COL_W,
            height=4.10,
            body_size=14,
            body_line_spacing=1.05,
            compact=True,
        )

    add_notes(
        slide,
        "Faire terminer la checklist humaine. Les contrôles signalés restent importants, "
        "mais ne deviennent pas des manipulations obligatoires dans ce TP.",
    )
    return slide
