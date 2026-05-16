"""Slide 02p : règles transversales de communication accessible.

Règles neuropédagogie appliquées :
- R5 : chunking - 3 familles de réflexes
- R12 : récupération active - préparer les checks repris plus tard
- R24 : action concrète - règles applicables dès la prochaine publication
"""

from igpde_dsfr_components import (
    CONTENT_W,
    GAP,
    MARGIN_L,
    add_card,
    add_highlight,
    add_notes,
    estimate_card_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Règles transversales : texte, contraste, QR",
        fil_ariane="1. Q5 - Comment | Règles transversales",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    card_w = (CONTENT_W - GAP * 2) / 3
    cards = [
        (
            "Textes lisibles",
            [
                "Police simple, sans empattement",
                "Alignement à gauche",
                "Paragraphes courts et aérés",
                "Taille adaptée au support final",
            ],
            1,
        ),
        (
            "Contrastes testés",
            [
                "Ratio 4,5:1 minimum",
                "Idéal : viser 7:1",
                "Éviter les dégradés sous le texte",
                "Tester avec un outil, pas à l'œil",
            ],
            2,
        ),
        (
            "QR codes utiles",
            [
                "Jamais le seul accès",
                "Lien visible à côté",
                "Mention « Scannez-moi ! »",
                "Taille et contraste suffisants",
            ],
            3,
        ),
    ]
    card_h = max(estimate_card_height(t, c, card_w, numero=n) for t, c, n in cards)
    top_cards = 2.30
    for i, (titre, contenu, numero) in enumerate(cards):
        add_card(
            slide,
            titre,
            contenu,
            top=top_cards,
            left=MARGIN_L + i * (card_w + GAP),
            width=card_w,
            height=card_h,
            numero=numero,
        )

    message = "Un support accessible ne dépend jamais d'un seul canal."
    add_highlight(
        slide,
        message,
        top=top_cards + card_h + 0.35,
    )

    add_notes(
        slide,
        "Cette slide annonce les réflexes qui seront travaillés ensuite dans Word, le web et les réseaux sociaux. "
        "Ne pas entrer trop tôt dans les détails techniques : elle doit installer un filtre de lecture commun. "
        "Pour les QR codes, rappeler la règle demandée : toujours ajouter le lien visible à côté et la mention Scannez-moi !",
    )
    return slide
