"""Casse et sigles de la station 4."""

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
    controls = station_controls(block["id"])[2:]
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 4 - Casse, accents et sigles",
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
        body_line_spacing=1.3,
        compact=True,
        item_space_after=10,
        emphasize_ids=True,
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
        body_line_spacing=1.3,
        compact=True,
        item_space_after=10,
        emphasize_ids=True,
    )
    add_highlight(
        slide,
        "Preuve : texte source accentué, première occurrence développée et majuscules contrôlées.",
        top=5.57,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Le texte reste-t-il correctement écrit sous son apparence visuelle ?",
            help_text="Faire restaurer la saisie normale avant d'appliquer la casse, puis rechercher la première occurrence du sigle.",
        ),
        structure=True,
    )
    return slide
