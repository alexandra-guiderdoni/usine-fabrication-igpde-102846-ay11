"""Slide 41 : Langue, majuscules et lisibilité.

Règles neuropédagogie appliquées :
- R19 : Procédures détaillées (balisage de langue, casse)
- R18 : Analogues pour dyslexie et prononciation (e vs è)
- R14 : Stack avec 3 callouts pour multiples procédures
"""

from igpde_dsfr_components import (
    add_callout, add_notes, new_slide,
    COL_R, COL_W, MARGIN_L,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Langue, majuscules et lisibilité",
        fil_ariane="2. Documents accessibles | 4. Langue",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Langue",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    balise_bullets = [
        "Langue principale : Fichier > Options > Langue",
        "Passage en langue étrangère : sélectionner le texte > Révision > Langue > Définir la langue",
        "Sans balisage de langue, le lecteur d'écran prononce mal le mot"
    ]
    add_callout(
        slide,
        "Balisage de langue",
        balise_bullets,
        top=2.3,
    )

    maj_bullets = [
        "Difficiles à lire pour les dyslexiques",
        "Prononciation ambiguë par les lecteurs d'écran",
        "Solution : minuscules d'abord, puis Police > Modifier la casse",
    ]
    add_callout(
        slide,
        "Majuscules : deux problèmes",
        maj_bullets,
        top=4.55,
        left=MARGIN_L,
        width=COL_W,
    )

    lisibilite_bullets = [
        "Police sans serif, 12 pt minimum",
        "Interligne 1,15, paragraphes aérés",
        "Alignement à gauche, pas de justification",
        "Contraste mesuré, fond non dégradé",
    ]
    add_callout(
        slide,
        "Lisibilité",
        lisibilite_bullets,
        top=4.55,
        left=COL_R,
        width=COL_W,
        line_spacing=1.05,
    )

    add_notes(
        slide,
        "Exemple concret de balisage : un document français avec un titre en anglais "
        "Annual Report. Sans balisage, le lecteur d'écran français prononce les mots "
        "anglais avec un accent français incompréhensible. Majuscules : UN INTERNE TUE - "
        "donne le ton d'une phrase choc en majuscules, pas d'un texte en majuscules. "
        "Pour la lisibilité, faire le lien avec les règles transversales vues en module 1 : "
        "police simple, texte aligné à gauche, paragraphes aérés, contraste mesuré et fonds non dégradés."
    )
    return slide
