"""Slide récap : obligations légales de mise en accessibilité."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_callout, add_notes, add_tableau, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Les obligations légales de mise en accessibilité",
        fil_ariane="1. Q3 - Cadre légal | Récap obligations",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.30)

    add_callout(
        slide,
        "Documents obligatoires",
        [
            "Schéma pluriannuel d'accessibilité numérique (SPAN)",
            "Plan d'action annuel",
            "Audit d'accessibilité RGAA en version 4.1.2",
            "Un moyen de contact",
            "RAN (Référent Accessibilité Numérique)",
        ],
        top=stack.push(2.40), height=2.60,
        compact=True,
    )

    headers = ["Mention", "Signification"]
    rows = [
        ["Accessibilité : non conforme", "49 % et moins, ou aucun audit en cours de validité"],
        ["Accessibilité : partiellement conforme", "De 50 % à 99 % des critères respectés"],
        ["Accessibilité : totalement conforme", "100 % des critères applicables validés"],
    ]
    add_tableau(
        slide, headers, rows,
        top=stack.push(len(rows) * 0.42 + 0.45),
        col_widths=[5.0, 7.28],
    )

    add_notes(
        slide,
        "Rappel : environ 25 % des tests RGAA sont automatisables, "
        "le reste nécessite un audit humain.\n"
        "Attention : 100 % conforme ne veut pas forcément dire accessible - "
        "le RGAA ne couvre pas tous les usages.\n"
        "Le RAN est le référent accessibilité numérique, interlocuteur interne "
        "pour piloter la démarche.",
    )
    return slide
