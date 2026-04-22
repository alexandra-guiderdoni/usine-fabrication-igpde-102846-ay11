"""Slide rs_14 : quiz de clôture - vrai/faux interleaving 4 questions."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, GAP,
    add_card, add_highlight, add_notes, new_slide,
    estimate_card_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Quiz : vrai ou faux ?",
        fil_ariane="4. Réseaux sociaux | Quiz de clôture",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30
    card_w = (CONTENT_W - GAP) / 2

    questions = [
        ("1 ou 2 émojis par post, en fin de message",
         ["VRAI - au-delà de 2, l'écoute devient incompréhensible"],
         1, MARGIN_L),
        ("#publicservice est aussi accessible que #PublicService",
         ["FAUX - sans CamelCase le lecteur lit un seul mot"],
         2, MARGIN_L + card_w + GAP),
        ("Un alt text vide est toujours une erreur",
         ["FAUX - une image décorative peut avoir un alt vide (ou 'Image décorative')"],
         3, MARGIN_L),
        ("Le faux gras InstaFont est lu comme du gras par NVDA",
         ["FAUX - les caractères Unicode sont lus lettre par lettre ou ignorés"],
         4, MARGIN_L + card_w + GAP),
    ]

    card_h = max(estimate_card_height(t, c, card_w, numero=n) for t, c, n, _ in questions)
    row1_top = top
    row2_top = round(row1_top + card_h + 0.25, 2)
    tops = [row1_top, row1_top, row2_top, row2_top]

    for (titre, contenu, numero, left), card_top in zip(questions, tops):
        add_card(slide, titre, contenu,
                 top=card_top, left=left, width=card_w, height=card_h, numero=numero)

    message = "4 réflexes = 4 questions. Vous avez toutes les réponses depuis le début du module."
    hl_h = estimate_highlight_height(message, CONTENT_W)
    add_highlight(slide, message,
                  top=round(row2_top + card_h + 0.25, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "Quiz à main levée - poser chaque question, laisser les réponses s'exprimer "
        "avant de révéler. Ne pas lire les réponses inscrites sur les cartes "
        "pendant la question. "
        "Interleaving (R14 neuropédagogie) : les 4 questions couvrent les 4 réflexes "
        "du module, pas uniquement le dernier thème. "
        "Si des stagiaires se trompent sur Q3 (alt vide) : "
        "c'est normal, c'est le point le plus contre-intuitif. "
        "Prendre 1 minute pour expliquer la distinction image décorative vs informative.",
    )
    return slide
