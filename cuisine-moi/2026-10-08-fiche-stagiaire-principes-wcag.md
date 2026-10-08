Fiche stagiaire - principes WCAG : notes cuisine-moi
===================================================

Date : 2026-10-08 | Objectif : redéfinir l'intention pédagogique du tableau des quatre questions en page 2/5.

## Résumé / décisions clés

- Le tableau actuel repose sur une mauvaise interprétation des couleurs des cartes.
- Sur les cartes, la couleur indique le niveau de conformité A, AA ou AAA ; elle n'indique pas le principe WCAG.
- Pour la formation, le niveau AAA n'est pas travaillé et la mention A/AA n'est probablement pas utile dans ce tableau.
- Le premier chiffre du critère indique le principe : 1 Perceptible, 2 Utilisable, 3 Compréhensible, 4 Robuste.
- Verbes d'action retenus : percevoir, utiliser, comprendre, fonctionner avec les outils.
- Le périmètre de réflexion est le tableau des quatre questions de la page 2/5 de la fiche stagiaire.
- La source éditable est `wcag/fiche-stagiaire-principes-wcag.md` ; le PDF est une sortie générée par `make pdf`.
- Le code couleur erroné vient d'une intention documentée dans la fiche formateur : réutiliser les couleurs des badges de personas. Cette convention entre en conflit avec celle des cartes, où la couleur code A, AA ou AAA.
- La slide « 4 principes pour tout retenir » utilise déjà les numéros 1 à 4 sans code couleur ; la slide « 6 profils, 4 questions » relie déjà les personas aux quatre principes.
- Décision : la page 2 sera un pont d'animation. Les quatre principes forment la boussole centrale et un décodage compact explique comment lire les cartes.
- Décision : le pont part d'un persona et suit le chemin `persona -> obstacle -> question/principe -> carte`.
- Décision : le décodage des cartes sera équilibré. Une carte exemple montrera les quatre couches utiles sans transformer la fiche en cours exhaustif.
- Décision affinée : les personas restent visibles dans la colonne « Qui est bloqué ? », mais ne servent plus de classement fixe des principes. Une note précise qu'un même persona peut être concerné par plusieurs principes.
- Décision affinée : le tableau conserve les colonnes pédagogiques « Question à se poser » et « Qui est bloqué si c'est absent ? », mais sans code couleur trompeur.
- Décision affinée : montrer trois parcours exemples après le tableau, puis faire construire les autres parcours pendant l'animation plutôt que de donner une correction exhaustive.
- Contrainte : la fiche doit rester sobre et claire.
- Décision : la colonne « Qui est bloqué ? » emploie une forme mixte courte associant le nom du persona et l'obstacle concret, avec une note indiquant qu'un persona peut relever de plusieurs principes.
- Décision : employer la double formulation compacte `repère + principe officiel -> action`, notamment `4.x Robuste -> fonctionner avec les outils`.
- Décision : conserver les trois exemples complémentaires proposés : Amir et l'image sans alternative (`1.x`, carte `1.1.1`), Agathe et la navigation impossible sans souris (`2.x`, carte `2.1.1`), Anaïs et le contraste insuffisant (`1.x`, carte `1.4.3`).
- Décision : présenter ces trois parcours au même niveau, sous le titre provisoire « Trois exemples pour démarrer », dans la forme compacte `persona + obstacle -> principe -> carte` ; la question n'est pas répétée dans chaque parcours puisqu'elle figure déjà dans le tableau.
- Décision : décoder la carte dans un encart textuel, avec `1.1.1` très visible, plutôt qu'avec une miniature annotée. Les cartes physiques étant manipulées pendant l'animation, la fiche privilégie la lisibilité et la sobriété.
- Décision : faire apparaître les six personas des PPTX dans le tableau, puis développer seulement les trois parcours compacts Amir, Agathe et Anaïs sous le tableau. Justine, Anatole et Paul restent ainsi reliés à la boussole sans multiplier les parcours corrigés.
- Compréhension partagée confirmée par l'utilisateur ; passage à la modification de la source puis à la régénération du PDF autorisé.
- Mise en œuvre terminée : la page 2 réunit le tableau corrigé, les trois parcours et l'encart de décodage ; le PDF conserve cinq pages et déclare PDF/UA-1.

## Journal questions-réponses

### Contexte initial fourni
- Capture : la fiche ne traite actuellement ni la fonction pédagogique des étiquettes des cartes (tri, animation, badge métier, usage), ni les 13 directives classées par principes. Un lien entre slides, cartes WCAG et personas est envisagé mais non décidé.
- Drapeaux : finalité prioritaire du tableau ; place des étiquettes ; place des 13 directives ; lien éventuel avec les personas ; formulation du principe 4.

### Q1 - Fonction prioritaire de la page 2
- Question : la page 2 doit-elle d'abord être une boussole des quatre principes, un mode d'emploi des cartes, ou un pont d'activité entre persona, obstacle, principe et carte ?
- Capture : choix du pont d'animation. Les quatre principes restent la boussole centrale ; le décodage des cartes est présent mais très compact.
- Drapeaux : aucun sur la fonction principale.

### Q2 - Point de départ du pont
- Question : le chemin d'animation doit-il partir du persona, d'une situation de travail, ou d'une carte tirée par le groupe ?
- Capture : choix du persona comme point de départ. Chemin retenu : `persona -> obstacle -> question/principe -> carte`.
- Drapeaux : aucun sur le point de départ.

