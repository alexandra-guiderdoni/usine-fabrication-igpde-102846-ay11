# T13 — Construire les slides de la station 4

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T12](T12-deck-station-3.md).

**Débloque :** [T14](T14-deck-station-5-et-synthese.md).

## À construire

Construire la séquence de slides « Langues et lisibilité » pour relier les
propriétés du document, les styles et la lecture effective du guide Sami.

## Critères d’acceptation

- [ ] La station couvre `P-15` à `P-18` sans ajouter de règle absente de la
  matrice et des trois DOCX.
- [ ] Les identifiants, libellés, niveaux et ordre de la station sont consommés
  directement depuis la matrice, sans liste normative recopiée dans le module.
- [ ] La langue principale et le passage dans une autre langue donnent lieu à
  une manipulation vérifiable.
- [ ] La procédure par les styles couvre une police sans sérif, un corps utile
  d’au moins 12 points, un interligne d’au moins 1,15 et l’alignement à gauche.
- [ ] La casse est appliquée par la mise en forme et les accents sont
  conservés.
- [ ] Les sigles et acronymes sont développés à la première occurrence et la
  vérification orthographique des majuscules est explicitée.
- [ ] Word est présenté en premier et Writer dans un encadré compact.
- [ ] Les notes formateur précisent durée, manipulation, preuve et point de
  synthèse de la station.
- [ ] L’ordre est testé relativement aux stations 3 et 5, sans index absolu.

## Preuves attendues

- [ ] Les tests ciblés de contenu, notes et ordre passent.
- [ ] `make deck` produit le deck complet sans avertissement de pied de page.
- [ ] La relecture visuelle confirme qu’aucun contenu utile n’est réduit sous
  12 points et que les exemples restent lisibles.

## À préserver

- Les stations 1 à 3 validées dans les tickets précédents.
- La distinction entre propriété de langue et correction orthographique.

## Hors périmètre

- Traiter la rédaction en langage clair au-delà des exemples du guide.
- Ajouter des réglages typographiques absents de la matrice.
