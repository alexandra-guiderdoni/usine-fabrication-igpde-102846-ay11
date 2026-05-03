"""Slide quiz final - Questions (5 erreurs a trouver)."""

from igpde_dsfr_components import (
    add_callout, add_highlight, add_notes, new_slide,
    estimate_highlight_height, estimate_callout_height,
    CONTENT_W, MARGIN_L, Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Quiz final : saurez-vous trouver les 5 erreurs ?",
        fil_ariane="2. Documents accessibles | Quiz final",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz final",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.25)

    consigne = (
        "Un collègue vous partage un document Word pour relecture.\n"
        "En l'analysant, vous repérez les éléments suivants."
    )
    add_highlight(
        slide, consigne,
        top=stack.push(estimate_highlight_height(consigne, CONTENT_W)),
    )

    titre_callout = "Identifiez les 5 erreurs d'accessibilité :"
    items = [
        "1. Le titre Introduction est en gras Arial 16 au lieu d'un style de titre",
        "2. Un tableau de suivi utilise uniquement des lignes rouges et vertes",
        "3. Un lien est rédigé : cliquez ici pour le formulaire",
        "4. La langue principale du document n'est pas définie",
        "5. Les propriétés du fichier (Titre et Auteur) sont vides",
    ]
    add_callout(
        slide,
        titre_callout,
        items,
        top=stack.push(estimate_callout_height(titre_callout, items, CONTENT_W)),
    )

    add_notes(
        slide,
        "Lancer le chronomètre : 3 minutes de réflexion individuelle en silence. "
        "Ne pas aider - la difficulté fait partie du processus d'apprentissage. "
        "Au bout des 3 minutes, demander à main levée : « Qui a trouvé "
        "3 erreurs ? 4 erreurs ? Les 5 ? » avant de passer à la correction.",
    )
    return slide
