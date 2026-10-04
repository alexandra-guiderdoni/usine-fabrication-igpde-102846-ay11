# T08 — Générer les checklists accessibles

**Statut :** `completed` — 2 octobre 2026

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T07](T07-docx-station-5-et-prototype.md).

**Débloque :** [T15](T15-aligner-le-pack-et-les-documents-igpde.md).

## À construire

Produire depuis la matrice une checklist papier accessible et une checklist
DOCX remplissable, utilisables dès le préambule puis après chaque station.

## Critères d’acceptation

- [x] Une cible `make checklist` génère le DOCX et la source Markdown du PDF.
- [x] `make pdf` utilise le générateur PDF/UA existant pour produire le PDF ;
  aucun second générateur PDF n’est créé.
- [x] Chaque ligne porte l’identifiant, le niveau `P`, `C` ou `S`, une
  formulation compréhensible et une zone de suivi.
- [x] Le DOCX est remplissable sans contrôle de formulaire interactif.
- [x] Les contrôles `S` apparaissent dans les deux checklists sans être
  transformés en manipulation obligatoire.
- [x] Les formulations `H1/H2/H3`, `CSS`, « sans erreur résiduelle » et les
  anciennes phrases corrompues ont disparu.
- [x] Les deux formats et leur source sont déclarés dans le paquet et dans le
  contrôle de fraîcheur.
- [x] Les données nécessaires aux futures slides de checklist viennent de la
  même matrice.
- [x] L’ancienne liste
  `livrables-IGPDE-2026-102846/Livrables-Formateur/_alex/checklist-bureautique.md` est
  retirée comme source normative : elle contient seulement un renvoi vers les
  checklists générées et la matrice canonique, sans conserver ses propres items.
- [x] La cible `make checklist` est documentée dans `make aide` et dans la
  section « Qui fabrique quoi dans le pack » d’`AGENTS.md`, avec ses entrées et
  ses sorties.

## Preuves attendues

- [x] `make checklist` produit les sorties attendues à partir d’un clone propre.
- [x] `make pdf` produit un PDF déclaré PDF/UA-1 avec arbre de structure.
- [x] Les tests comparent identifiants, niveaux, ordre et formulations à la
  matrice.
- [x] `make fraicheur-pack` détecte une checklist absente ou plus ancienne que
  sa source.
- [ ] L’usage papier et la saisie dans le DOCX sont éprouvés dans T16.

## Réalisation et vérifications

- `make checklist` a généré le Markdown et le DOCX depuis la matrice canonique.
- `make pdf` a produit le PDF avec la chaîne PDF/UA existante. Le fichier porte
  la déclaration PDF/UA-1, possède un arbre de structure et son rendu visuel de
  six pages a été relu sans débordement ni ligne de critère scindée.
- Les tests ciblés couvrent les deux formats, leur fidélité à la matrice, la
  fraîcheur, l’ordre séquentiel de `make pack` et la réutilisation du générateur
  PDF existant.
- `make verifier` est vert : 228 tests réussis, 5 ignorés, validation du site et
  contrôles du dépôt réussis.
- La revue indépendante est passée de `NO-GO` à `GO` après ajout du contrat de
  fraîcheur du PDF. Ses deux observations mineures sur l’ordre parallèle du pack
  et sa documentation ont ensuite été corrigées.
- Un clone distant propre de la branche au commit `7d0a910` a exécuté
  `make checklist` et `make pdf`. Après la régénération explicite des autres
  ressources contrôlées avec `make sami` et `make grille`, le contrôle
  `make fraicheur-pack` est vert.
- La grille XLSX a été régénérée dans `03-easy-checks/` et dans le site. Les
  deux copies sont identiques et le classeur contient les 17 feuilles attendues.

## À préserver

- Le générateur PDF accessible embarqué et son refus des PDF non PDF/UA-1.
- La checklist distribuée dès le début du TP.

## Hors périmètre

- Ajouter des champs de formulaire Word interactifs.
- Construire les slides de checklist.
