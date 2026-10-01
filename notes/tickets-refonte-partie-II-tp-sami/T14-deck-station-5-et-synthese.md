# T14 — Finaliser le deck de la partie II et la synthèse

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T13](T13-deck-station-4.md).

**Débloque :** [T15](T15-aligner-le-pack-et-les-documents-igpde.md).

## À construire

Construire la station « Finaliser et publier », intégrer la checklist, puis
terminer la matinée par une synthèse distincte avant la partie III.

## Critères d’acceptation

- [ ] La station couvre `P-19`, `C-01`, `P-20` et `C-02` : propriétés et nom
  du fichier, vérificateur Word, export PDF balisé, contrôle PAC ou Acrobat Pro
  et vérification humaine finale.
- [ ] Les données normatives de la station et des slides de checklist sont
  consommées directement depuis la matrice, sans inventaire parallèle.
- [ ] Les alertes pertinentes du vérificateur Word sont traitées et toute
  alerte résiduelle est expliquée ; l’absence d’alerte n’est pas assimilée à
  une preuve suffisante d’accessibilité.
- [ ] Les slides de checklist sont issues de la source consolidée et restent
  lisibles sans nombre arbitraire de slides.
- [ ] Le quiz diagnostic Documents A/B et sa réponse restent dans le préambule
  bref de la partie II.
- [ ] Le quiz final et sa correction sont supprimés sans être recréés sous un
  autre nom.
- [ ] Une à deux slides de synthèse de la matinée sont placées après la partie
  II et avant la partie III, hors des 90 minutes du TP.
- [ ] La synthèse consolide les acquis des parties I et II, accueille les
  questions et prépare la transition, sans identifiant `P`, `C` ou `S`.
- [ ] La partie II vise environ 20 à 30 slides sans réduire le texte ni
  surcharger une composition pour atteindre un total.
- [ ] Les notes formateur portent le minutage, les variantes guidée et autonome
  ainsi que les preuves attendues.
- [ ] La note formateur active
  `livrables-IGPDE-2026-102846/Formateur/_alex/formation-102846-octobre-2026-bureautique.md`
  est réalignée après la structure finale du deck et ne cite plus de slides
  obsolètes.
- [ ] Les tests d’ordre restent relatifs aux chapitres et aux stations, sans
  total global ni index absolu fragile.
- [ ] La migration réalisée dans T10 est vérifiée sur les parties I à IV et
  aucun test affecté ne réintroduit un numéro de slide ou un total global.
- [ ] Les références fragiles à « 138 slides » sont retirées ou rendues
  dynamiques dans `README.md`, `contraintes.md`, `architecture-c4-slides.md` et
  `publication-site/README.md` ; le deck généré reste la preuve observable de
  son nombre réel de slides.

## Preuves attendues

- [ ] Les tests ciblés du plan, des contenus, des notes et de la checklist
  passent.
- [ ] Un test de cohérence échoue si identifiant, libellé, niveau, station ou
  ordre divergent entre matrice, slides de station et slides de checklist.
- [ ] `make deck` produit le deck complet sans avertissement de pied de page.
- [ ] `make qa` produit `.qa/qa-pptx-report.md` avec le statut `CONVERGED`.
- [ ] La relecture humaine couvre toute la partie II, la synthèse et la
  transition vers la partie III.

## À préserver

- Les stations 1 à 4 validées dans les tickets précédents.
- Les autres parties du deck, hors renumérotation ou horaire rendu obsolète.

## Hors périmètre

- Refaire les parties Web ou réseaux sociaux.
- Enseigner la remédiation avancée d’un PDF dans Acrobat Pro.
