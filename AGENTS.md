# Formation 102638 (IGPDE / Carinne C.) - protocole Codex

Ce fichier adapte `CLAUDE.md` pour Codex. Les consignes globales Codex restent applicables.

## Contexte

- Formation accessibilite numerique, 1 jour, public communicants, pas developpeurs
- 91 slides PPTX DSFR, 4 modules : Introduction > Word accessible > Easy Checks W3C > Reseaux sociaux
- Ordre imperatif M1 > M2 > M3 > M4, jamais inverser
- Exercice Sami : 21 criteres a verifier dans 2 DOCX, spec dans `_source/exercice-sami-spec.md`

## Pipeline

- Editer `scripts/slides/NN_*.py`, jamais le PPTX livre directement
- Chaque module expose `build(prs, layouts, ctx)` avec `ctx.page_num`, `ctx.date`, `ctx.footer_base`
- Regenerer avec `python3 scripts/assemble.py`
- Tester une slide avec `python3 scripts/assemble.py --only NN`
- Regenerer les DOCX Sami avec `python3 scripts/generate_exercice_sami.py`
- `finalize_pptx()` est obligatoire avant livraison, via les scripts du projet

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

- Nouvelle slide : creer `scripts/slides/NN_nom.py`, suffixe lettre pour intercaler (`05a_`)
- Tester : `python3 scripts/assemble.py --only NN`
- Template absent : `python3 scripts/build_template.py`
- Quarantine macOS : `xattr -d com.apple.quarantine formation-102638-juin-2026.pptx`
- Controle tirets dans les scripts : `grep -rn $'—\|–' scripts/` doit retourner vide
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

| Ressource | Fichier |
|-----------|---------|
| Spec exercice Sami | `_source/exercice-sami-spec.md` |
| Diff des criteres Sami | `_source/exercice-sami-diff.md` |
| Lecons techniques | `lessons.md` |
| Easy Checks W3C | `03-easy-checks/w3c-easy-checks-fr.md` |
| Passation derniere session | `_source/passation-session-2026-05-03.md` |
| Dependances | Python 3 + `python-pptx` + `lxml` + `openpyxl` + Marianne, fallback Arial |
