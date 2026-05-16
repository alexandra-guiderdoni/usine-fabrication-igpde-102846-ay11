# Contraintes — Formation 102638 (IGPDE / Carinne C.)

- **Compile le** : 2026-05-16
- **Compilateur** : contraintes-vivantes v1

## 1. Dépendances externes

### Stack Python de generation

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`, imports Python dans `scripts/` et `validate.py`
- **Statut** : confirmee
- **Contrainte** : la regeneration du projet repose sur Python 3 et au minimum `python-pptx`, `lxml`, `openpyxl`, `python-docx`, `matplotlib`, `numpy` et `PyYAML`.
- **Impact** : sans cette stack, les sorties PPTX, DOCX, XLSX et la validation du site ne sont pas regenerables localement.
- **Decision / prochaine verification** : revalider la liste a chaque ajout d'import dans `scripts/` ou `validate.py`.
- **Composants affectes** : `AGENTS.md`, `CLAUDE.md`, `validate.py`, `scripts/igpde_dsfr_components.py`, `scripts/generate_exercice_sami.py`, `scripts/generate_grille_audit.py`, `scripts/generate_easy_checks_site_skeleton.py`

### Assets DSFR embarques

- **Date** : 2026-05-12
- **Source** : `validate.py`, `docs/assets/dsfr/`
- **Statut** : confirmee
- **Contrainte** : le site d'exercice depend des assets DSFR embarques localement (`dsfr.min.css`, `utility.min.css`, `dsfr.module.min.js`, `dsfr.nomodule.min.js`).
- **Impact** : un build ou une copie incomplete du dossier `docs/assets/dsfr/` casse le rendu ou les comportements interactifs du site.
- **Decision / prochaine verification** : conserver ces assets dans le depot et les verifier via `python3 validate.py`.
- **Composants affectes** : `validate.py`, `docs/assets/dsfr/`, `docs/index.html`, `docs/site-accessible/*.html`, `docs/site-inaccessible/*.html`, `docs/site-aide-correction/*.html`

### Hotes externes limites

- **Date** : 2026-05-12
- **Source** : `validate.py`
- **Statut** : confirmee
- **Contrainte** : les references HTTP/HTTPS du site d'exercice sont limitees a une liste blanche d'hotes, notamment `youtube.com`, `youtube-nocookie.com`, `accessibilite.numerique.gouv.fr` et quelques extensions navigateurs.
- **Impact** : toute nouvelle reference externe hors liste blanche fera echouer la validation.
- **Decision / prochaine verification** : etendre explicitement `ALLOWED_EXTERNAL_HOSTS` avant d'introduire un nouvel hote externe.
- **Composants affectes** : `validate.py`, `docs/**/*.html`

## 2. Runtime et infrastructure

### Runtime local sans orchestration

- **Date** : 2026-05-12
- **Source** : arborescence du projet, absence de `Dockerfile`, `docker-compose.yml`, `Makefile`
- **Statut** : confirmee
- **Contrainte** : le projet s'execute comme une suite de scripts Python locaux, sans orchestration Docker ni pipeline de boot declare.
- **Impact** : l'environnement de regeneration depend directement du poste local et de ses dependances Python.
- **Decision / prochaine verification** : si un mode de build reproductible est ajoute, le documenter ici et dans `AGENTS.md`.
- **Composants affectes** : `build.py`, `validate.py`, `scripts/*.py`

### Generation PPTX via scripts uniquement

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`, `scripts/assemble.py`
- **Statut** : confirmee
- **Contrainte** : le deck principal doit etre regenere via `python3 scripts/assemble.py`, avec `finalize_pptx()` obligatoire avant livraison.
- **Impact** : une modification directe du PPTX contourne le flux de production et risque d'etre ecrasee a la regeneration.
- **Decision / prochaine verification** : toute evolution du support doit passer par `scripts/slides/NN_*.py` puis une regeneration.
- **Composants affectes** : `scripts/assemble.py`, `scripts/slides/` (113 modules), `formation-102638-juin-2026.pptx` (112 slides)

## 3. Indexation et donnees

### Contrat source du site easy checks

- **Date** : 2026-05-12
- **Source** : `validate.py`, `scripts/generate_easy_checks_site_skeleton.py`, `03-easy-checks/evaluation_contract.yml`
- **Statut** : confirmee
- **Contrainte** : le site d'exercice et ses fichiers derives sont generes a partir de `03-easy-checks/evaluation_contract.yml`, qui doit contenir 13 pages et un schema minimal impose.
- **Impact** : un contrat incomplet ou incoherent casse la generation et la validation du site.
- **Decision / prochaine verification** : toute modification du contrat doit etre revalidee par `python3 validate.py`.
- **Composants affectes** : `03-easy-checks/evaluation_contract.yml`, `scripts/generate_easy_checks_site_skeleton.py`, `validate.py`, `docs/`

### Artefacts pedagogiques generes

- **Date** : 2026-05-12
- **Source** : docstring de `scripts/generate_exercice_sami.py`
- **Statut** : confirmee
- **Contrainte** : l'exercice Sami produit des PNG dans `_assets/` et trois DOCX distincts (`inaccessible`, `aide_correction`, `accessible`) a partir du script de generation.
- **Impact** : la coherence pedagogique de l'exercice depend du script et des assets qu'il regenere.
- **Decision / prochaine verification** : rerun le script apres toute modification du contenu ou des medias Sami.
- **Composants affectes** : `scripts/generate_exercice_sami.py`, `_assets/`, `sami-doc-inaccessible.docx`, `sami-doc-aide-correction.docx`, `sami-doc-accessible.docx`

### Copie de la grille d'audit dans le site

- **Date** : 2026-05-12
- **Source** : `validate.py`, `todo.md`, presence de `docs/assets/downloads/grille-audit-easy-checks.xlsx`
- **Statut** : confirmee
- **Contrainte** : la grille XLSX des easy checks doit exister a la fois dans `03-easy-checks/` et dans `docs/assets/downloads/` pour la mission finale.
- **Impact** : une copie manquante casse soit la source pedagogique, soit le telechargement depuis le site.
- **Decision / prochaine verification** : verifier les deux emplacements apres regeneration du site ou de la grille.
- **Composants affectes** : `03-easy-checks/grille-audit-easy-checks.xlsx`, `docs/assets/downloads/grille-audit-easy-checks.xlsx`, `validate.py`

## 4. Features deja implementees

| Feature | Fichier | Depuis quand |
|---------|---------|--------------|
| Assemblage du deck principal numerote automatiquement | `scripts/assemble.py` | constate le 2026-05-12 |
| Generation d'un deck distinct `WCAG en langage clair` et de sa version condensee | `scripts/generate_wcag_langage_clair.py` | constate le 2026-05-12 |
| Generation des trois DOCX Sami et de leurs medias PNG | `scripts/generate_exercice_sami.py` | constate le 2026-05-12 |
| Generation du site d'exercice easy checks en trois variantes | `scripts/generate_easy_checks_site_skeleton.py` | constate le 2026-05-12 |
| Validation automatisee du contrat, des assets et des pages HTML | `validate.py` | constate le 2026-05-12 |
| Generation de la grille d'audit XLSX | `scripts/generate_grille_audit.py` | constate le 2026-05-12 |
| Bibliotheque de composants PPTX DSFR IGPDE | `scripts/igpde_dsfr_components.py` | constate le 2026-05-12 |
| Jeu de slides modulaires par fichiers `NN_*.py` | `scripts/slides/` (113 modules) | constate le 2026-05-12 |
| Post-traitement accessibilite PPTX (ordre de lecture, lang, alt text, metadonnees, quarantine) | `scripts/igpde_dsfr_components.py` (`finalize_pptx()`) | constate le 2026-05-12 |
| Documentation architecture C4 du pipeline de slides | `architecture-c4-slides.md` | 2026-05-16 |
| README causal du projet | `README.md` | 2026-05-16 |

## 5. Securite et secrets

### Pas de secret applicatif identifie

- **Date** : 2026-05-12
- **Source** : arborescence inspectee, absence de `.env`, `.env.example` et de configuration de secret
- **Statut** : confirmee
- **Contrainte** : aucun mecanisme de secret ou d'authentification applicative n'a ete identifie dans les sources inspectees.
- **Impact** : le projet parait distribuable sans coffre de secrets, mais toute future dependance externe avec cle devra etre documentee explicitement.
- **Decision / prochaine verification** : recontroler cette hypothese si des appels API autentifies sont ajoutes.
- **Composants affectes** : racine du projet, `scripts/`, `docs/`

### Filtrage des references externes du site

- **Date** : 2026-05-12
- **Source** : `validate.py`
- **Statut** : confirmee
- **Contrainte** : les liens externes du site ne sont acceptes que s'ils appartiennent a une liste blanche d'hotes.
- **Impact** : cela limite l'introduction accidentelle de ressources externes non controlees dans le site d'exercice.
- **Decision / prochaine verification** : maintenir la liste blanche a jour avec toute nouvelle source pedagogique externe.
- **Composants affectes** : `validate.py`, `docs/**/*.html`

### Gitignore minimal

- **Date** : 2026-05-12
- **Source** : `.gitignore`
- **Statut** : confirmee
- **Contrainte** : le `.gitignore` n'exclut que `.DS_Store` et les fichiers temporaires Office `~$*.pptx` et `~$*.docx`.
- **Impact** : les artefacts generes principaux sont destines a etre suivis dans le depot, ce qui augmente le risque de gros diffs binaires mais preserve la distribuabilite.
- **Decision / prochaine verification** : ne pas supposer qu'un binaire genere sera ignore par git.
- **Composants affectes** : `.gitignore`, `*.pptx`, `*.docx`

## 6. RGPD et donnees utilisateurs

### Projet statique sans persistance applicative identifiee

- **Date** : 2026-05-12
- **Source** : scripts inspectes, absence de base de donnees, de backend web et de couche de persistance dediee
- **Statut** : confirmee
- **Contrainte** : aucune persistance applicative de donnees utilisateurs n'a ete identifiee dans les sources inspectees ; le projet produit surtout des documents et des pages statiques.
- **Impact** : les evolutions ajoutant formulaires avec soumission serveur, analytics ou stockage devront documenter leur impact RGPD.
- **Decision / prochaine verification** : requalifier cette contrainte si un backend ou un stockage est ajoute.
- **Composants affectes** : `scripts/*.py`, `docs/`

### Pages d'information vie privee deja presentes

- **Date** : 2026-05-12
- **Source** : presence de `docs/donnees-personnelles.html` et `docs/mentions-legales.html`
- **Statut** : confirmee
- **Contrainte** : le site d'exercice embarque deja des pages dediees aux donnees personnelles et aux mentions legales.
- **Impact** : toute modification du parcours ou des donnees collectees doit rester coherente avec ces pages.
- **Decision / prochaine verification** : verifier ces pages si le contenu du site ajoute une collecte nouvelle.
- **Composants affectes** : `docs/donnees-personnelles.html`, `docs/mentions-legales.html`, `docs/index.html`

### Sous-titres et transcriptions medias embarques

- **Date** : 2026-05-12
- **Source** : `todo.md`, presence de `docs/assets/shared/media/captcha-sous-titres.vtt`
- **Statut** : confirmee
- **Contrainte** : certains medias pedagogiques reposent sur des sous-titres et transcriptions locales versionnees dans `docs/assets/shared/media/`.
- **Impact** : supprimer ou desynchroniser ces fichiers degrade immediatement l'accessibilite et la coherence pedagogique des pages media.
- **Decision / prochaine verification** : verifier les fichiers `.vtt` et `.srt` a chaque remplacement de media.
- **Composants affectes** : `docs/assets/shared/media/`, `docs/site-*/ec09-captions.html`, `docs/site-*/ec10-transcript.html`

## 7. Qualite et benchmarks

### Validation automatisee du site easy checks

- **Date** : 2026-05-12
- **Source** : `validate.py`
- **Statut** : confirmee
- **Contrainte** : le projet dispose d'une validation scriptable qui controle le contrat YAML, les assets obligatoires, les liens locaux, la version accessible et des cas specifiques EC06.
- **Impact** : `python3 validate.py` est le garde-fou principal pour les regressions du site d'exercice.
- **Decision / prochaine verification** : executer la validation apres chaque regeneration du site ou changement des pages HTML.
- **Composants affectes** : `validate.py`, `03-easy-checks/evaluation_contract.yml`, `docs/`

### Passe visuelle PPTX non automatisee

- **Date** : 2026-05-16
- **Source** : `todo.md`
- **Statut** : confirmee
- **Contrainte** : une passe visuelle humaine PowerPoint reste necessaire avant diffusion pour detecter les chevauchements fins que les controles XML ne voient pas.
- **Impact** : une generation sans revue visuelle peut laisser passer des defauts de rendu sur certaines slides.
- **Decision / prochaine verification** : conserver une passe manuelle de livraison, en priorite sur les slides 16 a 22, 36, 75 a 76 et 82 a 106 (signalees dans `todo.md`).
- **Composants affectes** : `todo.md`, `formation-102638-juin-2026.pptx`, `scripts/slides/`

### Modes d'echec documentes dans lessons.md

- **Date** : 2026-05-16
- **Source** : `lessons.md`, `CLAUDE.md` section Modes d'echec connus
- **Statut** : confirmee
- **Contrainte** : 21 lecons techniques sont documentees dans `lessons.md`, couvrant les pieges python-pptx, les erreurs de positionnement, les debordements et les choix pedagogiques. A relire avant toute nouvelle session.
- **Impact** : ignorer ces lecons conduit a repeter les memes erreurs (string/liste, layout parasite, debordement _safe_top, estimation additive).
- **Decision / prochaine verification** : mettre a jour `lessons.md` a chaque nouveau piege decouvert.
- **Composants affectes** : `lessons.md`, `CLAUDE.md`, `scripts/igpde_dsfr_components.py`, `scripts/slides/`

### Controles de livraison documentes

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`
- **Statut** : confirmee
- **Contrainte** : la livraison du deck passe par regeneration, `finalize_pptx()`, controle des tirets dans `scripts/` et verification `unzip -t` du PPTX.
- **Impact** : sauter ces controles augmente le risque de regressions d'accessibilite, de typographie ou de corruption binaire.
- **Decision / prochaine verification** : conserver ces commandes dans le rituel de livraison.
- **Composants affectes** : `AGENTS.md`, `CLAUDE.md`, `scripts/assemble.py`, `formation-102638-juin-2026.pptx`

