"""Vue d'ensemble de l'étape 5."""

from igpde_dsfr_components import add_highlight, add_notes, add_tableau, new_slide
from sami_slide_data import sequence_block, station_controls, station_notes


def build(prs, layouts, ctx):
    block = sequence_block("station-5")
    controls = station_controls(block["id"])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre=f"Étape 5 - {block['titre']}",
        fil_ariane="2. Documents accessibles | Étape 5",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Étape 5",
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
        "Les outils automatiques filtrent ; la checklist et la vérification humaine concluent.",
        top=5.55,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Qu'est-ce que l'outil automatique ne peut pas décider à votre place ?",
            help_text="Faire distinguer propriété, vérification Word, export PDF et contrôle post-export.",
        ),
        structure=True,
    )
    return slide
