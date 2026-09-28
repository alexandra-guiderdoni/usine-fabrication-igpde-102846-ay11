"""Slide 02ndd : fiches solutions - déficiences visuelles et auditives."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_callout, add_highlight, add_notes, add_tableau,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Solutions par type de déficience (1/2)",
        fil_ariane="1. Q2 - Pour qui | Fiches solutions",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=1.85, gap=0.13)

    message = (
        "Chaque déficience appelle des solutions et des technologies "
        "d'assistance spécifiques."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    headers_v = ["", "Aveugle", "Malvoyant"]
    rows_v = [
        [
            "Difficultés",
            "Inaccessibilité au visuel",
            "Inaccessibilité partielle",
        ],
        [
            "Solutions",
            "Remplacer par audio et tactile",
            "Grossissement, contrastes, luminosité",
        ],
        [
            "Technologies",
            "Plage braille, synthèse vocale",
            "Loupe logicielle, synthèse vocale",
        ],
    ]
    tbl_h = add_tableau(
        slide, headers_v, rows_v,
        top=stack.push(len(rows_v) * 0.48 + 0.40),
        col_widths=[2.2, 4.9, 4.9],
    )

    headers_a = ["", "Sourd", "Malentendant"]
    rows_a = [
        [
            "Difficultés",
            "Inaccessibilité à l'audio",
            "Inaccessibilité partielle à l'audio",
        ],
        [
            "Solutions",
            "Remplacer par le visuel (sous-titres, LSF)",
            "Renforcement du signal auditif, visuel",
        ],
        [
            "Technologies",
            "Sous-titrage, velotypie, LSF",
            "Appareil auditif, boucle magnétique",
        ],
    ]
    add_tableau(
        slide, headers_a, rows_a,
        top=stack.push(len(rows_a) * 0.48 + 0.40),
        col_widths=[2.2, 4.9, 4.9],
    )

    add_notes(
        slide,
        "Faire le lien avec les personas vus juste avant : Amir = aveugle, "
        "Anais = malvoyante, Justine = sourde. Ce tableau récapitule les "
        "solutions de manière structurée. La plage braille et la loupe "
        "logicielle sont des technologies d'assistance qu'on peut montrer "
        "en photo ou en vidéo courte si le temps le permet.",
    )
    return slide
