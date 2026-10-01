# T08 — Générer les checklists accessibles

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T07](T07-docx-station-5-et-prototype.md).

**Débloque :** [T09a](T09a-recetter-prototype-90-minutes.md) et
[T15](T15-aligner-le-pack-et-les-documents-igpde.md).

## À construire

Produire depuis la matrice une checklist papier accessible et une checklist
DOCX remplissable, utilisables dès le préambule puis après chaque station.

## Critères d’acceptation

- [ ] Une cible `make checklist` génère le DOCX et la source Markdown du PDF.
- [ ] `make pdf` utilise le générateur PDF/UA existant pour produire le PDF ;
  aucun second générateur PDF n’est créé.
- [ ] Chaque ligne porte l’identifiant, le niveau `P`, `C` ou `S`, une
  formulation compréhensible et une zone de suivi.
- [ ] Le DOCX est remplissable sans contrôle de formulaire interactif.
- [ ] Les contrôles `S` apparaissent dans les deux checklists sans être
  transformés en manipulation obligatoire.
- [ ] Les formulations `H1/H2/H3`, `CSS`, « sans erreur résiduelle » et les
  anciennes phrases corrompues ont disparu.
- [ ] Les deux formats et leur source sont déclarés dans le paquet et dans le
  contrôle de fraîcheur.
- [ ] Les données nécessaires aux futures slides de checklist viennent de la
  même matrice.
- [ ] L’ancienne liste
  `livrables-IGPDE-2026-102846/Formateur/_alex/checklist-bureautique.md` est
  retirée comme source normative : elle contient seulement un renvoi vers les
  checklists générées et la matrice canonique, sans conserver ses propres items.
- [ ] La cible `make checklist` est documentée dans `make aide` et dans la
  section « Qui fabrique quoi dans le pack » d’`AGENTS.md`, avec ses entrées et
  ses sorties.

## Preuves attendues

- [ ] `make checklist` produit les sorties attendues à partir d’un clone propre.
- [ ] `make pdf` produit un PDF déclaré PDF/UA-1 avec arbre de structure.
- [ ] Les tests comparent identifiants, niveaux, ordre et formulations à la
  matrice.
- [ ] `make fraicheur-pack` détecte une checklist absente ou plus ancienne que
  sa source.
- [ ] L’usage papier et la saisie dans le DOCX sont éprouvés dans T09a, puis
  rejoués dans T16 si la source de la checklist a changé.

## À préserver

- Le générateur PDF accessible embarqué et son refus des PDF non PDF/UA-1.
- La checklist distribuée dès le début du TP.

## Hors périmètre

- Ajouter des champs de formulaire Word interactifs.
- Construire les slides de checklist.
