# Contraintes — Formation 102638 (IGPDE / Carinne C.)

- **Compile le** : 2026-05-16
- **Compilateur** : contraintes-vivantes v1

## 1. Dépendances externes

### Stack Python de génération

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`, imports Python dans `scripts/` et `validate.py`
- **Statut** : confirmée
- **Contrainte** : la régénération du projet repose sur Python 3 et au minimum `python-pptx`, `lxml`, `openpyxl`, `python-docx`, `matplotlib`, `numpy` et `PyYAML`.
- **Impact** : sans cette stack, les sorties PPTX, DOCX, XLSX et la validation du site ne sont pas regenerables localement.
- **Decision / prochaine verification** : revalider la liste a chaque ajout d'import dans `scripts/` ou `validate.py`.
- **Composants affectés** : `AGENTS.md`, `CLAUDE.md`, `validate.py`, `scripts/igpde_dsfr_components.py`, `scripts/generate_exercice_sami.py`, `scripts/generate_grille_audit.py`, `scripts/generate_easy_checks_site_skeleton.py`

### Assets DSFR embarqués

- **Date** : 2026-05-12
- **Source** : `validate.py`, `docs/assets/dsfr/`
- **Statut** : confirmée
- **Contrainte** : le site d'exercice dépend des assets DSFR embarqués localement (`dsfr.min.css`, `utility.min.css`, `dsfr.module.min.js`, `dsfr.nomodule.min.js`).
- **Impact** : un build ou une copie incomplete du dossier `docs/assets/dsfr/` casse le rendu ou les comportements interactifs du site.
- **Décision / prochaine vérification** : conserver ces assets dans le dépôt et les vérifier via `python3 validate.py`.
- **Composants affectés** : `validate.py`, `docs/assets/dsfr/`, `docs/index.html`, `docs/site-accessible/*.html`, `docs/site-inaccessible/*.html`, `docs/site-aide-correction/*.html`

### Hotes externes limites

- **Date** : 2026-05-12
- **Source** : `validate.py`
- **Statut** : confirmée
- **Contrainte** : les références HTTP/HTTPS du site d'exercice sont limitées à une liste blanche d'hôtes, notamment `youtube.com`, `youtube-nocookie.com`, `accessibilite.numerique.gouv.fr` et quelques extensions navigateurs.
- **Impact** : toute nouvelle reference externe hors liste blanche fera echouer la validation.
- **Decision / prochaine verification** : etendre explicitement `ALLOWED_EXTERNAL_HOSTS` avant d'introduire un nouvel hote externe.
- **Composants affectés** : `validate.py`, `docs/**/*.html`

## 2. Runtime et infrastructure

### Runtime local sans orchestration

- **Date** : 2026-05-12
- **Source** : arborescence du projet, absence de `Dockerfile`, `docker-compose.yml`, `Makefile`
- **Statut** : confirmée
- **Contrainte** : le projet s'exécute comme une suite de scripts Python locaux, sans orchestration Docker ni pipeline de boot déclaré.
- **Impact** : l'environnement de régénération dépend directement du poste local et de ses dépendances Python.
- **Decision / prochaine verification** : si un mode de build reproductible est ajoute, le documenter ici et dans `AGENTS.md`.
- **Composants affectés** : `validate.py`, `scripts/*.py`

### Generation PPTX via scripts uniquement

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`, `scripts/assemble.py`
- **Statut** : confirmée
- **Contrainte** : le deck principal doit etre regenere via `python3 scripts/assemble.py`, avec `finalize_pptx()` obligatoire avant livraison.
- **Impact** : une modification directe du PPTX contourne le flux de production et risque d'être écrasée à la régénération.
- **Décision / prochaine vérification** : toute évolution du support doit passer par `scripts/slides/NN_*.py` puis une régénération.
- **Composants affectés** : `scripts/assemble.py`, `scripts/slides/` (131 modules), `formation-102638-juin-2026.pptx` (131 slides)

## 3. Indexation et donnees

### Contrat source du site easy checks

- **Date** : 2026-05-12
- **Source** : `validate.py`, `scripts/generate_easy_checks_site_skeleton.py`, `03-easy-checks/evaluation_contract.yml`
- **Statut** : confirmée
- **Contrainte** : le site d'exercice et ses fichiers dérivés sont générés à partir de `03-easy-checks/evaluation_contract.yml`, qui doit contenir 13 pages et un schéma minimal imposé.
- **Impact** : un contrat incomplet ou incohérent casse la génération et la validation du site.
- **Décision / prochaine vérification** : toute modification du contrat doit être revalidée par `python3 validate.py`.
- **Composants affectés** : `03-easy-checks/evaluation_contract.yml`, `scripts/generate_easy_checks_site_skeleton.py`, `validate.py`, `docs/`

### Artefacts pédagogiques générés

- **Date** : 2026-05-12
- **Source** : docstring de `scripts/generate_exercice_sami.py`
- **Statut** : confirmée
- **Contrainte** : l'exercice Sami produit des PNG dans `_assets/` et trois DOCX distincts (`inaccessible`, `aide_correction`, `accessible`) à partir du script de génération.
- **Impact** : la cohérence pédagogique de l'exercice dépend du script et des assets qu'il régénère.
- **Décision / prochaine vérification** : réexécuter le script après toute modification du contenu ou des médias Sami.
- **Composants affectés** : `scripts/generate_exercice_sami.py`, `_assets/`, `sami-doc-inaccessible.docx`, `sami-doc-aide-correction.docx`, `sami-doc-accessible.docx`

### Copie de la grille d'audit dans le site

- **Date** : 2026-05-12
- **Source** : `validate.py`, `todo.md`, presence de `docs/assets/downloads/grille-audit-easy-checks.xlsx`
- **Statut** : confirmée
- **Contrainte** : la grille XLSX des easy checks doit exister a la fois dans `03-easy-checks/` et dans `docs/assets/downloads/` pour la mission finale.
- **Impact** : une copie manquante casse soit la source pédagogique, soit le téléchargement depuis le site.
- **Décision / prochaine vérification** : vérifier les deux emplacements après régénération du site ou de la grille.
- **Composants affectés** : `03-easy-checks/grille-audit-easy-checks.xlsx`, `docs/assets/downloads/grille-audit-easy-checks.xlsx`, `validate.py`

## 4. Features déjà implémentées

| Feature | Fichier | Depuis quand |
|---------|---------|--------------|
| Assemblage du deck principal numerote automatiquement | `scripts/assemble.py` | constate le 2026-05-12 |
| Generation d'un deck distinct `WCAG en langage clair` et de sa version condensee (dans `wcag/`) | `scripts/generate_wcag_langage_clair.py` | constate le 2026-05-12 |
| Génération des trois DOCX Sami et de leurs médias PNG | `scripts/generate_exercice_sami.py` | constaté le 2026-05-12 |
| Generation du site d'exercice easy checks en trois variantes | `scripts/generate_easy_checks_site_skeleton.py` | constate le 2026-05-12 |
| Validation automatisée du contrat, des assets et des pages HTML | `validate.py` | constaté le 2026-05-12 |
| Generation de la grille d'audit XLSX | `scripts/generate_grille_audit.py` | constate le 2026-05-12 |
| Bibliotheque de composants PPTX DSFR IGPDE | `scripts/igpde_dsfr_components.py` | constate le 2026-05-12 |
| Jeu de slides modulaires par fichiers `NN_*.py` | `scripts/slides/` (131 modules) | constate le 2026-05-16 |
| Post-traitement accessibilité PPTX (ordre de lecture, lang, alt text, métadonnées, quarantine) | `scripts/igpde_dsfr_components.py` (`finalize_pptx()`) | constaté le 2026-05-12 |
| Documentation architecture C4 du pipeline de slides | `architecture-c4-slides.md` | 2026-05-16 |
| README causal du projet | `README.md` | 2026-05-16 |

## 5. Securite et secrets

### Pas de secret applicatif identifie

- **Date** : 2026-05-12
- **Source** : arborescence inspectee, absence de `.env`, `.env.example` et de configuration de secret
- **Statut** : confirmée
- **Contrainte** : aucun mecanisme de secret ou d'authentification applicative n'a ete identifie dans les sources inspectees.
- **Impact** : le projet parait distribuable sans coffre de secrets, mais toute future dependance externe avec cle devra etre documentee explicitement.
- **Decision / prochaine verification** : recontroler cette hypothese si des appels API autentifies sont ajoutes.
- **Composants affectés** : racine du projet, `scripts/`, `docs/`

### Filtrage des références externes du site

- **Date** : 2026-05-12
- **Source** : `validate.py`
- **Statut** : confirmée
- **Contrainte** : les liens externes du site ne sont acceptés que s'ils appartiennent à une liste blanche d'hôtes.
- **Impact** : cela limite l'introduction accidentelle de ressources externes non controlees dans le site d'exercice.
- **Décision / prochaine vérification** : maintenir la liste blanche à jour avec toute nouvelle source pédagogique externe.
- **Composants affectés** : `validate.py`, `docs/**/*.html`

### Gitignore minimal

- **Date** : 2026-05-12
- **Source** : `.gitignore`
- **Statut** : confirmée
- **Contrainte** : le `.gitignore` n'exclut que `.DS_Store` et les fichiers temporaires Office `~$*.pptx` et `~$*.docx`.
- **Impact** : les artefacts générés principaux sont destinés à être suivis dans le dépôt, ce qui augmente le risque de gros diffs binaires mais préserve la distribuabilité.
- **Décision / prochaine vérification** : ne pas supposer qu'un binaire généré sera ignoré par git.
- **Composants affectés** : `.gitignore`, `*.pptx`, `*.docx`

## 6. RGPD et donnees utilisateurs

### Projet statique sans persistance applicative identifiee

- **Date** : 2026-05-12
- **Source** : scripts inspectes, absence de base de donnees, de backend web et de couche de persistance dediee
- **Statut** : confirmée
- **Contrainte** : aucune persistance applicative de donnees utilisateurs n'a ete identifiee dans les sources inspectees ; le projet produit surtout des documents et des pages statiques.
- **Impact** : les évolutions ajoutant formulaires avec soumission serveur, analytics ou stockage devront documenter leur impact RGPD.
- **Décision / prochaine vérification** : requalifier cette contrainte si un backend ou un stockage est ajouté.
- **Composants affectés** : `scripts/*.py`, `docs/`

### Pages d'information vie privée déjà présentes

- **Date** : 2026-05-12
- **Source** : présence de `docs/donnees-personnelles.html` et `docs/mentions-legales.html`
- **Statut** : confirmée
- **Contrainte** : le site d'exercice embarque déjà des pages dédiées aux données personnelles et aux mentions légales.
- **Impact** : toute modification du parcours ou des données collectées doit rester cohérente avec ces pages.
- **Décision / prochaine vérification** : vérifier ces pages si le contenu du site ajoute une collecte nouvelle.
- **Composants affectés** : `docs/donnees-personnelles.html`, `docs/mentions-legales.html`, `docs/index.html`

### Sous-titres et transcriptions médias embarqués

- **Date** : 2026-05-12
- **Source** : `todo.md`, présence de `docs/assets/shared/media/captcha-sous-titres.vtt`
- **Statut** : confirmée
- **Contrainte** : certains médias pédagogiques reposent sur des sous-titres et transcriptions locales versionnées dans `docs/assets/shared/media/`.
- **Impact** : supprimer ou désynchroniser ces fichiers dégrade immédiatement l'accessibilité et la cohérence pédagogique des pages média.
- **Décision / prochaine vérification** : vérifier les fichiers `.vtt` et `.srt` à chaque remplacement de média.
- **Composants affectés** : `docs/assets/shared/media/`, `docs/site-*/ec09-captions.html`, `docs/site-*/ec10-transcript.html`

## 7. Qualité et benchmarks

### Validation automatisée du site easy checks

- **Date** : 2026-05-12
- **Source** : `validate.py`
- **Statut** : confirmée
- **Contrainte** : le projet dispose d'une validation scriptable qui contrôle le contrat YAML, les assets obligatoires, les liens locaux, la version accessible et des cas spécifiques EC06.
- **Impact** : `python3 validate.py` est le garde-fou principal pour les régressions du site d'exercice.
- **Décision / prochaine vérification** : exécuter la validation après chaque régénération du site ou changement des pages HTML.
- **Composants affectés** : `validate.py`, `03-easy-checks/evaluation_contract.yml`, `docs/`

### Passe visuelle PPTX non automatisée

- **Date** : 2026-05-16
- **Source** : `todo.md`
- **Statut** : confirmée
- **Contrainte** : une passe visuelle humaine PowerPoint reste nécessaire avant diffusion pour détecter les chevauchements fins que les contrôles XML ne voient pas.
- **Impact** : une génération sans revue visuelle peut laisser passer des défauts de rendu sur certaines slides.
- **Décision / prochaine vérification** : conserver une passe manuelle de livraison, en priorité sur les slides 16 à 22, 36, 75 à 76 et 82 à 106 (signalées dans `todo.md`).
- **Composants affectés** : `todo.md`, `formation-102638-juin-2026.pptx`, `scripts/slides/`

### Modes d'échec documentés dans lessons.md

- **Date** : 2026-05-16
- **Source** : `lessons.md`, `CLAUDE.md` section Modes d'échec connus
- **Statut** : confirmée
- **Contrainte** : 21 leçons techniques sont documentées dans `lessons.md`, couvrant les pièges python-pptx, les erreurs de positionnement, les débordements et les choix pédagogiques. À relire avant toute nouvelle session.
- **Impact** : ignorer ces leçons conduit à répéter les mêmes erreurs (string/liste, layout parasite, débordement _safe_top, estimation additive).
- **Décision / prochaine vérification** : mettre à jour `lessons.md` à chaque nouveau piège découvert.
- **Composants affectés** : `lessons.md`, `CLAUDE.md`, `scripts/igpde_dsfr_components.py`, `scripts/slides/`

### Contrôles de livraison documentés

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`
- **Statut** : confirmée
- **Contrainte** : la livraison du deck passe par régénération, `finalize_pptx()`, contrôle des tirets dans `scripts/` et vérification `unzip -t` du PPTX.
- **Impact** : sauter ces contrôles augmente le risque de régressions d'accessibilité, de typographie ou de corruption binaire.
- **Decision / prochaine verification** : conserver ces commandes dans le rituel de livraison.
- **Composants affectés** : `AGENTS.md`, `CLAUDE.md`, `scripts/assemble.py`, `formation-102638-juin-2026.pptx`

