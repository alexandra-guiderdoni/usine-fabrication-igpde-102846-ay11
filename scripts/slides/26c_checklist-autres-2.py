"""Checklist progressive des stations 3 et 4."""

from igpde_dsfr_components import COL_R, COL_W, MARGIN_L, add_card, add_notes, new_slide
from sami_slide_data import checklist_item, sequence_block, station_controls


def build(prs, layouts, ctx):
    station_3 = sequence_block("station-3")
    station_4 = sequence_block("station-4")
    groups = (
        (station_3, station_controls(station_3["id"]), MARGIN_L),
        (station_4, station_controls(station_4["id"]), COL_R),
    )
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Checklist progressive - Stations 3 et 4",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    for block, controls, left in groups:
        add_card(
            slide,
            block["titre"],
            [checklist_item(control) for control in controls],
            top=2.30,
            left=left,
            width=COL_W,
            height=4.50,
            body_size=14,
            body_line_spacing=1.2,
            compact=True,
            item_space_after=6,
            emphasize_ids=True,
        )

    add_notes(
        slide,
        "Faire relire les cases renseignées après les stations 3 et 4. "
        "Demander quelle preuve a été conservée pour chaque correction.",
        structure=True,
    )
    return slide
