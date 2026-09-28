"""Slide 02nd : persona Agathe - déficience motrice."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L, VERT_CLAIR, VERT_SUCCES,
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
        titre="Agathe, chargée de mission - déficience motrice",
        fil_ariane="1. Q2 - Pour qui | Agathe",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_image(
        slide,
        "scripts/images/image11.png",
        top=2.20, left=MARGIN_L, width=PHOTO_W, height=PHOTO_W,
        alt_text="Portrait illustratif - Agathe",
    )

    titre_besoin = "Ses besoins au quotidien"
    bullets_besoin = [
        "Naviguer sans souris, avec des contacteurs adaptés",
        "Cibles cliquables suffisamment larges (44 x 44 px minimum)",
        "Convertisseur texte-parole pour communiquer plus facilement",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Utiliser",
        couleur_fond=VERT_CLAIR, couleur_accent=VERT_SUCCES,
    )

    img_top = 5.05
    item_w = (CONTENT_W - GAP * 2) / 3

    outils = [
        ("scripts/images/image14.jpeg", "Souris trackball", 0.75),
        ("scripts/images/image13.png", "Plage braille / contacteurs", 0.54),
        ("scripts/images/image9.png", "Contrôle vocal", 1.00),
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
        "Agathe utilise un fauteuil roulant et des contacteurs adaptés. "
        "Ce profil illustre la déficience motrice. Pour les communicants : "
        "penser aux zones cliquables suffisamment grandes dans les PDF "
        "et formulaires, et à la navigation au clavier.",
    )
    return slide
