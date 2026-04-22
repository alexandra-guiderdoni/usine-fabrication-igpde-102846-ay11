"""Slide 7 : Easy Check 2 - Titre de page.

Règles neuropédagogie appliquées :
- R8 : analogie - le titre de page est l'étiquette de l'onglet
- R3 : WIIFM - pourquoi ça change la vie des utilisateurs multi-onglets
- R19 : exemple OK/KO direct
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
        titre="Titre de page : l’étiquette qui oriente",
        fil_ariane="3. Easy Checks | 2. Titre de page",
        footer_text=f"{ctx.footer_base} / Easy Checks - Titre de page",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.25)

    highlight_texte = (
        "Le titre de page est la 1ʳᵉ chose que lit un lecteur d’écran "
        "et la seule chose visible dans l’onglet."
    )
    add_highlight(
        slide, highlight_texte,
        top=stack.push(estimate_highlight_height(highlight_texte)),
    )

    callout_titre = "Ce qu’il faut vérifier :"
    callout_bullets = [
        "Chaque page a un titre unique, différent des autres pages du site",
        "Le titre décrit le contenu puis le nom du site (« Déclarer - impots.gouv.fr »)",
        "Il change quand le contenu principal change (recherche, étape de formulaire)",
    ]
    add_callout(
        slide, callout_titre, callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Exemples"
    alert_bullets = [
        "OK : « Résultats de recherche : accessibilité - Ministère de la Culture »",
        "KO : « Accueil » sur chaque page du site",
        "KO : « Untitled Document » (oubli fréquent sur les PDF)",
    ]
    add_alert(
        slide, titre=alert_titre, bullets=alert_bullets,
        top=stack.push(estimate_alert_height(alert_titre, alert_bullets)),
        alert_type="info",
    )

    add_notes(
        slide,
        "Démo live : ouvrir 3 onglets de sites publics, demander lequel est identifiable juste à l’étiquette. "
        "Piège des CMS : beaucoup héritent du titre du template - toutes les pages « Accueil ». "
        "Outil : survoler l’onglet dans le navigateur ou regarder la balise <title>.",
    )
    return slide
