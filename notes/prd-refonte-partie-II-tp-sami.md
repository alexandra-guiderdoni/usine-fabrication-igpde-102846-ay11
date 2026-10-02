<!-- PDG-LARGE-FILE-JUSTIFICATION: cette spécification unique doit relier les décisions pédagogiques, les livrables générés et leurs preuves afin d’éviter une nouvelle divergence entre le deck, les DOCX, la checklist, les mémos et le pack. -->

# PRD — Refonte de la partie II et du TP Sami

Statut : validé humainement le 1er octobre 2026 ; T01 à T15 terminés le
2 octobre 2026, avec relecture humaine finale reportée sur T16.
Date de cadrage : 1er octobre 2026.
Session cible : 9 octobre 2026.
Paquet de repli : tag `avant-refonte-tp-sami-2026-10-01`.
Implémentation : T01 à T15 terminés ; T09a annulé faute de binôme disponible ;
T16 reste à exécuter. Le dernier contrôle de `make pack` signale encore les
quatre installeurs externes absents du dépôt.

Par décision explicite d'Alex le 2 octobre 2026, l'état de T01 à T09 peut être
fusionné dans `main` et T10 peut commencer sans exécution de T09a, faute de
binôme novice disponible. Le protocole T09a reste archivé comme procédure, mais
ses contrôles humains sont reportés sur T16. Cette exception n'autorise pas la
remise du nouveau paquet à l'IGPDE. Le tag de repli reste immuable.

## 1. Mission

Remplacer la partie II fragmentée par un TP guidé de 90 minutes où chaque binôme rend accessible un document Word qui explique lui-même comment rendre un document Word accessible. La théorie, la manipulation, la vérification et la synthèse doivent avancer ensemble.

### Verrou d’objectif

Le chantier doit produire un parcours utilisable par des communicants débutants, pas une démonstration technique exhaustive de Word ni un audit de conformité documentaire.

### Résultat observable

À la fin de la séquence, chaque binôme dispose :

- d’un DOCX corrigé par ses soins ;
- d’une checklist renseignée ;
- d’un PDF exporté avec les options d’accessibilité puis contrôlé ;
- du corrigé de référence, qui sert ensuite de guide pratique autonome.

Les trois DOCX portent la même information éditoriale et les mêmes exemples. Seuls diffèrent les défauts d’accessibilité, les commentaires d’aide et leur correction ; le corrigé n’introduit aucune règle ou procédure nouvelle.

## 2. Problème à résoudre

Le dispositif actuel sépare les apports, l’exercice Sami, le retour sur des erreurs cachées, le quiz final et quatre slides de checklist. Sa spécification décrit encore 25 minutes, 21 critères et une identification sans checklist. Les critères du générateur, du mémo, des slides et de la checklist ne se superposent pas. Le déroulé IGPDE conserve par ailleurs une synthèse générale de la matinée de 12 h à 12 h 15, dont le contenu doit être réconcilié avec le nouveau TP.

La fragmentation interne à la partie II rend le temps irréaliste, affaiblit le transfert et permet aux sources générées de diverger.

## 3. Publics et usages

- Stagiaire : apprend dans Word sous Windows, suit les pistes ou choisit le parcours autonome, produit et vérifie ses fichiers.
- Formateurs : introduisent chaque station, aident sans corriger à la place du binôme et synthétisent au fil de l’eau.
- Préparateur IGPDE : assure l’installation des outils, distribue les fichiers et contrôle la cohérence du paquet.
- Mainteneur : intervient sur une source canonique, régénère les sorties et obtient des tests qui signalent toute dérive.

## 4. Décisions normatives

