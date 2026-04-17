"""Slide 12 : Easy Check 5 - Lien d'évitement.

Règles neuropédagogie appliquées :
- R8 : analogie - l'ascenseur qui évite les 3 étages de menu
- R3 : WIIFM - gain de temps massif pour l'utilisateur clavier
- R11 : faire deviner combien de Tab on économise
"""

from igpde_dsfr_components import (
    Stack, add_alert, add_callout, add_highlight, add_notes,
    estimate_alert_height, estimate_callout_height, estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Lien d’évitement : le raccourci qui sauve 30 Tab",
        fil_ariane="3. Easy Checks | 5. Lien d’évitement",
        footer_text=f"{ctx.footer_base} / Easy Checks - Lien d’évitement",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    highlight_texte = (
        "Sans lien d’évitement, un utilisateur clavier tabule 20 à 40 fois "
        "par page juste pour franchir le menu."
    )
    add_highlight(
        slide, highlight_texte,
        top=stack.push(estimate_highlight_height(highlight_texte)),
    )

    callout_titre = "Ce qu’il faut vérifier :"
    callout_bullets = [
        "Un lien « Aller au contenu » est le 1ᵉʳ élément reçu par Tab en haut de page",
        "Il devient visible dès qu’il a le focus, même s’il était masqué",
        "Il mène au bloc principal via une ancre (#contenu, #main)",
    ]
    add_callout(
        slide, callout_titre, callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Démo en 3 Tab"
    alert_bullets = [
        "Ouvrez gouvernement.fr, appuyez sur Tab : le lien « Contenu » apparaît en haut à gauche",
        "Entrée → vous voilà au contenu, menu contourné",
    ]
    add_alert(
        slide, titre=alert_titre, bullets=alert_bullets,
        top=stack.push(estimate_alert_height(alert_titre, alert_bullets)),
        alert_type="success",
    )

    add_notes(
        slide,
        "Analogie : l’ascenseur dans un immeuble. Sans ascenseur, chacun monte les 10 étages à pied - "
        "y compris les personnes qui ne peuvent pas. "
        "Faire deviner : combien de tabulations sur la page de leur intranet pour arriver au contenu ? "
        "(réponse typique : 15-30). "
        "Rappel : le lien d’évitement peut être masqué visuellement mais doit apparaître au focus clavier.",
    )
    return slide
