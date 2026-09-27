# Leçons IGPDE - Formation 102846, ex-102638

Enseignements techniques tirés de la construction du support de formation et de la grille d'audit. À relire avant toute nouvelle session sur ce projet ou sur un projet similaire à base de template PPTX hérité.

---

## python-pptx : modifier un placeholder hérité

Quand on modifie `ph.top` ou `ph.height` sur un placeholder hérité du layout (ex. Title 1), python-pptx crée un `<a:xfrm>` sur le shape. Ce nouvel xfrm ÉCRASE l'héritage du layout, y compris pour les dimensions non setées.

**Symptôme** : le titre disparaît visuellement alors que `ph.text_frame.text` contient bien la valeur.

**Cause** : `left` et `width` tombent à `0` par défaut dans le xfrm créé, rendant le shape invisible (largeur 0).

**Fix** : copier explicitement les 4 dimensions avant modification.

```python
current_left = ph.left
current_width = ph.width
ph.top = Inches(1.15)
ph.left = current_left     # recopier
ph.width = current_width   # recopier
ph.height = Inches(1.05)
```

Source : `igpde_dsfr_components.py` fonction `new_slide()` section titre.

---

## Layout DSFR IGPDE : numérotation automatique parasite

Le layout IGPDE « Titre et contenu » applique par défaut une numérotation automatique (`<a:buAutoNum type="arabicPeriod"/>`) sur le placeholder du fil d'Ariane. LibreOffice rend cette numérotation comme préfixe « 1. » devant le texte.

**Symptôme** : le fil d'Ariane devient `1.3. points de contrôle rapides | ...` au lieu de `3. points de contrôle rapides | ...`.

**Fix** : fonction `_neutralize_auto_numbering(txBody)` qui injecte `<a:buNone/>` sur chaque `<a:pPr>` du placeholder après avoir posé le texte.

Source : `igpde_dsfr_components.py` fonction `_neutralize_auto_numbering`.

---

## macOS Gatekeeper : flag com.apple.quarantine

Tout fichier généré par un processus Python non signé (python-pptx, openpyxl) reçoit automatiquement le flag `com.apple.quarantine` de Gatekeeper. PowerPoint et Excel ouvrent alors le fichier en mode protégé et REFUSENT d'enregistrer les modifications de l'utilisateur.

**Symptôme** : l'utilisateur édite dans PowerPoint puis ne peut pas sauvegarder.

**Fix** : `xattr -d com.apple.quarantine <fichier>` après génération.

Intégré dans `finalize_pptx()` et `generate_grille_audit.py` via `subprocess.run(["xattr", "-d", ...])` silencieux (ne plante pas sur Linux / environnements sans xattr).

---

## Notes présentateur : langue fr-FR explicite

`tf.text = texte` (python-pptx) crée un `<a:r>` sans attribut `<a:rPr lang>`. PowerPoint / lecteurs d'écran interprètent alors le texte selon la langue système (souvent en-US).

**Symptôme** : correcteur rouge sur tout le texte, accent anglais en lecture assistive.

**Fix** : `_set_lang_on_runs(tf._txBody, lang="fr-FR")` qui parcourt les runs, crée les `rPr` manquants et pose l'attribut `lang`. Appelé dans `add_notes()` ET dans `finalize_pptx()` (sur `slide.notes_slide._element` aussi, pas seulement `slide._element`).

---

## LibreOffice : interligne réel > interligne déclaré

L'estimation `height = lignes × size/72` sous-évalue la hauteur rendue par LibreOffice. L'interligne réel est plus large que la valeur XML demandée (~1,15).

**Règle de calibration** : utiliser `line_height_mult=1.35` comme facteur multiplicateur empirique. Plus prudent : 1.45 pour les cas critiques en fin de slide (proche du footer).

