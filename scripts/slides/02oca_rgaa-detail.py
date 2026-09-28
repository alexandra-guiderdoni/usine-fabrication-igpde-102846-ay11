"""Slide RGAA en 3 colonnes : structure, thématiques visuelles."""

from igpde_dsfr_components import (
    CONTENT_W, GAP, MARGIN_L, Stack,
    add_callout, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="3_colonnes",
        titre="Le RGAA - Référentiel Général d'Amélioration de l'Accessibilité",
        fil_ariane="1. Q3 - Cadre légal | RGAA détail",
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
            "Obligations légales",
            "Méthode technique",
            "",
            "13 thématiques",
            "106 critères au total",
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
            "Multimédia",
            "Tableaux",
            "Liens",
            "Scripts",
        ],
        top=top, left=MARGIN_L + col_w + GAP, width=col_w, height=col_h,
    )

    add_callout(
        slide,
        "Éléments obligatoires",
        [
            "Structuration",
            "Navigation",
            "Présentation",
            "Formulaires",
            "Consultation",
        ],
        top=top, left=MARGIN_L + 2 * (col_w + GAP), width=col_w, height=col_h,
    )

    add_notes(
        slide,
        "Trois taux de conformité :\n"
        "- Non conforme : site non audité ou niveau inférieur à 50 %\n"
        "- Partiellement conforme : de 50 % a 99 %\n"
        "- Totalement conforme : 100 % des critères validés\n"
        "\n"
        "Exemptions :\n"
        "- Fichiers bureautiques publiés avant le 23 septembre 2018\n"
        "- Contenus intranets/extranets publiés avant le 23 septembre 2019\n"
        "- Contenus audios/vidéos publiés avant le 23 septembre 2020\n"
        "- Contenus vidéos, tiers, cartes peuvent aussi être exemptés\n"
        "\n"
        "Exemples de critères :\n"
        "1. Les images porteuses d'informations doivent avoir un texte alternatif. "
        "Les images décoratives ne doivent pas en avoir.\n"
        "2. Les médias avec du son doivent avoir une alternative (sous-titrage, LSF) "
        "et les vidéos une audiodescription.\n"
        "3. Plusieurs systèmes de navigation doivent être disponibles (menu, plan du site, recherche). "
        "Les éléments-clés sont toujours au même endroit.\n"
        "\n"
        "Ref : https://accessibilite.numerique.gouv.fr/\n"
        "Critères : https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/",
    )
    return slide
