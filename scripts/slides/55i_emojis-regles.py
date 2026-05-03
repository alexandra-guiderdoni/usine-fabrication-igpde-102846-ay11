"""Slide rs_09 : les 3 règles pour les émojis accessibles."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_stepper, add_highlight, add_alert, add_notes, new_slide,
    estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Émojis : 3 règles simples",
        fil_ariane="4. Réseaux sociaux | Émojis",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.30, gap=0.25)

    rappel = "Un lecteur d'écran lit le nom officiel de chaque émoji. En série, c'est incompréhensible."
    hl_h = estimate_highlight_height(rappel, CONTENT_W)
    add_highlight(slide, rappel, top=stack.push(hl_h), left=MARGIN_L, width=CONTENT_W)

    regles = [
        "1 ou 2 émojis par post maximum - au-delà, le sens se perd à l'écoute",
        "En fin de message uniquement - jamais en milieu de phrase",
        "Le texte doit avoir du sens sans eux - testez en retirant l'émoji",
    ]
    stepper_h = 2.5
    add_stepper(slide, regles, top=stack.push(stepper_h),
                left=MARGIN_L, width=CONTENT_W, height=stepper_h)

    test_titre = "Test rapide avant publication"
    test_bullets = [
        "Retirez tous les émojis du texte",
        "Le message est-il toujours clair et complet ? Si oui : bon signe",
        "Si non : l'émoji porte du sens - remplacez-le par le mot correspondant",
    ]
    add_alert(slide, test_titre, test_bullets,
              top=stack.push(0), left=MARGIN_L, width=CONTENT_W, alert_type="info")

    add_notes(
        slide,
        "La règle du test : retirer l'émoji et voir si le message tient. "
        "Exemple : 'Rejoignez-nous mardi prochain !' vs 'Rejoignez-nous mardi prochain !\U0001f4c5' "
        "- le calendrier ne porte pas de sens supplémentaire ici, c'est décoratif. "
        "Mais '\U0001f6a8 Fermeture exceptionnelle' : l'émoji alerte sert vraiment de signal. "
        "Dans ce cas il faut écrire 'ALERTE - Fermeture exceptionnelle' et mettre l'émoji après.",
    )
    return slide
