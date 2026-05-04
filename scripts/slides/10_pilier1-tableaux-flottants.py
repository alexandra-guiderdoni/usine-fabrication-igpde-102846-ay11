"""Slide 35 : Tableaux et objets flottants.

Règles neuropédagogie appliquées :
- R1 : Citation fondatrice pour ancrer la règle d'or
- R19 : Procédure détaillée (propriétés du tableau, habillage)
- R11 : Alerte pour piège courant
"""

from igpde_dsfr_components import (
    Stack, MARGIN_L, CONTENT_W,
    add_highlight, add_callout, add_alert, add_notes, new_slide,
    estimate_highlight_height, estimate_callout_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Tableaux et objets flottants",
        fil_ariane="2. Documents accessibles | 1. Structure",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Structure",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.20)

    regle_texte = (
        "Règle d'or : ne jamais utiliser Tab, Espace ou Entrée pour simuler une mise en page.\n"
        "Vous créez un obstacle de structure pour les technologies d'assistance."
    )
    add_highlight(slide, regle_texte,
                  top=stack.push(estimate_highlight_height(regle_texte, CONTENT_W)),
                  left=MARGIN_L, width=CONTENT_W)

    callout1_titre = "Tableaux de mise en page"
    callout1_bullets = [
        "Insertion > Tableau > colonnes et lignes",
        "Habillage : Propriétés > Aucun",
        "Un tableau flottant (Autour) est lu au mauvais moment",
    ]
    add_callout(slide, callout1_titre, callout1_bullets,
                top=stack.push(estimate_callout_height(callout1_titre, callout1_bullets, line_spacing=1.0)),
                left=MARGIN_L, width=CONTENT_W, line_spacing=1.0)

    alert_titre = "Objets flottants : zones de texte et images"
    alert_bullets = [
        "Lus dans un ordre aléatoire - solution : colonnes Word ou habillage En ligne",
    ]
    add_alert(slide, alert_titre, alert_bullets,
              top=5.75,
              left=MARGIN_L, width=CONTENT_W,
              alert_type="warning", line_spacing=1.0)

    add_notes(
        slide,
        "Piège le plus fréquent pour les communicants : la mise en page par espaces "
        "et tabulations. Montrer le mode Afficher tout (symbole paragraphe) pour révéler "
        "les espaces parasites. Les zones de texte flottantes sont un piège classique "
        "dans les documents Word avec mise en page élaborée."
    )
    return slide