- La partie II DOIT durer 90 minutes ; ses synthèses techniques sont incluses dans les stations.
- Elle NE DOIT PAS contenir de quiz final ni reporter son débrief pédagogique après 12 h.
- La synthèse générale de la matinée DOIT être maintenue de 12 h à 12 h 15, hors du minutage de la partie II, sans quiz final.
- Le quiz diagnostic Documents A/B est maintenu comme première activité du préambule et inclus dans ses cinq minutes. Il pose le message « l’accessibilité ne se voit pas : elle se manipule et se vérifie ». Ce périmètre conservé comprend `scripts/slides/05_quiz-flash-a-vs-b.py`, `scripts/slides/05a_quiz-flash-reponse.py`, le bloc « Réponse au quiz » de `scripts/slides/06_pourquoi-concerne.py` et `tests/test_quiz_documents_sequence.py`.
- La checklist DOIT être disponible dès le début et renseignée après chaque station.
- Les cartes WCAG 2.2 DOIVENT être utilisées comme mise en relation informelle, jamais comme évaluation.
- Chaque binôme DOIT traiter tout le socle pratique.
- Le DOCX avec pistes est le fichier conseillé ; le DOCX inaccessible est une variante autonome librement choisie.
- Les deux fichiers de départ DOIVENT contenir les mêmes défauts et conduire aux mêmes preuves.
- Le corrigé complet NE DOIT être révélé qu’à la fin.
- Word bureau sous Windows est l’environnement principal. Writer sous Windows DOIT apparaître en complément compact sur les slides et de façon détaillée dans le guide.
- Un résultat « zéro erreur » du vérificateur est une cible, jamais une preuve de conformité.
- La vérification humaine et la checklist restent obligatoires après les outils automatiques.

## 5. Séquence de 90 minutes

Le minutage comprend les consignes, les manipulations et les synthèses intermédiaires.

1. **Préambule — 5 minutes** : quiz diagnostic Documents A/B et message « l’accessibilité ne se voit pas : elle se manipule et se vérifie », puis ouverture des fichiers, mission, livrables, choix du fichier de départ, checklist et rapprochement informel avec les cartes WCAG.
2. **Station 1 — 17 minutes : structurer et naviguer**.
3. **Station 2 — 15 minutes : rendre les contenus et les liens compréhensibles**.
4. **Station 3 — 15 minutes : sécuriser couleurs, graphiques et tableaux**.
5. **Station 4 — 15 minutes : régler langues et lisibilité**.
6. **Station 5 — 18 minutes : finaliser, vérifier, exporter et contrôler**.
7. **Marge et remise — 5 minutes** : absorber un léger retard, enregistrer les productions, recevoir le corrigé et noter les alertes restant à approfondir.

Le premier essai chronométré PEUT déplacer jusqu’à trois minutes entre stations, mais le total NE DOIT PAS dépasser 90 minutes.

De 12 h à 12 h 15, une synthèse distincte consolide l’ensemble de la matinée et prépare la transition vers l’après-midi. Elle ne prolonge pas les manipulations du TP.

## 6. Matrice de couverture pédagogique

La source canonique doit attribuer un identifiant stable et un niveau à chaque contrôle :

- `P` pratiqué : le binôme réalise une action dans Word, sur le DOCX ou sur une sortie du DOCX, et en produit la preuve ;
- `C` contrôlé : le binôme exécute un outil ou une vérification humaine et consigne le résultat ;
- `S` signalé : le point figure dans la checklist, les slides de checklist et les notes formateur, sans manipulation obligatoire ni présence imposée dans les slides de station ou le guide.

### Station 1 — Structurer et naviguer

- `P-01` : distinguer le style du titre principal des styles de titres hiérarchiques.
- `P-02` : appliquer une hiérarchie sans saut et une numérotation de titres cohérente.
- `P-03` : vérifier les titres dans le volet de navigation et générer le sommaire automatique.
- `P-04` : remplacer les fausses puces et numéros par des listes natives.
- `P-05` : afficher les marques de mise en forme et remplacer paragraphes vides, espaces successifs, tabulations, retours forcés, sauts de page et colonnes simulées par les fonctions adaptées.

