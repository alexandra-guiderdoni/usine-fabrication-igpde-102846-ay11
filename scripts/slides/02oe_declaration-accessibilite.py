"""Slide 02s : la déclaration d'accessibilité - tableau + exercice."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L, Stack,
    add_alert, add_notes, add_tableau, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="La déclaration d'accessibilité",
        fil_ariane="1. Q3 - Cadre légal | Déclaration",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Que doit-elle contenir ?", "Exemple concret"]
    rows = [
        ["Taux de conformité RGAA", "Ex. : 62 % conforme"],
        ["Statut global", "Partiellement conforme"],
        ["Technologies utilisées", "HTML5, CSS3, JavaScript"],
        ["Environnements de test", "Chrome + NVDA, Safari + VoiceOver"],
        ["Contact et voie de recours", "accessibilite@mon-ministere.gouv.fr"],
    ]

    stack = Stack(top=2.30, gap=0.35)
    add_tableau(
        slide, headers, rows,
        top=stack.push(len(rows) * 0.38 + 0.45),
        left=MARGIN_L, width=CONTENT_W,
        col_widths=[5.5, 6.78],
    )

    add_alert(
        slide,
        "Exercice pratique",
        [
            "Cherchez la déclaration d'accessibilité de votre site",
            "URL type : /déclaration-accessibilité",
            "Notez le taux de conformité affiché",
        ],
        top=stack.cursor,
        alert_type="success",
        compact=True,
    )

    add_notes(
        slide,
        "5 minutes : chaque stagiaire cherche la déclaration de son propre site. "
        "Si introuvable : c'est déjà une non-conformité à signaler. "
        "La voie de recours = Défenseur des droits si absence de réponse en 2 mois.",
    )
    return slide
