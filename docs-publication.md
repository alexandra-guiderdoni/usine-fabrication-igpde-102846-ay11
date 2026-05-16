# Publication du site exercice points de contrôle rapides W3C

## Dépôt GitHub

- **Dépôt** : [Alexmacapple/easy-check-igpde](https://github.com/Alexmacapple/easy-check-igpde)
- **Visibilité** : public
- **Remote SSH** : `git@github.com:Alexmacapple/easy-check-igpde.git`

## URL publique

**https://alexmacapple.github.io/easy-check-igpde/**

Hébergement via GitHub Pages, branche `main`, racine `/`, mode legacy (déploiement direct depuis la branche).

## Contenu publié

Le site est généré depuis le projet `IGPDE-Carinne-C` (dossier `docs/`). Il contient :

- **Page d'accueil** (`index.html`) avec navigation vers les 3 versions
- **3 versions du site** :
  - `site-inaccessible/` : version avec défauts volontaires (exercice d'identification)
  - `site-aide-correction/` : version avec indices de correction
  - `site-accessible/` : version corrigée conforme
- **Pages légales** : mentions légales, données personnelles, accessibilité, plan du site
- **Assets** : DSFR, audio, vidéo, grille XLSX téléchargeable

## Procédure de publication

### Prérequis

- Clé SSH chargée (`ssh-add -l`)
- CLI GitHub (`gh`) authentifiée
- Dépôt cible créé sur GitHub (vide, public)

### Étapes

1. Copier le contenu de `docs/` dans un dossier temporaire (sans `.DS_Store` ni fichiers `.md` internes) :

```bash
rsync -a --exclude='.DS_Store' --exclude='*.md' docs/ /tmp/easy-check-igpde/
```

2. Ajouter `.nojekyll` à la racine (empêche Jekyll de filtrer les fichiers DSFR) :

```bash
touch /tmp/easy-check-igpde/.nojekyll
```

3. Initialiser le dépôt git et pusher :

```bash
cd /tmp/easy-check-igpde
git init
git remote add origin git@github.com:Alexmacapple/easy-check-igpde.git
git add -A
git commit -m "Publication du site exercice points de contrôle rapides W3C"
git branch -M main
git push -u origin main
```

4. Activer GitHub Pages en mode legacy :

```bash
gh api repos/Alexmacapple/easy-check-igpde/pages \
  -X POST --input - <<'EOF'
{"source":{"branch":"main","path":"/"},"build_type":"legacy"}
EOF
```

### Mise à jour du site

Pour republier après modification des sources :

1. Régénérer le site : `python3 scripts/generate_easy_checks_site_skeleton.py`
2. Valider : `python3 validate.py`
3. Synchroniser vers le dépôt :

```bash
rsync -a --delete --exclude='.DS_Store' --exclude='*.md' --exclude='.git' \
  docs/ /tmp/easy-check-igpde/
cd /tmp/easy-check-igpde
git add -A
git commit -m "Mise à jour du site"
git push
```

## Architecture : deux dépôts, un seul contenu

Le contenu HTML existe à deux endroits :

1. **`IGPDE-Carinne-C/docs/`** — dans le dépôt de la formation (source, généré par le script Python)
2. **`easy-check-igpde`** — dépôt standalone pour GitHub Pages (copie publiée)

Le dépôt de formation reste privé (il contient les scripts, les sources pédagogiques, les specs et les exercices). Le site public est une copie pushée manuellement via la procédure de mise à jour ci-dessus.

La source de vérité est toujours `IGPDE-Carinne-C` : toute modification passe par le script Python, puis est synchronisée vers le dépôt public.

## Points d'attention

- **`.nojekyll`** : indispensable, sans lui GitHub Pages active Jekyll qui peut ignorer certains fichiers DSFR
- **Mode legacy** (pas workflow) : le mode `workflow` nécessite un fichier GitHub Actions, le mode `legacy` déploie directement depuis la branche
- **SSH uniquement** : ne pas utiliser HTTPS pour les opérations git
- **Deux dépôts à synchroniser** : après chaque régénération du site, penser à republier vers `easy-check-igpde`
