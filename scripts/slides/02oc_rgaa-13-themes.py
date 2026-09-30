"""Slide 02rb : RGAA 13 thèmes et obligations (Martine 32+33)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, GAP, MARGIN_L,
    Stack,
    add_card, add_notes, add_tableau,
    estimate_card_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="RGAA : 13 thèmes, 3 niveaux de conformité",
        fil_ariane="1. Q3 - Cadre légal | 13 thèmes RGAA",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=1.90, gap=0.30)

    headers = ["Les 13 thèmes du RGAA", ""]
    rows = [
        ["1. Images", "8. Éléments obligatoires"],
        ["2. Cadres", "9. Structuration"],
        ["3. Couleurs", "10. Présentation"],
        ["4. Multimédia", "11. Formulaires"],
        ["5. Tableaux", "12. Navigation"],
        ["6. Liens", "13. Consultation"],
        ["7. Scripts", ""],
    ]
    tbl_top = stack.cursor
    tbl_h = add_tableau(
        slide, headers, rows,
        top=tbl_top,
        col_widths=[COL_W, COL_W],
        row_h=0.30,
    )
    stack.push(tbl_h)

    card_w = (CONTENT_W - GAP) / 2
    card_top = 5.10
    cards = [
        (
            "SPAN",
            "Schéma pluriannuel d'accessibilité sur 3 ans",
        ),
        (
            "Trois niveaux de conformité",
            [
                "Non conforme : moins de 50 % des critères",
                "Partiellement conforme : de 50 % à 99 %",
                "Totalement conforme : 100 % des critères applicables",
            ],
        ),
    ]
    for index, (titre, contenu) in enumerate(cards):
        card_h = estimate_card_height(titre, contenu, card_w, compact=True)
        add_card(
            slide,
            titre,
            contenu,
            top=card_top,
            left=MARGIN_L + index * (card_w + GAP),
            width=card_w,
            height=card_h + 0.17,
            body_line_spacing=1.2,
            compact=True,
        )

    add_notes(
        slide,
        "Ne pas détailler chaque thème : les participants les retrouveront "
        "dans les modules suivants. Insister sur le SPAN : c'est le document "
        "stratégique que chaque organisme public doit publier. Environ 25 % "
        "des tests RGAA sont automatisables, le reste nécessite un audit humain.",
    )
    return slide
