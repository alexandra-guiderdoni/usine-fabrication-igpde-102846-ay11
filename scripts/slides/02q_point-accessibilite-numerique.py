"""Slide 02q : point sur l'accessibilité numérique + 3 repères."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, TOP_CONTENT,
    GAP, Stack,
    add_highlight, add_notes, add_pave_chiffre, estimate_highlight_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Point sur l'accessibilité numérique",
        fil_ariane="1. Introduction | Cadre légal",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    texte_hl = (
        "L'accessibilité numérique permet d'accéder à l'information "
        "quel que soit le support, l'outil ou la situation."
    )
    stack = Stack(top=TOP_CONTENT, gap=0.40)
    add_highlight(slide, texte_hl, top=stack.push(estimate_highlight_height(texte_hl)))

    kpi_top = stack.cursor
    item_w = (CONTENT_W - GAP * 2) / 3
    kpis = [
        ("WCAG", "référence internationale\ndu W3C."),
        ("RGAA", "référentiel français\npublié par la DINUM."),
        ("106", "critères regroupés\nen 13 thèmes."),
    ]
    for i, (valeur, label) in enumerate(kpis):
        left = MARGIN_L + i * (item_w + GAP)
        add_pave_chiffre(slide, valeur=valeur, label=label,
                         top=kpi_top, left=left, width=item_w, height=1.5)

    add_notes(
        slide,
        "Cette slide fait la transition entre l'approche communication et le cadre de conformité. "
        "Ne pas détailler les 106 critères maintenant : expliquer que la formation donnera des clés utilisables, "
        "puis les points de contrôle rapides permettront de repérer les problèmes les plus fréquents.",
    )
    return slide
