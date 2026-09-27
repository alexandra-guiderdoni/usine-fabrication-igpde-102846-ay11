# Architecture C4 — Pipeline de génération des slides PPTX DSFR

## Contraintes et hypothèses

**Sources locales lues** :
- `CLAUDE.md`, `AGENTS.md`, `contraintes.md`
- `scripts/assemble.py`, `scripts/slides/__init__.py`
- `scripts/igpde_dsfr_components.py` (lignes 1-200, 302, 445-580, 631-1000, 1090-1230, 1287-1408)
- `scripts/build_template.py`
- `scripts/slides/02ma_definition-a11y.py` (module type)

**Système en scope** : pipeline de génération du deck PPTX principal `support-formation-102846-2026-IGPDE.pptx` (138 slides DSFR accessibles, nom porté par `config.yml`).

**Audiences** : Alex (formateur/développeur), Carine C. (commanditaire IGPDE, non technique).

**Contraintes non négociables** :
- Python 3.12 + python-pptx + lxml (pas de Docker, pas de CI)
- Template IGPDE rescalé 13,33" x 7,5" avec grille DSFR figée
- Police Marianne (fallback Arial)
- Accessibilité : ordre de lecture, `lang=fr-FR`, alt text, métadonnées
- macOS : quarantine Gatekeeper à retirer sur le PPTX généré
- Pas de modification directe du PPTX — tout passe par les scripts Python : les 138 slides sont générées, aucune n'est retouchée dans PowerPoint

---

## C1 — Contexte

```text
+------------------+                    +------------------+
|   Alex           |                    |  Carine C.       |
|  (formateur /    |                    |  (commanditaire  |
|   développeur)   |                    |   IGPDE)         |
+--------+---------+                    +--------+---------+
         |                                       |
         | édite les scripts Python               | reçoit le pack livrable
         | lance make deck                        | valide côté IGPDE
         | valide le rendu, anime                 |
         |                                       |
         v                                       v
+--------+---------------------------------------+--------+
|                                                         |
|   Pipeline de génération des slides PPTX DSFR           |
|   (138 modules Python -> 1 PPTX accessible)             |
|                                                         |
+---+---------------------+-------------------+-----------+
    |                     |                   |
    v                     v                   v
+---+------+     +--------+------+    +-------+--------+
| python-  |     | Template      |    | PowerPoint     |
| pptx     |     | IGPDE-DSFR    |    | (vérification  |
| (biblio- |     | (.pptx base)  |    |  manuelle)     |
| theque)  |     +---------------+    +----------------+
+----------+
```

Le formateur Alex édite les modules Python, lance la génération et anime la formation avec le deck. Le deck est remis à l'IGPDE (Carine C., commanditaire) dans le pack livrable. PowerPoint sert aussi de vérification manuelle (débordements, rendu visuel) car le pipeline ne couvre pas le rendu pixel.

---

## C2 — Containers

```text
+----------------------------------------------------------------------+
|  Pipeline de génération des slides                                   |
|                                                                      |
|  +------------------+     +-------------------+                      |
|  | build_template   |     | assemble.py       |                      |
|  | .py              |     | (orchestrateur)   |                      |
|  |                  |     |                   |                      |
|  | PPT IGPDE 10"    +---->| discover_slides() |                      |
|  | -> PPT DSFR      |     | filter / sort     |                      |
|  |    13,33"x7,5"   |     | boucle build()    |                      |
|  +------------------+     | finalize_pptx()   |                      |
|                           +---+--------+------+                      |
|                               |        |                             |
|              +----------------+        +----------------+            |
|              v                                          v            |
|  +-----------+-------------+   +------------------------+---------+  |
|  | scripts/slides/         |   | igpde_dsfr_components.py        |  |
|  | NN_*.py (138 modules)   |   | (bibliothèque DSFR)             |  |
|  |                         |   |                                 |  |
|  | Chacun expose :         |   | create_presentation()           |  |
|  |   build(prs,layouts,ctx)|   | new_slide()                     |  |
|  |                         |   | 17 composants (add_*)           |  |
|  | Contenu pédagogique +   |   | Stack, _safe_top, _estimate_h   |  |
|  | appels aux composants   |   | finalize_pptx() (a11y)          |  |
|  +-------------------------+   +---------------------------------+  |
|                                                                      |
+----------------------------------------------------------------------+

+---------------------------+     +------------------------------+
| PPT-IGPDE-DSFR-base-      |     | support-formation-102846-    |
| intervenant.pptx          |     | 2026-IGPDE.pptx              |
| (template avec layouts    |     | (artefact final, 138 slides) |
|  et master)               |     +------------------------------+
+---------------------------+
```

