"""Slide 33 : Pilier 1 - Les styles de titre : le fondement de tout.

Règles neuropédagogie appliquées :
- R5 : Perspective utilisateur (comment un lecteur d'écran voit les titres)
- R10 : Avant/Après contrastant pour mémorisation
- R19 : Procédure d'action détaillée + vérification
"""

from igpde_dsfr_components import (
    add_highlight, add_avant_apres, add_callout, add_notes, new_slide,
    estimate_callout_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 1 - Les styles de titre : le fondement de tout",
        fil_ariane="2. Documents accessibles | 1. Structure",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Structure",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "Devinez : comment un lecteur d'écran repère-t-il les titres dans Word ?",
        top=2.3
    )

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
        top=3.5,
        height=2.5
    )

    callout_bullets = [
        "Clic sur le titre > Accueil > Styles > Titre 1, Titre 2 ou Titre 3",
        "Raccourci volet Styles : Ctrl+Alt+Maj+S",
        "Vérification : Ctrl+F > onglet Titres - les titres apparaissent ? C'est bon."
    ]
    add_callout(
        slide,
        "Comment faire",
        callout_bullets,
        top=6.15
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
