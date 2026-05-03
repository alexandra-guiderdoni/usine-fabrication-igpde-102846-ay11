"""Slide 32 : 5 piliers, vue d'ensemble.

Règles neuropédagogie appliquées :
- R2 : Schéma global du parcours pour créer un cadre mental
- R14 : Tableau structurant pour mémorisation
- R17 : Parcours avant listes - ordre chronologique, pas alphabétique
"""

from igpde_dsfr_components import add_highlight, add_tableau, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="5 piliers, 21 critères",
        fil_ariane="2. Documents accessibles",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Vue d'ensemble",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "Chaque pilier = des critères actionnables immédiatement dans le ruban Word.",
        top=2.3
    )

    add_tableau(
        slide,
        ["Pilier", "Ce que vous allez apprendre"],
        [
            ["1. Structure", "Titres, listes, colonnes, tableaux, sauts de page"],
            ["2. Couleurs", "Rapport de contraste, couleur porteuse de sens"],
            ["3. Contenu alternatif", "Texte alternatif, objets alignés, liens descriptifs"],
            ["4. Langue et lisibilité", "Balisage linguistique, majuscules, espaces répétés"],
            ["5. Finalisation", "Vérificateur d'accessibilité, propriétés du document, export PDF"]
        ],
        top=3.65,
        col_widths=[3.5, 8.78]
    )

    add_notes(
        slide,
        "Plan de la session. Pointer chaque pilier. Insister : ce n'est pas une liste "
        "de règles à mémoriser, c'est un parcours. On commence par le plus impactant "
        "et on finit par le plus simple à vérifier."
    )
    return slide