Preuve : le volet présente la hiérarchie attendue, le sommaire est actualisable et les listes sont sémantiques.

### Station 2 — Contenus et liens

- `P-06` : rédiger soi-même l’alternative d’une image informative simple, sans reprendre une description générée automatiquement.
- `P-07` : associer une image complexe à une alternative courte et une description détaillée adjacente.
- `P-08` : marquer une image redondante comme décorative, avec la procédure Writer explicitement adaptée.
- `P-09` : remplacer un texte sous forme d’image par du vrai texte.
- `P-10` : donner aux liens un intitulé autonome et visuellement identifiable, puis ajouter format, poids et langue aux téléchargements quand ils sont connus.
- `P-11` : fournir dans le corps l’information essentielle portée seulement par un filigrane.

Preuve : toutes les images ont le traitement approprié, le texte reste sélectionnable et chaque lien est compréhensible hors contexte.

### Station 3 — Couleurs, graphiques et tableaux

- `P-12` : appliquer un code couleur puis mesurer le contraste avec un outil ; les seuils sont de 4,5:1 pour le texte normal et de 3:1 pour le grand texte ainsi que les éléments graphiques pertinents.
- `P-13` : ne pas transmettre une information par la couleur seule ; le graphique doit avoir étiquettes et motifs ou un équivalent textuel complet. La mention « Urgent » ne constitue pas à elle seule une preuve de couleur seule si son texte transmet déjà l’information.
- `P-14` : construire un tableau de données simple, titré, sans fusion, imbrication, fractionnement de ligne ni usage de mise en page, avec en-tête identifié et répété si nécessaire.

Le TP DOIT fournir une ressource ou une méthode qui permette de corriger le graphique dans Word sans logiciel d’image. L’ancienne valeur `#767676` sur blanc NE DOIT PAS être présentée comme un échec ; toute couleur de test est validée par calcul.

Preuve : mesure de contraste conservée, information perceptible sans couleur et structure du tableau vérifiable dans le DOCX.

### Station 4 — Langues et lisibilité

- `P-15` : définir la langue principale et baliser le passage dans une langue différente.
- `P-16` : modifier les styles pour employer une police sans sérif, un corps utile d’au moins 12 points, un interligne d’au moins 1,15 et un alignement à gauche.
- `P-17` : saisir les mots normalement puis appliquer la casse par la mise en forme ; conserver les accents.
- `P-18` : développer sigles et acronymes à la première occurrence et activer la vérification orthographique des mots en majuscules.

Preuve : propriétés et XML de langue cohérents, aucune information utile sous 12 points sans justification et contrôle visuel de la lisibilité.

### Station 5 — Finaliser et publier

- `P-19` : renseigner titre, auteur et langue, puis enregistrer sous un nom descriptif.
- `C-01` : lancer le vérificateur Word, traiter les alertes pertinentes et expliquer toute alerte résiduelle.
- `P-20` : exporter en PDF avec propriétés, balises de structure et signets issus des titres.
- `C-02` : contrôler avec PAC, ou Acrobat Pro en alternative, au minimum le titre, la langue, les balises et l’ordre de lecture ; terminer par la checklist humaine.

Preuve : DOCX final, capture ou relevé des alertes, PDF exporté et checklist renseignée.

### Contrôles signalés sans manipulation obligatoire

- `S-01` : document non protégé lorsque la modification doit rester possible.
- `S-02` : absence de contenu clignotant.
- `S-03` : absence de formulaire Word interactif dans ce parcours.
- `S-04` : absence d’objet ou de zone de texte flottante porteuse d’information.
- `S-05` : absence de tableau utilisé pour la mise en page ou doté d’un habillage flottant.

Ces contrôles NE DOIVENT PAS être qualifiés de secondaires au sens de leur importance ; seul leur mode de traitement diffère.

## 7. Contrat des trois DOCX

### Version inaccessible

