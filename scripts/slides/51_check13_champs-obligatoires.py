"""Slide 75 : Point de contrôle rapide 13 - Champs obligatoires et erreurs.

Règles neuropédagogie appliquées :
- R5 : chunking - deux temps de test
- R11 : prédiction - l'apprenant compare avant/après soumission
- R18 : sécurité psychologique - les erreurs doivent guider, pas punir
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
        titre="Champs obligatoires : prévenir puis guider",
        fil_ariane="3. points de contrôle rapides | 13. Champs obligatoires et erreurs",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Champs obligatoires et erreurs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=1.95, gap=0.08)

    hl_texte = "Test #13 = avant envoi + après soumission vide : l'obligation prévient, l'erreur guide."
    add_highlight(
        slide,
        hl_texte,
        top=stack.push(estimate_highlight_height(hl_texte)),
    )

    callout_titre = "Avant soumission"
    callout_bullets = [
        "Obligation écrite : « obligatoire » ou règle « tous sauf téléphone »",
        "Astérisque expliqué s'il est utilisé",
        'Attribut required ou aria-required="true" présent',
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Après soumission"
    alert_bullets = [
        "Aucune erreur ne doit apparaître avant l'envoi",
        "Message précis relié au champ, avec aria-invalid si erreur",
        "Focus vers le récapitulatif ou le premier champ en erreur",
    ]
    add_alert(
        slide,
        titre=alert_titre,
        bullets=alert_bullets,
        top=stack.push(estimate_alert_height(alert_titre, alert_bullets, line_spacing=1.25)),
        alert_type="info",
        line_spacing=1.25,
    )

    add_notes(
        slide,
        "Règle d'or : le contrôle 13 ne commence pas par les erreurs. "
        "D'abord, vérifier que l'obligation est comprise avant l'envoi. "
        "Ensuite, soumettre volontairement un formulaire vide : le message doit nommer le champ, être relié au champ et guider le focus. "
        "Message à éviter : « Erreur champ 3 ». Préférer : « L'adresse électronique doit respecter le format nom@domaine.fr ».",
    )
    return slide
