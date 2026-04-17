# Projet IGPDE — Formation 102638 (Carinne C.)

Template PPTX DSFRisé bâti sur la base graphique IGPDE (header + footer + logos institutionnels préservés). Ce CLAUDE.md hérite de `~/.claude/CLAUDE.md` (langue, style, typographie française) et de `~/Claude/CLAUDE.md` (workspace).

---

## Skills à utiliser systématiquement

Pour toute création, modification ou validation de slides dans ce projet, se référer aux deux skills suivants (ne pas réinventer la logique) :

| Skill | Fichier | Rôle |
|-------|---------|------|
| `/composition-dsfr-pptx` | `/Users/alex/Claude/.claude/skills/composition-dsfr-pptx/SKILL.md` | Composition des slides DSFR (triage, 4 mouvements structurer/composer/rendre/valider, recettes de composition, anti-patterns, 8 critères de validation) |
| `/accessible-pptx` | `/Users/alex/Claude/.claude/skills/accessible-pptx/SKILL.md` | Pipeline Markdown → PPTX accessible (post-traitement a11y, ordre de lecture, alt text, langue, en-têtes de tableau, métadonnées) |

**Règles d'usage** :
- Pour une nouvelle slide DSFR ou une refonte de layout : lire `/composition-dsfr-pptx` en priorité, appliquer le Mode B (script Python dédié) qui correspond au fonctionnement de ce projet
- Pour valider l'accessibilité d'un livrable avant remise : appliquer la checklist de `/accessible-pptx` (8 critères par slide, post-traitement `finalize_pptx`)
- Ne jamais livrer sans avoir passé le gate de livraison DSFR (8 critères par slide + post-traitement a11y + notes présentateur) décrit dans `/composition-dsfr-pptx`

---

## Scripts du projet

Tous les scripts Python vivent dans `/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/scripts/` :

