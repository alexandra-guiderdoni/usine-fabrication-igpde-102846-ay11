"""Slide 3 : ouverture du module « Naviguer sans souris ».

Règles neuropédagogie appliquées :
- R1 : casser la passivité par une question provocante (notes orateur)
- R3 : WIIFM - 3 bénéfices concrets pour l'apprenant
- R8 : analogie du GPS pour ancrer l'idée
- R9 : émotion via situation d’usage concrète
"""

from igpde_dsfr_components import (
    Stack,
    add_callout,
    add_highlight,
    add_notes,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Naviguer sans souris : le test qui change tout",
        fil_ariane="3. Easy Checks | 6. Focus et navigation clavier",
        footer_text=f"{ctx.footer_base} / Easy Checks - Clavier",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_highlight(
        slide,
        "Quand on navigue au clavier, un focus invisible suffit à perdre toute la page.",
        top=stack.push(estimate_highlight_height('Quand on navigue au clavier, un focus invisible suffit à perdre toute la page.')),
    )

    add_callout(
        slide,
        "En 15 minutes, vous saurez :",
        [
            "Utiliser 5 touches pour tester n’importe quelle page",
            "Repérer 3 signaux qui trahissent un défaut d’accessibilité",
            "Reproduire l’expérience d’un lecteur d’écran en 3 minutes",
        ],
        top=stack.push(estimate_callout_height('En 15 minutes, vous saurez :', ['Utiliser 5 touches pour tester n’importe quelle page', 'Repérer 3 signaux qui trahissent un défaut d’accessibilité', 'Reproduire l’expérience d’un lecteur d’écran en 3 minutes'])),
    )

    add_notes(
        slide,
        "Annoncer le rattachement : cette séquence correspond à l’Easy Check n° 6 du W3C "
        "« Focus clavier visible » (WCAG 2.4.7), qu’on élargit ici à la navigation clavier complète "
        "(tabulation, activation, lecture). Corpus de référence local : 03-easy-checks/w3c-easy-checks-fr.md. "
        "Ouvrir par une question : « Posez la main loin de la souris. "
        "Combien de temps tenez-vous sur votre site préféré ? » "
        "Laisser 10 secondes de silence. "
        "Analogie : le clavier est le GPS de votre site - s’il ne s’allume pas, personne ne trouve la route. "
        "Objectif : transformer le regard des stagiaires. Après cette slide, ils ne regarderont plus une page comme avant.",
    )
    return slide
