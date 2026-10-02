"""Vue d'ensemble de la station 4."""

from igpde_dsfr_components import add_highlight, add_notes, add_tableau, new_slide
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-4")
    controls = station_controls(block["id"])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre=f"Station 4 - {block['titre']}",
        fil_ariane="2. Documents accessibles | Station 4",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 4",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_tableau(
        slide,
        ["ID", "Niveau", "Points travaillés"],
        [
            [control["id"], control["niveau"], control["intitule"]]
            for control in controls
        ],
        top=2.30,
        col_widths=[1.15, 1.25, 9.88],
        row_h=0.62,
    )
    add_highlight(
        slide,
        "Corriger les styles sources : la langue et la lisibilité se règlent à l'échelle du document.",
        top=5.55,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Le réglage est-il porté par les propriétés et les styles, ou seulement par l'apparence ?",
            help_text="Faire corriger le style source et la langue du passage plutôt que les paragraphes un par un.",
        ),
    )
    return slide