| Container | Technologie | Responsabilite | Donnees |
|-----------|-------------|----------------|---------|
| `assemble.py` | Python 3 | Orchestre la decouverte, le tri, le chargement et l'execution sequentielle des modules de slides. Produit le PPTX final | Lit les modules `NN_*.py`, ecrit le `.pptx` |
| `scripts/slides/NN_*.py` (138 fichiers) | Python 3 | Chaque module definit le contenu d'une ou plusieurs slides. Expose `build(prs, layouts, ctx)` | Importe les composants depuis `igpde_dsfr_components` |
| `igpde_dsfr_components.py` | Python 3 + python-pptx + lxml | Bibliotheque de composants DSFR : grille, palette, 17 composants `add_*` et 2 `compose_*`, post-traitement a11y | Charge le template PPTX, manipule le XML OOXML |
| `build_template.py` | Python 3 + python-pptx | Premiere generation du template DSFR 13,33"x7,5" a partir du source IGPDE 10"x5,62" (rescaling + DSFRisation). Historique : ce source n'est plus dans le depot | Lisait `PPT-IGPDE-base-intervenant.pptx` (absent) |
| `rebuild_template_from_demo.py` | Python 3 + python-pptx | Voie actuelle pour reconstruire le template s'il manque (voir `AGENTS.md`) | Lit `_source/presentations-source/gabarits-ppt-igpde.pptx`, ecrit `PPT-IGPDE-DSFR-base-intervenant.pptx` |
| Template PPTX | OOXML | 6 layouts natifs IGPDE : couverture, titre_soustitre, sommaire, chapitre, 3_colonnes, titre_contenu | Fichier binaire PPTX |
| Artefact final | PPTX | Deck complet, copié dans le pack livrable par `make deck` à chaque génération complète (copie refusée si le deck est partiel, sautée si le contenu est identique) | 138 slides, ~3,4 Mo |

---

## C3 — Composants de `igpde_dsfr_components.py`

Le container central mérite un zoom car il porte toute la logique de composition et d'accessibilité.

```text
+-----------------------------------------------------------------------+
| igpde_dsfr_components.py                                              |
|                                                                       |
|  CONFIGURATION                                                        |
|  +------------------+  +-------------------+  +--------------------+  |
|  | Palette DSFR     |  | Grille IGPDE      |  | Layouts (6 index)  |  |
|  | (14 couleurs)    |  | MARGIN_L, COL_W,  |  | LAYOUT_COUVERTURE  |  |
|  | BLEU_FRANCE,     |  | TOP_CONTENT,      |  | LAYOUT_TITRE_...   |  |
|  | ROUGE_MARIANNE...|  | BOTTOM_CONTENT... |  | etc.               |  |
|  +------------------+  +-------------------+  +--------------------+  |
|                                                                       |
|  CYCLE DE VIE                                                         |
|  +-------------------+  +------------------+  +--------------------+  |
|  | create_           |  | new_slide()      |  | finalize_pptx()   |  |
|  | presentation()    |  | titre, footer,   |  | _reorder_shapes() |  |
|  | charge template   |  | fil d'ariane,    |  | _set_lang_on_runs |  |
|  | retourne (prs,    |  | accent couleur,  |  | _mark_decoratives |  |
|  |  layouts)         |  | page_num         |  | core properties   |  |
|  +-------------------+  +------------------+  | xattr quarantine  |  |
|                                               +--------------------+  |
|                                                                       |
|  COMPOSANTS (extrait ; liste complete dans le tableau ci-dessous)     |
|  +-------------+ +-------------+ +-----------+ +------------------+   |
|  | add_callout | | add_alert   | | add_high- | | add_quote        |   |
|  | (info box)  | | (warn/err/  | | light     | | (citation)       |   |
|  |             | |  success)   | | (emphase) | |                  |   |
|  +-------------+ +-------------+ +-----------+ +------------------+   |
|  +-------------+ +-------------+ +-----------+ +------------------+   |
|  | add_card    | | add_pave_   | | add_      | | add_tableau      |   |
|  | (carte)     | | chiffre     | | stepper   | | (table donnees)  |   |
|  |             | | (KPI)       | | (etapes)  | |                  |   |
|  +-------------+ +-------------+ +-----------+ +------------------+   |
|  +-------------+ +-------------+ +-----------+ +------------------+   |
|  | add_texte_  | | add_image   | | add_      | | add_encadre      |   |
|  | libre       | |             | | fleche    | | (fond colore)    |   |
|  +-------------+ +-------------+ +-----------+ +------------------+   |
|  +-------------+ +-------------+                                      |
|  | compose_    | | compose_    |                                      |
|  | sommaire    | | chapitre    |                                      |
|  +-------------+ +-------------+                                      |
|                                                                       |
|  POSITIONNEMENT                                                       |
|  +-------------------+  +------------------+  +--------------------+  |
|  | Stack (curseur     |  | _safe_top()      |  | _estimate_height  |  |
|  |  vertical)         |  | (anti-debord.    |  | estimate_callout_ |  |
|  | push(h) -> top     |  |  bas de slide)   |  | estimate_highlight|  |
|  +-------------------+  +------------------+  | estimate_quote_   |  |
|                                               | estimate_card_    |  |
|                                               +--------------------+  |
|                                                                       |
|  UTILITAIRES INTERNES                                                 |
|  +-------------------+  +------------------+  +--------------------+  |
|  | detect_font()     |  | _apply_text()    |  | _add_bullets()    |  |
|  | Marianne / Arial  |  | (run unique)     |  | (liste a puces)   |  |
|  +-------------------+  +------------------+  +--------------------+  |
|  +-------------------+                                                |
|  | _plain_text()     |                                                |
|  | (segments riches) |                                                |
|  +-------------------+                                                |
+-----------------------------------------------------------------------+
```

