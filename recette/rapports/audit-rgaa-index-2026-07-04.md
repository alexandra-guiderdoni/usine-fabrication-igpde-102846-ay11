# Audit RGAA ciblé - page d'accueil exercice

Date : 4 juillet 2026

## Résultat

Page auditée : `http://127.0.0.1:8765/index.html`.

Je ne constate pas de non-conformité RGAA avérée sur cette passe ciblée.

La hiérarchie de titres fournie est correcte :

```text
1 Les 13 points de contrôle rapides du W3C
2 Pré-diagnostic pédagogique
2 Choisir une version du site
3 Site à auditer
3 Aide à la correction
3 Site corrigé
2 Grille d'audit
3 Télécharger la grille d'audit des points de contrôle rapides
2 Pages à auditer
3 #1 Actualité illustrée
...
```

Le signal que j'avais remonté sur les titres concernait `site-accessible/index.html`, pas cette page racine.

## Preuves exécutées

- Capture navigateur AY11 sur `http://127.0.0.1:8765/index.html`.
- axe-core local 4.12.1.
- Build AY11 `rgaa-106` non persistant.
- Passe statique locale sur `docs/index.html`.

## Résultats observés

- axe-core : 0 violation.
- axe-core : 1 règle incomplète, `color-contrast`, liée aux arrière-plans DSFR que l'outil ne peut pas déterminer automatiquement.
- AY11 : 2 signaux candidats faibles, `8.7` et `12.6`, à vérifier humainement. Aucun des deux ne vaut non-conformité sans preuve complémentaire.
- `html lang="fr"` présent.
- Balise `title` présente.
- Hiérarchie de titres sans saut de niveau.
- Ancres internes présentes.
- Images avec attribut `alt`.
- Aucun formulaire, média, tableau ou iframe sur cette page.

## Points à garder

### Contrastes

Le contraste n'est pas conclu automatiquement. axe-core remonte `color-contrast` en `incomplete`, parce que certains arrière-plans DSFR sont calculés via images ou dégradés. Cela demande une mesure manuelle si on veut clore RGAA 3.2.

### Validation projet

Le validateur local global `validate.py` échoue encore sur `https://catalogue.igpde.finances.gouv.fr/`, non présent dans la whitelist. Cette anomalie concerne aussi `docs/index.html`, mais c'est un écart de contrat de validation locale, pas une non-conformité RGAA directe.

## Limites

- Pas d'audit formel complet des 106 critères.
- Pas de test lecteur d'écran réel.
- Pas de mesure manuelle des contrastes.
- Les signaux AY11 sont non décisionnels.