- Remplace le rapport trimestriel actuel par le guide pratique « Rendre un document Word accessible » attribué à Sami.
- Porte la totalité des règles, procédures et exemples qui figureront dans le corrigé, mais les met volontairement en œuvre de façon inaccessible.
- Contient chaque défaut praticable, sans commentaire d’aide.
- Sert au diagnostic autonome ou à la comparaison.
- Peut conserver volontairement des défauts de langue, de propriétés et de mise en forme identifiés dans la matrice.

### Version avec pistes

- Conserve la même information éditoriale, dans le même ordre, sans révéler une version déjà corrigée.
- Reprend exactement les mêmes défauts et occurrences.
- Ajoute une piste par occurrence : problème, impact, règle et première action.
- Ne corrige rien à la place du binôme.
- Ancre les défauts de niveau document sur un paragraphe stable du corps avec le préfixe « Document — » ; aucun commentaire n’est ancré dans un en-tête, un pied de page ou un objet dont Word masque la piste.

### Version corrigée

- Devient le guide pratique autonome distribué en fin de TP.
- Conserve la même information éditoriale que les deux fichiers de départ ; seules la structure, la mise en forme, les alternatives, les propriétés et les autres corrections d’accessibilité changent.
- Suit l’ordre des stations.
- Pour chaque point : problème, impact, règle, procédure Word, procédure Writer, manipulation et preuve de correction.
- Vise 20 à 30 pages sans compression artificielle ; la lisibilité prime sur la pagination.
- Limite les captures à celles qui changent réellement l’action et fournit une alternative pertinente à chacune.

## 8. Source unique et prévention de la dérive

L’implémentation DOIT créer une matrice structurée unique, proposée sous `_source/exercice-sami-matrice.yml`. Elle contient une section `sequence` avec chaque bloc et sa durée, puis les contrôles avec au minimum : identifiant, niveau, station éventuelle, intitulé, impact, règle, défaut ou action attendue, occurrences attendues, règle d’ancrage, piste, état corrigé, procédure Word, procédure Writer, mode de preuve automatique ou humain, ligne de checklist, section éventuelle du guide, module de slide et référence pédagogique locale.

Cette matrice DOIT être consommée directement par :

- le générateur des trois DOCX ;
- le générateur des checklists PDF et DOCX ;
- les données des slides de station et de checklist ;
- les tests de complétude et de fraîcheur.

La spécification, la liste des différences, le guide, les mémos et les notes peuvent conserver une rédaction humaine, mais leurs identifiants, libellés normalisés, niveaux et couverture DOIVENT être contrôlés contre la matrice. Les mémos Word et Writer peuvent conserver leur plan actuel en cinq thèmes si chaque section référence les identifiants de la matrice. Les contrôles `S` ont une station et une section de guide nulles ; ils figurent seulement dans la matrice, les deux checklists, les slides de checklist et les notes formateur.

Une référence locale `_source/references/martine-sutra-couverture.md` DOIT définir les codes de couverture repris de la source Martine sans copier son support ni conserver de chemin personnel. La matrice référence ces codes vérifiables depuis un clone propre.

Une cible `make checklist` DOIT produire le DOCX et la source Markdown du PDF depuis la matrice. Le PDF passe ensuite par le générateur PDF/UA existant avec `make pdf` ; aucun second générateur PDF n’est créé. La matrice DOIT être déclarée comme source du contrôle de fraîcheur et chaque nouvelle sortie comme sortie attendue du paquet.

Le chantier DOIT étendre le générateur existant. Il NE DOIT PAS créer un second générateur concurrent ni modifier directement les DOCX, PDF ou PPTX générés.

La première étape d’implémentation DOIT mettre à jour `AGENTS.md` : supprimer la règle « sans filet », remplacer le contrat de 21 critères et actualiser le volume du deck sans figer un nouveau total fragile. La spécification doit ensuite abandonner le format de 25 minutes, l’ancien code de formation, les anciennes références de slides et le verrou artificiel de 21 critères.

