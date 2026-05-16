"""Slide recap : obligations legales de mise en accessibilite."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_callout, add_notes, add_tableau, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Les obligations legales de mise en accessibilite",
        fil_ariane="1. Q3 - Cadre legal | Recap obligations",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.30)

    add_callout(
        slide,
        "Documents obligatoires",
        [
            "Schema pluriannuel d'accessibilite numerique (SPAN)",
            "Plan d'action annuel",
            "Audit d'accessibilite RGAA en version 4.1.2",
            "Un moyen de contact",
            "RAN (Referent Accessibilite Numerique)",
        ],
        top=stack.push(2.60), height=2.60,
    )

    headers = ["Mention", "Signification"]
    rows = [
        ["Accessibilite : non conforme", "49 % et moins, ou aucun audit en cours de validite"],
        ["Accessibilite : partiellement conforme", "De 50 % a 99 % des criteres respectes"],
        ["Accessibilite : totalement conforme", "100 % des criteres applicables valides"],
    ]
    add_tableau(
        slide, headers, rows,
        top=stack.push(len(rows) * 0.42 + 0.45),
        col_widths=[5.0, 7.28],
    )

    add_notes(
        slide,
        "Rappel : environ 25 % des tests RGAA sont automatisables, "
        "le reste necessite un audit humain.\n"
        "Attention : 100 % conforme ne veut pas forcement dire accessible - "
        "le RGAA ne couvre pas tous les usages.\n"
        "Le RAN est le referent accessibilite numerique, interlocuteur interne "
        "pour piloter la demarche.",
    )
    return slide
