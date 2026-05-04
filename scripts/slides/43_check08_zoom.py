"""Slide 18 : Point de contrôle rapide 8 - Zoom et redimensionnement du texte.

Règles neuropédagogie appliquées :
- R8 : analogie - zoomer à 200 % = lire avec des lunettes
- R3 : WIIFM - le zoom révèle les interfaces fragiles
"""

from igpde_dsfr_components import (
    Stack,
    add_alert,
    add_callout,
    add_highlight,
    add_notes,
    estimate_alert_height,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Zoom 200 % : tout doit rester lisible",
        fil_ariane="3. points de contrôle rapides | 8. Zoom",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Zoom",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.10, gap=0.18)

    add_highlight(
        slide,
        "À 200 %, votre site doit rester le même service : lisible, navigable et utilisable.",
        top=stack.push(estimate_highlight_height('À 200 %, votre site doit rester le même service : lisible, navigable et utilisable.')),
    )

    add_callout(
        slide,
        "Ce qu’il faut vérifier :",
        [
            "À 200 % de zoom, aucun texte n’est coupé ni superposé",
            "Pas d’apparition d’un défilement horizontal sur une page classique",
            "Les menus, boutons et formulaires restent utilisables, pas seulement visibles",
        ],
        top=stack.push(estimate_callout_height('Ce qu’il faut vérifier :', ['À 200 % de zoom, aucun texte n’est coupé ni superposé', 'Pas d’apparition d’un défilement horizontal sur une page classique', 'Les menus, boutons et formulaires restent utilisables, pas seulement visibles'])),
    )

    add_alert(
        slide,
        titre="Comment tester",
        bullets=[
            "Ctrl + (ou Cmd + sur Mac) pour zoomer jusqu’à 200 % - répéter 4 fois depuis 100 %",
            "Parcourir la page : formulaire, menu, pied de page. Si ça casse, le check échoue",
        ],
        top=stack.push(estimate_alert_height('Comment tester', ['Ctrl + (ou Cmd + sur Mac) pour zoomer jusqu’à 200 % - répéter 4 fois depuis 100 %', 'Parcourir la page : formulaire, menu, pied de page. Si ça casse, le check échoue'])),
        alert_type="info",
    )

    add_notes(
        slide,
        "Analogie : zoomer, c’est mettre des lunettes. Votre site doit rester opérationnel avec les lunettes. "
        "Test immédiat : demander à 2 stagiaires de zoomer à 200 % sur leur intranet et de tenter de remplir "
        "un formulaire. Souvent, un champ ou un bouton devient inaccessible. "
        "Ne pas confondre zoom navigateur (OK) et zoom tactile (mobile) - les deux doivent fonctionner.",
    )
    return slide
