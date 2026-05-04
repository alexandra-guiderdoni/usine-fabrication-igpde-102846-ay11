"""Slide 23 : Point de contrôle rapide 12 - Étiquettes de formulaire, le principe.

Règles neuropédagogie appliquées :
- R8 : analogie - l'étiquette est le nom sur une boîte aux lettres
- R3 : WIIFM - un formulaire sans label est un formulaire inutilisable au lecteur d'écran
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
        titre="Étiquettes : chaque champ a un nom",
        fil_ariane="3. points de contrôle rapides | 12. Étiquettes de formulaire",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Étiquettes",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_highlight(
        slide,
        "Sans étiquette, un champ est comme une boîte aux lettres sans nom - on ne sait pas ce qu’on glisse dedans.",
        top=stack.push(estimate_highlight_height('Sans étiquette, un champ est comme une boîte aux lettres sans nom - on ne sait pas ce qu’on glisse dedans.')),
    )

    add_callout(
        slide,
        "Ce qu’il faut vérifier :",
        [
            "Chaque champ (texte, case, menu déroulant) a une étiquette visible à côté",
            "L’étiquette reste affichée quand on commence à saisir - elle ne disparaît pas",
            "Cliquer sur l’étiquette déplace le focus dans le champ (test rapide et décisif)",
            "Le lecteur d’écran annonce l’étiquette ET le type de champ",
        ],
        top=stack.push(estimate_callout_height('Ce qu’il faut vérifier :', ['Chaque champ (texte, case, menu déroulant) a une étiquette visible à côté', 'L’étiquette reste affichée quand on commence à saisir - elle ne disparaît pas', 'Cliquer sur l’étiquette déplace le focus dans le champ (test rapide et décisif)', 'Le lecteur d’écran annonce l’étiquette ET le type de champ'])),
    )

    add_notes(
        slide,
        "Analogie : une rue d’immeubles où les boîtes aux lettres n’ont aucun nom - impossible de distribuer. "
        "Test décisif : cliquer sur le TEXTE de l’étiquette. Si le curseur saute dans le champ, c’est bien balisé. "
        "Sinon, l’association est cassée - même si visuellement ça semble OK.",
    )
    return slide
