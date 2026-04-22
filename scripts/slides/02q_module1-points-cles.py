"""Slide 02f : synthèse Module 1 - 3 points clés + plan d'action."""

from igpde_dsfr_components import (
    COL_R, COL_W, MARGIN_L, Stack,
    add_alert, add_encadre, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Module 1 - Ce que vous retenez",
        fil_ariane="1. Cadre légal | Synthèse",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.35)

    add_alert(
        slide,
        "3 points à retenir",
        [
            "L'accessibilité est une obligation légale - pas une option",
            "Le RGAA 4.1.2 est votre référentiel de conformité",
            "La déclaration d'accessibilité est publiée sur chaque site",
        ],
        top=stack.push(1.7),
        alert_type="info",
    )

    encadre_h = 1.5
    encadre_top = stack.push(encadre_h)

    add_encadre(
        slide,
        top=encadre_top,
        left=MARGIN_L,
        width=COL_W,
        height=encadre_h,
        titre="Dès demain matin",
        bullets=[
            "Vérifier votre déclaration d'accessibilité",
            "Noter le taux de conformité",
            "Faire réaliser un audit si celui-ci n'existe pas",
        ],
    )

    add_encadre(
        slide,
        top=encadre_top,
        left=COL_R,
        width=COL_W,
        height=encadre_h,
        titre="Cette semaine",
        bullets=[
            "Partager le taux à l'équipe projet et à votre supérieur hiérarchique",
            "Identifier les pages obligatoires de l'échantillon",
        ],
    )

    add_notes(
        slide,
        "Récupération active : demander à 2-3 stagiaires de citer un point retenu. "
        "Annoncer la suite : maintenant on passe à la pratique - Module 2 bureautique.",
    )
    return slide
