# T11 — Construire les slides de la station 2

**Statut :** `completed` — 2 octobre 2026 ; génération, tests et relecture
visuelle vérifiés. La validation humaine finale reste affectée à T16.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T10](T10-deck-ouverture-et-station-1.md).

**Débloque :** [T12](T12-deck-station-3.md).

## À construire

Construire la séquence de slides « Contenus et liens » comme une tranche
pédagogique complète, depuis l’observation du défaut jusqu’à la preuve de
correction dans le document Sami.

## Critères d’acceptation

- [x] La station couvre `P-06` à `P-11` sans ajouter de règle absente de la
  matrice et des trois DOCX.
- [x] Les identifiants, libellés, niveaux et ordre de la station sont consommés
  directement depuis la matrice, sans liste normative recopiée dans le module.
- [x] Images simples, images complexes et images décoratives sont distinguées
  par leurs usages et non par un slogan unique sur le texte alternatif.
- [x] Le texte sous forme d’image et les liens donnent lieu à une manipulation
  vérifiable dans le DOCX. `P-11` est expliqué à partir de la règle et de la
  mention placée dans le corps du corrigé, sans réintroduire de filigrane
  superposé dans les documents d’exercice.
- [x] Word est présenté en premier et Writer dans un encadré compact.
- [x] Les slides restent synthétiques et renvoient au guide pour les procédures
  détaillées.
- [x] Les notes formateur indiquent la durée, les questions de synthèse et les
  points d’aide possibles.
- [x] L’ordre des modules est testé relativement à la station 1 et à la station
  suivante.

## Preuves attendues

- [x] Les tests ciblés de contenu, notes et ordre passent.
- [x] `make deck` produit un deck complet sans avertissement de pied de page.
- [x] La relecture visuelle contrôle les images, alternatives, espacements et
  ordre de lecture.

## Réalisation et vérifications

- La station 2 est générée depuis les contrôles `P-06` à `P-11` de la matrice.
- Les variantes Word et Writer, les notes formateur et l’ordre relatif sont
  couverts par les tests structurels.
- La relecture du PDF rendu confirme l’absence de chevauchement et de coupe.

## À préserver

- L’ouverture et la station 1 validées dans T10.
- Le contenu des autres parties du deck.

## Hors périmètre

- Construire les stations 3 à 5.
- Ajouter des captures qui ne changent pas l’action à effectuer.
