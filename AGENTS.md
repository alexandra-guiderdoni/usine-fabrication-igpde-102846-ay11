# Usine de la formation 102846 (IGPDE) - protocole agent

Protocole unique pour tout agent (Claude, Codex ou autre) et pour un humain. `CLAUDE.md` l'importe. Ce dépôt est autonome : aucune règle n'est héritée d'un espace de travail extérieur. Si l'environnement de l'agent charge malgré tout des règles d'un dossier parent (par exemple une grille DSFR générique ou une autre bibliothèque de composants), elles ne s'appliquent pas ici : ce fichier et le code de l'usine priment.

## Contexte

- Formation « L'accessibilité numérique pour la bureautique et le web », IGPDE, code 102846 (ex-102638), 1 jour, public communicants, pas développeurs.
- Session du 9 octobre 2026. Code, date, pied de page, nom du deck et dossier de livraison sont centralisés dans `config.yml` : c'est la seule source des paramètres lus par la fabrication. Une nouvelle session demande en plus de renommer le dossier du pack, de mettre à jour à la main les documents administratifs, et de rechercher l'ancien code et l'ancienne date dans `docs/` et dans les Markdown structurants, qui citent le dossier du pack en toutes lettres.
- Deck de 138 slides DSFR, 4 modules dans un ordre impératif : 1. communication accessible et cadre légal, 2. Word accessible, 3. points de contrôle rapides W3C, 4. réseaux sociaux.
- Exercice Sami : 21 critères à vérifier dans 3 DOCX (inaccessible, aide à la correction, accessible), spécification dans `_source/exercice-sami-spec.md`.
- Site d'exercice dans `docs/` (versions `site-inaccessible/`, `site-aide-correction/`, `site-accessible/`, démo émojis, grille XLSX), publié sur https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/ depuis le dépôt `git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git`.
- Pack remis à l'IGPDE : `livrables-IGPDE-2026-102846/`, fabriqué par `make pack`.

## Deux dépôts liés : l'usine et le site publié

Le flux ne va que dans un sens : usine, puis site publié. Jamais l'inverse.

- **Cette usine** (`alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11`) est la seule source. Le site se modifie dans `docs/`. Le `README.md`, l'`AGENTS.md` et le `CLAUDE.md` du dépôt publié se modifient dans `publication-site/`, sous les noms `README.md`, `agents-site.md` et `claude-site.md`.
- **Le dépôt du site** (`alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11`) n'est qu'une copie de publication servie par GitHub Pages. Chacun de ses fichiers correspond à `docs/<même chemin>`, sauf `README.md`, `AGENTS.md` et `CLAUDE.md`, qui viennent de `publication-site/`.
- **Deux clones locaux du site**, en lecture seule pour un humain comme pour un agent (seul `make publier-site` y écrit) :
  - `livrables-IGPDE-2026-102846/Formateur/tp-easy-check-site-web-igpde/` : clone de publication, écrit par `make publier-site` (variable `SITE_CLONE`), ignoré par l'usine ;
  - `../tp-fabrication-igpde-102846-ay11/`, à côté de l'usine quand il existe : clone de consultation, avancé automatiquement à la fin de `make publier-site` (variable `SITE_CONSULTATION`).
- **MUST** : pour changer le site, éditer `docs/`, lancer `make verifier`, puis `make publier-site`. Pour savoir ce qui est en ligne, lire `docs/` ou l'adresse publique, pas un clone.
- **MUST NOT** : modifier, commiter ou pousser dans un clone du site. La publication suivante synchronise avec suppression et effacerait la modification ; un commit poussé depuis un clone ferait aussi échouer le push de `make publier-site`.
- **MUST NOT** : renommer `publication-site/agents-site.md` ou `claude-site.md` en `AGENTS.md` ou `CLAUDE.md` dans l'usine. Sous ces noms, les agents appliqueraient au dossier `publication-site/` la consigne « ne rien modifier ici », destinée au seul dépôt publié. `make publier-site` leur donne leur vrai nom au moment de la copie.

## Environnement

- macOS en priorité, Python 3.12 (Homebrew), `uv`, et pour les PDF : `pandoc`, `pango`, `glib` (Homebrew).
- `make installer` crée `.venv` depuis `requirements.lock` (installation avec vérification des empreintes) et active les hooks git versionnés (`.githooks`).
- Sans `.venv`, le `Makefile` utilise `/opt/homebrew/bin/python3.12`, et à défaut le `python3` du système, sans garantie sur les dépendances : lancer `make installer` d'abord. Les commandes courantes passent par `make` (`make aide` les liste) ; les quelques scripts sans cible (test d'une seule slide, diagnostics de `REEXPORTER-DECK-PPTX.md`) s'appellent avec le même interpréteur.

