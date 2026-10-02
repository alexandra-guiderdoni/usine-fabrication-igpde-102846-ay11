"""Procédures de structure et de navigation de la station 1."""

from igpde_dsfr_components import COL_R, COL_W, MARGIN_L, add_card, add_notes, new_slide
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-1")
    controls = station_controls(block["id"])[:3]
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 1 - Titres, hiérarchie et sommaire",
        fil_ariane="2. Documents accessibles | Station 1",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_card(
        slide,
        "Dans Word - procédure principale",
        [f"{control['id']} - {control['procedure_word']}" for control in controls],
        top=2.30,
        left=MARGIN_L,
        width=COL_W,
        height=3.85,
        body_size=14,
        body_line_spacing=1.08,
        compact=True,
    )
    add_card(
        slide,
        "Dans Writer - complément",
        [f"{control['id']} - {control['procedure_writer']}" for control in controls],
        top=2.30,
        left=COL_R,
        width=COL_W,
        height=3.85,
        body_size=14,
        body_line_spacing=1.08,
        compact=True,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Le volet et le sommaire racontent-ils le même plan ?",
            help_text="Faire ouvrir le volet avant de corriger les styles et rappeler que le sommaire en découle.",
        ),
    )
    return slide
