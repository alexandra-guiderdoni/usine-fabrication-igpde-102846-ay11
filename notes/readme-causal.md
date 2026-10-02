# Formation 102846, ex-102638 — Accessibilité numérique (IGPDE)

> README causal, écrit le 2026-05-22, mis à jour le 2026-09-27. Ce document raconte pourquoi le projet existe et pourquoi il est construit ainsi. Il ne donne aucune consigne de travail : pour agir, suivre `AGENTS.md` (protocole unique pour tous les agents et les humains) et `make aide`.

## En bref

Support de formation accessibilité numérique d'une journée, destiné aux communicants de l'administration (pas aux développeurs). Le projet produit un deck PPTX dont le total est calculé à la fabrication, un site d'exercices « points de contrôle rapides » W3C, un TP Word guidé en cinq stations, une grille d'audit XLSX et des fiches PDF accessibles. Le deck est entièrement généré par des scripts Python : on n'édite jamais le PPTX à la main.

Depuis le 2026-09-27, le projet vit dans ce dépôt autonome, l'usine, qui est sa seule source de référence. Le site d'exercice est publié depuis `docs/` sur un dépôt séparé (voir `PUBLIER-SITE.md`).

---

## Pourquoi ce projet existe

L'IGPDE (institut de formation du ministère des Finances) programme une formation d'une journée sur l'accessibilité numérique pour des agents communicants. La commande vient de Carine C., référente formation à l'IGPDE, commanditaire et interlocutrice administrative. Le public ne code pas : il produit des documents Word, des PDF, des visuels pour les réseaux sociaux, des newsletters.

Le point de départ est un template PowerPoint IGPDE natif au format 10" x 5,62", sans composants DSFR, sans accessibilité (pas d'ordre de lecture XML, pas de langue déclarée sur les runs, pas d'alt text). Les slides d'origine étaient construites à la main dans PowerPoint : chaque modification obligeait à retoucher la mise en forme, les pieds de page, la numérotation.

À 138 slides, ce modèle artisanal ne tient plus : les corrections typographiques en cascade (remplacement « pilier » par « thème » sur 21 fichiers), les ajustements de grille après un changement de calibration, le maintien de la cohérence DSFR sur chaque slide exigent un pipeline programmatique ou une équipe dédiée. L'équipe n'existe pas.

*Sources : commits initiaux `d5cd1693`, `7cbb3483`, `474152ff` ; `lessons.md` ; `_source/passation-session-2026-05-03.md`.*

---

## Pourquoi cette approche

**Kairos** : la première session était programmée pour le 4 juin 2026, puis la formation a été reprogrammée au 9 octobre 2026 sous le code 102846. Le RGAA impose l'accessibilité des supports de formation produits par l'administration. Le template IGPDE fournit les layouts institutionnels (logos, pied de page, ligne séparatrice) ; il manquait la couche DSFR et le pipeline de génération.

**Nécessitation** : la chaîne de contraintes qui rend cette architecture inévitable :

1. **138 slides** avec cohérence visuelle obligatoire : la génération manuelle dérive à coup sûr.
2. **Accessibilité PPTX** (ordre de lecture, `lang=fr-FR`, alt text, métadonnées) : impossible à garantir à la main sur chaque slide.
3. **Modifications fréquentes** (retours pédagogiques entre sessions, ajouts de contenu) : chaque modification doit être rejouable sans reformater.
4. **Template IGPDE imposé** (logos, grille, pied de page institutionnel) : la solution doit hériter du template, pas le remplacer.
5. **Public non technique** : le livrable doit être un fichier PowerPoint standard, pas un export web ou PDF.

Ces cinq contraintes simultanées excluent les alternatives : un générateur Markdown vers PPTX générique ne respecte pas le template IGPDE ; une édition manuelle ne garantit ni la cohérence ni l'accessibilité à l'échelle ; un outil sans code de type Canva ne produit pas de PPTX OOXML avec ordre de lecture.

*Sources : `contraintes.md` sections 2 et 4 ; `scripts/assemble.py` ; `config.yml`.*

---

## Comment le pipeline est construit

**Pattern** : pipeline programmatique à trois couches. Un assembleur orchestre des modules de contenu qui consomment une bibliothèque de composants DSFR, et un post-traitement garantit l'accessibilité.

