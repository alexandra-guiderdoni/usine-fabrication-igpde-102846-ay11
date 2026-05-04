"""Slide de cadrage : remplir la grille points de contrôle rapides.

Règles neuropédagogie appliquées :
- R24 : action concrète - transformer le test en remontée exploitable
- R5 : chunking - 5 champs de grille, pas plus
- R18 : sécurité psychologique - qualifier l'impact avant de prioriser
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
        ["Verdict", "C, NC ou NA", "NC"],
        ["Sévérité", "Bloquant, gênant, mineur ou info", "Gênant"],
        ["Constat", "Ce que vous observez concrètement", "Le lien d’évitement n’apparaît pas au focus."],
        ["Correctif", "Ce que l’équipe doit corriger", "Rendre le lien visible et cibler #contenu."],
        ["Preuve", "URL, capture, sélecteur ou extrait", "/actualites - premier appui sur Tab"],
    ]
    add_tableau(
        slide,
        headers,
        rows,
        top=2.15,
        col_widths=[2.05, 4.20, 6.03],
        row_h=0.55,
    )

    add_callout(
        slide,
        "Règle de travail",
        [
            "Un défaut sans preuve est difficile à traiter.",
            "Une preuve sans sévérité est difficile à prioriser.",
        ],
        top=5.45,
        line_spacing=1.0,
    )

    add_notes(
        slide,
        "Faire ouvrir 03-easy-checks/grille-audit-easy-checks.xlsx. "
        "Expliquer que l’objectif n’est pas seulement de dire « ça passe » ou « ça échoue ». "
        "Une remontée utile doit permettre à l’équipe web de comprendre le problème, mesurer l’impact, "
        "retrouver l’endroit exact et corriger sans refaire toute l’enquête. "
        "Insister sur les quatre niveaux de sévérité : bloquant, gênant, mineur, info.",
    )
    return slide
