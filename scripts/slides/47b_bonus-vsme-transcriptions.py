"""Slide bonus : VSME et niveaux de transcription.

Règles neuropédagogie appliquées :
- R5 : chunking - une colonne VSME, une colonne transcription
- R15 : jargon traduit - VSME expliqué par l'usage
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
        titre="Bonus médias : VSME et transcriptions",
        fil_ariane="3. points de contrôle rapides | Bonus médias",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Bonus médias",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.16)

    message = (
        "Quand le son porte de l'information, la transcription des paroles ne suffit pas toujours."
    )
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    vsme_titre = "VSME : ce que ça ajoute"
    vsme_bullets = [
        "Dialogues visibles et hors champ",
        "Bruits utiles, effets sonores et musique",
        "Voix off, narration, pensée intérieure",
        "Langue étrangère et son venant d'un haut-parleur",
    ]
    transcript_titre = "Transcription : choisir le niveau"
    transcript_bullets = [
        "Semi-intégrale : résumé détaillé + citations",
        "Intégrale éditée : texte complet, corrigé et lisible",
        "Verbatim : mot à mot, hésitations et sons inclus",
    ]
    col_h = max(
        estimate_callout_height(vsme_titre, vsme_bullets, COL_W, line_spacing=1.15),
        estimate_alert_height(transcript_titre, transcript_bullets, COL_W, line_spacing=1.15),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide,
        vsme_titre,
        vsme_bullets,
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
        "VSME signifie Voix, Sons, Musiques et Éléments sonores. "
        "La codification classique utilise notamment : blanc pour les dialogues visibles, jaune pour le hors champ, "
        "rouge pour les bruits importants, magenta pour la musique, cyan pour les voix off ou narrations, "
        "vert pour une langue étrangère, et un astérisque quand le son vient d'un haut-parleur. "
        "Ne pas demander au groupe de mémoriser les couleurs : l'objectif pédagogique est de comprendre que le son utile "
        "ne se limite pas aux dialogues.",
    )
    return slide
