"""Slide 45 : Étude de cas - Le compte rendu de Sophie.

Règles neuropédagogie appliquées :
- R6 : Mise en situation (assistant de direction, cas réaliste)
- R16 : Interleaving (5 tâches de piliers différents)
- R18 : Timing réaliste (8 minutes mesurées, pas estimées)
"""

from igpde_dsfr_components import (
    add_callout, add_stepper, add_highlight, add_notes, new_slide,
    estimate_callout_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Étude de cas : le compte rendu de Sophie",
        fil_ariane="2. Documents accessibles | Étude de cas",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Étude de cas",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    callout_bullets = [
        "3 niveaux de titres mis en gras manuellement",
        "2 tableaux avec la 1re ligne en gras (sans ligne d'en-tête identifiée)",
        "1 organigramme sans texte alternatif",
        "1 lien cliquez ici pour le formulaire",
        "Le filigrane CONFIDENTIEL"
    ]
    add_callout(
        slide,
        "Sophie, assistante de direction, doit publier un compte rendu de réunion.",
        callout_bullets,
        top=2.3
    )

    add_stepper(
        slide,
        [
            "Remplacer le gras manuel par les styles Titre 1, Titre 2, Titre 3",
            "Identifier la ligne d'en-tête dans chaque tableau (onglet Création > Ligne d'en-tête)",
            "Ajouter un texte alt sur l'organigramme : Organigramme du service - 4 équipes",
            "Renommer le lien : Accéder au formulaire de demande",
            "Ajouter CONFIDENTIEL en première ligne du document"
        ],
        top=4.8,
        height=2.0
    )

    add_highlight(
        slide,
        "Temps estimé : 8 minutes.",
        top=6.95
    )

    add_notes(
        slide,
        "Sophie a tout faux, mais aucune de ses erreurs n'est due à de la mauvaise "
        "volonté - juste des habitudes. Tout le monde a fait au moins 3 de ces erreurs "
        "dans sa carrière. Le temps de 8 minutes est mesuré - pas estimé. Proposer aux "
        "stagiaires de corriger un vrai document en 8 minutes."
    )
    return slide