## 8. Distribuabilite

### Depot consultable sans CDN

- **Date** : 2026-05-12
- **Source** : `docs/assets/dsfr/`, `validate.py`
- **Statut** : confirmee
- **Contrainte** : le site d'exercice embarque ses assets DSFR localement et ne depend pas d'un CDN pour son CSS/JS principal.
- **Impact** : le site peut etre previsualise hors ligne, sous reserve de disposer des fichiers du depot.
- **Decision / prochaine verification** : conserver les assets localement lors de toute mise a jour DSFR.
- **Composants affectes** : `docs/assets/dsfr/`, `docs/**/*.html`

### Quarantaine macOS sur les fichiers generes

- **Date** : 2026-05-12
- **Source** : `lessons.md`, `AGENTS.md`, `CLAUDE.md`
- **Statut** : confirmee
- **Contrainte** : sur macOS, les fichiers Office generes par les scripts Python peuvent recevoir le flag `com.apple.quarantine` et doivent etre post-traites avant edition utilisateur.
- **Impact** : PowerPoint ou Excel peuvent ouvrir le fichier en mode protege et refuser la sauvegarde tant que l'attribut n'est pas retire.
- **Decision / prochaine verification** : conserver `finalize_pptx()` et les post-traitements `xattr -d com.apple.quarantine` dans le flux de livraison.
- **Composants affectes** : `lessons.md`, `AGENTS.md`, `CLAUDE.md`, `formation-102638-juin-2026.pptx`, `scripts/generate_grille_audit.py`

### Regeneration reservee a un poste equipe Python

- **Date** : 2026-05-12
- **Source** : `AGENTS.md`, `CLAUDE.md`, imports Python dans `scripts/`
- **Statut** : confirmee
- **Contrainte** : un collegue peut consulter les artefacts livres du depot, mais ne peut pas regenerer le projet from scratch sans un environnement Python outille et les bibliotheques listees.
- **Impact** : la distribuabilite du code source est conditionnee par la preparation du poste local.
- **Decision / prochaine verification** : documenter explicitement les dependances si une installation from scratch doit etre deleguee.
- **Composants affectes** : `AGENTS.md`, `CLAUDE.md`, `scripts/*.py`
