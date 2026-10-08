Tableau de liaison de l'atelier Word : notes cuisine-moi
=======================================================

Date : 2026-10-08 | Objectif : concevoir un tableau complémentaire reliant le déroulé des slides Word, les manipulations, la checklist et les cartes WCAG sans recopier la checklist.

## Résumé / décisions clés

- Le tableau rapide « Pendant l'atelier Word » est conservé comme vue synthétique centrée sur les réflexes et les personas.
- Un tableau complémentaire doit suivre l'ordre pédagogique des slides et soutenir la boucle `slide -> point expliqué -> manipulation Word -> checklist -> carte WCAG`.
- Les références de checklist doivent employer les identifiants canoniques `P-01` à `P-20`, `C-01` à `C-02` et `S-01` à `S-05`.
- Les références WCAG seront présentées comme des correspondances pédagogiques lorsqu'elles sont pertinentes, et non comme une déclaration de conformité directe d'un fichier DOCX aux WCAG.
- La checklist contient 27 contrôles répartis en 5 stations ; les slides regroupent déjà ces contrôles en séquences thématiques plus compactes.
- Contrainte : compléter la checklist sans la recopier intégralement et conserver une fiche sobre et claire.
- Décision : le tableau complémentaire comporte une ligne par séquence pédagogique, soit environ 13 lignes, et regroupe les références de checklist associées.
- Décision : le tableau complémentaire est une table de liaison à quatre colonnes : `Séquence / point présenté | Action dans Word | Checklist | Carte(s) WCAG`.
- Décision : l'observation utile est formulée brièvement dans la colonne « Action dans Word » ; aucune colonne « Preuve », « Persona » ou « Question » n'est ajoutée.
- Décision : chaque bloc affiche la station ; la première colonne affiche le numéro réel de la slide graphique projetée et l'intitulé de la séquence. Les numéros du déroulé sont considérés comme stabilisés.
- Décision : la colonne WCAG affiche `numéro + intitulé court` lorsqu'une correspondance solide existe, par exemple `1.3.1 - Informations et relations`.
- Décision : une séquence sans correspondance suffisamment directe porte la mention explicite « Pas de carte directe » ; aucun critère WCAG n'est forcé.
- Décision : les contrôles signalés `S-01` à `S-05` sont regroupés dans la dernière ligne du bloc de la station 5, intitulée « Contrôles signalés avant diffusion » et présentée comme une vérification sans manipulation obligatoire pendant l'atelier.
- Décision : le tableau couvre uniquement les 13 séquences opérationnelles du module Word. Dans le deck complet, leurs numéros sont 61, 62, 64 à 66, 68 à 70, 72, 73, 75, 76 et 79.
- Décision : les slides d'ouverture de station, de quiz et de synthèse ne créent pas de lignes sans action ni référence de checklist.
- Décision : lorsqu'une séquence réunit des contrôles ayant des rattachements WCAG différents, la cellule détaille la correspondance par identifiant de checklist, par exemple `P-15 -> 3.1.1, 3.1.2 ; P-16 -> Pas de carte directe`.
- Décision : cette correspondance détaillée est réservée aux cellules mixtes des slides 72, 75, 76 et 79 ; les autres cellules WCAG restent compactes.
- Décision : sous la section « Pendant l'atelier Word », le tableau actuel est présenté comme « Les réflexes essentiels » et le tableau complémentaire comme « Le fil de l'atelier Word », avec la légende « Slides, actions, checklist et cartes WCAG ».
- Contrainte technique vérifiée : les tableaux de la fiche sont configurés pour rester entiers sur une page, car leur fragmentation entre deux pages provoquait un échec PDF/UA-1 avec WeasyPrint. Une table unique de 13 lignes et quatre colonnes serait trop haute ou exigerait une réduction excessive du texte.
- Décision : le fil reste conceptuellement unique, mais il est matérialisé par cinq tableaux courts, un par station, afin de préserver la lisibilité et la génération PDF/UA-1.
- Autorisation : l'utilisateur demande de mettre en œuvre cette proposition, de régénérer le PDF et de conserver la possibilité de revenir en arrière si le résultat ne lui convient pas.
- Mise en œuvre : la fiche conserve le tableau rapide sous « Les réflexes essentiels » et ajoute « Le fil de l'atelier Word » sous la forme de cinq tableaux, pour un total de 13 séquences opérationnelles.
- Mise en œuvre : le PDF généré compte 7 pages ; le nouveau contenu occupe les pages 3 à 5 et le rendu a été contrôlé visuellement.
- Vérification : le générateur annonce PDF/UA-1, l'audit éditorial HTML ne signale aucun problème, 21 tests ciblés PDF/fabrication réussissent et les 12 tests PDF sont confirmés après l'installation du rendu final.
- Vérification globale : 286 tests réussissent ; l'unique échec concerne l'absence antérieure de « PDF Accessibility Checker 2024 » dans la fiche technique administrative, hors périmètre de cette proposition.
- Fraîcheur du pack : la fiche WCAG est à jour ; le contrôle global reste bloqué par les trois documents Sami, plus anciens que leur générateur, hors périmètre de cette proposition.

