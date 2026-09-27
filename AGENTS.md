# Usine de la formation 102846 (IGPDE) - protocole agent

Protocole unique pour tout agent (Claude, Codex ou autre) et pour un humain. `CLAUDE.md` l'importe. Ce dépôt est autonome : aucune règle n'est héritée d'un espace de travail extérieur.

## Contexte

- Formation « L'accessibilité numérique pour la bureautique et le web », IGPDE, code 102846 (ex-102638), 1 jour, public communicants, pas développeurs.
- Session du 9 octobre 2026. Code, date, pied de page, nom du deck et dossier de livraison sont centralisés dans `config.yml` : c'est la seule source à modifier pour une nouvelle session.
- Deck de 138 slides DSFR, 4 modules dans un ordre impératif : 1. communication accessible et cadre légal, 2. Word accessible, 3. points de contrôle rapides W3C, 4. réseaux sociaux.
- Exercice Sami : 21 critères à vérifier dans 3 DOCX (inaccessible, aide à la correction, accessible), spécification dans `_source/exercice-sami-spec.md`.
- Site d'exercice dans `docs/` (versions `site-inaccessible/`, `site-aide-correction/`, `site-accessible/`, démo émojis, grille XLSX), publié sur https://alexmacapple.github.io/easy-check-igpde/ depuis le dépôt `git@github.com:Alexmacapple/easy-check-igpde.git`.
- Pack remis à l'IGPDE : `IGPDE-102846-livrables-octobre-2026/`, fabriqué par `make pack`.

## Environnement

- macOS en priorité, Python 3.12 (Homebrew), `uv`, et pour les PDF : `pandoc`, `pango`, `glib` (Homebrew).
- `make installer` crée `.venv` depuis `requirements.lock` (installation avec vérification des empreintes) et active les hooks git versionnés (`.githooks`).
- Sans `.venv`, le `Makefile` utilise `/opt/homebrew/bin/python3.12`. Toutes les commandes passent par `make` : `make aide` les liste.

## Chaîne de fabrication

- **Ne jamais modifier le PPTX directement.** Éditer `scripts/slides/NN_*.py`, puis `make deck`. La prochaine régénération écraserait toute retouche faite dans PowerPoint. État au 2026-09-27 : les 138 slides sont générées par script.
- Nommage des modules : `NN_nom.py` ou `NNxx_nom.py` pour intercaler (`02ma_`, `05a_`). L'ordre du deck suit l'ordre alphabétique des fichiers ; le numéro du fichier n'est donc pas la position dans le deck.
- Chaque module expose `build(prs, layouts, ctx)` et utilise `ctx.page_num`, `ctx.date`, `ctx.footer_base`, jamais de valeur en dur.
- Composants : exclusivement `scripts/igpde_dsfr_components.py` (grille IGPDE 13,33 x 7,5 pouces), jamais une bibliothèque DSFR extérieure.
- `finalize_pptx()` est obligatoire (langue, ordre de lecture, métadonnées, quarantaine macOS) ; `scripts/assemble.py` l'appelle.
- Tester une slide : `python scripts/assemble.py --only NN`.
- DOCX de l'exercice Sami : `python scripts/generate_exercice_sami.py`.
- Grille d'audit : `make grille`. PDF du pack : `make pdf` (générateur embarqué dans `vendor/`).
- Gabarit IGPDE : `_source/presentations-source/PPT-IGPDE-DSFR-base-intervenant.pptx`. S'il manque : `python scripts/rebuild_template_from_demo.py`.
- Le site `docs/` est maintenu à la main page par page : ne pas relancer `scripts/generate_easy_checks_site_skeleton.py` sans comparer ensuite le diff complet, il écraserait les corrections faites depuis juillet.

## Qui fabrique quoi dans le pack

`make pack` enchaîne tout ce qui se génère. Chaque livrable relève de l'une de ces trois catégories.

- **Généré par une commande**
  - Deck `support-formation-*.pptx` : `make deck`, copié dans le pack par `make pack`.
  - Export PDF du deck (`Formateur/_alex/`) : `make supports` (nécessite LibreOffice).
  - Mémos Word et LibreOffice, fiches WCAG formateur et stagiaire, fiche des liens des TP : `make pdf`, depuis `fiche-pratique/*.md`, `wcag/*.md` et `liens-tp-en-ligne.md`.
  - Documents Sami (`Formateur/tp-word-igpde/`) : `make sami` dans `_source/`, puis `make supports` pour la copie dans le pack.
  - Démo réseaux sociaux hors ligne (`Formateur/tp-reseaux-sociaux-igpde/`) : `make supports`, depuis `docs/demo-mauvaise-restitution-emojis.html`.
  - Grille d'audit XLSX : `make grille` (dans `03-easy-checks/` et dans le site).
  - Installeurs (`outils/`) : `make outils-telecharger`, sauf PAC à déposer à la main (voir `outils/MANIFEST.md`).
