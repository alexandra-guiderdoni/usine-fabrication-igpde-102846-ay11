# T07 — Finaliser la station 5 et le prototype DOCX

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T06](T06-docx-station-4.md).

**Débloque :** [T08](T08-checklists-accessibles.md) et
[T09](T09-memos-et-notes-formateur.md).

## À construire

Achever la migration des trois DOCX avec la station « Finaliser et publier » et
retirer les anciens contenus normatifs du générateur. Le chronométrage du kit
complet intervient seulement après la checklist, les mémos et les notes.

## Critères d’acceptation

- [ ] `P-19`, `C-01`, `P-20` et `C-02` sont présents dans les trois versions
  avec les différences prévues par la matrice.
- [ ] Le corrigé renseigne titre, auteur et langue ; le générateur préserve les
  trois noms de sortie historiques. `P-19` demande au participant de donner un
  nom descriptif à sa copie de travail, action humaine prouvée dans T09a et T16.
- [ ] Le vérificateur Word est présenté comme une aide ; toute alerte résiduelle
  est expliquée et la vérification humaine reste obligatoire.
- [ ] Le guide décrit l’export PDF avec propriétés, balises et signets, puis le
  contrôle PAC ou Acrobat Pro.
- [ ] Le corrigé suit l’ordre des stations, détaille Word et Writer et vise 20
  à 30 pages sans compression artificielle.
- [ ] Chaque point du corrigé présente le problème, l’impact, la règle, la
  procédure Word, la procédure Writer, la manipulation et la preuve de
  correction.
- [ ] Les captures sont limitées à celles qui changent réellement l’action et
  chacune porte une alternative pertinente.
- [ ] Le corrigé n’introduit aucune règle, procédure ou exemple absent des deux
  fichiers de départ.
- [ ] Chaque commentaire du fichier guidé contient le problème, l’impact, la
  règle et la première action, sans corriger à la place du binôme.
- [ ] Le nombre de commentaires du fichier guidé égale les occurrences prévues
  et son corps éditorial reste identique à l’inaccessible.
- [ ] Les anciennes branches normatives du générateur sont retirées seulement
  lorsque toutes les sorties sont pilotées par la matrice.
- [ ] Tous les motifs de la liste fermée du PRD ont disparu de la spécification
  et de la liste des différences ; l’historique utile est reformulé et les deux
  fichiers renvoient à la matrice pour les identifiants, libellés, niveaux et
  ordre.

## Preuves attendues

- [ ] `make sami` produit les trois DOCX complets.
- [ ] Les tests XML et les tests d’égalité éditoriale passent.
- [ ] Un test négatif réinjecte au moins un défaut de chaque famille détectable
  dans le corrigé et échoue comme attendu.
- [ ] Chaque défaut attendu est présent dans les deux fichiers de départ et
  absent du corrigé.
- [ ] Les identifiants, libellés, niveaux et ordre de la spécification, de la
  liste des différences, du guide et des tests correspondent à la matrice.
- [ ] Les contrôles d’intégrité ZIP et XML confirment trois DOCX lisibles ;
  l’ouverture dans Word sans réparation et la visibilité des commentaires sont
  portées par T09a, puis T16.

## Hors périmètre

- Générer les checklists, chronométrer le kit complet ou modifier les slides.
- Déclarer la conformité sur la seule base d’un vérificateur automatique.
