# Architecture C4 — Pipeline de generation des slides PPTX DSFR

## Contraintes et hypotheses

**Sources locales lues** :
- `CLAUDE.md`, `AGENTS.md`, `contraintes.md`
- `scripts/assemble.py`, `scripts/slides/__init__.py`
- `scripts/igpde_dsfr_components.py` (lignes 1-200, 302, 445-580, 631-1000, 1090-1230, 1287-1408)
- `scripts/build_template.py`
- `scripts/slides/02ma_definition-a11y.py` (module type)

**Systeme en scope** : pipeline de generation du deck PPTX principal `formation-102638-juin-2026.pptx` (131 slides DSFR accessibles).

**Audiences** : Alex (formateur/developpeur), Carinne C. (commanditaire IGPDE, non-technique).

**Contraintes non negociables** :
- Python 3.12 + python-pptx + lxml (pas de Docker, pas de CI)
- Template IGPDE rescale 13,33" x 7,5" avec grille DSFR figee
- Police Marianne (fallback Arial)
- Accessibilite : ordre de lecture, `lang=fr-FR`, alt text, metadonnees
- macOS : quarantine Gatekeeper a retirer sur le PPTX genere
- Pas de modification directe du PPTX — tout passe par les scripts Python
- Deux regimes de slides : generees par script vs retouchees manuellement

---

## C1 — Contexte

```text
+------------------+                    +------------------+
|   Alex           |                    |  Carinne C.      |
|  (formateur /    |                    |  (commanditaire  |
|   developpeur)   |                    |   IGPDE)         |
+--------+---------+                    +--------+---------+
         |                                       |
         | edite les scripts Python               | recoit le PPTX final
         | lance assemble.py                      | ouvre dans PowerPoint
         | valide le rendu visuel                 | anime la formation
         |                                       |
         v                                       v
+--------+---------------------------------------+--------+
|                                                         |
|   Pipeline de generation des slides PPTX DSFR           |
|   (131 modules Python -> 1 PPTX accessible)             |
|                                                         |
+---+---------------------+-------------------+-----------+
    |                     |                   |
    v                     v                   v
+---+------+     +--------+------+    +-------+--------+
| python-  |     | Template      |    | PowerPoint     |
| pptx     |     | IGPDE-DSFR    |    | (verification  |
| (biblio- |     | (.pptx base)  |    |  manuelle)     |
| theque)  |     +---------------+    +----------------+
+----------+
```

Le formateur Alex edite les modules Python et lance la generation. Le deck PPTX produit est livre a Carinne C. qui l'utilise dans PowerPoint pour animer la formation. PowerPoint sert aussi de verification manuelle (debordements, rendu visuel) car le pipeline ne couvre pas le rendu pixel.

---

## C2 — Containers

```text
+----------------------------------------------------------------------+
|  Pipeline de generation des slides                                   |
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
|  | NN_*.py (131 modules)   |   | (bibliotheque DSFR)             |  |
|  |                         |   |                                 |  |
|  | Chacun expose :         |   | create_presentation()           |  |
|  |   build(prs,layouts,ctx)|   | new_slide()                     |  |
|  |                         |   | 16 composants (add_*)           |  |
|  | Contenu pedagogique +   |   | Stack, _safe_top, _estimate_h   |  |
|  | appels aux composants   |   | finalize_pptx() (a11y)          |  |
|  +-------------------------+   +---------------------------------+  |
|                                                                      |
+----------------------------------------------------------------------+

+---------------------------+     +------------------------------+
| PPT-IGPDE-DSFR-base-      |     | formation-102638-juin-2026   |
| intervenant.pptx          |     | .pptx                        |
| (template avec layouts    |     | (artefact final, 131 slides) |
|  et master)               |     +------------------------------+
+---------------------------+
```

| Container | Technologie | Responsabilite | Donnees |
|-----------|-------------|----------------|---------|
| `assemble.py` | Python 3 | Orchestre la decouverte, le tri, le chargement et l'execution sequentielle des modules de slides. Produit le PPTX final | Lit les modules `NN_*.py`, ecrit le `.pptx` |
| `scripts/slides/NN_*.py` (131 fichiers) | Python 3 | Chaque module definit le contenu d'une ou plusieurs slides. Expose `build(prs, layouts, ctx)` | Importe les composants depuis `igpde_dsfr_components` |
| `igpde_dsfr_components.py` (55 Ko) | Python 3 + python-pptx + lxml | Bibliotheque de composants DSFR : grille, palette, 16 helpers de composition, post-traitement a11y | Charge le template PPTX, manipule le XML OOXML |
| `build_template.py` | Python 3 + python-pptx | Genere le template DSFR 13,33"x7,5" a partir du source IGPDE 10"x5,62" (rescaling + DSFRisation) | Lit `PPT-IGPDE-base-intervenant.pptx`, ecrit le template DSFR |
| Template PPTX | OOXML | 6 layouts natifs IGPDE : couverture, titre_soustitre, sommaire, chapitre, 3_colonnes, titre_contenu | Fichier binaire PPTX |
| Artefact final | PPTX | Deck complet livre a la formatrice | 131 slides, ~5 Mo |

---

## C3 — Composants de `igpde_dsfr_components.py`

Le container central merite un zoom car il porte toute la logique de composition et d'accessibilite.

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
|  COMPOSANTS (16 helpers publics)                                      |
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

