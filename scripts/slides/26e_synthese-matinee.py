"""Synthèse de la matinée, distincte des 90 minutes du TP."""

from igpde_dsfr_components import (
    COL_R,
    COL_W,
    MARGIN_L,
    add_card,
    add_highlight,
    add_notes,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Synthèse de la matinée - de l'intention à la preuve",
        fil_ariane="Matin | Synthèse",
        footer_text=f"{ctx.footer_base} / Synthèse de la matinée",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_card(
        slide,
        "Ce que nous retenons",
        [
            "L'environnement peut créer ou supprimer une situation de handicap",
            "La structure et le sens comptent autant que l'apparence",
            "Une correction doit produire une preuve vérifiable",
        ],
        top=2.30,
        left=MARGIN_L,
        width=COL_W,
        height=2.65,
    )
    add_card(
        slide,
        "Questions et transition",
        [
            "Quel réflexe allez-vous réutiliser dans votre prochain document ?",
            "Quel point demande encore une clarification ?",
            "Après les documents, nous appliquerons la même démarche au Web",
        ],
        top=2.30,
        left=COL_R,
        width=COL_W,
        height=2.65,
    )
    add_highlight(
        slide,
        "Structurer, rendre compréhensible, vérifier avec les outils, puis contrôler humainement.",
        top=5.35,
    )

    add_notes(
        slide,
        "Cette synthèse dure 15 minutes, de 12 h à 12 h 15, hors des 90 minutes du TP. "
        "Recueillir les questions, faire formuler un acquis transférable et annoncer la "
        "partie III consacrée aux points de contrôle rapides sur le Web.",
    )
    return slide
