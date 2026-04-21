"""Slide 47 : Quiz final - Trouvez les 5 erreurs.

Règles neuropédagogie appliquées :
- R4 : Récupération active (quiz de synthèse)
- R16 : Interleaving (5 erreurs de piliers différents)
- R3 : Préparation mentale pour discrimination tous les 5 piliers
"""

from igpde_dsfr_components import (
    add_alert, add_callout, add_notes, new_slide,
    estimate_alert_height, estimate_callout_height
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

    alert_bullets = [
        "1. Un titre Introduction mis en gras Arial 16 (sans style)",
        "2. Un tableau de 3 colonnes avec la 1re ligne en gras (sans Ligne d'en-tête)",
        "3. Un lien cliquez ici pour le formulaire",
        "4. Un filigrane PROJET sans mention dans le corps du document",
        "5. Une photo de l'équipe sans texte alternatif"
    ]
    add_alert(
        slide,
        "Un document Word contient :",
        alert_bullets,
        top=2.3,
        alert_type="info"
    )

    callout_bullets = [
        "1. Appliquer le style Titre 1",
        "2. Activer la ligne d'en-tête (onglet Création)",
        "3. Renommer : Accéder au formulaire de demande RH",
        "4. Ajouter PROJET en première ligne du document",
        "5. Texte alt : Équipe du service communication, 8 personnes"
    ]
    add_callout(
        slide,
        "5 erreurs - une par point",
        callout_bullets,
        top=5.4
    )

    add_notes(
        slide,
        "Laisser 3 minutes de réflexion individuelle. Corriger en groupe, commenter "
        "les erreurs manquées. Si quelqu'un trouve les 5 : féliciter et demander combien "
        "de temps il a mis. Si moins de 3 : identifier quel pilier est moins bien maîtrisé "
        "et orienter vers les slides correspondantes."
    )
    return slide
