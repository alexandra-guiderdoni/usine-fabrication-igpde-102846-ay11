"""Slide 02nde : fiches solutions - déficiences motrices et cognitives."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    Stack,
    add_highlight, add_notes, add_tableau,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Solutions par type de déficience (2/2)",
        fil_ariane="1. Q2 - Pour qui | Fiches solutions",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=1.85, gap=0.13)

    message = (
        "Les déficiences motrices et cognitives impliquent des réponses "
        "différentes, mais un principe commun : simplifier l'interaction."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    headers_m = ["", "Handicap moteur", "Dyslexie / troubles dys"]
    rows_m = [
        [
            "Difficultés",
            "Manipulation, préhension, pointage",
            "Lecture, repérage, décodage",
        ],
        [
            "Solutions",
            "Navigation clavier, zones cliquables larges",
            "Polices simples, texte non justifié, mise en page aérée",
        ],
        [
            "Technologies",
            "Trackball, clavier virtuel, commande oculaire",
            "Synthèse vocale, règle de lecture",
        ],
    ]
    tbl_h = add_tableau(
        slide, headers_m, rows_m,
        top=stack.push(len(rows_m) * 0.48 + 0.40),
        col_widths=[2.2, 4.9, 4.9],
    )

    headers_c = ["", "Handicap mental", "TSA"]
    rows_c = [
        [
            "Difficultés",
            "Compréhension, défilement, animation",
            "Structuration, repérage",
        ],
        [
            "Solutions",
            "Interfaces simples, FALC, pictogrammes",
            "Consignes claires, structure documentaire",
        ],
        [
            "Technologies",
            "Pas de technologie d'assistance spécifique",
            "Pas de technologie d'assistance spécifique",
        ],
    ]
    add_tableau(
        slide, headers_c, rows_c,
        top=stack.push(len(rows_c) * 0.48 + 0.40),
        col_widths=[2.2, 4.9, 4.9],
    )

    add_notes(
        slide,
        "Faire le lien avec Agathe (motrice), Paul (dyslexie/TDAH) et "
        "Anatole (cognitif). Pour le handicap mental et le TSA, insister "
        "sur le fait qu'il n'existe pas de technologie d'assistance "
        "spécifique : c'est le contenu et l'interface qui doivent s'adapter. "
        "Le FALC et le langage clair sont les réponses principales.",
    )
    return slide
