"""Slide de cadrage : remplir la grille points de contrôle rapides.

Règles neuropédagogie appliquées :
- R24 : action concrète - transformer le test en remontée exploitable
- R5 : chunking - 3 champs de diagnostic, pas plus
- R18 : sécurité psychologique - décrire un écart sans notation
"""

from igpde_dsfr_components import add_callout, add_notes, add_tableau, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs,
        layouts,
        layout_name="titre_contenu",
        titre="Ce qu’on remonte dans la grille",
        fil_ariane="3. points de contrôle rapides | Grille d’audit",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Grille",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Champ", "Ce qu’il faut écrire", "Exemple court"]
    rows = [
        ["Constat", "Ce que vous observez concrètement", "Le lien d’évitement n’apparaît pas au focus."],
        ["Mise en conformité à réaliser", "Ce que l’équipe doit corriger", "Rendre le lien visible et cibler #contenu."],
        ["Preuve de l’écart", "URL, capture, sélecteur ou extrait", "/actualites - premier appui sur Tab"],
    ]
    add_tableau(
        slide,
        headers,
        rows,
        top=2.15,
        col_widths=[2.05, 4.20, 6.03],
        row_h=0.70,
    )

    add_callout(
        slide,
        "Règle de travail",
        [
            "Un défaut sans preuve est difficile à traiter.",
            "L’objectif est de documenter l’écart et de proposer sa correction, pas de calculer un taux.",
        ],
        top=4.95,
        line_spacing=1.15,
    )

    add_notes(
        slide,
        "Faire ouvrir la grille d’audit grille-audit-easy-checks.xlsx, téléchargeable depuis la page d’accueil du site d’exercice. "
        "Expliquer que l’objectif est de documenter un problème et sa correction, pas de produire un verdict ni un taux. "
        "Une remontée utile doit permettre à l’équipe web de comprendre le problème, "
        "retrouver l’endroit exact et corriger sans refaire toute l’enquête. "
        "Faire renseigner les trois champs : constat, mise en conformité à réaliser et preuve de l’écart.",
    )
    return slide
