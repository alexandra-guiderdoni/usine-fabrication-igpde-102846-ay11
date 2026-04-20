#!/usr/bin/env python3
"""
Génération du PPTX DSFR : Rendre un document Word accessible — VERSION COURTE
15 slides (~30 min) — condensation Chain-of-Density de la version longue (30 slides)

Technique : chaque slide fusionne 2-3 sujets de la version longue.
Les 22 critères sont tous couverts, mais avec moins d'exemples et sans les quiz intermédiaires.
"""

import sys
import os

sys.path.insert(0, os.path.expanduser("~/Claude/.claude/skills/accessible-pptx/scripts"))
from dsfr_components import *

FOOTER = "Accessibilité Word — avril 2026"
TOTAL = 15
prs, TITRES = create_presentation("dsfr")


# ═══════════════════════════════════════════════════════════════
# SLIDE 1 — Titre + accroche
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Rendre un document Word accessible",
                  footer=FOOTER, page_number=1, total_pages=TOTAL)

add_highlight(slide,
    "22 critères en 5 piliers — version essentielle (~30 min)",
    top=1.6, height=0.8)

add_alert(slide, "Document A — inaccessible", [
    "Titres en gras manuellement, image sans texte alt,",
    'tableau fusionné, nom « Document1.docx »',
], top=2.7, left=MARGIN_L, width=COL_W, height=1.5, alert_type="error")

add_alert(slide, "Document B — accessible", [
    "Styles Titre 1/2, description fonctionnelle,",
    'tableau simple avec en-tête, nom descriptif',
], top=2.7, left=COL_R, width=COL_W, height=1.5, alert_type="success")

add_highlight(slide,
    "Visuellement identiques — seul le B est lisible par un lecteur d'écran.",
    top=4.5)

add_notes(slide,
    "- Demander : « Lequel choisissez-vous ? » (R9)\n"
    "- Révéler : la différence est invisible à l'oeil, structurelle uniquement\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 2 — Pourquoi + périmètre
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pourquoi ça vous concerne",
                  footer=FOOTER, page_number=2, total_pages=TOTAL)

kpi_w = (CONTENT_W - GAP * 2) / 3
for i, (val, lbl) in enumerate([
    ("15 %", "de la population\nen situation de handicap"),
    ("80 %", "des handicaps\nsont invisibles"),
    ("0", "ligne de code\nnécessaire"),
]):
    add_pave_chiffre(slide, val, lbl, top=1.4,
                     left=MARGIN_L + i * (kpi_w + GAP), width=kpi_w, height=1.5)

add_alert(slide, "Périmètre", [
    "Format .docx obligatoire (pas .doc ni .docm)",
    "Hors périmètre : macros, documents protégés, formulaires Word",
], top=3.3, left=MARGIN_L, width=CONTENT_W, height=1.2, alert_type="info")

add_highlight(slide,
    "L'accessibilité Word est 100 % éditoriale : pas de code, juste les bons réflexes dans le ruban.",
    top=4.8)

add_notes(slide,
    "- Sources : 15 % = OMS (2011, confirmé 2023) ; 80 % = DREES\n"
    "- « Vous produisez déjà des documents Word — il s'agit d'utiliser les bonnes fonctionnalités »\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 3 — Vue d'ensemble : 5 piliers
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "5 piliers, 22 critères",
                  footer=FOOTER, page_number=3, total_pages=TOTAL)

card_w = (CONTENT_W - GAP * 4) / 5
for i, (titre, contenu) in enumerate([
    ("Structure", "Titres, listes,\ncolonnes, tableaux\n\n6 critères"),
    ("Couleurs", "Contraste et\nsignification\n\n2 critères"),
    ("Contenus", "Images, liens,\nzones de texte\n\n5 critères"),
    ("Langue\net médias", "Balisage, médias,\nclignotement\n\n4 critères"),
    ("Finalisation", "Propriétés, nom,\nvérificateur\n\n5 critères"),
]):
    add_card(slide, titre, contenu, top=1.4,
             left=MARGIN_L + i * (card_w + GAP), width=card_w, height=2.8)

