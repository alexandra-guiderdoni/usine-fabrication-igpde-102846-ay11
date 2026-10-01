# T02 — Introduire la matrice pédagogique canonique

**Statut :** `completed` — matrice et validateur vérifiés le 1er octobre 2026.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T01](T01-verrouiller-et-inventorier.md).

**Débloque :** [T03](T03-docx-station-1.md).

## À construire

Ajouter la source structurée unique qui décrit la séquence de 90 minutes et la
couverture P/C/S. Cette étape est la phase d’expansion : la matrice et ses
validateurs coexistent temporairement avec le générateur actuel, sans créer un
second générateur.

## Critères d’acceptation

- [x] `_source/exercice-sami-matrice.yml` contient les sept blocs de la
  séquence et un total calculable de 90 minutes.
- [x] Les contrôles `P-01` à `P-20`, `C-01` à `C-02` et `S-01` à `S-05` sont
  présents, ordonnés et rattachés aux stations prévues.
- [x] Chaque contrôle porte les champs obligatoires du PRD, y compris les
  preuves, procédures Word et Writer, références de checklist, guide, slides
  et couverture pédagogique locale.
- [x] La matrice expose une lecture structurée réutilisable par le générateur
  Sami, les checklists, les slides et les tests ; aucune nouvelle liste
  normative parallèle n’est nécessaire aux tickets suivants.
- [x] Les règles propres aux occurrences à zéro et aux contrôles `S` sont
  validées explicitement.
- [x] L’identité éditoriale désigne le même texte, les mêmes informations et le
  même ordre dans le corps des trois DOCX ; seules les transformations de
  représentation déclarées par un contrôle de la matrice sont admises, par
  exemple le remplacement d’un texte en image par du vrai texte, un libellé de
  lien explicite, la reprise d’une information de filigrane ou le développement
  d’un acronyme.
- [x] Un validateur échoue sur un identifiant dupliqué, un champ obligatoire
  absent, une durée différente de 90 minutes ou une surface interdite pour `S`.
- [x] Les motifs hérités interdits sont recherchés dans le périmètre borné du
  PRD, avec l’exception historique `ex-102638` ; les occurrences conservées
  dans les deux fichiers historiques sont signalées comme exceptions
  temporaires jusqu’à T07 et ne sont pas confondues avec une recherche à zéro.
- [x] Le générateur actuel continue de fonctionner pendant cette phase
  d’expansion.

## Preuves attendues

- [x] Les tests du validateur passent sur la matrice complète.
- [x] Un test négatif existe pour chaque famille d’invariant de la matrice.
- [x] Un test échoue si un défaut est créé hors matrice ou si une différence
  éditoriale non déclarée apparaît entre les trois versions.
- [x] `make sami` reste exécutable sans modification manuelle des DOCX.
- [x] Aucun second générateur, inventaire parallèle ou liste normative n’est
  introduit.

## À préserver

- Les trois noms de fichiers DOCX.
- Les commandes Make existantes.
- Les contenus hors partie II.

## Hors périmètre

- Migrer le contenu des stations dans les DOCX.
- Générer les checklists ou reconstruire le deck.

## Preuves d’exécution

- `tests/test_exercice_sami_matrice.py` : 16 tests réussis, dont les cas
  négatifs sur la durée, le huitième bloc, les doublons, les champs et preuves
  absents, les occurrences à zéro, les surfaces `S`, les stations, les niveaux,
  les références, les défauts hors matrice et l’identité éditoriale.
- `make sami` exécuté dans une copie temporaire : les trois DOCX historiques
  sont générés sous leurs noms inchangés, sans modifier les binaires du
  worktree.
- `make verifier` : 140 tests réussis, 5 ignorés, validation du site réussie et
  contrôles du dépôt réussis. Le cache pytest reste non inscriptible dans le
  bac à sable, sans incidence sur les tests.
- La recherche des anciens contrats retrouve les exceptions et migrations déjà
  classées dans `_source/inventaire-refonte-partie-II.md`. Elle n’est pas
  présentée comme une recherche à zéro : certaines durées de 25 minutes sont
  légitimes hors de la partie II.
- La relecture structurelle locale conclut `GO`. La relecture indépendante
  demandée à Claude n’a produit aucune sortie et ne constitue donc pas une
  preuve de validation.
