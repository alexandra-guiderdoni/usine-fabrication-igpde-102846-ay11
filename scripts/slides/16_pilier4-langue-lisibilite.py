"""Mesure du contraste dans la station 3."""

import re

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    MARGIN_L,
    add_card,
    add_highlight,
    add_notes,
    add_pave_chiffre,
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
    controls = station_controls(block["id"])[:1]
    control = controls[0]
    ratios = re.findall(r"(\d+(?:,\d+)?) pour 1", control["regle"])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 3 - Le contraste se mesure",
        fil_ariane="2. Documents accessibles | Station 3",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 3",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        control_heading(control),
        top=2.15,
    )
    add_pave_chiffre(
        slide,
        valeur=f"{ratios[0]}:1",
        label="Texte normal",
        top=3.20,
        left=MARGIN_L,
        width=COL_W,
        height=1.20,
    )
    add_pave_chiffre(
        slide,
        valeur=f"{ratios[1]}:1",
        label="Grand texte et éléments graphiques",
        top=3.20,
        left=COL_R,
        width=COL_W,
        height=1.20,
    )
    add_card(
        slide,
        "Dans Word - procédure principale",
        [control["procedure_word"], control["action_attendue"]],
        top=4.55,
        left=MARGIN_L,
        width=COL_W,
        height=2.20,
        body_size=14,
        compact=True,
        body_line_spacing=1.3,
        item_space_after=10,
        emphasize_ids=True,
    )
    add_card(
        slide,
        "Dans Writer - complément",
        [control["procedure_writer"]],
        top=4.55,
        left=COL_R,
        width=COL_W,
        height=2.20,
        body_size=14,
        compact=True,
        body_line_spacing=1.3,
        item_space_after=10,
        emphasize_ids=True,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Quel seuil s'applique avant même de lire le résultat ?",
            help_text="Faire relever les couleurs, choisir le seuil, puis seulement lancer l'outil de mesure.",
        ),
        structure=True,
    )
    return slide
