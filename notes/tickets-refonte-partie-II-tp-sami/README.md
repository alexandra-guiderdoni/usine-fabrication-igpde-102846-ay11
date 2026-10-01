# Tickets — Refonte de la partie II et du TP Sami

Source de vérité : [PRD validé](../prd-refonte-partie-II-tp-sami.md).

Ce dossier constitue le tracker local du chantier. Le statut `ready-for-agent`
signifie que le périmètre est spécifié ; `ready-for-human` signale une porte
humaine prête mais non exécutée. Un ticket ne doit cependant pas commencer tant
que ses blocages ne sont pas levés.

Aucune issue GitHub n’est créée par ce découpage. L’implémentation reste dans le
worktree isolé jusqu'à sa vérification. Par exception explicite du 2 octobre
2026, T01 à T09 et le protocole T09a peuvent être fusionnés dans `main` avant
la recette réelle. Cette exception ne débloque pas T10 et n'autorise aucune
livraison à l'IGPDE.

## Frontier initiale

- [T01 — Verrouiller le chantier et inventorier l’existant](T01-verrouiller-et-inventorier.md)

Après T07, T08 et T09 peuvent avancer en parallèle. T09a vérifie ensuite le
prototype complet : un binôme novice réalise le parcours guidé en 90 minutes,
puis un essai distinct vérifie le parcours autonome avant toute réécriture du deck. Les
tickets du deck restent séquentiels afin d’éviter les conflits sur son ordre,
ses tests et sa cohérence pédagogique.

## Tickets et blocages

1. [T01 — Verrouiller le chantier et inventorier l’existant](T01-verrouiller-et-inventorier.md) — aucun blocage.
2. [T02 — Introduire la matrice pédagogique canonique](T02-matrice-pedagogique-canonique.md) — bloqué par T01.
3. [T03 — Migrer la station 1 dans les trois DOCX](T03-docx-station-1.md) — bloqué par T02.
4. [T04 — Migrer la station 2 dans les trois DOCX](T04-docx-station-2.md) — bloqué par T03.
5. [T05 — Migrer la station 3 dans les trois DOCX](T05-docx-station-3.md) — bloqué par T04.
6. [T06 — Migrer la station 4 dans les trois DOCX](T06-docx-station-4.md) — bloqué par T05.
7. [T07 — Finaliser la station 5 et le prototype DOCX](T07-docx-station-5-et-prototype.md) — bloqué par T06.
8. [T08 — Générer les checklists accessibles](T08-checklists-accessibles.md) — bloqué par T07.
9. [T09 — Aligner les mémos et les notes formateur](T09-memos-et-notes-formateur.md) — bloqué par T07.
10. [T09a — Recetter le prototype complet en 90 minutes](T09a-recetter-prototype-90-minutes.md) — protocole validé ; recette humaine réelle à exécuter.
11. [T10 — Reconstruire l’ouverture du deck et la station 1](T10-deck-ouverture-et-station-1.md) — bloqué par T09a.
12. [T11 — Construire les slides de la station 2](T11-deck-station-2.md) — bloqué par T10.
13. [T12 — Construire les slides de la station 3](T12-deck-station-3.md) — bloqué par T11.
14. [T13 — Construire les slides de la station 4](T13-deck-station-4.md) — bloqué par T12.
15. [T14 — Finaliser le deck de la partie II et la synthèse](T14-deck-station-5-et-synthese.md) — bloqué par T13.
16. [T15 — Aligner le pack et les documents IGPDE](T15-aligner-le-pack-et-les-documents-igpde.md) — bloqué par T08, T09 et T14.
17. [T16 — Exécuter la recette intégrée sous Windows](T16-recette-integree-windows.md) — bloqué par T15.

## Invariants communs

- Étendre les générateurs, composants et commandes existants ; ne créer aucun
  moteur concurrent.
- Modifier les sources, jamais les DOCX, PDF ou PPTX générés à la main.
- Préserver le quiz diagnostic Documents A/B et supprimer le quiz final.
- Maintenir le TP à 90 minutes et la synthèse générale de 12 h à 12 h 15 hors
  de ce minutage.
- Distribuer au début seulement le DOCX de départ choisi, les checklists et les
  ressources prévues pour le préambule ; remettre le DOCX corrigé de référence
  uniquement pendant la remise finale.
- Ne pas modifier les parties Web et réseaux sociaux, sauf référence devenue
  fausse à cause de la renumérotation.
- Ne jamais assimiler un résultat automatique sans erreur à une preuve de
  conformité.
- Archiver dans Git uniquement une synthèse de recette expurgée ; les captures
  et rapports bruts contenant des données personnelles restent hors du dépôt public.

## Condition de livraison

T16 produit les preuves de recette. Il ne pousse pas et ne remet aucun paquet
à l’IGPDE.

La fusion anticipée de T01 à T09 dans `main` ne vaut ni réalisation de T09a,
ni autorisation de T10, ni validation du paquet final.

Si les sources du kit pratique changent après la porte T09a, le parcours humain
affecté doit être rejoué. Sinon, T16 peut réutiliser les preuves datées de T09a
sans répéter artificiellement le même essai de 90 minutes.
