"""Slide 38 : Texte alternatif sur les images.

Règles neuropédagogie appliquées :
- R7 : Procédure détaillée en stepper (4 étapes = décomposition)
- R20 : Distinction fonction vs apparence pour éviter le piège
- R14 : Tableau montrant bon/mauvais texte alt
"""

from igpde_dsfr_components import add_stepper, add_tableau, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Texte alternatif sur les images",
        fil_ariane="2. Documents accessibles | 3. Contenus",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Contenus",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_stepper(
        slide,
        [
            "Clic droit sur l'image > Format de l'image > Texte de remplacement",
            "Image significative : décrire la fonction, pas l'apparence",
            "Image décorative : cocher Marquer comme décoratif"
        ],
        top=2.3,
        height=2.0
    )

    add_tableau(
        slide,
        ["Mauvais texte alt", "Bon texte alt"],
        [
            [
                "Photo d'un graphique en barres colorées",
                "Chiffre d'affaires 2020-2024 : hausse de 15 à 23 %"
            ],
            [
                "Icône d'enveloppe ou E-mail",
                'alt="" (vide - icône redondante)'
            ],
            [
                "image.png",
                "Organigramme du service : 4 équipes, 28 agents"
            ]
        ],
        top=4.5,
        col_widths=[5.5, 6.78]
    )

    add_notes(
        slide,
        "Décrire la FONCTION, pas l'apparence. Un logo sans texte = décoratif "
        "(le lecteur annonce déjà le nom de la société dans les propriétés). "
        "Un graphique = décrire les données clés, pas les couleurs des barres. "
        "Objet décoratif = filets, séparateurs, icones visuelles. Les marquer évite "
        "que le lecteur annonce image, image, séparateur en permanence."
    )
    return slide
