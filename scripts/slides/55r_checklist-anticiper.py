"""Slide rs_17 : checklist réseaux sociaux - anticiper."""

from igpde_dsfr_components import (
    CONTENT_W, MARGIN_L,
    add_checklist, add_highlight, add_notes, new_slide,
)


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Checklist réseaux sociaux : anticiper (1/3)",
        fil_ariane="4. Réseaux sociaux | Checklist",
        footer_text=f"{ctx.footer_base} / Réseaux sociaux",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    accroche = (
        "Avant de créer : l'information doit exister en version accessible, "
        "pas seulement dans le visuel."
    )
    add_highlight(slide, accroche, top=2.30, left=MARGIN_L, width=CONTENT_W)

    items = [
        "Média prévu ? image = alt text, audio = transcription, vidéo = sous-titres",
        "Visuels : représentations diverses et cohérentes avec la réalité accessible",
        "Visuel très chargé ? prévoir une version complète en ligne ou dans le post",
        "Police lisible, sans fantaisie, assez épaisse pour un écran mobile",
        "Texte sur image : contraste >= 4,5:1, pas de fond qui gêne la lecture",
    ]
    add_checklist(
        slide, items,
        top=3.30, left=MARGIN_L, width=CONTENT_W,
        height=None, size=14,
    )

    add_notes(
        slide,
        "Cette première checklist est un support d'exercice. "
        "Les binômes cochent uniquement ce qu'ils peuvent vérifier sur leur publication. "
        "Le point représentation doit être traité sans procès d'intention : on évalue "
        "le choix éditorial et sa cohérence avec l'action réelle. "
        "L'objectif est d'éviter le piège classique : tenter de réparer à la publication "
        "un visuel qui porte toute l'information. "
        "Faire le lien avec Word : comme pour un document, on gagne du temps quand "
        "l'accessibilité est pensée avant la mise en forme.",
    )
    return slide
