# T04 — Migrer la station 2 dans les trois DOCX

**Statut :** `completed` — génération, tests XML et contre-revue vérifiés le
1er octobre 2026 ; les contrôles humains restent assignés à T09a et T16.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T03](T03-docx-station-1.md).

**Débloque :** [T05](T05-docx-station-3.md).

## À construire

Ajouter la tranche « Contenus et liens » pilotée par la matrice dans les trois
DOCX, avec des actions réellement praticables dans Word et des procédures
Writer détaillées dans le guide corrigé.

## Critères d’acceptation

- [x] Les trois DOCX portent le même contenu éditorial pour `P-06` à `P-11`.
- [x] Une image informative simple demande une alternative rédigée par le
  binôme, sans alternative automatique présentée comme acceptable.
- [x] Une image complexe associe alternative courte et description détaillée
  adjacente.
- [x] Une image redondante est traitée comme décorative, avec une procédure
  Writer adaptée à la version réellement testée.
- [x] Le texte sous forme d’image est remplacé par du texte sélectionnable dans
  le corrigé.
- [x] Les liens sont autonomes, visuellement identifiables et complétés par le
  format, le poids et la langue lorsque ces informations sont connues.
- [x] `P-11` reste expliqué dans la station et dans la version guidée, sans
  filigrane superposé dans les DOCX ; le corrigé illustre la reprise du statut
  dans le corps.
- [x] Chaque occurrence fautive possède une piste fiable dans la version
  guidée.

## Preuves attendues

- [x] `make sami` régénère les trois documents sans sortie manquante.
- [x] Les tests XML distinguent alternative informative, description complexe
  et marqueur décoratif.
- [x] Les tests confirment la présence de vrai texte, de liens explicites et de
  l’information essentielle dans le corps, ainsi que l’absence du filigrane
  « CONFIDENTIEL » dans les trois DOCX.
- [x] La visibilité et l’ancrage des pistes sont couverts par le scénario
  humain Word de T09a, puis par la recette finale T16.

## À préserver

- Les stations déjà migrées et les contenus non encore migrés.
- L’égalité éditoriale des trois versions.

## Hors périmètre

- Modifier les couleurs, tableaux, langues ou procédures d’export.
- Modifier les slides.

## Décision de lisibilité — 2 octobre 2026

La recette humaine a montré que le filigrane « CONFIDENTIEL » rendait le texte
du document difficile à lire. Il est supprimé des versions inaccessible et
guidée, et le générateur ne doit plus l’injecter. Cette suppression ne retire
pas l’enseignement de `P-11` : la règle reste présentée dans la station, la
version guidée et la checklist, tandis que le corrigé montre comment placer
l’information essentielle dans le corps du document.

## Preuves d’exécution

- `make sami` a régénéré les trois DOCX historiques depuis la matrice, sans
  retouche manuelle des binaires.
- Les tests ciblés de matrice, de DOCX, de fraîcheur et de paquet comptent
  80 réussites. Ils vérifient notamment l’ordre canonique de `P-06` à `P-11`,
  les alternatives, la description complexe déclarée comme transformation,
  le marqueur décoratif, le retrait de l’image de texte, le lien ciblé et
  le traitement de `P-11` sans filigrane superposé.
- Les six pistes sont ancrées sur les occurrences réelles dans le DOCX guidé :
  images pour `P-06`, `P-07` et `P-09`, pictogramme pour `P-08`, paragraphe du
  lien pour `P-10` et premier paragraphe d’introduction pour `P-11`.
- `make verifier` compte 199 tests réussis et 5 ignorés ; la validation du site
  et les contrôles du dépôt passent. Le seul avertissement concerne le cache
  pytest non inscriptible dans le bac à sable.
- `make fraicheur-pack` ne signale aucun des trois DOCX Sami. La cible globale
  reste rouge à cause de la grille d’audit XLSX, antérieure à son générateur et
  hors du périmètre T04.
- La première revue ShipGuard a conclu `NO-GO` sur trois P1 et deux P2 : preuve
  P-10 tronquée, transformation P-07 non déclarée, commentaires mal ancrés,
  faux sommaire incohérent et tests P-09/P-10 trop globaux. Après correction
  test-first, la contre-revue conclut `GO`, confirme les cinq constats fermés et
  ne relève aucun nouveau P0 ou P1 directement introduit.
- Restent `NOT VERIFIED` humainement : affichage des commentaires superposés
  sur l’introduction, visibilité et ergonomie des commentaires sur les images
  et le lien, menus Word et Writer sous Windows, comportement du marqueur
  décoratif avec les technologies d’assistance, pertinence des alternatives,
  pagination et rendu visuel final. Ces preuves appartiennent à T09a et T16.
