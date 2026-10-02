# T12 — Construire les slides de la station 3

**Statut :** `completed` — 2 octobre 2026 ; génération, tests et relecture
visuelle vérifiés. La validation humaine finale reste affectée à T16.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T11](T11-deck-station-2.md).

**Débloque :** [T13](T13-deck-station-4.md).

## À construire

Construire la séquence de slides « Couleurs, graphiques et tableaux » autour
des manipulations réellement possibles dans le document Sami.

## Critères d’acceptation

- [x] La station couvre `P-12` à `P-14` sans ajouter de règle absente de la
  matrice et des trois DOCX.
- [x] Les identifiants, libellés, niveaux et ordre de la station sont consommés
  directement depuis la matrice, sans liste normative recopiée dans le module.
- [x] Le contraste est présenté comme une mesure calculée avec les seuils
  applicables, jamais comme un verdict attaché à une couleur codée en dur.
- [x] Le défaut de couleur seule et sa correction sont démontrables dans le
  graphique fourni, avec des étiquettes, des motifs ou un équivalent textuel.
- [x] La correction du graphique reste réalisable dans Word sans logiciel
  d’image ; la ressource ou la méthode nécessaire est indiquée.
- [x] Le tableau proposé reste un tableau de données simple, titré, sans
  fusion, imbrication ni usage de mise en page.
- [x] Word est présenté en premier et Writer dans un encadré compact.
- [x] Les notes formateur précisent durée, manipulation, preuve et point de
  synthèse de la station.
- [x] L’ordre est testé relativement aux stations 2 et 4, sans index absolu.

## Preuves attendues

- [x] Les tests ciblés de contenu, notes et ordre passent.
- [x] `make deck` produit le deck complet sans avertissement de pied de page.
- [x] La relecture visuelle confirme la lisibilité des contrastes, du graphique
  et du tableau.

## Réalisation et vérifications

- La station 3 est générée depuis `P-12` à `P-14`, y compris les seuils de
  contraste portés par la matrice.
- Le graphique ne repose pas sur la couleur seule et le tableau reste simple.
- La relecture à pleine résolution des slides denses confirme leur lisibilité.

## À préserver

- Les stations 1 et 2 validées dans T10 et T11.
- Les valeurs de contraste exactes portées par la matrice.

## Hors périmètre

- Enseigner les tableaux complexes ou les tableaux flottants.
- Ajouter une manipulation dans un logiciel d’image.
