"""Slide rs_01 : accroche - quiz flash tweet OMS."""

from igpde_dsfr_components import (
    COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height,
)

TWEET = (
    "Protégez-vous de la #COVID19 :\n"
    "Lavez-vous les \U0001f450 avec 1 désinfectant à base d'alcool,"
    " du \U0001f9fc & de l'\U0001f4a6.\n"
    "Quand vous toussez ou \U0001f927 couvrez votre \U0001f444"
    " & le \U0001f443\U0001f3fb dans le pli du coude ou mouchoir.\n"
    "Évitez de toucher les \U0001f440, le \U0001f443 & la \U0001f444."
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Regardez ce tweet - qu'est-ce qui ne va pas ?",
        fil_ariane="4. Réseaux sociaux | Cas pratique",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30
    tweet_titre = "Tweet publié par l'OMS en 2020"
    tweet_bullets = [
        TWEET,
    ]
    tweet_h = estimate_callout_height(tweet_titre, tweet_bullets, COL_W)

    consigne_titre = "En binôme - 2 minutes"
    consigne_bullets = [
        "Identifiez le maximum de problèmes d'accessibilité",
        "Ne lisez pas le tweet à voix haute",
        "Notez ce qui vous gêne ou vous surprend",
    ]
    consigne_h = estimate_alert_height(consigne_titre, consigne_bullets, COL_W)

    col_h = max(tweet_h, consigne_h)

    add_callout(slide, tweet_titre, tweet_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h)
    add_alert(slide, consigne_titre, consigne_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="info")

    add_notes(
        slide,
        "Ne rien dire. Distribuer la consigne, laisser 2 minutes en silence. "
        "Certains stagiaires vont identifier les émojis, d'autres le contraste, d'autres rien. "
        "C'est exactement l'objectif : révéler que le problème n'est pas évident visuellement. "
        "Recueillir les réponses à l'oral avant de passer à la slide suivante.",
    )
    return slide
