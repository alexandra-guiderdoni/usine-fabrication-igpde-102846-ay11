# Tickets — Refonte de la partie II et du TP Sami

Source de vérité : [PRD validé](../prd-refonte-partie-II-tp-sami.md).

Ce dossier constitue le tracker local du chantier. Le statut `ready-for-agent`
signifie que le périmètre est spécifié ; `cancelled` signale un ticket abandonné
par décision humaine. Un ticket ne doit cependant pas commencer tant que ses
blocages ne sont pas levés.

Aucune issue GitHub n’est créée par ce découpage. Par décision explicite du
2 octobre 2026, T01 à T09 ont été fusionnés dans `main` et T10 a pu démarrer
sans exécution de T09a, faute de binôme disponible. T10 à T15 ont ensuite été
implémentés et vérifiés ; cette décision n'autorise aucune livraison à l'IGPDE.
Alex a ensuite déclaré la recette T16 du 3 octobre satisfaisante et demandé sa
clôture le 4 octobre. L'envoi des livrables reste à effectuer.

## Frontier initiale

- [T01 — Verrouiller le chantier et inventorier l’existant](T01-verrouiller-et-inventorier.md)

Après T07, T08 et T09 peuvent avancer en parallèle. La porte T09a prévue avant
le deck a été annulée faute de binôme disponible ; ses contrôles sont reportés
sur T16. Les tickets du deck restent séquentiels afin d’éviter les conflits sur
son ordre, ses tests et sa cohérence pédagogique.

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
10. [T09a — Recetter le prototype complet en 90 minutes](T09a-recetter-prototype-90-minutes.md) — annulé faute de binôme disponible ; protocole conservé.
11. [T10 — Reconstruire l’ouverture du deck et la station 1](T10-deck-ouverture-et-station-1.md) — terminé.
12. [T11 — Construire les slides de la station 2](T11-deck-station-2.md) — terminé.
13. [T12 — Construire les slides de la station 3](T12-deck-station-3.md) — terminé.
14. [T13 — Construire les slides de la station 4](T13-deck-station-4.md) — terminé.
15. [T14 — Finaliser le deck de la partie II et la synthèse](T14-deck-station-5-et-synthese.md) — terminé, relecture humaine finale reportée sur T16.
16. [T15 — Aligner le pack et les documents IGPDE](T15-aligner-le-pack-et-les-documents-igpde.md) — terminé ; quatre installeurs externes présents localement, hors Git.
17. [T16 — Exécuter la recette intégrée sous Windows](T16-recette-integree-windows.md) — clos sur validation humaine déclarée par Alex le 4 octobre 2026.

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

T16 consigne la validation humaine de la recette. Il ne pousse pas et ne remet
aucun paquet à l’IGPDE. L'envoi du paquet est une action distincte, encore à
effectuer.

L'annulation de T09a et l'autorisation de T10 ne valent pas validation du paquet
final. Les critères initialement répartis entre T09a et la recette finale ont
été repris dans T16 ; la clôture repose sur la déclaration d'Alex et non sur
des relevés détaillés consultables dans ce dépôt.
