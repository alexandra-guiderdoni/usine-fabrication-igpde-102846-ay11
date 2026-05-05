"""Slide bonus : liens et documents PDF sur une page web.

Règles neuropédagogie appliquées :
- R5 : chunking - 2 familles de signaux bonus
- R21 : échafaudage - bonus séparé des 13 points obligatoires
- R24 : action concrète - signaler dans la grille si rencontré
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
        titre="Bonus site web : liens et PDF à repérer",
        fil_ariane="3. points de contrôle rapides | Bonus",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Bonus web",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.12)

    message = (
        "Pendant l'audit, ces points ne remplacent pas les 13 checks. "
        "Mais si vous les voyez, notez-les : ils améliorent vraiment l'expérience utilisateur."
    )
    add_highlight(
        slide,
        message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
        left=MARGIN_L,
        width=CONTENT_W,
    )

    liens_titre = "Liens"
    liens_bullets = [
        "Éviter les pages saturées de liens sans hiérarchie",
        "Libellé explicite : « programme de l'exposition photo »",
        "Éviter « cliquez ici », « en savoir plus », « programme » seul",
        "Téléchargement : indiquer type et poids du fichier",
    ]
    pdf_titre = "Documents PDF"
    pdf_bullets = [
        "Texte sélectionnable : pas de PDF image ou scanné non navigable",
        "Structure : titres, sommaire et liens internes si le document est long",
        "Images avec texte alternatif",
        "Si possible : proposer aussi un format éditable ou OpenDocument",
    ]
    col_h = max(
        estimate_callout_height(liens_titre, liens_bullets, COL_W, line_spacing=1.05),
        estimate_alert_height(pdf_titre, pdf_bullets, COL_W, line_spacing=1.05),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide,
        liens_titre,
        liens_bullets,
        top=top_cols,
        left=MARGIN_L,
        width=COL_W,
        height=col_h,
        line_spacing=1.05,
    )
    add_alert(
        slide,
        pdf_titre,
        pdf_bullets,
        top=top_cols,
        left=COL_R,
        width=COL_W,
        alert_type="info",
        line_spacing=1.05,
    )

    add_notes(
        slide,
        "Positionner cette slide comme un bonus volontaire, pas comme un 14e et 15e point de contrôle. "
        "Pour les liens, rappeler le principe RGAA : un lien doit être compréhensible seul ou avec son contexte immédiat. "
        "La meilleure pratique reste un libellé directement explicite, surtout pour les personnes qui listent les liens avec un lecteur d'écran. "
        "Pour les fichiers en téléchargement, citer la logique Opquast : indiquer le format et la taille aide l'utilisateur à décider avant de télécharger. "
        "Nuance importante : ne pas transformer l'exercice en audit documentaire complet. "
        "Si un PDF pose problème, le noter comme signal bonus dans la grille, puis renvoyer vers les méthodes d'audit PDF ou vers le module Word/PDF.",
    )
    return slide
