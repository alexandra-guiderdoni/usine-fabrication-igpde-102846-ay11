"""Slide 41 : Langue, majuscules et lisibilité.

Règles neuropédagogie appliquées :
- R19 : Procédures détaillées (balisage de langue, casse)
- R18 : Analogues pour dyslexie et prononciation (e vs è)
- R14 : Stack avec 3 callouts pour multiples procédures
"""

from igpde_dsfr_components import (
    add_callout, add_highlight, add_notes, new_slide, Stack,
    estimate_callout_height, estimate_highlight_height
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

    stack = Stack(top=2.3, gap=0.25)

    balise_bullets = [
        "Langue principale : Fichier > Options > Langue",
        "Passage en langue étrangère : sélectionner le texte > Révision > Langue > Définir la langue",
        "Sans balisage de langue, le lecteur d'écran prononce mal le mot"
    ]
    add_callout(
        slide,
        "Balisage de langue",
        balise_bullets,
        top=stack.push(estimate_callout_height("Balisage de langue", balise_bullets))
    )

    maj_bullets = [
        "Difficiles à lire pour les dyslexiques",
        "Prononciation ambiguë par les lecteurs d'écran",
        "Solution : minuscules d'abord, puis Police > Modifier la casse > MAJUSCULES"
    ]
    add_callout(
        slide,
        "Majuscules : deux problèmes",
        maj_bullets,
        top=stack.push(estimate_callout_height("Majuscules : deux problèmes", maj_bullets))
    )

    highlight_text = "Police sans serif (Arial, Marianne), 12 pt minimum, interligne 1,15. Ne pas justifier le texte."
    add_highlight(
        slide,
        highlight_text,
        top=stack.push(estimate_highlight_height(highlight_text))
    )

    add_notes(
        slide,
        "Exemple concret de balisage : un document français avec un titre en anglais "
        "Annual Report. Sans balisage, le lecteur d'écran français prononce les mots "
        "anglais avec un accent français incompréhensible. Majuscules : UN INTERNE TUE - "
        "donne le ton d'une phrase choc en majuscules, pas d'un texte en majuscules."
    )
    return slide
