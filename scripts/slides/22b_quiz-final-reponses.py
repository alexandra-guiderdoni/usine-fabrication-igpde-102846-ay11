"""Slide quiz final - Correction des 5 erreurs."""

from igpde_dsfr_components import (
    add_callout, add_notes, new_slide,
    estimate_callout_height,
    CONTENT_W, MARGIN_L,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Correction : les 5 erreurs et leurs solutions",
        fil_ariane="2. Documents accessibles | Quiz final",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz final",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    callout_bullets = [
        [
            ("Structure", True),
            (" : le gras n'est pas reconnu par les lecteurs d'écran "
             "- appliquer le style Titre 1", False),
        ],
        [
            ("Couleurs", True),
            (" : l'information ne doit pas reposer sur la couleur seule "
             "- ajouter les étiquettes Conforme / Non conforme", False),
        ],
        [
            ("Contenus", True),
            (" : un lien doit être compréhensible hors contexte "
             "- renommer en Accéder au formulaire de demande RH", False),
        ],
        [
            ("Langue", True),
            (" : sans déclaration, la synthèse vocale prononce avec le mauvais accent "
             "- Révision > Langue > Définir : Français", False),
        ],
        [
            ("Finalisation", True),
            (" : le titre est la première information lue par le lecteur d'écran "
             "- Fichier > Informations > saisir Titre et Auteur", False),
        ],
    ]
    add_callout(
        slide,
        "5 erreurs, 5 solutions",
        callout_bullets,
        top=2.3,
        left=MARGIN_L,
        width=CONTENT_W,
        line_spacing=1.8,
    )

    add_notes(
        slide,
        "Passer en revue chaque point en expliquant l'impact utilisateur "
        "(pourquoi c'est une erreur), puis la correction dans Word. "
        "Si quelqu'un trouve les 5 : féliciter et demander combien de temps. "
        "Si moins de 3 : identifier quel thème est moins maîtrisé "
        "et orienter vers les slides correspondantes.",
    )
    return slide