Si un composant déborde visuellement malgré le calcul, augmenter `h_padding` du composant (par défaut 0,25") à 0,30-0,35".

Source : helper `_estimate_height()` dans `igpde_dsfr_components.py`.

---

## Calibration de base des cartes empilées

Pour des cartes côte à côte (2 à 4), la hauteur DOIT être uniforme pour un rendu propre. Deux approches :

- **Recommandée** : calculer le max via `estimate_card_height()` pour chaque carte, puis passer la valeur max à chaque `add_card(height=H)`. Les cartes restent alignées quel que soit le contenu.
- **Alternative simple** : passer `height=None` à toutes, chaque carte aura sa hauteur auto (différences visibles).

```python
from igpde_dsfr_components import estimate_card_height
cards = [(titre, contenu, numero), ...]
HEIGHT = max(estimate_card_height(t, c, CARD_W, n) for t, c, n in cards)
for (t, c, n), i in zip(cards, range(len(cards))):
    add_card(slide, t, c, top=TOP, left=MARGIN+i*STEP, width=CARD_W, height=HEIGHT, numero=n)
```

---

## Positionnement relatif avec Stack

Pour empiler plusieurs composants (highlight + callout + alert…) :

```python
stack = Stack(top=2.3, gap=0.35)
add_highlight(slide, texte, top=stack.push(estimate_highlight_height(texte)))
add_callout(slide, titre, bullets, top=stack.push(estimate_callout_height(titre, bullets)))
add_alert(slide, titre=t2, bullets=b2, top=stack.push(estimate_alert_height(t2, b2)))
```

Avantage : le positionnement reste cohérent quelle que soit la variation du contenu (bullets ajoutés, titre modifié). Le `gap` constant contrôle l'aération entre composants. Valeur par défaut 0,35" ; 0,55" pour les tableaux après highlight (effet visuel d'ombre portée).

---

## Palette alerts unifiée

Choix esthétique DSFR IGPDE : toutes les alerts utilisent **fond gris clair + accent Bleu France**, indépendamment du `alert_type` (success, warning, error, info). Le paramètre reste dans la signature pour compatibilité mais n'affecte plus le rendu.

Justification : palette sobre, homogène, sans signal rouge/vert/orange qui alourdirait visuellement un deck pédagogique déjà riche. La distinction sémantique se fait dans le titre de l'alert (ex. « Piège fréquent », « Démo en 3 Tab », « Objectif : votre permis clavier »).

---

## add_callout / add_alert : hauteur de titre dynamique

Avant cette session, la hauteur du titre était fixée à `Inches(0.4)` et le corps commençait toujours à `top + 0.55"`. Si le titre passait sur 2 lignes, le corps chevauchait le titre.

**Fix appliqué** : `h_titre_box = max(_estimate_height(titre, width-0.35, size=14), 0.35)` — hauteur calculée dynamiquement. Corps positionné à `top + 0.10 + h_titre_box + 0.10`.

Affecte : `add_callout()` et `add_alert()` dans `igpde_dsfr_components.py`.

---

## add_highlight : saut de ligne via `\n`

`add_highlight` appelle `_apply_text` qui pose `run.text = str(texte)` sans interpréter les `\n`.

**Fix appliqué** : splitta sur `\n`, premier segment via `_apply_text`, segments suivants via `tf.add_paragraph()` avec le même formatage (FONT, 18pt, bold, BLEU_FRANCE).

`_estimate_height` gérait déjà `\n` correctement (split interne).

---

## add_textbox direct sans Inches() = positions brisées

`slide.shapes.add_textbox(0.52, 3.15, ...)` passe des valeurs en EMU, pas en pouces. 0.52 EMU ≈ 0 sur un slide de 13,33 pouces.

**Règle** : toujours utiliser `Inches(x)` ou les helpers `add_texte_libre` / `add_callout`. Ne jamais appeler `add_textbox` directement avec des valeurs décimales.

---

## Grille 2 rangées de cartes : top dynamique anti-débordement

Pour deux rangées de cartes (ex. sommaire 2x2), calculer le `row1_top` en fonction de `card_h` :

```python
BOTTOM_SAFE = BOTTOM_CONTENT - 0.05
row1_top = min(2.20, BOTTOM_SAFE - 2 * card_h - GAP_ROWS)
row2_top = row1_top + card_h + GAP_ROWS
```

- Si les cartes sont petites : `row1_top = 2.20"` (proche du titre)
- Si les cartes sont grandes : `row1_top` se recale vers le haut pour ne pas déborder

