"""Slide 02nf : déficience n'est pas situation de handicap."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    Stack,
    add_highlight, add_image, add_callout, add_notes,
    estimate_highlight_height,
    new_slide,
)

IMG_W = 5.5
TEXTE_LEFT = round(MARGIN_L + IMG_W + 0.35, 2)
TEXTE_W = round(CONTENT_W - IMG_W - 0.35, 2)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Déficience n'est pas situation de handicap",
        fil_ariane="1. Q2 - Pour qui | Déficience vs situation",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "Le handicap n'est pas un état fixe : c'est la rencontre "
        "entre une déficience et un environnement inadapté."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    img_top = stack.push(3.2)
    add_image(
        slide,
        "scripts/images/image4.png",
        top=img_top, left=MARGIN_L, width=IMG_W, height=3.0,
        alt_text=(
            "Schéma montrant 3 situations : une personne en fauteuil "
            "devant un bureau adapté (pas de handicap), en fauteuil seul "
            "(état de déficience), en fauteuil face à un escalier "
            "(situation de handicap)"
        ),
    )

    titre_cle = "Ce que ça change pour vous"
    bullets_cle = [
        "C'est l'environnement qui crée le handicap, pas la personne",
        "Un document inaccessible = une barrière que vous pouvez lever",
        "Accessibiliser votre communication supprime la situation de handicap",
    ]
    add_callout(
        slide, titre_cle, bullets_cle,
        top=img_top, left=TEXTE_LEFT, width=TEXTE_W,
        line_spacing=1.3,
    )

    add_notes(
        slide,
        "Le schéma illustre le modèle social du handicap, opposé au modèle médical. "
        "La personne en fauteuil n'est pas en situation de handicap devant un bureau adapté, "
        "mais le devient face à un escalier. Transposer au numérique : "
        "un PDF non structuré = un escalier pour un lecteur d'écran.",
    )
    return slide
