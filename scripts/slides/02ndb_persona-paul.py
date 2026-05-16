"""Slide 02ndb : persona Paul - TDAH et dyslexie."""

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
        titre="Paul, attache de presse - TDAH et dyslexie",
        fil_ariane="1. Q2 - Pour qui | Paul",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_image(
        slide,
        "images-coi/personas-extraites/paul-1.png",
        top=2.20, left=MARGIN_L, width=PHOTO_W, height=PHOTO_W,
        alt_text="Portrait illustratif - Paul",
    )

    titre_besoin = "Ses besoins au quotidien"
    bullets_besoin = [
        "Mettre en pause les animations (carrousels, video autoplay)",
        "Textes non justifies, avec un espacement suffisant",
        "Polices lisibles, sans empattement (sans serif)",
        "Mise en page aeree, paragraphes courts",
    ]
    add_callout(
        slide, titre_besoin, bullets_besoin,
        top=2.20, left=BIO_LEFT, width=BIO_W,
        line_spacing=1.3,
    )

    add_encadre(
        slide, top=4.42, left=MARGIN_L, width=PHOTO_W, height=0.45,
        titre="Comprendre + Percevoir",
        couleur_fond=ORANGE_CLAIR, couleur_accent=ORANGE_WARN,
    )

    add_callout(
        slide,
        "Profil",
        [
            "Consulte quotidiennement des sites d'info pour ses revues de presse",
            "Trouble de l'attention : les animations non controlables le deconcentrent",
            "Dyslexie : le texte justifie et les polices a empattement ralentissent sa lecture",
        ],
        top=4.80, left=MARGIN_L, width=CONTENT_W,
        line_spacing=1.3,
    )

    add_notes(
        slide,
        "Paul illustre les troubles dys et le TDAH. Pour les communicants : "
        "ne jamais justifier le texte dans un document Word ou PDF, "
        "privilegier les polices sans serif (Marianne, Arial), eviter les "
        "carrousels en lecture automatique sans bouton pause, et garder "
        "des paragraphes courts. Ces regles beneficient a tous les lecteurs.",
    )
    return slide
