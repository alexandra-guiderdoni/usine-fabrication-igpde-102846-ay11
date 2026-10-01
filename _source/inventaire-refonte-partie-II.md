# Inventaire décisionnel de la partie II

**Statut :** à valider par Alex avant T10.

Cet inventaire applique le PRD
`notes/prd-refonte-partie-II-tp-sami.md` aux modules actuellement présents de
`03` à `26c`. Les décisions décrivent le devenir pédagogique des contenus ;
elles n'autorisent encore aucun retrait de fichier.

## Point de départ vérifié

- Tag annoté : `avant-refonte-tp-sami-2026-10-01`.
- Objet du tag : `a79fe6db76e0cd9794ec0f66b3ffd7f407852bda`.
- Commit cible : `3e4b81eaa1727d20d27151b5bdebe481ac390d88`.
- Écart après actualisation : aucun commit derrière `origin/main`, un commit
  local devant.
- Environnement initial : `.venv` absent.
- Installation : la cible `make installer` échouait avant sa recette, car le
  chargement de `config.yml` exigeait déjà PyYAML. Le bootstrap et son test de
  non-régression ont été corrigés sur demande ; les dépendances verrouillées
  sont maintenant installées dans `.venv`.
- Vérification initiale, avant correction du bootstrap : `make verifier` a
  terminé avec 123 tests réussis, 5 ignorés, validation du site réussie et
  contrôles du dépôt réussis. Seul avertissement : le cache pytest ne pouvait
  pas être écrit dans le bac à sable.
- Vérification après correction du bootstrap : 124 tests réussis, 5 ignorés,
  validation du site et contrôles du dépôt réussis.

## Conserver

- `03_chapitre-word.py` : conserver le chapitre et sa frise, puis remplacer ses
  libellés par le plan des cinq stations. Test direct :
  `tests/test_plan_partie_2.py`.
- `04_ouverture-lecteur-ecran.py` : conserver l'amorce sensorielle avant la
  manipulation. Test direct : `tests/test_quiz_documents_sequence.py`.
- `05_quiz-flash-a-vs-b.py` : conserver le diagnostic Documents A/B dans les
  cinq minutes du préambule. Test direct :
  `tests/test_quiz_documents_sequence.py`.
- `05a_quiz-flash-reponse.py` : conserver la révélation séparée, sans en faire
  une évaluation. Test direct : `tests/test_quiz_documents_sequence.py`.
- `06_pourquoi-concerne.py` : conserver le message « l'accessibilité ne se
  voit pas : elle se manipule et se vérifie » et le bloc de réponse prévu par
  le PRD. Test direct : `tests/test_quiz_documents_sequence.py`.

## Fusionner dans les stations

- `08_pilier1-styles-titre.py` : fusionner styles, hiérarchie et navigation
  dans la station 1.
- `09_pilier1-listes.py` : fusionner les listes natives dans la station 1.
- `11_pilier2-contraste.py` : fusionner la mesure du contraste dans la station
  3 et remplacer l'ancien exemple fautif par une valeur calculée.
- `12_pilier2-couleur-seule.py` : fusionner couleur, motifs et étiquettes dans
  la station 3.
- `13_pilier3-alt-text.py` : fusionner images simples, complexes et décoratives
  dans la station 2.
- `14_pilier3-liens-infos.py` : fusionner liens autonomes, téléchargements et
  information essentielle dans la station 2.
- `16_pilier4-langue-lisibilite.py` : fusionner langues, casse et lisibilité
  dans la station 4.
- `19_pilier5-verificateur.py` : fusionner l'usage raisonné du vérificateur
  Word dans la station 5.
- `20_export-pdf-accessible.py` : fusionner l'export PDF et ses réglages dans la
  station 5.
- `21_etude-cas-sophie.py` : répartir son retour sur Sami dans les synthèses au
  fil de l'eau, sans second débrief après le TP.
- `22_par-ou-commencer.py` : intégrer ses repères d'action au préambule et à la
  checklist progressive.

Ces onze modules n'ont pas de test unitaire dédié. Leur ordre et leur éventuel
regroupement affectent toutefois les tests de plan et d'index listés plus bas,
ainsi que la recette `make deck` puis `make qa`.

## Remplacer

- `07_5-piliers-vue-ensemble.py` : remplacer l'ancien contrat « 5 thèmes,
  21 critères » par la mission de 90 minutes et le plan des stations.
