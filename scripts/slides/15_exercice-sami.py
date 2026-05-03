"""Slide : Exercice - Les erreurs de Sami."""

from pptx.util import Pt
from igpde_dsfr_components import (
    add_card, add_highlight, add_notes, new_slide,
    estimate_card_height, estimate_highlight_height,
    MARGIN_L, CONTENT_W, COL_W, COL_R, Stack,
)


def _bold_keywords(slide, keywords):
    """Met en gras les mots-cles dans tous les text frames de la slide."""
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                for kw in keywords:
                    if kw in run.text:
                        parts = run.text.split(kw, 1)
                        if parts[0] == "" and parts[1] == "":
                            run.font.bold = True
                            continue
                        run.text = parts[0]
                        from pptx.oxml.ns import qn
                        from copy import deepcopy
                        # Inserer un run bold pour le keyword
                        new_r = deepcopy(run._r)
                        new_r.text = kw
                        rPr = new_r.find(qn("a:rPr"))
                        if rPr is None:
                            from lxml import etree
                            rPr = etree.SubElement(new_r, qn("a:rPr"))
                        rPr.set("b", "1")
                        run._r.addnext(new_r)
                        # Inserer un run normal pour le reste
                        if parts[1]:
                            rest_r = deepcopy(run._r)
                            rest_r.text = parts[1]
                            rPr2 = rest_r.find(qn("a:rPr"))
                            if rPr2 is not None:
                                rPr2.attrib.pop("b", None)
                            new_r.addnext(rest_r)
                        break


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_contenu",
        titre="Exercice : les erreurs de Sami",
        fil_ariane="2. Documents accessibles | Exercice",
        footer_text=f"{ctx.footer_base} / Documents accessibles - Exercice",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )

    stack = Stack(top=2.3, gap=0.15)

    card1_titre = "Mise en situation"
    card1_contenu = (
        "Sami, chargé de communication, envoie son rapport trimestriel "
        "à 40 personnes.\n\n"
        "1. Quelles erreurs d'accessibilité trouvez-vous ?\n"
        "2. Quelles corrections proposez-vous ?"
    )

    card2_titre = "Le document contient"
    card2_contenu = (
        "Structure : titres en gras sans styles, "
        "tableau sans en-tête, fausses listes\n\n"
        "Couleurs : mention Urgent en rouge sans autre indication, "
        "note en gris à contraste insuffisant\n\n"
        "Contenus : graphique et organigramme sans alt adapté, "
        "icône redondante, lien cliquez ici"
    )

    card_h = max(
        estimate_card_height(card1_titre, card1_contenu, COL_W),
        estimate_card_height(card2_titre, card2_contenu, COL_W),
    )
    cards_top = stack.push(card_h)

    add_card(slide, card1_titre, card1_contenu, top=cards_top, left=MARGIN_L, width=COL_W, height=card_h)
    add_card(slide, card2_titre, card2_contenu, top=cards_top, left=COL_R, width=COL_W, height=card_h)

    _bold_keywords(slide, ["Structure :", "Couleurs :", "Contenus :"])

    stack.gap = 0.35
    accroche = "30 minutes en binôme : trouvez les erreurs, puis corrigez-les."
    add_highlight(slide, accroche, top=stack.push(estimate_highlight_height(accroche, CONTENT_W)))

    add_notes(
        slide,
        "Distribuer sami-doc-inaccessible.docx aux binômes.\n\n"
        "Phase 1 - Identification (10 min) : « Trouvez toutes les erreurs "
        "d'accessibilité. Notez-les sans corriger. » Pas de checklist.\n\n"
        "Phase 2 - Correction (15 min) : afficher la liste des 12 erreurs. "
        "Les binômes corrigent dans l'ordre structure > couleurs > contenus. "
        "Le vérificateur Word sert d'outil de découverte : « Que détecte-t-il ? "
        "Que rate-t-il ? »\n\n"
        "Phase 3 - Restitution (5 min) : débriefer l'erreur de contraste "
        "(gris #767676, ratio 4,48:1) avec le Colour Contrast Analyser. "
        "Question de transfert : « Sur votre dernier document, laquelle de "
        "ces erreurs avez-vous probablement faite ? » Tour de table rapide.",
    )
    return slide
