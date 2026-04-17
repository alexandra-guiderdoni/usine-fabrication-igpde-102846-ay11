"""Génère gabarits-ppt-igpde.pptx : 1 slide par layout + composants DSFR.

Ce fichier sert de démonstration pédagogique pour l'intervenant : chaque gabarit
IGPDE-DSFR (couverture, titre-sous-titre, sommaire, chapitre, 3 colonnes,
titre-contenu) est illustré avec les composants DSFR disponibles.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from igpde_dsfr_components import (
    create_presentation, new_slide, finalize_pptx,
    add_callout, add_alert, add_highlight, add_quote, add_card,
    add_pave_chiffre, add_stepper, add_tableau, add_fleche,
    add_texte_libre, add_encadre, add_notes,
    add_checklist, add_avant_apres, add_exemple_contre_exemple,
    compose_sommaire, compose_chapitre,
    MARGIN_L, CONTENT_W, GAP, COL_W, COL_R, TOP_CONTENT, TOP_CARDS,
    BLEU_FRANCE, ROUGE_MARIANNE, GRIS_CLAIR, BLEU_CLAIR,
)
from pptx.enum.text import PP_ALIGN

OUTPUT = Path(__file__).parent.parent / "gabarits-ppt-igpde.pptx"


def main():
    prs, layouts = create_presentation()

    DATE = "4 juin 2026"

    # --- SLIDE 1 : Couverture ---
    s1 = new_slide(prs, layouts, layout_name="couverture",
                   titre="Accessibilité numérique",
                   footer_text="Institut de la Gestion publique et du Développement économique",
                   date_text=DATE, page_num=1)
    # Sous-titre aligné à droite, sous le titre, au-dessus du pied de page (y=5.72)
    from pptx.enum.text import PP_ALIGN
    from pptx.util import Inches
    sub_box = s1.shapes.add_textbox(
        Inches(5.8), Inches(5.3), Inches(7.1), Inches(0.35),
    )
    sub_box.name = "DSFR-couverture-soustitre"
    from igpde_dsfr_components import _apply_text, FONT
    _apply_text(sub_box.text_frame, "Formation 102638 | Bureautique et web",
                font=FONT, size=14, bold=True, color=ROUGE_MARIANNE,
                align=PP_ALIGN.RIGHT)
    add_notes(s1, "Slide de couverture - accueil des stagiaires, tour de table.")

    # --- SLIDE 2 : Titre et sous-titre ---
    s2 = new_slide(prs, layouts, layout_name="titre_soustitre",
                   titre="Objectifs pédagogiques",
                   footer_text="Formation 102638 / Objectifs",
                   date_text=DATE, page_num=2)
    add_callout(
        s2, "À l\u2019issue de cette formation, les stagiaires sauront :",
        ["Identifier les critères RGAA 4.1.2 applicables",
         "Produire un document bureautique accessible",
         "Auditer une page web avec les outils standards",
         "Remédier aux non-conformités détectées"],
        top=3.8, height=2.5,
    )
    add_notes(s2,
              "Présenter les 4 objectifs, insister sur le caractère opérationnel.")

    # --- SLIDE 3 : Sommaire DSFR ---
    s3 = new_slide(prs, layouts, layout_name="sommaire", titre="Sommaire",
                   footer_text="Formation 102638 / Sommaire",
                   date_text=DATE, page_num=3)
    compose_sommaire(s3, "Sommaire", [
        ("Cadre légal",
         "RGAA 4.1.2, décret 2019, obligations des administrations"),
        ("Bureautique",
         "Word, Excel, PowerPoint accessibles : structure, styles, alt text"),
        ("Web et réseaux",
         "Easy Checks, tests clavier, réseaux sociaux accessibles"),
    ])
    add_notes(s3,
              "Présenter l\u2019enchaînement des 3 parties sur 2 journées.")

    # --- SLIDE 4 : Chapitre DSFR ---
    s4 = new_slide(prs, layouts, layout_name="chapitre", titre="",
                   footer_text="Formation 102638 / Partie 1",
                   date_text=DATE, page_num=4)
    compose_chapitre(
        s4, numero=1,
        titre="Comprendre l\u2019accessibilité numérique et son cadre légal",
    )
    add_notes(s4, "Transition vers la partie 1, 15 min.")

    # --- SLIDE 5 : 3 colonnes (cards) ---
    s5 = new_slide(prs, layouts, layout_name="3_colonnes",
                   titre="Les trois piliers de l\u2019accessibilité",
                   fil_ariane="1. Cadre légal | Introduction",
                   footer_text="Formation 102638 / Cadre légal",
                   date_text=DATE, page_num=5)
    card_w = (CONTENT_W - GAP * 2) / 3
    for i, (t, c) in enumerate([
        ("Perceptible",
         ["Alternatives textuelles",
          "Contrastes suffisants",
          "Sous-titres"]),
        ("Utilisable",
         ["Navigation au clavier",
          "Temps suffisant",
          "Pas de clignotement"]),
        ("Compréhensible",
         ["Langue identifiée",
          "Texte lisible",
          "Prévisibilité"]),
    ]):
        add_card(s5, t, c, top=TOP_CARDS, left=MARGIN_L + i * (card_w + GAP),
                 width=card_w, height=3.5, numero=i + 1)
    add_notes(s5,
              "R1 : comprendre les 4 principes WCAG. R2 : ancrage pédagogique.")

    # --- SLIDE 6 : Titre et contenu - KPI + alert ---
    s6 = new_slide(prs, layouts, layout_name="titre_contenu",
                   titre="État de l\u2019accessibilité dans les administrations",
                   fil_ariane="1. Cadre légal | Chiffres clés",
                   footer_text="Formation 102638 / Cadre légal",
                   date_text=DATE, page_num=6)
    kpi_w = (CONTENT_W - GAP * 2) / 3
    for i, (val, label) in enumerate([
        ("43 %", "Taux moyen RGAA (2025)"),
        ("96 %", "Meilleur taux (DGFiP)"),
        ("11", "Non-conformités moyennes"),
    ]):
        add_pave_chiffre(s6, val, label, top=TOP_CONTENT,
                         left=MARGIN_L + i * (kpi_w + GAP),
                         width=kpi_w, height=1.5)
    add_alert(
        s6, "À retenir",
        ["L\u2019audit doit être réalisé par un tiers qualifié",
         "La déclaration d\u2019accessibilité est obligatoire",
         "Un plan pluriannuel doit être publié"],
        top=TOP_CONTENT + 1.8, height=1.8, alert_type="info",
    )
    add_notes(s6,
              "Source : Observatoire DINUM 2025. "
              "Insister sur l\u2019écart entre directions.")

    # --- SLIDE 7 : Stepper ---
    s7 = new_slide(prs, layouts, layout_name="titre_contenu",
                   titre="Démarche d\u2019audit en 4 étapes",
                   fil_ariane="2. Bureautique | Méthodologie",
                   footer_text="Formation 102638 / Bureautique",
                   date_text=DATE, page_num=7)
    add_stepper(s7, [
        "Inventaire des pages et documents",
        "Tests automatisés (axe-core, Wave)",
        "Tests manuels (clavier, lecteur d\u2019écran)",
        "Rédaction du rapport et plan d\u2019action",
    ], top=TOP_CONTENT, height=2.8)
    add_highlight(
        s7,
        "La durée moyenne d\u2019un audit complet est de 10 à 15 jours ouvrés",
        top=TOP_CONTENT + 3.0, height=0.9,
    )
    add_notes(s7,
              "R7 : chaque étape est séquentielle. "
              "R12 : éviter de sauter des étapes.")

    # --- SLIDE 8 : Tableau + quote ---
    s8 = new_slide(prs, layouts, layout_name="titre_contenu",
                   titre="Outils d\u2019audit recommandés",
                   fil_ariane="3. Web | Outils",
                   footer_text="Formation 102638 / Web",
                   date_text=DATE, page_num=8)
    tbl_h = add_tableau(
        s8,
        headers=["Outil", "Usage", "Coût"],
        rows=[
            ["axe-core", "Tests automatisés navigateur", "Gratuit"],
            ["WAVE", "Audit visuel WCAG", "Gratuit"],
            ["Lighthouse", "Audit performance et accessibilité", "Gratuit"],
            ["NVDA", "Lecteur d\u2019écran Windows", "Gratuit"],
            ["VoiceOver", "Lecteur d\u2019écran macOS/iOS", "Intégré OS"],
        ],
        top=TOP_CONTENT,
    )
    add_quote(
        s8,
        "L\u2019accessibilité n\u2019est pas un coût, "
        "c\u2019est un investissement dans la qualité du service public.",
        auteur="Circulaire DINUM 2024",
        top=TOP_CONTENT + tbl_h + 0.3, height=1.3,
    )
    add_notes(s8,
              "R14 : outils gratuits et accessibles à tous. "
              "Pas de barrière budgétaire.")

    # --- SLIDE 9 : 2 colonnes (callout + alert) ---
    s9 = new_slide(prs, layouts, layout_name="titre_contenu",
                   titre="Bonnes pratiques et pièges",
                   fil_ariane="3. Web | Récapitulatif",
                   footer_text="Formation 102638 / Récapitulatif",
                   date_text=DATE, page_num=9)
    add_callout(s9, "Bonnes pratiques",
                ["Structurer le document avec des styles",
                 "Ajouter un alt text à chaque image",
                 "Vérifier le contraste (\u2265 4.5:1)",
                 "Tester au clavier avant livraison"],
                top=TOP_CONTENT, left=MARGIN_L, width=COL_W, height=3.5)
    add_alert(s9, "Pièges à éviter",
              ["Pas de tableau pour la mise en page",
               "Pas de capture d\u2019écran de texte",
               "Pas de justification (alignement gauche)",
               "Pas d\u2019acronyme sans explicitation"],
              top=TOP_CONTENT, left=COL_R, width=COL_W, height=3.5,
              alert_type="warning")
    add_notes(s9,
              "R21 : comparer pratiques et pièges en miroir. "
              "R25 : ancrage par opposition.")

    # --- SLIDE 10 : Section 2 ---
    s10 = new_slide(prs, layouts, layout_name="chapitre", titre="",
                    footer_text="Formation 102638 / Partie 2",
                    date_text=DATE, page_num=10)
    compose_chapitre(s10, numero=2,
                     titre="Créer des documents bureautiques accessibles")
    add_notes(s10, "Transition vers la partie 2, bureautique accessible.")

    # --- SLIDE 11 : Section 3 ---
    s11 = new_slide(prs, layouts, layout_name="chapitre", titre="",
                    footer_text="Formation 102638 / Partie 3",
                    date_text=DATE, page_num=11)
    compose_chapitre(
        s11, numero=3,
        titre="Pratiquer les évaluations rapides d\u2019accessibilité web "
              "(Easy Checks)",
    )
    add_notes(s11, "Transition vers la partie 3, Easy Checks W3C.")

    # --- SLIDE 12 : Section 4 ---
    s12 = new_slide(prs, layouts, layout_name="chapitre", titre="",
                    footer_text="Formation 102638 / Partie 4",
                    date_text=DATE, page_num=12)
    compose_chapitre(
        s12, numero=4,
        titre="Améliorer l\u2019accessibilité numérique des publications "
              "sur les réseaux sociaux",
    )
    add_notes(s12, "Transition vers la partie 4, réseaux sociaux accessibles.")

    # --- SLIDE 13 : 1 carte DSFR (centrée) ---
    s13 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Layout une carte - message central",
                    fil_ariane="Démo | 1 carte",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=13)
    add_card(s13, "Principe fondamental",
             ["Une information doit être perceptible,",
              "utilisable, compréhensible et robuste",
              "(acronyme POUR de WCAG 2.2)."],
             top=TOP_CARDS, left=MARGIN_L,
             width=CONTENT_W, height=3.5, numero=1)
    add_notes(s13,
              "Usage : message unique à retenir, concept structurant. "
              "Carte centrée pour focaliser l\u2019attention.")

    # --- SLIDE 14 : 2 cartes DSFR (côte à côte) ---
    s14 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Layout deux cartes - comparer ou opposer",
                    fil_ariane="Démo | 2 cartes",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=14)
    card_w_2 = COL_W
    for i, (t, c) in enumerate([
        ("Audit automatique",
         ["Rapide (quelques minutes)",
          "Couvre 30 % des critères",
          "Outils : axe-core, WAVE, Lighthouse"]),
        ("Audit manuel",
         ["Long (journées à semaines)",
          "Couvre 100 % des critères",
          "Tests clavier, lecteur d\u2019écran, contraste"]),
    ]):
        add_card(s14, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (card_w_2 + GAP),
                 width=card_w_2, height=3.5, numero=i + 1)
    add_notes(s14,
              "Usage : comparaison en miroir, avant/après, deux approches. "
              "R21 de la neuropédagogie : apprentissage par opposition.")

    # --- SLIDE 15 : 3 cartes DSFR (côte à côte) ---
    s15 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Layout trois cartes - triptyque ou séquence",
                    fil_ariane="Démo | 3 cartes",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=15)
    card_w_3 = (CONTENT_W - GAP * 2) / 3
    for i, (t, c) in enumerate([
        ("Analyser",
         ["Identifier les points de blocage",
          "Prioriser par impact utilisateur"]),
        ("Corriger",
         ["Appliquer les remédiations",
          "Documenter les écarts restants"]),
        ("Vérifier",
         ["Tester sur le terrain",
          "Mesurer la progression"]),
    ]):
        add_card(s15, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (card_w_3 + GAP),
                 width=card_w_3, height=3.0, numero=i + 1)
    add_notes(s15,
              "Usage : triptyque (3 directions), séquence (3 étapes), "
              "triade conceptuelle. Au-delà de 3 cartes, préférer un tableau.")

    # --- SLIDE 16 : 1 carte + callout plein largeur ---
    s16 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Une carte + callout - accroche et renforcement",
                    fil_ariane="Démo | 1 carte + callout",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=16)
    add_card(s16, "Principe fondamental",
             ["Une information doit être perceptible,",
              "utilisable, compréhensible et robuste",
              "(acronyme POUR de WCAG 2.2)."],
             top=TOP_CARDS, left=MARGIN_L,
             width=CONTENT_W, height=2.3, numero=1)
    add_callout(
        s16, "Point d\u2019attention",
        ["Ces 4 principes structurent l\u2019ensemble des 50 critères RGAA 4.1.2.",
         "Les retenir facilite la lecture du référentiel."],
        top=TOP_CARDS + 2.6, height=1.5,
    )
    add_notes(s16,
              "Usage : carte = message principal, callout = renforcement "
              "ou implication concrète.")

    # --- SLIDE 17 : 2 cartes + callout plein largeur ---
    s17 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Deux cartes + callout - comparaison et synthèse",
                    fil_ariane="Démo | 2 cartes + callout",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=17)
    card_h_2 = 2.3
    for i, (t, c) in enumerate([
        ("Audit automatique",
         ["Rapide (quelques minutes)",
          "Couvre 30 % des critères"]),
        ("Audit manuel",
         ["Long (journées à semaines)",
          "Couvre 100 % des critères"]),
    ]):
        add_card(s17, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (COL_W + GAP),
                 width=COL_W, height=card_h_2, numero=i + 1)
    add_callout(
        s17, "À retenir",
        ["Les deux approches sont complémentaires :",
         "automatique pour détecter, manuel pour qualifier."],
        top=TOP_CARDS + card_h_2 + 0.3, height=1.5,
    )
    add_notes(s17,
              "Usage : cartes = comparaison, callout = conclusion/synthèse "
              "qui relie les deux.")

    # --- SLIDE 18 : 3 cartes + callout plein largeur ---
    s18 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Trois cartes + callout - processus et rappel",
                    fil_ariane="Démo | 3 cartes + callout",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=18)
    card_w_3b = (CONTENT_W - GAP * 2) / 3
    card_h_3 = 2.3
    for i, (t, c) in enumerate([
        ("Analyser",
         ["Identifier les blocages",
          "Prioriser par impact"]),
        ("Corriger",
         ["Appliquer les remédiations",
          "Documenter les écarts"]),
        ("Vérifier",
         ["Tester sur le terrain",
          "Mesurer la progression"]),
    ]):
        add_card(s18, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (card_w_3b + GAP),
                 width=card_w_3b, height=card_h_3, numero=i + 1)
    add_callout(
        s18, "Règle d\u2019or",
        ["Un cycle Analyser-Corriger-Vérifier dure 2 à 3 semaines.",
         "Le répéter tant qu\u2019il reste des non-conformités bloquantes."],
        top=TOP_CARDS + card_h_3 + 0.3, height=1.5,
    )
    add_notes(s18,
              "Usage : cartes = étapes d\u2019un processus, callout = règle "
              "transverse à retenir.")

    # --- SLIDE 19 : 1 carte sans numéro (pleine largeur) ---
    s19 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Une carte sans numéro - message sans séquence",
                    fil_ariane="Démo | 1 carte sans n°",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=19)
    add_card(s19, "Principe fondamental",
             ["Une information doit être perceptible,",
              "utilisable, compréhensible et robuste",
              "(acronyme POUR de WCAG 2.2)."],
             top=TOP_CARDS, left=MARGIN_L,
             width=CONTENT_W, height=3.5)
    add_notes(s19,
              "Usage : carte isolée sans numérotation - un concept, "
              "pas une étape de séquence.")

    # --- SLIDE 20 : 2 cartes sans numéro ---
    s20 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Deux cartes sans numéro - deux facettes équivalentes",
                    fil_ariane="Démo | 2 cartes sans n°",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=20)
    for i, (t, c) in enumerate([
        ("Audit automatique",
         ["Rapide (quelques minutes)",
          "Couvre 30 % des critères",
          "Outils : axe-core, WAVE, Lighthouse"]),
        ("Audit manuel",
         ["Long (journées à semaines)",
          "Couvre 100 % des critères",
          "Tests clavier, lecteur d\u2019écran, contraste"]),
    ]):
        add_card(s20, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (COL_W + GAP),
                 width=COL_W, height=3.5)
    add_notes(s20,
              "Usage : deux approches équivalentes, pas de hiérarchie ni "
              "d\u2019ordre implicite - pas de numérotation.")

    # --- SLIDE 21 : 3 cartes sans numéro ---
    s21 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Trois cartes sans numéro - triade de concepts",
                    fil_ariane="Démo | 3 cartes sans n°",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=21)
    card_w_3c = (CONTENT_W - GAP * 2) / 3
    for i, (t, c) in enumerate([
        ("Perceptible",
         ["Alternatives textuelles",
          "Contrastes suffisants",
          "Sous-titres"]),
        ("Utilisable",
         ["Navigation au clavier",
          "Temps suffisant",
          "Pas de clignotement"]),
        ("Compréhensible",
         ["Langue identifiée",
          "Texte lisible",
          "Prévisibilité"]),
    ]):
        add_card(s21, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (card_w_3c + GAP),
                 width=card_w_3c, height=3.5)
    add_notes(s21,
              "Usage : trois concepts juxtaposés sans ordre - "
              "triade, piliers, dimensions équivalentes.")

    # --- SLIDE 22 : 1 carte sans numéro + callout plein largeur ---
    s22 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Une carte sans numéro + callout",
                    fil_ariane="Démo | 1 carte sans n° + callout",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=22)
    add_card(s22, "Principe fondamental",
             ["Une information doit être perceptible,",
              "utilisable, compréhensible et robuste",
              "(acronyme POUR de WCAG 2.2)."],
             top=TOP_CARDS, left=MARGIN_L,
             width=CONTENT_W, height=2.3)
    add_callout(
        s22, "Point d\u2019attention",
        ["Ces 4 principes structurent l\u2019ensemble des 50 critères RGAA 4.1.2.",
         "Les retenir facilite la lecture du référentiel."],
        top=TOP_CARDS + 2.6, height=1.5,
    )
    add_notes(s22,
              "Usage : carte sans numérotation + callout de renforcement. "
              "Un concept unique relié à une implication concrète.")

    # --- SLIDE 23 : 2 cartes sans numéro + callout plein largeur ---
    s23 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Deux cartes sans numéro + callout",
                    fil_ariane="Démo | 2 cartes sans n° + callout",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=23)
    card_h_2b = 2.3
    for i, (t, c) in enumerate([
        ("Audit automatique",
         ["Rapide (quelques minutes)",
          "Couvre 30 % des critères"]),
        ("Audit manuel",
         ["Long (journées à semaines)",
          "Couvre 100 % des critères"]),
    ]):
        add_card(s23, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (COL_W + GAP),
                 width=COL_W, height=card_h_2b)
    add_callout(
        s23, "À retenir",
        ["Les deux approches sont complémentaires :",
         "automatique pour détecter, manuel pour qualifier."],
        top=TOP_CARDS + card_h_2b + 0.3, height=1.5,
    )
    add_notes(s23,
              "Usage : deux facettes équivalentes (pas d\u2019ordre) + "
              "synthèse qui relie les deux.")

    # --- SLIDE 24 : 3 cartes sans numéro + callout plein largeur ---
    s24 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Trois cartes sans numéro + callout",
                    fil_ariane="Démo | 3 cartes sans n° + callout",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=24)
    card_w_3d = (CONTENT_W - GAP * 2) / 3
    card_h_3b = 2.3
    for i, (t, c) in enumerate([
        ("Perceptible",
         ["Alternatives textuelles",
          "Contrastes suffisants"]),
        ("Utilisable",
         ["Navigation au clavier",
          "Temps suffisant"]),
        ("Compréhensible",
         ["Langue identifiée",
          "Texte lisible"]),
    ]):
        add_card(s24, t, c, top=TOP_CARDS,
                 left=MARGIN_L + i * (card_w_3d + GAP),
                 width=card_w_3d, height=card_h_3b)
    add_callout(
        s24, "Règle d\u2019or",
        ["Les 4 principes POUR couvrent 100 % des exigences WCAG.",
         "Tout critère se rattache à l\u2019un d\u2019eux."],
        top=TOP_CARDS + card_h_3b + 0.3, height=1.5,
    )
    add_notes(s24,
              "Usage : triade équivalente + règle transverse qui englobe "
              "les trois. Pas de séquence, pas de numérotation.")

    # --- SLIDE 25 : Checklist ---
    s25 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Checklist - préparer un document accessible",
                    fil_ariane="Démo | Checklist",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=25)
    add_checklist(s25, [
        ("Styles hiérarchiques appliqués (Titre 1, Titre 2, Titre 3)", True),
        ("Alt text renseigné sur toutes les images informatives", True),
        ("Contrastes vérifiés (\u2265 4,5:1 pour le texte courant)", False),
        ("Tableaux avec en-têtes de colonne identifiés", True),
        ("Liens avec texte descriptif (pas « cliquer ici »)", False),
        ("Langue du document définie (fr-FR)", True),
        ("Pas de justification - alignement à gauche", False),
    ], top=TOP_CARDS)
    add_notes(s25,
              "Usage : récap de critères, to-do post-formation. "
              "Cases cochées = acquis, cases vides = à travailler.")

    # --- SLIDE 26 : Avant / après ---
    s26 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Avant / après - un lien accessible",
                    fil_ariane="Démo | Avant et après",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=26)
    add_avant_apres(
        s26,
        avant_titre="Avant",
        avant_bullets=[
            "« Cliquez ici pour en savoir plus »",
            "Hors contexte, le lecteur ne sait pas où il arrive",
            "Échec du critère RGAA 6.1",
        ],
        apres_titre="Après",
        apres_bullets=[
            "« Consulter le rapport d\u2019audit 2025 »",
            "Le texte du lien décrit sa destination",
            "Conforme au critère RGAA 6.1",
        ],
        top=TOP_CARDS, height=3.5,
    )
    add_notes(s26,
              "Usage : montrer la correction d\u2019un défaut courant. "
              "Rouge clair pour le défaut, vert clair pour la version accessible.")

    # --- SLIDE 27 : Exemple / contre-exemple ---
    s27 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Exemple et contre-exemple - alt text d\u2019image",
                    fil_ariane="Démo | Bon et mauvais exemple",
                    footer_text="Formation 102638 / Démo composants",
                    date_text=DATE, page_num=27)
    add_exemple_contre_exemple(
        s27,
        bon_titre="À faire",
        bon_bullets=[
            "alt=\"Graphique en barres : progression 2020-2025\"",
            "Description concise et informative",
            "Rend l\u2019image compréhensible sans la voir",
        ],
        mauvais_titre="À éviter",
        mauvais_bullets=[
            "alt=\"image\" ou alt=\"image1.png\"",
            "Texte sans valeur informative",
            "alt=\"\" sur une image porteuse d\u2019information",
        ],
        top=TOP_CARDS, height=3.5,
    )
    add_notes(s27,
              "Usage : ancrage pédagogique par opposition. "
              "Icônes ✓ et ✗ signalent immédiatement la nature de chaque colonne.")

    # --- SLIDE 28 : Clôture ---
    s28 = new_slide(prs, layouts, layout_name="titre_contenu",
                    titre="Merci pour votre attention",
                    footer_text="Formation 102638 / Clôture",
                    date_text=DATE, page_num=28)
    add_highlight(
        s28,
        "Pour toute question : formation-igpde@finances.gouv.fr",
        top=3.2, height=1.0,
    )
    add_texte_libre(
        s28, "Retrouvez les supports sur l\u2019espace Alizé de l\u2019IGPDE",
        top=4.6, left=MARGIN_L, width=CONTENT_W, height=0.5,
        size=14, color=BLEU_FRANCE, align=PP_ALIGN.CENTER,
    )
    add_texte_libre(
        s28, "Merci de répondre à l\u2019évaluation à chaud en sortant de salle",
        top=5.3, left=MARGIN_L, width=CONTENT_W, height=0.5,
        size=12, color=GRIS_CLAIR, align=PP_ALIGN.CENTER,
    )
    add_notes(s28,
              "Slide de clôture : remerciements, contact formateur, rappel "
              "évaluation à chaud. Pas de fil d\u2019Ariane (fin de parcours).")

    finalize_pptx(prs, str(OUTPUT),
                  title="Template IGPDE-DSFR - démonstration",
                  author="Alex Guiderdoni",
                  subject="Démonstration des composants DSFR sur template IGPDE")
    print(f"[OK] {OUTPUT.name} généré ({len(prs.slides)} slides)")


if __name__ == "__main__":
    main()
