"""Slide rs_21 : plan d'action - 3 gestes concrets + encadre 'dans 7 jours'."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, Stack,
    add_stepper, add_alert, add_notes, new_slide,
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

    stack = Stack(top=2.20, gap=0.12)

    gestes = [
        "Avant votre prochain post : passez la checklist Anticiper / Rédiger / Publier",
        "Relisez votre dernière publication : qui est représenté, qui est absent ?",
        "Vérifiez un post avec QR code : lien visible + « Scannez-moi ! »",
    ]
    stepper_h = 1.90
    add_stepper(slide, gestes, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    sept_jours_titre = "Dans 7 jours"
    sept_jours_bullets = [
        "Publiez un post en appliquant les 3 temps de la checklist",
        "Faites relire une publication par un binôme avant mise en ligne",
        "Partagez le mémo à votre équipe de communication",
    ]
    add_alert(slide, sept_jours_titre, sept_jours_bullets,
              top=stack.push(0), left=MARGIN_L, width=COL_W,
              alert_type="success", line_spacing=1.15)

    rappel_titre = "Mémo : les 3 temps"
    rappel_bullets = [
        "Anticiper : médias, représentations, contraste",
        "Rédiger : texte natif, émojis, hashtags, langage inclusif",
        "Publier : alt text, sous-titres, transcription, QR code",
    ]
    add_alert(slide, rappel_titre, rappel_bullets,
              top=stack.cursor, left=COL_R, width=COL_W,
              alert_type="info", line_spacing=1.15)

    add_notes(
        slide,
        "Clôture du module. Laisser 2 minutes aux stagiaires pour noter "
        "leur engagement personnel (1 seul geste concret pour demain). "
        "La restitution orale de ces engagements crée une responsabilisation sociale "
        "(R24 neuropédagogie - plan d'action + pair learning). "
        "Annoncer : un mémo PDF 'Réseaux sociaux accessibles' sera envoyé "
        "par mail après la formation avec la checklist, le tableau des plateformes "
        "et les points de vigilance sur la communication inclusive. "
        "Remercier les stagiaires pour leur participation et leur attention "
        "sur un sujet qui impacte directement les millions d'usagers de leurs services.",
    )
    return slide
