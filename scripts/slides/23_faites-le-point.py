"""Slide : Faites le point - Questions a trous."""

from igpde_dsfr_components import (
    Stack, MARGIN_L, CONTENT_W,
    add_highlight, add_texte_libre, add_notes, new_slide,
    estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Faites le point",
        fil_ariane="2. Documents accessibles | Bilan",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Bilan",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.20)

    consigne = "Sans relire le support, complétez de mémoire :"
    add_highlight(
        slide, consigne,
        top=stack.push(estimate_highlight_height(consigne, CONTENT_W)),
    )

    questions = [
        "1.  La règle la plus importante pour qu'un lecteur d'écran "
        "comprenne la structure de votre document : _______________",
        "2.  La vérification à faire en 30 secondes avant d'envoyer "
        "n'importe quel document : _______________",
        "3.  Le geste que vous ferez dès demain sur votre prochain "
        "document : _______________",
    ]

    stack.gap = 0.15
    for q in questions:
        add_texte_libre(
            slide, q,
            top=stack.push(0.70),
            left=MARGIN_L, width=CONTENT_W,
            height=0.65, size=14,
        )

    add_notes(
        slide,
        "Silence total pendant 2 minutes. Ne pas aider. La difficulté "
        "de récupération est ce qui consolide la mémoire à long terme. "
        "Quand tout le monde a écrit, passer à la slide suivante.",
    )
    return slide
