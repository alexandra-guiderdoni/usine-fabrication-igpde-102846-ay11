"""Slide 5 : Easy Check 1 - Règles de rédaction de l'alt text.

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
        titre="Rédiger un alt text qui sert vraiment",
        fil_ariane="3. Easy Checks | 1. Alternatives textuelles",
        footer_text=f"{ctx.footer_base} / Easy Checks - Alt text",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.35)

    callout_titre = "5 règles pour un alt text utile :"
    callout_bullets = [
        "Concis : 125 caractères maximum",
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
        "Un nom de fichier (IMG_4578.jpg) en guise d’alt = alt absent pour l’utilisateur",
        "Un alt qui décrit la décoration au lieu du contenu utile",
    ]
    add_alert(
        slide, titre=alert_titre, bullets=alert_bullets,
        top=stack.push(estimate_alert_height(alert_titre, alert_bullets)),
        alert_type="warning",
    )

    add_notes(
        slide,
        "Prédiction avant de montrer les 5 règles : « Combien de caractères max pour un bon alt ? » "
        "La plupart diront 255 - la bonne réponse est 125 (JAWS coupe au-delà). "
        "Exemple live : une photo du ministère avec alt=\"photo du ministère de Bercy prise en 2023\" "
        "→ refactorer en \"Ministère de Bercy, façade ouest.\" - même info, moitié de caractères.",
    )
    return slide
