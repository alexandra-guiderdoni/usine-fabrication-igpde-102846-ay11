"""Slide rs_03 : tweet OMS corrigé - avant/après accessible."""

from igpde_dsfr_components import (
    COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="3 changements, 0 perte de sens",
        fil_ariane="4. Réseaux sociaux | Cas pratique",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30

    avant_titre = "Version originale - problématique"
    avant_bullets = [
        "Lavez-vous les \U0001f450 avec 1 désinfectant à base d'alcool, du \U0001f9fc & de l'\U0001f4a6.",
        "Quand vous toussez ou \U0001f927 couvrez votre \U0001f444 & le \U0001f443\U0001f3fb.",
        "Évitez de toucher les \U0001f440, le \U0001f443 & la \U0001f444.",
    ]
    avant_h = estimate_alert_height(avant_titre, avant_bullets, COL_W)

    apres_titre = "Version accessible"
    apres_bullets = [
        "Protégez-vous du #COVID19 - trois gestes essentiels :",
        "1. Lavez-vous régulièrement les mains avec du savon et de l'eau \U0001f9fc",
        "2. Quand vous toussez, couvrez-vous avec le pli du coude",
        "3. Évitez de toucher votre visage",
    ]
    apres_h = estimate_callout_height(apres_titre, apres_bullets, COL_W)

    col_h = max(avant_h, apres_h)

    add_alert(slide, avant_titre, avant_bullets,
              top=top, left=MARGIN_L, width=COL_W, alert_type="error")
    add_callout(slide, apres_titre, apres_bullets,
                top=top, left=COL_R, width=COL_W, height=col_h)

    changements_titre = "Les 3 changements"
    changements_bullets = [
        "Émojis réduits à 1, placé en fin de phrase - le message tient sans eux",
        "Structure numérotée - navigation facile pour tous les utilisateurs",
        "Hashtag conservé mais seul, séparé du texte informatif",
    ]
    add_alert(slide, changements_titre, changements_bullets,
              top=round(top + col_h + 0.25, 2),
              left=MARGIN_L, width=COL_W, alert_type="success")

    add_notes(
        slide,
        "Insister : aucune information perdue. Le message est même plus clair pour tout le monde. "
        "L'accessibilité améliore la qualité pour tous, pas seulement pour les personnes handicapées. "
        "Question à poser : 'Combien de temps faut-il pour faire ces 3 modifications ?' - Réponse : 2 minutes.",
    )
    return slide
