"""Slide 22 : Easy Check 11 - Audiodescription.

Règles neuropédagogie appliquées :
- R8 : analogie - la voix off qui décrit l'écran pour qui ne le voit pas
- R3 : WIIFM - obligation légale dès qu'il y a une vidéo informative
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
        fil_ariane="3. Easy Checks | 11. Audiodescription",
        footer_text=f"{ctx.footer_base} / Easy Checks - Audiodescription",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_highlight(
        slide,
        "L’audiodescription ajoute une voix off qui décrit les images clés pendant les silences.",
        top=stack.push(estimate_highlight_height('L’audiodescription ajoute une voix off qui décrit les images clés pendant les silences.')),
    )

    add_callout(
        slide,
        "Ce qu’il faut vérifier :",
        [
            "La vidéo propose une piste audiodécrite activable (bouton AD)",
            "L’audiodescription décrit les éléments visuels essentiels à la compréhension",
            "Elle s’intercale dans les silences, sans couvrir les dialogues",
            "Pour une vidéo sans dialogue essentiel : une description textuelle synchronisée suffit",
        ],
        top=stack.push(estimate_callout_height('Ce qu’il faut vérifier :', ['La vidéo propose une piste audiodécrite activable (bouton AD)', 'L’audiodescription décrit les éléments visuels essentiels à la compréhension', 'Elle s’intercale dans les silences, sans couvrir les dialogues', 'Pour une vidéo sans dialogue essentiel : une description textuelle synchronisée suffit'])),
    )

    add_quote(
        slide,
        texte="Sans audiodescription, une vidéo reste une porte fermée pour 1,7 million de personnes aveugles ou malvoyantes en France.",
        auteur="Fédération des Aveugles de France",
        top=stack.push(estimate_quote_height('Sans audiodescription, une vidéo reste une porte fermée pour 1,7 million de personnes aveugles ou malvoyantes en France.', 'Fédération des Aveugles de France')),
    )

    add_notes(
        slide,
        "Démo : montrer 30 secondes d’un film d’animation sans dialogue, puis avec audiodescription. "
        "Le contraste est saisissant. "
        "Exception pratique : si la vidéo est entièrement commentée en voix off (ex. reportage narré), "
        "l’audiodescription est souvent superflue - tout est déjà dit.",
    )
    return slide