### Q3 - Profondeur du décodage des cartes
- Question : le décodage compact doit-il montrer seulement le repère numérique, ajouter la signification des étiquettes, ou expliquer toutes les couches d'une carte sans énumérer les 13 directives ?
- Capture : choix du décodage équilibré. Une carte exemple explique : premier chiffre = principe, intitulé = directive, couleur = niveau de conformité, étiquettes = pistes de tri par publics, métiers ou usages. Pas de liste des 13 directives ni de cours sur A/AA/AAA.
- Drapeaux : aucun sur la profondeur du décodage.

### Q4 - Place des personas dans la boussole
- Question : faut-il conserver une colonne de personas dans le tableau, déplacer les personas dans une consigne d'animation séparée, ou montrer un seul exemple de parcours ?
- Capture : décision initiale de ne plus associer rigidement un persona à un principe. Décision affinée ensuite : conserver les six personas dans la colonne « Qui est bloqué ? » comme exemples d'obstacles, avec une note signalant qu'un persona peut relever de plusieurs principes.
- Drapeaux : aucun sur la présence des personas dans le tableau.

### Q5 - Six parcours fournis ou construits
- Question : faut-il fournir six parcours terminés, donner un modèle puis faire construire les six parcours, ou ne conserver qu'un exemple dans la fiche et traiter les six parcours dans l'animation ?
- Capture : la piste initiale d'un parcours modèle a été affinée. La fiche fournit finalement trois parcours compacts au même niveau ; les autres associations restent à construire pendant l'animation. Le tableau conserve « Question à se poser » et « Qui est bloqué si c'est absent ? ».
- Drapeaux : aucun ; l'emplacement matériel des productions relève de l'animation, pas de cette page.

### Q6 - Forme de la colonne « Qui est bloqué ? »
- Question : cette colonne doit-elle citer les personas, décrire les situations fonctionnelles, ou combiner brièvement les deux ?
- Capture : choix de la forme mixte courte, par exemple « Amir - ne perçoit pas l'image » ou « Agathe - ne peut pas utiliser la souris ». Ajouter une note précisant qu'un persona peut apparaître dans plusieurs principes selon l'obstacle.
- Drapeaux : aucun sur la quatrième colonne.

### Q7 - Nom officiel et verbe d'action
- Question : le tableau doit-il afficher uniquement les verbes simples, uniquement les noms officiels des principes, ou les deux dans une formulation compacte ?
- Capture : choix de la double formulation compacte : « 1.x Perceptible -> percevoir », « 2.x Utilisable -> utiliser », « 3.x Compréhensible -> comprendre », « 4.x Robuste -> fonctionner avec les outils ».
- Drapeaux : aucun sur le vocabulaire central.

### Q8 - Parcours persona modèle
- Question : quel persona et quel obstacle doivent servir d'exemple entièrement résolu sous le tableau ?
- Capture : l'utilisateur retient Amir face à une image informative sans alternative, mais souhaite finalement montrer les trois parcours proposés : `Amir + image sans alternative -> 1.x Perceptible -> carte 1.1.1`, `Agathe + navigation impossible sans souris -> 2.x Utilisable -> carte 2.1.1`, `Anaïs + contraste insuffisant -> 1.x Perceptible -> carte 1.4.3`. Les trois exemples illustrent à la fois la transversalité, l'action et un contrôle mesurable.
- Drapeaux : résolu en Q9 : trois parcours au même niveau.

### Q9 - Hiérarchie des trois parcours
- Question : faut-il développer Amir et condenser Agathe et Anaïs, ou présenter les trois parcours compacts au même niveau ?
- Capture : choix des trois parcours compacts présentés au même niveau, sous un titre comme « Trois exemples pour démarrer ». La forme retenue évite de désigner Amir comme parcours canonique et limite la densité de la page.
- Drapeaux : aucun sur la hiérarchie des trois exemples.

### Q10 - Forme du décodage de la carte
- Question : faut-il utiliser une miniature annotée de la carte 1.1.1, un encart textuel ou une forme hybride ?
- Capture : choix de l'encart textuel, avec `1.1.1` très visible. La manipulation des cartes physiques assure déjà la reconnaissance visuelle ; la fiche reste un repère lisible.
- Drapeaux : aucun sur la forme du décodage.

### Q11 - Représentation des six personas
- Question : faut-il ne montrer que les trois personas des parcours, développer six parcours, ou conserver les six personas dans le tableau et seulement trois parcours exemples ?
- Capture : l'utilisateur juge pertinente la répartition recommandée : les six personas des PPTX restent visibles dans « Qui est bloqué ? », tandis que seuls Amir, Agathe et Anaïs font l'objet des trois parcours compacts. Cette structure préserve la continuité avec les slides sans alourdir la page.
- Drapeaux : résolu en Q12.

### Q12 - Validation de la compréhension partagée
- Question : la structure validée peut-elle maintenant être mise en œuvre dans la source puis régénérée en PDF ?
- Capture : oui. L'utilisateur autorise la modification de `wcag/fiche-stagiaire-principes-wcag.md` et la régénération du PDF stagiaire.
- Drapeaux : aucun.

## Mise en œuvre et vérification

- Source modifiée : `wcag/fiche-stagiaire-principes-wcag.md`.
- Livrable régénéré : `livrables-IGPDE-2026-102846/Livrables-Stagiaires/fil-rouge-principes-wcag-igpde/fiche-stagiaire-principes-wcag.pdf`.
- Rendu contrôlé visuellement : les trois blocs tiennent sur la page 2, sans modifier la pagination totale de cinq pages.
- Contrôle ciblé : PDF tagué, PDF/UA-1 déclaré, 12 tests PDF réussis.
- Contrôle global : 285 tests réussis ; un test sans lien échoue sur la fiche technique administrative déjà modifiée (`PDF Accessibility Checker 2024` absent).

## Drapeaux ouverts

- Aucun pour la fiche stagiaire WCAG.
