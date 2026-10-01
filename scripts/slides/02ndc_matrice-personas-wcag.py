"""Slide 02ndc : matrice personas x principes WCAG."""

from igpde_dsfr_components import (
    BLEU_INFO, BLEU_INFO_CLAIR, CONTENT_W, MARGIN_L,
    ORANGE_CLAIR, ORANGE_WARN, VERT_CLAIR, VERT_SUCCES,
    add_notes, add_tableau,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="6 profils, 4 questions - votre boussole WCAG",
        fil_ariane="1. Q2 - Pour qui | Synthèse",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    headers = ["Persona", "Percevoir", "Utiliser", "Comprendre", "Compatible"]
    rows = [
        ["Amir (aveugle)", "Alt text, structure", "", "", "Lecteur d'écran"],
        ["Anaïs (malvoyante)", "Contrastes, taille", "", "", ""],
        ["Justine (sourde)", "Sous-titres, transcription", "", "", ""],
        ["Agathe (motrice)", "", "Clavier, cibles 44px", "", ""],
        ["Anatole (cognitif)", "", "", "FALC, phrases courtes", ""],
        ["Paul (TDAH, dyslexie)", "Polices lisibles", "", "Pas de justification", ""],
    ]

    tbl_h = add_tableau(
        slide, headers, rows,
        top=2.30, col_widths=[2.8, 2.6, 2.6, 2.6, 1.68],
    )

    add_notes(
        slide,
        "Slide de synthèse qui fait le lien entre les personas et les "
        "4 principes WCAG. Distribuer la fiche stagiaire "
        "(fiche-stagiaire-principes-wcag.pdf) à ce moment-là. "
        "Dire : « Vous n'avez pas besoin de retenir tout WCAG. Gardez les "
        "4 questions sous la main. À chaque anomalie Word ou web, "
        "demandez-vous : est-ce un problème pour percevoir, utiliser, "
        "comprendre ou être lu par les outils ? »",
    )
    return slide
