"""Vrai texte et liens compréhensibles de l'étape 2."""

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
    block = sequence_block("station-2")
    controls = station_controls(block["id"])[3:5]
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Étape 2 - Vrai texte et liens compréhensibles",
        fil_ariane="2. Documents accessibles | Étape 2",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Étape 2",
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
        height=2.75,
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
        height=2.75,
        body_size=14,
        body_line_spacing=1.3,
        compact=True,
        item_space_after=10,
        emphasize_ids=True,
    )
    add_highlight(
        slide,
        "Preuve : le texte se sélectionne et chaque lien reste clair hors contexte.",
        top=5.43,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Le texte peut-il être sélectionné et le lien compris tout seul ?",
            help_text="Faire tester la sélection du texte puis lire uniquement le libellé du lien.",
        ),
        structure=True,
    )
    return slide
