"""Slide 02d : jalons législatifs RGAA - stepper 4 étapes."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_alert, add_notes, add_stepper, estimate_alert_height, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Le cadre légal : de 2005 à aujourd'hui",
        fil_ariane="1. Introduction | Cadre légal",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    etapes = [
        "Loi Handicap 2005 : 1re obligation d'accessibilité",
        "Directive européenne 2016 : extension au secteur public",
        "RGAA 4.1.2 (décret 2019-768) : référentiel opposable",
        "Contrôle Arcom effectif - contrôle DINUM en cours de mise en place",
    ]

    titre_alert = "Qui est concerné ?"
    bullets_alert = [
        "État, collectivités, établissements publics",
        "Entreprises privées gérant un service public ou CA > 250 M EUR",
        "Pénalité jusqu'à 25 000 EUR par service non conforme",
    ]

    stepper_h = 2.0
    stack = Stack(top=2.30, gap=0.20)
    add_stepper(slide, etapes, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    add_alert(
        slide,
        titre_alert,
        bullets_alert,
        top=stack.cursor,
        alert_type="info",
    )

    add_notes(
        slide,
        "Chronologie en 4 étapes : montrer la progression du droit. "
        "Le RGAA 4.1.2 = 106 critères regroupés en 13 thèmes. "
        "Préciser : contrôle Arcom = médias audiovisuels (effectif depuis 2023). "
        "Contrôle DINUM = sites publics, dispositif en cours de déploiement.",
    )
    return slide