## Chaîne de fabrication

- **Ne jamais modifier le PPTX directement.** Éditer `scripts/slides/NN_*.py`, puis `make deck`. La prochaine régénération écraserait toute retouche faite dans PowerPoint. État au 2026-09-27 : les 138 slides sont générées par script.
- Nommage des modules : `NN_nom.py` ou `NNxx_nom.py` pour intercaler (`02a_`, `02ma_`). L'ordre du deck suit l'ordre alphabétique des fichiers ; le numéro du fichier n'est donc pas la position dans le deck.
- Chaque module expose `build(prs, layouts, ctx)` et utilise `ctx.page_num`, `ctx.date`, `ctx.footer_base`, jamais de valeur en dur.
- Composants : exclusivement `scripts/igpde_dsfr_components.py` (grille IGPDE 13,33 x 7,5 pouces), jamais une bibliothèque DSFR extérieure.
- `finalize_pptx()` est obligatoire (langue, ordre de lecture, métadonnées, quarantaine macOS) ; `scripts/assemble.py` l'appelle.
- Tester une seule slide (pas de cible `make`) : `.venv/bin/python scripts/assemble.py --only NN`, ou `/opt/homebrew/bin/python3.12` sans `.venv`. Cette commande écrit un deck partiel à la racine : relancer `make deck` ensuite. Le livrable du pack n'est jamais remplacé par un deck partiel. Même interpréteur pour les autres scripts appelés directement ci-dessous.
- DOCX de l'exercice Sami : `make sami` (écrit dans `_source/`). Grille d'audit : `make grille`. Deck WCAG condensé : `make wcag`. PDF du pack : `make pdf` (générateur embarqué dans `vendor/`).
- Gabarit IGPDE : `_source/presentations-source/PPT-IGPDE-DSFR-base-intervenant.pptx`. S'il manque : `scripts/rebuild_template_from_demo.py`, depuis `_source/presentations-source/gabarits-ppt-igpde.pptx`. `scripts/build_template.py` est historique : sa source IGPDE native n'est plus dans le dépôt.
- Le site `docs/` est maintenu à la main page par page : ne pas relancer `scripts/generate_easy_checks_site_skeleton.py` sans comparer ensuite le diff complet, il écraserait les corrections faites depuis juillet.

## Qui fabrique quoi dans le pack

`make pack` régénère le deck, puis les PDF, les supports et la vérification des outils. Il ne relance ni `make sami`, ni `make grille`, ni `make wcag` : les lancer d'abord si leurs sources ont changé. Chaque livrable relève de l'une de ces trois catégories.

- **Généré par une commande**
  - Deck `support-formation-*.pptx` : `make deck`, qui génère le deck à la racine (sortie de travail, ignorée par git) puis le copie dans le pack (livrable versionné). La copie refuse un deck partiel.
  - Export PDF du deck (`Formateur/_alex/`) : `make supports` (nécessite LibreOffice).
  - Mémos Word et LibreOffice, fiches WCAG formateur et stagiaire, fiche des liens des TP : `make pdf`, depuis `fiche-pratique/*.md`, `wcag/*.md` et `liens-tp-en-ligne.md`. `make pdf` n'accepte que du PDF/UA-1 : sinon il s'arrête en erreur et laisse le livrable précédent en place (voir `contraintes.md`).
  - Documents Sami (`Formateur/tp-word-igpde/`) : `make sami` (écrit dans `_source/`), puis `make supports` ou `make pack` pour la copie dans le pack.
  - Démo réseaux sociaux hors ligne (`Formateur/tp-reseaux-sociaux-igpde/`) : `make supports`, depuis `docs/demo-mauvaise-restitution-emojis.html`.
  - Grille d'audit XLSX : `make grille` (dans `03-easy-checks/` et dans le site).
  - Installeurs (`livrables-IGPDE-2026-102846/outils/`) : `make outils-telecharger`, sauf PAC à déposer à la main (voir `MANIFEST.md` dans ce dossier).
