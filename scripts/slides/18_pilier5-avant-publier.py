"""Tableau de données simple dans la station 3."""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    MARGIN_L,
    add_card,
    add_highlight,
    add_notes,
    new_slide,
)
from sami_slide_data import (
    control_heading,
    sequence_block,
    station_controls,
    station_notes,
)


def build(prs, layouts, ctx):
    block = sequence_block("station-3")
    controls = station_controls(block["id"])[2:]
    control = controls[0]
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 3 - Un tableau de données simple",
        fil_ariane="2. Documents accessibles | Station 3",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 3",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        control_heading(control),
        top=2.20,
    )
    add_card(
        slide,
        "Dans Word - procédure principale",
        [control["regle"], control["procedure_word"], control["action_attendue"]],
        top=3.30,
        left=MARGIN_L,
        width=COL_W,
        height=2.75,
        body_size=14,
        body_line_spacing=1.08,
        compact=True,
    )
    add_card(
        slide,
        "Dans Writer - complément",
        [control["procedure_writer"], f"Preuve : {control['preuve']['attendu']}"],
        top=3.30,
        left=COL_R,
        width=COL_W,
        height=2.75,
        body_size=14,
        body_line_spacing=1.08,
        compact=True,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Chaque cellule appartient-elle à une grille de données simple ?",
            help_text="Faire distinguer tableau de données et mise en page avant d'ouvrir les propriétés du tableau.",
        ),
    )
    return slide
