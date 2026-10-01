# T04 — Migrer la station 2 dans les trois DOCX

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T03](T03-docx-station-1.md).

**Débloque :** [T05](T05-docx-station-3.md).

## À construire

Ajouter la tranche « Contenus et liens » pilotée par la matrice dans les trois
DOCX, avec des actions réellement praticables dans Word et des procédures
Writer détaillées dans le guide corrigé.

## Critères d’acceptation

- [ ] Les trois DOCX portent le même contenu éditorial pour `P-06` à `P-11`.
- [ ] Une image informative simple demande une alternative rédigée par le
  binôme, sans alternative automatique présentée comme acceptable.
- [ ] Une image complexe associe alternative courte et description détaillée
  adjacente.
- [ ] Une image redondante est traitée comme décorative, avec une procédure
  Writer adaptée à la version réellement testée.
- [ ] Le texte sous forme d’image est remplacé par du texte sélectionnable dans
  le corrigé.
- [ ] Les liens sont autonomes, visuellement identifiables et complétés par le
  format, le poids et la langue lorsque ces informations sont connues.
- [ ] L’information portée seulement par le filigrane est reprise dans le corps
  du corrigé.
- [ ] Chaque occurrence fautive possède une piste fiable dans la version
  guidée.

## Preuves attendues

- [ ] `make sami` régénère les trois documents sans sortie manquante.
- [ ] Les tests XML distinguent alternative informative, description complexe
  et marqueur décoratif.
- [ ] Les tests confirment la présence de vrai texte, de liens explicites et de
  l’information essentielle dans le corps.
- [ ] La visibilité et l’ancrage des pistes sont couverts par le scénario
  humain Word de T09a, puis par la recette finale T16.

## À préserver

- Les stations déjà migrées et les contenus non encore migrés.
- L’égalité éditoriale des trois versions.

## Hors périmètre

- Modifier les couleurs, tableaux, langues ou procédures d’export.
- Modifier les slides.
