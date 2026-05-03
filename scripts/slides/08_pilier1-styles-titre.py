"""Slide 33 : Les styles de titre : le fondement de tout.

Regles neuropedagogie appliquees :
- R5 : Perspective utilisateur (comment un lecteur d'ecran voit les titres)
- R10 : Avant/Apres contrastant pour memorisation
- R19 : Procedure d'action detaillee + verification
"""

from igpde_dsfr_components import (
    add_highlight, add_avant_apres, add_callout, add_notes, new_slide,
    estimate_highlight_height, estimate_callout_height,
    MARGIN_L, CONTENT_W, Stack,
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

    stack.gap = 0.35
    add_avant_apres(
        slide,
        "Sans styles de titre",
        [
            "Texte, texte, texte, texte...",
            "Un bloc plat - aucun repère de navigation",
            "4 minutes d'écoute sans pouvoir avancer"
        ],
        "Avec Titre 1, Titre 2, Titre 3",
        [
            "Titre 1 : Rapport annuel",
            "Titre 2 : Budget / Titre 3 : Prévisions 2025",
            "Navigation en quelques secondes comme une table des matières interactive"
        ],
        top=stack.push(2.0),
        height=2.0
    )

    callout_bullets = [
        "Clic sur le titre > Accueil > Styles > Titre 1, Titre 2 ou Titre 3",
        "Raccourci volet Styles : Ctrl+Alt+Maj+S",
        "Vérification : Ctrl+F > onglet Titres - les titres apparaissent ? C'est bon."
    ]
    stack.gap = 0.30
    add_callout(
        slide,
        "Comment faire",
        callout_bullets,
        top=stack.push(estimate_callout_height("Comment faire", callout_bullets,
                                               CONTENT_W)),
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
