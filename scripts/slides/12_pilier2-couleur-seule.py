"""Slide 37 : La couleur ne suffit jamais.

Règles neuropedagogie appliquees :
- R13 : Chiffre-cle personnalise (8 % = 1 sur 12 = 16 sur 200)
- R10 : Tableau inaccessible vs accessible pour discrimination
- R6 : Simulation de la vision daltonienne pour empathie
"""

from igpde_dsfr_components import (
    add_pave_chiffre, add_tableau, add_highlight, add_image,
    add_notes, new_slide,
    estimate_highlight_height,
    MARGIN_L, CONTENT_W, Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="La couleur ne doit pas porter l'information à elle seule",
        fil_ariane="2. Documents accessibles | 2. Couleurs",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Couleurs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.25)

    # Rangee haute : KPI a gauche, image pastilles a droite
    row1_top = stack.push(1.5)

    add_pave_chiffre(
        slide,
        valeur="8 %",
        label="des hommes ne distinguent pas toutes les couleurs",
        top=row1_top,
        left=MARGIN_L,
        width=3.5,
        height=1.5
    )

    add_image(
        slide,
        "_assets/pastilles-daltonisme.png",
        top=row1_top - 0.15,
        left=4.5,
        width=5.5,
        alt_text=(
            "Trois pastilles rouge, orange, verte en vision normale "
            "puis en deutéranopie : les deux premières deviennent "
            "indiscernables sans légende textuelle."
        ),
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
        top=stack.push(1.2),
        col_widths=[6.14, 6.14]
    )

    accroche = "Doublez toujours la couleur avec une légende textuelle\net idéalement un motif visuel distinct."
    stack.gap = 0.45
    add_highlight(
        slide, accroche,
        top=stack.push(estimate_highlight_height(accroche, CONTENT_W))
    )

    add_notes(
        slide,
        "8 % des hommes = 1 personne dans une réunion de 12. Dans une direction de "
        "200 agents : 16 personnes concernées. Montrer l'image : en deutéranopie, "
        "En retard et En cours sont indiscernables. Demander aux stagiaires : "
        "« Dans vos documents, utilisez-vous des codes couleur sans texte ? »"
    )
    return slide
