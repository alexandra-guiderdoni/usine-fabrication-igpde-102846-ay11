# Formation 102638 (IGPDE / Carinne C.) — protocole agent

Hérite de `~/.claude/CLAUDE.md` et `~/Claude/CLAUDE.md`. Ne pas dupliquer les règles parentes.

## Contexte

- Formation accessibilité numérique, 1 jour, public communicants (pas développeurs)
- 90 slides PPTX DSFR, 4 modules : Introduction > Word accessible > Easy Checks W3C > Réseaux sociaux
- Ordre impératif M1 > M2 > M3 > M4, jamais inverser
- Exercice Sami : 21 erreurs dans 2 DOCX (inaccessible/accessible), spec dans `_source/exercice-sami-spec.md`

## Comment je travaille

- Éditer `scripts/slides/NN_*.py`, jamais le PPTX livré directement
- Chaque module expose `build(prs, layouts, ctx)` avec `ctx.page_num`, `ctx.date`, `ctx.footer_base`
- `python3 scripts/assemble.py` pour régénérer, `--only NN` pour tester en isolation
- `python3 scripts/generate_exercice_sami.py` pour régénérer les DOCX
- `finalize_pptx()` obligatoire avant livraison (a11y + quarantine macOS)
- Avant toute nouvelle slide : `/pedagogie-neuro` puis `/composition-dsfr-pptx` puis `/accessible-pptx`

## Playbooks

- **Nouvelle slide** : créer `scripts/slides/NN_nom.py`, suffixe lettre pour intercaler (`05a_`)
- **Tester** : `python3 scripts/assemble.py --only NN`
- **Template absent** : `python3 scripts/build_template.py`
- **Quarantine** : `xattr -d com.apple.quarantine formation-102638-juin-2026.pptx`
- **Contrôle tirets** : `grep -rn $'—\|–' scripts/` doit retourner vide

**Grille IGPDE-DSFR (13,33" x 7,5")** :

| Constante | Valeur |
|-----------|--------|
| `MARGIN_L` | 0,52" |
| `CONTENT_W` | 12,28" |
| `COL_W` / `COL_R` | 5,98" / 6,83" |
| `TOP` contenu | 2,30" |
| `BOTTOM_CONTENT` | 6,80" |
| `FOOTER_Y` | 6,98" |

**Layouts** : `couverture`, `titre_soustitre` (logos), `titre_contenu` (standard), `chapitre`, `sommaire`, `3_colonnes`

**Composants** : `add_callout`, `add_alert`, `add_highlight`, `add_quote`, `add_card`, `add_pave_chiffre`, `add_stepper`, `add_tableau`, `add_image`, `add_texte_libre`, `add_notes`, `add_encadre`, `add_fleche`, `compose_sommaire`, `compose_chapitre`

## À ne pas faire

- Jamais hardcoder `page_num` — toujours `ctx.page_num`
- Jamais `slide.shapes.add_textbox()` direct — utiliser `add_texte_libre` (EMU vs pouces)
- Jamais de tiret cadratin ni demi-cadratin dans les scripts — tiret simple `-`
- Jamais modifier la ligne séparatrice IGPDE à y=6,98" ni la disposition des logos
- Jamais de jargon développeur dans le contenu des slides (ARIA, DOM, CSS)
- Jamais livrer sans `finalize_pptx()`
- Pas de mot « pilier » — remplacé par « thème »

## Modes d'échec connus

- `add_alert`/`add_callout` avec une string au lieu d'une liste : itère sur chaque caractère, slide pétée
- Changement typographique global (taille, espacement) sans recalibrer `_estimate_height` : 50+ slides débordent
- `add_image` sans `height=` à côté d'un autre composant : l'image déborde sur le composant suivant
- `layout_name="titre_soustitre"` sur une slide de contenu : affiche les logos institutionnels par erreur
- Accent `accent_w` différent de 0,08" (sauf chapitre 0,16") : perçu comme défaut d'alignement
- Placeholder Title : copier les 4 dimensions `(top, left, width, height)` sinon `left` et `width` tombent à 0
- Quiz : questions + réponses sur la même slide. Toujours séparer (suffixe `b`)
- `Stack` : le `_safe_top` interne remonte les composants quand l'estimation dépasse `BOTTOM_CONTENT`

## Références

| Ressource | Fichier |
|-----------|---------|
| Spec exercice Sami | `_source/exercice-sami-spec.md` |
| Diff 21 erreurs | `_source/exercice-sami-diff.md` |
| Leçons techniques | `lessons.md` |
| Easy Checks W3C | `03-easy-checks/w3c-easy-checks-fr.md` |
| Passation dernière session | `_source/passation-session-2026-05-03.md` |
| Dépendances | Python 3 + `python-pptx` + `lxml` + `openpyxl` + Marianne (fallback Arial) |
