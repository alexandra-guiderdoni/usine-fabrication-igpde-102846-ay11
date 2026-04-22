"""Slide 34 : Pilier 1 - Listes natives.

Règles neuropédagogie appliquées :
- R10 : Bon/Mauvais contrastant pour discrimination
- R19 : Procédure action avec boutons dans le ruban
- R15 : Démonstration pratique proposée
"""

from igpde_dsfr_components import (
    add_exemple_contre_exemple, add_callout, add_notes, new_slide,
    estimate_callout_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 1 - Listes natives",
        fil_ariane="2. Documents accessibles | 1. Structure",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Structure",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_exemple_contre_exemple(
        slide,
        "Liste accessible",
        [
            "Le lecteur annonce : liste de 3 éléments, élément 1 sur 3",
            "Navigation par élément avec les touches flèches",
            "Créer avec : Accueil > Paragraphe > Puces ou Numérotation"
        ],
        "Liste inaccessible",
        [
            "Tirets manuels : le lecteur lit tiret Premier élément",
            "Tabulations pour simuler une numérotation",
            "Réseaux d'espaces pour aligner visuellement"
        ],
        top=2.45,
        height=3.0
    )

    callout_bullets = [
        "Maj+F1 (Révéler la mise en forme) > Puces et numérotation doit apparaître"
    ]
    add_callout(
        slide,
        "Vérification",
        callout_bullets,
        top=5.40
    )

    add_notes(
        slide,
        "Démonstration rapide : créer une liste avec tirets manuels, passer en mode "
        "lecteur d'écran ou montrer la capture. Refaire avec la fonctionnalité native. "
        "L'annonce change complètement. Ce réflexe s'acquiert en 2 minutes."
    )
    return slide
