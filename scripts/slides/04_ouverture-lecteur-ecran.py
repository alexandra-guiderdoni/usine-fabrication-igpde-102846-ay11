"""Slide 29 : Ouverture - Le lecteur d'écran en action.

Règles neuropédagogie appliquées :
- R5 : Contextualisation par la perspective utilisateur (empathie)
- R8 : Déclenchement émotionnel (citation choquante) pour créer l'attention
- R13 : Chiffre ancrant (15 %, 80 %, 1 sur 12) pour mémorisation
"""

from igpde_dsfr_components import add_quote, add_alert, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        titre="Le lecteur d'écran en action",
        fil_ariane="2. Documents accessibles",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Contexte",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_quote(
        slide,
        "Texte, texte, texte, texte, texte, texte... Pendant 4 minutes. Sans titre. Sans repère. Sans pouvoir naviguer vers la section qui le concerne.",
        auteur="Ce qu'entend une personne malvoyante face à votre document Word",
        top=2.3
    )

    add_alert(
        slide,
        "15 % de vos destinataires sont concernés",
        [
            "80 % de ces handicaps sont invisibles",
            "Dans une réunion de 12 personnes : au moins 1 daltonien",
            "Parmi 30 destinataires : 4 ou 5 ont un handicap"
        ],
        top=4.5,
        alert_type="warning"
    )

    add_notes(
        slide,
        "Lire la citation à voix haute, lentement, avec des pauses. Ne pas commenter. "
        "Laisser le silence s'installer 5 secondes. Demander : est-ce que vous avez déjà reçu "
        "un document ou un email illisible ? Cette personne vivait ça tous les jours."
    )
    return slide
