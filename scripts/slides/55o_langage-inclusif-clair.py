"""Slide rs_15 : langage inclusif - clarte et accessibilite."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Langage inclusif : clarté d'abord",
        fil_ariane="4. Réseaux sociaux | Communication inclusive",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 1.92

    ok_titre = "À privilégier"
    ok_bullets = [
        "Formules épicènes : 'Nous vous convions', 'les personnes concernées'",
        "Mots collectifs : 'le public', 'l'équipe', 'la clientèle'",
        "Double flexion si nécessaire : 'les utilisateurs et utilisatrices'",
        "Mots-valises si le public les comprend : 'iels', 'amateurices'",
    ]
    oh = estimate_callout_height(ok_titre, ok_bullets, COL_W, line_spacing=1.05)

    eviter_titre = "À éviter ou tester"
    eviter_bullets = [
        "Point médian ou ponctuation répétée quand cela gêne la lecture",
        "Formes trop compressées : elles ralentissent aussi la lecture visuelle",
        "Formes ambiguës à l'oral si le message doit être lu à voix haute",
    ]
    eh = estimate_alert_height(eviter_titre, eviter_bullets, COL_W, line_spacing=1.05)

    col_h = max(oh, eh)
    add_callout(slide, ok_titre, ok_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h,
                line_spacing=1.05)
    add_alert(slide, eviter_titre, eviter_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="warning",
              line_spacing=1.05)

    message = (
        "Recommandation : choisir la forme la plus inclusive qui reste claire, lisible et prononçable."
    )
    hl_h = estimate_highlight_height(message, CONTENT_W)
    add_highlight(slide, message,
                  top=round(top + col_h + 0.10, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "Sujet sensible à traiter avec neutralité : le critère est la compréhension. "
        "Les synthèses vocales et les usages évoluent rapidement ; une forme mal acceptée "
        "aujourd'hui peut devenir plus lisible demain. "
        "En revanche, la charge de lecture reste un vrai sujet pour les personnes dyslexiques "
        "ou fatiguées cognitivement. "
        "Conseil pratique : privilégier d'abord les formules épicènes et les mots collectifs, "
        "puis la double flexion si le contexte exige de nommer explicitement les genres.",
    )
    return slide
