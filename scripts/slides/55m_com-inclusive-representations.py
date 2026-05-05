"""Slide rs_13 : communication inclusive - les representations comptent."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, Stack,
    add_alert, add_callout, add_highlight, add_notes, new_slide,
    estimate_alert_height, estimate_callout_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Communication inclusive : les représentations comptent",
        fil_ariane="4. Réseaux sociaux | Communication inclusive",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.10, gap=0.12)

    message = (
        "Une image n'est jamais neutre : elle montre qui est attendu, "
        "qui est légitime, qui est concerné."
    )
    add_highlight(slide, message,
                  top=stack.push(estimate_highlight_height(message, CONTENT_W)),
                  left=MARGIN_L, width=CONTENT_W)

    questions_titre = "3 questions avant de choisir un visuel"
    questions_bullets = [
        "Qui est visible dans cette communication ?",
        "Qui est absent ou toujours montré en marge ?",
        "Quelle norme le visuel installe-t-il sans le dire ?",
    ]
    impact_titre = "Pourquoi c'est important"
    impact_bullets = [
        "Les personnes concernées peuvent se sentir attendues",
        "La communication évite de reconduire une seule norme",
        "Le public se projette plus facilement dans le message",
    ]
    col_h = max(
        estimate_callout_height(questions_titre, questions_bullets, COL_W, line_spacing=1.15),
        estimate_alert_height(impact_titre, impact_bullets, COL_W, line_spacing=1.15),
    )
    col_top = stack.push(col_h)
    add_callout(slide, questions_titre, questions_bullets,
                top=col_top, left=MARGIN_L, width=COL_W,
                height=col_h, line_spacing=1.15)
    add_alert(slide, impact_titre, impact_bullets,
              top=col_top, left=COL_R, width=COL_W,
              alert_type="info", line_spacing=1.15)

    add_notes(
        slide,
        "Introduire la communication inclusive par les images, pas par le vocabulaire. "
        "Cela évite de réduire le sujet à l'écriture inclusive. "
        "Expliquer que les photos, illustrations et vidéos transmettent des normes : âge, "
        "genre, handicap, origine, corpulence, situation sociale. "
        "Ne pas culpabiliser les stagiaires : l'objectif est de créer un réflexe de sélection.",
    )
    return slide
