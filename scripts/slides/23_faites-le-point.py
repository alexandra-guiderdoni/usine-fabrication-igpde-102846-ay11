"""Slide 48 : Faites le point - Métacognition et récupération active.

Règles neuropédagogie appliquées :
- R4 : Récupération active sans relecture
- R23 : Métacognition (évaluation de sa propre compréhension)
- R25 : Silence et travail individuel pour consolidation
"""

from igpde_dsfr_components import (
    Stack, MARGIN_L, CONTENT_W,
    add_highlight, add_texte_libre, add_alert, add_notes, new_slide,
    estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Faites le point",
        fil_ariane="2. Documents accessibles | Métacognition",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Métacognition",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.30)

    consigne = "Avant de regarder la réponse, notez sans relire :"
    add_highlight(slide, consigne,
                  top=stack.push(estimate_highlight_height(consigne, CONTENT_W)),
                  left=MARGIN_L, width=CONTENT_W)

    questions = [
        "1.  La règle la plus importante pour les lecteurs d'écran : _______________",
        "2.  La vérification à faire en 30 secondes sur n'importe quel document : _______________",
        "3.  Le geste que vous ferez dès demain sur votre prochain document : _______________",
    ]
    for q in questions:
        add_texte_libre(slide, q,
                        top=stack.push(0.55),
                        left=MARGIN_L, width=CONTENT_W,
                        height=0.50, size=14)

    add_alert(
        slide,
        "Si vous avez répondu...",
        [
            "Styles de titre - Ctrl+F onglet Titres - et vérifier le texte alternatif",
            "Vous avez retenu l'essentiel. Sinon : relire Structure et Contenus.",
        ],
        top=stack.cursor,
        left=MARGIN_L, width=CONTENT_W,
        alert_type="success",
    )

    add_notes(
        slide,
        "Silence total pendant 2 minutes. Ne pas aider. Ce travail de récupération active "
        "consolide la mémoire à long terme plus efficacement que relire le support. "
        "Quand tout le monde a écrit : comparer avec la réponse. L'écart entre ce qu'on "
        "croit savoir et ce qu'on sait vraiment est très instructif.",
    )
    return slide
