"""Slide 45 : Exporter Word vers PDF accessible.

Règles neuropedagogie appliquees :
- R12 : Procedure objective en 3 étapes
- R11 : Alerte sur le point de rupture critique
- R19 : Options d'action directement retrouvables dans Word bureau Windows
"""

from igpde_dsfr_components import (
    add_callout,
    add_highlight,
    add_notes,
    add_stepper,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Exporter Word vers PDF sans perdre l'accessibilité",
        fil_ariane="2. Documents accessibles | 5. Finalisation",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Finalisation",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "Un Word accessible peut devenir un PDF inaccessible si l'export est mal fait.",
        top=2.3,
    )

    add_stepper(
        slide,
        [
            "Vérifier l'accessibilité dans Word",
            "Fichier > Enregistrer sous > PDF > Options",
            "Cocher les options d'accessibilité avant d'enregistrer",
        ],
        top=3.35,
        height=1.55,
    )

    add_callout(
        slide,
        "Options à cocher dans Word bureau Windows",
        [
            "Propriétés du document",
            "Balises de structure pour l'accessibilité",
            "Créer des signets à l'aide des titres ou en-têtes",
            "Ne pas convertir le texte en image bitmap",
        ],
        top=5.00,
        line_spacing=1.15,
    )

    add_notes(
        slide,
        "Insister sur la règle d'or : partir d'un Word déjà accessible, puis exporter "
        "avec les balises de structure activées. Le PDF balisé conserve le plan, les "
        "titres, les listes, les tableaux et l'ordre de lecture. Sans balises, le "
        "lecteur d'écran ne distingue plus correctement la structure du document final. "
        "Sur Mac, utiliser Fichier > Enregistrer sous > PDF puis choisir l'option "
        "Idéal pour la distribution électronique et l'accessibilité. Word Online ne "
        "doit pas être présenté comme la voie de référence pour produire le PDF final : "
        "si le PDF est destiné à être diffusé officiellement, préférer Word bureau et "
        "tester le PDF généré avec un vérificateur PDF.",
    )
    return slide
