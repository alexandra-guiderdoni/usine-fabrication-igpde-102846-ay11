"""Slide 50 : Checklist - Vos 21 critères.

Règles neuropédagogie appliquées :
- R17 : Checklist ordonnée par thème et impact
- R2 : Partition en 2 colonnes = cognition distribuée
- R12 : Vérification progressive (5 premiers critères = 80 % impact)
"""

from igpde_dsfr_components import (
    add_checklist, add_notes, new_slide,
    MARGIN_L, CONTENT_W, GAP, COL_W, COL_R
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist : vos 21 critères",
        fil_ariane="2. Documents accessibles | Checklist",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Checklist",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    items_left = [
        "Fichier .docx + nom descriptif",
        "Document non protégé",
        "Titres avec styles intégrés (pas du gras manuel)",
        "Hiérarchie des titres cohérente",
        "Listes avec Puces/Numérotation (pas de tirets manuels)",
        "Colonnes intégrées (pas de tabulations)",
        "Sauts de page propres",
        "Tableaux de mise en page avec habillage Aucun",
        "Tableaux de données avec ligne d'en-tête",
        "Contraste >= 4,5:1 texte standard, >= 3:1 grand texte",
        "Couleur doublée en texte"
    ]

    items_right = [
        "Texte alt sur images significatives / décoratifs marqués",
        "Pas de zones de texte flottantes",
        "Liens descriptifs (pas cliquez ici)",
        "Infos essentielles dans le corps (pas seulement filigrane)",
        "Langue principale balisée",
        "Passages en langue étrangère balisés",
        "Aucun objet clignotant",
        "Propriétés renseignées (Titre, Auteur, Objet)",
        "Aucun formulaire Word interactif",
        "Vérificateur d'accessibilité sans erreur résiduelle"
    ]

    add_checklist(
        slide,
        items_left,
        top=2.3,
        left=MARGIN_L,
        width=COL_W,
        height=None,
        size=14
    )

    add_checklist(
        slide,
        items_right,
        top=2.3,
        left=COL_R,
        width=COL_W,
        height=None,
        size=14
    )

    add_notes(
        slide,
        "Cette checklist est l'outil quotidien. La plastifier ou la garder en favoris. "
        "5 minutes avant d'envoyer un document : parcourir de haut en bas. Ne pas tout "
        "faire d'un coup au début : commencer par les 3 premiers critères de chaque colonne."
    )
    return slide
