"""Slide 02o : handicap, contexte et validisme.

Règles neuropédagogie appliquées :
- R3 : WIIFM - donner l'échelle du sujet
- R16 : visuel - 3 chiffres clés plutôt qu'un bloc explicatif
- R15 : jargon traduit - validisme expliqué par les effets concrets
"""

from igpde_dsfr_components import (
    CONTENT_W,
    GAP,
    MARGIN_L,
    Stack,
    add_callout,
    add_highlight,
    add_notes,
    add_pave_chiffre,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Handicap : sortir de l'angle mort",
        fil_ariane="1. Introduction | Communication accessible",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "L'accessibilité n'est pas une faveur : c'est une condition d'accès "
        "équitable à l'information."
    )
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    item_w = (CONTENT_W - GAP * 2) / 3
    kpi_top = stack.push(1.5)
    kpis = [
        ("1 sur 5", "personne en situation\nde handicap ou trouble invalidant."),
        ("85 %", "des handicaps sont acquis\nau cours de la vie."),
        ("1er", "facteur de discrimination\nselon le Défenseur des droits."),
    ]
    for i, (valeur, label) in enumerate(kpis):
        left = MARGIN_L + i * (item_w + GAP)
        add_pave_chiffre(
            slide,
            valeur=valeur,
            label=label,
            top=kpi_top,
            left=left,
            width=item_w,
            height=1.5,
        )

    titre = "Validisme : le piège à déconstruire"
    bullets = [
        "Penser le public comme valide par défaut",
        "Confondre bonne intention et accès réel",
        "Oublier les handicaps invisibles, acquis ou temporaires",
    ]
    add_callout(
        slide,
        titre,
        bullets,
        top=stack.push(estimate_callout_height(titre, bullets, CONTENT_W, line_spacing=1.2)),
        line_spacing=1.2,
    )

    add_notes(
        slide,
        "Les chiffres viennent du guide Accessibiliser sa communication. "
        "Ne pas transformer cette slide en cours théorique sur le validisme. "
        "Objectif : faire comprendre que l'accessibilité de la communication répond à des situations nombreuses, "
        "souvent invisibles, et qu'une bonne intention ne garantit pas l'accès effectif.",
    )
    return slide
