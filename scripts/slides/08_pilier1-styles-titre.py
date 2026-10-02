"""Vue d'ensemble de la station 1."""

from igpde_dsfr_components import add_highlight, add_notes, add_tableau, new_slide
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-1")
    controls = station_controls(block["id"])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre=f"Station 1 - {block['titre']}",
        fil_ariane="2. Documents accessibles | Station 1",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 1",
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
        top=2.25,
        col_widths=[1.15, 1.25, 9.88],
        row_h=0.56,
    )
    add_highlight(
        slide,
        "Manipuler la structure, puis prouver le résultat dans le volet et le sommaire.",
        top=5.75,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Comment prouver que le document est réellement navigable ?",
            help_text="Faire distinguer le rôle du texte de son apparence avant d'ouvrir le ruban.",
        ),
        structure=True,
    )
    return slide
