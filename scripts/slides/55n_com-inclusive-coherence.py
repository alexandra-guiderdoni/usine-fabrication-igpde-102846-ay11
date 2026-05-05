"""Slide rs_14 : communication inclusive - representation et coherence."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_alert, add_callout, add_highlight, add_notes, new_slide,
    estimate_alert_height, estimate_callout_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Représenter sans faire vitrine",
        fil_ariane="4. Réseaux sociaux | Communication inclusive",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.05

    utile_titre = "Représentation utile"
    utile_bullets = [
        "Diversité montrée dans des situations ordinaires",
        "Personnes concernées en rôle actif, pas seulement décoratif",
        "Visuel cohérent avec le public réel de l'action",
    ]
    piege_titre = "Piège à éviter"
    piege_bullets = [
        "Image symbolique sans réalité derrière",
        "Personne réduite à son handicap ou à son identité",
        "Événement annoncé inclusif mais non accessible",
    ]
    col_h = max(
        estimate_callout_height(utile_titre, utile_bullets, COL_W, line_spacing=1.15),
        estimate_alert_height(piege_titre, piege_bullets, COL_W, line_spacing=1.15),
    )
    add_callout(slide, utile_titre, utile_bullets,
                top=top, left=MARGIN_L, width=COL_W,
                height=col_h, line_spacing=1.15)
    add_alert(slide, piege_titre, piege_bullets,
              top=top, left=COL_R, width=COL_W,
              alert_type="warning", line_spacing=1.15)

    rappel = (
        "Règle simple : si vos visuels montrent des personnes handicapées, "
        "vos espaces, événements et pratiques doivent être accessibles."
    )
    add_highlight(slide, rappel,
                  top=round(top + col_h + 0.12, 2),
                  left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "Le point délicat : éviter la représentation opportuniste. "
        "Dire clairement qu'un visuel inclusif ne compense pas une organisation inaccessible. "
        "Exemple : montrer une personne en fauteuil dans la communication d'un événement "
        "alors que le lieu, l'inscription ou les supports ne sont pas accessibles. "
        "Faire le lien avec l'exercice : la checklist doit vérifier aussi la cohérence réelle.",
    )
    return slide