## 9. Slides et animation

- Avant toute réécriture, les modules actuels 03 à 26c DOIVENT être classés dans un inventaire `conserver`, `fusionner`, `remplacer` ou `supprimer`. Toute suppression autre que le quiz final exige une validation humaine. Le plan cible devient celui des stations.
- La partie II vise 20 à 30 slides, sans plafond rigide.
- Chaque station associe brièvement règle, défaut Sami, procédure Word, encadré Writer, manipulation et preuve.
- Le deck NE DOIT PAS recopier l’intégralité du guide.
- Le quiz diagnostic Documents A/B et sa réponse sont conservés au début de la partie II comme amorce brève, sans devenir une évaluation ni allonger le préambule.
- Le quiz final et sa correction DOIVENT disparaître.
- Un module de synthèse de la matinée de une à deux slides DOIT être créé après la partie II et avant la partie III ; il consolide les acquis des parties I et II, accueille les questions et assure la transition, sans nouvelle évaluation.
- La checklist reste dans le deck, mais son nombre de slides est déterminé par la lisibilité de la source consolidée.
- Les compositions utilisent les composants DSFR-IGPDE existants et sont validées visuellement. Le support Martine reste une inspiration humaine pour la respiration et la variété, pas une source d’acceptation exécutable depuis le clone.
- L’ordre des slides est testé relativement au chapitre et aux stations, sans total global ni index absolu fragile.
- Les notes formateur portent les consignes, le minutage, les points de synthèse et les variantes guidée/autonome.

## 10. Checklist et livrables stagiaires

La même source alimente les sorties suivantes :

- avec `make checklist`, un DOCX accessible remplissable sans contrôle de formulaire et la source Markdown du PDF ;
- avec `make pdf`, un PDF imprimable accessible issu de cette source Markdown ;
- les extraits nécessaires au deck et au guide.

Chaque ligne porte l’identifiant stable, le niveau de traitement, une formulation compréhensible et une case de suivi. Les formulations `H1/H2/H3`, `CSS`, « sans erreur résiduelle » et les phrases corrompues de l’ancienne checklist sont interdites.

## 11. Cohérence IGPDE et paquet

Le chantier doit réviser les dépendances directes de la partie II :

- le déroulé pédagogique : intégrer la synthèse technique du TP dans le bloc 10 h 30–12 h, maintenir la synthèse générale de la matinée de 12 h à 12 h 15, supprimer le quiz final et actualiser les anciennes plages de slides ainsi que le contrat de 21 critères ;
- la fiche technique : confirmer que PAC est préinstallé ou maintenir une consigne explicite de préparation et une solution Acrobat Pro ;
- le README du pack et le dossier `tp-word-igpde` : inventorier les trois DOCX, les deux checklists, les mémos et toute ressource nécessaire à la correction du graphique ;
- les mémos Word et Writer : aligner le contenu et les procédures sans créer une troisième source narrative concurrente ;
- les notes formateur : aligner minutage, distribution des fichiers et preuves attendues.

`make pack` ne régénère pas Sami. La procédure de livraison DOIT donc conserver l’ordre : régénérer les sources concernées, contrôler leur fraîcheur, puis fabriquer le pack.

## 12. Critères d’acceptation et preuves

### Automatisables

