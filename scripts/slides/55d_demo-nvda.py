"""Slide rs_04 : démonstration NVDA - lecteur d'écran en direct."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_stepper, add_alert, add_notes, new_slide,
    estimate_alert_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Démonstration NVDA - le lecteur d'écran en direct",
        fil_ariane="4. Réseaux sociaux | Démonstration",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.25)

    etapes = [
        "Ouvrir le post problématique préparé (avec émojis en série)",
        "Activer NVDA : Ctrl+Alt+N - une voix démarre",
        "Naviguer sur le texte : flèches ou Tab",
        "Écouter la restitution - ne pas regarder l'écran",
    ]
    stepper_h = 2.0
    add_stepper(slide, etapes, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    consigne_titre = "Pour les stagiaires pendant la démo"
    consigne_bullets = [
        "Fermez les yeux ou regardez ailleurs - écoutez uniquement",
        "Notez le premier mot qui vous vient à l'écoute",
    ]
    ch = estimate_alert_height(consigne_titre, consigne_bullets, CONTENT_W)
    add_alert(slide, consigne_titre, consigne_bullets,
              top=stack.push(ch), left=MARGIN_L, width=CONTENT_W, alert_type="info")

    add_notes(
        slide,
        "Post à préparer avant la session : un post LinkedIn ou Twitter avec 5-6 émojis en série "
        "et un hashtag sans CamelCase. L'effet est immédiatement compréhensible. "
        "NVDA : Ctrl+Alt+N pour démarrer, Insert+Q pour quitter. "
        "Si NVDA n'est pas disponible, utiliser Narrateur Windows (Win+Ctrl+Entrée). "
        "Durée de la démo : 5 minutes max. Laisser ensuite 5 minutes aux stagiaires pour tester eux-mêmes "
        "sur leur propre PC si le temps le permet.",
    )
    return slide
