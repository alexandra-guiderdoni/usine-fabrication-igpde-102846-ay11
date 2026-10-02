"""Vue d'ensemble de la station 2."""

from igpde_dsfr_components import add_highlight, add_notes, add_tableau, new_slide
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-2")
    controls = station_controls(block["id"])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre=f"Station 2 - {block['titre']}",
        fil_ariane="2. Documents accessibles | Station 2",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 2",
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
        top=2.20,
        col_widths=[1.15, 1.25, 9.88],
        row_h=0.49,
    )
    add_highlight(
        slide,
        "Choisir le traitement selon l'usage : informative, complexe, décorative ou textuelle.",
        top=5.82,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="L'information reste-t-elle compréhensible si l'image ou le contexte disparaît ?",
            help_text="Faire identifier la fonction de chaque contenu avant d'ouvrir le volet du texte alternatif.",
        ),
        structure=True,
    )
    return slide
