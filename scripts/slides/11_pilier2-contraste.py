"""Slide 36 : Contraste : un seuil chiffré, pas une opinion.

Règles neuropédagogie appliquées :
- R12 : Mesure objective (ratio 4,5:1, 3:1) élimine la subjectivité
- R7 : Outil gratuit démystifie la tâche
- R18 : Analogue (SMS à 3h du matin) pour contextualisation
"""

from igpde_dsfr_components import (
    add_stepper, add_pave_chiffre, add_qrcode, add_notes, new_slide,
    MARGIN_L, CONTENT_W, GAP
)

KPI_W = 3.25
QR_SIZE = 1.10
QR_LEFT = MARGIN_L + 2 * (KPI_W + GAP)
QR_LABEL_W = MARGIN_L + CONTENT_W - (QR_LEFT + QR_SIZE + 0.14)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Contraste : un seuil chiffré, pas une opinion",
        fil_ariane="2. Documents accessibles | 2. Couleurs",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Couleurs",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_stepper(
        slide,
        [
            "Ouvrir le Colour Contrast Analyser (CCA) de TPGi - gratuit Windows et macOS",
            "Pipette Premier plan sur la couleur du texte",
            "Pipette Arrière-plan sur la couleur du fond",
            "Lire le ratio : conforme si >= 4,5:1 pour le texte normal",
            ">= 3:1 pour le grand texte (18 pt+ ou 14 pt gras)",
        ],
        top=2.3,
        height=2.4
    )

    add_pave_chiffre(
        slide,
        valeur="4,5:1",
        label="Texte normal",
        top=5.05,
        left=MARGIN_L,
        width=KPI_W,
        height=1.5
    )

    add_pave_chiffre(
        slide,
        valeur="3:1",
        label="Grand texte",
        top=5.05,
        left=MARGIN_L + KPI_W + GAP,
        width=KPI_W,
        height=1.5
    )

    add_qrcode(
        slide,
        "_assets/qrcode-vispero-contrast.png",
        url="https://vispero.com/lp/color-contrast-checker/",
        top=5.12,
        left=QR_LEFT,
        size=QR_SIZE,
        label_width=QR_LABEL_W,
    )

    add_notes(
        slide,
        "Le contraste est le critère a11y le plus souvent échoué : 56 % des sites "
        "(WebAIM 2024). Analogie : lire un SMS à 3h du matin sur un écran en plein "
        "soleil. Texte noir sur fond blanc = toujours conforme. Le test ne s'applique "
        "qu'aux textes colorés."
    )
    return slide
