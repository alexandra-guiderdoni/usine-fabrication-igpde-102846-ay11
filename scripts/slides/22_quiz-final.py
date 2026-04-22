"""Slide 47 : Quiz final - Trouvez les 5 erreurs.

Règles neuropédagogie appliquées :
- R4 : Récupération active (quiz de synthèse)
- R16 : Interleaving (5 erreurs, 1 par pilier)
- R3 : Préparation mentale pour discrimination tous les 5 piliers
"""

from igpde_dsfr_components import (
    add_alert, add_callout, add_notes, new_slide,
    estimate_alert_height, estimate_callout_height,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Quiz final : trouvez les 5 erreurs",
        fil_ariane="2. Documents accessibles | Quiz final",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz final",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    alert_titre = "Un document Word contient :"
    alert_bullets = [
        "Un titre Introduction mis en gras Arial 16 (sans style) [P1]",
        "Un tableau de résultats avec des lignes en rouge et en vert [P2]",
        "Un lien cliquez ici pour le formulaire [P3]",
        "La langue du document non définie dans les propriétés Word [P4]",
        "Les propriétés du document Titre et Auteur non renseignées [P5]",
    ]
    add_alert(
        slide,
        alert_titre,
        alert_bullets,
        top=2.3,
        alert_type="info",
    )

    callout_titre = "5 piliers, 5 corrections"
    callout_bullets = [
        "P1 — Appliquer le style Titre 1",
        "P2 — Ajouter les étiquettes : Conforme et Non conforme dans les cellules",
        "P3 — Renommer le lien : Accéder au formulaire de demande RH",
        "P4 — Révision > Langue > Définir la langue de vérification : Français",
        "P5 — Fichier > Informations > Propriétés : saisir Titre et Auteur",
    ]
    add_callout(
        slide,
        callout_titre,
        callout_bullets,
        top=round(2.3 + estimate_alert_height(alert_titre, alert_bullets) + 0.25, 2),
    )

    add_notes(
        slide,
        "Laisser 3 minutes de réflexion individuelle. Corriger en groupe, commenter "
        "les erreurs manquées. Si quelqu'un trouve les 5 : féliciter et demander combien "
        "de temps il a mis. Si moins de 3 : identifier quel pilier est moins bien maîtrisé "
        "et orienter vers les slides correspondantes."
    )
    return slide
