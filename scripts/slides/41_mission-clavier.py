"""Slide 6 : votre mission - passage à l'action sur site d'entraînement.

Règles neuropédagogie appliquées :
- R24 : plan d'action concret (« Quelle est la 1re chose que vous ferez ? »)
- R9 : émotion positive via la gamification (« permis clavier »)
- R19 : feedback immédiat - le site d'entraînement répondra en direct
"""

from config import load_formation_config
from igpde_dsfr_components import (
    COL_R,
    COL_W,
    MARGIN_L,
    Stack,
    add_alert,
    add_callout,
    add_notes,
    add_qrcode,
    estimate_alert_height,
    estimate_callout_height,
    new_slide,
)


SITE_ENTRAINEMENT = load_formation_config()["site_url"]


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Votre mission",
        fil_ariane="3. points de contrôle rapides | 6. Focus et navigation clavier",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Focus et navigation clavier",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    callout_titre = "Site d’entraînement :"
    callout_bullets = [
        "Cachez votre souris derrière l’écran",
        "Tabulez 10 fois et notez chaque fois que le focus disparaît",
        "Essayez Entrée sur un bouton, Espace sur une case à cocher",
        "Listez les pièges détectés et associez-les aux 3 signaux",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Objectif : votre permis clavier"
    alert_bullets = [
        "1 signal détecté = vous avez l’œil",
        "3 signaux détectés = vous êtes auditeur clavier",
    ]
    alert_top = stack.push(
        estimate_alert_height(alert_titre, alert_bullets, width=COL_W)
    )
    add_alert(
        slide,
        titre=alert_titre,
        bullets=alert_bullets,
        top=alert_top,
        left=MARGIN_L,
        width=COL_W,
        alert_type="success",
    )
    add_qrcode(
        slide,
        "scripts/images/qrcode-site-entrainement.png",
        url=SITE_ENTRAINEMENT,
        top=alert_top,
        left=COL_R,
        size=1.10,
        label_width=COL_W - 1.24,
        url_size=10,
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
