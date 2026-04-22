"""Slide 44 : Pilier 5 - Le vérificateur d'accessibilité Word.

Règles neuropédagogie appliquées :
- R14 : Tableau montrant détecte vs ne détecte pas
- R3 : Démystification des limites de l'outil
- R9 : Réalisme pédagogique (pas de faux sentiment de sécurité)
"""

from igpde_dsfr_components import (
    add_tableau, add_alert, add_notes, new_slide,
    estimate_alert_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 5 - Le vérificateur d'accessibilité Word",
        fil_ariane="2. Documents accessibles | 5. Finalisation",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Finalisation",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_tableau(
        slide,
        ["Ce qu'il détecte", "Ce qu'il ne détecte PAS"],
        [
            [
                "Texte alt manquant sur les images",
                "Qualité du texte alt (contenu)"
            ],
            [
                "Styles de titre absents",
                "Pertinence des noms de liens"
            ],
            [
                "Ordre de lecture problématique",
                "Couleur porteuse de sens seule"
            ],
            [
                "Tableaux sans en-tête",
                "Langue des passages étrangers"
            ],
            [
                "",
                "Contraste insuffisant"
            ]
        ],
        top=2.3,
        col_widths=[6.14, 6.14]
    )

    alert_bullets = [
        "Il signale ce qu'il peut détecter automatiquement - pas ce qui est vraiment accessible",
        "Une absence d'erreur ne signifie pas que le document est accessible"
    ]
    add_alert(
        slide,
        "Le vérificateur est un premier filtre, pas un certificat de conformité.",
        alert_bullets,
        top=5.30,
        alert_type="warning"
    )

    add_notes(
        slide,
        "Analogie : le vérificateur d'orthographe ne détecte pas les fautes de sens "
        "(il accepte et la et à). Le vérificateur d'accessibilité ne détecte pas un texte "
        "alt vide de sens. Les 5 colonnes du tableau montrent la limite de l'outil. "
        "Toujours faire une relecture humaine."
    )
    return slide
