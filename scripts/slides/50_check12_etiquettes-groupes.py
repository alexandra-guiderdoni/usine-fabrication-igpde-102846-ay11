"""Slide 25 : Point de contrôle rapide 12 - Groupes de champs (radios, cases à cocher).

Règles neuropédagogie appliquées :
- R8 : analogie - fieldset est le cadre qui rassemble la famille de champs
- R16 : visuel - tableau OK/KO pour ancrer
"""

from igpde_dsfr_components import add_callout, add_notes, add_tableau, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Groupes de champs : l’étiquette commune",
        fil_ariane="3. points de contrôle rapides | 12. Étiquettes de formulaire",
        footer_text=f"{ctx.footer_base} / points de contrôle rapides - Étiquettes de formulaire",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_callout(
        slide,
        "Quand regrouper :",
        [
            "Plusieurs boutons radio qui répondent à la même question (« Civilité : M / Mme / autre »)",
            "Plusieurs cases à cocher qui partagent un thème (« Jours travaillés »)",
            "Adresse découpée en plusieurs champs (n°, rue, code postal, ville)",
        ],
        top=2.4, height=2.00,
    )

    headers = ["Cas", "Code vérifié", "Verdict lecteur d’écran"]
    rows = [
        [
            "3 radios « Civilité » sans regroupement",
            "Chaque radio a son label seul",
            "« M, bouton radio » - question perdue",
        ],
        [
            "3 radios dans un <fieldset> avec <legend>",
            "<fieldset><legend>Civilité</legend>… <input type=\"radio\">…",
            "« Civilité, M, bouton radio » - question claire",
        ],
    ]
    add_tableau(
        slide, headers, rows,
        top=4.35,
        col_widths=[3.20, 4.58, 4.50],
        row_h=0.80,
    )

    add_notes(
        slide,
        "Analogie : sans <fieldset>/<legend>, les radios sont comme des enfants sans nom de famille - "
        "on les entend, on ne sait pas à quelle question ils répondent. "
        "Côté visuel : le fieldset se traduit souvent par une bordure ou un titre de section - "
        "le design peut l’habiller, il ne doit pas le supprimer.",
    )
    return slide
