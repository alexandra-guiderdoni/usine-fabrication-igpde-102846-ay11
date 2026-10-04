# T16 — Exécuter la recette intégrée sous Windows

**Statut :** `completed` — recette du 3 octobre 2026, clôture demandée par Alex le 4 octobre 2026.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T15](T15-aligner-le-pack-et-les-documents-igpde.md).

**Débloque :** aucun ticket de ce lot.

## Clôture

Alex confirme que la recette humaine T16, notamment les parcours sous Word et
Writer Windows, le contrôle du PDF et la relecture du support dans PowerPoint,
a été réalisée le 3 octobre 2026 avec un résultat satisfaisant. Il demande la
clôture de T16 et indique que l'envoi des livrables à l'IGPDE reste à effectuer.
Cette validation humaine est rapportée par Alex ; les relevés détaillés et le
minutage ne sont pas versés dans ce dépôt public. Les contrôles locaux du
4 octobre ont par ailleurs donné
`make verifier` réussi (282 tests) et une QA PPTX `CONVERGED`.

Les listes ci-dessous conservent le protocole prévu ; elles ne constituent pas
un registre de preuves indépendantes de cette déclaration.

## Objet initial

Exécuter la recette automatisée et humaine de bout en bout, corriger les écarts
observés dans leur ticket d’origine et constituer la preuve de validation finale.

## Critères de la recette

- Deux parcours distincts sont couverts : le parcours guidé chronométré
  avec un binôme novice et le parcours fonctionnel autonome depuis le DOCX
  inaccessible. T09a ayant été annulé, T16 constitue l'unique porte humaine et
  doit produire toutes les preuves correspondantes.
- Les procédures sont vérifiées dans Microsoft Word bureau sous Windows et
  LibreOffice Writer sous Windows sur les versions installées.
- Le résultat du vérificateur Word est conservé pour le fichier inaccessible
  et pour le fichier corrigé ; les alertes pertinentes sont traitées et toute
  alerte résiduelle est expliquée.
- Le vrai DOCX de travail est exporté en PDF puis contrôlé avec PAC, ou
  Acrobat Pro en alternative, pour le titre, la langue, les balises et l’ordre
  de lecture.
- La checklist humaine est renseignée progressivement et jointe aux preuves.
- Le parcours guidé chronométré produit en 90 minutes au plus un DOCX au
  nom descriptif, une checklist renseignée et un PDF exporté puis contrôlé. Le
  parcours autonome produit les mêmes types de preuves sans devenir une
  seconde porte chronométrée arbitraire ; le corrigé de référence est remis
  seulement à la fin.
- Les slides et le guide sont relus visuellement, y compris leurs
  alternatives, leur ordre de lecture et leur lisibilité.
- Tout écart conduit à une correction de la source et à la reprise de la
  vérification concernée, sans retouche manuelle d’un binaire généré.

## Preuves prévues au protocole

- La recette automatisée est exécutée dans cet ordre : `make sami`,
  `make checklist`, `make pdf`, `make deck`, `make fraicheur-pack`, `make qa`,
  `make pack`, puis `make verifier` sur le paquet final.
- `.qa/qa-pptx-report.md` porte le statut `CONVERGED`.
- Les relevés Word, Writer, PAC ou Acrobat Pro, le chronométrage et la
  relecture visuelle sont résumés dans `notes/recette-tp-sami/README.md` sans
  donnée personnelle ; les preuves brutes sensibles restent hors du dépôt
  public.
- La recette vérifie le moment réel de distribution : DOCX de départ,
  checklist et ressources d’appui au début ; DOCX corrigé de référence pendant
  la remise finale seulement.
- Une validation humaine explicite autorise seulement ensuite la remise du
  nouveau paquet à l'IGPDE.

## À préserver

- Le tag de repli `avant-refonte-tp-sami-2026-10-01`, qui reste immuable.
- Les sources T01 à T15 déjà fusionnées dans `main` et le paquet préparatoire,
  qui ne devient livrable qu'après la décision humaine finale.

## Hors périmètre

- Publier le site pendant cette recette Windows.
- Remettre une sortie partielle à l’IGPDE.
