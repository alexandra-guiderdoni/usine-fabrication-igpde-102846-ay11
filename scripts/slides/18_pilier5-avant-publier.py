"""Slide 43 : Pilier 5 - Avant de publier : 5 vérifications en 2 minutes.

Règles neuropédagogie appliquées :
- R7 : Procédure stepper (5 étapes mécaniques)
- R12 : Seuil objectif (80 % des oublis restants)
- R2 : Checklist finale crée un sentiment de contrôle
"""

from igpde_dsfr_components import add_stepper, add_highlight, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Pilier 5 - Avant de publier : 5 vérifications en 2 minutes",
        fil_ariane="2. Documents accessibles | 5. Finalisation",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Finalisation",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_stepper(
        slide,
        [
            "Propriétés (Titre, Auteur, Objet) : Fichier > Informations > Propriétés",
            "Nom de fichier descriptif en .docx (pas Document1.docx)",
            "Protection : aucune restriction > Révision > Restreindre la modification",
            "Formulaires : aucun champ Word interactif dans le document",
            "Vérificateur d'accessibilité : Fichier > Vérifier l'accessibilité"
        ],
        top=2.3,
        height=2.5
    )

    add_highlight(
        slide,
        "Ces 5 vérifications couvrent 80 % des oublis restants.",
        top=5.05
    )

    add_notes(
        slide,
        "Le pilier 5 est la checklist finale avant envoi. 2 minutes maximum. Le vérificateur "
        "Word est le dernier filet de sécurité - mais il ne détecte pas tout (voir slide "
        "suivante). Insister sur le nom de fichier : c'est le seul identifiant visible "
        "avant d'ouvrir le document."
    )
    return slide
