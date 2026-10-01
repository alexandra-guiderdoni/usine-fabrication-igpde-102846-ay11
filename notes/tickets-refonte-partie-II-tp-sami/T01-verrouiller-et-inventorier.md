# T01 — Verrouiller le chantier et inventorier l’existant

**Statut :** `completed` — inventaire validé par Alex le 1er octobre 2026.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** aucun — frontier initiale.

**Débloque :** [T02](T02-matrice-pedagogique-canonique.md).

## À construire

Établir un point de départ exécutable et non contradictoire avant toute refonte.
Le ticket confirme le repli, retire l’autorité des anciennes règles et produit
l’inventaire décisionnel des modules actuels de la partie II dans
`_source/inventaire-refonte-partie-II.md`.

## Critères d’acceptation

- [x] Le tag `avant-refonte-tp-sami-2026-10-01` existe, sa cible est consignée
  et le tag n’est ni déplacé ni recréé.
- [x] `AGENTS.md` ne prescrit plus 21 critères, 25 minutes ni un diagnostic
  sans checklist ; il ne fige pas un nouveau total de slides.
- [x] `_source/exercice-sami-spec.md` et `_source/exercice-sami-diff.md`
  affichent un bandeau d’obsolescence explicite : le PRD validé fait autorité
  jusqu’à T02, puis la matrice canonique devient la source normative.
- [x] Le contenu historique de ces deux fichiers est conservé pendant la phase
  d’expansion ; leurs anciens contrats sont des exceptions temporaires
  documentées jusqu’à leur retrait dans T07 et ne guident aucune nouveauté.
- [x] `_source/references/martine-sutra-couverture.md` décrit localement les
  codes de couverture issus des thèmes listés au §16 du PRD, sans prétendre
  reproduire le support externe absent du clone et sans chemin personnel.
- [x] `_source/references/formation-accessibilite-word.md` porte un bandeau qui
  le classe comme apport pédagogique non normatif et renvoie vers le PRD ; sa
  liste de 21 réflexes ne devient pas une cinquième source active.
- [x] `_source/inventaire-refonte-partie-II.md` classe chaque module actuel de
  03 à 26c `conserver`, `fusionner`,
  `remplacer` ou `supprimer`, avec sa justification et ses tests dépendants.
- [x] Toute suppression autre que le quiz final reste soumise à validation
  humaine.
- [x] L’inventaire est explicitement validé par un humain avant T10.
- [x] Les tests et documents qui figent un total global ou une position absolue
  de slide sont inventoriés avant le travail sur le deck, dont les parties I à
  IV, le README racine, `contraintes.md`, `architecture-c4-slides.md`, le README
  du site publié et celui du paquet.
- [x] L'environnement d'exécution est consigné ; si `.venv` est absent,
  l’installation documentée est réalisée avant toute génération, puis le
  verdict initial de `make verifier` est noté sans masquer les échecs existants.

## Preuves attendues

- [x] La cible du tag est obtenue par Git et citée dans le compte rendu.
- [x] Une recherche bornée des anciens contrats utilise la liste du PRD et
  distingue l’exception historique `ex-102638` et les exceptions temporaires de
  la spécification et de la liste des différences jusqu’à T07.
- [x] Le diff ne contient aucun binaire généré ni changement hors du cadrage et
  de l’inventaire.
- [x] Les liens et les formulations françaises de chaque Markdown modifié sont
  relus ; aucun vérificateur d’accents local au dépôt n’est supposé présent.

## À préserver

- Les noms des trois DOCX et le générateur Sami existant.
- Le quiz diagnostic Documents A/B et ses tests.
- Les autres parties de la formation.

## Hors périmètre

- Créer la matrice ou modifier le générateur.
- Réécrire les slides.
- Fusionner, pousser ou livrer.
