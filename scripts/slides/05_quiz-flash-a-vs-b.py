"""Slide 05 : Quiz flash - Lequel est accessible ?

Règles neuropédagogie appliquées :
- R3 : Préparation mentale par une question ouverte
- R6 : Closure de Zeigarnik (boucle ouverte) pour maintenir l'engagement
- R16 : Pause délibérée avant la réponse pour la récupération active
"""

from igpde_dsfr_components import (
    COL_R, COL_W, CONTENT_W, MARGIN_L, Stack,
    add_card, add_highlight, add_notes,
    estimate_card_height, estimate_highlight_height, new_slide,
)


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
    stack = Stack(top=2.30, gap=0.35)
    add_highlight(slide, texte_hl,
                  top=stack.push(estimate_highlight_height(texte_hl, CONTENT_W)))

    bullets_a = [
        "Titres mis en gras, police Arial 16",
        "Image sans description",
        "Fichier nommé Document1.docx",
    ]
    bullets_b = [
        "Titres avec le style « Titre 1 »",
        "Image avec texte alternatif",
        "Fichier nommé rapport-bilan-2024.docx",
    ]

    card_h = max(
        estimate_card_height("Document A", bullets_a, COL_W),
        estimate_card_height("Document B", bullets_b, COL_W),
    ) + 0.5
    cards_top = stack.push(card_h)

    add_card(slide, titre="Document A", contenu=bullets_a,
             top=cards_top, left=MARGIN_L, width=COL_W, height=card_h)
    add_card(slide, titre="Document B", contenu=bullets_b,
             top=cards_top, left=COL_R, width=COL_W, height=card_h)

    add_highlight(slide, "Votre réponse ?",
                  top=stack.cursor)

    add_notes(
        slide,
        "Laisser 30 secondes pour que chacun vote. Demander à main levée. "
        "Ne pas donner la réponse maintenant - la curiosité crée l'attention. "
        "Zeigarnik : la boucle ouverte maintient l'engagement.",
    )
    return slide
