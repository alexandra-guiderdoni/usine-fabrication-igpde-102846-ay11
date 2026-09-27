#!/usr/bin/env python3
"""
Génération du PPTX DSFR : Rendre un document Word accessible
30 slides pédagogiques — 5 piliers, 22 critères

v3 vs v2 (28 slides) :
  S8  scindée en S8 (listes) + S9 (colonnes et sauts de page)
  S21 ajoutée : quiz contenus (après pilier 3)
  Notes orateur : chiffres sourcés (OMS, DREES)
"""

import sys
import os

sys.path.insert(0, os.path.expanduser("~/Claude/.claude/skills/accessible-pptx/scripts"))
from dsfr_components import *

FOOTER = "Accessibilité Word — avril 2026"
TOTAL = 30
prs, TITRES = create_presentation("dsfr")


# ═══════════════════════════════════════════════════════════════
# SLIDE 1 — Titre (NEW)
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Rendre un document Word accessible",
                  footer=FOOTER, page_number=1, total_pages=TOTAL)

add_highlight(slide,
    "Guide méthodologique pas-à-pas — 22 critères en 5 piliers",
    top=1.8, height=1.0)

add_callout(slide, "Public", [
    "Agents publics, services communication, secrétariats",
    "Aucun prérequis technique — juste Word pour PC",
], top=3.2, left=MARGIN_L, width=COL_W, height=1.5)

add_callout(slide, "Format", [
    "30 slides, ~60 minutes",
    "Alternance théorie / pratique / quiz",
], top=3.2, left=COL_R, width=COL_W, height=1.5)

add_notes(slide,
    "- Accueillir les participants, vérifier que chacun a Word ouvert\n"
    "- Préciser que la formation est 100 % pratique\n"
    "- Timing : 1 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 2 — Accroche : ce document est-il accessible ?
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Ce document est-il accessible ?",
                  footer=FOOTER, page_number=2, total_pages=TOTAL)

add_alert(slide, "Document A", [
    "Titres en gras manuellement",
    "Image sans texte alternatif",
    "Tableau avec cellules fusionnées",
    'Nom : "Document1.docx"',
], top=1.4, left=MARGIN_L, width=COL_W, height=2.5, alert_type="error")

add_alert(slide, "Document B", [
    "Titres avec styles Titre 1, Titre 2",
    "Image avec description fonctionnelle",
    "Tableau simple avec en-tête identifié",
    'Nom : "rapport-accessibilite-2024.docx"',
], top=1.4, left=COL_R, width=COL_W, height=2.5, alert_type="success")

add_highlight(slide,
    "Visuellement identiques — mais seul le document B est lisible par un lecteur d'écran.",
    top=4.2)

add_notes(slide,
    "- Afficher les 2 colonnes, demander : « Lequel choisissez-vous ? » (R9)\n"
    "- Laisser 10 secondes puis révéler : visuellement identiques, structure différente (R8)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 3 — Pourquoi ça vous concerne
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pourquoi ça vous concerne",
                  footer=FOOTER, page_number=3, total_pages=TOTAL)

kpi_w = (CONTENT_W - GAP * 2) / 3
for i, (val, lbl) in enumerate([
    ("15 %", "de la population\nen situation de handicap"),
    ("80 %", "des handicaps\nsont invisibles"),
    ("0", "ligne de code\nnécessaire"),
]):
    add_pave_chiffre(slide, val, lbl, top=1.4,
                     left=MARGIN_L + i * (kpi_w + GAP), width=kpi_w, height=1.6)

add_highlight(slide,
    "L'accessibilité Word est 100 % éditoriale : pas de code, juste les bons réflexes dans le ruban.",
    top=3.4)

add_notes(slide,
    "- Ce n'est pas une compétence technique, c'est une compétence rédactionnelle (R12 — WIIFM)\n"
    "- Sources : 15 % = OMS, Rapport mondial sur le handicap (2011, confirmé 2023)\n"
    "  80 % = DREES, enquête Handicap-Santé (handicaps non visibles)\n"
    "- « Vous produisez déjà des documents Word — il s'agit d'utiliser les bonnes fonctionnalités »\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 4 — Ce que couvre cette formation (NEW)
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Ce que couvre cette formation",
                  footer=FOOTER, page_number=4, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Pilier", "Sujets couverts", "Gestes Word"],
    [
        ["Structure", "Titres, listes, colonnes, sauts de page, tableaux", "Styles, volet de navigation, Insertion > Tableau"],
        ["Couleurs", "Contraste, couleur porteuse de sens", "Colour Contrast Analyser"],
        ["Contenus", "Texte alt, liens, zones de texte, infos essentielles", "Texte de remplacement, Ctrl+K"],
        ["Langue et médias", "Balisage langue, transcriptions, clignotement", "Révision > Langue"],
        ["Finalisation", "Propriétés, nom, formulaires, vérificateur", "Fichier > Informations"],
    ],
    top=1.4, col_widths=[2.0, 5.5, 4.5])

