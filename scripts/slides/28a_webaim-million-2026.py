"""Slide d'accroche : WebAIM Million 2026, constat global.

Règles neuropédagogie appliquées :
- R1 : accroche par preuve externe récente
- R2 : primauté - installer le besoin d'une méthode de vérification rapide
- R15 : nuance - rappeler la limite d'un audit automatisé
"""

from igpde_dsfr_components import add_callout, add_notes, add_pave_chiffre, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="WebAIM Million 2026 : le constat",
        fil_ariane="3. points de contrôle rapides | WebAIM Million 2026",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - WebAIM",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    MARGIN = 0.52
    GAP = 0.33
    KPI_W = (12.28 - 2 * GAP) / 3

    add_pave_chiffre(
        slide,
        valeur="95,9 %",
        label="des pages d’accueil ont au moins une erreur WCAG détectée",
        top=2.15,
        left=MARGIN,
        width=KPI_W,
        height=1.35,
    )
    add_pave_chiffre(
        slide,
        valeur="56,1",
        label="erreurs détectées en moyenne par page d’accueil",
        top=2.15,
        left=MARGIN + KPI_W + GAP,
        width=KPI_W,
        height=1.35,
    )
    add_pave_chiffre(
        slide,
        valeur="1 437",
        label="éléments par page en moyenne : la complexité augmente",
        top=2.15,
        left=MARGIN + 2 * (KPI_W + GAP),
        width=KPI_W,
        height=1.35,
    )

    add_callout(
        slide,
        "Comment lire ces chiffres",
        [
            "WebAIM analyse automatiquement les pages d’accueil : c’est un thermomètre, pas un audit RGAA complet.",
            "L’absence d’erreur détectée ne prouve pas qu’une page est accessible.",
            "Mais la présence d’erreurs détectées révèle des barrières très probables pour les utilisateurs.",
        ],
        top=3.90,
        line_spacing=1.0,
    )

    add_notes(
        slide,
        "Source : The WebAIM Million, mise à jour 2026, https://webaim.org/projects/million/. "
        "WebAIM a évalué les pages d’accueil des 1 000 000 de sites web les plus visités avec l’API WAVE autonome "
        "et des outils complémentaires de collecte technique. "
        "Résultats publiés à partir de données de février 2026 et dernière mise à jour indiquée au 30 mars 2026. "
        "Expliquer la limite méthodologique : WAVE détecte des erreurs probables et utiles à repérer, "
        "mais un résultat automatisé ne remplace pas un audit RGAA complet. "
        "Message pédagogique : l’objectif n’est pas de faire peur, mais de rendre visible un problème massif et mesurable. "
        "La slide suivante montre pourquoi les points de contrôle rapides sont un bon premier filtre.",
    )
    return slide
