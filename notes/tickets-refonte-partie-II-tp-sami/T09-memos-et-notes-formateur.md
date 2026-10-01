# T09 — Aligner les mémos et les notes formateur

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T07](T07-docx-station-5-et-prototype.md).

**Débloque :** [T09a](T09a-recetter-prototype-90-minutes.md) et
[T15](T15-aligner-le-pack-et-les-documents-igpde.md).

## À construire

Réconcilier les mémos Word et Writer et les notes formateur avec les cinq
stations, sans créer une troisième source narrative concurrente du guide Sami.
La note formateur active est
`livrables-IGPDE-2026-102846/Formateur/_alex/formation-102846-octobre-2026-bureautique.md`.

## Critères d’acceptation

- [ ] Les mémos Word et Writer conservent un plan lisible mais référencent les
  identifiants de la matrice pour chaque procédure couverte.
- [ ] Word bureau sous Windows reste le parcours principal.
- [ ] Writer sous Windows fournit les procédures correspondantes et signale
  explicitement toute différence de version encore inconnue.
- [ ] Les mémos couvrent la vérification, l’export PDF et le contrôle
  post-export sans enseigner la remédiation avancée dans Acrobat Pro.
- [ ] Les notes formateur décrivent les 90 minutes, les cinq stations, le choix
  du fichier guidé ou autonome et la distribution progressive des livrables.
- [ ] Les notes couvrent les contrôles `S` dans la checklist et le débrief,
  sans les transformer en manipulation obligatoire.
- [ ] Les durées des notes formateur reprennent les sept blocs de la matrice et
  leur somme vaut exactement 90 minutes.
- [ ] Le corrigé de référence n’est distribué qu’à la fin, pendant la marge et
  la remise.
- [ ] Les notes répartissent l’animation entre les deux formateurs et leur
  synthèse commune au fil des stations, sans corriger à la place des binômes.
- [ ] Les cartes WCAG sont reliées informellement aux critères pendant le
  préambule et ne servent pas d’évaluation.
- [ ] Les synthèses techniques sont intégrées aux stations ; la synthèse
  générale de 12 h à 12 h 15 reste distincte.
- [ ] Les anciennes consignes de 25 ou 30 minutes, erreurs cachées, diagnostic
  sans checklist et quiz final ont disparu des sources actives.
- [ ] Les mémos et la note formateur active ne présentent plus `#767676` ou
  `4,48` comme un échec de contraste ; les seuils et conclusions viennent d’un
  calcul cohérent avec la matrice.
- [ ] La distribution est sans ambiguïté : DOCX de départ choisi, checklists et
  cartes disponibles au début ; DOCX corrigé de référence remis seulement à la
  fin.

## Preuves attendues

- [ ] Les identifiants présents dans les mémos et notes sont tous connus de la
  matrice et couvrent les sections attendues.
- [ ] Un test compare les durées des notes à la section `sequence` de la
  matrice et échoue si le total diffère de 90 minutes.
- [ ] `make pdf` régénère les deux mémos en PDF/UA-1.
- [ ] La recherche des anciens contrats ne remonte aucune occurrence active non
  autorisée dans `fiche-pratique/memo-word.md`,
  `fiche-pratique/memo-libreoffice-writer.md`, la note formateur active et le
  pointeur de checklist retiré. La recherche globale reste portée par T15.
- [ ] Les chemins Word sont vérifiés dans T09a, puis les chemins Word et Writer
  sur les versions installées dans T16.

## À préserver

- Le plan utile des mémos existants et leurs images encore exactes.
- Les notes des autres parties de la formation.

## Hors périmètre

- Réécrire le guide Sami dans les mémos.
- Modifier les slides ou les documents administratifs IGPDE.
