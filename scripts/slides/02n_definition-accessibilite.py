"""Slide 02c : définition de l'accessibilité numérique + 3 KPI."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, TOP_CONTENT,
    GAP, Stack,
    add_highlight, add_notes, add_pave_chiffre, estimate_highlight_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pourquoi l'accessibilité numérique ?",
        fil_ariane="1. Introduction | Cadre légal",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    texte_hl = (
        "Un site accessible, c'est un site que tout le monde peut utiliser - "
        "avec ou sans handicap, avec ou sans outil d'assistance."
    )
    stack = Stack(top=TOP_CONTENT, gap=0.40)
    add_highlight(slide, texte_hl, top=stack.push(estimate_highlight_height(texte_hl)))

    kpi_top = stack.cursor
    item_w = (CONTENT_W - GAP * 2) / 3
    kpis = [
        ("12 millions", "de personnes en situation\nde handicap en France"),
        ("80 %", "des sites publics non\nconformes au RGAA"),
        ("2005", "loi Handicap : obligation\nd'accessibilité numérique"),
    ]
    for i, (valeur, label) in enumerate(kpis):
        left = MARGIN_L + i * (item_w + GAP)
        add_pave_chiffre(slide, valeur=valeur, label=label,
                         top=kpi_top, left=left, width=item_w, height=1.5)

    add_notes(
        slide,
        "Poser la question : avez-vous déjà été bloqué par un site mal conçu ? "
        "Les 12 millions incluent les handicaps permanents ET temporaires. "
        "Insister : 80 % de non-conformité, c'est aussi 80 % de risque juridique.",
    )
    return slide
