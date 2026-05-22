# Formation 102638 (IGPDE / Carinne C.) - protocole Codex

Ce fichier adapte `CLAUDE.md` pour Codex. Les consignes globales Codex restent applicables.

## Contexte

- Formation accessibilité numérique, 1 jour, public communicants, pas développeurs
- 138 slides PPTX DSFR, 4 modules : Introduction communication accessible et cadre légal > Word accessible > points de contrôle rapides W3C > Réseaux sociaux
- Ordre impératif M1 > M2 > M3 > M4, jamais inverser
- Exercice Sami : 21 critères à vérifier dans 3 DOCX, spec dans `_source/exercice-sami-spec.md`
- Site d'exercice points de contrôle rapides dans `docs/`, avec versions `site-inaccessible/`, `site-aide-correction/`, `site-accessible/` et grille XLSX téléchargeable
- Site publié sur GitHub Pages via dépôt standalone `easy-check-igpde` : https://alexmacapple.github.io/easy-check-igpde/
- Dernier état livré : deck `formation-102638-juin-2026.pptx` à 138 slides (2026-05-17)
- Deck WCAG condensé : `wcag/WCAG en langage clair - condensé.pptx` (13 slides), généré par `scripts/generate_wcag_langage_clair.py --condensed`

## Pipeline

- **Toujours modifier les scripts Python, jamais le PPTX directement** : éditer `scripts/slides/NN_*.py` puis régénérer avec `python3 scripts/assemble.py`
- Pattern de nommage : `NN_nom.py` ou `NNxx_nom.py` (suffixe multi-lettres accepté, ex. `02ma_`, `02rb_`)
- Chaque module expose `build(prs, layouts, ctx)` avec `ctx.page_num`, `ctx.date`, `ctx.footer_base`
- Régénérer avec `python3 scripts/assemble.py`
- Tester une slide avec `python3 scripts/assemble.py --only NN`
- Réexporter le deck complet : suivre `REEXPORTER-DECK-PPTX.md` avant livraison
- Régénérer les DOCX Sami avec `python3 scripts/generate_exercice_sami.py`
- Valider le site d'exercice avec `python3 validate.py`
- `finalize_pptx()` est obligatoire avant livraison, via les scripts du projet

## Règles validées manuellement

- Les decks PPTX ont deux régimes : les slides générées par script et les slides figées ou retouchées manuellement dans PowerPoint. Avant toute régénération, identifier le régime des slides concernées afin de ne pas écraser des corrections manuelles.
- Un skill destiné à être publié doit être auto-suffisant : `SKILL.md`, références, scripts, templates et modules nécessaires doivent être inclus dans le dépôt ou explicitement documentés. Avant publication, vérifier les imports, chemins relatifs et dépendances externes.
- Chaque skill publié ou stabilisé doit avoir une fiche opérationnelle dans le wiki : objectif, cas d'usage, commande ou déclencheur, fichiers clés, limites connues et exemples d'utilisation.
- La version accessible du site d'exercice doit rester sobre, comme un vrai site corrigé, sans pédagogie visible.
- Les erreurs de formulaire ne doivent apparaître qu'après une tentative de soumission ou après interaction avec le champ concerné.
- Les documents accessibles doivent déclarer des métadonnées cohérentes avec leur langue réelle, notamment `fr` pour les documents en français. Les versions volontairement inaccessibles peuvent conserver des défauts pédagogiques explicites.
- Exercice pédagogique : ne pas distribuer la checklist au moment de l'identification. Les stagiaires doivent d'abord diagnostiquer sans filet ; la checklist sert ensuite à consolider, pas à court-circuiter le jugement.

## Compétences à utiliser

Pour une nouvelle slide ou une restructuration pédagogique :

1. `pedagogie-neuro`
2. `composition-dsfr-pptx`
3. `accessible-pptx`

Pour transformer un corpus en présentation avant composition :

1. `pedagogie-neuro`
2. `slides-pedagogiques`
3. `composition-dsfr-pptx`
4. `accessible-pptx`

Si les skills ne sont pas automatiquement injectés dans la session, lire leurs aliases dans `~/.codex/skills/<nom>/SKILL.md`. Ces aliases pointent vers les sources Claude dans `/Users/alex/Claude/.claude/skills`.

## Playbooks

- Nouvelle slide : créer `scripts/slides/NN_nom.py`, suffixe lettre(s) pour intercaler (`05a_`, `02ma_`)
- Réexport deck stable : lire `REEXPORTER-DECK-PPTX.md`, puis lancer `python3 scripts/qa_pptx.py . --max-iterations 5 --clean` avant `python3 scripts/assemble.py`
- Tests unitaires : `python3 -m pytest tests/ -v` (suite complète helpers + composants + a11y + QA deck)
- Tests géométrie : `python3 scripts/assemble.py --qa-map -o .qa/formation-test-qa.pptx && QA_PPTX_PATH=.qa/formation-test-qa.pptx python3 -m pytest tests/test_deck_geometry.py -v`
- Boucle QA PPTX PRD-119 : `python3 scripts/qa_pptx.py . --max-iterations 5 --clean`
- Correcteur accents QA : utiliser `python3 scripts/qa_pptx.py . --max-iterations 5 --apply-accents` seulement si les patchs d'accents sûrs doivent être appliqués
- Verdict QA PPTX : lire `.qa/qa-pptx-report.md` et le champ `status`; ne pas interpréter le seul exit code comme une preuve de convergence
- Sorties QA PPTX : garder les fichiers sous `.qa/` ; les chemins de sortie hors projet ne sont pas supportés en v1
- Tester : `python3 scripts/assemble.py --only NN`
- Template absent : `python3 scripts/build_template.py`
- Prévisualiser le site des points de contrôle rapides : depuis `docs/`, lancer `python3 -m http.server 8765 --bind 127.0.0.1`, puis ouvrir `http://127.0.0.1:8765/index.html`
- Alternative fichier direct : ouvrir `file:///Users/alex/Claude/projets-formations/IGPDE-Carinne-C/docs/index.html`, mais préférer le serveur local si les composants DSFR interactifs ne réagissent pas
- Arrêter le serveur local : revenir dans le terminal qui exécute `http.server` et faire `Ctrl+C`
- Quarantine macOS : `xattr -d com.apple.quarantine formation-102638-juin-2026.pptx`
- Controle tirets dans les scripts : `grep -rn $'—\|–' scripts/` doit retourner vide
- Controle PPTX : `unzip -t formation-102638-juin-2026.pptx`
- Warnings footer : diagnostiquer par slide, corriger le positionnement source, puis régénérer le deck complet
- Publier le site : `rsync -a --delete --exclude='.DS_Store' --exclude='*.md' --exclude='.git' docs/ /tmp/easy-check-igpde/ && cd /tmp/easy-check-igpde && git add -A && git commit -m "Mise à jour du site" && git push`

