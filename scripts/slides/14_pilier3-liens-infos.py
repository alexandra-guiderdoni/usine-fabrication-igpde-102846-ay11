"""Slide 39 : Pilier 3 - Liens et informations essentielles.

Règles neuropédagogie appliquées :
- R10 : Tableau mauvais/bon pour discrimination des liens
- R11 : Alerte sur les zones invisibles (en-têtes, pieds, filigranes)
- R19 : Procédure enrichie pour liens de téléchargement
"""

from igpde_dsfr_components import (
    add_tableau, add_callout, add_alert, add_notes, new_slide,
    MARGIN_L, COL_W, COL_R,
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

    add_alert(
        slide,
        "Informations essentielles dans les zones non lues",
        [
            "En-têtes et pieds de page : non lus automatiquement",
            "Filigranes (Confidentiel, Brouillon) : invisibles",
            "Solution : reproduire l'info dans le corps du document",
        ],
        top=4.4,
        left=MARGIN_L,
        width=COL_W,
        alert_type="warning",
        line_spacing=1.0,
    )

    add_callout(
        slide,
        "Liens de téléchargement",
        [
            "Titre + format + poids + langue si différente",
            "Exemple : Rapport annuel 2024 (PDF, 2 Mo, anglais)",
        ],
        top=4.4,
        left=COL_R,
        width=COL_W,
        line_spacing=1.0,
    )

    add_notes(
        slide,
        "Lire à voix haute les liens inaccessibles puis les accessibles. La différence "
        "est immédiate. Pour les filigranes : montrer un vrai document avec CONFIDENTIEL "
        "en filigrane. Demander : est-ce que votre lecteur d'écran l'annonce ? Non - "
        "il faut reproduire l'information dans le corps du document."
    )
    return slide
