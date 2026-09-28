"""Slide 02nac : persona Amir - cécité (aveugle de naissance)."""

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
LABEL_H = 0.40


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Amir, charge d'études - cécité",
        fil_ariane="1. Q2 - Pour qui | Amir",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_image(
        slide,
        "scripts/images/personas-extraites/amir-1.png",
        top=2.20, left=MARGIN_L, width=PHOTO_W, height=PHOTO_W,
        alt_text="Portrait illustratif - Amir",
    )

    titre_besoin = "Ses besoins au quotidien"
    bullets_besoin = [
        "Alternative textuelle sur chaque image (attribut alt)",
        "Structure logique du document (titres, listes, tableaux)",
        "Liens explicites (pas de « cliquez ici »)",
        "Formulaires avec des étiquettes associées aux champs",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Percevoir + Compatible",
        couleur_fond=BLEU_INFO_CLAIR, couleur_accent=BLEU_INFO,
    )

    img_top = 5.05
    item_w = (CONTENT_W - GAP * 2) / 3

    outils = [
        ("scripts/images/personas-extraites/amir-3.png", "Lecteurs d'écran", 1.81),
        ("scripts/images/personas-extraites/amir-2.png", "Plage braille", 0.58),
        ("scripts/images/image9.png", "Synthèse vocale", 1.00),
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
            size=14, bold=True,
        )

    add_notes(
        slide,
        "Amir est aveugle de naissance et utilise un lecteur d'écran "
        "(NVDA ou JAWS) pour tout son travail. Ce profil est central "
        "pour les communicants : chaque image sans alt, chaque tableau "
        "sans structure, chaque lien « cliquez ici » est un mur pour lui. "
        "Faire la demo du lecteur d'écran sur un document mal structure "
        "vs bien structure pour marquer les esprits.",
    )
    return slide
