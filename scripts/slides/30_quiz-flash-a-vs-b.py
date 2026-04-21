"""Slide 30 : Quiz flash - Lequel est accessible ?

Règles neuropédagogie appliquées :
- R3 : Préparation mentale par une question ouverte
- R6 : Closure de Zeigarnik (boucle ouverte) pour maintenir l'engagement
- R16 : Pause délibérée avant la réponse pour la récupération active
"""

from igpde_dsfr_components import add_alert, add_highlight, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Quiz flash : lequel est accessible ?",
        fil_ariane="2. Documents accessibles",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Quiz",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    add_alert(
        slide,
        "Document A ou document B ?",
        [
            "A : titres en gras Arial 16, image sans description, nom de fichier Document1.docx",
            "B : titres avec le style Titre 1, image avec texte de remplacement, nom rapport-bilan-2024.docx",
            "Ils sont visuellement identiques."
        ],
        top=2.3,
        alert_type="info"
    )

    add_highlight(
        slide,
        "Réponse après la prochaine section.",
        top=5.5
    )

    add_notes(
        slide,
        "Laisser 30 secondes pour que chacun vote. Demander à main levée. Ne pas donner "
        "la réponse maintenant - la curiosité crée l'attention. Zeigarnik : la boucle "
        "ouverte maintient l'engagement."
    )
    return slide
