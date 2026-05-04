"""Slide : Checklist autres - Mise en page et formatage."""

from igpde_dsfr_components import (
    add_checklist, add_highlight, add_notes, new_slide,
    MARGIN_L, CONTENT_W,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist : autres critères essentiels (2/2)",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = "Mise en page et formatage propre."
    add_highlight(slide, accroche, top=2.3)

    items = [
        "Pas de zones de texte flottantes",
        "Sauts de page propres (pas de retours à la ligne)",
        "Colonnes intégrées (pas de tabulations)",
        "Tableaux de mise en page avec habillage Aucun",
        "Aucun formulaire Word interactif",
    ]

    add_checklist(
        slide, items,
        top=3.3, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Conseil : intégrer 2-3 nouveaux critères par semaine "
        "jusqu'à ce que les 21 soient automatiques. Suggérer de "
        "plastifier ces 4 slides ou de les garder en favoris.",
    )
    return slide
