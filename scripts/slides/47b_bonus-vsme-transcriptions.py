"""Slide bonus : audio-description et niveaux de transcription.

Règles neuropédagogie appliquées :
- R5 : chunking - une colonne audio-description, une colonne transcription
- R15 : jargon traduit - l'audio-description expliquée par l'usage
- R24 : action concrète - choisir le niveau utile avant publication
"""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    CONTENT_W,
    MARGIN_L,
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
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Bonus médias : Audio-description et transcription",
        fil_ariane="3. points de contrôle rapides | Bonus médias",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Bonus médias",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.16)

    message = "Image et son : proposer un autre accès à toute information utile."
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    audiodescription_titre = "Audio-description : ce que ça ajoute"
    audiodescription_bullets = [
        "Décors, lieux et changements de scène utiles",
        "Actions, gestes et expressions qui ne s’entendent pas",
        "Textes et informations importantes affichés à l’écran",
        "Une voix placée dans les silences, sans couvrir les dialogues",
    ]
    transcript_titre = "Transcription : choisir le niveau"
    transcript_bullets = [
        "Semi-intégrale : résumé détaillé + citations",
        "Intégrale éditée : texte complet, corrigé et lisible",
        "Verbatim : mot à mot, hésitations et sons inclus",
    ]
    col_h = max(
        estimate_callout_height(
            audiodescription_titre,
            audiodescription_bullets,
            COL_W,
            line_spacing=1.15,
        ),
        estimate_alert_height(transcript_titre, transcript_bullets, COL_W, line_spacing=1.15),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide,
        audiodescription_titre,
        audiodescription_bullets,
        top=top_cols,
        left=MARGIN_L,
        width=COL_W,
        line_spacing=1.15,
    )
    add_alert(
        slide,
        transcript_titre,
        transcript_bullets,
        top=top_cols,
        left=COL_R,
        width=COL_W,
        alert_type="info",
        line_spacing=1.15,
    )

    rappel = "IA utile pour brouillonner. Publication seulement après relecture humaine."
    add_highlight(
        slide,
        rappel,
        top=stack.push(estimate_highlight_height(rappel, CONTENT_W)),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    add_notes(
        slide,
        "L’audio-description rend accessibles les informations visuelles essentielles : lieux, actions, gestes, "
        "expressions et textes affichés. Elle s’insère dans les silences sans couvrir les dialogues ni les sons utiles. "
        "Pour la transcription, faire choisir le niveau adapté à l’usage : semi-intégrale pour restituer l’essentiel, "
        "intégrale éditée pour une lecture complète et fluide, verbatim lorsqu’une restitution mot à mot est nécessaire. "
        "Un outil d’IA peut produire un premier jet, mais la publication exige une relecture humaine.",
    )
    return slide
