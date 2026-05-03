"""Slide rs_07 : rédiger un texte alternatif - bon vs mauvais + exercice."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L, Stack,
    add_callout, add_alert, add_highlight, add_notes, new_slide,
    estimate_highlight_height, estimate_alert_height, estimate_callout_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Comment rédiger un bon texte alternatif ?",
        fil_ariane="4. Réseaux sociaux | Alt text",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    top = 2.30

    mauvais_titre = "À éviter"
    mauvais_bullets = [
        '"image.jpg" - nom de fichier, aucun sens',
        '"Photo" - trop vague, aucune information',
        '"Image de la réunion du 12 mars 2026" - date inutile sans contexte',
        '"Voir l\'image ci-dessous" - redondant, ne décrit rien',
    ]
    mh = estimate_alert_height(mauvais_titre, mauvais_bullets, COL_W)

    bon_titre = "Ce qui fonctionne"
    bon_bullets = [
        '"Trois agents discutent autour d\'une table, documents ouverts"',
        '"Logo DINUM - bleu avec texte blanc"',
        '"Graphique : le taux d\'accessibilité passe de 45 à 78 % entre 2023 et 2025"',
        '"Infographie : 4 étapes pour publier un post accessible (texte ci-dessous)"',
    ]
    bh = estimate_callout_height(bon_titre, bon_bullets, COL_W)

    col_h = max(mh, bh)
    add_alert(slide, mauvais_titre, mauvais_bullets,
              top=top, left=MARGIN_L, width=COL_W, alert_type="error")
    add_callout(slide, bon_titre, bon_bullets,
                top=top, left=COL_R, width=COL_W, height=col_h)

    consigne = (
        "Exercice en binôme (7 min) : rédigez l'alt text pour 3 images "
        "que vous avez publiées récemment sur vos réseaux professionnels."
    )
    hl_h = estimate_highlight_height(consigne, CONTENT_W)
    add_highlight(slide, consigne,
                  top=round(top + col_h + 0.25, 2), left=MARGIN_L, width=CONTENT_W)

    add_notes(
        slide,
        "La règle d'or : décrire ce qui est utile pour comprendre le message, "
        "pas ce qui est visible. Une photo de groupe sans texte = "
        '"Équipe de 5 agents en réunion de travail". '
        "Une infographie avec des chiffres = décrire les chiffres clés dans l'alt text "
        "OU dire que le détail est dans le texte du post. "
        "Recueillir 1-2 exemples à l'oral avant de passer à la slide suivante.",
    )
    return slide