| Script | Rôle |
|--------|------|
| `igpde_dsfr_components.py` | Bibliothèque de composants DSFR calée sur la grille IGPDE (13,33" × 7,5") avec préservation automatique du header (logos, titre) et du footer (ligne séparatrice à y=6,98", date, n° diapo, pied de page institut) |
| `build_template.py` | Construit `PPT-IGPDE-DSFR-base-intervenant.pptx` depuis le source IGPDE original (rescale 10" × 5,62" → 13,33" × 7,5", suppression des slides exemples) |
| `rebuild_template_from_demo.py` | Reconstruit le template depuis la démo (fallback quand le source original est indisponible) |
| `generate_demo.py` | Génère `demo-template-dsfr.pptx` — 9 slides démonstrant chaque layout et chaque composant |

Exécution type :
```bash
cd /Users/alex/Claude/projets-formations/IGPDE-Carinne-C
python3 scripts/build_template.py         # construit le template
python3 scripts/generate_demo.py          # génère la démo
```

---

## Grille IGPDE-DSFR (13,33" × 7,5")

Constantes exportées par `igpde_dsfr_components.py` :

| Constante | Valeur | Rôle |
|-----------|--------|------|
| `SLIDE_W` | 13,33" | Largeur slide |
| `SLIDE_H` | 7,5" | Hauteur slide |
| `MARGIN_L` | 0,52" | Marge gauche |
| `CONTENT_W` | 12,28" | Largeur utile |
| `GAP` | 0,33" | Gouttière entre colonnes |
| `COL_W` | 5,98" | Largeur colonne 50 % |
| `COL_R` | 6,83" | Position colonne droite |
| `TOP_CONTENT` | 2,68" | Début zone contenu sous le titre |
| `BOTTOM_CONTENT` | 6,80" | Fin zone contenu avant le footer |
| `FOOTER_Y` | 6,98" | Y de la ligne séparatrice du footer |

---

## Layouts IGPDE disponibles

| Nom (clé Python) | Usage | Particularités |
|------------------|-------|----------------|
| `couverture` | Page de garde | Logos IGPDE préservés, titre posé à droite (hors zone du pied de page) |
| `titre_soustitre` | Titre + intro | Logos IGPDE, titre en zone centrale |
| `sommaire` | Sommaire en 3 cards DSFR | Refonte DSFR via `compose_sommaire()` (3 cards numérotées) |
| `chapitre` | Transition de partie | Refonte DSFR via `compose_chapitre()` (bandeau bleu pleine largeur + n° rouge) |
| `3_colonnes` | Comparatif ou triptyque | Fil d'Ariane à droite, 3 cartes DSFR |
| `titre_contenu` | Contenu libre | Zone libre pour tout composant DSFR |

---

## Composants DSFR disponibles

Importés depuis `igpde_dsfr_components` :

| Helper | Rôle |
|--------|------|
| `new_slide(prs, layouts, layout_name, titre, fil_ariane, footer_text, date_text, page_num)` | Nouvelle slide avec header/footer IGPDE préservés |
| `add_callout` | Encadré bleu à accent gauche (titre + bullets) |
| `add_alert(..., alert_type)` | Alerte colorée (`success`, `warning`, `error`, `info`) |
| `add_highlight` | Phrase d'emphase (accent bleu, 18pt) |
| `add_quote` | Citation italique + auteur |
| `add_card(..., numero)` | Carte DSFR avec pastille numérotée optionnelle |
| `add_pave_chiffre` | KPI (valeur blanc sur bleu + label) |
| `add_stepper` | Étapes numérotées avec connecteurs |
| `add_tableau` | Tableau DSFR avec en-têtes accessibles |
| `add_fleche` | Flèche verte d'évolution |
| `add_encadre` | Encadré paramétrable |
| `add_texte_libre` | Zone de texte positionnée |
| `add_notes` | Notes présentateur |
| `compose_sommaire` | Recette : 3 cards numérotées |
| `compose_chapitre` | Recette : bandeau bleu pleine largeur |
| `finalize_pptx` | Post-traitement a11y + sauvegarde |

---

## Conventions pour ce projet

- **Typographie française irréprochable** : accents, apostrophes typographiques ', espaces insécables, guillemets français « ». Jamais « Accessibilite » — voir `~/.claude/CLAUDE.md` pour la règle complète
- **Pied de page** : toujours « Formation 102638 / {section} » avec la date du jour de formation (« 4 juin 2026 » pour cette session)
- **Fil d'Ariane** : format « N. Section | Sous-section » avec numéro de section et espaces autour du `|`, aligné à droite (préservation du style IGPDE natif)
- **Date** : format long français « 4 juin 2026 » (pas « 04/06/2026 »)
- **Header et footer** : ne jamais modifier la ligne séparatrice IGPDE à y=6,98" ni la disposition des logos — ils définissent l'identité graphique institutionnelle
- **Couverture** : titre à droite (x=5,80"), pour ne pas chevaucher le pied de page qui occupe la moitié basse-gauche
- **Contraintes DSFR** : palette Bleu France `#000091` + Rouge Marianne `#E1000F`, police Marianne (fallback Arial si non installée), composants suivant `/composition-dsfr-pptx`
- **Accessibilité** : post-traitement `finalize_pptx()` obligatoire avant livraison. Ne jamais livrer un PPTX qui n'a pas été post-traité

---

## Livrables

| Fichier | Contenu |
|---------|---------|
| `PPT-IGPDE-DSFR-base-intervenant.pptx` | Template vierge (6 layouts, aucune slide) — base pour toute nouvelle présentation |
| `demo-template-dsfr.pptx` | Démonstration (9 slides) — 1 par layout + composants DSFR |
| `_assets/` | Logos et visuels IGPDE extraits du source original |
| `_source/` | Sources du programme de formation 102638 (DOCX, cartographie) |

---

## Dépendances

- Python 3 + `python-pptx` + `lxml` (installés globalement)
- Police Marianne installée sur le système (fallback Arial automatique)
- Template IGPDE-DSFR présent (`PPT-IGPDE-DSFR-base-intervenant.pptx`) — sinon lancer `build_template.py` ou `rebuild_template_from_demo.py`
