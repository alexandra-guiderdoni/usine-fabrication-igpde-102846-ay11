# T12 — Construire les slides de la station 3

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T11](T11-deck-station-2.md).

**Débloque :** [T13](T13-deck-station-4.md).

## À construire

Construire la séquence de slides « Couleurs, graphiques et tableaux » autour
des manipulations réellement possibles dans le document Sami.

## Critères d’acceptation

- [ ] La station couvre `P-12` à `P-14` sans ajouter de règle absente de la
  matrice et des trois DOCX.
- [ ] Les identifiants, libellés, niveaux et ordre de la station sont consommés
  directement depuis la matrice, sans liste normative recopiée dans le module.
- [ ] Le contraste est présenté comme une mesure calculée avec les seuils
  applicables, jamais comme un verdict attaché à une couleur codée en dur.
- [ ] Le défaut de couleur seule et sa correction sont démontrables dans le
  graphique fourni, avec des étiquettes, des motifs ou un équivalent textuel.
- [ ] La correction du graphique reste réalisable dans Word sans logiciel
  d’image ; la ressource ou la méthode nécessaire est indiquée.
- [ ] Le tableau proposé reste un tableau de données simple, titré, sans
  fusion, imbrication ni usage de mise en page.
- [ ] Word est présenté en premier et Writer dans un encadré compact.
- [ ] Les notes formateur précisent durée, manipulation, preuve et point de
  synthèse de la station.
- [ ] L’ordre est testé relativement aux stations 2 et 4, sans index absolu.

## Preuves attendues

- [ ] Les tests ciblés de contenu, notes et ordre passent.
- [ ] `make deck` produit le deck complet sans avertissement de pied de page.
- [ ] La relecture visuelle confirme la lisibilité des contrastes, du graphique
  et du tableau.

## À préserver

- Les stations 1 et 2 validées dans T10 et T11.
- Les valeurs de contraste exactes portées par la matrice.

## Hors périmètre

- Enseigner les tableaux complexes ou les tableaux flottants.
- Ajouter une manipulation dans un logiciel d’image.
