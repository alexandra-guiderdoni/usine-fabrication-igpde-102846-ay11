"""Slide quiz final - Réponses aux 5 erreurs."""

from igpde_dsfr_components import (
    add_callout, add_notes, new_slide,
    CONTENT_W, MARGIN_L,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Réponses au quiz final : trouvez les 5 erreurs",
        fil_ariane="2. Documents accessibles | Quiz final",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz final",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    callout_bullets = [
        "Structure : appliquer le style Titre 1 sur Introduction",
        "Couleurs : ajouter les étiquettes texte Conforme et Non conforme",
        "Contenus : renommer le lien Accéder au formulaire de demande RH",
        "Langue : Révision > Langue > Définir la langue : Français",
        "Finalisation : Fichier > Informations > saisir Titre et Auteur",
    ]
    add_callout(
        slide,
        "5 thèmes, 5 corrections",
        callout_bullets,
        top=2.3,
        left=MARGIN_L,
        width=CONTENT_W,
    )

    add_notes(
        slide,
        "Corriger en groupe, thème par thème. Commenter les erreurs manquées. "
        "Si quelqu'un trouve les 5 : féliciter et demander combien de temps il a mis. "
        "Si moins de 3 : identifier quel thème est moins bien maîtrisé "
        "et orienter vers les slides correspondantes."
    )
    return slide
