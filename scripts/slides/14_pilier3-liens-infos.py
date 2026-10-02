"""Information essentielle portée dans le corps du document."""

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
    block = sequence_block("station-2")
    controls = station_controls(block["id"])[5:]
    control = controls[0]
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Station 2 - L'information essentielle reste dans le corps",
        fil_ariane="2. Documents accessibles | Station 2",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Station 2",
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
        top=3.27,
        left=MARGIN_L,
        width=COL_W,
        height=3.15,
        body_size=14,
        body_line_spacing=1.3,
        compact=True,
        item_space_after=10,
        emphasize_ids=True,
    )
    add_card(
        slide,
        "Dans Writer - complément",
        [control["procedure_writer"], f"Preuve : {control['preuve']['attendu']}"],
        top=3.27,
        left=COL_R,
        width=COL_W,
        height=3.15,
        body_size=14,
        body_line_spacing=1.3,
        compact=True,
        item_space_after=10,
        emphasize_ids=True,
    )

    add_notes(
        slide,
        station_notes(
            block["id"],
            controls=controls,
            question="Le statut reste-t-il compréhensible quand on lit uniquement le corps ?",
            help_text="Faire masquer mentalement l'en-tête et l'arrière-plan, sans recréer de filigrane dans l'exercice.",
        ),
        structure=True,
    )
    return slide
