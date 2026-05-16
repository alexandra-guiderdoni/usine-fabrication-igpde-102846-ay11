"""Slide rs_18 : checklist réseaux sociaux - rédiger."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    add_checklist, add_highlight, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist réseaux sociaux : rédiger (2/3)",
        fil_ariane="4. Réseaux sociaux | Checklist",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = (
        "Le post doit rester compréhensible quand on retire l'image, "
        "les effets visuels et les émojis."
    )
    add_highlight(slide, accroche, top=2.30, left=MARGIN_L, width=CONTENT_W)

    items = [
        "Informations essentielles écrites dans le texte du post",
        "Paragraphes courts, texte natif, pas de faux gras Unicode",
        "Émojis : 1 ou 2, en fin de message, sens vérifié",
        "Hashtags : CamelCase, courts, regroupés à la fin, 2 ou 3 maximum",
        "Langage inclusif clair : épicène, double flexion ou mot-valise compris",
    ]
    add_checklist(
        slide, items,
        top=3.30, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Cette slide transforme les règles vues une par une en routine éditoriale. "
        "Demander aux binômes de cocher les cinq points sur le post choisi, puis "
        "de sélectionner un seul problème prioritaire. "
        "Pour le langage inclusif, demander : est-ce que la phrase reste claire "
        "à l'écoute et à la lecture rapide ? "
        "Le test UX est simple : si le sens disparaît quand on retire les effets, "
        "le post dépend trop de sa mise en forme.",
    )
    return slide
