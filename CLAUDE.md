# Projet IGPDE — Formation 102638 (Carinne C.)

Template PPTX DSFRisé bâti sur la base graphique IGPDE (header + footer + logos institutionnels préservés). Ce CLAUDE.md hérite de `~/.claude/CLAUDE.md` (langue, style, typographie française) et de `~/Claude/CLAUDE.md` (workspace).

---

## Skills à utiliser systématiquement

Pour toute création, modification ou validation de slides dans ce projet, se référer aux trois skills suivants, dans cet ordre (amont pédagogique → composition DSFR → accessibilité) :

| Skill | Fichier | Rôle |
|-------|---------|------|
| `/pedagogie-neuro` | `/Users/alex/Claude/.claude/skills/pedagogie-neuro/SKILL.md` | Transformation du contenu brut en expérience d'apprentissage (26 règles neuropédagogie, diagnostic → transformation → livrable). OBLIGATOIRE avant toute écriture de slide |
| `/composition-dsfr-pptx` | `/Users/alex/Claude/.claude/skills/composition-dsfr-pptx/SKILL.md` | Composition des slides DSFR (triage, 4 mouvements structurer/composer/rendre/valider, recettes de composition, anti-patterns, 8 critères de validation) |
| `/accessible-pptx` | `/Users/alex/Claude/.claude/skills/accessible-pptx/SKILL.md` | Pipeline Markdown → PPTX accessible (post-traitement a11y, ordre de lecture, alt text, langue, en-têtes de tableau, métadonnées) |

**Règles d'usage** :
- Avant d'écrire quoi que ce soit dans `scripts/slides/NN_*.py`, appliquer `/pedagogie-neuro` sur le corpus source pour sortir un contenu pédagogique transformé (analogie, chunking, exercice, plan d'action)
- Pour une nouvelle slide DSFR ou une refonte de layout : lire `/composition-dsfr-pptx` en priorité, appliquer le Mode B (script Python dédié) qui correspond au fonctionnement de ce projet
- Pour valider l'accessibilité d'un livrable avant remise : appliquer la checklist de `/accessible-pptx` (8 critères par slide, post-traitement `finalize_pptx`)
- Ne jamais livrer sans avoir passé le gate de livraison DSFR (8 critères par slide + post-traitement a11y + notes présentateur) décrit dans `/composition-dsfr-pptx`

---

## Philosophie pédagogique du projet

Ce support de formation n'est pas une documentation illustrée : c'est une **expérience d'apprentissage** qui vise la transformation, pas l'information (règle 26 de la neuropédagogie). Toute slide produite ici doit pouvoir se justifier devant cette checklist :