Pour trouver un composant dans le code : `grep -n "^def nom" scripts/igpde_dsfr_components.py` (les numéros de ligne changent à chaque modification, ils ne sont donc pas notés ici).

| Composant | Interface | Responsabilite |
|-----------|-----------|----------------|
| `create_presentation()` | `() -> (prs, layouts)` | Charge le template PPTX, construit le dict des 6 layouts |
| `new_slide()` | `(prs, layouts, layout_name, titre, ...) -> slide` | Crée une slide avec layout, titre, footer, fil d'ariane, accent couleur |
| `Stack` | `.push(h) -> top` | Curseur vertical qui empile les composants avec gap constant (évite le calcul manuel des `top`) |
| `_safe_top()` | `(top, height) -> top` | Garde-fou : remonte le composant si `top+height > BOTTOM_CONTENT` |
| `_estimate_height()` | `(content, width, ...) -> float` | Estime la hauteur en pouces d'un texte pour le positionnement |
| `add_callout` | `(slide, titre, bullets, top, ...) -> shape` | Boite d'information bleue DSFR avec titre + bullets |
| `add_alert` | `(slide, titre, bullets, top, severity, ...) -> shape` | Alerte DSFR (warning / error / success / info) |
| `add_highlight` | `(slide, texte, top, ...) -> shape` | Bandeau d'emphase avec accent bleu |
| `add_quote` | `(slide, texte, auteur, ...) -> shape` | Citation avec guillemets et attribution |
| `add_card` | `(slide, titre, contenu, top, left, ...) -> shape` | Carte DSFR avec numero, titre et contenu |
| `add_pave_chiffre` | `(slide, valeur, label, ...) -> shape` | Pave KPI (chiffre + label) |
| `add_stepper` | `(slide, etapes, top, ...) -> shape` | Processus sequentiel DSFR (pastilles numerotees) |
| `add_tableau` | `(slide, headers, rows, ...) -> float` | Tableau DSFR. Retourne la hauteur pour empilement |
| `add_image` | `(slide, path, top, left, ...) -> shape` | Image avec alt text obligatoire |
| `add_texte_libre` | `(slide, texte, top, ...) -> shape` | Texte positionne sans composant DSFR |
| `add_qrcode` | `(slide, image_path, url, top, left, ...) -> shape` | QR code imprime avec alternative visible : appel a l'action et URL lisible |
| `add_checklist` | `(slide, items, top, ...) -> shape` | Liste a cocher DSFR (case Unicode et texte) |
| `add_avant_apres` | `(slide, avant_titre, avant_bullets, apres_titre, apres_bullets, ...) -> shape` | Comparaison avant/apres en 2 colonnes |
| `add_exemple_contre_exemple` | `(slide, bon_titre, bon_bullets, mauvais_titre, mauvais_bullets, ...) -> shape` | Bon exemple et contre-exemple en 2 colonnes |
| `add_notes` | `(slide, texte, lang="fr-FR") -> None` | Notes presentateur (invisibles en projection) |
| `add_encadre` | `(slide, ...) -> shape` | Encadre fond colore parametrable |
| `add_fleche` | `(slide, top, left, ...) -> shape` | Fleche decorative entre elements |
| `compose_sommaire` | `(slide, titre, parties) -> None` | Compose un sommaire avec cards numerotees |
| `compose_chapitre` | `(slide, numero, titre) -> None` | Compose une slide de chapitre avec bandeau bleu |
| `finalize_pptx` | `(prs, output, ...) -> path` | Post-traitement a11y complet : ordre de lecture, langue, décoratifs, métadonnées, quarantine macOS |

---

## Flux dynamique — Generation du deck

