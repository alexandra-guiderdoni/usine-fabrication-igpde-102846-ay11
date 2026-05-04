"""Slide 33 : Les styles de titre : le fondement de tout.

Regles neuropedagogie appliquees :
- R5 : Perspective utilisateur (comment un lecteur d'ecran voit les titres)
- R10 : Avant/Apres contrastant pour memorisation
- R19 : Procedure d'action detaillee + verification
"""

from igpde_dsfr_components import (
    add_highlight, add_card, add_notes, new_slide,
    estimate_highlight_height,
    MARGIN_L, CONTENT_W, COL_R, COL_W, Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Les styles de titre : le fondement de tout",
        fil_ariane="2. Documents accessibles | 1. Structure",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Structure",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.1, gap=0.30)

    question = "Comment un lecteur d'écran repère-t-il les titres dans Word ?"
    add_highlight(
        slide, question,
        top=stack.push(estimate_highlight_height(question, CONTENT_W)),
    )

    stack.gap = 0.25
    cards_top = stack.push(1.95)
    add_card(
        slide,
        "Sans styles de titre",
        [
            "Un bloc plat, sans repère de navigation",
            "Le lecteur d'écran ne peut pas aller de titre en titre",
            "L'utilisateur doit écouter tout le document"
        ],
        top=cards_top,
        left=MARGIN_L,
        width=COL_W,
        height=1.95,
    )
    add_card(
        slide,
        "Avec Titre 1, Titre 2, Titre 3",
        [
            "Titre 1 : Rapport annuel",
            "Titre 2 : Budget / Titre 3 : Prévisions",
            "Navigation rapide, comme une table des matières"
        ],
        top=cards_top,
        left=COL_R,
        width=COL_W,
        height=1.95,
    )

    procedure = [
        "Appliquer : Accueil > Styles > Titre 1, Titre 2 ou Titre 3",
        "Vérifier : Ctrl+F > onglet Titres"
    ]
    add_card(
        slide,
        "Comment faire",
        procedure,
        top=5.12,
        left=MARGIN_L,
        width=CONTENT_W,
        height=1.50,
    )

    add_notes(
        slide,
        "Réponse à la question : le lecteur d'écran lit les balises HTML ou les styles "
        "Word - pas la mise en forme visuelle. Un titre en gras 16pt n'est pas un titre "
        "pour un lecteur d'écran. Faire la démonstration en direct si possible : ouvrir "
        "un document vierge, écrire un titre en gras, puis avec le style Titre 1. "
        "La différence est invisible visuellement mais fondamentale pour l'accessibilité."
    )
    return slide
