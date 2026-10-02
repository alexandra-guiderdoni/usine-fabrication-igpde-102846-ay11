# T15 — Aligner le pack et les documents IGPDE

**Statut :** `completed` — 2 octobre 2026 ; alignement, génération et contrôles
du chantier vérifiés. Le contrôle global de `make pack` reste rouge uniquement
sur les quatre installeurs externes absents, non versionnés.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T08](T08-checklists-accessibles.md),
[T09](T09-memos-et-notes-formateur.md) et
[T14](T14-deck-station-5-et-synthese.md).

**Débloque :** [T16](T16-recette-integree-windows.md).

## À construire

Réconcilier les documents administratifs, l’inventaire du pack et les contrôles
de fraîcheur avec le TP de 90 minutes et ses livrables réels.

## Critères d’acceptation

- [x] Le déroulé pédagogique place le TP de 10 h 30 à 12 h, y inclut ses
  synthèses techniques et maintient la synthèse générale de 12 h à 12 h 15.
- [x] Le quiz final, toute ancienne plage de slides et toute mention devenue
  fausse du contrat de 21 critères sont retirés du déroulé.
- [x] La fiche technique demande PAC préinstallé ou conserve une consigne de
  préparation explicite, avec Acrobat Pro comme alternative.
- [x] Le README et le dossier `tp-word-igpde` inventorient les trois DOCX, la
  checklist DOCX, la checklist PDF, les mémos et la ressource de correction du
  graphique.
- [x] Le README du paquet distingue ce qui est remis au début du TP de ce qui
  est remis à la fin : le DOCX corrigé de référence n’est jamais présenté comme
  document de départ, même s’il se trouve dans le paquet formateur.
- [x] Le README du paquet ne fige plus le total obsolète de 138 slides.
- [x] Les scripts du pack copient chaque sortie attendue et le contrôle de
  fraîcheur relie chaque sortie à ses sources.
- [x] Pour chaque DOCX administratif édité manuellement, le texte est extrait
  avant et après, le document source est modifié dans Word ou LibreOffice, le
  diff textuel est limité aux passages attendus, puis le DOCX est rouvert sans
  demande de réparation. Aucun binaire généré n’est retouché à la main.
- [x] Les anciens contrats sont absents du périmètre de recherche fermé défini
  par le PRD, hors exception historique autorisée.
- [x] Le balayage global final confirme aussi qu’aucune source active ne
  présente `#767676` ou `4,48` comme un échec de contraste.
- [x] `fiche-pratique/README.md` et `scripts/slides/README.md` sont alignés sur
  la matrice et l’inventaire final ; les motifs `21 bonnes pratiques` et
  `21 criteres` sont intégrés au balayage des anciens contrats et supprimés
  avec leurs renvois obsolètes.
- [x] La procédure de livraison indique que `make pack` ne régénère pas Sami et
  impose la régénération des sources avant le contrôle de fraîcheur.

## Preuves attendues

- [x] `make sami`, `make checklist` et `make pdf` produisent les ressources
  attendues.
- [x] `make fraicheur-pack` confirme que les sorties ne sont pas obsolètes.
- [ ] `make pack` fabrique un paquet qui contient tous les fichiers inventoriés.
- [x] Les tests ciblés du pack, de l’inventaire et des anciens contrats passent.
- [x] Une inspection du paquet confirme les noms, formats et emplacements des
  livrables.
- [x] Si la recette complète ne peut pas être obtenue avant la session, le
  paquet existant et le tag de repli sont conservés ; aucune sortie partielle
  n’est fusionnée ni livrée.

## Réalisation et vérifications

- Le déroulé et la fiche technique ont été extraits avant modification,
  normalisés puis rouverts par LibreOffice sans demande de réparation. Leurs
  huit pages rendues ont été relues sans coupe ni chevauchement visible.
- `make sami`, `make checklist`, `make pdf`, `make deck`,
  `make fraicheur-pack` et `make qa` réussissent. Les six PDF produits déclarent
  PDF/UA-1 ; la QA du deck converge en une itération sans anomalie.
- `make pack` régénère les PDF et le deck, puis copie les trois DOCX et les
  supports attendus. Son dernier contrôle s’arrête avec un code non nul parce
  que NVDA, Colour Contrast Analyser, Focus Highlight et PAC sont absents du
  dossier `outils/`. Aucun téléchargement implicite n’a été effectué.
- Les tests ciblés réussissent : 89 tests. Le contrôle final `make verifier`
  réussit : 254 tests, validation des points de contrôle rapides et hook sur
  2 976 fichiers.
- Le paquet n’a pas été remis à l’IGPDE. La validation humaine Word, Writer,
  PowerPoint et PAC reste `NOT VERIFIED` et appartient à T16.

## À préserver

- L’ordre de fabrication documenté par le PRD.
- Les contenus administratifs sans lien avec la partie II.

## Hors périmètre

- Remettre le paquet à l’IGPDE.
- Fusionner, committer ou pousser la refonte.
