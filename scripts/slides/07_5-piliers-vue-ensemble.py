"""Mission, ressources et productions attendues du TP Sami."""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    CONTENT_W,
    MARGIN_L,
    add_card,
    add_highlight,
    add_notes,
    new_slide,
)
from sami_slide_data import (
    preamble_notes,
    station_blocks,
    tp_duration,
    version_filename,
)


def build(prs, layouts, ctx):
    blocks = station_blocks()
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Votre mission : rendre accessible le guide de Sami",
        fil_ariane="2. Documents accessibles | Préambule",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Mission",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_card(
        slide,
        "Point de départ",
        [
            f"Conseillé : {version_filename('avec_pistes')}",
            f"Variante autonome : {version_filename('inaccessible')}",
            f"{len(blocks)} stations en {tp_duration()} minutes",
        ],
        top=2.30,
        left=MARGIN_L,
        width=COL_W,
        height=2.05,
    )
    add_card(
        slide,
        "Productions à remettre",
        [
            "Le DOCX corrigé par votre binôme",
            "La checklist renseignée au fil des stations",
            "Le PDF exporté puis contrôlé",
        ],
        top=2.30,
        left=COL_R,
        width=COL_W,
        height=2.05,
    )
    add_highlight(
        slide,
        "Checklist dès le départ ; cartes WCAG reliées informellement à chaque contrôle.",
        top=4.72,
        left=MARGIN_L,
        width=CONTENT_W,
    )

    add_notes(slide, preamble_notes())
    return slide