- **`scripts/assemble.py`** (orchestrateur) répond à la contrainte de reproductibilité. Il découvre les modules `scripts/slides/*.py` par tri alphabétique, les exécute avec un contexte injecté (`page_num`, `date`, `footer_base`, tirés de `config.yml`) et appelle `finalize_pptx()` en sortie.
- **`scripts/slides/`** répond à la contrainte de modularité. Chaque module expose `build(prs, layouts, ctx)` ; le suffixe alphabétique (`02ma_`) permet d'intercaler une slide sans renuméroter.
- **`scripts/igpde_dsfr_components.py`** répond à la contrainte de cohérence DSFR : palette, grille IGPDE (13,33" x 7,5"), composants de composition (`add_callout`, `add_alert`, `add_stepper`, etc.), positionnement vertical (`Stack`, `_safe_top`, estimateurs de hauteur).
- **`finalize_pptx()`** répond à la contrainte d'accessibilité : réordonnancement des formes (titre, contenu, pied de page, décoratifs), `lang=fr-FR` sur chaque run, alt text vide sur les décoratifs, métadonnées, retrait de la quarantaine macOS.
- **Le gabarit** `_source/presentations-source/PPT-IGPDE-DSFR-base-intervenant.pptx` a d'abord été produit par `scripts/build_template.py` (mise à l'échelle 10" vers 13,33" et DSFRisation), dont la source IGPDE native n'est plus dans le dépôt. Pour le reconstruire aujourd'hui : `scripts/rebuild_template_from_demo.py` (voir `AGENTS.md`).

**Ce que la solution ne fait pas, volontairement** :

- pas de rendu pixel : le pipeline manipule du XML OOXML, pas un moteur de rendu ;
- pas de retouche manuelle du deck : toute correction passe par un module de `scripts/slides/`, sinon la régénération suivante l'écrase ;
- pas d'intégration continue : la génération est locale, lancée par le formateur avec `make`.

**Autres générateurs** : exercice Sami (`make sami`), grille d'audit XLSX (`make grille`), deck WCAG condensé (`make wcag`), PDF accessibles (`make pdf`). Le site d'exercice `docs/` a été amorcé par `scripts/generate_easy_checks_site_skeleton.py`, mais il est maintenu à la main depuis juillet 2026 : ce générateur ne doit plus être relancé sans relire le diff complet. `validate.py` contrôle le site (contrat YAML, assets, liens).

*Sources : `scripts/assemble.py`, `scripts/igpde_dsfr_components.py`, `Makefile`, `architecture-c4-slides.md`.*

---

## Ce qui reste non résolu

**Exclusions assumées** :

- **Pas de rendu pixel automatisé**. Les tests couvrent les contrats Python, l'accessibilité XML, la géométrie et la boucle QA du deck, mais ne remplacent pas une ouverture dans PowerPoint : une relecture visuelle humaine reste nécessaire.
- **Estimation heuristique des hauteurs** (`_estimate_height`). Le calcul approxime les caractères par pouce sans moteur de rendu texte ; les cas limites peuvent déborder, d'où la relecture visuelle avant livraison.

**Dettes tracées** :

- **`_safe_top` masque les débordements** au lieu de les signaler : il remonte le composant, mais peut créer un chevauchement avec le précédent. L'avertissement de pied de page est le seul signal, à ne jamais ignorer.
- **La boucle QA du deck (`make qa`) est déterministe, pas visuelle**. Elle détecte les régressions XML et géométriques et peut corriger les accents sous option, mais ne juge pas le rendu typographique.
- **Dépendance à macOS** pour le retrait de la quarantaine Gatekeeper (`xattr`), sans effet ailleurs.

*Sources : `todo.md`, `lessons.md`, `contraintes.md`, section « Modes d'échec connus » d'`AGENTS.md`.*

---

## Pour aller plus loin

- Protocole de travail, commun à tous les agents : `AGENTS.md` (`CLAUDE.md` l'importe)
- Présentation et installation : `README.md`
- Architecture de la chaîne : `architecture-c4-slides.md`
- Réexport du deck : `REEXPORTER-DECK-PPTX.md`
- Publication du site : `PUBLIER-SITE.md`
- Contraintes, leçons, suivi : `contraintes.md`, `lessons.md`, `todo.md`
- Exercice Sami : `_source/exercice-sami-matrice.yml`
- Passations de mai 2026 (historique) : `_source/passation-session-2026-05-03.md`, `_source/passation-session-2026-05-04.md`
