"""Slide 31 : Pourquoi ça vous concerne.

Règles neuropédagogie appliquées :
- R13 : Chiffres ancreurs (15 %, 80 %, 0 ligne)
- R4 : Fermeture de la boucle ouverte (réponse au quiz)
- R9 : Déconstruction de la barrière psychologique (0 ligne de code)
"""

from igpde_dsfr_components import (
    add_pave_chiffre, add_callout, add_notes, new_slide,
    estimate_callout_height, MARGIN_L, CONTENT_W, GAP
)

KPI_W = (CONTENT_W - 2 * GAP) / 3


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pourquoi ça vous concerne",
        fil_ariane="2. Documents accessibles",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Pourquoi",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_pave_chiffre(
        slide,
        valeur="15 %",
        label="de vos destinataires sont concernés par un handicap",
        top=2.3,
        left=MARGIN_L,
        width=KPI_W,
        height=1.5
    )

    add_pave_chiffre(
        slide,
        valeur="80 %",
        label="de ces handicaps sont invisibles - rien ne le montre",
        top=2.3,
        left=MARGIN_L + KPI_W + GAP,
        width=KPI_W,
        height=1.5
    )

    add_pave_chiffre(
        slide,
        valeur="0 ligne",
        label="de code nécessaire - uniquement des réflexes dans le ruban Word",
        top=2.3,
        left=MARGIN_L + 2 * (KPI_W + GAP),
        width=KPI_W,
        height=1.5
    )

    callout_bullets = [
        "Le style Titre 1 crée une structure de navigation",
        "Le texte de remplacement décrit la fonction de l'image",
        "Le nom de fichier permet de retrouver le document"
    ]
    callout_height = estimate_callout_height("Réponse au quiz : Document B", callout_bullets)

    add_callout(
        slide,
        "Réponse au quiz : Document B",
        callout_bullets,
        top=4.15
    )

    add_notes(
        slide,
        "Répondre au quiz de la slide précédente. Document B - mais les deux semblent "
        "identiques à l'écran. C'est l'invisible qui fait la différence. 15 % = moyenne "
        "nationale Source : OMS 2024. Le chiffre 0 ligne de code est le déclencheur de "
        "confiance : tout le monde peut le faire."
    )
    return slide
