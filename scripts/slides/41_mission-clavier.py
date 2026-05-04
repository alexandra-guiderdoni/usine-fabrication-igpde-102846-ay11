"""Slide 6 : votre mission - passage à l'action sur site d'entraînement.

Règles neuropédagogie appliquées :
- R24 : plan d'action concret (« Quelle est la 1re chose que vous ferez ? »)
- R9 : émotion positive via la gamification (« permis clavier »)
- R19 : feedback immédiat - le site d'entraînement répondra en direct
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
        titre="Votre mission",
        fil_ariane="3. points de contrôle rapides | 6. Focus et navigation clavier",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Clavier",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_callout(
        slide,
        "Sur le site d’entraînement qui vous sera fourni :",
        [
            "Cachez votre souris derrière l’écran",
            "Tabulez 10 fois et notez chaque fois que le focus disparaît",
            "Essayez Entrée sur un bouton, Espace sur une case à cocher",
            "Listez les pièges détectés et associez-les aux 3 signaux",
        ],
        top=stack.push(estimate_callout_height('Sur le site d’entraînement qui vous sera fourni :', ['Cachez votre souris derrière l’écran', 'Tabulez 10 fois et notez chaque fois que le focus disparaît', 'Essayez Entrée sur un bouton, Espace sur une case à cocher', 'Listez les pièges détectés et associez-les aux 3 signaux'])),
    )

    add_alert(
        slide,
        titre="Objectif : votre permis clavier",
        bullets=[
            "1 signal détecté = vous avez l’œil",
            "3 signaux détectés = vous êtes auditeur clavier",
        ],
        top=stack.push(estimate_alert_height('Objectif : votre permis clavier', ['1 signal détecté = vous avez l’œil', '3 signaux détectés = vous êtes auditeur clavier'])),
        alert_type="success",
    )

    add_notes(
        slide,
        "Distribuer l’URL du site d’entraînement (fabriqué en interne, avec pièges volontaires). "
        "Chronométrer 5 minutes. "
        "Débriefer en collectif : quel signal a été le plus difficile à repérer ? pourquoi ? "
        "Clore le module avec la question métacognitive (R25) : "
        "« Qu’est-ce qui vous aurait aidé à repérer plus vite ? » "
        "Engagement : chaque stagiaire annonce ce qu’il testera dès demain sur son propre site.",
    )
    return slide
