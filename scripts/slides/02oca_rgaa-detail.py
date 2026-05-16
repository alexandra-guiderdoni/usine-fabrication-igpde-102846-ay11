"""Slide RGAA en 3 colonnes : structure, thematiques visuelles."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L, Stack,
    add_callout, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="3_colonnes",
        titre="Le RGAA - Referentiel General d'Amelioration de l'Accessibilite",
        fil_ariane="1. Q3 - Cadre legal | RGAA detail",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    col_w = (CONTENT_W - GAP * 2) / 3
    top = 2.30
    col_h = 4.30

    add_callout(
        slide,
        "Structure en 2 parties",
        [
            "Obligations legales",
            "Methode technique",
            "",
            "13 thematiques",
            "106 criteres au total",
            "258 tests unitaires",
        ],
        top=top, left=MARGIN_L, width=col_w, height=col_h,
    )

    add_callout(
        slide,
        "Images",
        [
            "Cadres",
            "Couleurs",
            "Multimedia",
            "Tableaux",
            "Liens",
            "Scripts",
        ],
        top=top, left=MARGIN_L + col_w + GAP, width=col_w, height=col_h,
    )

    add_callout(
        slide,
        "Elements obligatoires",
        [
            "Structuration",
            "Navigation",
            "Presentation",
            "Formulaires",
            "Consultation",
        ],
        top=top, left=MARGIN_L + 2 * (col_w + GAP), width=col_w, height=col_h,
    )

    add_notes(
        slide,
        "Trois taux de conformite :\n"
        "- Non conforme : site non audite ou niveau inferieur a 50 %\n"
        "- Partiellement conforme : de 50 % a 99 %\n"
        "- Totalement conforme : 100 % des criteres valides\n"
        "\n"
        "Exemptions :\n"
        "- Fichiers bureautiques publies avant le 23 septembre 2018\n"
        "- Contenus intranets/extranets publies avant le 23 septembre 2019\n"
        "- Contenus audios/videos publies avant le 23 septembre 2020\n"
        "- Contenus videos, tiers, cartes peuvent aussi etre exemptes\n"
        "\n"
        "Exemples de criteres :\n"
        "1. Les images porteuses d'informations doivent avoir un texte alternatif. "
        "Les images decoratives ne doivent pas en avoir.\n"
        "2. Les medias avec du son doivent avoir une alternative (sous-titrage, LSF) "
        "et les videos une audiodescription.\n"
        "3. Plusieurs systemes de navigation doivent etre disponibles (menu, plan du site, recherche). "
        "Les elements-cles sont toujours au meme endroit.\n"
        "\n"
        "Ref : https://accessibilite.numerique.gouv.fr/\n"
        "Criteres : https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/",
    )
    return slide