## Journal questions-réponses

### Q1 - Granularité du tableau complémentaire
- Question : faut-il organiser le tableau par contrôle de checklist, par station ou par séquence pédagogique correspondant à un groupe de slides et de manipulations ?
- Capture : choix d'une ligne par séquence pédagogique. Cette granularité intermédiaire permet de couvrir tous les contrôles par regroupements, de respecter le déroulé des slides et de préserver la sobriété de la fiche.
- Drapeaux : résolu - 13 séquences opérationnelles.

### Q2 - Colonnes et fonction du tableau
- Question : faut-il privilégier une table de liaison en quatre colonnes, ajouter une colonne de preuve ou réintroduire les personas et les questions du tableau rapide ?
- Capture : choix de la table de liaison en quatre colonnes : `Séquence / point présenté | Action dans Word | Checklist | Carte(s) WCAG`. L'observation attendue reste intégrée en quelques mots dans l'action afin d'éviter une cinquième colonne et toute répétition du tableau rapide.
- Drapeaux : aucun sur la structure des colonnes.

### Q3 - Repérage des slides
- Question : faut-il identifier les séquences par numéro et titre, par station et intitulé sans numéro, ou par un intitulé générique ?
- Capture : choix de `numéro de slide + station + intitulé de la séquence`. L'utilisateur précise qu'il s'agit des slides graphiques projetées et que leur ordre ne va pas bouger.
- Drapeaux : résolu - numéros 61, 62, 64 à 66, 68 à 70, 72, 73, 75, 76 et 79.

### Q4 - Correspondances WCAG absentes ou indirectes
- Question : faut-il laisser un tiret, indiquer « Pas de carte directe » ou afficher seulement un principe général lorsqu'aucune correspondance WCAG solide n'existe ?
- Capture : choix de la mention « Pas de carte directe ». Lorsqu'une correspondance existe, la cellule affiche le numéro et l'intitulé court de la carte. Les critères ne sont pas forcés pour remplir toutes les lignes.
- Drapeaux : résolu à partir des cartes WCAG fournies et de la matrice canonique du TP.

### Q5 - Contrôles signalés
- Question : faut-il intégrer `S-01` à `S-05` dans une dernière ligne du tableau principal, les placer dans un encart séparé ou renvoyer uniquement vers la checklist ?
- Capture : choix d'une dernière ligne dans le tableau principal : « Contrôles signalés avant diffusion », avec `S-01` à `S-05`. Cette ligne conserve la complétude et l'ordre des slides tout en indiquant qu'aucune manipulation n'est obligatoire pendant le TP.
- Drapeaux : aucun sur la présence des contrôles signalés.

### Q6 - Périmètre des slides
- Question : faut-il couvrir seulement les 13 séquences opérationnelles, ajouter les cinq ouvertures de station ou reprendre les 27 slides du module Word ?
- Capture : choix des 13 séquences opérationnelles avec leurs numéros réels. Le tableau commence à la première manipulation et suit l'ordre des slides utiles sans devenir un second sommaire du deck.
- Drapeaux : aucun sur le périmètre des slides.

### Q7 - Correspondances dans les séquences mixtes
- Question : faut-il afficher une liste globale de cartes, détailler le rattachement contrôle par contrôle dans les seules cellules mixtes ou scinder ces séquences en plusieurs lignes ?
- Capture : choix du détail dans les seules cellules mixtes. Les lignes restent organisées par séquence pédagogique, mais les slides 72, 75, 76 et 79 indiquent quel contrôle possède une carte directe et lequel n'en possède pas.
- Drapeaux : aucun sur la présentation des correspondances mixtes.

### Q8 - Hiérarchie des titres
- Question : faut-il nommer le second tableau « Le fil de l'atelier Word », « Du support à la checklist » ou « Slides, checklist et cartes WCAG » ?
- Capture : choix de la hiérarchie recommandée : section « Pendant l'atelier Word », tableau actuel « Les réflexes essentiels », nouveau tableau « Le fil de l'atelier Word » et légende « Slides, actions, checklist et cartes WCAG ».
- Drapeaux : aucun sur les titres.

### Q9 - Découpage matériel du fil
- Question : faut-il produire cinq tableaux par station, trois tables de continuation ou une table unique réduite ou fragmentée ?
- Capture : choix d'un seul fil de l'atelier matérialisé par cinq petits tableaux, un par station. L'utilisateur autorise la réalisation de la proposition et souhaite pouvoir la révoquer après examen du rendu.
- Drapeaux : résolu - 7 pages, nouveau fil réparti sur les pages 3 à 5, sans tableau fragmenté.

## Drapeaux ouverts

- Validation visuelle et pédagogique de la proposition finale -> utilisateur.
