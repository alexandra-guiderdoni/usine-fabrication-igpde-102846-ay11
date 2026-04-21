"""Slide 48 : Faites le point - Métacognition et retrait active.

Règles neuropédagogie appliquées :
- R4 : Récupération active sans relecture
- R23 : Métacognition (évaluation de sa propre compréhension)
- R25 : Silence et travail individuel pour consolidation
"""

from igpde_dsfr_components import (
    add_highlight, add_alert, add_notes, new_slide
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

    add_highlight(
        slide,
        "Avant de regarder la réponse, notez sans relire :",
        top=2.3
    )

    # Create three text areas for free-text responses
    # Note: igpde_dsfr_components doesn't have add_texte_libre, so we'll use simple text representations
    slide.shapes.add_textbox(0.52, 3.15, 12.28, 0.8).text_frame.text = \
        "1.  La règle la plus importante pour les lecteurs d'écran : _______________"
    slide.shapes.add_textbox(0.52, 4.1, 12.28, 0.8).text_frame.text = \
        "2.  La vérification à faire en 30 secondes sur n'importe quel document : _______________"
    slide.shapes.add_textbox(0.52, 5.05, 12.28, 0.8).text_frame.text = \
        "3.  Le geste que vous ferez dès demain sur votre prochain document : _______________"

    alert_bullets = [
        "Styles de titre - Ctrl+F onglet Titres - et vérifier le texte alternatif",
        "Vous avez retenu l'essentiel. Sinon : relire les piliers 1 et 3."
    ]
    add_alert(
        slide,
        "Si vous avez répondu...",
        alert_bullets,
        top=6.0,
        alert_type="success"
    )

    add_notes(
        slide,
        "Silence total pendant 2 minutes. Ne pas aider. Ce travail de récupération active "
        "consolide la mémoire à long terme plus efficacement que relire le support. "
        "Quand tout le monde a écrit : comparer avec la réponse. L'écart entre ce qu'on "
        "croit savoir et ce qu'on sait vraiment est très instructif."
    )
    return slide
