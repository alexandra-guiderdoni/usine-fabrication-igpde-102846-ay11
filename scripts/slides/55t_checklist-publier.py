"""Slide rs_19 : checklist reseaux sociaux - publier."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    add_checklist, add_highlight, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist réseaux sociaux : publier (3/3)",
        fil_ariane="4. Réseaux sociaux | Checklist",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = (
        "Juste avant de cliquer : chaque accès visuel ou sonore doit avoir "
        "une alternative visible."
    )
    add_highlight(slide, accroche, top=2.30, left=MARGIN_L, width=CONTENT_W)

    items = [
        "Alt text clair et unique pour chaque image informative",
        "Infographie ou carrousel : chiffres et messages clés repris dans le post",
        "Audio : transcription écrite jointe ou lien visible",
        "Vidéo : sous-titres relus, transcription si nécessaire",
        "QR code jamais seul : lien visible + « Scannez-moi ! », taille et contraste",
    ]
    add_checklist(
        slide, items,
        top=3.30, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Dernière checklist de l'exercice. "
        "Demander aux binômes de vérifier les alternatives qui manquent vraiment "
        "sur leur publication. "
        "Insister sur la logique d'accès multiple : une information importante ne doit jamais "
        "dépendre d'un seul canal. "
        "Pour les QR codes, rappeler la règle corrigée dans le deck : le QR code aide, "
        "mais le lien visible reste indispensable.",
    )
    return slide
