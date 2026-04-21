"""Slide 35 : Pilier 1 - Tableaux et objets flottants.

Règles neuropédagogie appliquées :
- R1 : Citation fondatrice pour ancrer la règle d'or
- R19 : Procédure détaillée (propriétés du tableau, habillage)
- R11 : Alerte pour piège courant
"""

from igpde_dsfr_components import (
    add_quote, add_callout, add_alert, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 1 - Tableaux et objets flottants",
        fil_ariane="2. Documents accessibles | 1. Structure",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Structure",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_quote(
        slide,
        "Si vous touchez à Tab, Espace ou Entrée pour simuler une mise en page, "
        "vous créez une barrière invisible pour les technologies d'assistance.",
        auteur="La règle d'or",
        top=2.3
    )

    callout1_bullets = [
        "Insertion > Tableau > choisir les colonnes et lignes",
        "Habillage : clic droit > Propriétés > Habillage = Aucun",
        "Un tableau flottant (Autour) n'est pas lu au bon moment"
    ]
    add_callout(
        slide,
        "Tableaux de mise en page",
        callout1_bullets,
        top=4.0
    )

    alert_bullets = [
        "Invisibles ou lus dans un ordre aléatoire par le lecteur d'écran",
        "Solution : colonnes intégrées Word ou habillage En ligne avec le texte"
    ]
    add_alert(
        slide,
        "Objets flottants : zones de texte et images en habillage Devant le texte",
        alert_bullets,
        top=5.7,
        alert_type="warning"
    )

    add_notes(
        slide,
        "Piège le plus fréquent pour les communicants : la mise en page par espaces "
        "et tabulations. Montrer le mode Afficher tout (symbole paragraphe) pour révéler "
        "les espaces parasites. Les zones de texte flottantes sont un piège classique "
        "dans les documents Word avec mise en page élaborée."
    )
    return slide
