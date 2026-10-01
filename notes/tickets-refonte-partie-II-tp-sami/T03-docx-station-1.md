# T03 — Migrer la station 1 dans les trois DOCX

**Statut :** `completed` — génération, tests XML et contre-revue vérifiés le
1er octobre 2026 ; les contrôles humains restent assignés à T09a et T16.

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T02](T02-matrice-pedagogique-canonique.md).

**Débloque :** [T04](T04-docx-station-2.md).

## À construire

Faire de la station « Structurer et naviguer » une première tranche verticale
pilotée par la matrice dans les trois DOCX. Le générateur existant reste
l’unique point de production.

## Critères d’acceptation

- [x] Les trois DOCX portent le même contenu éditorial pour `P-01` à `P-05`.
- [x] Les deux fichiers de départ contiennent les mêmes défauts de styles,
  hiérarchie, sommaire, listes et mise en forme.
- [x] Le fichier avec pistes contient une aide par occurrence sans corriger le
  défaut à la place du binôme.
- [x] Le corrigé applique les styles, une hiérarchie sans saut, un sommaire
  actualisable, des listes natives et une mise en forme propre.
- [x] `P-05` couvre explicitement les paragraphes vides, espaces successifs,
  tabulations, retours forcés, sauts de page et colonnes simulées, remplacés
  par les fonctions adaptées.
- [x] Le volet de navigation dispose de la hiérarchie de styles attendue ; son
  rendu réel sous Word reste à vérifier humainement dans T09a et T16.
- [x] Toute piste de niveau document est ancrée dans un paragraphe stable du
  corps, commence par `Document —` et n’est jamais placée dans un en-tête, un
  pied de page ou un objet qui la masquerait dans Word.
- [x] Les parties non encore migrées restent fonctionnelles jusqu’aux tickets
  suivants.
- [x] La matrice devient une entrée du générateur Sami existant et de son
  contrôle de fraîcheur : sa modification rend les trois DOCX obsolètes.
- [x] Le générateur n’embarque plus une seconde liste normative d’identifiants,
  de libellés ou d’ordre des stations ; un test structurel prouve la
  consommation directe de la matrice.

## Preuves attendues

- [x] `make sami` régénère les trois DOCX sous leurs noms historiques.
- [x] Les tests XML couvrent styles, niveaux de titres, listes, sommaire,
  paragraphes vides, espaces, tabulations, retours, sauts et colonnes simulées.
- [x] Les tests comparent les occurrences attendues entre inaccessible, guidé
  et corrigé.
- [x] Le volet de navigation et la mise à jour du sommaire figurent dans le
  scénario humain Word de T09a, puis dans la recette finale T16.

## À préserver

- Le contenu déjà fonctionnel hors station 1.
- L’identité éditoriale entre les trois versions.

## Hors périmètre

- Corriger les images, couleurs, langues ou contrôles de publication.
- Modifier le deck ou les checklists.

## Preuves d’exécution

- `make sami` a régénéré les trois DOCX historiques depuis la matrice, sans
  retouche manuelle des binaires.
- Les tests ciblés de matrice, de DOCX, de fraîcheur et de paquet comptent
  70 réussites. Ils vérifient notamment les contenus communs de `P-01` à
  `P-05`, les cinq pistes, la numérotation multiniveau, les listes, le champ de
  sommaire, les artifices de mise en page, les commentaires hors en-têtes et
  la conservation du défaut `ANNEXES` jusqu’à sa migration.
- `make verifier` compte 189 tests réussis et 5 ignorés ; la validation du site
  et les contrôles du dépôt passent. Le seul avertissement concerne le cache
  pytest non inscriptible dans le bac à sable.
- `make fraicheur-pack` ne signale aucun des trois DOCX Sami. La cible globale
  reste rouge à cause de la grille d’audit XLSX, antérieure à son générateur et
  hors du périmètre T03.
- La première revue ShipGuard a conclu `NO-GO` sur six écarts. Après correction
  test-first, sa contre-revue conclut `GO` et confirme les six constats fermés,
  sans nouveau défaut directement introduit.
- Restent `NOT VERIFIED` humainement : rendu réel de la numérotation et mise à
  jour du sommaire dans Word, volet de navigation, annonce des listes par un
  lecteur d’écran, rendu des sauts et colonnes, comportement sous Writer et
  mise en page visuelle finale. Ces preuves appartiennent à T09a et T16.
