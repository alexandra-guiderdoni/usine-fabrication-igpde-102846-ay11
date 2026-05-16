"""Slide 28 : Ouverture du module 2 - Documents bureautiques accessibles.

Règles neuropédagogie appliquées :
- R1 : Transition vers nouveau module par banneau visuel
- R2 : Annonce du plan global pour créer un cadre mental
"""

from igpde_dsfr_components import add_notes, new_slide, compose_chapitre


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="chapitre",
        titre="",
        footer_text=f"{ctx.footer_base} / Documents bureautiques accessibles",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    compose_chapitre(slide, numero="2", titre="Documents bureautiques accessibles",
                     sous_titre="Mise en pratique")

    add_notes(
        slide,
        "Transition vers le module 2. Annoncer : 24 réflexes en 5 thèmes. "
        "Public : communicants, pas développeurs. Chaque slide = 1 réflexe actionnable."
    )
    return slide
