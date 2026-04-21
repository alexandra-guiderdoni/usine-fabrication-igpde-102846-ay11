"""Slide 46 : Par où commencer ?

Règles neuropédagogie appliquées :
- R2 : Matrice Importance/Effort pour priorisation
- R9 : Déconstruction (commencer par le haut-gauche = impact fort/effort faible)
- R12 : Ordre d'action clair (4 étapes, pas 50)
"""

from igpde_dsfr_components import (
    add_tableau, add_callout, add_notes, new_slide,
    estimate_callout_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Par où commencer ?",
        fil_ariane="2. Documents accessibles | Priorités",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Priorités",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_tableau(
        slide,
        ["", "Effort faible", "Effort élevé"],
        [
            [
                "Impact fort",
                "Styles de titre + Texte alt + Nom de fichier + Vérificateur",
                "Retravailler un document existant entier"
            ],
            [
                "Impact faible",
                "Propriétés (Titre, Auteur)",
                "Corriger le contraste sur des centaines de pages"
            ]
        ],
        top=2.3,
        col_widths=[1.8, 5.5, 4.98]
    )

    callout_bullets = [
        "1. Styles de titre sur tous les titres",
        "2. Texte alt sur chaque image",
        "3. Lancer le vérificateur d'accessibilité",
        "4. Vérifier les propriétés du document"
    ]
    add_callout(
        slide,
        "Commencez par le quadrant haut-gauche : impact fort, effort faible",
        callout_bullets,
        top=5.2
    )

    add_notes(
        slide,
        "Le quadrant haut-gauche est le meilleur investissement. 4 actions qui couvrent "
        "les piliers 1, 3 et 5 - les plus impactants. Retravailler un document entier est "
        "décourageant : commencer par les nouveaux documents. Le contraste sur des centaines "
        "de pages = piège : traiter à la source (templates, charte graphique)."
    )
    return slide
