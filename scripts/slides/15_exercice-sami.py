"""Vue d'ensemble de la station 3."""

from igpde_dsfr_components import add_highlight, add_notes, add_tableau, new_slide
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-3")
    controls = station_controls(block["id"])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre=f"Station 3 - {block['titre']}",
        fil_ariane="2. Documents accessibles | Station 3",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 3",
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
        row_h=0.66,
    )
    add_highlight(
        slide,
        "Mesurer, rendre l'information indépendante de la couleur, puis vérifier la structure.",
        top=5.40,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Quelle preuve distingue une impression visuelle d'un contrôle vérifiable ?",
            help_text="Faire choisir le seuil avant la mesure et rappeler que le graphique se reconstruit directement dans Word.",
        ),
    )
    return slide
