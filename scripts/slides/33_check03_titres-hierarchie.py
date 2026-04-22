"""Slide 8 : Easy Check 3 - Titres de rubriques, la hiérarchie.

Règles neuropédagogie appliquées :
- R8 : analogie - la hiérarchie des titres est le sommaire automatique du document
- R16 : visuel - stepper qui matérialise les niveaux
- R5 : chunking - 3 règles clés
"""

from igpde_dsfr_components import (
    Stack, add_callout, add_highlight, add_notes,
    estimate_callout_height, estimate_highlight_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Titres : la hiérarchie qui structure",
        fil_ariane="3. Easy Checks | 3. Titres de rubriques",
        footer_text=f"{ctx.footer_base} / Easy Checks - Titres",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    highlight_texte = (
        "Un utilisateur de lecteur d’écran navigue de titre en titre "
        "comme on navigue dans une table des matières."
    )
    add_highlight(
        slide, highlight_texte,
        top=stack.push(estimate_highlight_height(highlight_texte)),
    )

    callout_titre = "3 règles qui font passer le check :"
    callout_bullets = [
        "Un seul H1 par page, qui reprend le sujet principal",
        "Les niveaux s’emboîtent sans saut : H1 → H2 → H3, jamais H2 → H4",
        "Un titre n’est pas une simple mise en forme gras/gros - c’est une balise <h1> à <h6>",
    ]
    add_callout(
        slide, callout_titre, callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    add_notes(
        slide,
        "Analogie : un document Word où tout le texte est en gras 18 pt n’a pas de plan. "
        "Même principe sur le web. "
        "Prédire : « Quel est le saut de hiérarchie le plus fréquent ? » (H2 → H4, parce que H3 « n’est pas assez joli »). "
        "Outil : l’extension HeadingsMap pour Chrome / Firefox affiche l’arbre des titres en un clic.",
    )
    return slide
