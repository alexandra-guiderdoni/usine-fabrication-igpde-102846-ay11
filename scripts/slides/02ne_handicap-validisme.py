"""Slide 02o : handicap, contexte et validisme.

Règles neuropédagogie appliquées :
- R3 : WIIFM - donner l'échelle du sujet
- R16 : visuel - 3 chiffres clés plutôt qu'un bloc explicatif
- R15 : jargon traduit - validisme expliqué par les effets concrets
"""

from igpde_dsfr_components import (
    CONTENT_W,
    GAP,
    MARGIN_L,
    Stack,
    add_card,
    add_callout,
    add_highlight,
    add_notes,
    estimate_card_height,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Handicap : sortir de l'angle mort",
        fil_ariane="1. Q2 - Pour qui | Chiffres",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.20)

    message = (
        "L'accessibilité n'est pas une faveur : c'est une condition d'accès "
        "équitable à l'information."
    )
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    chiffres_cles = [
        (
            "1/5",
            "1 personne sur 5 est en situation de handicap ou connaît un trouble invalidant.",
        ),
        ("85%", "des handicaps sont acquis au cours de la vie"),
        (
            "1er",
            "Le handicap est le 1er facteur de discrimination selon le Défenseur des droits",
        ),
    ]
    item_w = (CONTENT_W - GAP * 2) / 3
    card_h = (
        max(
            estimate_card_height(titre, texte, item_w, compact=True)
            for titre, texte in chiffres_cles
        )
        + 0.12
    )
    cards_top = stack.push(card_h)
    for i, (titre_carte, texte_carte) in enumerate(chiffres_cles):
        left = MARGIN_L + i * (item_w + GAP)
        add_card(
            slide,
            titre_carte,
            texte_carte,
            top=cards_top,
            left=left,
            width=item_w,
            height=card_h,
            title_size=24,
            compact=True,
        )

    titre = "Validisme : le piège à déconstruire"
    bullets = [
        "Penser le public comme valide par défaut",
        "Confondre bonne intention et accès réel",
        "Oublier les handicaps invisibles, acquis ou temporaires",
    ]
    add_callout(
        slide,
        titre,
        bullets,
        top=stack.push(
            estimate_callout_height(titre, bullets, CONTENT_W, compact=True)
        ),
        line_spacing=1.2,
        compact=True,
    )

    add_notes(
        slide,
        "Les chiffres viennent du guide Accessibiliser sa communication. "
        "Ne pas transformer cette slide en cours théorique sur le validisme. "
        "Objectif : faire comprendre que l'accessibilité de la communication répond à des situations nombreuses, "
        "souvent invisibles, et qu'une bonne intention ne garantit pas l'accès effectif.",
    )
    return slide