- Un test de matrice échoue si un contrôle `P` ou `C` n’a pas de station, d’action attendue, d’état corrigé, de ligne de checklist, de section de guide, de slide ou de preuve. Le défaut, la règle d’ancrage et la piste sont exigés seulement lorsque le nombre d’occurrences attendues est supérieur à zéro. Pour un contrôle `S`, le test exige une ligne de checklist, une slide de checklist et une note formateur, avec une station et une section de guide nulles.
- Des tests DOCX inspectent le XML : styles, hiérarchie, listes, en-têtes de tableau, absence de fusion, alternatives, marqueur décoratif, langues, propriétés, casse, alignement, tailles et espacements.
- Chaque défaut attendu est présent dans les deux fichiers de départ et absent du corrigé.
- Un test négatif réinjecte au moins un défaut par famille détectable dans le corrigé et doit échouer.
- Les pistes couvrent chaque occurrence et ne modifient pas le contenu fautif.
- Le calcul de contraste valide les couleurs plutôt qu’un commentaire codé en dur.
- Pour les niveaux `P` et `C`, les identifiants, libellés, niveaux, stations et ordre sont cohérents entre matrice, checklists, guide, slides et tests ; les contrôles `S` restent limités aux surfaces prévues.
- La recherche des anciens contrats couvre `AGENTS.md`, `_source/exercice-sami-*`, le générateur Sami, les scripts actifs et l’index des slides, les mémos, les checklists, la note formateur active, les tests, le README du pack et les documents administratifs. La liste fermée des motifs recherchés est : `21 critères`, `25 min`, `25 minutes`, `sans checklist`, `sans filet`, `rapport trimestriel` et `102638`. La seule occurrence active autorisée de `102638` est la mention historique « ex-102638 » d’`AGENTS.md`. Sont explicitement exclus `todo.md`, `lessons.md`, les autres fichiers de `notes/`, les prompts de fabrication et `_source/references/`, sauf la nouvelle couverture Martine.
- Les tests de deck n’emploient plus de total global ni de positions absolues, y compris dans les tests des parties I, III et IV affectés par la renumérotation.
- Le plan du deck conserve la synthèse de la matinée après la partie II et avant la partie III, hors des 90 minutes du TP.
- Les fichiers attendus sont copiés dans le pack et déclarés au contrôle de fraîcheur.
- La somme des blocs de la section `sequence` de la matrice et des durées des notes formateur vaut 90 minutes. Le module de synthèse de la matinée est absent de `sequence`, placé après la partie II et ne référence aucun identifiant de contrôle `P`, `C` ou `S`.
- Le nombre de commentaires du fichier avec pistes égale les occurrences attendues de la matrice ; le corps éditorial reste identique à l’inaccessible hors marqueurs de commentaires.
- Les contrastes sont calculés pour les couleurs utiles du corrigé et aucune source active ne présente `#767676` ou `4,48` comme un échec.

### Commandes de recette

1. `make sami`
2. `make checklist`
3. `make pdf`
4. `make deck`
5. `make fraicheur-pack`
6. `make qa`, puis lecture de `.qa/qa-pptx-report.md` avec statut `CONVERGED`
7. `make pack`
8. `make verifier` sur le paquet final

### Vérifications humaines sous Windows

- Corriger une fois depuis le DOCX avec pistes et une fois depuis le DOCX inaccessible.
- Vérifier les chemins Word et Writer sur les versions installées.
- Archiver le résultat du vérificateur Word sur l’inaccessible et le corrigé.
- Exporter le vrai fichier de travail en PDF et conserver le relevé PAC ou Acrobat Pro.
- Chronométrer la séquence avec un binôme novice ; toutes les productions doivent être obtenues en 90 minutes.
- Relire visuellement les slides modifiées et le guide ; vérifier les alternatives et l’ordre de lecture.

## 13. Phasage futur en tickets

1. **Autorité, cible et inventaire** : confirmer le tag de repli, mettre à jour les règles, rendre locale la couverture Martine et classer chaque module existant.
2. **Matrice** : créer la source unique et écrire les tests de complétude en échec.
3. **Prototype DOCX représentatif** : produire les trois fichiers avec tout le contenu éditorial cible et les occurrences minimales de chaque règle, puis chronométrer immédiatement un binôme novice avant d’étendre le deck.
4. **DOCX et générateur** : stabiliser les occurrences, les pistes fiables et le guide corrigé sans ajouter de contenu au corrigé.
5. **Checklist, mémos et notes** : générer les deux formats et réconcilier les procédures.
6. **Deck** : conserver le quiz diagnostic Documents A/B et ses quatre éléments, reconstruire la suite de la partie II autour des stations, créer la synthèse de la matinée et supprimer le quiz final.
7. **Paquet et documents IGPDE** : aligner inventaires, déroulé, fiche technique et fraîcheur.
8. **Recette Windows** : produire les preuves manuelles, corriger les écarts puis lancer la recette complète.

