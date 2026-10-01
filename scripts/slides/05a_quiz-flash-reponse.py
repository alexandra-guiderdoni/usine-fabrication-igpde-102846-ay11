"""Slide 05a : réponse au quiz flash sur les documents accessibles."""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    CONTENT_W,
    MARGIN_L,
    Stack,
    add_card,
    add_highlight,
    add_notes,
    estimate_card_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Réponse - le document B est accessible",
        fil_ariane="2. Documents accessibles | Quiz flash",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Réponse",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    texte_hl = (
        "À l'écran, rien ne les distingue. "
        "La différence se trouve dans la structure du fichier."
    )
    stack = Stack(top=2.30, gap=0.35)
    add_highlight(
        slide,
        texte_hl,
        top=stack.push(estimate_highlight_height(texte_hl, CONTENT_W)),
    )

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
    card_h = (
        max(
            estimate_card_height("Document A", bullets_a, COL_W),
            estimate_card_height("Document B", bullets_b, COL_W),
        )
        + 0.35
    )
    cards_top = stack.push(card_h)

    add_card(
        slide,
        titre="Document A",
        contenu=bullets_a,
        top=cards_top,
        left=MARGIN_L,
        width=COL_W,
        height=card_h,
    )
    add_card(
        slide,
        titre="Document B",
        contenu=bullets_b,
        top=cards_top,
        left=COL_R,
        width=COL_W,
        height=card_h,
    )

    add_highlight(
        slide,
        "La structure du fichier détermine ce que NVDA peut restituer.",
        top=stack.cursor,
    )

    add_notes(
        slide,
        "Donner la réponse : le document B. Expliquer que les deux documents "
        "peuvent être identiques à l'écran, mais que NVDA dépend des styles de "
        "titres, des textes alternatifs et d'un nom de fichier explicite.",
    )
    return slide
