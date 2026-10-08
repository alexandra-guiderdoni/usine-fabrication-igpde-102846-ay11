Section « Pendant l'atelier web » : notes cuisine-moi
=====================================================

Date : 2026-10-08 | Objectif : restructurer la section web de la fiche stagiaire pour la relier explicitement aux 13 points du site d'exercice et aux cartes WCAG.

## Résumé / décisions clés

- Demande 1 : afficher explicitement les points `#1` à `#13` du site d'exercice.
- Demande 2 : donner pour chaque point la ou les références WCAG correspondantes.
- Demande 3 : conserver strictement l'ordre du site, de `#1` à `#13`.
- Fait vérifié : le tableau actuel comporte 11 lignes et omet `#5 Lien d'évitement` et `#11 Audiodescription`.
- Décision : remplacer le tableau actuel par une table de liaison unique de 13 lignes et quatre colonnes : `# et point du site | Ce que je vérifie | Qui est bloqué ? | Carte(s) WCAG`.
- Décision : rendre les intitulés `#1` à `#13` cliquables.
- Décision : chaque intitulé ouvre directement la page correspondante du site à auditer.
- Décision : la colonne WCAG affiche le critère principal avec son intitulé, puis les références associées sous forme compacte.
- Décision : le parcours unique est matérialisé par quatre petits tableaux thématiques, dans l'ordre `#1` à `#13` : contenus et structure (`#1` à `#4`), navigation et lecture (`#5` à `#8`), médias (`#9` à `#11`) et formulaires (`#12` à `#13`).
- Décision : « Ce que je vérifie » est formulé comme une question courte, concrète et directement testable.
- Décision antérieure conservée : « Qui est bloqué ? » utilise une forme mixte courte, par exemple `Amir - ne perçoit pas l'image`.
- Décision : le lien affiche le numéro et le nom complet du point de contrôle, par exemple `#1 - Texte alternatif des images`, et ouvre le scénario correspondant du site à auditer.
- Décision : afficher sous chaque intitulé la ou les slides visuelles correspondantes du PPTX, sans ajouter de cinquième colonne.
- Correspondance vérifiée dans le PPTX généré : `#1` slides 84 à 86 ; `#2` slide 87 ; `#3` slides 88 et 89 ; `#4` slides 90 et 91 ; `#5` slide 92 ; `#6` slides 93 à 96 ; `#7` slide 97 ; `#8` slide 98 ; `#9` slides 99 et 100 ; `#10` slide 101 ; `#11` slide 102 ; `#12` slides 105 à 107 ; `#13` slide 108.
- Correspondances vérifiées dans la grille canonique :
  - `#1` : **1.1.1 - Contenu non textuel**.
  - `#2` : **2.4.2 - Titre de page**.
  - `#3` : **2.4.6 - En-têtes et étiquettes** ; associé : `1.3.1`.
  - `#4` : **1.4.3 - Contraste (minimum)** ; associé : `1.4.11`.
  - `#5` : **2.4.1 - Contourner des blocs**.
  - `#6` : **2.4.7 - Visibilité du focus** ; associés : `2.1.1`, `2.1.2`, `2.4.3`.
  - `#7` : **3.1.1 - Langue de la page** ; associé : `3.1.2`.
  - `#8` : **1.4.4 - Redimensionnement du texte** ; associé : `1.4.10`.
  - `#9` : **1.2.2 - Sous-titres (pré-enregistrés)**.
  - `#10` : **1.2.1 - Contenus seulement audio et seulement vidéo pré-enregistrés**.
  - `#11` : **1.2.5 - Audiodescription (pré-enregistrée)** ; associé : `1.2.3`.
  - `#12` : **3.3.2 - Étiquettes ou instructions** ; associés : `1.3.1`, `2.5.3`.
  - `#13` : **3.3.2 - Étiquettes ou instructions** ; associés : `3.3.1`, `3.3.3`.
- Contrainte : conserver une fiche sobre et lisible, sans créer un tableau trop large.

## Journal questions-réponses

### Q1 - Architecture du tableau
- Question : faut-il privilégier une table de liaison en quatre colonnes, une table en cinq colonnes conservant « Principe » et « Réflexe », ou deux tableaux distincts ?
- Capture : choix de la table de liaison en quatre colonnes, avec 13 lignes dans l'ordre du site et les intitulés numérotés cliquables. La colonne « Principe » est remplacée par les références précises aux cartes WCAG ; le réflexe est intégré dans « Ce que je vérifie ».
- Drapeaux : destination exacte des liens à décider.

### Q2 - Destination des liens
- Question : faut-il ouvrir directement la page correspondante du site à auditer, revenir à la page d'accueil des 13 points ou proposer plusieurs destinations par ligne ?
- Capture : choix d'un lien direct depuis chaque intitulé numéroté vers la page correspondante du site à auditer. Cette destination soutient le déroulé du TP sans exposer prématurément l'aide ou la correction.
- Drapeaux : aucun sur la destination des liens.

### Q3 - Niveau de détail WCAG
- Question : faut-il afficher un seul critère principal, tous les critères avec leurs intitulés complets, ou un critère principal nommé suivi de références associées compactes ?
- Capture : choix du critère principal avec son intitulé, suivi des références associées sous forme compacte. Cette convention conserve un point d'entrée lisible tout en couvrant les correspondances directes utiles à l'exercice.
- Drapeaux : sélection du critère principal à vérifier pour chacun des 13 points dans les sources canoniques.

### Q4 - Découpage matériel du parcours
- Question : faut-il conserver un tableau unique potentiellement fragmenté, deux grands tableaux ou quatre petits tableaux thématiques dans l'ordre du site ?
- Capture : choix d'un seul parcours matérialisé par quatre tableaux : `#1` à `#4` contenus et structure, `#5` à `#8` navigation et lecture, `#9` à `#11` médias, `#12` à `#13` formulaires. Ce découpage préserve l'ordre, la lisibilité et le contournement PDF/UA qui maintient chaque tableau entier.
- Drapeaux : aucun sur le découpage.

### Q5 - Formulation de la vérification
- Question : faut-il rédiger chaque vérification comme une question courte, une consigne d'action ou une preuve attendue ?
- Capture : choix d'une question courte, concrète et directement testable pour chacun des 13 points. Cette formulation prolonge la logique de la boussole WCAG sans recopier la grille d'audit.
- Drapeaux : aucun sur la formulation des questions.

### Q6 - Libellé cliquable du point
- Question : faut-il afficher le nom complet du point de contrôle, un nom très court ou le titre du scénario du site ?
- Capture : choix du numéro suivi du nom complet du point de contrôle. Le lien reste autonome et explicite, tandis que sa destination ouvre le scénario correspondant dans le site à auditer.
- Drapeaux : aucun sur le libellé des liens.

### Q7 - Références aux slides visuelles
- Question : faut-il aussi relier chaque point Web aux slides visuelles correspondantes du PPTX ?
- Capture : oui. La référence est placée sous l'intitulé du point dans la première colonne afin de préserver les quatre colonnes et la largeur du tableau.
- Drapeaux : aucun sur les références aux slides.

## Drapeaux ouverts

- Aucun. Cadrage validé par l'utilisateur avant réalisation.
