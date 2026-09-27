# Passation prochaine session - 4 mai 2026

Projet : Formation 102638 (IGPDE / Carinne C.) - module web, site des points de contrôle rapides.

---

## État livré

- Branche : `main`.
- Dernier correctif produit poussé : `704d5eb7 Corrige le libelle courriel EC01`.
- EC01 testé et stabilisé.
- Terminologie décidée : remplacer l'ancienne terminologie anglaise par `Point(s) de contrôle rapide(s)`, avec P majuscule.
- PRD créé : `prd-meta-workflow/PRD-116-site-easy-checks-igpde.MD`.

---

## EC01 - testé

Page concernée : `docs/site-accessible/ec01-images.html`, avec comparaison dans `site-inaccessible/` et `site-aide-correction/`.

Points validés :

- image informative pleine largeur sur la grille ;
- image décorative séparatrice sous le visuel informatif ;
- titre `h3` "Nous contacter" ;
- paragraphes avant/après chaque image ;
- lien image courriel avec libellé visible `Par courriel :` ;
- lien composite SMS avec icône décorative silencieuse en version corrigée ;
- aide en haut de page avec 3 niveaux progressifs ;
- messages ciblés pour les 4 cas EC01 ;
- contenu principal contraint à 8 colonnes DSFR ;
- couleurs du schéma conformes aux contrastes DSFR ;
- validation `python3 validate.py` OK avant la reprise terminologique.

---

## À faire en prochaine session

1. Tester le Point de contrôle rapide 2 : titre de page.
2. Ouvrir les trois versions :
   - `docs/site-inaccessible/ec02-page-title.html`
   - `docs/site-aide-correction/ec02-page-title.html`
   - `docs/site-accessible/ec02-page-title.html`
3. Vérifier que l'exercice EC02 est compréhensible sans annoncer trop directement la correction.
4. Vérifier le `<title>` dans chaque version :
   - version inaccessible : erreur volontaire claire ;
   - aide : accordéon en haut avec indice, problème, correction ;
   - accessible : titre unique, spécifique, information principale en premier.
5. Relancer les contrôles :
   - `python3 build.py`
   - `python3 validate.py`
   - `tidy` ciblé sur les pages EC02 ;
   - contrôle `rg` pour confirmer que l'ancienne terminologie anglaise ne reste pas visible.

---

## Commandes utiles

```bash
# historique : à la racine de l'ancien dossier du projet ; aujourd'hui, dans l'usine : make apercu
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

URL locale :

```text
http://127.0.0.1:8765/index.html
```

Contrôles rapides :

```bash
python3 build.py
python3 validate.py
rg -n "Point de contrôle rapide|points de contrôle rapides" docs 03-easy-checks scripts
```
