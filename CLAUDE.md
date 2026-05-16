# Formation 102638 (IGPDE / Carinne C.) — protocole agent

Hérite de `~/.claude/CLAUDE.md` et `~/Claude/CLAUDE.md`. Ne pas dupliquer les règles parentes.

## Contexte

- Formation accessibilité numérique, 1 jour, public communicants, pas développeurs
- 131 slides PPTX DSFR, 4 modules : Introduction communication accessible et cadre légal > Word accessible > points de contrôle rapides W3C > Réseaux sociaux
- Ordre impératif M1 > M2 > M3 > M4, jamais inverser
- Exercice Sami : 21 critères à vérifier dans 3 DOCX (inaccessible/aide correction/accessible), spec dans `_source/exercice-sami-spec.md`
- Site d'exercice points de contrôle rapides dans `docs/`, avec versions `site-inaccessible/`, `site-aide-correction/`, `site-accessible/` et grille XLSX téléchargeable
- Site publié sur GitHub Pages via dépôt standalone `easy-check-igpde` : https://alexmacapple.github.io/easy-check-igpde/
- Date, footer et nom du fichier de sortie centralisés dans `config.yml` (source unique)
- Dernier état livré : deck `formation-102638-juin-2026.pptx` à 131 slides (2026-05-16)
- Deck WCAG condensé : `wcag/WCAG en langage clair - condensé.pptx` (13 slides), généré par `scripts/generate_wcag_langage_clair.py --condensed`

## Comment je travaille

- **Toujours modifier les scripts Python, jamais le PPTX directement** : éditer `scripts/slides/NN_*.py` puis régénérer avec `python3 scripts/assemble.py`
- Pattern de nommage : `NN_nom.py` ou `NNxx_nom.py` (suffixe multi-lettres accepté, ex. `02ma_`, `02rb_`)
- Chaque module expose `build(prs, layouts, ctx)` avec `ctx.page_num`, `ctx.date`, `ctx.footer_base`
- `python3 scripts/assemble.py` pour régénérer, `--only NN` pour tester en isolation
- `python3 scripts/generate_exercice_sami.py` pour régénérer les DOCX
- `python3 validate.py` pour valider le site d'exercice et les liens locaux
- `finalize_pptx()` obligatoire avant livraison (a11y + quarantine macOS)
- Avant toute nouvelle slide : `/pedagogie-neuro` puis `/composition-dsfr-pptx` puis `/accessible-pptx`

## Règles validées manuellement

- Les decks PPTX ont deux régimes : les slides générées par script et les slides figées ou retouchées manuellement dans PowerPoint. Avant toute régénération, identifier le régime des slides concernées afin de ne pas écraser des corrections manuelles. **État actuel (2026-05-17) : 100 % des 131 slides sont en régime script. Aucune slide manuelle pour l'instant.**
- Un skill destiné à être publié doit être auto-suffisant : `SKILL.md`, références, scripts, templates et modules nécessaires doivent être inclus dans le dépôt ou explicitement documentés. Avant publication, vérifier les imports, chemins relatifs et dépendances externes.
- Chaque skill publié ou stabilisé doit avoir une fiche opérationnelle dans le wiki : objectif, cas d'usage, commande ou déclencheur, fichiers clés, limites connues et exemples d'utilisation.
- La version accessible du site d'exercice doit rester sobre, comme un vrai site corrigé, sans pédagogie visible.
- Les erreurs de formulaire ne doivent apparaître qu'après une tentative de soumission ou après interaction avec le champ concerné.
- Les documents accessibles doivent déclarer des métadonnées cohérentes avec leur langue réelle, notamment `fr` pour les documents en français. Les versions volontairement inaccessibles peuvent conserver des défauts pédagogiques explicites.
- Exercice pédagogique : ne pas distribuer la checklist au moment de l'identification. Les stagiaires doivent d'abord diagnostiquer sans filet ; la checklist sert ensuite à consolider, pas à court-circuiter le jugement.

## Playbooks

