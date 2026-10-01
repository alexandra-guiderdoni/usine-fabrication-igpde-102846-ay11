# T11 — Construire les slides de la station 2

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T10](T10-deck-ouverture-et-station-1.md).

**Débloque :** [T12](T12-deck-station-3.md).

## À construire

Construire la séquence de slides « Contenus et liens » comme une tranche
pédagogique complète, depuis l’observation du défaut jusqu’à la preuve de
correction dans le document Sami.

## Critères d’acceptation

- [ ] La station couvre `P-06` à `P-11` sans ajouter de règle absente de la
  matrice et des trois DOCX.
- [ ] Les identifiants, libellés, niveaux et ordre de la station sont consommés
  directement depuis la matrice, sans liste normative recopiée dans le module.
- [ ] Images simples, images complexes et images décoratives sont distinguées
  par leurs usages et non par un slogan unique sur le texte alternatif.
- [ ] Le texte sous forme d’image, les liens et le filigrane donnent lieu à une
  manipulation vérifiable dans le DOCX.
- [ ] Word est présenté en premier et Writer dans un encadré compact.
- [ ] Les slides restent synthétiques et renvoient au guide pour les procédures
  détaillées.
- [ ] Les notes formateur indiquent la durée, les questions de synthèse et les
  points d’aide possibles.
- [ ] L’ordre des modules est testé relativement à la station 1 et à la station
  suivante.

## Preuves attendues

- [ ] Les tests ciblés de contenu, notes et ordre passent.
- [ ] `make deck` produit un deck complet sans avertissement de pied de page.
- [ ] La relecture visuelle contrôle les images, alternatives, espacements et
  ordre de lecture.

## À préserver

- L’ouverture et la station 1 validées dans T10.
- Le contenu des autres parties du deck.

## Hors périmètre

- Construire les stations 3 à 5.
- Ajouter des captures qui ne changent pas l’action à effectuer.
