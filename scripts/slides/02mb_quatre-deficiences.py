"""Slide 02mb : c'est pour qui - 4 familles de déficiences (Martine 8+9)."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L,
    Stack,
    add_card, add_highlight, add_notes,
    estimate_card_height, estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="C'est pour qui ? 4 familles de besoins",
        fil_ariane="1. Introduction | Qui",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "Chaque type de handicap implique des besoins concrets "
        "que vos contenus doivent prendre en compte."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    cards = [
        (
            "Visuelle",
            [
                "Lecteur d'écran, loupe, contraste",
                "Alt text, structure, couleurs",
            ],
        ),
        (
            "Auditive",
            [
                "Sous-titres, transcription, LSF",
                "Alertes visuelles, pas que sonores",
            ],
        ),
        (
            "Motrice",
            [
                "Clavier seul, contacteur, voix",
                "Cibles larges, pas de geste imposé",
            ],
        ),
        (
            "Cognitive",
            [
                "Langage clair, mise en page aérée",
                "Navigation prévisible, pas de surcharge",
            ],
        ),
    ]

    card_w = (CONTENT_W - GAP * 3) / 4
    card_h = max(estimate_card_height(t, c, card_w) for t, c in cards)
    top_cards = stack.push(card_h)
    for i, (titre, contenu) in enumerate(cards):
        add_card(
            slide, titre, contenu,
            top=top_cards,
            left=MARGIN_L + i * (card_w + GAP),
            width=card_w,
            height=card_h,
        )

    add_notes(
        slide,
        "Ne pas détailler chaque handicap - l'objectif est de montrer la diversité "
        "des besoins. Faire le lien avec les gestes concrets vus dans les modules "
        "suivants : alt text (visuelle), sous-titres (auditive), clavier (motrice), "
        "langage clair (cognitive).",
    )
    return slide
