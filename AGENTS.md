# Formation 102638 (IGPDE / Carinne C.) - protocole Codex

Ce fichier adapte `CLAUDE.md` pour Codex. Les consignes globales Codex restent applicables.

## Contexte

- Formation accessibilité numérique, 1 jour, public communicants, pas développeurs
- 112 slides PPTX DSFR, 4 modules : Introduction communication accessible et cadre légal > Word accessible > points de contrôle rapides W3C > Réseaux sociaux
- Ordre impératif M1 > M2 > M3 > M4, jamais inverser
- Exercice Sami : 21 critères à vérifier dans 3 DOCX, spec dans `_source/exercice-sami-spec.md`
- Site d'exercice points de contrôle rapides dans `docs/`, avec versions `site-inaccessible/`, `site-aide-correction/`, `site-accessible/` et grille XLSX téléchargeable
- Dernier état livré : deck `formation-102638-juin-2026.pptx` à 112 slides (2026-05-12)
- Deck WCAG condensé : `WCAG en langage clair - condensé.pptx` (13 slides), généré par `scripts/generate_wcag_langage_clair.py --condensed`

## Pipeline

- **Toujours modifier les scripts Python, jamais le PPTX directement** : editer `scripts/slides/NN_*.py` puis regenerer avec `python3 scripts/assemble.py`
- Pattern de nommage : `NN_nom.py` ou `NNxx_nom.py` (suffixe multi-lettres accepte, ex. `02ma_`, `02rb_`)
- Chaque module expose `build(prs, layouts, ctx)` avec `ctx.page_num`, `ctx.date`, `ctx.footer_base`
- Regenerer avec `python3 scripts/assemble.py`
- Tester une slide avec `python3 scripts/assemble.py --only NN`
- Regenerer les DOCX Sami avec `python3 scripts/generate_exercice_sami.py`
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

## Competences a utiliser

Pour une nouvelle slide ou une restructuration pedagogique :

1. `pedagogie-neuro`
2. `composition-dsfr-pptx`
3. `accessible-pptx`

Pour transformer un corpus en presentation avant composition :

1. `pedagogie-neuro`
2. `slides-pedagogiques`
3. `composition-dsfr-pptx`
4. `accessible-pptx`

Si les skills ne sont pas automatiquement injectes dans la session, lire leurs aliases dans `~/.codex/skills/<nom>/SKILL.md`. Ces aliases pointent vers les sources Claude dans `/Users/alex/Claude/.claude/skills`.

## Playbooks

- Nouvelle slide : creer `scripts/slides/NN_nom.py`, suffixe lettre(s) pour intercaler (`05a_`, `02ma_`)
- Tester : `python3 scripts/assemble.py --only NN`
- Template absent : `python3 scripts/build_template.py`
- Previsualiser le site des points de contrôle rapides : depuis `docs/`, lancer `python3 -m http.server 8765 --bind 127.0.0.1`, puis ouvrir `http://127.0.0.1:8765/index.html`
- Alternative fichier direct : ouvrir `file:///Users/alex/Claude/projets-formations/IGPDE-Carinne-C/docs/index.html`, mais preferer le serveur local si les composants DSFR interactifs ne reagissent pas
- Arreter le serveur local : revenir dans le terminal qui execute `http.server` et faire `Ctrl+C`
- Quarantine macOS : `xattr -d com.apple.quarantine formation-102638-juin-2026.pptx`
- Controle tirets dans les scripts : `grep -rn $'—\|–' scripts/` doit retourner vide
- Controle PPTX : `unzip -t formation-102638-juin-2026.pptx`
- Warnings footer : diagnostiquer par slide, corriger le positionnement source, puis regenerer le deck complet

## Grille IGPDE-DSFR

| Constante | Valeur |
|-----------|--------|
| `MARGIN_L` | 0,52" |
| `CONTENT_W` | 12,28" |
| `COL_W` / `COL_R` | 5,98" / 6,83" |
| `TOP` contenu | 2,30" |
| `BOTTOM_CONTENT` | 6,80" |
| `FOOTER_Y` | 6,98" |

Layouts : `couverture`, `titre_soustitre`, `titre_contenu`, `chapitre`, `sommaire`, `3_colonnes`.

Composants : `add_callout`, `add_alert`, `add_highlight`, `add_quote`, `add_card`, `add_pave_chiffre`, `add_stepper`, `add_tableau`, `add_image`, `add_texte_libre`, `add_notes`, `add_encadre`, `add_fleche`, `compose_sommaire`, `compose_chapitre`.

## A ne pas faire

- Ne jamais hardcoder `page_num` - toujours `ctx.page_num`
- Ne jamais utiliser `slide.shapes.add_textbox()` directement - utiliser `add_texte_libre`
- Ne jamais introduire de tiret cadratin ni demi-cadratin dans les scripts - tiret simple `-`
- Ne jamais modifier la ligne separatrice IGPDE a `y=6,98"` ni la disposition des logos
- Ne jamais mettre de jargon developpeur dans le contenu des slides : ARIA, DOM, CSS
- Ne jamais livrer sans regeneration et `finalize_pptx()`
- Ne pas utiliser le mot "pilier" dans les slides - remplacer par "theme"

## Modes d'echec connus

- `add_alert` ou `add_callout` avec une string au lieu d'une liste : itere sur chaque caractere
- Changement typographique global sans recalibrer `_estimate_height` : risque de debordement massif
- `add_image` sans `height=` pres d'un autre composant : risque de debordement
- Estimation additive texte + image : ne pas supposer que `_estimate_height(text) + image_height` garantit l'absence de chevauchement ; verifier le rendu et contraindre les hauteurs
- `layout_name="titre_soustitre"` sur une slide de contenu : logos institutionnels affiches par erreur
- `accent_w` different de `0,08"` sauf chapitre `0,16"` : defaut d'alignement visible
- Placeholder Title : copier les 4 dimensions `(top, left, width, height)` sinon `left` et `width` tombent a 0
- Quiz : questions et reponses doivent etre separees, souvent avec suffixe `b`
- `Stack` / `_safe_top` : `_safe_top` evite le debordement bas en remontant le composant, mais peut creer un chevauchement avec le bloc precedent si le `top` initial est trop optimiste
- Warning footer : ne jamais le traiter comme un simple bruit console. Verifier l'ecart avec le bloc precedent, resserrer ou recomposer la slide, puis viser `TOTAL_WARNINGS 0`

## References

- `contraintes.md` pour les dependances, limitations et features existantes.

| Ressource | Fichier |
|-----------|---------|
| Spec exercice Sami | `_source/exercice-sami-spec.md` |
| Diff des criteres Sami | `_source/exercice-sami-diff.md` |
| Lecons techniques | `lessons.md` |
| points de contrôle rapides W3C | `03-easy-checks/w3c-easy-checks-fr.md` |
| Guide accessibiliser sa communication | `_source/references/Guide-2026-Accessibiliser-sa-communication-police-14-coul.md` |
| Notes reseaux sociaux | `04-reseaux-sociaux/md-reseaux-sociaux.md` |
| Notes FALC | `05-falc/md-falc.md` |
| Notes medias | `06-medias/md-medias.md` |
| Passation derniere session | `_source/passation-session-2026-05-03.md` |
| Dependances | Python 3 + `python-pptx` + `lxml` + `openpyxl` + Marianne, fallback Arial |
