# T05 — Migrer la station 3 dans les trois DOCX

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** [T04](T04-docx-station-2.md).

**Débloque :** [T06](T06-docx-station-4.md).

## À construire

Ajouter la tranche « Couleurs, graphiques et tableaux » dans les trois DOCX.
La correction doit être réalisable dans Word sans imposer un logiciel d’image
supplémentaire.

## Critères d’acceptation

- [ ] Les trois DOCX portent le même contenu éditorial pour `P-12` à `P-14`.
- [ ] Une couleur réellement non conforme est utilisée dans les deux fichiers
  de départ et sa correction est validée par calcul.
- [ ] Les seuils de 4,5:1 et 3:1 sont appliqués selon le type de contenu.
- [ ] Le défaut de couleur seule ne repose pas sur un mot qui transmet déjà à
  lui seul l’information attendue.
- [ ] Le graphique peut être corrigé pendant le TP grâce à une ressource ou une
  méthode fournie dans Word.
- [ ] Le tableau corrigé est un tableau de données simple, titré, sans fusion,
  imbrication, fractionnement de ligne ni usage de mise en page.
- [ ] La ligne d’en-tête est identifiée et répétée lorsque nécessaire.
- [ ] `#767676` et `4,48` ne sont jamais présentés comme un échec de contraste.

## Preuves attendues

- [ ] `make sami` produit les trois DOCX et la ressource graphique nécessaire.
- [ ] Les tests calculent les contrastes au lieu de comparer un commentaire.
- [ ] Les tests DOCX inspectent les en-têtes, fusions, imbrications et options
  de fractionnement du tableau.
- [ ] La correction du graphique dans Word fait partie du scénario humain
  chronométré de T09a, puis de la recette finale T16.

## À préserver

- Les stations 1 et 2 déjà migrées.
- Les graphiques et ressources générés par la chaîne existante.

## Hors périmètre

- Transformer les tableaux flottants en manipulation obligatoire.
- Enseigner un outil graphique externe.
