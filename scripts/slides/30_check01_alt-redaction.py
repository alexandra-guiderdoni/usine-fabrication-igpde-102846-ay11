"""Slide 5 : Point de contrôle rapide 1 - Règles de rédaction du texte alternatif.

Règles neuropédagogie appliquées :
- R5 : chunking - 5 règles concrètes
- R15 : bannir le jargon - formulations simples
- R19 : feedback immédiat via exemples OK/KO
"""

from igpde_dsfr_components import (
    Stack, add_alert, add_callout, add_notes,
    estimate_alert_height, estimate_callout_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Rédiger un texte alternatif qui sert vraiment",
        fil_ariane="3. points de contrôle rapides | 1. Alternatives textuelles",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Texte alternatif",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    callout_titre = "5 règles pour un texte alternatif utile :"
    callout_bullets = [
        "Concis : une phrase courte, centrée sur l’information utile",
        "Objectif : décrit, ne commente pas",
        "Pas de « photo de » ni « image de » - le lecteur d’écran le dit déjà",
        "Contextuel : ce qui compte dans cette page, pas tout ce qui est visible",
        "Ponctué : point final, pour que le lecteur marque la pause",
    ]
    add_callout(
        slide, callout_titre, callout_bullets,
        top=stack.push(estimate_callout_height(callout_titre, callout_bullets)),
    )

    alert_titre = "Piège fréquent"
    alert_bullets = [
        "Un nom de fichier (IMG_4578.jpg) en guise de texte alternatif = information perdue",
        "Un texte alternatif qui décrit la décoration au lieu du contenu utile",
    ]
    add_alert(
        slide, titre=alert_titre, bullets=alert_bullets,
        top=stack.push(estimate_alert_height(alert_titre, alert_bullets)),
        alert_type="warning",
    )

    add_notes(
        slide,
        "Prédiction avant de montrer les 5 règles : « Qu’est-ce qui rend un texte alternatif vraiment utile ? » "
        "La bonne réponse n’est pas une longueur magique : c’est le contexte. "
        "Exemple live : une photo du ministère avec alt=\"photo du ministère de Bercy prise en 2023\" "
        "→ refactorer en \"Ministère de Bercy, façade ouest.\" - même info, moitié de caractères.",
    )
    return slide
