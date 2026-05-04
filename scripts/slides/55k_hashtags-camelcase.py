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

    top = 1.70

    pourquoi_titre = "Pourquoi le CamelCase ?"
    pourquoi_bullets = [
        "#ServicePublic : le lecteur d'écran lit 'Service Public' - correct",
        "#servicepublic : lu 'servicepublic' - un seul mot sans sens",
        "#SERVICEPUBLIC : lu lettre par lettre S-E-R-V-I-C-E-P-U-B-L-I-C",
        "La majuscule en début de chaque mot = découpage naturel pour le lecteur d'écran",
    ]
    ph = estimate_callout_height(pourquoi_titre, pourquoi_bullets, COL_W)

    regles_titre = "3 règles pour les hashtags"
    regles_bullets = [
        "CamelCase obligatoire : #AccessibilitéNumerique pas #accessibilitenumerique",
        "En fin de post, regroupés - jamais insérés dans la phrase",
        "2 à 3 maximum - au-delà on perd le sens et l'engagement baisse",
    ]
    rh = estimate_alert_height(regles_titre, regles_bullets, COL_W)

    col_h = max(ph, rh)
    add_callout(slide, pourquoi_titre, pourquoi_bullets,
                top=top, left=MARGIN_L, width=COL_W, height=col_h)
    add_alert(slide, regles_titre, regles_bullets,
              top=top, left=COL_R, width=COL_W, alert_type="success")

    anecdote = (
        "#SusanAlbumParty (2012) : sans CamelCase, lu 'Susan album party'. "
        "Avec majuscules, ça aurait été encore plus clair - et moins ... ambigu."
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
        "C'est une des rares règles d'accessibilité qui est aussi devenue "
        "la norme éditoriale standard - bon exemple que l'accessibilité "
        "améliore la communication pour tout le monde.",
    )
    return slide
