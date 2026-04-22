"""Slide 21 : Easy Check 10 - Transcriptions audio/vidéo.

Règles neuropédagogie appliquées :
- R8 : analogie - la transcription est le podcast en version imprimable
- R3 : WIIFM - référencement SEO bonus
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
        titre="Transcription : la version texte qui accompagne",
        fil_ariane="3. Easy Checks | 10. Transcriptions",
        footer_text=f"{ctx.footer_base} / Easy Checks - Transcriptions",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.25)

    hl_texte = "La transcription est au podcast ce que le script est au film : la version lisible, indexable, citable."
    add_highlight(
        slide,
        hl_texte,
        top=stack.push(estimate_highlight_height(hl_texte)),
    )

    callout_titre = "Ce qu'il faut vérifier :"
    callout_bullets = [
        "Toute vidéo / audio propose un lien visible « Lire la transcription »",
        "La transcription est complète : paroles + informations sonores essentielles",
        "Elle est sur la même page ou à un clic, jamais cachée à deux étages de menu",
        "Pour une vidéo : la transcription DESCRIPTIVE inclut aussi l'action visible",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Bonus souvent oublié"
    alert_bullets = [
        "Les moteurs de recherche indexent les transcriptions - référencement gratuit",
        "Les utilisateurs qui cherchent une citation précise vous remercient",
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
        "Différence avec les sous-titres : sous-titres = synchronisés avec la vidéo, "
        "transcription = texte autonome lisible hors vidéo. "
        "Les deux coexistent pour une vidéo de référence. "
        "Piège : publier une transcription brute générée par Whisper sans relecture - bourrée d'erreurs.",
    )
    return slide