- `10_pilier1-tableaux-flottants.py` : séparer le tableau de données pratiqué en
  station 3 des objets flottants seulement signalés dans la checklist.
- `15_exercice-sami.py` : remplacer l'annonce ponctuelle par les fichiers de
  départ, les livrables, le choix guidé ou autonome et les preuves attendues.
- `17_pilier4-espaces-clignotants.py` : intégrer les marques et espacements à la
  station 1 ; limiter le clignotement et les objets flottants aux contrôles
  signalés.
- `18_pilier5-avant-publier.py` : remplacer les cinq vérifications en deux
  minutes par la station 5 complète, avec outil, vérification humaine,
  checklist et contrôle après export.
- `26_checklist-21-criteres.py` : remplacer la première page de l'ancienne
  checklist par une sortie lisible de la matrice.
- `26a_checklist-exercice-2.py` : remplacer la seconde page de l'ancienne
  checklist par une sortie lisible de la matrice.
- `26b_checklist-autres.py` : remplacer la première page des autres critères
  par les contrôles `S` issus de la matrice.
- `26c_checklist-autres-2.py` : remplacer la seconde page des autres critères
  par les contrôles `S` issus de la matrice.

Ces neuf remplacements n'ont pas de test direct aujourd'hui. T10 devra créer
des tests fondés sur l'ordre relatif du chapitre, des stations, de la synthèse
de la matinée et du chapitre suivant.

## Supprimer

- `23b_quiz-final-reponses.py` : supprimer la correction du quiz final. Le PRD
  autorise explicitement ce seul retrait ; `tests/test_plan_partie_3.py` doit
  cesser d'exiger sa présence.

Toute autre disparition de module, y compris après une fusion ou un
remplacement, reste soumise à la validation humaine ci-dessous.

## Dépendances à rendre relatives

Les fichiers suivants figent actuellement un total global ou une position
absolue et devront être adaptés lors de T10 :

- `tests/test_plan_partie_1.py` ;
- `tests/test_plan_partie_2.py` ;
- `tests/test_plan_partie_3.py` ;
- `tests/test_plan_partie_4.py` ;
- `tests/test_quiz_documents_sequence.py` ;
- `tests/test_slide_99_site_entrainement.py`.

Les documents suivants publient aussi un total fixe ou un index appelé à
changer ; ils relèvent du balayage final de T14 et T15 :

- `AGENTS.md` pour l'ancien total, corrigé dès T01 ;
- `README.md` ;
- `contraintes.md` ;
- `architecture-c4-slides.md` ;
- `publication-site/README.md` ;
- `livrables-IGPDE-2026-102846/README.md` ;
- `scripts/slides/README.md` pour l'index des modules.

## Recherche bornée des anciens contrats

La recherche du 1er octobre 2026 a porté sur les motifs fermés du PRD :
`21 critères`, `25 min`, `25 minutes`, `sans checklist`, `sans filet`,
`rapport trimestriel` et `102638`. Elle a couvert `AGENTS.md`, les deux anciens
contrats Sami, le générateur, les scripts actifs, les mémos, les checklists, la
note formateur, les tests, le README du paquet et les documents administratifs.

Les résultats sont classés ainsi :

- exception historique permanente : `ex-102638` dans `AGENTS.md` ;
- exceptions transitoires jusqu'à T07 :
  `_source/exercice-sami-spec.md` et `_source/exercice-sami-diff.md`, désormais
  précédés d'un bandeau d'obsolescence ;
- génération Sami à remplacer par T03 puis à nettoyer par T07 :
  `scripts/generate_exercice_sami.py` ;
- ancien plan et ancien exercice à remplacer par T10 :
  `scripts/slides/07_5-piliers-vue-ensemble.py` et
  `scripts/slides/15_exercice-sami.py` ;
- note formateur à aligner par T09 :
  `livrables-IGPDE-2026-102846/Formateur/_alex/formation-102846-octobre-2026-bureautique.md` ;
- historique du paquet à vérifier et aligner par T14 et T15 :
  `livrables-IGPDE-2026-102846/README.md`.

La recherche n'a trouvé aucun ancien contrat supplémentaire dans les tests ou
les documents administratifs parcourus. Les références pédagogiques sont hors
de ce balayage, sauf la couverture Martine créée par T01.

## Porte de validation humaine

- [ ] Alex valide ces classements avant toute réécriture du deck en T10.
- [ ] Toute suppression autre que `23b_quiz-final-reponses.py` fait l'objet
  d'une confirmation explicite après transfert vérifié de son contenu utile.
