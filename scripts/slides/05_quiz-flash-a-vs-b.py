"""Slide 05 : Quiz flash - Lequel est accessible ?

Règles neuropédagogie appliquées :
- R3 : Préparation mentale par une question ouverte
- R6 : Closure de Zeigarnik (boucle ouverte) pour maintenir l'engagement
- R16 : Pause délibérée avant la réponse pour la récupération active
"""

from pptx.enum.text import PP_ALIGN

from igpde_dsfr_components import (
    COL_R, COL_W, CONTENT_W, MARGIN_L,
    add_highlight, add_image, add_notes, add_texte_libre,
    estimate_highlight_height, new_slide,
)

IMAGE_W = 2.15
IMAGE_TOP = 3.45
LABEL_TOP = 3.00


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Quiz - lequel de ces deux documents est accessible ?",
        fil_ariane="2. Documents accessibles | Quiz flash",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    texte_hl = "Ils sont visuellement identiques. Lequel préférez-vous pour NVDA ?"
    add_highlight(slide, texte_hl,
                  top=2.15)

    documents = [
        ("Document A", "scripts/images/quiz-document-a-dsfr.png", MARGIN_L),
        ("Document B", "scripts/images/quiz-document-b-dsfr.png", COL_R),
    ]
    for label, image_path, col_left in documents:
        add_texte_libre(
            slide, label,
            top=LABEL_TOP, left=col_left, width=COL_W, height=0.40,
            size=18, bold=True, align=PP_ALIGN.CENTER,
        )
        add_image(
            slide, image_path,
            top=IMAGE_TOP,
            left=col_left + (COL_W - IMAGE_W) / 2,
            width=IMAGE_W,
            alt_text=(
                f"Aperçu stylisé du {label.lower()}, visuellement identique "
                "à l'autre document."
            ),
        )

    add_notes(
        slide,
        "Laisser 30 secondes pour que chacun vote. Demander à main levée. "
        "Ne pas donner la réponse maintenant - la curiosité crée l'attention. "
        "Zeigarnik : la boucle ouverte maintient l'engagement.",
    )
    return slide
