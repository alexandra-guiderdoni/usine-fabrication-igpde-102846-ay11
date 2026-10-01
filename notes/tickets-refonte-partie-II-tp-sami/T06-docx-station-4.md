# T06 — Migrer la station 4 dans les trois DOCX

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T05](T05-docx-station-3.md).

**Débloque :** [T07](T07-docx-station-5-et-prototype.md).

## À construire

Ajouter la tranche « Langues et lisibilité » dans les trois DOCX, en reliant
les propriétés vérifiables du document aux manipulations Word et Writer.

## Critères d’acceptation

- [ ] Les trois DOCX portent le même contenu éditorial pour `P-15` à `P-18`.
- [ ] Les deux fichiers de départ contiennent les mêmes défauts de langue
  principale et de passage en langue différente.
- [ ] Le corrigé déclare une langue cohérente dans les propriétés, les styles et
  le passage concerné.
- [ ] Les styles du corrigé utilisent une police sans sérif, un corps utile
  d’au moins 12 points, un interligne d’au moins 1,15 et un alignement à gauche.
- [ ] Les majuscules sont obtenues par mise en forme à partir de mots saisis
  normalement et les accents sont conservés.
- [ ] Les sigles et acronymes sont développés à la première occurrence.
- [ ] La procédure active la vérification orthographique des mots en majuscules.
- [ ] Les procédures Word et Writer correspondent aux versions qui seront
  réellement utilisées pendant la recette.

## Preuves attendues

- [ ] `make sami` régénère les trois DOCX.
- [ ] Les tests XML couvrent langues, styles, tailles, espacements, alignement
  et propriétés de casse.
- [ ] La lisibilité et les chemins de menus Word sont couverts par la porte
  humaine T09a ; les chemins Word et Writer sont rejoués sur les versions
  installées dans T16.

## À préserver

- Les stations 1 à 3 déjà migrées.
- Le contenu éditorial identique entre les trois versions.

## Hors périmètre

- Finaliser les métadonnées, le vérificateur ou l’export PDF.
- Réduire la taille du texte pour contraindre artificiellement la pagination.
