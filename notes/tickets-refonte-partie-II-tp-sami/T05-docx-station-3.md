# T05 — Migrer la station 3 dans les trois DOCX

**Statut :** `completed` — génération, tests XML, contrôle visuel des
graphiques et contre-revue vérifiés le 1er octobre 2026 ; les manipulations
humaines sous Word et Writer restent assignées à T09a et T16.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T04](T04-docx-station-2.md).

**Débloque :** [T06](T06-docx-station-4.md).

## À construire

Ajouter la tranche « Couleurs, graphiques et tableaux » dans les trois DOCX.
La correction doit être réalisable dans Word sans imposer un logiciel d’image
supplémentaire.

## Critères d’acceptation

- [x] Les trois DOCX portent le même contenu éditorial pour `P-12` à `P-14`.
- [x] Une couleur réellement non conforme est utilisée dans les deux fichiers
  de départ et sa correction est validée par calcul.
- [x] Les seuils de 4,5:1 et 3:1 sont appliqués selon le type de contenu.
- [x] Le défaut de couleur seule ne repose pas sur un mot qui transmet déjà à
  lui seul l’information attendue.
- [x] Le graphique peut être corrigé pendant le TP grâce à une ressource ou une
  méthode fournie dans Word.
- [x] Le tableau corrigé est un tableau de données simple, titré, sans fusion,
  imbrication, fractionnement de ligne ni usage de mise en page.
- [x] La ligne d’en-tête est identifiée et répétée lorsque nécessaire.
- [x] `#767676` et `4,48` ne sont jamais présentés comme un échec de contraste.

## Preuves attendues

- [x] `make sami` produit les trois DOCX et la ressource graphique nécessaire.
- [x] Les tests calculent les contrastes au lieu de comparer un commentaire.
- [x] Les tests DOCX inspectent les en-têtes, fusions, imbrications et options
  de fractionnement du tableau.
- [x] La correction du graphique dans Word fait partie du scénario humain
  chronométré de T09a, puis de la recette finale T16.

## À préserver

- Les stations 1 et 2 déjà migrées.
- Les graphiques et ressources générés par la chaîne existante.

## Hors périmètre

- Transformer les tableaux flottants en manipulation obligatoire.
- Enseigner un outil graphique externe.

## Preuves d’exécution

- `make sami` a régénéré les deux graphiques et les trois DOCX historiques
  depuis le générateur, sans retouche manuelle des binaires.
- Les tests ciblés de matrice, de DOCX, de fraîcheur et de paquet comptent
  84 réussites. Le test P-13 a d’abord échoué sur l’ancien ancrage
  « Graphique éditable », avant la correction du contrat et des sorties.
- Les contrastes sont calculés depuis les couleurs réelles : `#9A9A9A` sur
  blanc vaut 2,81:1 et échoue ; `#595959` vaut 7,00:1 et passe. Les deux
  couleurs porteuses du graphique atteignent le seuil de 3:1.
- Dans les deux fichiers de départ, le graphique affiche ses valeurs mais la
  légende associe les séries uniquement au rouge et au vert ; l’alternative
  reste générique et aucun équivalent textuel complet ne neutralise le défaut.
  Le corrigé ajoute motifs, étiquettes et alternative complète.
- Le tableau corrigé ne contient ni `gridSpan`, ni `vMerge`, ni tableau
  imbriqué. Sa première ligne est déclarée comme en-tête et ses trois lignes
  portent `cantSplit`.
- `make verifier` compte 203 tests réussis et 5 ignorés ; la validation du site
  et les contrôles du dépôt passent. Le seul avertissement concerne le cache
  pytest non inscriptible dans le bac à sable.
- `make fraicheur-pack` ne signale aucun DOCX ni graphique Sami. La cible
  globale reste rouge uniquement à cause de la grille d’audit XLSX, antérieure
  à son générateur et hors du périmètre T05.
- La première revue ShipGuard a conclu `NO-GO` sur deux P1 et deux P2 : défaut
  P-13 neutralisé par un équivalent textuel, ancrage présenté à tort comme
  éditable, titre non accentué et test incomplet des fusions. Après correction
  test-first, la contre-revue conclut `GO` sans nouveau P0, P1 ou P2.
- Restent `NOT VERIFIED` humainement : reconstruction chronométrée dans Word
  et Writer sous Windows, lisibilité à la taille réelle d’insertion, affichage
  des commentaires et exactitude des chemins de menus. Ces preuves
  appartiennent à T09a et T16.
