"""Slide 9 : Easy Check 3 - Comment repérer les titres sans outil.

Règles neuropédagogie appliquées :
- R16 : tableau visuel d'outils
- R19 : feedback immédiat par checklist opérationnelle
- R24 : plan d'action - tester sa propre page dès demain
"""

from igpde_dsfr_components import add_notes, add_tableau, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Titres : 3 façons de vérifier",
        fil_ariane="3. Easy Checks | 3. Titres de rubriques",
        footer_text=f"{ctx.footer_base} / Easy Checks - Titres",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Méthode", "Comment faire", "Ce que vous cherchez"]
    rows = [
        [
            "Extension HeadingsMap",
            "Installer l’extension, ouvrir le panneau latéral.",
            "L’arbre complet des titres s’affiche, les anomalies en rouge.",
        ],
        [
            "Mode lecture du navigateur",
            "Firefox : icône livre dans la barre d’URL.",
            "Si la page se simplifie correctement, la hiérarchie est probablement saine.",
        ],
        [
            "Clic droit « Inspecter »",
            "Rechercher `h1`, `h2`, `h3` dans l’onglet Éléments.",
            "Un seul <h1>, pas de saut, pas de titre factice (<div class=\"titre\">).",
        ],
    ]
    add_tableau(
        slide, headers, rows,
        top=2.4,
        col_widths=[2.80, 4.48, 5.00],
        row_h=0.75,
    )

    add_notes(
        slide,
        "Démo HeadingsMap sur legifrance.gouv.fr ou service-public.fr. "
        "Engagement (R24) : chaque stagiaire teste sa page d’accueil personnelle ou professionnelle ce soir "
        "et note le nombre de H1 détectés - idéalement 1, souvent 0 ou 3.",
    )
    return slide