add_alert(slide, "Hors périmètre", [
    "Documents avec macros (.docm, .dotm), documents protégés, formulaires Word interactifs.",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.0, alert_type="info")

add_notes(slide,
    "- Le tableau est la référence visuelle, l'oral donne le fil rouge (R5 — double codage)\n"
    "- « Chaque pilier se termine par une vérification concrète »\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 5 — Quiz vrai ou faux
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Quiz : vrai ou faux ?",
                  footer=FOOTER, page_number=5, total_pages=TOTAL)

add_stepper(slide, [
    "Un texte en gras taille 16\nest un titre pour\nle lecteur d'écran",
    "Un tableau créé avec\ndes tabulations est\nlisible par les TA",
    "Le vérificateur d'accessibilité\nde Word détecte tous\nles problèmes",
], top=1.4, step_height=2.8)

add_highlight(slide,
    "Réponse : les trois sont FAUX. Si vous avez eu au moins un faux, cette formation va vous aider.",
    top=4.8)

add_notes(slide,
    "- Faire voter à main levée pour chaque affirmation (R14)\n"
    "- 1. FAUX : seuls les styles de titre comptent\n"
    "- 2. FAUX : fonctionnalité Tableau obligatoire\n"
    "- 3. FAUX : premier filtre utile mais incomplet\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 6 — Vue d'ensemble : 5 piliers
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "5 piliers, 22 critères",
                  footer=FOOTER, page_number=6, total_pages=TOTAL)

card_w = (CONTENT_W - GAP * 4) / 5
for i, (titre, contenu) in enumerate([
    ("Structure", "Titres, listes, colonnes,\ntableaux, sauts de page\n\n6 critères"),
    ("Couleurs", "Contraste et\nsignification visuelle\n\n2 critères"),
    ("Contenus", "Images, liens,\nzones de texte,\ninfos essentielles\n5 critères"),
    ("Langue\net médias", "Balisage linguistique,\ntranscriptions\n\n4 critères"),
    ("Finalisation", "Propriétés, nom,\nformulaires,\nvérificateur\n5 critères"),
]):
    add_card(slide, titre, contenu, top=1.4,
             left=MARGIN_L + i * (card_w + GAP), width=card_w, height=3.0)

add_notes(slide,
    "- Carte mentale du parcours : « On avance pilier par pilier » (R4)\n"
    "- « Le pilier Structure représente 60 % de l'effort — c'est là qu'on commence » (R11)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 7 — Pilier 1 : styles de titre
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 1 — Les styles de titre",
                  footer=FOOTER, page_number=7, total_pages=TOTAL)

add_alert(slide, "Ce que le lecteur d'écran voit", [
    '"Texte, texte, texte, texte..."',
    "Un bloc plat sans repère de navigation.",
], top=1.4, left=MARGIN_L, width=COL_W, height=1.8, alert_type="error")

add_alert(slide, "Avec les styles de titre", [
    '"Titre 1 : Rapport > Titre 2 : Budget > Titre 3 : Prévisions..."',
    "Navigation par titres en quelques secondes.",
], top=1.4, left=COL_R, width=COL_W, height=1.8, alert_type="success")

add_callout(slide, "Chemin menu", [
    "Accueil > Styles > Titre 1, Titre 2, Titre 3...",
    "Raccourci : Ctrl+Alt+Maj+S pour ouvrir le volet Styles",
    "Vérification : Ctrl+F > onglet Titres (volet de navigation)",
], top=3.5, left=MARGIN_L, width=CONTENT_W, height=2.0)

add_notes(slide,
    "- « Imaginez lire un livre de 50 pages sans table des matières » (R7 — analogie)\n"
    "- Montrer le volet de navigation en direct\n"
    "- Hiérarchie : Titre 1 > Titre 2 > Titre 3, pas de saut de niveau\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 8 — Listes intégrées
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Listes : puces et numérotation natives",
                  footer=FOOTER, page_number=8, total_pages=TOTAL)

add_alert(slide, "Inaccessible : tirets et chiffres manuels", [
    "- Premier élément",
    "- Deuxième élément",
    "- Troisième élément",
    "",
    "Le lecteur d'écran lit « tiret Premier élément » — pas une liste.",
], top=1.4, left=MARGIN_L, width=COL_W, height=2.8, alert_type="error")

add_alert(slide, "Accessible : fonctionnalité de liste", [
    "Premier élément",
    "Deuxième élément",
    "Troisième élément",
    "",
    "Le lecteur d'écran annonce « liste de 3 éléments, élément 1 sur 3 ».",
], top=1.4, left=COL_R, width=COL_W, height=2.8, alert_type="success")

add_callout(slide, "Chemin menu", [
    "Accueil > Paragraphe > Puces, Numérotation ou Liste à plusieurs niveaux",
    "Vérification : Maj+F1 (Révéler la mise en forme) > « Puces et numérotation » doit apparaître",
], top=4.5, left=MARGIN_L, width=CONTENT_W, height=1.5)

add_notes(slide,
    "- Exercice en binôme (2 min) : « Ouvrez un document, Maj+F1, cliquez sur une liste » (R17)\n"
    "- Word auto-corrige souvent les tirets en listes — mais pas toujours, vérifier\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 9 — Colonnes et sauts de page
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Colonnes et sauts de page",
                  footer=FOOTER, page_number=9, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Besoin", "Fonctionnalité intégrée", "Piège courant"],
    [
        ["Colonnes", "Mise en page > Colonnes", "Tabulations ou espaces"],
        ["Saut de page", "Insertion > Saut de page (Ctrl+Entrée)", "Retours chariot (Entrée x15)"],
    ],
    top=1.4, col_widths=[2.5, 5.5, 4.0])

add_callout(slide, "Vérification des colonnes", [
    "Curseur sur le texte en colonnes > Maj+F1 (Révéler la mise en forme)",
    "La mention « Colonnes » doit apparaître sous « Section »",
    "Si absente : les colonnes sont simulées avec des tabulations (inaccessible)",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.8)

add_alert(slide, "Règle d'or", [
    "Si vous touchez à Tab, Espace ou Entrée pour simuler une mise en page,",
    "vous créez une barrière invisible pour les technologies d'assistance.",
], top=1.4 + tbl_h + 0.3 + 1.8 + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.3, alert_type="warning")

add_notes(slide,
    "- Les retours chariot pour sauter une page : le lecteur d'écran lit chaque ligne vide\n"
    "- Ctrl+Entrée = 1 saut propre, invisible pour les TA, robuste au redimensionnement\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 10 — Tableaux de mise en page
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Tableaux de mise en page",
                  footer=FOOTER, page_number=10, total_pages=TOTAL)

add_stepper(slide, [
    "Insertion > Tableau >\nnombre de colonnes\net lignes",
    "Remplir le contenu\n(gauche à droite,\nhaut en bas)",
    "Vérifier l'ordre :\nTab dans la 1re cellule,\nparcourir avec Tab",
    "Vérifier l'alignement :\nclic droit > Propriétés >\nHabillage = Aucun",
], top=1.4, step_height=2.8)

add_alert(slide, "Pourquoi « Aucun » ?", [
    "Un tableau avec habillage « Autour » flotte sur la page —",
    "le lecteur d'écran ne le lit pas au bon moment par rapport au reste du contenu.",
], top=4.6, left=MARGIN_L, width=CONTENT_W, height=1.3, alert_type="info")

add_notes(slide,
    "- Distinguer tableau de mise en page (pas d'en-têtes) et tableau de données (en-têtes)\n"
    "- « Le piège classique : copier-coller un tableau sans vérifier l'habillage » (R6)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 11 — Tableaux de données
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Tableaux de données",
                  footer=FOOTER, page_number=11, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Exigence", "Comment"],
    [
        ["Créer avec l'outil intégré", "Insertion > Tableau (jamais d'image)"],
        ["Pas de cellules fusionnées", "Tableau simple uniquement"],
        ["Identifier la ligne d'en-tête", "Clic droit > Propriétés > Ligne > Répéter en tant que ligne d'en-tête"],
        ["Aligner avec le texte", "Propriétés > Tableau > Habillage = Aucun"],
    ],
    top=1.4, col_widths=[4.0, 8.0])

add_alert(slide, "Limitation", [
    "Les tableaux complexes (multi-niveaux d'en-têtes, cellules fusionnées)",
    "ne peuvent pas être rendus accessibles dans Word.",
    "Solution : convertir en PDF accessible.",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.6, alert_type="warning")

add_notes(slide,
    "- Montrer la différence entre « Outils Image » (image de tableau) et « Outils de tableau »\n"
    "- « Répéter en tant que ligne d'en-tête » : invisible visuellement mais capital pour les TA\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 12 — Quiz mi-parcours structure
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Quiz : vérifier la structure en 30 secondes",
                  footer=FOOTER, page_number=12, total_pages=TOTAL)

add_callout(slide, "Votre collègue vous envoie un document Word. Comment vérifiez-vous la structure ?", [
    "A. Vous regardez si les titres sont en gras",
    "B. Vous ouvrez le volet de navigation (Ctrl+F) et vérifiez que les titres y apparaissent",
    "C. Vous lancez le correcteur orthographique",
    "D. Vous vérifiez que le fichier est en .docx",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=3.0)

add_highlight(slide,
    "Réponse : B — le volet de navigation est le test ultime de la structure.",
    top=4.7)

add_notes(slide,
    "- Faire voter (R14). Bonne réponse : B\n"
    "- « D est nécessaire mais pas suffisant — le format .docx est un prérequis, pas une preuve »\n"
    "- Feedback immédiat après le vote (R19)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 13 — Pilier 2 : contraste des couleurs
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 2 — Contraste des couleurs",
                  footer=FOOTER, page_number=13, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Type de texte", "Ratio minimum"],
    [
        ["Standard (< 14 pt gras)", "4,5:1"],
        ["Grande taille (>= 14 pt gras ou >= 18 pt)", "3:1"],
    ],
    top=1.4, col_widths=[7.0, 5.0])

add_callout(slide, "Outil : Colour Contrast Analyser (CCA) de TPGi", [
    "Pipette premier plan (texte) + pipette arrière-plan (fond) = ratio instantané",
    "Téléchargement gratuit, fonctionne sous Windows et macOS",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.5)

add_highlight(slide,
    "Texte noir sur fond blanc = toujours conforme. Le test ne s'applique qu'aux textes colorés.",
    top=1.4 + tbl_h + 0.3 + 1.5 + 0.3)

add_notes(slide,
    "- Si possible, projeter CCA en direct sur un extrait de document (R5 — double codage)\n"
    "- « Les designers connaissent ce ratio — votre rôle est de vérifier » (R21)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 14 — Mesurer le contraste pas-à-pas
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Mesurer le contraste : méthode pas-à-pas",
                  footer=FOOTER, page_number=14, total_pages=TOTAL)

add_stepper(slide, [
    "Ouvrir le Colour\nContrast Analyser\n(CCA)",
    "Pipette « Premier plan »\nsur la couleur\ndu texte",
    "Pipette « Arrière-plan »\nsur la couleur\ndu fond",
    "Lire le ratio :\n>= 4,5:1 standard\n>= 3:1 grande taille",
], top=1.4, step_height=2.8)

add_alert(slide, "Avant", [
    "Texte gris clair (#999) sur fond blanc (#FFF)",
    "Ratio : 2,85:1 — ÉCHEC",
], top=4.6, left=MARGIN_L, width=COL_W, height=1.3, alert_type="error")

add_alert(slide, "Après", [
    "Texte gris foncé (#595959) sur fond blanc (#FFF)",
    "Ratio : 7,0:1 — CONFORME",
], top=4.6, left=COL_R, width=COL_W, height=1.3, alert_type="success")

add_notes(slide,
    "- Démonstration en direct si CCA est installé\n"
    "- Astuce : ajuster le gris par pas de 10 en hexadécimal jusqu'au ratio cible\n"
    "- « La plupart du temps, il suffit de foncer légèrement le gris » (R21 — scaffolding)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 15 — La couleur ne suffit jamais
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "La couleur ne suffit jamais",
                  footer=FOOTER, page_number=15, total_pages=TOTAL)

add_alert(slide, "Inaccessible", [
    "| Projet | Statut |",
    "| Migration | (rouge) |",
    "| Formation | (vert) |",
    "| Audit | (jaune) |",
    "",
    "Un daltonien voit 3 couleurs identiques.",
], top=1.4, left=MARGIN_L, width=COL_W, height=3.2, alert_type="error")

add_alert(slide, "Accessible", [
    "| Projet | Statut |",
    "| Migration | En retard |",
    "| Formation | Terminé |",
    "| Audit | En cours |",
    "",
    "Le texte porte l'information, la couleur la renforce.",
], top=1.4, left=COL_R, width=COL_W, height=3.2, alert_type="success")

add_highlight(slide,
    "8 % des hommes sont daltoniens — dans une réunion de 12 personnes, il y en a probablement un.",
    top=4.9)

add_notes(slide,
    "- Fait surprenant : 8 % des hommes daltoniens (R8)\n"
    "- Règle simple : « Si vous imprimez en noir et blanc, l'information est-elle compréhensible ? »\n"
    "- Source : 8 % = Colour Blind Awareness, étude population masculine européenne\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 16 — Pilier 3 : texte alternatif
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 3 — Texte alternatif",
                  footer=FOOTER, page_number=16, total_pages=TOTAL)

add_stepper(slide, [
    "Sélectionner l'image >\nclic droit >\nFormat de l'image >\nTexte de remplacement",
    "Image significative :\ndécrire la FONCTION,\npas l'apparence",
    "Image décorative :\ninsérer des espaces\nvides dans Description",
], top=1.4, step_height=2.5)

add_alert(slide, "Mauvais texte alt", [
    '"Photo d\'un graphique en barres colorées"',
], top=4.2, left=MARGIN_L, width=COL_W, height=1.0, alert_type="error")

add_alert(slide, "Bon texte alt", [
    '"Chiffre d\'affaires 2020-2024 : hausse de 15 % à 23 %"',
], top=4.2, left=COL_R, width=COL_W, height=1.0, alert_type="success")

add_notes(slide,
    "- Test mental : « Si je remplace l'image par le texte alt, le document reste compréhensible ? » (R7)\n"
    "- Exercice : montrer une image, rédiger un alt en 15 secondes, comparer (R17)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 17 — Objets décoratifs
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Objets décoratifs : le silence est d'or",
                  footer=FOOTER, page_number=17, total_pages=TOTAL)

add_callout(slide, "Qu'est-ce qu'un objet décoratif ?", [
    "Filets, séparateurs, icônes purement visuelles, images d'ambiance",
    "Tout objet qui n'apporte aucune information que le texte ne contient pas déjà",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=1.5)

add_alert(slide, "Le piège", [
    "Un lecteur d'écran annonce chaque image qu'il rencontre.",
    "Un objet décoratif avec texte alt pollue la lecture :",
    '"Image, image, séparateur bleu, icône, image..."',
    "L'utilisateur perd le fil du contenu réel.",
], top=3.2, left=MARGIN_L, width=COL_W, height=2.5, alert_type="warning")

add_alert(slide, "La solution", [
    "Clic droit > Format de l'image > Texte de remplacement",
    "Insérer des espaces vides dans le champ Description",
    "(ou cocher « Marquer comme décoratif » si disponible)",
    "Le lecteur d'écran ignore l'objet silencieusement.",
], top=3.2, left=COL_R, width=COL_W, height=2.5, alert_type="success")

add_notes(slide,
    "- Analogie : « C'est comme un figurant au cinéma — il est là pour le décor, pas pour parler » (R7)\n"
    "- Question au public : « Dans vos documents, combien d'images sont purement décoratives ? » (R13)\n"
    "- En cas de doute : décrire plutôt que marquer comme décoratif\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 18 — Alignement et zones de texte
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Alignement et zones de texte",
                  footer=FOOTER, page_number=18, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Objet", "Exigence", "Chemin menu"],
    [
        ["Images", "Aligné sur le texte", "Outils Image > Format > Position"],
        ["Formes", "Aligné sur le texte", "Idem"],
        ["Zones de texte", "Aligné (ou éviter)", "Idem"],
    ],
    top=1.4, col_widths=[3.0, 4.0, 5.0])

add_alert(slide, "Piège des zones de texte", [
    "Même alignées, les zones de texte peuvent être lues dans un ordre inattendu.",
    "Les éviter quand c'est possible — préférer les colonnes intégrées.",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.5, alert_type="warning")

add_highlight(slide,
    "Objet flottant = objet invisible pour le lecteur d'écran.",
    top=1.4 + tbl_h + 0.3 + 1.5 + 0.3)

add_notes(slide,
    "- Phrase à retenir : « Objet flottant = objet invisible » (R3 — charge cognitive réduite)\n"
    "- Le vérificateur d'accessibilité signale les objets non alignés (pilier 5)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 19 — Liens descriptifs
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Liens descriptifs",
                  footer=FOOTER, page_number=19, total_pages=TOTAL)

add_alert(slide, "Inaccessible", [
    '"Cliquez ici"',
    '"En savoir plus"',
    '"https://www.exemple.fr/page?id=4827&ref=nav"',
], top=1.4, left=MARGIN_L, width=COL_W, height=2.0, alert_type="error")

add_alert(slide, "Accessible", [
    '"Consulter le guide d\'accessibilité Word"',
    '"Télécharger le rapport annuel 2024 (PDF, 2 Mo)"',
    '"Accéder au formulaire de contact"',
], top=1.4, left=COL_R, width=COL_W, height=2.0, alert_type="success")

add_callout(slide, "Méthode", [
    "Sélectionner le texte descriptif > clic droit > Lien hypertexte (Ctrl+K)",
    "Attention : supprimer le dernier caractère du texte d'un lien supprime le lien entier",
], top=3.7, left=MARGIN_L, width=CONTENT_W, height=1.5)

add_notes(slide,
    "- « Un utilisateur de lecteur d'écran navigue de lien en lien — imaginez entendre\n"
    "  'cliquez ici, cliquez ici, cliquez ici' sans contexte » (R7 — analogie)\n"
    "- Pour les documents imprimés ET numériques : inclure l'URL entre parenthèses\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 20 — Informations essentielles invisibles
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Informations essentielles invisibles",
                  footer=FOOTER, page_number=20, total_pages=TOTAL)

add_callout(slide, "Ce que les TA ne lisent pas automatiquement", [
    "En-têtes de page",
    "Pieds de page",
    "Filigranes",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=1.8)

add_highlight(slide,
    "Si une information est essentielle (« CONFIDENTIEL », « Répondre avant le 15 avril »), "
    "elle doit être reproduite dans le corps du document.",
    top=3.5, height=1.0)

add_alert(slide, "Exemple concret", [
    "Vous mettez « CONFIDENTIEL » en filigrane pour que tout le monde le voie —",
    "sauf que 15 % de vos lecteurs ne le voient pas du tout.",
    "Solution : une ligne au début du document reprenant l'information.",
], top=4.8, left=MARGIN_L, width=CONTENT_W, height=1.6, alert_type="info")

add_notes(slide,
    "- Surprise : le filigrane que tout le monde voit est invisible pour les TA (R8)\n"
    "- Solution simple : une ligne au début du document\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 21 — Quiz mi-parcours contenus (NEW)
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Quiz : avez-vous les bons réflexes contenus ?",
                  footer=FOOTER, page_number=21, total_pages=TOTAL)

add_callout(slide, "Pour chaque situation, quelle est la bonne action ?", [
    "1. Une photo d'équipe illustre la page « Qui sommes-nous »",
    "2. Un filet bleu sépare deux sections du document",
    "3. Un lien « En savoir plus » renvoie vers le site intranet",
    '4. Le filigrane indique « BROUILLON — Ne pas diffuser »',
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=2.8)

add_alert(slide, "Réponses", [
    "1. Texte alt décrivant la fonction : « Équipe du service communication, 8 personnes »",
    "2. Marquer comme décoratif (espaces vides dans le champ Description)",
    "3. Renommer en « Consulter la page intranet du projet X »",
    "4. Reproduire « BROUILLON — Ne pas diffuser » au début du document",
], top=4.5, left=MARGIN_L, width=CONTENT_W, height=2.0, alert_type="success")

add_notes(slide,
    "- Faire répondre individuellement puis corriger en groupe (R14 — récupération active)\n"
    "- Insister sur la distinction significatif/décoratif (questions 1 vs 2)\n"
    "- Feedback immédiat après chaque réponse (R19)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 22 — Pilier 4 : langue et médias
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 4 — Langue et médias",
                  footer=FOOTER, page_number=22, total_pages=TOTAL)

add_callout(slide, "Balisage de langue", [
    "Langue principale : Fichier > Options > Langue",
    "Passage étranger : sélectionner > Révision > Langue > Définir la langue de vérification",
    'Sans balisage, le lecteur d\'écran prononce "meeting" comme "mé-é-ting"',
], top=1.4, left=MARGIN_L, width=COL_W, height=2.5)

tbl_h = add_tableau(slide,
    ["Média intégré", "Alternative requise"],
    [
        ["Audio seul", "Transcription textuelle"],
        ["Vidéo seule", "Description textuelle"],
        ["Audio + vidéo", "Sous-titres ET description audio"],
    ],
    top=1.4, left=COL_R, width=COL_W, col_widths=[2.5, 3.335])

add_notes(slide,
    "- Faire écouter une synthèse vocale lisant un mot anglais avec balisage français (R8)\n"
    "- « La plupart de vos documents contiennent au moins un anglicisme — feedback, planning... »\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 23 — Objets clignotants
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Objets clignotants : tolérance zéro",
                  footer=FOOTER, page_number=23, total_pages=TOTAL)

add_alert(slide, "Interdit — aucune exception", [
    "Animations de clignotement, GIF avec flashs, vidéos avec séquences > 3 Hz",
    "",
    "Risque : crise d'épilepsie.",
    "Un document contenant un objet clignotant ne peut jamais être considéré comme accessible.",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=2.5, alert_type="error")

add_highlight(slide,
    "Si vous hésitez sur un GIF animé : supprimez-le et remplacez-le par une image statique.",
    top=4.2)

add_notes(slide,
    "- Court et direct — interdit absolu\n"
    "- « C'est le seul critère binaire : un seul objet clignotant = document non accessible »\n"
    "- Timing : 1 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 24 — Pilier 5 : avant de publier
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 5 — Avant de publier",
                  footer=FOOTER, page_number=24, total_pages=TOTAL)

add_stepper(slide, [
    "Propriétés :\nFichier > Informations\n> Titre, Auteur, Objet",
    "Nom de fichier :\ndescriptif + .docx\n(pas « Document1 »)",
    "Protection :\nRévision > Restreindre\n> aucune restriction",
    "Formulaires :\naucun champ de\nformulaire Word",
    "Vérificateur :\nFichier > Vérifier\nl'accessibilité",
], top=1.4, step_height=3.0)

add_highlight(slide,
    "Ces 5 vérifications prennent 2 minutes et attrapent 80 % des oublis restants.",
    top=4.8)

add_notes(slide,
    "- « Ces 5 vérifications prennent 2 minutes » (R12 — WIIFM)\n"
    "- Le titre dans les propriétés est celui que les TA annoncent à l'ouverture\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 25 — Vérificateur : allié imparfait
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Le vérificateur : allié imparfait",
                  footer=FOOTER, page_number=25, total_pages=TOTAL)

add_alert(slide, "Ce qu'il détecte", [
    "Texte alt manquant",
    "Objets non alignés",
    "Styles de titre absents",
    "Tableaux sans en-tête",
    "Ordre de lecture",
], top=1.4, left=MARGIN_L, width=COL_W, height=2.8, alert_type="success")

add_alert(slide, "Ce qu'il ne détecte PAS", [
    "Qualité du texte alt",
    "Pertinence des noms de liens",
    "Couleur porteuse de sens",
    "Langue des passages étrangers",
    "Contraste insuffisant",
], top=1.4, left=COL_R, width=COL_W, height=2.8, alert_type="warning")

add_highlight(slide,
    "Le vérificateur est un premier filtre, pas un certificat de conformité.",
    top=4.5)

add_notes(slide,
    "- « Pensez au correcteur orthographique : il attrape les fautes évidentes,\n"
    "  mais il ne garantit pas que votre texte est bien écrit » (R7 — analogie)\n"
    "- Montrer le vérificateur en direct si possible\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 26 — Étude de cas de A à Z
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Étude de cas : un document de A à Z",
                  footer=FOOTER, page_number=26, total_pages=TOTAL)

add_callout(slide, "Sophie, assistante de direction, doit publier un compte rendu de réunion", [
    "Le document contient : 3 niveaux de titres, 2 tableaux, 1 organigramme, 1 lien",
    "Il porte la mention « CONFIDENTIEL » en filigrane",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=1.5)

tbl_h = add_tableau(slide,
    ["Étape", "Ce que Sophie fait", "Pilier"],
    [
        ["1", "Applique Titre 1, 2, 3 via Accueil > Styles", "Structure"],
        ["2", "Identifie la ligne d'en-tête de chaque tableau", "Structure"],
        ["3", "Ajoute un texte alt fonctionnel sur l'organigramme", "Contenus"],
        ["4", "Renomme le lien « cliquez ici » en description claire", "Contenus"],
        ["5", "Ajoute « CONFIDENTIEL » au début du document", "Contenus"],
        ["6", "Renseigne Titre et Auteur dans Fichier > Informations", "Finalisation"],
        ["7", "Lance le vérificateur > corrige les 2 erreurs restantes", "Finalisation"],
    ],
    top=3.2, col_widths=[1.0, 7.0, 4.0])

add_notes(slide,
    "- Storytelling : Sophie est le héros, le document inaccessible est le conflit (R6)\n"
    "- « En 7 étapes et 10 minutes, Sophie a rendu son document accessible »\n"
    "- Demander : « Combien de ces étapes faites-vous déjà ? » (R25 — métacognition)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 27 — Quiz final
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Quiz final : trouvez les erreurs",
                  footer=FOOTER, page_number=27, total_pages=TOTAL)

add_callout(slide, "Un document Word contient :", [
    "1. Un titre « Introduction » mis en gras Arial 16 (sans style)",
    "2. Un tableau de 3 colonnes avec la 1re ligne en gras (sans « Répéter en tant que ligne d'en-tête »)",
    '3. Un lien « cliquez ici pour le formulaire »',
    "4. Un filigrane « PROJET » sans mention dans le corps du document",
    "5. Une photo de l'équipe sans texte alternatif",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=3.5)

add_highlight(slide,
    "Combien d'erreurs d'accessibilité comptez-vous ? Réponse : 5 erreurs (une par point).",
    top=5.2)

add_notes(slide,
    "- Faire compter individuellement, puis partager (R14)\n"
    "- Parcourir chaque erreur et rappeler le critère correspondant\n"
    "- « Si vous les avez toutes trouvées, vous avez intégré les 5 piliers » (R25)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 28 — Matrice effort/impact
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Par où commencer ?",
                  footer=FOOTER, page_number=28, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["", "Effort faible", "Effort modéré"],
    [
        ["Impact fort",
         "Styles de titre\nListes intégrées\nNom descriptif\nPropriétés du document",
         "Texte alternatif\nLiens descriptifs\nTableaux avec en-têtes"],
        ["Impact modéré",
         "Sauts de page\nColonnes intégrées\nLangue des passages",
         "Contraste couleurs\nAlignement objets\nZones de texte"],
    ],
    top=1.4, col_widths=[2.5, 5.0, 4.5])

add_highlight(slide,
    "Commencez par le quadrant haut-gauche : 4 actions à effort faible qui transforment l'accessibilité.",
    top=1.4 + tbl_h + 0.3)

add_notes(slide,
    "- « Si vous ne retenez qu'une chose : les styles de titre. Quick win numéro 1 » (R2)\n"
    "- La matrice sert de feuille de route pour les semaines suivantes\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 29 — Checklist 21 critères
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Checklist : vos 21 critères",
                  footer=FOOTER, page_number=29, total_pages=TOTAL)

add_encadre(slide, top=1.4, left=MARGIN_L, width=COL_W, height=5.0,
            couleur_fond=GRIS_CLAIR, titre="Structure et couleurs",
            bullets=[
                "1. Fichier .docx + nom descriptif",
                "2. Document non protégé",
                "3. Titres avec styles intégrés",
                "4. Hiérarchie cohérente",
                "5. Listes avec Puces/Numérotation",
                "6. Colonnes intégrées",
                "7. Sauts de page propres",
                "8. Tableaux mise en page OK",
                "9. Tableaux données + en-têtes",
                "10. Contraste >= 4,5:1 / 3:1",
                "11. Couleur doublée en texte",
            ])

add_encadre(slide, top=1.4, left=COL_R, width=COL_W, height=5.0,
            couleur_fond=GRIS_CLAIR, titre="Contenus, langue, finalisation",
            bullets=[
                "12. Texte alt sur images/objets",
                "13. Objets alignés sur le texte",
                "14. Liens descriptifs",
                "15. Infos essentielles dans le corps",
                "16. Langue des passages balisée",
                "17. Médias avec alternatives",
                "18. Aucun objet clignotant",
                "19. Propriétés renseignées",
                "20. Aucun formulaire Word",
                "21. Vérificateur sans erreur",
            ])

add_notes(slide,
    "- Distribuer la checklist imprimée ou la partager en version numérique\n"
    "- « Imprimez-la, collez-la à côté de votre écran » (R26 — transformation)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 30 — Demain à 9h
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Demain à 9h",
                  footer=FOOTER, page_number=30, total_pages=TOTAL)

add_highlight(slide,
    "Quelle est la première chose que vous ferez sur votre prochain document Word ?",
    top=1.4, height=1.0)

card_w = (CONTENT_W - GAP * 2) / 3
for i, (titre, contenu) in enumerate([
    ("Réflexe 1",
     "Ctrl+F > onglet Titres\n\nVérifier que tous les titres\napparaissent dans le volet\nde navigation"),
    ("Réflexe 2",
     "Clic droit > Texte\nde remplacement\n\nDécrire la fonction\nde chaque image"),
    ("Réflexe 3",
     "Fichier > Vérifier\nl'accessibilité\n\nCorriger les erreurs\navant d'envoyer"),
]):
    add_card(slide, titre, contenu, top=2.7,
             left=MARGIN_L + i * (card_w + GAP), width=card_w, height=3.0)

add_notes(slide,
    "- Demander à chaque participant de choisir SON premier réflexe (R24 — plan d'action)\n"
    "- « 3 réflexes, 30 secondes chacun, 90 % des problèmes couverts » (R15)\n"
    "- Clôturer avec énergie (R22 — neurones miroirs)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# FINALISATION
# ═══════════════════════════════════════════════════════════════
output_path = os.path.join(os.path.dirname(__file__), "accessibilite-word-dsfr.pptx")
finalize_pptx(prs, TITRES, output=output_path,
              title="Rendre un document Word accessible",
              subject="Formation accessibilité Word — 22 critères en 5 piliers")
