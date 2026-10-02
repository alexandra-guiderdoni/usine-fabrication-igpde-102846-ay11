"""Langues et styles typographiques de la station 4."""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    MARGIN_L,
    add_card,
    add_highlight,
    add_notes,
    new_slide,
)
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-4")
    controls = station_controls(block["id"])[:2]
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 4 - Langues et styles typographiques",
        fil_ariane="2. Documents accessibles | Station 4",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 4",
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
        height=2.95,
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
        height=2.95,
        body_size=14,
        body_line_spacing=1.08,
        compact=True,
    )
    add_highlight(
        slide,
        "Preuve : langue cohérente, corps à 12 points minimum, interligne 1,15 et alignement à gauche.",
        top=5.57,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Une correction du style Normal améliore-t-elle tout le corps ?",
            help_text="Faire distinguer la langue principale de celle du passage, puis modifier le style plutôt que chaque paragraphe.",
        ),
    )
    return slide
