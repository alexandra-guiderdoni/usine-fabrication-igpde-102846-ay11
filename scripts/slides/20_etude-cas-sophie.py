"""Slide 45 : Étude de cas - Le compte rendu de Sophie.

Règles neuropédagogie appliquées :
- R6 : Mise en situation (assistant de direction, cas réaliste)
- R16 : Interleaving (5 erreurs, 1 par pilier)
- R18 : Timing réaliste (8 minutes mesurées, pas estimées)
"""

from igpde_dsfr_components import (
    add_card, add_callout, add_notes, new_slide,
    estimate_card_height, estimate_callout_height,
    MARGIN_L, COL_W, COL_R,
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

    card1_titre = "Mise en situation"
    card1_contenu = [
        "Sophie, assistante de direction, doit publier son compte rendu de réunion.",
        "Quels piliers sont concernés ?",
        "Quelles corrections, dans quel ordre ?",
    ]

    card2_titre = "Le document contient"
    card2_contenu = [
        "titres en gras et tableaux sans en-tête",
        "une action en rouge sans étiquette texte",
        "image sans alt, lien cliquez ici",
        "passage anglais sans balisage de langue",
        "propriétés Titre et Auteur vides",
    ]

    card_h = max(
        estimate_card_height(card1_titre, card1_contenu, COL_W),
        estimate_card_height(card2_titre, card2_contenu, COL_W),
    )

    add_card(slide, card1_titre, card1_contenu, top=2.3, left=MARGIN_L, width=COL_W, height=card_h)
    add_card(slide, card2_titre, card2_contenu, top=2.3, left=COL_R, width=COL_W, height=card_h)

    callout_titre = "5 piliers, 5 corrections, 8 minutes"
    callout_bullets = [
        "P1 - Styles Titre 1/2/3 et Ligne d'en-tête dans chaque tableau",
        "P2 - Ajouter : Alerte avant le texte écrit en rouge",
        "P3 - Texte alt sur l'image et renommer le lien",
        "P4 - Sélectionner le passage > Révision > Langue > Définir",
        "P5 - Fichier > Informations > renseigner Titre et Auteur",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=round(2.3 + card_h + 0.25, 2),
    )

    add_notes(
        slide,
        "Sophie a tout faux, mais aucune de ses erreurs n'est due à de la mauvaise "
        "volonté - juste des habitudes. Tout le monde a fait au moins 3 de ces erreurs "
        "dans sa carrière. Le temps de 8 minutes est mesuré - pas estimé. Proposer aux "
        "stagiaires de corriger un vrai document en 8 minutes."
    )
    return slide
