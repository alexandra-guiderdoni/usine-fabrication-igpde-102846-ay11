"""Slide 29 : Ouverture - Le lecteur d'écran en action.

Règles neuropédagogie appliquées :
- R5 : Contextualisation par la perspective utilisateur (empathie)
- R8 : Déclenchement émotionnel (citation choquante) pour créer l'attention
- R13 : Chiffre ancrant (15 %, 80 %, 1 sur 12) pour mémorisation
"""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L,
    add_card, add_notes, estimate_card_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Le lecteur d'écran en action",
        fil_ariane="2. Documents accessibles | Ouverture",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Contexte",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    cartes = [
        (
            "Ce qu’entend le lecteur d’écran",
            "Texte, texte, texte, texte, texte, texte ...\n\n"
            "Pendant 4 minutes. Sans titre. Sans repère.\n"
            "Sans pouvoir naviguer vers la section qui le concerne.\n\n"
            "-> C'est ce qu'entend une personne malvoyante face à votre document Word.",
            MARGIN_L,
        ),
        (
            "15 % de vos destinataires sont concernés",
            [
                "80 % de ces handicaps sont invisibles",
                "Dans une réunion de 12 personnes : au moins 1 daltonien",
                "Parmi 30 destinataires : 4 ou 5 ont un handicap",
            ],
            COL_R,
        ),
    ]
    card_height = max(
        estimate_card_height(titre, contenu, COL_W)
        for titre, contenu, _ in cartes
    )
    for titre, contenu, left in cartes:
        add_card(
            slide,
            titre=titre,
            contenu=contenu,
            top=2.45,
            left=left,
            width=COL_W,
            height=card_height,
            title_size=16,
            body_line_spacing=1.25,
        )

    add_notes(
        slide,
        "Lire la citation à voix haute, lentement, avec des pauses. Ne pas commenter. "
        "Laisser le silence s'installer 5 secondes. Demander : est-ce que vous avez déjà reçu "
        "un document ou un email illisible ? Cette personne vivait ça tous les jours."
    )
    return slide