add_notes(slide,
    "- « On avance pilier par pilier, du plus structurant au plus fin » (R4)\n"
    "- « Le pilier Structure = 60 % de l'effort » (R11)\n"
    "- Timing : 1 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 4 — Pilier 1a : titres, listes, colonnes, sauts
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 1 — Structure du texte",
                  footer=FOOTER, page_number=4, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Besoin", "Fonctionnalité intégrée", "Piège courant"],
    [
        ["Titres", "Accueil > Styles > Titre 1, 2, 3", "Texte en gras manuellement"],
        ["Listes", "Accueil > Puces / Numérotation", "Tirets ou chiffres manuels"],
        ["Colonnes", "Mise en page > Colonnes", "Tabulations ou espaces"],
        ["Saut de page", "Insertion > Saut de page (Ctrl+Entrée)", "Retours chariot (Entrée x15)"],
    ],
    top=1.4, col_widths=[2.5, 5.0, 4.5])

add_callout(slide, "Vérification express", [
    "Titres : Ctrl+F > onglet Titres — tous les titres doivent y apparaître",
    "Listes : Maj+F1 — « Puces et numérotation » doit apparaître",
    "Colonnes : Maj+F1 — « Colonnes » doit apparaître sous « Section »",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=CONTENT_W, height=1.8)

add_notes(slide,
    "- « Imaginez lire un livre de 50 pages sans table des matières » (R7)\n"
    "- Exercice binôme : « Ouvrez un document, Maj+F1, cliquez sur une liste » (R17)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 5 — Pilier 1b : tableaux
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Tableaux de mise en page et de données",
                  footer=FOOTER, page_number=5, total_pages=TOTAL)

add_callout(slide, "Tableau de mise en page (pas d'en-têtes)", [
    "Insertion > Tableau > remplir gauche à droite, haut en bas",
    "Vérifier : Tab parcourt les cellules dans l'ordre visuel",
    "Habillage du texte = « Aucun » (clic droit > Propriétés > Tableau)",
], top=1.4, left=MARGIN_L, width=COL_W, height=2.2)

add_callout(slide, "Tableau de données (en-têtes obligatoires)", [
    "Insertion > Tableau — jamais d'image de tableau",
    "Pas de cellules fusionnées ni divisées",
    "1re ligne > clic droit > Propriétés > Ligne > Répéter en tant que ligne d'en-tête",
    "Habillage du texte = « Aucun »",
], top=1.4, left=COL_R, width=COL_W, height=2.2)

add_alert(slide, "Limitation", [
    "Les tableaux complexes (multi-niveaux, cellules fusionnées) ne peuvent pas être",
    "rendus accessibles dans Word — convertir en PDF accessible.",
], top=3.9, left=MARGIN_L, width=CONTENT_W, height=1.2, alert_type="warning")

add_notes(slide,
    "- Distinguer les deux types : mise en page (organisation) vs données (en-têtes nécessaires)\n"
    "- « Répéter en tant que ligne d'en-tête » : invisible visuellement, capital pour les TA\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 6 — Pilier 2 : couleurs
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 2 — Couleurs et contraste",
                  footer=FOOTER, page_number=6, total_pages=TOTAL)

tbl_h = add_tableau(slide,
    ["Type de texte", "Ratio minimum", "Outil"],
    [
        ["Standard (< 14 pt gras)", "4,5:1", "Colour Contrast Analyser (CCA)"],
        ["Grande taille (>= 14 pt gras / >= 18 pt)", "3:1", "Pipette premier plan + arrière-plan"],
    ],
    top=1.4, col_widths=[4.5, 3.0, 4.5])

add_alert(slide, "Inaccessible", [
    "Statut en rouge/vert/jaune uniquement",
    "Un daltonien voit 3 couleurs identiques",
], top=1.4 + tbl_h + 0.3, left=MARGIN_L, width=COL_W, height=1.5, alert_type="error")

add_alert(slide, "Accessible", [
    "Statut en texte : « En retard / Terminé / En cours »",
    "La couleur renforce, le texte porte le sens",
], top=1.4 + tbl_h + 0.3, left=COL_R, width=COL_W, height=1.5, alert_type="success")

add_highlight(slide,
    "Texte noir sur fond blanc = toujours conforme. 8 % des hommes sont daltoniens.",
    top=1.4 + tbl_h + 0.3 + 1.5 + 0.3)

add_notes(slide,
    "- Source daltonisme : Colour Blind Awareness, population masculine européenne\n"
    "- Règle simple : « imprimez en noir et blanc — l'info est-elle compréhensible ? »\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 7 — Pilier 3a : texte alt + objets décoratifs + alignement
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 3 — Images et objets",
                  footer=FOOTER, page_number=7, total_pages=TOTAL)

add_stepper(slide, [
    "Image significative :\nclic droit > Texte de\nremplacement >\ndécrire la FONCTION",
    "Image décorative :\nespaces vides dans\nle champ Description\n(ou « Marquer décoratif »)",
    "Tout objet :\naligner sur le texte\n(Format > Position)\nSinon = invisible",
], top=1.4, step_height=2.8)

add_alert(slide, "Mauvais texte alt", [
    '"Photo d\'un graphique en barres colorées"',
], top=4.5, left=MARGIN_L, width=COL_W, height=0.9, alert_type="error")

add_alert(slide, "Bon texte alt", [
    '"Chiffre d\'affaires 2020-2024 : hausse de 15 % à 23 %"',
], top=4.5, left=COL_R, width=COL_W, height=0.9, alert_type="success")

add_notes(slide,
    "- Test mental : « Si je remplace l'image par le texte alt, le document reste compréhensible ? »\n"
    "- Objet flottant = objet invisible pour le lecteur d'écran\n"
    "- Zones de texte : les éviter si possible, sinon aligner sur le texte\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 8 — Pilier 3b : liens + infos essentielles
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Liens et informations essentielles",
                  footer=FOOTER, page_number=8, total_pages=TOTAL)

add_alert(slide, "Liens inaccessibles", [
    '"Cliquez ici", "En savoir plus", URL brute',
], top=1.4, left=MARGIN_L, width=COL_W, height=1.2, alert_type="error")

add_alert(slide, "Liens accessibles", [
    '"Consulter le guide d\'accessibilité Word"',
    "Méthode : sélectionner le texte > Ctrl+K > coller l'URL",
], top=1.4, left=COL_R, width=COL_W, height=1.2, alert_type="success")

add_callout(slide, "En-têtes, pieds de page, filigranes : invisibles pour les TA", [
    "Les technologies d'assistance ne lisent pas ces zones automatiquement",
    "Si l'information est essentielle (« CONFIDENTIEL », date limite),",
    "la reproduire dans le corps du document, idéalement au début",
], top=2.9, left=MARGIN_L, width=CONTENT_W, height=2.0)

add_highlight(slide,
    "Supprimer le dernier caractère du texte d'un lien supprime le lien entier — attention.",
    top=5.2)

add_notes(slide,
    "- « Un utilisateur de lecteur d'écran navigue de lien en lien » (R7)\n"
    "- Le filigrane « CONFIDENTIEL » est invisible pour 15 % des lecteurs\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 9 — Pilier 4 : langue + médias + clignotants
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 4 — Langue, médias, clignotement",
                  footer=FOOTER, page_number=9, total_pages=TOTAL)

add_callout(slide, "Balisage de langue", [
    "Langue principale : Fichier > Options > Langue",
    "Passage étranger : sélectionner > Révision > Langue > Définir la langue",
    'Sans balisage, "meeting" est prononcé "mé-é-ting" par le lecteur d\'écran',
], top=1.4, left=MARGIN_L, width=COL_W, height=2.2)

tbl_h = add_tableau(slide,
    ["Média", "Alternative"],
    [
        ["Audio seul", "Transcription textuelle"],
        ["Vidéo seule", "Description textuelle"],
        ["Audio + vidéo", "Sous-titres + description audio"],
    ],
    top=1.4, left=COL_R, width=COL_W, col_widths=[2.5, 3.335])

add_alert(slide, "Objets clignotants : interdit absolu", [
    "GIF avec flashs, animations > 3 Hz = risque de crise d'épilepsie",
    "Un seul objet clignotant = document non accessible, sans exception",
], top=4.0, left=MARGIN_L, width=CONTENT_W, height=1.3, alert_type="error")

add_notes(slide,
    "- Si vous hésitez sur un GIF animé : remplacez-le par une image statique\n"
    "- La plupart des documents contiennent au moins un anglicisme à baliser\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 10 — Pilier 5 : finalisation + vérificateur
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Pilier 5 — Finalisation",
                  footer=FOOTER, page_number=10, total_pages=TOTAL)

add_stepper(slide, [
    "Propriétés :\nFichier > Informations\n> Titre, Auteur",
    "Nom de fichier :\ndescriptif + .docx",
    "Protection :\naucune restriction",
    "Formulaires :\naucun champ Word",
    "Vérificateur :\nFichier > Vérifier\nl'accessibilité",
], top=1.4, step_height=2.5)

add_alert(slide, "Le vérificateur détecte", [
    "Texte alt manquant, objets non alignés, titres absents, tableaux sans en-tête",
], top=4.2, left=MARGIN_L, width=COL_W, height=1.2, alert_type="success")

add_alert(slide, "Il ne détecte PAS", [
    "Qualité du texte alt, noms de liens, couleur porteuse de sens, langue",
], top=4.2, left=COL_R, width=COL_W, height=1.2, alert_type="warning")

add_highlight(slide,
    "Le vérificateur est un premier filtre, pas un certificat de conformité.",
    top=5.7)

add_notes(slide,
    "- Ces 5 vérifications prennent 2 minutes (R12 — WIIFM)\n"
    "- Analogie : « Le correcteur orthographique attrape les fautes, pas le style » (R7)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 11 — Étude de cas
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Étude de cas : un document de A à Z",
                  footer=FOOTER, page_number=11, total_pages=TOTAL)

add_callout(slide, "Sophie doit publier un compte rendu de réunion", [
    "3 niveaux de titres, 2 tableaux, 1 organigramme, 1 lien, filigrane « CONFIDENTIEL »",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=1.2)

tbl_h = add_tableau(slide,
    ["Étape", "Action", "Pilier"],
    [
        ["1", "Applique Titre 1, 2, 3 via Accueil > Styles", "Structure"],
        ["2", "Identifie la ligne d'en-tête de chaque tableau", "Structure"],
        ["3", "Texte alt fonctionnel sur l'organigramme", "Contenus"],
        ["4", "Renomme « cliquez ici » en description claire", "Contenus"],
        ["5", "Ajoute « CONFIDENTIEL » au début du document", "Contenus"],
        ["6", "Renseigne Titre et Auteur dans Fichier > Informations", "Finalisation"],
        ["7", "Lance le vérificateur, corrige les 2 erreurs restantes", "Finalisation"],
    ],
    top=2.9, col_widths=[1.0, 7.5, 3.5])

add_notes(slide,
    "- Sophie est le héros, le document inaccessible est le conflit (R6 — storytelling)\n"
    "- « En 7 étapes et 10 minutes, Sophie a rendu son document accessible »\n"
    "- « Combien de ces étapes faites-vous déjà ? » (R25 — métacognition)\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 12 — Quiz final
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Quiz : trouvez les 5 erreurs",
                  footer=FOOTER, page_number=12, total_pages=TOTAL)

add_callout(slide, "Un document Word contient :", [
    "1. Un titre « Introduction » mis en gras Arial 16 (sans style)",
    "2. Un tableau de 3 colonnes sans « Répéter en tant que ligne d'en-tête »",
    '3. Un lien « cliquez ici pour le formulaire »',
    "4. Un filigrane « PROJET » sans mention dans le corps",
    "5. Une photo de l'équipe sans texte alternatif",
], top=1.4, left=MARGIN_L, width=CONTENT_W, height=3.2)

add_highlight(slide,
    "Réponse : 5 erreurs, une par point. Si vous les avez toutes, vous maîtrisez les 5 piliers.",
    top=4.9)

add_notes(slide,
    "- Faire compter individuellement puis partager (R14 — récupération active)\n"
    "- Parcourir chaque erreur et rappeler le pilier\n"
    "- Timing : 3 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 13 — Matrice effort/impact
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Par où commencer ?",
                  footer=FOOTER, page_number=13, total_pages=TOTAL)

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
    "Commencez par le quadrant haut-gauche : 4 actions à effort faible, impact maximal.",
    top=1.4 + tbl_h + 0.3)

add_notes(slide,
    "- « Si vous ne retenez qu'une chose : les styles de titre » (R2 — primauté)\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 14 — Checklist 21 critères
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Checklist : vos 21 critères",
                  footer=FOOTER, page_number=14, total_pages=TOTAL)

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
    "- Distribuer en version imprimée ou numérique\n"
    "- « Imprimez-la, collez-la à côté de votre écran » (R26)\n"
    "- Timing : 1 min")


# ═══════════════════════════════════════════════════════════════
# SLIDE 15 — Demain à 9h
# ═══════════════════════════════════════════════════════════════
slide = new_slide(prs, TITRES, "Demain à 9h",
                  footer=FOOTER, page_number=15, total_pages=TOTAL)

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
    "- Chaque participant choisit SON premier réflexe (R24 — plan d'action)\n"
    "- « 3 réflexes, 30 secondes chacun, 90 % des problèmes couverts »\n"
    "- Timing : 2 min")


# ═══════════════════════════════════════════════════════════════
# FINALISATION
# ═══════════════════════════════════════════════════════════════
output_path = os.path.join(os.path.dirname(__file__), "accessibilite-word-dsfr-court.pptx")
finalize_pptx(prs, TITRES, output=output_path,
              title="Rendre un document Word accessible — version essentielle",
              subject="Formation accessibilité Word — 22 critères, 15 slides")
