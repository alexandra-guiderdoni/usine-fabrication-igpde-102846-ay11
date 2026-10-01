"""Slide 02r : jalons législatifs RGAA - stepper 4 étapes."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_alert, add_notes, add_stepper, estimate_alert_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Le cadre légal : de 2005 à aujourd'hui",
        fil_ariane="1. Q3 - Cadre légal | Jalons législatifs",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    étapes = [
        "Loi Handicap 2005 : 1re obligation d'accessibilité",
        "Directive européenne 2016 : extension au secteur public",
        "RGAA 4.1.2 (décret 2019-768) : référentiel opposable",
        "2023 : l'Arcom devient l'autorité de contrôle",
    ]

    titre_alert = "Qui est concerné ?"
    bullets_alert = [
        "État, collectivités, établissements publics",
        "Entreprises privées gérant un service public ou CA > 250 M EUR",
        "Jusqu'à 50 000 EUR : accessibilité des organismes publics et assimilés",
        "Jusqu'à 25 000 EUR : obligations déclaratives",
    ]

    stepper_h = 2.0
    stack = Stack(top=2.30, gap=0.20)
    add_stepper(slide, étapes, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    add_alert(
        slide,
        titre_alert,
        bullets_alert,
        top=stack.cursor,
        alert_type="info",
        compact=True,
    )

    add_notes(
        slide,
        "Chronologie en 4 étapes : montrer la progression du droit. "
        "Le RGAA 4.1.2 = 106 critères regroupés en 13 thèmes. "
        "Depuis 2023, l'Arcom est l'autorité de contrôle de l'article 47. "
        "La DINUM édite le RGAA et accompagne les administrations. "
        "La sanction peut atteindre 50 000 EUR pour le non-respect de "
        "l'obligation d'accessibilité par les organismes publics et assimilés, "
        "et 25 000 EUR pour le non-respect des obligations déclaratives.",
    )
    return slide
