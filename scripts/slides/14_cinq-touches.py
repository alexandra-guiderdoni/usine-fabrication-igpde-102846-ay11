"""Slide 4 : les 5 touches à maîtriser, consolidées en un tableau unique.

Règles neuropédagogie appliquées :
- R5 : chunking - 5 touches regroupées en 3 intentions (Naviguer / Agir / Lire)
- R6 : double codage - titre oral + visuel tableau
- R16 : visuel - un tableau comparable d'un coup d'œil
"""

from igpde_dsfr_components import (
    Stack, add_highlight, add_notes, add_tableau,
    estimate_highlight_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="5 touches, 3 intentions",
        fil_ariane="3. Easy Checks | 6. Focus et navigation clavier",
        footer_text=f"{ctx.footer_base} / Easy Checks - Clavier",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    # Gap genereux (0,55) car l'ombre portee du highlight et le header bleu
    # du tableau creent un effet de chevauchement visuel avec un gap serre.
    stack = Stack(top=2.3, gap=0.55)

    highlight_texte = "Naviguer → Tab / Shift+Tab    Agir → Entrée / Espace    Lire → Flèches ↑ ↓"
    add_highlight(
        slide, highlight_texte,
        top=stack.push(estimate_highlight_height(highlight_texte)),
    )

    headers = ["Touche", "À quoi elle sert", "Ce qu’il faut vérifier"]
    rows = [
        [
            "Tab",
            "Avancer sur l’élément interactif suivant (lien, bouton, champ).",
            "Le focus se déplace et reste visible à chaque étape.",
        ],
        [
            "Shift + Tab",
            "Reculer sur l’élément interactif précédent.",
            "L’ordre inverse est logique, sans saut imprévu.",
        ],
        [
            "Entrée",
            "Activer un lien ou soumettre un formulaire.",
            "L’action attendue se déclenche immédiatement.",
        ],
        [
            "Barre d’espace",
            "Cocher, décocher, sélectionner un bouton radio.",
            "L’état coché / non coché est annoncé vocalement.",
        ],
        [
            "Flèches ↑ ↓",
            "Lire le contenu ligne par ligne avec un lecteur d’écran.",
            "Le texte alternatif des images est lu à haute voix.",
        ],
    ]
    add_tableau(
        slide, headers, rows,
        top=stack.push(0),  # le tableau se positionne ; sa hauteur est geree par row_h * n_rows
        col_widths=[1.80, 4.90, 5.58],
        row_h=0.52,
    )

    add_notes(
        slide,
        "Faire deviner avant de révéler la 3e colonne (R11) : "
        "« Devinez ce qui doit se passer quand j’appuie sur Tab ». "
        "Insister sur l’indicateur de focus visible - c’est LE critère qui tombe en premier. "
        "Piège fréquent : un site qui n’annonce jamais l’état d’une case à cocher (ligne Espace).",
    )
    return slide