| Composant | Interface | Responsabilite | Source locale |
|-----------|-----------|----------------|--------------|
| `create_presentation()` | `() -> (prs, layouts)` | Charge le template PPTX, construit le dict des 6 layouts | L.188 |
| `new_slide()` | `(prs, layouts, layout_name, titre, ...) -> slide` | Cree une slide avec layout, titre, footer, fil d'ariane, accent couleur | L.302 |
| `Stack` | `.push(h) -> top` | Curseur vertical qui empile les composants avec gap constant (evite le calcul manuel des `top`) | L.555 |
| `_safe_top()` | `(top, height) -> top` | Garde-fou : remonte le composant si `top+height > BOTTOM_CONTENT` | L.478 |
| `_estimate_height()` | `(content, width, ...) -> float` | Estime la hauteur en pouces d'un texte pour le positionnement | L.496 |
| `add_callout` | `(slide, titre, bullets, top, ...) -> shape` | Boite d'information bleue DSFR avec titre + bullets | L.631 |
| `add_alert` | `(slide, titre, bullets, top, severity, ...) -> shape` | Alerte DSFR (warning / error / success / info) | L.677 |
| `add_highlight` | `(slide, texte, top, ...) -> shape` | Bandeau d'emphase avec accent bleu | L.722 |
| `add_quote` | `(slide, texte, auteur, ...) -> shape` | Citation avec guillemets et attribution | L.769 |
| `add_card` | `(slide, titre, contenu, top, left, ...) -> shape` | Carte DSFR avec numero, titre et contenu | L.807 |
| `add_pave_chiffre` | `(slide, valeur, label, ...) -> shape` | Pave KPI (chiffre + label) | L.859 |
| `add_stepper` | `(slide, etapes, top, ...) -> shape` | Processus sequentiel DSFR (pastilles numerotees) | L.884 |
| `add_tableau` | `(slide, headers, rows, ...) -> float` | Tableau DSFR. Retourne la hauteur pour empilement | L.931 |
| `add_image` | `(slide, path, top, left, ...) -> shape` | Image avec alt text obligatoire | L.998 |
| `add_texte_libre` | `(slide, texte, top, ...) -> shape` | Texte positionne sans composant DSFR | L.984 |
| `add_notes` | `(slide, texte) -> None` | Notes presentateur (invisibles en projection) | L.445 |
| `add_encadre` | `(slide, ...) -> shape` | Encadre fond colore parametrable | L.1181 |
| `add_fleche` | `(slide, top, left, ...) -> shape` | Fleche decorative entre elements | L.1090 |
| `compose_sommaire` | `(slide, titre, parties) -> None` | Compose un sommaire avec cards numerotees | L.1209 |
| `compose_chapitre` | `(slide, numero, titre) -> None` | Compose une slide de chapitre avec bandeau bleu | L.1227 |
| `finalize_pptx` | `(prs, output, ...) -> path` | Post-traitement a11y complet : ordre de lecture, langue, decoratifs, metadonnees, quarantine macOS | L.1368 |

---

## Flux dynamique — Generation du deck

```text
1. Alex lance : python3 scripts/assemble.py
                      |
2. assemble.py        | appelle create_presentation()
                      | -> charge PPT-IGPDE-DSFR-base-intervenant.pptx
                      | -> retourne (prs, layouts)
                      |
3.                    | appelle discover_slides()
                      | -> scanne scripts/slides/, filtre NN_*.py, trie par nom
                      | -> retourne [Path x 113]
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
6.                    | print "[OK] formation-102638-juin-2026.pptx"
```

---

## Limites a dire en presentation

- **Pas de rendu pixel** : le pipeline genere du XML OOXML, pas un rendu visuel. Les debordements fins ne sont detectables que dans PowerPoint (passe manuelle obligatoire).
- **`_estimate_height` est heuristique** : l'estimation de hauteur repose sur un calcul approximatif (caracteres par pouce), pas sur un moteur de rendu texte. Les cas limites (texte long, polices variables) peuvent deborder.
- **`_safe_top` est un garde-fou de dernier recours** : il remonte un composant pour eviter de sortir de la zone utile, mais peut creer un chevauchement avec le composant precedent si le `top` initial etait deja trop bas.
- **Deux regimes de slides** : certaines slides sont retouchees manuellement dans PowerPoint apres generation. La regeneration ecrase ces corrections. Il faut identifier le regime avant de relancer `assemble.py`.
- **Pas de CI/CD** : la generation est locale, sur le poste d'Alex. Pas de pipeline de build automatise.
- **Pas de tests unitaires** : la bibliotheque de composants n'a pas de suite de tests. La validation repose sur `validate.py` (site easy checks uniquement) et la passe visuelle manuelle.

---

## Checklist de conformité C4

- [x] Systeme en scope et systemes externes distingues
- [x] Personnes/roles visibles en C1
- [x] Containers C2 sont des applications ou data stores en runtime
- [x] Chaque element a type, responsabilite et technologie
- [x] Chaque relation est orientee et labellisee
- [x] Contraintes et hypotheses documentees avant les recommandations
- [x] C3 present uniquement pour le container critique (igpde_dsfr_components.py)
- [x] Sources locales lues citees
- [x] Chaque vue a un titre lisible indiquant son niveau
