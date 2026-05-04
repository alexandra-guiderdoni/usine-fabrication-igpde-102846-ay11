"""Slide 26 : Easy Check 13 - Champs obligatoires.

Règles neuropédagogie appliquées :
- R5 : chunking - 3 règles simples
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
        titre="Champs obligatoires : dits, pas juste marqués",
        fil_ariane="3. Easy Checks | 13. Champs obligatoires",
        footer_text=f"{ctx.footer_base} / Easy Checks - Champs obligatoires",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.12)

    hl_texte = "Un astérisque rouge est un signal visuel - il doit être doublé d'une information textuelle pour tous."
    add_highlight(
        slide,
        hl_texte,
        top=stack.push(estimate_highlight_height(hl_texte)),
    )

    callout_titre = "Ce qu'il faut vérifier :"
    callout_bullets = [
        "Les champs obligatoires sont indiqués en texte : « obligatoire » ou « requis »",
        "La légende « * champ obligatoire » est présente en début de formulaire",
        'Techniquement : attribut required ou aria-required="true" sur le champ',
        "En cas d'erreur : le message pointe le champ par son étiquette, pas « champ 3 »",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Pattern recommandé"
    alert_bullets = [
        "Quand presque tous les champs sont requis, marquer les champs optionnels peut rendre le formulaire plus lisible",
    ]
    add_alert(
        slide,
        titre=alert_titre,
        bullets=alert_bullets,
        top=stack.push(estimate_alert_height(alert_titre, alert_bullets)),
        alert_type="info",
    )

    add_notes(
        slide,
        "Règle d'or : couleur seule = information perdue pour les aveugles et les daltoniens. "
        "Exemple à tester : un champ obligatoire marqué uniquement par astérisque rouge - lecteur d'écran n'annonce rien. "
        "Message d'erreur à éviter : « Erreur champ 3 » → préférer « Votre adresse électronique est obligatoire ».",
    )
    return slide
