"""Slide rs_11 : hashtags CamelCase - pourquoi et l'anecdote Susan Boyle."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_callout_height, estimate_alert_height, estimate_highlight_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Hashtags : le CamelCase qui change tout",
        fil_ariane="4. Réseaux sociaux | Hashtags",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.05

    pourquoi_titre = "Pourquoi le CamelCase ?"
    pourquoi_bullets = [
        "#ServicePublic : les mots sont séparés naturellement",
        "#servicepublic : un seul bloc, plus difficile à comprendre",
        "#SERVICEPUBLIC : risque de lecture lettre par lettre",
    ]
    ph = estimate_callout_height(pourquoi_titre, pourquoi_bullets, COL_W, line_spacing=1.15)

    regles_titre = "3 règles avant publication"
    regles_bullets = [
        "Majuscule au début de chaque mot",
        "Hashtags regroupés à la fin du post",
        "2 à 3 maximum, courts et utiles",
    ]
    rh = estimate_alert_height(regles_titre, regles_bullets, COL_W, line_spacing=1.15)

    col_h = max(ph, rh)
    add_callout(slide, pourquoi_titre, pourquoi_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h,
                line_spacing=1.15)
    add_alert(slide, regles_titre, regles_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="success",
              line_spacing=1.15)

    anecdote = (
        "Mini-test : relisez le hashtag à voix haute. Si vous hésitez sur les mots, "
        "raccourcissez-le ou ajoutez les majuscules."
    )
    hl_h = estimate_highlight_height(anecdote, CONTENT_W)
    add_highlight(slide, anecdote,
                  top=round(top + col_h + 0.12, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "L'anecdote Susan Boyle : en 2012 le label de Susan Boyle a lancé le hashtag "
        "#susanalbumparty pour son album. Sans CamelCase, le lecteur d'écran "
        "(et les humains !) lisaient quelque chose de très différent. "
        "Depuis, le CamelCase est la norme sur toutes les plateformes. "
        "Ajouter le critère de longueur : un hashtag trop long devient difficile "
        "à lire, à mémoriser et à comprendre à l'écoute. "
        "C'est une des rares règles d'accessibilité qui est aussi devenue "
        "la norme éditoriale standard - bon exemple que l'accessibilité "
        "améliore la communication pour tout le monde.",
    )
    return slide
