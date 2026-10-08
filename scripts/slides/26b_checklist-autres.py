"""Checklist progressive des étapes 1 et 2."""

from igpde_dsfr_components import COL_R, COL_W, MARGIN_L, add_card, add_notes, new_slide
from sami_slide_data import checklist_item, sequence_block, station_controls


def build(prs, layouts, ctx):
    station_1 = sequence_block("station-1")
    station_2 = sequence_block("station-2")
    groups = (
        (station_1, station_controls(station_1["id"]), MARGIN_L),
        (station_2, station_controls(station_2["id"]), COL_R),
    )
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Checklist progressive - Étapes 1 et 2",
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
            body_line_spacing=1.15,
            compact=True,
            item_space_after=4,
            emphasize_ids=True,
        )

    add_notes(
        slide,
        "Faire relire les cases renseignées après les deux premières étapes. "
        "La formulation et l'ordre proviennent de la matrice et de la checklist distribuée.",
        structure=True,
    )
    return slide
