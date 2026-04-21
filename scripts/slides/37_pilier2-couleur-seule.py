"""Slide 37 : Pilier 2 - La couleur ne suffit jamais.

Règles neuropédagogie appliquées :
- R13 : Chiffre-clé personnalisé (8 % = 1 sur 12 = 16 sur 200)
- R10 : Tableau inaccessible vs accessible pour discrimination
- R6 : Simulation de la vision daltonienne pour empathie
"""

from igpde_dsfr_components import (
    add_pave_chiffre, add_tableau, add_highlight, add_notes, new_slide,
    MARGIN_L
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 2 - La couleur ne suffit jamais",
        fil_ariane="2. Documents accessibles | 2. Couleurs",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Couleurs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_pave_chiffre(
        slide,
        valeur="8 %",
        label="des hommes ne distinguent pas toutes les couleurs",
        top=2.3,
        left=MARGIN_L,
        width=3.5,
        height=1.5
    )

    add_tableau(
        slide,
        ["Inaccessible", "Accessible"],
        [
            [
                "Statut : rouge / vert / jaune (couleur seule)",
                "Statut : En retard / Terminé / En cours (texte + couleur)"
            ],
            [
                "Budget : zone verte = OK (couleur seule)",
                "Budget : OK (vert) / Attention (orange) / Dépassé (rouge)"
            ]
        ],
        top=4.0,
        col_widths=[6.14, 6.14]
    )

    add_highlight(
        slide,
        "Règle : le texte porte l'information, la couleur la renforce.",
        top=6.0
    )

    add_notes(
        slide,
        "8 % des hommes = 1 personne dans une réunion de 12. Dans une direction de "
        "200 agents : 16 personnes concernées. Démonstration : ouvrir un tableau de bord "
        "avec codes couleur uniquement. Simuler la vision daltonienne avec un outil en "
        "ligne ou le mode de simulation de Chrome DevTools."
    )
    return slide