- **Document source édité à la main** (pas de générateur : modifier le fichier ; les versions précédentes restent dans l'historique git, pas de copie sur le disque)
  - Fiche catalogue, fiche technique, programme et déroulé (`Formateur/documents-administratifs-igpde/`), au format Word de l'IGPDE.
  - Site d'exercice `docs/`, publié par `make publier-site`.
  - Notes formateur `Formateur/_alex/*.md` et `alternatives.*`.
  - README du dossier `Formateur/fil-rouge-principes-wcag-igpde/`.
- **Ressource fixe** (fournie, jamais régénérée)
  - Cartes idées reçues (`Formateur/ice-breaker-idées-recues-cartes-igpde/`), cartes WCAG 2.2 (`fil-rouge-principes-wcag-igpde/cartes-criteres-wcag-2-2-a-imprimer.pdf`, crédits et licence dans `CREDITS.md` à côté), bandeaux IGPDE.
  - Convocation des intervenants : sur le disque seulement, jamais versionnée.

`scripts/assemble_reseaux_sociaux.py` est obsolète : les slides du module 4 sont intégrées au deck principal. `scripts/generate_demo.py` est hors chaîne (voir `todo.md`).

## Vérifier avant de livrer

- `make verifier` : 87 tests (dont la déclaration PDF/UA-1 des PDF livrés), validation du site (`validate.py`), contrôles du dépôt. Le verdict se lit sur le code de sortie.
- `make qa` : boucle qualité du deck. Lire `.qa/qa-pptx-report.md` et son champ `status` ; le code de sortie seul ne prouve pas la convergence.
- Réexport complet du deck : suivre `REEXPORTER-DECK-PPTX.md`.
- Recette visuelle du site corrigé : `make recette` (plugin ShipGuard requis ; ses manifestes sont dans `recette/visual-tests/`).
- Une relecture visuelle humaine du deck reste nécessaire : les contrôles automatiques ne voient pas les chevauchements fins.

## Publier

- Site : `make publier-site` (valide, synchronise `docs/` et `publication-site/` vers le clone de publication, commit, push, puis avance le clone de consultation). Voir « Deux dépôts liés » ci-dessus et `PUBLIER-SITE.md`.
- Dépôt de l'usine : commits en français, forme nominale, première ligne de 50 caractères au plus, sans point final. Aucune ligne d'attribution d'agent (`Co-Authored-By`, `Generated with` ou signature d'outil).
- Le hook `.githooks/pre-commit` bloque : fichiers de verrou Office, fichiers de plus de 50 Mo, convocation, installeurs `.msi` et `.exe`, tirets cadratins dans `scripts/`, chemins personnels absolus dans les dossiers qu'il surveille (`scripts/`, `tests/`, `recette/`, `docs/`, `fiche-pratique/`, `wcag/`, `03-easy-checks/`, `Makefile`, `config.yml`, `validate.py`, `liens-tp-en-ligne.md`). Ailleurs, notamment dans `notes/` et `_source/`, la règle reste à appliquer à la main. Ne jamais contourner le hook avec `--no-verify`.

## Dépôt public : règles de contenu

- Ce dépôt est public. Ne jamais ajouter aux fichiers de travail (Markdown, scripts, notes, todo) de coordonnées personnelles de tiers (téléphone, adresse), de convocation nominative, de transcription de conversation d'agent, ni d'informations logistiques de session (salle, horaires, gestionnaire) : ces informations restent dans la convocation, hors dépôt. Les documents administratifs IGPDE du pack (fiche catalogue, fiche technique, programme, déroulé) sont publiés tels quels, par décision d'Alex.
- Les installeurs du pack ne sont pas versionnés : `make outils-telecharger` les récupère et vérifie leur empreinte (`livrables-IGPDE-2026-102846/outils/outils.json`).

## Règles pédagogiques validées

- La version accessible du site d'exercice reste sobre, comme un vrai site corrigé, sans pédagogie visible.
- Les erreurs de formulaire n'apparaissent qu'après une tentative de soumission ou une interaction avec le champ.
- Les documents accessibles déclarent une langue cohérente (`fr`). Les versions volontairement inaccessibles peuvent garder des défauts pédagogiques explicites.
- Exercice : ne pas distribuer la checklist au moment de l'identification ; les stagiaires diagnostiquent d'abord sans filet.
- Quiz : questions et réponses sur des slides séparées (suffixe `b`).

## Compétences recommandées, si l'agent en dispose

- Nouvelle slide ou restructuration pédagogique : `pedagogie-neuro`, puis `composition-dsfr-pptx`, puis `accessible-pptx`.
- Corpus à transformer en présentation : `pedagogie-neuro`, `slides-pedagogiques`, `composition-dsfr-pptx`, `accessible-pptx`.
- Ces compétences ne sont pas dans le dépôt. Sans elles, appliquer les règles de ce fichier et la grille ci-dessous.

## Grille IGPDE-DSFR