```text
1. Alex lance : make deck (scripts/assemble.py)
                      |
2. assemble.py        | appelle create_presentation()
                      | -> charge PPT-IGPDE-DSFR-base-intervenant.pptx
                      | -> retourne (prs, layouts)
                      |
3.                    | appelle discover_slides()
                      | -> scanne scripts/slides/, filtre NN_*.py, trie par nom
                      | -> retourne [Path x 138]
                      |
4. Pour chaque module (page_num = 1..N) :
   |
   |  4a. load_slide_module(path)
   |      -> importlib.util charge le .py, verifie build()
   |
   |  4b. module.build(prs, layouts, ctx)
   |      |
   |      |  Le module :
   |      |  - appelle new_slide() avec layout + titre + footer
   |      |  - cree un Stack(top=X, gap=Y)
   |      |  - estime les hauteurs (estimate_*_height)
   |      |  - empile les composants (add_callout, add_highlight, ...)
   |      |  - ajoute les notes presentateur (add_notes)
   |      |
   |  4c. print "[NN] fichier.py"
   |
5. assemble.py        | appelle finalize_pptx(prs, output, ...)
                      |   -> _mark_decoratives() sur chaque slide
                      |   -> _set_lang_on_runs() fr-FR sur chaque run
                      |   -> _reorder_shapes() titre > contenu > footer > decos
                      |   -> core_properties (title, author, subject, lang)
                      |   -> prs.save(output)
                      |   -> xattr -d com.apple.quarantine (macOS)
                      |
6.                    | print "[OK] support-formation-102846-2026-IGPDE.pptx"
```

---

## Usine autonome — containers ajoutés le 2026-09-27

Depuis l'extraction en dépôt autonome, la chaîne de génération décrite ci-dessus est pilotée par des containers d'orchestration et de preuve qui ne dépendent plus d'aucun espace de travail extérieur.

- **`Makefile`** (make) : point d'entrée unique pour un humain ou un agent. Choisit l'interpréteur (`.venv`, sinon Python 3.12 Homebrew) et enchaîne deck, contrôle qualité, tests, validation du site, PDF, pack et publication.
- **`scripts/fabriquer_pack.py`** (Python 3) : lit `config.yml`, copie le deck généré dans le pack, régénère les PDF accessibles par le générateur embarqué, récupère et vérifie par SHA-256 les installeurs listés dans `livrables-IGPDE-2026-102846/outils/outils.json`.
- **`vendor/accessible-pdf/`** (Python 3, Pandoc, WeasyPrint, pikepdf) : générateur Markdown vers PDF/UA-1, copié du skill d'origine avec ses gabarits CSS.
- **`recette/`** (bash, Node, ShipGuard) : recette visuelle du site corrigé à partir des manifestes `recette/visual-tests/`, prévisualisation locale ; le site servi reste `docs/`.
- **`.githooks/pre-commit`** (bash 3.2) : contrôles bloquants du dépôt, indépendants de l'agent qui commite.

Relations : `Makefile` appelle `assemble.py`, `qa_pptx.py`, `pytest`, `validate.py`, `fabriquer_pack.py` et les scripts de `recette/` ; `fabriquer_pack.py` appelle `vendor/accessible-pdf/scripts/md2pdf.py` ; `git commit` déclenche `.githooks/pre-commit`.

## Limites à dire en présentation

- **Pas de rendu pixel** : le pipeline génère du XML OOXML, pas un rendu visuel. Les débordements fins ne sont détectables que dans PowerPoint (passe manuelle obligatoire).
- **`_estimate_height` est heuristique** : l'estimation de hauteur repose sur un calcul approximatif (caractères par pouce), pas sur un moteur de rendu texte. Les cas limites (texte long, polices variables) peuvent déborder.
- **`_safe_top` est un garde-fou de dernier recours** : il remonte un composant pour éviter de sortir de la zone utile, mais peut créer un chevauchement avec le composant précédent si le `top` initial était déjà trop bas.
- **Aucune retouche dans PowerPoint** : les 138 slides sont générées par script ; une retouche faite dans PowerPoint serait écrasée à la régénération suivante. Toute correction passe par `scripts/slides/`.
- **Pas de CI/CD** : la génération est locale, sur le poste d'Alex. Pas de pipeline de build automatisé.
- **74 tests pytest** : la bibliothèque de composants, les contrats a11y, la géométrie deck, la boucle QA du deck (`make qa`) et la copie du deck dans le pack (`tests/test_fabriquer_pack.py`) sont couverts par pytest. La validation repose aussi sur `validate.py` (site easy checks) et la passe visuelle manuelle.

---

## Checklist de conformité C4

- [x] Système en scope et systèmes externes distingués
- [x] Personnes/roles visibles en C1
- [x] Containers C2 sont des applications ou data stores en runtime
- [x] Chaque element a type, responsabilite et technologie
- [x] Chaque relation est orientee et labellisee
- [x] Contraintes et hypothèses documentées avant les recommandations
- [x] C3 present uniquement pour le container critique (igpde_dsfr_components.py)
- [x] Sources locales lues citees
- [x] Chaque vue a un titre lisible indiquant son niveau
