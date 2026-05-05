"""Slide 6 : Point de contrôle rapide 1 - Exemples OK / KO de texte alternatif.

Règles neuropédagogie appliquées :
- R11 : prédiction avant révélation
- R19 : feedback immédiat OK/KO
- R16 : tableau visuel comparatif
"""

from igpde_dsfr_components import add_notes, add_tableau, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Texte alternatif : passe ou échoue ?",
        fil_ariane="3. points de contrôle rapides | 1. Texte alternatif des images",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Texte alternatif des images",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Image", "Alt proposé", "Verdict"]
    rows = [
        [
            "Logo ministère dans l’en-tête (lien vers l’accueil)",
            "alt=\"Ministère de l’Économie - Accueil\"",
            "OK - fonctionnelle, action nommée",
        ],
        [
            "Photo d’illustration d’un article sur la fraude",
            "alt=\"image\"",
            "KO - aucune information",
        ],
        [
            "Séparateur graphique entre deux sections",
            "alt=\"\"",
            "OK - décorative, alt vide",
        ],
        [
            "Graphique de répartition budgétaire",
            "alt=\"graphique montrant la répartition du budget 2026, voir détail ci-dessous\"",
            "OK - alt court + renvoi au détail",
        ],
        [
            "Icône loupe dans un bouton de recherche",
            "alt=\"loupe\"",
            "KO - décrit l’image, pas l’action (devrait être « Rechercher »)",
        ],
    ]
    add_tableau(
        slide, headers, rows,
        top=2.4,
        col_widths=[4.20, 4.58, 3.50],
        row_h=0.62,
    )

    add_notes(
        slide,
        "Masquer la colonne verdict et demander à voter pour chaque ligne. "
        "Débrief rapide après chaque cas : pourquoi KO ? que rédiger à la place ? "
        "Ligne 5 (loupe) est le piège le plus commun : on décrit ce qu’on voit, "
        "pas ce que l’utilisateur fera en cliquant.",
    )
    return slide