- Format 13,33 x 7,5 pouces ; marge gauche `MARGIN_L` 0,52 ; largeur utile `CONTENT_W` 12,28.
- Colonnes : `COL_W` 5,98 et `COL_R` 6,83 ; contenu de `TOP_CONTENT` 2,68 à `BOTTOM_CONTENT` 6,80 ; ligne de pied `FOOTER_Y` 6,98.
- Layouts : `couverture`, `titre_soustitre` (logos), `titre_contenu` (standard), `chapitre`, `sommaire`, `3_colonnes`.
- Composants (17 `add_*` et 2 `compose_*`, tous dans `scripts/igpde_dsfr_components.py`) : `add_callout`, `add_alert`, `add_highlight`, `add_quote`, `add_card`, `add_pave_chiffre`, `add_stepper`, `add_tableau`, `add_image`, `add_texte_libre`, `add_qrcode`, `add_checklist`, `add_avant_apres`, `add_exemple_contre_exemple`, `add_notes`, `add_encadre`, `add_fleche`, `compose_sommaire`, `compose_chapitre`. Vérifier qu'un composant existe avant d'en créer un.

## À ne pas faire

- Jamais de français sans accents, dans les slides, les scripts et les documents.
- Jamais de tiret cadratin ni demi-cadratin dans les scripts : tiret simple.
- Jamais `slide.shapes.add_textbox()` direct : utiliser `add_texte_libre` (pouces et EMU).
- Jamais toucher à la ligne séparatrice IGPDE (y = 6,97, soit `FOOTER_Y` moins 0,01) ni à la disposition des logos.
- Jamais de jargon développeur dans les slides (ARIA, DOM, CSS).
- Pas de mot « pilier » dans le texte affiché des slides : utiliser « thème ». Les noms de fichiers historiques (`08_pilier1-…`) restent tels quels.

## Modes d'échec connus

- `add_alert` ou `add_callout` reçoit une chaîne au lieu d'une liste : chaque caractère devient une puce.
- Changement typographique global sans recalibrer `_estimate_height` : des dizaines de slides débordent.
- `add_image` sans `height=` près d'un autre composant : l'image déborde ; ne pas supposer que hauteur de texte plus hauteur d'image suffit, vérifier le rendu.
- `layout_name="titre_soustitre"` sur une slide de contenu : les logos institutionnels apparaissent.
- `accent_w` différent de 0,08 (0,16 pour un chapitre) : défaut d'alignement visible.
- Placeholder de titre : copier les 4 dimensions, sinon `left` et `width` tombent à 0.
- `_safe_top` remonte un composant pour éviter le débordement bas, mais peut créer un chevauchement avec le bloc précédent.
- Avertissement de pied de page : ne jamais l'ignorer ; resserrer ou recomposer la slide, viser `TOTAL_WARNINGS 0`.
- Tableau coupé entre deux pages dans une source de `wcag/` : WeasyPrint refuse le PDF/UA-1 et `make pdf` s'arrête ; garder le style qui laisse les tableaux entiers, en tête de la source.
- Un `.gitignore` global d'un autre dépôt peut exclure des formats entiers (PPTX, DOCX, MP4) : vérifier qu'un livrable est bien suivi (`git ls-files`), pas seulement présent sur le disque.

## Références

- Contraintes et limites connues : `contraintes.md`. Leçons techniques : `lessons.md`. Suivi : `todo.md`.
- Architecture de la chaîne : `architecture-c4-slides.md`. Index slides et modules : `scripts/slides/README.md`.
- Exercice Sami : `_source/exercice-sami-spec.md`, `_source/exercice-sami-diff.md`.
- Points de contrôle rapides W3C : `03-easy-checks/w3c-easy-checks-fr.md`. Contrat d'évaluation : `03-easy-checks/evaluation_contract.yml`.
- Guide « Accessibiliser sa communication » : `_source/references/Guide-2026-Accessibiliser-sa-communication-police-14-coul.md`.
- Notes de contenu : `04-reseaux-sociaux/md-reseaux-sociaux.md`, `05-falc/md-falc.md`, `06-medias/md-medias.md`.
- Passations de mai 2026, historiques (écrites dans l'ancien espace de travail, ne pas suivre leurs commandes) : `_source/passation-session-2026-05-03.md`, `_source/passation-session-2026-05-04.md`.
- Deck WCAG condensé : `wcag/WCAG en langage clair - condensé.pptx` (13 slides), régénéré par `make wcag`.
- Pourquoi le projet est construit ainsi : `notes/readme-causal.md` (histoire, sans consigne de travail).
