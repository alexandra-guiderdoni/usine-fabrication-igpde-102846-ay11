"""Slide rs_16 : exercice en binome - checklist reseaux sociaux."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, Stack,
    add_alert, add_highlight, add_notes, add_stepper, new_slide,
    estimate_alert_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Exercice en binôme : passez la checklist",
        fil_ariane="4. Réseaux sociaux | Exercice",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.15, gap=0.12)

    mission = (
        "Choisissez un post réel ou un exemple fourni. Objectif : trouver "
        "2 améliorations utiles : accès, lisibilité ou représentation."
    )
    add_highlight(
        slide, mission,
        top=stack.push(estimate_highlight_height(mission, CONTENT_W)),
        left=MARGIN_L, width=CONTENT_W,
    )

    etapes = [
        "Choisir 1 publication",
        "Cocher Anticiper / Rédiger / Publier",
        "Retenir 2 risques prioritaires",
        "Préparer 1 min de restitution",
    ]
    stepper_h = 1.75
    add_stepper(slide, etapes, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    timing_titre = "Déroulé"
    timing_bullets = [
        "3 min : choisir le post et le contexte",
        "8 min : passer les 3 checklists",
        "4 min : formuler 2 corrections",
    ]
    restitution_titre = "À restituer"
    restitution_bullets = [
        "Le point le plus bloquant",
        "La correction proposée",
        "La règle à garder pour vos prochains posts",
    ]
    col_h = max(
        estimate_alert_height(timing_titre, timing_bullets, COL_W, line_spacing=1.0),
        estimate_alert_height(restitution_titre, restitution_bullets, COL_W, line_spacing=1.0),
    )
    col_top = stack.push(col_h)
    add_alert(slide, timing_titre, timing_bullets,
              top=col_top, left=MARGIN_L, width=COL_W,
              alert_type="info", line_spacing=1.0)
    add_alert(slide, restitution_titre, restitution_bullets,
              top=col_top, left=COL_R, width=COL_W,
              alert_type="success", line_spacing=1.0)

    add_notes(
        slide,
        "Former des binômes. "
        "Si les stagiaires n'ont pas de publication sous la main, proposer un post exemple "
        "préparé par le formateur. "
        "La consigne limite volontairement à 2 améliorations : on cherche la priorisation, "
        "pas l'exhaustivité. "
        "Encourager les binômes à choisir au moins un point lié aux représentations "
        "si le post contient un visuel. "
        "Pendant l'exercice, circuler et donner un feedback immédiat sur les arbitrages. "
        "La restitution orale active l'apprentissage social : chaque binôme enseigne "
        "un point au groupe.",
    )
    return slide