## Grille IGPDE-DSFR

| Constante | Valeur |
|-----------|--------|
| `MARGIN_L` | 0,52" |
| `CONTENT_W` | 12,28" |
| `COL_W` / `COL_R` | 5,98" / 6,83" |
| `TOP` contenu | 2,68" |
| `BOTTOM_CONTENT` | 6,80" |
| `FOOTER_Y` | 6,98" |

Layouts : `couverture`, `titre_soustitre`, `titre_contenu`, `chapitre`, `sommaire`, `3_colonnes`.

Composants : `add_callout`, `add_alert`, `add_highlight`, `add_quote`, `add_card`, `add_pave_chiffre`, `add_stepper`, `add_tableau`, `add_image`, `add_texte_libre`, `add_notes`, `add_encadre`, `add_fleche`, `compose_sommaire`, `compose_chapitre`.

## À ne pas faire

- Ne jamais écrire du français sans accents (é, è, ê, à, ç, ô, etc.) — dans les slides, les scripts, les docs et lessons.md. Vérifier : `grep -rn 'debordement\|Regle\b\|Symptome\b\|echec\b' lessons.md scripts/`
- Ne jamais hardcoder `page_num` — toujours `ctx.page_num`
- Ne jamais utiliser `slide.shapes.add_textbox()` directement — utiliser `add_texte_libre`
- Ne jamais introduire de tiret cadratin ni demi-cadratin dans les scripts — tiret simple `-`
- Ne jamais modifier la ligne séparatrice IGPDE à `y=6,98"` ni la disposition des logos
- Ne jamais mettre de jargon développeur dans le contenu des slides : ARIA, DOM, CSS
- Ne jamais livrer sans régénération et `finalize_pptx()`
- Ne pas utiliser le mot « pilier » dans les slides — remplacer par « thème »

## Modes d'échec connus

- `add_alert` ou `add_callout` avec une string au lieu d'une liste : itère sur chaque caractère
- Changement typographique global sans recalibrer `_estimate_height` : risque de débordement massif
- `add_image` sans `height=` près d'un autre composant : risque de débordement
- Estimation additive texte + image : ne pas supposer que `_estimate_height(text) + image_height` garantit l'absence de chevauchement ; vérifier le rendu et contraindre les hauteurs
- `layout_name="titre_soustitre"` sur une slide de contenu : logos institutionnels affichés par erreur
- `accent_w` différent de `0,08"` sauf chapitre `0,16"` : défaut d'alignement visible
- Placeholder Title : copier les 4 dimensions `(top, left, width, height)` sinon `left` et `width` tombent à 0
- Quiz : questions et réponses doivent être séparées, souvent avec suffixe `b`
- `Stack` / `_safe_top` : `_safe_top` évite le débordement bas en remontant le composant, mais peut créer un chevauchement avec le bloc précédent si le `top` initial est trop optimiste
- Warning footer : ne jamais le traiter comme un simple bruit console. Vérifier l'écart avec le bloc précédent, resserrer ou recomposer la slide, puis viser `TOTAL_WARNINGS 0`

## Références

- `contraintes.md` pour les dépendances, limitations et features existantes.

| Ressource | Fichier |
|-----------|---------|
| Architecture C4 slides | `architecture-c4-slides.md` |
| Spec exercice Sami | `_source/exercice-sami-spec.md` |
| Diff des critères Sami | `_source/exercice-sami-diff.md` |
| Leçons techniques | `lessons.md` |
| Points de contrôle rapides W3C | `03-easy-checks/w3c-easy-checks-fr.md` |
| Guide accessibiliser sa communication | `_source/references/Guide-2026-Accessibiliser-sa-communication-police-14-coul.md` |
| Notes réseaux sociaux | `04-reseaux-sociaux/md-reseaux-sociaux.md` |
| Notes FALC | `05-falc/md-falc.md` |
| Notes médias | `06-medias/md-medias.md` |
| Passation dernière session | `_source/passation-session-2026-05-03.md` |
| Publication site | `docs-publication.md` |
| Dépôt site standalone | `git@github.com:Alexmacapple/easy-check-igpde.git` |
| URL publique site | https://alexmacapple.github.io/easy-check-igpde/ |
| Dépendances | Python 3 + `python-pptx` + `lxml` + `openpyxl` + Marianne, fallback Arial |
