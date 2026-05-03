"""Slide rs_10 : émojis - avant/après avec restitution NVDA."""

from igpde_dsfr_components import (
    COL_W, COL_R, CONTENT_W, MARGIN_L,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Ce que ça donne avec trop d'émojis",
        fil_ariane="4. Réseaux sociaux | Émojis",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30

    avant_titre = "Post original"
    avant_bullets = [
        "\U0001f389\U0001f389 Rejoignez-nous \U0001f4c5 mardi 10 juin \U0001f3e2 salle B3 "
        "pour notre atelier \U0001f4bb sur l'accessibilité \U0001f9e0 numérique \U0001f44f\U0001f44f",
    ]
    ah = estimate_callout_height(avant_titre, avant_bullets, COL_W)

    apres_titre = "Ce que NVDA lit"
    apres_bullets = [
        "Visage qui fête quelque chose. Visage qui fête quelque chose. "
        "Rejoignez-nous. Calendrier spirale. mardi 10 juin. Bâtiment de bureau. "
        "salle B3 pour notre atelier. Ordinateur portable. sur l'accessibilité. "
        "Cerveau. numérique. Mains qui applaudissent, peau claire. "
        "Mains qui applaudissent, peau claire.",
    ]
    bh = estimate_alert_height(apres_titre, apres_bullets, COL_W)

    col_h = max(ah, bh)
    add_callout(slide, avant_titre, avant_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h)
    add_alert(slide, apres_titre, apres_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="warning")

    version_ok = (
        "Version accessible : 'Rejoignez-nous mardi 10 juin, salle B3, "
        "pour notre atelier sur l'accessibilité numérique. \U0001f4bb'"
    )
    hl_h = estimate_highlight_height(version_ok, CONTENT_W)
    add_highlight(slide, version_ok,
                  top=round(top + col_h + 0.25, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "Lire la colonne de droite à voix haute, d'une seule traite, "
        "sans intonation. L'effet est immédiat. "
        "Puis lire la version accessible : nette et compréhensible. "
        "Question à poser : 'Combien de temps pour corriger ce post ?' - 30 secondes. "
        "L'information est la même, la lisibilité est incomparablement meilleure.",
    )
    return slide
