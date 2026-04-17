"""Slide 27 : mission finale - audit groupé avec les 13 Easy Checks.

Règles neuropédagogie appliquées :
- R24 : plan d'action concret (« Quelle est la 1re chose que vous ferez demain ? »)
- R20 : apprentissage social - binômes pour débriefer
- R25 : métacognition - quel check a été le plus difficile ?
"""

from igpde_dsfr_components import add_callout, add_notes, add_stepper, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Votre mission : audit en 30 minutes",
        fil_ariane="3. Easy Checks | Mission finale",
        footer_text=f"{ctx.footer_base} / Easy Checks - Mission",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_callout(
        slide,
        "Choisissez une page de votre site pro ou d’un site public et passez-la aux 13 Easy Checks :",
        [
            "Notez pour chaque check : passe, échoue, ou doute",
            "Mesurez le contraste d’au moins 3 zones",
            "Testez clavier et zoom 200 % sur un parcours complet",
            "Listez 3 non-conformités à remonter à votre équipe web",
        ],
        top=2.3, height=2.85,
    )

    etapes = [
        "Choisir 1 page",
        "13 checks",
        "Binôme : débrief 5 min",
        "1 action dès demain",
    ]
    add_stepper(
        slide,
        etapes,
        top=5.3, height=1.00,
    )

    add_notes(
        slide,
        "Distribuer la grille d’audit : 03-easy-checks/grille-audit-easy-checks.xlsx. "
        "Onglet Grille vierge à dupliquer par stagiaire, onglet Exemple pour s’orienter, onglet Synthèse pour consolider. "
        "Timing : 20 min audit individuel, 5 min binôme, 5 min restitution collective. "
        "Outils autorisés : DevTools, HeadingsMap, Colour Contrast Analyser, clavier + casque audio. "
        "Clôture métacognitive (R25) : « Quel check vous a surpris ? Quel est le plus facile à faire adopter dans votre équipe ? » "
        "Engagement (R24) : chaque stagiaire annonce UNE action qu’il lancera dès demain 9 h. "
        "Livrable individuel : grille Easy Checks remplie + 3 actions priorisées + 1 engagement personnel.",
    )
    return slide