Erreur fréquente : hardcoder `TOP_CARDS = 2.45"` sans vérifier que `row2_top + card_h <= BOTTOM_CONTENT`.

---

## add_callout / add_alert : string au lieu de liste = slide cassée

Passer une string unique au lieu d'une liste de bullets à `add_callout` ou `add_alert` itère sur chaque caractère de la string. Chaque lettre devient un bullet.

**Symptôme** : la slide affiche des dizaines de lignes d'un caractère chacune.

**Cause** : `_add_bullets(tf, items, ...)` itère sur `items`. Si `items` est une string `"Texte"`, Python itère sur `['T', 'e', 'x', 't', 'e']`.

**Fix** : toujours passer une liste, même pour un seul bullet : `["Mon texte"]`, jamais `"Mon texte"`.

Source : `AGENTS.md` section Modes d'échec connus.

---

## Changement typographique global : recalibrer _estimate_height

Modifier la taille de police, l'interligne ou l'espacement sur l'ensemble du deck sans recalibrer les constantes de `_estimate_height` provoque des débordements en cascade sur 50+ slides.

**Symptôme** : texte coupé ou chevauchement massif après un changement de taille de police apparemment mineur.

**Règle** : tout changement typographique global (taille, interligne, espacement) impose une passe de recalibration de `_estimate_height` et des `h_padding` avant régénération.

Source : `AGENTS.md` section Modes d'échec connus.

---

## add_image sans height= : débordement sur le composant suivant

`add_image` sans paramètre `height=` laisse python-pptx calculer la hauteur à partir du ratio natif de l'image. Si l'image est haute, elle déborde sur le composant empilé en dessous.

**Règle** : toujours passer `height=` à `add_image` quand un autre composant suit sur la même slide. Vérifier visuellement que `image_top + image_height` reste au-dessus du composant suivant.

Source : `AGENTS.md` section Modes d'échec connus.

---

## Estimation additive texte + image : ne pas additionner

Ne pas supposer que `_estimate_height(text) + image_height` garantit l'absence de chevauchement. L'estimation de texte est heuristique et les marges internes des composants ajoutent des pouces invisibles.

**Règle** : contraindre les hauteurs explicitement et vérifier le rendu dans PowerPoint. Ne pas se fier à un calcul purement additif.

Source : `AGENTS.md` section Modes d'échec connus.

---

## Layout titre_soustitre sur une slide de contenu : logos parasites

Utiliser `layout_name="titre_soustitre"` sur une slide de contenu normal affiche les logos institutionnels (République française, IGPDE) en plein milieu de la slide, au-dessus du contenu.

**Règle** : `titre_soustitre` est réservé à la page de couverture et à la slide de clôture. Pour le contenu, utiliser `titre_contenu`.

Source : `AGENTS.md` section Modes d'échec connus ; incident slide 21 (`_source/passation-session-2026-05-03.md`).

---

## Accent accent_w : 0,08" sauf chapitre

L'accent bleu vertical à gauche du titre doit mesurer 0,08" de large. Toute autre valeur (0,05", 0,10") est perçue comme un défaut d'alignement par rapport aux autres slides.

**Exception** : les slides de chapitre utilisent `accent_w=0,16"` (bandeau plus large, voulu).

Source : `AGENTS.md` section Modes d'échec connus.

---

## Quiz : séparer questions et réponses

Les questions et réponses d'un quiz ne doivent jamais figurer sur la même slide. Le stagiaire voit la réponse avant de réfléchir, ce qui annule l'effet pédagogique.

**Règle** : créer deux modules : `NN_quiz.py` (question) et `NNb_quiz.py` (réponse, suffixe `b`).

Source : `AGENTS.md` section Modes d'échec connus.

---

## _safe_top : chevauchement silencieux avec le bloc précédent

`_safe_top(top, height)` remonte le composant si `top + height > BOTTOM_CONTENT`. Cela évite le débordement bas mais peut créer un chevauchement avec le composant précédent si le `top` initial était déjà trop bas.

**Symptôme** : deux composants superposés visuellement, mais aucune erreur dans la console.

