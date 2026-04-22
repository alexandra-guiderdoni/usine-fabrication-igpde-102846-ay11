"""Slide 24 : Easy Check 12 - Piège du placeholder pris pour étiquette.

Règles neuropédagogie appliquées :
- R18 : sécurité psychologique - piège ultra-fréquent, on pardonne vite
- R19 : feedback par démo visuelle
"""

from igpde_dsfr_components import (
    Stack,
    add_alert,
    add_callout,
    add_notes,
    estimate_alert_height,
    estimate_callout_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Placeholder ≠ étiquette",
        fil_ariane="3. Easy Checks | 12. Étiquettes de formulaire",
        footer_text=f"{ctx.footer_base} / Easy Checks - Étiquettes",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_callout(
        slide,
        "Pourquoi le placeholder ne remplace jamais l’étiquette :",
        [
            "Il disparaît dès qu’on commence à saisir - on oublie ce qu’on remplit",
            "Son contraste est souvent trop faible pour passer le check 4",
            "Les lecteurs d’écran l’ignorent ou l’annoncent comme « texte exemple »",
            "Impossible d’y revenir : il est perdu dès la 1ʳᵉ lettre tapée",
        ],
        top=stack.push(estimate_callout_height('Pourquoi le placeholder ne remplace jamais l’étiquette :', ['Il disparaît dès qu’on commence à saisir - on oublie ce qu’on remplit', 'Son contraste est souvent trop faible pour passer le check 4', 'Les lecteurs d’écran l’ignorent ou l’annoncent comme « texte exemple »', 'Impossible d’y revenir : il est perdu dès la 1ʳᵉ lettre tapée'])),
    )

    add_alert(
        slide,
        titre="Pattern recommandé",
        bullets=[
            "Étiquette visible au-dessus du champ (ou à gauche)",
            "Placeholder optionnel, pour donner un exemple de format : « JJ/MM/AAAA »",
            "Ne JAMAIS mettre l’information essentielle uniquement dans le placeholder",
        ],
        top=stack.push(estimate_alert_height('Pattern recommandé', ['Étiquette visible au-dessus du champ (ou à gauche)', 'Placeholder optionnel, pour donner un exemple de format : « JJ/MM/AAAA »', 'Ne JAMAIS mettre l’information essentielle uniquement dans le placeholder'])),
        alert_type="success",
    )

    add_notes(
        slide,
        "Démo : formulaire courant (type CAF, impots.gouv) avec labels floating - "
        "zoomer à 200 % et montrer que l’étiquette disparaît derrière le texte saisi. "
        "Règle pragmatique : si on doit choisir entre joli et utilisable, on choisit utilisable. "
        "Les labels au-dessus du champ sont plus hauts mais clairs pour tous.",
    )
    return slide