Les tickets seront rédigés en Markdown local après validation de ce PRD. Aucune issue GitHub n’est autorisée par ce document.

## 14. Non-objectifs et raccourcis interdits

- Ne pas refondre les parties Web ou réseaux sociaux, sauf correction d’un horaire ou d’un numéro de slide devenu faux.
- Ne pas enseigner la remédiation avancée d’un PDF dans Acrobat Pro.
- Ne pas transformer les tableaux ou objets flottants en manipulation obligatoire.
- Ne pas déclarer un DOCX accessible sur la seule base du vérificateur Word.
- Ne pas modifier les binaires générés à la main.
- Ne pas conserver quatre listes de critères par compatibilité historique.
- Ne pas réduire la taille du texte ou surcharger les slides pour respecter un volume arbitraire.
- Ne pas ajouter de quiz final sous un autre nom.

## 15. Risques et parades

- **Temps insuffisant** : la matrice fixe les occurrences réellement conçues et les cinq dernières minutes servent de marge et remise. Si le prototype dépasse 90 minutes, réduire les répétitions avant de proposer le passage d’un contrôle `P` vers `C` ou `S`, qui exige une validation humaine.
- **Variations de Word ou Writer** : procédures testées sur les versions installées et libellés robustes plutôt que captures dépendantes d’une version.
- **PAC absent** : vérification avant la session et alternative Acrobat Pro préparée.
- **Graphique impossible à corriger** : ressource de remplacement ou méthode équivalente fournie dans le fichier de travail.
- **Dérive entre sorties** : matrice canonique, égalité des identifiants et contrôle de fraîcheur étendu.
- **Fausse confiance automatisée** : outils automatiques suivis d’une vérification humaine obligatoire.
- **Document trop dense** : priorité au corps de 12 points, aux stations et à la divulgation progressive.
- **Échéance proche** : la refonte vise la session du 9 octobre 2026 ; T01 à T15 sont fusionnés dans `main`, mais aucune sortie ne doit être remise à l’IGPDE avant la recette finale T16.

## 16. Sources et ancrage

Sources internes inspectées : `AGENTS.md`, `_source/exercice-sami-spec.md`, `_source/exercice-sami-diff.md`, `scripts/generate_exercice_sami.py`, `fiche-pratique/memo-word.md`, la checklist formateur, l’index des slides, les scripts de chapitre, d’exercice et de checklist de la partie II, les tests de plan et de séquence, `Makefile`, les scripts du pack, le README du pack, le déroulé pédagogique et la fiche technique.

Source pédagogique inspectée : support Markdown Martine Sutra de juin 2025, notamment contrastes, images, métadonnées, langues, styles, titres, navigation, sommaire, listes, majuscules, acronymes, marques de mise en forme, liens, lisibilité, vérificateurs, export PDF, tableaux et contrôle post-export.

### Matrice d’affirmations sourcées

