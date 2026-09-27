# Cadrage : usine standalone de la formation accessibilité IGPDE

Statut : cadrage initial rédigé le 2026-09-27 à partir de mesures sur disque.
Mise en œuvre partielle le 2026-09-28 : les corpus documentaires des thèmes 1, 2, 4, 5 et 6 sont regroupés dans `corpus-documentaire-preparatoire/` ; `03-easy-checks/` reste à la racine car il alimente la fabrication et la validation du site.
Aucune fiche `why-context` n'existe sur ce projet : le pourquoi repose sur l'état réel du dépôt.

---

## Verdict

L'idée est bonne : le projet est déjà une usine de fait (config centrale, 138 générateurs de slides, tests, QA, site statique généré), et il n'a plus rien à faire au milieu des autres projets du workspace. Mais trois points doivent être tranchés avant de copier quoi que ce soit, sinon on déplace le désordre au lieu de le réduire :

1. L'usine doit contenir les **sources**, pas les **binaires tiers** : 199 Mo sur 501 viennent de trois installeurs (CCA, PAC, NVDA) qui n'ont rien à faire dans git.
2. L'usine doit **fabriquer** le pack livrable, pas l'héberger à la main : aujourd'hui le pack est une copie recopiée fichier par fichier, avec un site dupliqué et un clone git imbriqué.
3. L'usine doit être **réellement autonome** : plusieurs dépendances cachées vers le workspace la casseraient dès qu'on l'ouvre ailleurs.

## Ce que mesurent les 501 Mo

- `IGPDE-102846-livrables-octobre-2026/` : 260 Mo, dont 199 Mo d'installeurs dans `outils/` (CCA 87 Mo, PAC 74 Mo, NVDA 38 Mo) et 24 Mo de clone du site (doublon de `docs/`, vidéo de 12 Mo comprise).
- `outputs/` : 144 Mo, l'expérience de slides générées par image de juillet (`ia-slides`), hors de la chaîne de fabrication.
- `docs/` : 24 Mo, la source du site d'exercice (vidéo audiodécrite de 12 Mo).
- `corpus-documentaire-preparatoire/04-reseaux-sociaux/` : 17 Mo, surtout d'anciens PPTX sources (webinaire, module 4 historique).
- `tmp/` 14 Mo, `.qa/` 4 Mo : régénérables.
- Le cœur réel (scripts, `_source`, `_assets`, `docs`, contenus Markdown, tests) pèse environ 55 Mo ; avec un pack livrable sans installeurs ni doublon du site, l'usine tiendrait autour de 90 Mo (estimation).

## Ce qui entre dans l'usine

Ta liste est juste, il y manque surtout ce qui prouve que l'usine marche et ce qui fabrique le site :

- **Cités par toi** : `scripts/` (dont `scripts/images/`), `_source/`, `_assets/`, `config.yml`, `AGENTS.md`, `todo.md`, `architecture-c4-slides.md`, `lessons.md`, `contraintes.md`, `REEXPORTER-DECK-PPTX.md`, `README.md`, le pack livrable.
- **Oubliés, indispensables** :
  - `docs/` : source du site d'exercice, lue par `validate.py` et par le générateur du site ; sans elle, plus de site.
  - `tests/` (69 tests, baselines de géométrie), `validate.py`, `requirements.txt`, `.gitignore` : c'est le harnais de preuve.
  - `CLAUDE.md` : tu as cité `AGENTS.md` mais pas lui ; il porte les règles de génération et les modes d'échec.
  - `03-easy-checks/` : la grille XLSX y est générée, et `evaluation_contract.yml` y vit.
  - `wcag/` et `fiche-pratique/` : sources Markdown des fiches WCAG et des mémos PDF.
  - `liens-tp-en-ligne.md`, `corpus-documentaire-preparatoire/01-cadre-legal/cadre-legal.md`, `03-easy-checks/web.md` : source de la fiche des liens et transcriptions du deck.
  - `corpus-documentaire-preparatoire/04-reseaux-sociaux/` : seulement les Markdown et les images réellement utilisées (un script y lit encore), pas les anciens PPTX.
- **À discuter** : `pedagogie-methode/` (références pédagogiques, 20 Ko), `gestast.md`, `cadrage-usine-standalone.md` (ce document).

## Ce qui reste dehors

- Les installeurs de `outils/` : remplacés par le `MANIFEST.md` existant, complété de l'URL officielle, de la version et de l'empreinte SHA-256 de chaque fichier. Le pack final les récupère au moment de l'assemblage. Raison : un binaire versionné pèse pour toujours dans l'historique, GitHub refuse les fichiers de plus de 100 Mo et avertit dès 50 Mo (CCA est à 87 Mo).
- `outputs/`, `tmp/`, `.qa/`, `.pytest_cache/`, `.ruff_cache/`, `__pycache__/`, `useless-report/` : régénérables ou hors chaîne.
- `archive-oldformation-102638-juin-2026.pptx`, `20250926_COI_presentation…pptx`, `docs-publication.pdf` : archives, déjà dans l'historique du workspace.
- Le clone `tp-easy-check-site-web-igpde/` : c'est un dépôt git dans un dépôt git, la même cause que le lien cassé d'hier. Il reste un dossier de travail ignoré, ou devient un sous-module assumé.
- La convocation nominative : déjà hors de git.