- **Engagement immédiat** : chaque module ouvre par une question, un chiffre choc ou une devinette — jamais par « Plan du module » ou « Présentation de l'intervenant »
- **Chunking** : 3 à 5 éléments par slide maximum. Au-delà, on scinde ou on synthétise en tableau
- **Analogie concrète** : chaque concept technique est connecté à un référent du quotidien (le clavier est le GPS, l'alt text est un sous-titre, le focus est un curseur)
- **Récupération active** : au moins une prédiction, un quiz ou un mini-exercice par bloc de 2-3 slides
- **Plan d'action en clôture** : chaque module se termine par « Que faites-vous demain à 9 h ? » — un geste concret et mesurable
- **Sécurité psychologique** : l'erreur du stagiaire est une donnée d'apprentissage, pas une faute. Les alertes `warning/error` parlent des **pièges techniques**, jamais de l'utilisateur

**Ton et typographie** : ton direct et conversationnel, comme si on expliquait à un collègue. Pas de jargon pédagogique (« objectif opérationnel », « compétence visée »). Pas de formule passive (« il sera vu que… »). Typographie française irréprochable (voir section Conventions).

**Notes présentateur (`add_notes`)** : chaque slide porte les indications d'animation (question à poser, silence à tenir, prédiction à provoquer, cas concret à évoquer) — elles sont la bande-son de la slide.

---

## Public cible — formation 102638

| Critère | Valeur |
|---------|--------|
| Code | 102638 — « L'accessibilité numérique pour la bureautique et le web » |
| Durée | 1 jour (environ 7 h) |
| Niveau | Initiation — aucun prérequis obligatoire |
| Public | Communicants de toutes les directions ministérielles et producteurs de contenu numérique. **Profil métier, pas développeurs.** |
| Intervenant | Formateur Opquast certifié (Carinne C.), référent Assurance Qualité Web et accessibilité numérique RGAA/WCAG |
| Salle | Équipée d'ordinateurs ; chaque stagiaire apporte un casque audio pour tester un lecteur d'écran |
| Méthode | Apports théoriques brefs + exercices pratiques (création de documents, correction d'erreurs, tests lecteur d'écran) |
| Évaluation | Auto-évaluation en début et fin de formation pour mesurer la progression |

**Conséquences pour la conception des slides** :
- Éviter le jargon développeur (ARIA, DOM, CSS, sélecteur, API) — si un terme technique est nécessaire, le définir en 1 phrase
- Privilégier les analogies de communication (publication, brief, correction) plutôt que de développement
- Prévoir systématiquement un temps de manipulation (site d'entraînement, document Word à corriger, export PDF à tester)
- Les slides servent l'oral, elles ne le remplacent pas — 1 slide = 2 minutes maximum

### Modules du programme détaillé

**Ordre impératif : M1 → M2 → M3 → M4. Ne jamais inverser.**

| N° | Module | Fichiers sources | Pages PPTX | Contenu clé |
|----|--------|-----------------|------------|-------------|
| 0 | Introduction, cadre légal | `01_` → `02q_` | 1–19 | Couverture, objectifs, sommaire, intervenants, idées reçues, définition, RGAA, déclaration |
| 2 | Créer des documents bureautiques accessibles | `03_` → `26_` | 20–44 | Word, 5 piliers, exercices, quiz, checklist, clôture |
| 3 | Pratiquer les évaluations rapides d'accessibilité web (Easy Checks) | `28_` → `52_` | 45–69 | 13 vérifications W3C WAI — corpus local dans `03-easy-checks/` |
| 4 | Améliorer l'accessibilité des publications sur les réseaux sociaux | `53_` → `55o_` | 70–86 | Alt text, hashtags, émojis, écriture inclusive |

---

## Correspondance des Easy Checks W3C avec les slides du module 3

Le module 3 couvre les 13 Easy Checks du W3C WAI (source : `03-easy-checks/w3c-easy-checks-fr.md`). Chaque slide est rattachée à un Easy Check identifié par son numéro.

**Convention** : le fil d'Ariane des slides du module 3 a la forme `3. Easy Checks | N. Libellé court` où `N` est le numéro du check W3C.

| Easy Check W3C | WCAG | Fichiers sources | Libellé court retenu |
|----------------|------|-----------------|----------------------|
| Chapitre d'ouverture module 3 | — | `28_chapitre-easy-checks` | 3. Easy Checks |
| 1. Texte alternatif des images | 1.1.1 | `29_` à `31_` (3 slides : types / rédaction / exemples) | 1. Alternatives textuelles |
| 2. Titre de page | 2.4.2 | `32_` (1 slide) | 2. Titre de page |
| 3. Titres de rubriques | 1.3.1, 2.4.6 | `33_` à `34_` (2 slides : hiérarchie / outils) | 3. Titres de rubriques |
| 4. Contraste des couleurs | 1.4.3 | `35_` à `36_` (2 slides : principe / outils) | 4. Contraste |
| 5. Lien d'évitement | 2.4.1 | `37_` (1 slide) | 5. Lien d'évitement |
| **6. Focus clavier visible** | 2.4.7 | `38_` à `41_` (4 slides : ouverture / 5 touches / signaux / mission) | **6. Focus et navigation clavier** (élargi) |
| 7. Langue de la page | 3.1.1 | `42_` (1 slide) | 7. Langue |
| 8. Zoom | 1.4.4 | `43_` (1 slide) | 8. Zoom |
| 9. Sous-titres | 1.2.2 | `44_` à `45_` (2 slides : principe / pièges auto) | 9. Sous-titres |
| 10. Transcriptions | 1.2.1 | `46_` (1 slide) | 10. Transcriptions |
| 11. Audiodescription | 1.2.5 | `47_` (1 slide) | 11. Audiodescription |
| 12. Étiquettes de formulaire | 3.3.2, 1.3.1 | `48_` à `50_` (3 slides : principe / placeholder / groupes) | 12. Étiquettes de formulaire |
| 13. Champs obligatoires | 3.3.2 | `51_` (1 slide) | 13. Champs obligatoires |
| Mission finale module 3 | — | `52_mission-13-checks` | Mission finale |

**Note sur l'Easy Check 6 étendu** : l'Easy Check 6 du W3C se concentre strictement sur le **focus clavier visible** (CR 2.4.7). La séquence `03_` à `06_` élargit ce périmètre à la **navigation clavier complète** (tabulation avec `Tab` / `Shift+Tab`, activation avec `Entrée` / `Espace`, lecture aux flèches, annonce d'état) parce que le public cible (communicants) a besoin d'une boîte à outils clavier cohérente, pas d'un critère isolé. L'extension touche aussi WCAG 2.1.1 (fonctionnalités au clavier) et 2.4.3 (ordre de tabulation logique).

---

## Scripts du projet

Tous les scripts Python vivent dans `/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/scripts/` :

| Script | Rôle |
|--------|------|
| `igpde_dsfr_components.py` | Bibliothèque de composants DSFR calée sur la grille IGPDE (13,33" × 7,5") avec préservation automatique du header (logos, titre) et du footer (ligne séparatrice à y=6,98", date, n° diapo, pied de page institut) |
| `build_template.py` | Construit `PPT-IGPDE-DSFR-base-intervenant.pptx` depuis le source IGPDE original (rescale 10" × 5,62" → 13,33" × 7,5", suppression des slides exemples) |
| `rebuild_template_from_demo.py` | Reconstruit le template depuis la démo (fallback quand le source original est indisponible) |
| `generate_demo.py` | Génère `gabarits-ppt-igpde.pptx` - démonstration pédagogique des gabarits IGPDE-DSFR et de tous les composants disponibles |
| `assemble.py` | Assemble les slides de `scripts/slides/` en un PPTX unique (support de formation) |
| `slides/NN_nom.py` | Une slide par module, ordre garanti par préfixe numérique (`01_`, `02_`…) |
| `generate_grille_audit.py` | Génère `03-easy-checks/grille-audit-easy-checks.xlsx` - classeur d'audit pour les stagiaires (13 critères, 4 onglets, validation de données, formules de synthèse) |
| `generate_exercice_sami.py` | Génère les 2 DOCX de l'exercice Sami (`_source/sami-doc-inaccessible.docx` + `_source/sami-doc-accessible.docx`) et les 2 graphiques PNG (`_assets/graphique-*.png`). Spec dans `_source/exercice-sami-spec.md` |

Exécution type :
```bash
cd /Users/alex/Claude/projets-formations/IGPDE-Carinne-C
python3 scripts/build_template.py         # construit le template
python3 scripts/generate_demo.py          # génère la démo
python3 scripts/assemble.py               # génère le support de formation
```

---

## Procédure slides modulaires (`scripts/slides/` + `assemble.py`)

Chaque slide vit dans son propre module Python sous `scripts/slides/`, ce qui permet d'ajouter, tester ou réordonner une slide sans toucher aux autres.

### Convention de nommage

- Nom de fichier : `NN_nom-descriptif.py` où `NN` = numéro à 2 chiffres (`01`, `02`, …, `42`)
- Pour insérer une slide entre deux existantes sans tout renuméroter : suffixe lettre (`05a_intercalee.py` passe entre `05_` et `06_`)
- Les modules sont découverts automatiquement par tri alphabétique

### Contrat d'un module de slide

Chaque module expose exactement une fonction `build(prs, layouts, ctx)` :

```python
"""Slide N : description courte."""

from igpde_dsfr_components import add_callout, add_notes, new_slide


def build(prs, layouts, ctx):
    slide = new_slide(
        prs, layouts,
        layout_name="titre_soustitre",
        titre="Titre de la slide",
        footer_text=f"{ctx.footer_base} / Sous-section",
        date_text=ctx.date,
        page_num=ctx.page_num,
    )
    add_callout(slide, "Accroche", ["Point 1", "Point 2"], top=3.8, height=2.5)
    add_notes(slide, "Notes du présentateur.")
    return slide
```

Le `ctx` (type `SlideContext`) est injecté par `assemble.py` et porte :

| Champ | Rôle |
|-------|------|
| `ctx.page_num` | Numéro de page recalculé à chaque assemblage — jamais hardcodé |
| `ctx.date` | Date formatée en français long (ex. « 4 juin 2026 ») |
| `ctx.footer_base` | Préfixe de pied de page (ex. « Formation 102638 ») |

### Commandes `assemble.py`

```bash
python3 scripts/assemble.py                          # toutes les slides
python3 scripts/assemble.py --only 05                # une seule slide (page_num=1)
python3 scripts/assemble.py --from 03 --to 07        # plage de slides
python3 scripts/assemble.py -o variante.pptx         # sortie personnalisée
python3 scripts/assemble.py --date "15 octobre 2026" # autre date de session
python3 scripts/assemble.py --footer-base "Formation 102638 v2"
```

Sortie par défaut : `formation-102638-juin-2026.pptx` à la racine du projet.

### Règles d'or

- **Ne jamais hardcoder `page_num`** dans un module — toujours passer par `ctx.page_num`. Sinon, insérer une slide casse la pagination des suivantes
- **Ne pas modifier `generate_demo.py`** pour ajouter des slides de formation — ce script documente les composants disponibles, il reste intact
- **Toujours appliquer `/composition-dsfr-pptx` et `/accessible-pptx`** avant d'ajouter une nouvelle slide — voir la section « Skills à utiliser systématiquement » ci-dessus
- **Pour tester une slide en isolation** : utiliser `--only NN`. La slide est générée en page 1 d'un PPTX vierge, ce qui permet de vérifier rendu et composants sans polluer le support complet

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
| `TOP_CONTENT` | 2,68" | Début zone contenu sous le titre (KPI, stepper, tableau, callout seul) |
| `TOP_CARDS` | 2,45" | Début zone cartes (gap serré au titre — spécifique aux slides à cartes) |
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

- **Typographie française irréprochable** : accents, apostrophes typographiques ', espaces insécables, guillemets français « ». Jamais « Accessibilite ». Voir `~/.claude/CLAUDE.md` pour la règle complète
- **Jamais de tiret cadratin ni demi-cadratin dans les scripts** : utiliser le tiret simple `-` à la place. Règle fixée en session (2026-04-17). Concerne tout le contenu des fichiers Python (docstrings, commentaires, chaînes de caractères) ET le texte affiché sur les slides. Le script `generate_grille_audit.py` et tous les modules `scripts/slides/*.py` respectent cette convention. Commande de contrôle : `grep -rn $'\u2014\|\u2013' scripts/ 03-easy-checks/ CLAUDE.md` doit ne rien retourner dans `scripts/`
- **Pied de page** : toujours « Formation 102638 / {section} » avec la date du jour de formation (« 4 juin 2026 » pour cette session)
- **Fil d'Ariane** : format « N. Section | Sous-section » avec numéro de section et espaces autour du `|`, aligné à droite (préservation du style IGPDE natif)
- **Date** : format long français « 4 juin 2026 » (pas « 04/06/2026 »)
- **Header et footer** : ne jamais modifier la ligne séparatrice IGPDE à y=6,98" ni la disposition des logos — ils définissent l'identité graphique institutionnelle
- **Couverture** : titre à droite (x=5,80"), pour ne pas chevaucher le pied de page qui occupe la moitié basse-gauche
- **Contraintes DSFR** : palette Bleu France `#000091` + Rouge Marianne `#E1000F`, police Marianne (fallback Arial si non installée), composants suivant `/composition-dsfr-pptx`
- **Accessibilité** : post-traitement `finalize_pptx()` obligatoire avant livraison. Ne jamais livrer un PPTX qui n'a pas été post-traité
- **Fichiers générés et quarantine macOS** : les PPTX et XLSX produits par Python portent automatiquement le flag `com.apple.quarantine` (Gatekeeper). PowerPoint et Excel les ouvrent alors en mode protégé et refusent d'enregistrer les modifications. `finalize_pptx` et `generate_grille_audit.py` retirent ce flag automatiquement via `xattr -d com.apple.quarantine <fichier>` après sauvegarde. Si ce fix saute (environnement non macOS ou exception silencieuse), lancer manuellement : `xattr -d com.apple.quarantine formation-102638.pptx`
- **Éditer les sources Python, pas le PPTX livré** : `formation-102638-juin-2026.pptx` et `gabarits-ppt-igpde.pptx` sont des LIVRABLES régénérés à chaque exécution des scripts - toute modification directe dans PowerPoint sera perdue à la prochaine génération. Pour modifier une slide, éditer le module `scripts/slides/NN_*.py` correspondant, puis relancer `assemble.py`
- **Largeur d'accent unifiée à 0,08"** : tous les composants non structurants (callout, alert, highlight, card, quote, encadré) posent leur accent vertical gauche avec `accent_w=0.08` dans `_make_box`. Seul `compose_chapitre` conserve `accent_w=0.16` pour son rôle de bandeau structurant pleine largeur. Ne jamais introduire de valeur intermédiaire (0,10 ou 0,12) : l'œil perçoit les différences comme un défaut d'alignement visuel
- **Resserrage du placeholder Title** : `new_slide()` force `ph.top = 1,15"` et `ph.height = 1,05"` sur le placeholder titre hérité du layout (qui a une hauteur native de ~1,5" avec un vide interne d'~1"). Les 4 dimensions `(top, left, width, height)` doivent être copiées explicitement car python-pptx crée un `<a:xfrm>` sur le shape qui écrase l'héritage du layout — sans copie, `left` et `width` tombent à 0 et le titre n'est plus rendu
- **Contenu qui commence à top=2,30"** : premier composant de contenu (highlight, callout, tableau, cards) positionné à `top=2.30` minimum pour laisser respirer le titre resserré tout en évitant le vide excessif. Les composants suivants sont décalés avec des gaps de 0,25 à 0,40"
- **Hauteur auto des composants** : `add_callout`, `add_alert`, `add_highlight`, `add_quote` calculent TOUJOURS leur hauteur à partir du contenu (le paramètre `height` est ignoré). `add_card` prend `max(height, auto)` pour respecter l'alignement cross-cartes. Helper interne `_estimate_height(content, width, size, line_height_mult=1.35)` (~7,5 car/pouce à 11pt). Helpers publics exposés : `estimate_callout_height(titre, bullets, width)`, `estimate_alert_height(...)`, `estimate_highlight_height(texte, width)`, `estimate_quote_height(texte, auteur, width)`, `estimate_card_height(titre, contenu, width, numero)`
- **Positionnement en cascade** : classe `Stack(top=2.30, gap=0.35)` qui empile les composants verticalement. Usage :
  ```python
  stack = Stack(top=2.3, gap=0.35)
  add_highlight(slide, texte, top=stack.push(estimate_highlight_height(texte)))
  add_callout(slide, titre, bullets, top=stack.push(estimate_callout_height(titre, bullets)))
  ```
  Les slides à plusieurs composants empilés utilisent ce pattern pour un rendu sans vide et sans débordement, quel que soit le contenu
- **Langue des notes présentateur** : `add_notes()` pose `lang="fr-FR"` sur chaque run dès la création ; `finalize_pptx()` repasse sur le `notes_slide` de chaque diapo. Cette double passe corrige un bug latent de python-pptx : `tf.text = texte` crée un `<a:r>` sans `<a:rPr lang>`, et PowerPoint interprète alors le texte selon la langue système (souvent en-US). Sans ce fix, les notes s'affichent soulignées en rouge par le correcteur et sont lues avec un accent anglais par les lecteurs d'écran. Le fix est dans `igpde_dsfr_components.py` (`_set_lang_on_runs` crée les `rPr` manquants, `finalize_pptx` traite aussi les notes)
- **`add_highlight` supporte `\n`** : un `\n` dans le texte crée un vrai saut de paragraphe (pas un retour à la ligne visuel). `_estimate_height` gère déjà `\n` correctement. Exemple : `"Règle d'or :\nvous créez un obstacle..."` affiche deux lignes distinctes
- **Hauteur titre dynamique dans `add_callout` / `add_alert`** : la hauteur du titre n'est plus fixée à `0.4"`. Elle est calculée via `_estimate_height(titre, ..., size=14)` et le corps commence à `top + 0.10 + h_titre_box + 0.10`. Un titre sur 2 lignes ne chevauche plus le corps
- **Ne jamais appeler `add_textbox` directement** : `slide.shapes.add_textbox(0.52, 3.15, ...)` passe des valeurs en EMU, pas en pouces — positions à zéro. Toujours utiliser `add_texte_libre` ou les helpers DSFR qui wrappent avec `Inches()`
- **Grille 2 rangées de cartes** : pour un sommaire 2×2, calculer `row1_top` dynamiquement pour éviter tout débordement sur le footer : `row1_top = min(2.20, BOTTOM_CONTENT - 0.05 - 2 * card_h - GAP_ROWS)`. Ne pas hardcoder `TOP_CARDS` pour les layouts multi-rangées
- **Quiz en deux slides distinctes** : questions sur une slide, réponses sur la slide suivante (suffixe `b` dans le nom de fichier, ex. `22_quiz-final.py` + `22b_quiz-final-reponses.py`). Jamais questions + réponses sur la même slide

---

## Livrables

| Fichier | Contenu |
|---------|---------|
| `PPT-IGPDE-DSFR-base-intervenant.pptx` | Template vierge (6 layouts, aucune slide) - base pour toute nouvelle présentation |
| `gabarits-ppt-igpde.pptx` | Démonstration pédagogique - 1 slide par gabarit IGPDE-DSFR + composants DSFR illustrés. Produit par `scripts/generate_demo.py` |
| `formation-102638-juin-2026.pptx` | Support de formation complet pour la session de juin 2026 (86 slides, assemblé depuis `scripts/slides/`). Produit par `scripts/assemble.py` |
| `_source/sami-doc-inaccessible.docx` | Exercice Sami - document Word avec 8 erreurs intentionnelles (3 faux titres, tableau sans en-tête, URGENT couleur seule, contraste #767676, graphique sans alt, lien non descriptif). Distribué aux binômes en slide 32. Produit par `scripts/generate_exercice_sami.py`. Sera enrichi au fil des slides 20 à 44 |
| `_source/sami-doc-accessible.docx` | Exercice Sami - version corrigée (vrais styles, en-tête balisée, contraste #595959, alt text, lien descriptif, propriétés document). Produit par `scripts/generate_exercice_sami.py`. Sera enrichi au fil des slides 20 à 44 |
| `03-easy-checks/grille-audit-easy-checks.md` | Grille d'audit documentaire (13 critères, mode d'emploi, imprimable) |
| `03-easy-checks/grille-audit-easy-checks.xlsx` | Grille d'audit opérationnelle (16 onglets : Mode d'emploi, Échantillon RGAA, 12 onglets de page obligatoire/représentative pré-remplis avec l'intitulé, Exemple, Synthèse multi-pages avec agrégation automatique via formules cross-sheet). Pour saisie pendant la mission finale de la slide 27 |
| `_assets/` | Logos, visuels IGPDE et graphiques de l'exercice Sami (versions accessible et inaccessible) |
| `_source/` | Sources du programme de formation 102638 (DOCX, cartographie, spec exercice Sami) |

**Convention de nommage des PPTX produits** : pour une nouvelle session, créer une variante datée via `python3 scripts/assemble.py -o formation-102638-<mois-année>.pptx`. Le script conserve la source unique dans `scripts/slides/`, seul le livrable change de nom.

---

## Dépendances

- Python 3 + `python-pptx` + `lxml` + `openpyxl` (installés globalement)
- Police Marianne installée sur le système (fallback Arial automatique)
- Template IGPDE-DSFR présent (`PPT-IGPDE-DSFR-base-intervenant.pptx`) — sinon lancer `build_template.py` ou `rebuild_template_from_demo.py`
- LibreOffice (`/Applications/LibreOffice.app`) pour conversion PDF et captures de vérification

---

## Leçons capitalisées

Les patterns techniques non évidents découverts pendant le développement sont documentés dans `lessons.md` à la racine du projet : modification de placeholder hérité python-pptx, numérotation auto parasite des layouts DSFR, quarantine macOS, langue des notes présentateur, interligne LibreOffice, calibration Stack, palette alerts unifiée, hauteur titre dynamique callout/alert, support `\n` dans highlight, grille 2 rangées anti-débordement. À relire avant toute extension du support.

---

**Dernière mise à jour** : 2026-04-22
**Version** : 1.3.0 (86 slides, quiz scindé, titre dynamique, highlight \n, grille 2×2 dynamique)