## 8. Distribuabilite

### Depot consultable sans CDN

- **Date** : 2026-05-12
- **Source** : `docs/assets/dsfr/`, `validate.py`
- **Statut** : confirmée
- **Contrainte** : le site d'exercice embarque ses assets DSFR localement et ne dépend pas d'un CDN pour son CSS/JS principal.
- **Impact** : le site peut être prévisualisé hors ligne, sous réserve de disposer des fichiers du dépôt.
- **Décision / prochaine vérification** : conserver les assets localement lors de toute mise à jour DSFR.
- **Composants affectés** : `docs/assets/dsfr/`, `docs/**/*.html`

### Quarantaine macOS sur les fichiers générés

- **Date** : 2026-05-12
- **Source** : `lessons.md`, `AGENTS.md`, `CLAUDE.md`
- **Statut** : confirmée
- **Contrainte** : sur macOS, les fichiers Office générés par les scripts Python peuvent recevoir le flag `com.apple.quarantine` et doivent être post-traités avant édition utilisateur.
- **Impact** : PowerPoint ou Excel peuvent ouvrir le fichier en mode protégé et refuser la sauvegarde tant que l'attribut n'est pas retiré.
- **Décision / prochaine vérification** : conserver `finalize_pptx()` et les post-traitements `xattr -d com.apple.quarantine` dans le flux de livraison.
- **Composants affectés** : `lessons.md`, `AGENTS.md`, `CLAUDE.md`, `formation-102638-juin-2026.pptx`, `scripts/generate_grille_audit.py`

### Regeneration reservee a un poste equipe Python

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`, imports Python dans `scripts/`
- **Statut** : confirmée
- **Contrainte** : un collègue peut consulter les artefacts livrés du dépôt, mais ne peut pas régénérer le projet from scratch sans un environnement Python outillé et les bibliothèques listées.
- **Impact** : la distribuabilité du code source est conditionnée par la préparation du poste local.
- **Décision / prochaine vérification** : documenter explicitement les dépendances si une installation from scratch doit être déléguée.
- **Composants affectés** : `AGENTS.md`, `CLAUDE.md`, `scripts/*.py`
