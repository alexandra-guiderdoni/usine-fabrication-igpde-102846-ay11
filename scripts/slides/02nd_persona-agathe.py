"""Slide 02nd : persona Agathe - déficience motrice."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L, VERT_CLAIR, VERT_SUCCES,
    add_callout, add_encadre, add_image, add_notes, new_slide,
)

PHOTO_W = 2.2
BIO_LEFT = round(MARGIN_L + PHOTO_W + 0.30, 2)
BIO_W = round(CONTENT_W - PHOTO_W - 0.30, 2)

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
        "Commande vocale pour piloter l'interface",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
        compact=True,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Utiliser",
        couleur_fond=VERT_CLAIR, couleur_accent=VERT_SUCCES,
    )

    outils_top = 5.05
    item_w = (CONTENT_W - GAP * 2) / 3

    outils = [
        "Clavier et contacteurs",
        "Souris trackball",
        "Commande vocale",
    ]
    for i, label in enumerate(outils):
        left = MARGIN_L + i * (item_w + GAP)
        add_encadre(
            slide, top=outils_top, left=left, width=item_w, height=1.35,
            titre=label,
            couleur_fond=VERT_CLAIR, couleur_accent=VERT_SUCCES,
        )

    add_notes(
        slide,
        "Agathe utilise un fauteuil roulant et des contacteurs adaptés. "
        "Ce profil illustre la déficience motrice. Pour les communicants : "
        "penser aux zones cliquables suffisamment grandes dans les PDF "
        "et formulaires, et à la navigation au clavier.",
    )
    return slide
