"""Slide 39 : Pilier 3 - Liens et informations essentielles.

Règles neuropédagogie appliquées :
- R10 : Tableau mauvais/bon pour discrimination des liens
- R11 : Alerte sur les zones invisibles (en-têtes, pieds, filigranes)
- R19 : Procédure enrichie pour liens de téléchargement
"""

from igpde_dsfr_components import (
    add_tableau, add_alert, add_callout, add_notes, new_slide,
    estimate_alert_height, estimate_callout_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 3 - Liens et informations essentielles",
        fil_ariane="2. Documents accessibles | 3. Contenus",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Contenus",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_tableau(
        slide,
        ["Inaccessible", "Accessible"],
        [
            [
                "Cliquez ici",
                "Consulter le guide d'accessibilité Word"
            ],
            [
                "En savoir plus",
                "Télécharger le rapport annuel 2024 (PDF, 2 Mo)"
            ],
            [
                "URL brute",
                "Accéder au formulaire de contact"
            ]
        ],
        top=2.3,
        col_widths=[4.5, 7.78]
    )

    alert_bullets = [
        "En-têtes et pieds de page : non lus automatiquement",
        "Filigranes (CONFIDENTIEL, BROUILLON) : invisibles pour le lecteur",
        "Solution : reproduire l'information essentielle dans le corps du document"
    ]
    add_alert(
        slide,
        "Informations essentielles dans les zones non lues",
        alert_bullets,
        top=4.0,
        alert_type="warning"
    )

    callout_bullets = [
        "Intégrer : titre + format + poids + langue si elle diffère du document",
        "Exemple : \"Rapport annuel 2024 (PDF, 2 Mo, version anglaise)\""
    ]
    add_callout(
        slide,
        "Pour les liens de téléchargement",
        callout_bullets,
        top=5.50
    )

    add_notes(
        slide,
        "Lire à voix haute les liens inaccessibles puis les accessibles. La différence "
        "est immédiate. Pour les filigranes : montrer un vrai document avec CONFIDENTIEL "
        "en filigrane. Demander : est-ce que votre lecteur d'écran l'annonce ? Non - "
        "il faut le mettre dans le corps."
    )
    return slide