- **Document source édité à la main** (pas de générateur : modifier le fichier, garder l'original dans `V1/`)
  - Fiche catalogue, fiche technique, programme et déroulé (`Formateur/documents-administratifs-igpde/`), au format Word de l'IGPDE.
  - Site d'exercice `docs/`, publié par `make publier-site`.
  - Notes formateur `Formateur/_alex/*.md` et `alternatives.*`.
- **Ressource fixe** (fournie, jamais régénérée)
  - Cartes idées reçues (`Formateur/ice-breaker-idées-recues-cartes-igpde/`), cartes WCAG 2.2 (`fil-rouge-principes-wcag-igpde/WCAG-2.2-Card-Deck-FR-6-par-page.pdf`), bandeaux IGPDE.
  - Convocation des intervenants : sur le disque seulement, jamais versionnée.

`scripts/assemble_reseaux_sociaux.py` est obsolète : les slides du module 4 sont intégrées au deck principal. `scripts/generate_demo.py` est hors chaîne (voir `todo.md`).

## Vérifier avant de livrer

- `make verifier` : 69 tests, validation du site (`validate.py`), contrôles du dépôt. Le verdict se lit sur le code de sortie.
- `make qa` : boucle qualité du deck. Lire `.qa/qa-pptx-report.md` et son champ `status` ; le code de sortie seul ne prouve pas la convergence.
- Réexport complet du deck : suivre `REEXPORTER-DECK-PPTX.md`.
- Recette visuelle du site corrigé : `make recette` (plugin ShipGuard requis ; ses manifestes sont dans `recette/visual-tests/`).
- Une relecture visuelle humaine du deck reste nécessaire : les contrôles automatiques ne voient pas les chevauchements fins.

## Publier

- Site : `make publier-site` (valide, synchronise `docs/` vers le clone du dépôt du site, commit et push). Détail : `PUBLIER-SITE.md`.
- Dépôt de l'usine : commits en français, forme nominale, première ligne de 50 caractères au plus, sans point final. Aucune ligne d'attribution d'agent (`Co-Authored-By`, `Generated with` ou signature d'outil).
- Les hooks `.githooks/pre-commit` bloquent : fichiers de verrou Office, fichiers de plus de 50 Mo, convocation, installeurs, tirets cadratins dans les scripts, chemins personnels absolus. Ne jamais les contourner avec `--no-verify`.

## Dépôt public : règles de contenu

- Ce dépôt est public. Ne jamais y ajouter de coordonnées personnelles de tiers (téléphone, adresse), de convocation nominative, de transcription de conversation d'agent, ni d'informations logistiques de session (salle, horaires, gestionnaire).
- Les installeurs du pack ne sont pas versionnés : `make outils-telecharger` les récupère et vérifie leur empreinte (`outils/outils.json`).

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
- Colonnes : `COL_W` 5,98 et `COL_R` 6,83 ; contenu de `TOP` 2,68 à `BOTTOM_CONTENT` 6,80 ; ligne de pied `FOOTER_Y` 6,98.
- Layouts : `couverture`, `titre_soustitre` (logos), `titre_contenu` (standard), `chapitre`, `sommaire`, `3_colonnes`.
- Composants : `add_callout`, `add_alert`, `add_highlight`, `add_quote`, `add_card`, `add_pave_chiffre`, `add_stepper`, `add_tableau`, `add_image`, `add_texte_libre`, `add_notes`, `add_encadre`, `add_fleche`, `compose_sommaire`, `compose_chapitre`.

## À ne pas faire

- Jamais de français sans accents, dans les slides, les scripts et les documents.
- Jamais de tiret cadratin ni demi-cadratin dans les scripts : tiret simple.
- Jamais `slide.shapes.add_textbox()` direct : utiliser `add_texte_libre` (pouces et EMU).
- Jamais toucher à la ligne séparatrice IGPDE (y = 6,98) ni à la disposition des logos.
- Jamais de jargon développeur dans les slides (ARIA, DOM, CSS).
- Pas de mot « pilier » : utiliser « thème ».

## Modes d'échec connus

- `add_alert` ou `add_callout` reçoit une chaîne au lieu d'une liste : chaque caractère devient une puce.
- Changement typographique global sans recalibrer `_estimate_height` : des dizaines de slides débordent.
- `add_image` sans `height=` près d'un autre composant : l'image déborde ; ne pas supposer que hauteur de texte plus hauteur d'image suffit, vérifier le rendu.
- `layout_name="titre_soustitre"` sur une slide de contenu : les logos institutionnels apparaissent.
- `accent_w` différent de 0,08 (0,16 pour un chapitre) : défaut d'alignement visible.
- Placeholder de titre : copier les 4 dimensions, sinon `left` et `width` tombent à 0.
- `_safe_top` remonte un composant pour éviter le débordement bas, mais peut créer un chevauchement avec le bloc précédent.
- Avertissement de pied de page : ne jamais l'ignorer ; resserrer ou recomposer la slide, viser `TOTAL_WARNINGS 0`.
- Un `.gitignore` global d'un autre dépôt peut exclure des formats entiers (PPTX, DOCX, MP4) : vérifier qu'un livrable est bien suivi (`git ls-files`), pas seulement présent sur le disque.

## Références

- Contraintes et limites connues : `contraintes.md`. Leçons techniques : `lessons.md`. Suivi : `todo.md`.
- Architecture de la chaîne : `architecture-c4-slides.md`. Index slides et modules : `scripts/slides/README.md`.
- Exercice Sami : `_source/exercice-sami-spec.md`, `_source/exercice-sami-diff.md`.
- Points de contrôle rapides W3C : `03-easy-checks/w3c-easy-checks-fr.md`. Contrat d'évaluation : `03-easy-checks/evaluation_contract.yml`.
- Guide « Accessibiliser sa communication » : `_source/references/Guide-2026-Accessibiliser-sa-communication-police-14-coul.md`.
- Notes de contenu : `04-reseaux-sociaux/md-reseaux-sociaux.md`, `05-falc/md-falc.md`, `06-medias/md-medias.md`.
- Passations de session : `_source/passation-session-2026-05-03.md`, `_source/passation-session-2026-05-04.md`.
- Deck WCAG condensé : `wcag/WCAG en langage clair - condensé.pptx` (13 slides), `python scripts/generate_wcag_langage_clair.py --condensed`.
