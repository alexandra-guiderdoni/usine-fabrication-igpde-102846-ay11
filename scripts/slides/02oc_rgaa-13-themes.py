"""Slide 02rb : RGAA 13 thèmes et obligations (Martine 32+33)."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, GAP, MARGIN_L,
    Stack,
    add_alert, add_notes, add_tableau,
    estimate_alert_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="RGAA : 13 thèmes, 3 niveaux de conformité",
        fil_ariane="1. Q3 - Cadre légal | 13 thèmes RGAA",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.00, gap=0.30)

    headers = ["Les 13 thèmes du RGAA", ""]
    rows = [
        ["1. Images", "8. Éléments obligatoires"],
        ["2. Cadres", "9. Structuration"],
        ["3. Couleurs", "10. Présentation"],
        ["4. Multimédia", "11. Formulaires"],
        ["5. Tableaux", "12. Navigation"],
        ["6. Liens", "13. Consultation"],
        ["7. Scripts", ""],
    ]
    tbl_top = stack.cursor
    tbl_h = add_tableau(
        slide, headers, rows,
        top=tbl_top,
        col_widths=[COL_W, COL_W],
        row_h=0.30,
    )
    stack.push(tbl_h)

    titre_oblig = "Obligations de publication"
    bullets_oblig = [
        "Schéma pluriannuel d'accessibilité (SPAN) sur 3 ans",
        "Non conforme : moins de 50 % des critères",
        "Partiellement conforme : de 50 % à 99 %",
        "Totalement conforme : 100 % des critères applicables",
    ]
    add_alert(
        slide, titre_oblig, bullets_oblig,
        top=stack.push(estimate_alert_height(titre_oblig, bullets_oblig, CONTENT_W, line_spacing=1.2)),
        alert_type="warning",
        line_spacing=1.2,
    )

    add_notes(
        slide,
        "Ne pas détailler chaque thème : les participants les retrouveront "
        "dans les modules suivants. Insister sur le SPAN : c'est le document "
        "stratégique que chaque organisme public doit publier. Environ 25 % "
        "des tests RGAA sont automatisables, le reste nécessite un audit humain.",
    )
    return slide
