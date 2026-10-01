# T09 — Aligner les mémos et les notes formateur

**Statut :** `completed` — 2 octobre 2026

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T07](T07-docx-station-5-et-prototype.md).

**Débloque :** [T15](T15-aligner-le-pack-et-les-documents-igpde.md).

## À construire

Réconcilier les mémos Word et Writer et les notes formateur avec les cinq
stations, sans créer une troisième source narrative concurrente du guide Sami.
La note formateur active est
`livrables-IGPDE-2026-102846/Formateur/_alex/formation-102846-octobre-2026-bureautique.md`.

## Critères d’acceptation

- [x] Les mémos Word et Writer conservent un plan lisible mais référencent les
  identifiants de la matrice pour chaque procédure couverte.
- [x] Word bureau sous Windows reste le parcours principal.
- [x] Writer sous Windows fournit les procédures correspondantes et signale
  explicitement toute différence de version encore inconnue.
- [x] Les mémos couvrent la vérification, l’export PDF et le contrôle
  post-export sans enseigner la remédiation avancée dans Acrobat Pro.
- [x] Les notes formateur décrivent les 90 minutes, les cinq stations, le choix
  du fichier guidé ou autonome et la distribution progressive des livrables.
- [x] Les notes couvrent les contrôles `S` dans la checklist et le débrief,
  sans les transformer en manipulation obligatoire.
- [x] Les durées des notes formateur reprennent les sept blocs de la matrice et
  leur somme vaut exactement 90 minutes.
- [x] Le corrigé de référence n’est distribué qu’à la fin, pendant la marge et
  la remise.
- [x] Les notes répartissent l’animation entre les deux formateurs et leur
  synthèse commune au fil des stations, sans corriger à la place des binômes.
- [x] Les cartes WCAG sont reliées informellement aux critères pendant le
  préambule et ne servent pas d’évaluation.
- [x] Les synthèses techniques sont intégrées aux stations ; la synthèse
  générale de 12 h à 12 h 15 reste distincte.
- [x] Les anciennes consignes de 25 ou 30 minutes, erreurs cachées, diagnostic
  sans checklist et quiz final ont disparu des sources actives.
- [x] Les mémos et la note formateur active ne présentent plus `#767676` ou
  `4,48` comme un échec de contraste ; les seuils et conclusions viennent d’un
  calcul cohérent avec la matrice.
- [x] La distribution est sans ambiguïté : DOCX de départ choisi, checklists et
  cartes disponibles au début ; DOCX corrigé de référence remis seulement à la
  fin.

## Preuves attendues

- [x] Les identifiants présents dans les mémos et notes sont tous connus de la
  matrice et couvrent les sections attendues.
- [x] Un test compare les durées des notes à la section `sequence` de la
  matrice et échoue si le total diffère de 90 minutes.
- [x] `make pdf` régénère les deux mémos en PDF/UA-1.
- [x] La recherche des anciens contrats ne remonte aucune occurrence active non
  autorisée dans `fiche-pratique/memo-word.md`,
  `fiche-pratique/memo-libreoffice-writer.md`, la note formateur active et le
  pointeur de checklist retiré. La recherche globale reste portée par T15.
- [ ] Les chemins Word et Writer sont vérifiés sur les versions installées dans
  T16.

## Réalisation et vérifications

- Les deux mémos suivent les cinq stations et référencent, dans l’ordre, les
  contrôles `P-01` à `P-20`, puis `C-01` et `C-02`. Les contrôles `S` restent
  hors des mémos conformément à la matrice.
- La note formateur reprend les sept blocs canoniques, les rôles des deux
  formateurs, le choix guidé ou autonome et la distribution progressive. Les
  durées totalisent exactement 90 minutes.
- Le cycle TDD a d’abord produit 6 échecs attendus, puis 7 réussites sur le
  contrat T09. La campagne ciblée matrice, mémos et PDF/UA totalise 72 tests
  réussis.
- `make pdf` a produit les mémos Word et Writer en PDF/UA-1. Les deux PDF font
  10 pages, sont balisés, sans élément suspect, et leurs copies du pack sont
  identiques aux sorties de `fiche-pratique/`.
- La relecture visuelle des 20 pages n’a montré ni débordement ni page
  anormalement vide.
- `make fraicheur-pack` est vert. `make verifier` est vert avec 235 tests
  réussis, 5 ignorés, puis la validation métier et les contrôles du dépôt
  réussis.
- **Non vérifié à ce stade** : les libellés et chemins réels dans Word et Writer
  sous Windows. Cette preuve humaine appartient à T09a et T16.

## À préserver

- Le plan utile des mémos existants et leurs images encore exactes.
- Les notes des autres parties de la formation.

## Hors périmètre

- Réécrire le guide Sami dans les mémos.
- Modifier les slides ou les documents administratifs IGPDE.
