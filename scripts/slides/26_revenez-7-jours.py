"""Slide 51 : Revenez dans 7 jours - Répétitions espacées.

Règles neuropédagogie appliquées :
- R24 : Répétitions espacées (J+7, J+30) pour mémorisation long terme
- R4 : Récupération active (refaire le quiz)
- R22 : Progression (niveaux de maîtrise : 3/5 vs 5/5)
"""

from igpde_dsfr_components import (
    add_callout, add_highlight, add_notes, new_slide,
    estimate_callout_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        titre="Revenez dans 7 jours",
        fil_ariane="2. Documents accessibles | Répétitions espacées",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Répétitions",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    callout1_bullets = [
        "5/5 : les réflexes sont installés - passez à la checklist sur un vrai document",
        "3-4/5 : relisez les piliers correspondant aux erreurs manquées",
        "Moins de 3 : reprenez les piliers 1 et 3 (80 % des cas)"
    ]
    add_callout(
        slide,
        "J+7 : refaites le quiz final sans rouvrir ce support",
        callout1_bullets,
        top=2.3
    )

    callout2_bullets = [
        "Parcourez la checklist de haut en bas",
        "C'est le seul test qui compte"
    ]
    add_callout(
        slide,
        "J+30 : ouvrez votre prochain document Word",
        callout2_bullets,
        top=4.1
    )

    add_highlight(
        slide,
        "Phrase-clé à 6 mois : Titres avec styles, images avec texte alt, vérificateur avant d'envoyer.",
        top=5.60
    )

    add_notes(
        slide,
        "Les répétitions espacées multiplient par 3 la rétention à long terme "
        "(Ebbinghaus, confirmé par Pashler 2007). J+7 = pic de l'oubli. J+30 = consolidation "
        "à long terme. La phrase-clé est l'ancre : si un stagiaire ne retient qu'une chose, "
        "c'est ça."
    )
    return slide
