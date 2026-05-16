"""Slide 02qd : l'accessibilité by design - conclusion visuelle module 1."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    Stack,
    add_highlight, add_image, add_notes, add_callout,
    estimate_highlight_height,
    new_slide,
)

IMG_W = 6.0
TEXTE_LEFT = round(MARGIN_L + IMG_W + 0.35, 2)
TEXTE_W = round(CONTENT_W - IMG_W - 0.35, 2)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="L'accessibilité dès la conception",
        fil_ariane="1. Q5 - Comment | Conception accessible",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "L'accessibilité rend les choses possibles pour certains "
        "et plus simples pour tous."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    img_top = stack.push(2.8)
    add_image(
        slide,
        "images-coi/image19.jpeg",
        top=img_top, left=MARGIN_L, width=IMG_W, height=2.8,
        alt_text=(
            "Escalier avec rampe intégrée dès la conception : "
            "la pente douce est fondue dans les marches, "
            "utilisable par tous sans aménagement postérieur"
        ),
    )

    titre_cle = "Concevoir accessible, pas adapter après"
    bullets_cle = [
        "Intégrer l'accessibilité dès le début, pas en rattrapage",
        "Un document bien structuré profite à tous les lecteurs",
        "La rampe intégrée est plus élégante que la rampe ajoutée",
    ]
    add_callout(
        slide, titre_cle, bullets_cle,
        top=img_top, left=TEXTE_LEFT, width=TEXTE_W,
        line_spacing=1.3,
    )

    add_image(
        slide,
        "images-coi/image21.png",
        top=img_top + 2.8 + 0.15,
        left=MARGIN_L + (CONTENT_W - 3.5) / 2,
        width=3.5,
        alt_text=(
            "Bandeau #accessibleatous : pictogrammes poussette, "
            "personne âgée, femme enceinte, fauteuil roulant"
        ),
    )

    add_notes(
        slide,
        "L'escalier avec rampe intégrée est un exemple emblématique "
        "du design universel. Faire le parallèle avec la communication : "
        "un document structuré dès le départ (titres, alt text, contraste) "
        "est accessible sans effort supplémentaire. Le bandeau "
        "#accessibleatous rappelle que les bénéficiaires dépassent "
        "largement le public handicapé.",
    )
    return slide
