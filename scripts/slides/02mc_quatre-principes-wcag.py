"""Slide 02mc : les 4 principes WCAG (Percevoir, Utiliser, Comprendre, Compatible)."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L, TOP_CONTENT,
    Stack,
    add_card, add_highlight, add_notes,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="4 principes pour tout retenir",
        fil_ariane="1. Q1 - C'est quoi | 4 principes WCAG",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=TOP_CONTENT, gap=0.30)

    intro = (
        "Les WCAG reposent sur 4 principes. "
        "Chacun se résume en une question à poser devant tout contenu."
    )
    add_highlight(slide, intro, top=stack.push(estimate_highlight_height(intro)))

    principes = [
        ("Percevoir", "L'information reste-t-elle disponible si je ne vois pas ou n'entends pas ?"),
        ("Utiliser", "Puis-je naviguer et agir sans souris, sans geste imposé ?"),
        ("Comprendre", "Les mots, formulaires et comportements sont-ils prévisibles ?"),
        ("Compatible", "Les aides techniques peuvent-elles interpréter l'interface ?"),
    ]

    n = len(principes)
    card_w = (CONTENT_W - GAP * (n - 1)) / n
    card_h = 2.8
    card_top = stack.push(card_h)

    for i, (titre, contenu) in enumerate(principes):
        left = MARGIN_L + i * (card_w + GAP)
        add_card(slide, titre, contenu,
                 top=card_top, left=left, width=card_w, height=card_h,
                 numero=i + 1, title_size=14, body_size=14)

    add_notes(
        slide,
        "Mnémonique : PUCC (Percevoir, Utiliser, Comprendre, Compatible). "
        "Faire reformuler par le groupe : 'Si je suis aveugle, quel principe est en jeu ?' "
        "(Percevoir). 'Si je ne peux pas utiliser la souris ?' (Utiliser). "
        "Ces 4 principes structurent le RGAA et reviendront dans les modules suivants.",
    )
    return slide
