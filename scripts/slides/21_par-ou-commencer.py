"""Slide 46 : Par ou commencer ?

Regles neuropedagogie appliquees :
- R2 : Priorisation par facilite (pas par importance - tout est important)
- R9 : Deconstruction (3 reflexes, pas 50)
- R12 : Ordre d'action clair et immediat
"""

from igpde_dsfr_components import (
    add_highlight, add_stepper, add_notes, new_slide,
    estimate_highlight_height,
    MARGIN_L, CONTENT_W, Stack,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Par où commencer ?",
        fil_ariane="2. Documents accessibles | Priorités",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Priorités",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.30)

    accroche = "Tout est important. Commencez par ce qui prend 30 secondes."
    add_highlight(
        slide, accroche,
        top=stack.push(estimate_highlight_height(accroche, CONTENT_W)),
    )

    add_stepper(
        slide,
        [
            "Styles de titre sur tous les titres",
            "Texte alternatif sur chaque image",
            "Lancer le vérificateur d'accessibilité avant d'envoyer",
        ],
        top=stack.push(2.5),
        height=2.5,
    )

    add_notes(
        slide,
        "Ne pas hiérarchiser les thèmes entre eux : tous sont obligatoires. "
        "La logique ici est l'effort, pas l'importance. Ces 3 réflexes couvrent "
        "Structure, Contenus et Finalisation et prennent moins d'une minute chacun. "
        "Le reste (contraste, langue, propriétés, listes) vient naturellement "
        "une fois que ces 3 réflexes sont installés.",
    )
    return slide
