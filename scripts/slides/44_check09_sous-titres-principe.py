"""Slide 19 : Point de contrôle rapide 9 - Sous-titres vidéo, le principe.

Règles neuropédagogie appliquées :
- R3 : WIIFM - les sous-titres servent aussi quand le son est indisponible
- R8 : analogie - les sous-titres servent aussi dans un train bruyant
- R5 : chunking - 3 bénéficiaires clés
"""

from igpde_dsfr_components import (
    Stack,
    add_callout,
    add_highlight,
    add_notes,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Sous-titres : le son que tout le monde lit",
        fil_ariane="3. points de contrôle rapides | 9. Sous-titres vidéo",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Sous-titres vidéo",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    add_highlight(
        slide,
        "Une vidéo sans sous-titres devient inutilisable dès que le son manque, est coupé ou ne peut pas être entendu.",
        top=stack.push(estimate_highlight_height('Une vidéo sans sous-titres devient inutilisable dès que le son manque, est coupé ou ne peut pas être entendu.')),
    )

    add_callout(
        slide,
        "Ce qu’il faut vérifier :",
        [
            "La vidéo propose des sous-titres synchronisés (pas seulement une transcription)",
            "Les sous-titres incluent les paroles ET les informations sonores importantes : « (rires) », « (sonnerie) »",
            "Ils sont activables/désactivables par l’utilisateur (bouton CC)",
        ],
        top=stack.push(estimate_callout_height('Ce qu’il faut vérifier :', ['La vidéo propose des sous-titres synchronisés (pas seulement une transcription)', 'Les sous-titres incluent les paroles ET les informations sonores importantes : « (rires) », « (sonnerie) »', 'Ils sont activables/désactivables par l’utilisateur (bouton CC)'])),
    )

    add_notes(
        slide,
        "Analogie : dans un train bruyant, même un entendant lit les sous-titres. "
        "Bénéficiaires (faire deviner) : personnes sourdes ou malentendantes, "
        "utilisateurs en open space, apprenants d’une langue étrangère, personnes qui préfèrent lire. "
        "Nuance capitale : une transcription écrite sur la page n’est pas un sous-titre - les deux sont utiles, "
        "pas interchangeables.",
    )
    return slide
