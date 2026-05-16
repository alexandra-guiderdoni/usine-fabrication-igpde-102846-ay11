"""Slide 02nc : persona Justine - surdité congénitale profonde."""

from igpde_dsfr_components import (
    BLEU_INFO, BLEU_INFO_CLAIR, CONTENT_W, GAP, MARGIN_L,
    Stack,
    add_callout, add_encadre, add_image, add_notes, add_texte_libre,
    new_slide,
)

PHOTO_W = 2.2
BIO_LEFT = round(MARGIN_L + PHOTO_W + 0.30, 2)
BIO_W = round(CONTENT_W - PHOTO_W - 0.30, 2)

IMG_H = 1.3
LABEL_H = 0.35


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Justine, chargée de communication - surdité",
        fil_ariane="1. Q2 - Pour qui | Justine",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_image(
        slide,
        "images-coi/image7.png",
        top=2.20, left=MARGIN_L, width=PHOTO_W, height=PHOTO_W,
        alt_text="Portrait illustratif - Justine",
    )

    titre_besoin = "Ses besoins au quotidien"
    bullets_besoin = [
        "Sous-titres sur toutes les vidéos et contenus audio",
        "Transcription textuelle des podcasts et webinaires",
        "Alertes visuelles, jamais uniquement sonores",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Percevoir",
        couleur_fond=BLEU_INFO_CLAIR, couleur_accent=BLEU_INFO,
    )

    img_top = 5.05
    item_w = (CONTENT_W - GAP * 2) / 3

    outils = [
        ("images-coi/image9.png", "Transcription", 1.00),
        ("images-coi/image16.png", "Vérificateur accessibilité", 0.47),
        ("images-coi/image12.png", "NVDA - lecteur d'écran", 1.00),
    ]
    for i, (img_path, label, ratio) in enumerate(outils):
        left = MARGIN_L + i * (item_w + GAP)
        img_w = min(item_w - 0.2, IMG_H / ratio)
        img_left = left + (item_w - img_w) / 2
        add_image(
            slide, img_path,
            top=img_top, left=img_left, width=img_w,
            alt_text=label,
        )
        add_texte_libre(
            slide, label,
            top=img_top + IMG_H + 0.05,
            left=left, width=item_w, height=LABEL_H,
            size=12, bold=True,
        )

    add_notes(
        slide,
        "Justine est sourde de naissance. Ce profil illustre la déficience auditive. "
        "Le message clé pour les communicants : tout contenu audio "
        "doit avoir un équivalent textuel. Les sous-titres automatiques "
        "ne suffisent pas toujours, une relecture humaine est nécessaire.",
    )
    return slide
