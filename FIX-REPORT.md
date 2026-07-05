# Rapport de suivi - correction RGAA 8.2 header DSFR

Date : 4 juillet 2026

## Résultat

Correction appliquée sur les trois variantes du site :

- `docs/site-inaccessible/`
- `docs/site-aide-correction/`
- `docs/site-accessible/`

La correction retire l’attribut `aria-label="Menu principal"` du conteneur générique suivant :

```html
<div class="fr-header__menu fr-modal" id="modal-menu">
```

Le nom accessible de la navigation principale reste porté par l’élément sémantique adapté :

```html
<nav class="fr-nav" role="navigation" aria-label="Menu principal" id="navigation-principale">
```

## Non-conformité traitée

- Critère : RGAA 8.2, test 8.2.1.
- Source du signal : W3C Nu HTML Checker.
- Problème : `aria-label` ne doit pas être porté par un `div` générique sans rôle adapté.
- Correction : retrait de l’attribut interdit sur le conteneur de menu d’en-tête.
- Périmètre : 42 pages HTML, soit 14 pages pour chacun des trois sites.

## Preuves

- Recherche locale après correction : `0` occurrence de `<div ... aria-label=...>` dans les trois sites.
- Comptage local : `42` conteneurs `<div class="fr-header__menu fr-modal" id="modal-menu">` corrigés.
- Validation W3C Nu par soumission HTML sur les 42 pages : `0` erreur restante du type `aria-label attribute must not be specified on any div element`.
- Validation W3C Nu sur `docs/site-accessible/index.html` : `0` erreur.

## Limites

- La validation projet `uv run --with PyYAML python validate.py` échoue encore à cause d’assets multimédias et de fichiers de revue visuelle manquants, sans lien avec cette correction.
- La passe W3C Nu complète remonte encore d’autres erreurs HTML hors correction demandée : `6` dans `site-accessible`, `12` dans `site-aide-correction`, `9` dans `site-inaccessible`.
- Le rapport d’audit RGAA 106 critères n’a pas été réécrit dans cette remédiation ; le changement permet de retester le critère 8.2 sur `site-accessible/index.html`.