**Règle** : ne pas compter sur `_safe_top` comme filet de sécurité. Calibrer les hauteurs et les gaps en amont via `Stack` + estimateurs. Si `_safe_top` se déclenche, c'est un signal que la slide est trop chargée — la recomposer.

Source : `AGENTS.md` section Modes d'échec connus.

---

## Warning footer : jamais du bruit

Le warning `footer overlap` en console signale qu'un composant empiète sur la zone footer (y > 6,80"). Ne jamais le traiter comme du bruit console.

**Règle** : vérifier l'écart entre le dernier composant et le footer, resserrer les gaps ou recomposer la slide. Objectif : `TOTAL_WARNINGS 0` avant livraison.

Source : `AGENTS.md` section Modes d'échec connus.

---

## Refactoring massif via AST

Pour patcher 14 slides en une opération (remplacer `top=X.XX, height=Y.YY` par `top=stack.push(estimate_*(args))`), un script Python utilisant `ast` + `ast.unparse` a été efficace. Préservation des args de chaque composant via `ast.unparse(arg_node)` pour regénérer le code source fidèlement.

Script jetable sauvegardé dans `/tmp/auto_stack.py` (supprimé en fin de session). Re-créable si besoin à partir du même pattern.

Leçon : pour >5 fichiers avec un pattern répétitif stable, un script AST est plus sûr qu'un regex.

---

## Livrable présent sur le disque, absent de git

Le `.gitignore` global de l'ancien espace de travail excluait les formats `*.pptx`, `*.docx`, `*.mp4` et `*.mp3`. Le deck régénéré, les documents administratifs renumérotés et les médias du site existaient sur le disque sans jamais avoir été versionnés, et le renommage du dossier du pack avait fait sortir de git les trois DOCX de l'exercice Sami.

**Règle** : un livrable est prouvé par `git ls-files`, pas par `ls`. Après un renommage de dossier, comparer la liste suivie avant et après (`git status --ignored`).

Source : migration vers l'usine autonome, 2026-09-27.

---

## git filter-repo : les remplacements littéraux passent avant les expressions régulières

Avec `--replace-text`, une règle littérale (un numéro de téléphone) a été appliquée avant une règle `regex:` qui ciblait la ligne entière contenant ce numéro. La regex ne trouvait plus rien, et l'adresse est restée dans l'historique jusqu'à une troisième passe.

**Règle** : écrire les expressions régulières sur la forme finale du texte, ou ne pas faire chevaucher règles littérales et regex. Toujours vérifier par une recherche sur toutes les révisions : `git grep -l "motif" $(git rev-list --all)`.

Source : extraction de l'historique, 2026-09-27.

---

## zsh ne découpe pas les variables

Une variable contenant une liste de chemins (`INC="scripts docs ..."`), passée à `grep -r $INC`, est traitée par zsh comme un seul chemin inexistant : la recherche renvoie zéro résultat sans erreur, ce qui ressemble à un résultat propre.

**Règle** : pour une liste, utiliser un tableau sous `bash -c` (`"${INC[@]}"`), et se méfier d'un zéro obtenu trop facilement sur une recherche de données sensibles.

Source : recherche de données personnelles avant publication, 2026-09-27.

---

## Hooks git et bash de macOS

Le `bash` fourni par macOS est la version 3.2 : `mapfile` n'existe pas et un hook qui l'utilise échoue en silence sur une variable vide. Les hooks de `.githooks/` lisent leurs listes par `while IFS= read -r`.

**Règle** : tester chaque hook en positif et en négatif (un faux fichier interdit indexé doit bloquer le commit) avec `/bin/bash`.

Source : `.githooks/pre-commit`, 2026-09-27.

---

## Supprimer la destination avant de vérifier la source

`scripts/build_template.py` supprimait le gabarit de destination avant de copier sa source. La source (gabarit IGPDE 10 pouces) n'existant plus, un lancement aurait effacé le gabarit indispensable à la génération, puis échoué.

**Règle** : dans un script de reconstruction, vérifier l'existence de la source avant toute suppression.

Source : revue des scripts de gabarit, 2026-09-27.