## Les dépendances cachées qui casseraient l'autonomie

1. **Les règles héritées.** `CLAUDE.md` commence par « Hérite de `~/.claude/CLAUDE.md` et `~/Claude/CLAUDE.md` ». Cloné ailleurs, l'agent perd les règles git, de langue, de commit. Il faut un `CLAUDE.md` et un `AGENTS.md` auto-suffisants.
2. **Les hooks.** Les contrôles actuels (Markdown au pre-commit, CHANGELOG au pre-push, formatage à l'écriture) viennent du workspace. Une session ouverte dans un sous-dossier ne charge pas les hooks du projet parent : l'usine doit porter ses propres contrôles, ou accepter de s'en passer.
3. **La fabrication des PDF.** Les mémos, fiches WCAG et la fiche des liens sont produits par le skill `accessible-pdf` du workspace (`~/Claude/.claude/skills/accessible-pdf/scripts/md2pdf.py`), pas par `scripts/`. Il faut l'embarquer (vendoring) ou documenter la dépendance.
4. **Les skills de conception.** `CLAUDE.md` impose `/pedagogie-neuro`, `/composition-dsfr-pptx`, `/accessible-pptx` avant toute nouvelle slide : ce sont des skills du workspace, absents d'un clone isolé.
5. **Les chemins absolus.** `scripts/build_template.py` et `scripts/rebuild_template_from_demo.py` pointent vers un chemin absolu de l'espace de travail d'Alex et vers des fichiers qui ne sont plus à la racine du projet : à corriger ou à retirer.
6. **L'environnement Python.** `python-pptx` n'est installé que dans `/opt/homebrew/bin/python3.12`. L'usine doit fixer son environnement (`uv` ou `venv` avec dépendances épinglées).

## Harnais ShipGuard et Loriq, concrètement

- **ShipGuard** est un plugin Claude Code : on ne l'embarque pas, on embarque ses manifestes. Or ils existent déjà, mal rangés : `docs/visual-tests/` est l'outillage de recette visuelle, publié par erreur sur le site public et qui fait échouer `validate.py`. Dans l'usine, il sort de `docs/` (par exemple `recette/visual-tests/`). `retour-shipguard.md` contient tes propositions d'amélioration du plugin : c'est une note, pas un composant.
- **Loriq** est le dépôt tiers de Loïc (`projets-heberges/Loriq`, push désactivé). La seule trace « contrat » dans le projet est `03-easy-checks/evaluation_contract.yml`, qui porte encore le code 102638. Question ouverte : qu'attends-tu de Loriq ici (entrées signées, contrats de comportement, cérémonie de validation) ? Sans réponse, je recommande de ne pas le brancher au départ : une dépendance tierce de plus pour un gain non défini.

## Le nom

`usine-fabrication-igpde-102846-ay11` fige le code 102846 dans le nom, alors qu'il a changé cette semaine (102638 vers 102846) et changera probablement en 2027. Le code vit déjà dans `config.yml`. Proposition : `usine-formation-ay11-igpde`, et une session par dossier de livraison (`livraisons/2026-10-09-102846/`).

## L'historique git

Deux options :

- **Départ neuf** (recommandé) : premier commit « genèse » qui cite le commit source du workspace (`d496f1c29`). L'historique complet reste consultable dans `claude-workflow-perso`.
- **Extraction de l'historique** (`git filter-repo` sur un clone) : garde les commits depuis mai, mais embarque les 199 Mo d'installeurs déjà présents dans cet historique, sauf à les purger aussi. Plus lourd, pour peu de valeur.

## Le sort de la copie dans le workspace

C'est le vrai risque : deux sources de vérité modifiées en parallèle. Après bascule vérifiée, `projets-formations/IGPDE-Carinne-C/` doit être remplacé par un README qui pointe vers le nouveau dépôt. Cette suppression demande ton accord explicite, et une vérification par empreinte que rien ne manque.

## Questions à trancher

1. Le dépôt sera-t-il **privé** ? Il contiendrait des gabarits IGPDE, des ressources sous licence tierce et des noms d'intervenants : je le recommande privé.
2. L'usine doit-elle être autonome **pour toi seul** sur ce Mac, ou **distribuable** (Codex, un collègue, une autre machine) ? Cela décide de l'effort sur les points 1 à 6 des dépendances.
3. Les installeurs : **manifeste avec téléchargement** (recommandé), Git LFS, ou hors dépôt ?
4. Le pack livrable : **fabriqué** par un script d'assemblage à partir des sources (recommandé), ou **copie versionnée** comme aujourd'hui ?
5. Loriq : quel rôle précis, ou pas de Loriq au départ ?
6. Le nom : garde-t-on 102846 dedans ?

## Décisions d'Alex du 2026-09-27

1. Dépôt **public** : `https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11`, copie locale dans `git-hors-workflow/usine-fabrication-igpde-102846-ay11`. Le nom avec 102846 est conservé.
2. Autonomie : macOS (environnement d'Alex en priorité), agnostique autant que possible entre Claude, Codex et autres agents.
3. Loriq non branché au départ. ShipGuard non embarqué, ses manifestes conservés et rangés au bon endroit ; `validate.py` doit passer au vert.
4. Historique extrait (le travail effectué doit rester visible).
5. La copie du workspace n'est supprimée qu'après la mise en place complète (distant et local) et sur le GO explicite d'Alex.

Constats du même jour qui en découlent :

- Le compte `Alexmacapple` relié à ce Mac n'a que le droit de lecture sur le dépôt cible (vérifié par l'API GitHub) : aucun push possible en l'état.
- L'historique du projet compte 153 commits depuis le 2026-04-11. Il contient les installeurs CCA (87 Mo) et NVDA (38 Mo), la convocation nominative (3 commits) et l'adresse `alexandra.guiderdoni@gmail.com` comme auteur de tous les commits.
- Données de tiers dans les fichiers candidats : téléphone et adresse de Carine Couplan (`_source/references/Notes-formation.md`), photo et adresse professionnelle de Bertrand Matge (slides intervenant et contact), nom de la gestionnaire IGPDE (`CLAUDE.md`, `AGENTS.md`), transcriptions de conversations d'agents (`_source/agent-artifacts/`).
- Contenus IGPDE ou de tiers dans `_source/presentations-source/` : gabarit IGPDE (indispensable à la génération), gabarits, présentation de Carine, présentation de Martine.

## Réponses d'Alex aux questions du 2026-09-27

1. **Accès en écriture** : Alex invite `Alexmacapple` comme collaborateur avec droit d'écriture ; l'accès est vérifié par l'API avant tout push.
2. **Contenus IGPDE et de tiers** : tout est publié (gabarits, présentations de Carine et de Martine, originaux 102638), sous la responsabilité d'Alex.
3. **Données personnelles** : anonymisation. `Notes-formation.md` est conservé sans le téléphone ni l'adresse de Carine, y compris dans l'historique ; la convocation et `_source/agent-artifacts/` sont purgés de l'historique ; le nom de la gestionnaire IGPDE, la salle et les horaires sont retirés des `CLAUDE.md` et `AGENTS.md` publics.
4. **Bertrand** : il est d'accord, sa photo et son adresse professionnelle sont publiées.
5. **Courriel des commits** : `alexandra.guiderdoni@gmail.com` reste visible dans l'historique.
6. **Messages de commit** : neutralisés par l'agent sans validation préalable (mentions d'autres projets ou de l'infrastructure), résultat montré après coup.
7. **Licence** : etalab-2.0. Le site `easy-check-igpde` reste sous `alexmacapple.github.io`, publié depuis l'usine par le playbook actuel.

## Plan proposé, après tes réponses

1. Inventaire par empreinte de tout ce qui entre, avec la liste de ce qui reste dehors et pourquoi.
2. Création du dépôt dans `git-hors-workflow/` (déjà ignoré par le workspace), `.gitignore` et environnement Python épinglé.
3. Copie des sources, correction des chemins absolus, `CLAUDE.md` et `AGENTS.md` auto-suffisants.
4. Script d'assemblage du pack livrable à partir de `config.yml`.
5. Preuve de fonctionnement sur un clone frais, dans un autre dossier : régénération du deck, 69 tests, `validate.py`, assemblage du pack, et comparaison du deck produit avec celui d'aujourd'hui.
6. Inscription dans `DEPOTS-AUTONOMES.md`, puis seulement ensuite, sur ton accord, remplacement de la copie du workspace par un pointeur.

**Critère de réussite** : un clone frais, sur un dossier vierge, produit le deck, le site, la grille et le pack sans aucun fichier du workspace, et tous les contrôles passent.

## Contraintes et hypothèses

- Estimations de taille faites sur `du` : environ 90 Mo pour l'usine, hypothèse à confirmer à l'inventaire.
- Hypothèse : le site `easy-check-igpde` reste un dépôt séparé, publié depuis `docs/` par le playbook actuel.
- Non vérifié : la licence de redistribution des gabarits IGPDE et du guide « Accessibiliser sa communication » dans `_source/`.
