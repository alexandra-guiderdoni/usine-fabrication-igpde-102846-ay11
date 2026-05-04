"""Slide 22 : Point de contrôle rapide 11 - Audiodescription.

Règles neuropédagogie appliquées :
- R8 : analogie - la voix off qui décrit l'écran pour qui ne le voit pas
- R3 : WIIFM - ne pas perdre l'information portée uniquement par l'image
"""

from igpde_dsfr_components import (
    Stack,
    add_callout,
    add_highlight,
    add_notes,
    add_quote,
    estimate_callout_height,
    estimate_highlight_height,
    estimate_quote_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Audiodescription : la voix qui montre",
        fil_ariane="3. points de contrôle rapides | 11. Audiodescription",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Audiodescription",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.15)

    add_highlight(
        slide,
        "L’audiodescription ajoute une voix off qui décrit les images clés pendant les silences.",
        top=stack.push(estimate_highlight_height('L’audiodescription ajoute une voix off qui décrit les images clés pendant les silences.')),
    )

    callout_titre = "Ce qu’il faut vérifier :"
    callout_bullets = [
        "La vidéo propose une piste audiodécrite activable (bouton AD)",
        "L’audiodescription décrit les éléments visuels essentiels à la compréhension",
        "Elle s’intercale dans les silences, sans couvrir les dialogues",
        "Pour une vidéo sans dialogue essentiel : une description textuelle synchronisée suffit",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets, line_spacing=1.0)),
        line_spacing=1.0,
    )

    add_quote(
        slide,
        texte="Quand l’image porte l’information, elle doit aussi être disponible autrement que par la vue.",
        auteur="Principe d’accessibilité vidéo",
        top=stack.push(estimate_quote_height('Quand l’image porte l’information, elle doit aussi être disponible autrement que par la vue.', 'Principe d’accessibilité vidéo')),
    )

    add_notes(
        slide,
        "Démo : montrer 30 secondes d’un film d’animation sans dialogue, puis avec audiodescription. "
        "Le contraste est saisissant. "
        "Exception pratique : si la vidéo est entièrement commentée en voix off (ex. reportage narré), "
        "l’audiodescription est souvent superflue - tout est déjà dit.",
    )
    return slide
