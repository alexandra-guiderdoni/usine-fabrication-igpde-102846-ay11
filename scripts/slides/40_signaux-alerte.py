"""Slide 5 : les 3 signaux qui trahissent un défaut d'accessibilité.

Règles neuropédagogie appliquées :
- R5 : chunking - 3 signaux exactement, pas plus
- R11 : faire deviner le signal le plus bloquant
- R18 : sécurité psychologique - l'erreur est normale, on l'apprend à la détecter
"""

from igpde_dsfr_components import (
    add_card, add_notes, estimate_card_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="3 signaux qui trahissent un défaut",
        fil_ariane="3. points de contrôle rapides | 6. Focus et navigation clavier",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Focus et navigation clavier",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    # Grille : 3 cartes côte à côte, marge 0,52", gouttière 0,33"
    MARGIN = 0.52
    GAP = 0.33
    CARD_W = 3.87
    TOP = 2.55

    cards = [
        (
            "Le focus disparaît",
            "Plus de contour visible pendant la tabulation. "
            "L’utilisateur est perdu dès la 3ᵉ touche Tab.",
            1,
        ),
        (
            "L’ordre est illogique",
            "Le focus saute à droite avant le menu à gauche. "
            "Le lecteur d’écran parcourt la page dans le désordre.",
            2,
        ),
        (
            "L’état n’est pas annoncé",
            "Une case qui coche sans dire « coché ». "
            "L’information est invisible pour qui ne voit pas l’écran.",
            3,
        ),
    ]
    HEIGHT = max(estimate_card_height(t, c, CARD_W, n) for t, c, n in cards)

    for i, (titre_c, contenu, numero) in enumerate(cards):
        add_card(
            slide,
            titre=titre_c,
            contenu=contenu,
            top=TOP, left=MARGIN + i * (CARD_W + GAP),
            width=CARD_W, height=HEIGHT,
            numero=numero,
        )

    add_notes(
        slide,
        "Avant de révéler les 3 cartes, demander : « Quel est le signal qui vous semble le plus grave ? » "
        "Laisser parler 2 stagiaires. "
        "Rappel rassurant (R18) : détecter un de ces signaux ne sert pas à désigner un coupable, "
        "mais à prouver qu’un test clavier doit entrer dans la routine de publication.",
    )
    return slide
