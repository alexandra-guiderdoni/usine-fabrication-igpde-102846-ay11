# Leçons IGPDE - Formation 102638

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

**Symptôme** : le fil d'Ariane devient `1.3. Easy Checks | ...` au lieu de `3. Easy Checks | ...`.

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

## Refactoring massif via AST

Pour patcher 14 slides en une opération (remplacer `top=X.XX, height=Y.YY` par `top=stack.push(estimate_*(args))`), un script Python utilisant `ast` + `ast.unparse` a été efficace. Préservation des args de chaque composant via `ast.unparse(arg_node)` pour regénérer le code source fidèlement.

Script jetable sauvegardé dans `/tmp/auto_stack.py` (supprimé en fin de session). Re-créable si besoin à partir du même pattern.

Leçon : pour >5 fichiers avec un pattern répétitif stable, un script AST est plus sûr qu'un regex.
