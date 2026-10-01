# T07 — Finaliser la station 5 et le prototype DOCX

**Statut :** `completed` — 1er octobre 2026

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T06](T06-docx-station-4.md).

**Débloque :** [T08](T08-checklists-accessibles.md) et
[T09](T09-memos-et-notes-formateur.md).

## À construire

Achever la migration des trois DOCX avec la station « Finaliser et publier » et
retirer les anciens contenus normatifs du générateur. Le chronométrage du kit
complet intervient seulement après la checklist, les mémos et les notes.

## Critères d’acceptation

- [x] `P-19`, `P-20`, `C-01` et `C-02` sont présents dans les trois versions
  avec les différences prévues par la matrice.
- [x] Le corrigé renseigne titre, auteur et langue ; le générateur préserve les
  trois noms de sortie historiques. `P-19` demande au participant de donner un
  nom descriptif à sa copie de travail, action humaine prouvée dans T09a et T16.
- [x] Le vérificateur Word est présenté comme une aide ; toute alerte résiduelle
  est expliquée et la vérification humaine reste obligatoire.
- [x] Le guide décrit l’export PDF avec propriétés, balises et signets, puis le
  contrôle PAC ou Acrobat Pro.
- [x] Le corrigé suit l’ordre des stations, détaille Word et Writer et produit
  24 pages dans LibreOffice sans compression artificielle. Le volume sous Word
  et en A4 reste à confirmer dans T09a et T16.
- [x] Chaque point du corrigé présente le problème, l’impact, la règle, la
  procédure Word, la procédure Writer, la manipulation et la preuve de
  correction.
- [x] Aucune capture supplémentaire n’est introduite ; chaque image existante
  conserve le traitement alternatif prévu par sa station.
- [x] Le corrigé n’introduit aucune règle, procédure ou exemple absent des deux
  fichiers de départ.
- [x] Chaque commentaire du fichier guidé contient le problème, l’impact, la
  règle et la première action, sans corriger à la place du binôme.
- [x] Le nombre de commentaires du fichier guidé égale les occurrences prévues
  et son corps éditorial reste identique à l’inaccessible.
- [x] Les anciennes branches normatives du générateur sont retirées seulement
  lorsque toutes les sorties sont pilotées par la matrice.
- [x] Tous les motifs de la liste fermée du PRD ont disparu de la spécification
  et de la liste des différences ; l’historique utile est reformulé et les deux
  fichiers renvoient à la matrice pour les identifiants, libellés, niveaux et
  ordre.

## Preuves attendues

- [x] `make sami` produit les trois DOCX complets.
- [x] Les tests XML et les tests d’égalité éditoriale passent.
- [x] Un test négatif réinjecte au moins un défaut de chaque famille détectable
  dans le corrigé et échoue comme attendu.
- [x] Chaque défaut attendu est présent dans les deux fichiers de départ et
  absent du corrigé.
- [x] Les identifiants, libellés, niveaux et ordre de la spécification, de la
  liste des différences, du guide et des tests correspondent à la matrice.
- [x] Les contrôles d’intégrité ZIP et XML confirment trois DOCX lisibles ;
  l’ouverture dans Word sans réparation et la visibilité des commentaires sont
  portées par T09a, puis T16.

## Réalisation et preuves

- TDD : `P-19`, les contrôles sans occurrence, le retrait des anciens contrats,
  les marqueurs du générateur et la pagination ont chacun été observés en échec
  avant leur correction.
- `make sami` : les trois DOCX et les ressources graphiques ont été régénérés.
- Suite ciblée Sami : `95 passed`.
- `make verifier` : `214 passed`, `5 skipped`, validation métier et contrôles du
  dépôt réussis.
- Le test global confirme 19 commentaires pour 19 occurrences et une signature
  corps plus tableaux identique entre l’inaccessible et le fichier avec pistes.
- Le test négatif réinjecte un défaut de structure, de lien, de contraste, de
  typographie et de métadonnées ; chaque variante est rejetée.
- `unzip -t` ne signale aucune erreur sur les trois DOCX.
- Conversion de contrôle LibreOffice : PDF balisé de 24 pages, avec titre,
  sujet, auteur et mots-clés renseignés.
- Revue PDV : `GO`, sans bloqueur structurel.
- Revue indépendante : `GO`, aucun P0, P1 ou P2.
- `make fraicheur-pack` reste rouge uniquement pour les deux copies de
  l’ancienne grille XLSX, hors périmètre de T07 ; les ressources Sami ne sont
  pas signalées.

## Non vérifié dans T07

- L’ouverture sans réparation et la visibilité des commentaires dans Microsoft
  Word sous Windows.
- Le rendu et la pagination sous Word en A4 ; la mesure automatisée actuelle a
  été obtenue dans LibreOffice en format Letter.
- Le rejeu des chemins de menus Word et Writer, le vérificateur Word, PAC et
  Acrobat Pro.
- Le minutage avec un binôme novice.

Ces contrôles restent affectés aux portes humaines T09a et T16.

## Hors périmètre

- Générer les checklists, chronométrer le kit complet ou modifier les slides.
- Déclarer la conformité sur la seule base d’un vérificateur automatique.
