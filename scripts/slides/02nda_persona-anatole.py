"""Slide 02nda : persona Anatole - handicap cognitif (trisomie 21)."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, ORANGE_CLAIR, ORANGE_WARN,
    add_callout, add_encadre, add_image, add_notes,
    new_slide,
)

PHOTO_W = 2.2
BIO_LEFT = round(MARGIN_L + PHOTO_W + 0.30, 2)
BIO_W = round(CONTENT_W - PHOTO_W - 0.30, 2)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Anatole, lyceen - handicap cognitif",
        fil_ariane="1. Q2 - Pour qui | Anatole",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_image(
        slide,
        "images-coi/personas-extraites/anatole-1.png",
        top=2.20, left=MARGIN_L, width=PHOTO_W, height=PHOTO_W,
        alt_text="Portrait illustratif - Anatole",
    )

    titre_besoin = "Ses besoins au quotidien"
    bullets_besoin = [
        "Phrases courtes et simples, sans double negation",
        "Mise en page aeree, une idee par paragraphe",
        "Pictogrammes pour accompagner le texte",
        "Navigation previsible, sans changements inattendus",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Comprendre",
        couleur_fond=ORANGE_CLAIR, couleur_accent=ORANGE_WARN,
    )

    add_callout(
        slide,
        "Profil",
        [
            "Porteur de trisomie 21",
            "Lire lui demande du temps et de la concentration",
            "Il comprend mieux les phrases simples et courtes",
            "Le langage clair et le FALC lui sont indispensables",
        ],
        top=5.20, left=MARGIN_L, width=CONTENT_W,
        line_spacing=1.3,
    )

    add_notes(
        slide,
        "Anatole illustre la deficience cognitive. Pour les communicants : "
        "les regles du FALC et du langage clair ne profitent pas qu'aux "
        "personnes handicapees mentales - elles aident aussi les personnes "
        "agees, fatiguees, en situation de stress ou dont le francais "
        "n'est pas la langue maternelle. Faire le lien avec les slides FALC.",
    )
    return slide
