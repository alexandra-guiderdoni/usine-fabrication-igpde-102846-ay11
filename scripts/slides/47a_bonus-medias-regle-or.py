"""Slide bonus : règle d'or des médias accessibles sur le web.

Règles neuropédagogie appliquées :
- R3 : WIIFM - un média bloqué doit rester utilisable autrement
- R5 : chunking - 3 familles de médias, 3 contrôles bonus
- R21 : échafaudage - synthèse placée après les checks médias
"""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    CONTENT_W,
    MARGIN_L,
    Stack,
    add_alert,
    add_callout,
    add_highlight,
    add_notes,
    estimate_alert_height,
    estimate_callout_height,
    estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Bonus médias : toujours 2 accès",
        fil_ariane="3. points de contrôle rapides | Bonus médias",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Bonus médias",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.18)

    message = (
        "Règle d'or : un média en ligne doit rester compréhensible "
        "par au moins deux chemins : voir, lire ou écouter."
    )
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    acces_titre = "Le réflexe"
    acces_bullets = [
        "Image, schéma ou plan -> description ou texte alternatif",
        "Vidéo -> sous-titres + informations visuelles essentielles",
        "Audio ou podcast -> transcription visible et relue",
    ]
    qualite_titre = "Les pièges à repérer"
    qualite_bullets = [
        "Sous-titres lisibles : contraste fort, bandeau si besoin",
        "Format réseau social : sous-titres non masqués par l'interface",
        "PDF : texte sélectionnable, pas une image scannée",
    ]
    col_h = max(
        estimate_callout_height(acces_titre, acces_bullets, COL_W, line_spacing=1.2),
        estimate_alert_height(qualite_titre, qualite_bullets, COL_W, line_spacing=1.2),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide,
        acces_titre,
        acces_bullets,
        top=top_cols,
        left=MARGIN_L,
        width=COL_W,
        line_spacing=1.2,
    )
    add_alert(
        slide,
        qualite_titre,
        qualite_bullets,
        top=top_cols,
        left=COL_R,
        width=COL_W,
        alert_type="info",
        line_spacing=1.2,
    )

    add_notes(
        slide,
        "Positionner cette slide comme une synthèse, pas comme un nouveau critère. "
        "Elle relie les contrôles déjà vus : alternatives textuelles, sous-titres, transcription et audiodescription. "
        "Question à poser au groupe : si je coupe le son, si je ne vois pas l'image, ou si le PDF est scanné, "
        "est-ce que l'information reste accessible ?",
    )
    return slide
