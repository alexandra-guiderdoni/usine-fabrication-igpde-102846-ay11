"""Export et contrôle du PDF dans la station 5."""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    CONTENT_W,
    MARGIN_L,
    add_card,
    add_notes,
    add_texte_libre,
    new_slide,
)
from sami_slide_data import (
    control_heading,
    sequence_block,
    station_controls,
    station_notes,
)


def build(prs, layouts, ctx):
    block = sequence_block("station-5")
    station = station_controls(block["id"])
    controls = (station[1], station[3])
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 5 - Exporter puis contrôler le PDF",
        fil_ariane="2. Documents accessibles | Station 5",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 5",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    for control, left in zip(controls, (MARGIN_L, COL_R), strict=True):
        add_card(
            slide,
            f"Dans Word - {control_heading(control)}",
            [
                control["regle"],
                control["procedure_word"],
                f"Preuve : {control['preuve']['attendu']}",
            ],
            top=2.30,
            left=left,
            width=COL_W,
            height=3.30,
            body_size=14,
            body_line_spacing=1.3,
            compact=True,
            item_space_after=10,
            emphasize_ids=True,
        )
    add_texte_libre(
        slide,
        "Dans Writer - complément : "
        + " | ".join(control["procedure_writer"] for control in controls),
        top=5.72,
        left=MARGIN_L,
        width=CONTENT_W,
        height=0.90,
        size=14,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Le PDF conserve-t-il le titre, la langue, les balises, les signets et un ordre lisible ?",
            help_text="Faire vérifier les options avant l'export, puis commenter le rapport PAC sans enseigner la remédiation avancée.",
        ),
        structure=True,
    )
    return slide
