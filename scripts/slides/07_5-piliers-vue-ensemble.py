"""Slide 32 : 5 themes, vue d'ensemble.

Regles neuropedagogie appliquees :
- R2 : Schema global du parcours pour creer un cadre mental
- R14 : Tableau structurant pour memorisation
- R17 : Parcours avant listes - ordre chronologique, pas alphabetique
"""

from igpde_dsfr_components import add_highlight, add_tableau, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="5 thèmes, 21 critères",
        fil_ariane="2. Documents accessibles",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Vue d'ensemble",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "Chaque thème = des critères actionnables immédiatement dans le ruban Word.",
        top=2.3
    )

    add_tableau(
        slide,
        ["Thème", "Ce que vous allez apprendre"],
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
        "Plan de la session. Pointer chaque thème. Insister : ce n'est pas une liste "
        "de règles à mémoriser, c'est un parcours. On commence par le plus impactant "
        "et on finit par le plus simple à vérifier."
    )
    return slide
