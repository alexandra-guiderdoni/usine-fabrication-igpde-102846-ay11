"""Slide rs_06 : texte alternatif - pourquoi et qui en bénéficie."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, Stack,
    add_callout, add_highlight, add_alert, add_notes, new_slide,
    estimate_highlight_height, estimate_callout_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Le texte alternatif : votre sous-titre d'image",
        fil_ariane="4. Réseaux sociaux | Geste 1 - Texte alternatif",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30

    analogie = (
        "L'alt text, c'est comme un sous-titre pour votre image : "
        "il dit ce qu'elle montre à ceux qui ne peuvent pas la voir."
    )
    hl_h = estimate_highlight_height(analogie, CONTENT_W)
    add_highlight(slide, analogie, top=top, left=MARGIN_L, width=CONTENT_W)

    top2 = round(top + hl_h + 0.25, 2)

    beneficiaires_titre = "Qui en bénéficie ?"
    beneficiaires_bullets = [
        "Personnes aveugles ou malvoyantes (lecteur d'écran lit l'alt text)",
        "Connexion lente ou image non chargée (le texte s'affiche à la place)",
        "Moteurs de recherche (Google indexe les images via l'alt text)",
        "Intelligences artificielles et outils d'analyse d'image",
        "Toute personne dans un contexte défavorable (mauvaise luminosité, etc.)",
    ]
    bh = estimate_callout_height(beneficiaires_titre, beneficiaires_bullets, COL_W)

    exemples_titre = "Concrètement sur les réseaux"
    exemples_bullets = [
        "LinkedIn : Modifier → Ajouter du texte alternatif",
        "Facebook : Modifier l'image → Texte alternatif",
        "Twitter/X : intégré au formulaire de publication",
        "Instagram : Paramètres avancés → Texte alternatif",
        "Canva : Clic droit sur l'image → Texte alternatif",
    ]
    eh = estimate_callout_height(exemples_titre, exemples_bullets, COL_W)

    col_h = max(bh, eh)
    add_callout(slide, beneficiaires_titre, beneficiaires_bullets,
                top=top2, left=MARGIN_L, width=COL_W, height=col_h)
    add_alert(slide, exemples_titre, exemples_bullets,
              top=top2, left=COL_R, width=COL_W, alert_type="info")

    add_notes(
        slide,
        "L'analogie du sous-titre fonctionne très bien - tout le monde comprend immédiatement. "
        "Insister sur le fait que ça bénéficie AUSSI au référencement : argument qui convainc "
        "les agents qui ne sont pas sensibles à l'accessibilité pure. "
        "Montrer rapidement où trouver le champ alt text sur LinkedIn (le plus utilisé en contexte pro). "
        "Ne pas aller dans le détail de toutes les plateformes ici - ça sera dans le tableau comparatif.",
    )
    return slide