- **Affirmation** : l’ancien contrat impose 25 minutes et une identification sans checklist. **Source** : spécification Sami et `AGENTS.md`. **Verdict** : confirmé. **Impact** : ces règles doivent être remplacées avant l’implémentation.
- **Affirmation** : les trois DOCX existent déjà et sont copiés explicitement dans le pack. **Source** : générateur Sami, `scripts/pack_supports.py` et son test. **Verdict** : confirmé. **Impact** : étendre la chaîne existante, ne pas la dupliquer.
- **Affirmation** : les listes de critères divergent. **Source** : spécification, checklist, mémo et quatre slides de checklist. **Verdict** : confirmé. **Impact** : matrice unique et test d’égalité.
- **Affirmation** : le corrigé actuel ne respecte pas encore 12 points minimum. **Source** : générateur, corps et éléments utiles de 9 à 11 points ; support Martine, minimum de 12 points. **Verdict** : confirmé. **Impact** : remédiation et tests typographiques.
- **Affirmation** : `#767676` échoue à 4,5:1. **Source** : commentaires actuels uniquement. **Verdict** : réfuté. **Impact** : calcul automatique et nouvel exemple fautif.
- **Affirmation** : le déroulé prévoit 1 h 30 puis 15 minutes de synthèse de la matinée. **Source** : DOCX du déroulé converti en texte. **Verdict** : confirmé et maintenu. **Impact** : actualiser le contenu du créneau sans le supprimer ni rallonger le TP.
- **Affirmation** : PAC doit être demandé à l’IGPDE. **Source** : fiche technique convertie en texte. **Verdict** : partiel, car PAC y figure déjà avec une formulation conditionnelle. **Impact** : confirmer l’installation ou renforcer la consigne, sans créer un doublon.

## 17. Inconnues et portes de validation

- Le rendu visuel du PPTX Martine n’a pas été réévalué pendant la rédaction de ce PRD ; il reste une référence humaine, pas une source mécanique.
- Les mémos et les scripts de la partie II ont été alignés sur la matrice canonique ; leurs procédures restent à rejouer sur les versions Windows installées.
- Les chemins de menus n’ont pas été rejoués sur les versions installées de Word et Writer.
- Les DOCX générés ont passé les contrôles structurels et une réouverture LibreOffice sans réparation ; leur recette dans Word bureau sous Windows reste à effectuer.
- Le résultat PAC, le résultat du vérificateur Word et le minutage restent à produire pendant la réalisation.
- La reconstruction du graphique à partir des valeurs visibles est décrite dans la matrice et les mémos ; sa manipulation réelle reste à vérifier sous Word et Writer.
- La présence d’une option « Décoratif » dans Writer dépend de la version installée et doit être rejouée avant de figer la procédure.

## 18. PDG pass

- **Déclenchement** : oui, car ce PRD sera exécuté par d’autres agents et porte sur plusieurs sources de vérité et sorties générées.
- **Compétence** : `to-spec` pour rendre les exigences testables ; `progressive-disclosure-guard` pour borner le chantier et interdire les raccourcis.
- **Recouvrements** : réutiliser le générateur et les cibles Make ; étendre la fraîcheur et les tests ; remplacer l’ancien contrat pédagogique ; éviter tout générateur ou inventaire parallèle.
- **Connu** : décisions humaines, trois DOCX, durée, environnements, formats de checklist, chaîne de génération et divergence actuelle.
- **Inconnu** : comportements réels des logiciels Windows, contrôle PAC final, minutage et rendu visuel final.
- **Mauvais chemin** : retoucher directement le PPTX et les DOCX, conserver les 21 critères, ou déclarer la réussite sur un outil automatique.
- **Garde-fou** : matrice canonique, tests négatifs, commandes réelles et preuves humaines Windows.
- **Comportements préservés** : noms des trois DOCX, générateur Sami, composants DSFR-IGPDE, commandes de fabrication, autres parties de la formation et site d’exercice.
- **Fichiers matériels contrôlés** : les sorties PPTX, DOCX et PDF ont passé les contrôles structurels automatisés ; la relecture complète sous Word et Writer Windows, le contrôle PAC et le minutage restent à produire pendant T16.
- **Revue** : contre-revue Claude du cadrage obtenue avant rédaction ; cette passe finale reste un auto-contrôle PDG et nécessite la validation humaine du PRD.
