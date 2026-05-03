"""Slide rs_15 : plan d'action - 3 gestes concrets + encadré 'dans 7 jours'."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, Stack,
    add_stepper, add_alert, add_highlight, add_notes, new_slide,
    estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Que faites-vous demain matin ?",
        fil_ariane="4. Réseaux sociaux | Plan d'action",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.15)

    gestes = [
        "Avant votre prochain post : activez l'alt text sur votre plateforme principale",
        "Relisez votre dernière publication : comptez les émojis et testez le texte sans eux",
        "Vérifiez vos 3 derniers hashtags : sont-ils en CamelCase ?",
    ]
    stepper_h = 2.0
    add_stepper(slide, gestes, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    sept_jours_titre = "Dans 7 jours"
    sept_jours_bullets = [
        "Publiez un post en appliquant les 4 réflexes",
        "Vérifiez que vos collègues de direction savent où trouver l'alt text",
        "Partagez ce mémo à votre équipe de communication",
    ]
    add_alert(slide, sept_jours_titre, sept_jours_bullets,
              top=stack.push(0), left=MARGIN_L, width=COL_W,
              alert_type="success", line_spacing=1.0)

    rappel_titre = "Mémo : les 4 réflexes"
    rappel_bullets = [
        "Alt text : 1 phrase par image",
        "Émojis : 1-2, en fin de message",
        "Hashtags : CamelCase, 2-3 en fin de post",
        "Texte : pas de faux gras ni italique",
    ]
    add_alert(slide, rappel_titre, rappel_bullets,
              top=stack.cursor, left=COL_R, width=COL_W,
              alert_type="info", line_spacing=1.0)

    add_notes(
        slide,
        "Clôture du module. Laisser 2 minutes aux stagiaires pour noter "
        "leur engagement personnel (1 seul geste concret pour demain). "
        "La restitution orale de ces engagements crée une responsabilisation sociale "
        "(R24 neuropédagogie - plan d'action + pair learning). "
        "Annoncer : un mémo PDF 'Réseaux sociaux accessibles' sera envoyé "
        "par mail après la formation avec les 4 réflexes et le tableau des plateformes. "
        "Remercier les stagiaires pour leur participation et leur attention "
        "sur un sujet qui impacte directement les millions d'usagers de leurs services.",
    )
    return slide
