"""Slide 02qcb : méthode FALC en 5 étapes + conditions de validation."""

from igpde_dsfr_components import (
    CONTENT_W, COL_W, COL_R, MARGIN_L,
    Stack,
    add_alert, add_callout, add_highlight, add_image, add_notes,
    estimate_alert_height, estimate_callout_height, estimate_highlight_height,
    new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="FALC : la méthode en 5 étapes",
        fil_ariane="1. Q5 - Comment | FALC méthode",
        footer_text=f"{ctx.footer_base} / Module 1",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.05, gap=0.20)

    message = (
        "Il est tres difficile de faire simple ! "
        "Le FALC suit un processus rigoureux."
    )
    add_highlight(
        slide, message,
        top=stack.push(estimate_highlight_height(message, CONTENT_W)),
    )

    titre_etapes = "Les 5 étapes"
    bullets_etapes = [
        "1. Préparatoire : recherches, résumé simplifié, contrôle des contre-sens",
        "2. Transcription en duo : simplification, illustrations, mise en page",
        "3. Validation : relecture par des personnes handicapees intellectuelles",
        "4. Publication : logo FALC, credit des personnes impliquees",
        "5. Iteration : savoir dire stop - un texte ne sera jamais compris a 100 %",
    ]
    titre_conditions = "Conditions obligatoires"
    bullets_conditions = [
        "Validation par des personnes concernées (obligatoire)",
        "80 % des critères FALC respectes (Unapei)",
        "Logo europeen FALC + credit des valideurs",
    ]
    col_h = max(
        estimate_callout_height(titre_etapes, bullets_etapes, COL_W, line_spacing=1.15),
        estimate_alert_height(titre_conditions, bullets_conditions, COL_W, line_spacing=1.15),
    )
    top_cols = stack.push(col_h)
    add_callout(
        slide, titre_etapes, bullets_etapes,
        top=top_cols, left=MARGIN_L, width=COL_W,
        line_spacing=1.15,
    )
    add_alert(
        slide, titre_conditions, bullets_conditions,
        top=top_cols, left=COL_R, width=COL_W,
        alert_type="warning",
        line_spacing=1.15,
    )

    add_image(
        slide,
        "scripts/images/guide-unapei-falc.png",
        top=top_cols + col_h - 0.30, left=COL_R + (COL_W - 1.0) / 2,
        width=1.0,
        alt_text="Couverture du guide Unapei - L'information pour tous",
    )

    add_notes(
        slide,
        "Insister sur le fait que le FALC n'est pas juste 'ecrire simple'. "
        "C'est un processus formalise avec une validation obligatoire par "
        "des personnes concernées. 'Rien pour nous sans nous' est le principe "
        "fondamental. Le logo FALC ne peut pas être appose sans cette "
        "validation. En pratique, contacter des associations comme l'Unapei "
        "ou des ESAT pour trouver des relecteurs. Le guide Unapei "
        "'L'information pour tous' est téléchargeable gratuitement.",
    )
    return slide
