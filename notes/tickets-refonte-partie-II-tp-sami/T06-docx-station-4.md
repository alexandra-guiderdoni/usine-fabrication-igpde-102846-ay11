# T06 — Migrer la station 4 dans les trois DOCX

**Statut :** `completed` — 1er octobre 2026

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T05](T05-docx-station-3.md).

**Débloque :** [T07](T07-docx-station-5-et-prototype.md).

## À construire

Ajouter la tranche « Langues et lisibilité » dans les trois DOCX, en reliant
les propriétés vérifiables du document aux manipulations Word et Writer.

## Critères d’acceptation

- [x] Les trois DOCX portent le même contenu éditorial pour `P-15` à `P-18`,
  sous réserve des transformations éditoriales déclarées pour `P-17` et `P-18`.
- [x] Les deux fichiers de départ contiennent les mêmes défauts de langue
  principale et de passage en langue différente.
- [x] Le corrigé déclare une langue cohérente dans les propriétés, les styles et
  le passage concerné.
- [x] Les styles du corrigé utilisent une police sans sérif, un corps utile
  d’au moins 12 points, un interligne d’au moins 1,15 et un alignement à gauche.
- [x] Les majuscules sont obtenues par mise en forme à partir de mots saisis
  normalement et les accents sont conservés.
- [x] Les sigles et acronymes sont développés à la première occurrence.
- [x] La procédure documente l’activation de la vérification orthographique des
  mots en majuscules.
- [x] Les procédures Word et Writer sont rédigées pour les versions Windows
  prévues ; leur rejeu réel reste confié aux portes humaines T09a et T16.

## Preuves attendues

- [x] `make sami` régénère les trois DOCX.
- [x] Les tests XML couvrent langues, styles, tailles, espacements, alignement
  et propriétés de casse.
- [x] La lisibilité et les chemins de menus Word sont confiés à la porte
  humaine T09a ; les chemins Word et Writer sont rejoués sur les versions
  installées dans T16.

## Réalisation et preuves

- TDD : les contrôles ajoutés ont d’abord échoué sur les textes utiles à 9
  points et sur la transformation `P-17` absente, puis sont passés après
  correction.
- `make sami` : les graphiques et les trois DOCX ont été régénérés.
- Suite ciblée Sami : `88 passed`.
- `make verifier` : `207 passed`, `5 skipped`, validation métier et contrôles du
  dépôt réussis.
- Intégrité : `unzip -t` ne signale aucune erreur sur les trois DOCX et
  `git diff --check` est propre.
- Revue indépendante ciblée : `GO`, aucun P0 ni P1 ; l’OOXML du corrigé porte
  bien les textes utiles d’en-tête et de pied à 12 points et la transformation
  `P-17` est déclarée puis testée.
- `make fraicheur-pack` reste rouge uniquement pour les deux copies de
  l’ancienne grille XLSX, hors périmètre de T06 ; les ressources Sami ne sont
  pas signalées.

## Non vérifié dans T06

- Le rendu, la pagination et la lisibilité réels sous Microsoft Word et
  LibreOffice Writer pour Windows.
- Le rejeu des chemins de menus et le comportement du correcteur
  orthographique sur les versions installées.
- L’actualisation des champs de pied de page par les applications bureautiques.

Ces contrôles restent affectés aux portes humaines T09a et T16.

## À préserver

- Les stations 1 à 3 déjà migrées.
- Le contenu éditorial identique entre les trois versions.

## Hors périmètre

- Finaliser les métadonnées, le vérificateur ou l’export PDF.
- Réduire la taille du texte pour contraindre artificiellement la pagination.
