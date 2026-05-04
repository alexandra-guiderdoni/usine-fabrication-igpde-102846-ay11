"""Slide 10 : Point de contrôle rapide 4 - Contraste, le principe.

Règles neuropédagogie appliquées :
- R8 : analogie - lire à 3 h du matin sur un écran fatigué
- R16 : visuel - pavé chiffré avec les seuils clés
- R9 : émotion - certaines visions rendent les faibles contrastes illisibles
"""

from igpde_dsfr_components import add_callout, add_highlight, add_notes, add_pave_chiffre, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Contraste : un seuil chiffré, pas une opinion",
        fil_ariane="3. points de contrôle rapides | 4. Contraste",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Contraste",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_highlight(
        slide,
        "Ce que vous trouvez « joli gris » peut devenir illisible selon l’écran, la lumière ou la vision de l’utilisateur.",
        top=2.3, height=0.80,
    )

    # 3 KPI : texte normal, texte large, composants
    MARGIN = 0.52
    GAP = 0.33
    KPI_W = (12.28 - 2 * GAP) / 3  # ≈ 4.09

    add_pave_chiffre(
        slide,
        valeur="4,5:1",
        label="Texte normal (sous 18 pt)",
        top=3.4, left=MARGIN, width=KPI_W, height=1.50,
    )
    add_pave_chiffre(
        slide,
        valeur="3:1",
        label="Texte large (18 pt+ ou 14 pt gras) et composants graphiques",
        top=3.4, left=MARGIN + (KPI_W + GAP), width=KPI_W, height=1.50,
    )
    add_pave_chiffre(
        slide,
        valeur="7:1",
        label="Niveau AAA - recommandé pour texte dense",
        top=3.4, left=MARGIN + 2 * (KPI_W + GAP), width=KPI_W, height=1.50,
    )

    add_callout(
        slide,
        "Ce qui compte :",
        [
            "Le rapport entre la couleur du texte et celle du fond (ou l’arrière-plan visible)",
            "Sur un dégradé ou une image, mesurer à l’endroit le moins contrasté",
            "Ne pas se fier seulement à l’œil - mesurer avec un outil",
        ],
        top=5.1, height=1.60,
    )

    add_notes(
        slide,
        "Analogie : lire un SMS à 3 h du matin sur un écran en plein soleil - "
        "c’est ce que vit un malvoyant en permanence avec un contraste trop faible. "
        "Rappeler : le contraste fait partie des défauts les plus fréquents dans les observations WebAIM Million.",
    )
    return slide
