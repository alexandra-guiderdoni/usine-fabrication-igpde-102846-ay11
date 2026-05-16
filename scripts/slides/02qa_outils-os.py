"""Slide 02qa : outils d'accessibilité intégrés aux OS et suites bureautiques."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_callout, add_highlight, add_image, add_notes,
    estimate_callout_height, estimate_highlight_height,
    new_slide,
)

LOGO_NVDA_W = 1.0


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Des outils déjà intégrés à vos postes",
        fil_ariane="1. Q5 - Comment | Outils intégrés",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.25)

    message = (
        "Les systèmes d'exploitation et les suites bureautiques "
        "intègrent déjà des fonctions d'accessibilité. "
        "Pas besoin de tout réinventer."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    titre_vision = "Vision"
    bullets_vision = [
        "Loupe et zoom intégrés",
        "Filtres de couleur et mode sombre",
        "Narrateur / NVDA (lecteur d'écran)",
        "Réglage de la taille du texte",
    ]
    titre_audition = "Audition et interaction"
    bullets_audition = [
        "Sous-titres en temps réel",
        "Commandes vocales",
        "Navigation au clavier",
        "Vérification d'accessibilité (Word, PowerPoint)",
    ]

    col_h = max(
        estimate_callout_height(titre_vision, bullets_vision, COL_W, line_spacing=1.2),
        estimate_callout_height(titre_audition, bullets_audition, COL_W, line_spacing=1.2),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_vision, bullets_vision,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.2,
    )
    add_callout(
        slide, titre_audition, bullets_audition,
        top=top_cols, left=COL_R, width=COL_W,
        line_spacing=1.2,
    )

    add_image(
        slide,
        "scripts/images/image12.png",
        top=top_cols + col_h + 0.15,
        left=MARGIN_L + (CONTENT_W - LOGO_NVDA_W) / 2,
        width=LOGO_NVDA_W,
        alt_text="Logo NVDA - lecteur d'écran gratuit et open source",
    )

    add_notes(
        slide,
        "Montrer rapidement où trouver ces réglages : "
        "Windows > Paramètres > Accessibilité / macOS > Préférences Système > Accessibilité. "
        "Word et PowerPoint proposent un vérificateur d'accessibilité intégré "
        "(onglet Révision). On le verra en détail dans le module 2.",
    )
    return slide
