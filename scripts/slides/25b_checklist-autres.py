"""Slide : Checklist autres - Securite et semantique."""

from igpde_dsfr_components import (
    add_checklist, add_highlight, add_notes, new_slide,
    MARGIN_L, CONTENT_W,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist : autres critères essentiels (1/2)",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = "Tout aussi importants, à intégrer progressivement."
    add_highlight(slide, accroche, top=2.3)

    items = [
        "Aucun objet clignotant",
        "Document non protégé",
        "Langue principale balisée",
        "Fichier .docx + nom descriptif",
        "Vérificateur d'accessibilité sans erreur résiduelle",
        "Infos essentielles dans le corps (pas seulement en filigrane)",
    ]

    add_checklist(
        slide, items,
        top=3.3, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Ces critères n'ont pas été pratiqués dans l'exercice mais sont "
        "tout aussi obligatoires. Les 3 premiers sont des critères bloquants "
        "(sécurité et accès fondamental).",
    )
    return slide