- **Nouvelle slide** : créer `scripts/slides/NN_nom.py`, suffixe lettre(s) pour intercaler (`05a_`, `02ma_`)
- **Tester** : `python3 scripts/assemble.py --only NN`
- **Template absent** : `python3 scripts/build_template.py`
- **Quarantine** : `xattr -d com.apple.quarantine formation-102638-juin-2026.pptx`
- **Contrôle tirets** : `grep -rn $'—\|–' scripts/` doit retourner vide
- **Contrôle PPTX** : `unzip -t formation-102638-juin-2026.pptx`
- **Warnings footer** : diagnostiquer par slide, corriger le positionnement source, puis régénérer le deck complet
- **Publier le site** : `rsync -a --delete --exclude='.DS_Store' --exclude='*.md' --exclude='.git' docs/ /tmp/easy-check-igpde/ && cd /tmp/easy-check-igpde && git add -A && git commit -m "Mise à jour du site" && git push`

**Grille IGPDE-DSFR (13,33" x 7,5")** :

| Constante | Valeur |
|-----------|--------|
| `MARGIN_L` | 0,52" |
| `CONTENT_W` | 12,28" |
| `COL_W` / `COL_R` | 5,98" / 6,83" |
| `TOP` contenu | 2,68" |
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
- Jamais importer depuis le skill global `~/.claude/skills/accessible-pptx/` — utiliser exclusivement `scripts/igpde_dsfr_components.py` (grille IGPDE 13,33", copie divergente)

## Modes d'échec connus

- `add_alert`/`add_callout` avec une string au lieu d'une liste : itère sur chaque caractère, slide pétée
- Changement typographique global (taille, espacement) sans recalibrer `_estimate_height` : 50+ slides débordent
- `add_image` sans `height=` à côté d'un autre composant : l'image déborde sur le composant suivant
- Estimation additive texte + image : ne pas supposer que `_estimate_height(text) + image_height` garantit l'absence de chevauchement ; vérifier le rendu et contraindre les hauteurs
- `layout_name="titre_soustitre"` sur une slide de contenu : affiche les logos institutionnels par erreur
- Accent `accent_w` différent de 0,08" (sauf chapitre 0,16") : perçu comme défaut d'alignement
- Placeholder Title : copier les 4 dimensions `(top, left, width, height)` sinon `left` et `width` tombent à 0
- Quiz : questions + réponses sur la même slide. Toujours séparer (suffixe `b`)
- `Stack` / `_safe_top` : `_safe_top` évite le débordement bas en remontant le composant, mais peut créer un chevauchement avec le bloc précédent si le `top` initial est trop optimiste
- Warning footer : ne jamais le traiter comme un simple bruit console. Vérifier l'écart avec le bloc précédent, resserrer ou recomposer la slide, puis viser `TOTAL_WARNINGS 0`

## Références

- `contraintes.md` pour les dépendances, limitations et features existantes.

| Ressource | Fichier |
|-----------|---------|
| Index slides ↔ modules | `scripts/slides/README.md` |
| Architecture C4 slides | `architecture-c4-slides.md` |
| Spec exercice Sami | `_source/exercice-sami-spec.md` |
| Diff des critères Sami | `_source/exercice-sami-diff.md` |
| Leçons techniques | `lessons.md` |
| points de contrôle rapides W3C | `03-easy-checks/w3c-easy-checks-fr.md` |
| Guide accessibiliser sa communication | `_source/references/Guide-2026-Accessibiliser-sa-communication-police-14-coul.md` |
| Notes réseaux sociaux | `04-reseaux-sociaux/md-reseaux-sociaux.md` |
| Notes FALC | `05-falc/md-falc.md` |
| Notes médias | `06-medias/md-medias.md` |
| Passation dernière session | `_source/passation-session-2026-05-03.md` |
| Publication site | `docs-publication.md` |
| Dépôt site standalone | `git@github.com:Alexmacapple/easy-check-igpde.git` |
| URL publique site | https://alexmacapple.github.io/easy-check-igpde/ |
| Dépendances | Python 3 + `python-pptx` + `lxml` + `openpyxl` + Marianne (fallback Arial) |
