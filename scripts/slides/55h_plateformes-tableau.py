"""Slide rs_08 : où ajouter l'alt text - tableau des plateformes."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_tableau, add_alert, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Alt text : où le trouver sur chaque plateforme ?",
        fil_ariane="4. Réseaux sociaux | Plateformes",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.15, gap=0.18)

    headers = ["Plateforme", "Accès", "Moment"]
    rows = [
        ["LinkedIn",
         "Modifier la publication > modifier l'image > Ajouter du texte alternatif",
         "À la publication ou après"],
        ["Facebook",
         "Modifier la photo > Texte alternatif",
         "À la publication ou après"],
        ["X (Twitter)",
         "Ajouter une description (icône Accessibilité sous l'image)",
         "Avant publication uniquement"],
        ["Instagram",
         "Paramètres avancés > Accessibilité > Écrire le texte alternatif",
         "Avant publication uniquement"],
        ["Canva",
         "Clic droit sur l'image > Texte alternatif",
         "Pendant la création"],
    ]
    col_widths = [2.2, 7.0, 3.0]
    tbl_h = add_tableau(slide, headers, rows,
                        top=stack.push(0), left=MARGIN_L, width=CONTENT_W,
                        col_widths=col_widths, row_h=0.40)
    stack.push(tbl_h)

    astuce_titre = "Astuce : activez-le par défaut"
    astuce_bullets = [
        "LinkedIn et Instagram proposent un rappel si vous oubliez l'alt text",
        "X : paramètre Accessibilité dans les réglages de compte",
    ]
    add_alert(slide, astuce_titre, astuce_bullets,
              top=stack.push(0), left=MARGIN_L, width=CONTENT_W, alert_type="success")

    add_notes(
        slide,
        "Ne pas lire le tableau ligne par ligne - il sert de mémo à imprimer ou photographier. "
        "Insister : sur X/Twitter il faut le faire AVANT de publier, "
        "on ne peut pas l'ajouter après. "
        "Sur LinkedIn c'est possible après coup, donc pas d'excuse. "
        "La checklist réseaux sociaux de fin de module reprend ces réflexes.",
    )
    return slide
