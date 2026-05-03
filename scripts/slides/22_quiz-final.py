"""Slide quiz final - Questions uniquement (5 erreurs a trouver)."""

from igpde_dsfr_components import (
    add_alert, add_highlight, add_notes, new_slide,
    estimate_highlight_height, CONTENT_W, MARGIN_L,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Quiz final : trouvez les 5 erreurs",
        fil_ariane="2. Documents accessibles | Quiz final",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz final",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    consigne = "Un document Word contient les éléments suivants. Identifiez les 5 erreurs d'accessibilité."
    add_highlight(slide, consigne,
                  top=2.3, left=MARGIN_L, width=CONTENT_W)

    alert_bullets = [
        "Un titre Introduction mis en gras Arial 16 (sans style)",
        "Un tableau de résultats avec des lignes en rouge et en vert",
        "Un lien cliquez ici pour le formulaire",
        "La langue du document non définie dans les propriétés Word",
        "Les propriétés du document Titre et Auteur non renseignées",
    ]
    add_alert(
        slide,
        "Le document contient :",
        alert_bullets,
        top=round(2.3 + estimate_highlight_height(consigne, CONTENT_W) + 0.3, 2),
        alert_type="info",
    )

    add_notes(
        slide,
        "Laisser 3 minutes de réflexion individuelle avant de passer à la slide suivante. "
        "Ne pas aider - la difficulté fait partie de l'apprentissage. "
        "Demander à main levée combien trouvent 3 erreurs, 4, les 5."
    )
    return slide
