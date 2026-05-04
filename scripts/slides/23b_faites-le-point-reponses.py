"""Slide : Faites le point - Reponses."""

from igpde_dsfr_components import (
    Stack, MARGIN_L, CONTENT_W,
    add_callout, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Faites le point : les réponses",
        fil_ariane="2. Documents accessibles | Bilan",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Bilan",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.25)

    bullets = [
        "1. Utiliser les styles de titre (Titre 1, Titre 2) "
        "pour structurer le document",
        "2. Lancer le vérificateur d'accessibilité "
        "(Révision > Vérifier l'accessibilité)",
        "3. Ajouter un texte alternatif aux images "
        "ou renseigner le titre dans les propriétés",
    ]
    add_callout(
        slide,
        "Les réponses",
        bullets,
        top=stack.push(estimate_callout_height("Les réponses", bullets,
                                               CONTENT_W)),
        bullet_prefix="",
    )

    bilan = (
        "Vous avez ces réflexes ? L'essentiel est acquis.\n"
        "Sinon : relisez Structure et Contenus."
    )
    add_highlight(
        slide, bilan,
        top=stack.push(estimate_highlight_height(bilan, CONTENT_W)),
    )

    add_notes(
        slide,
        "Comparer avec ce que les stagiaires ont écrit. L'écart entre "
        "ce qu'on croit savoir et ce qu'on sait vraiment est instructif. "
        "Insister sur le raccourci Ctrl+F onglet Titres : c'est l'astuce "
        "visuelle la plus pratique pour prouver qu'un document est bien "
        "ou mal structuré. Terminer sur une note positive.",
    )
    return slide
