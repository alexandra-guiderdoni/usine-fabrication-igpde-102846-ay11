# Formation 102638 — Accessibilité numérique (IGPDE)

> README causal — 2026-05-16

## En bref

Support de formation accessibilité numérique d'une journée, destiné aux communicants de l'administration (pas aux développeurs). Le projet produit un deck PPTX de 131 slides conformes au Design System de l'État (DSFR), un site d'exercices « points de contrôle rapides » W3C, un exercice sur document Word (Sami, 21 critères) et une grille d'audit XLSX. Tout est généré par des scripts Python — on n'édite jamais le PPTX à la main.

**Commande principale** : `python3 scripts/assemble.py`

---

## Pourquoi ce projet existe

L'IGPDE (institut de formation du ministère des Finances) programme une formation d'une journée sur l'accessibilité numérique pour des agents communicants. La commande vient de Carinne C., référente formation. Le public ne code pas : il produit des documents Word, des PDF, des visuels pour les réseaux sociaux, des newsletters.

Le point de départ est un template PowerPoint IGPDE natif au format 10" x 5,62", sans composants DSFR, sans accessibilité (pas d'ordre de lecture XML, pas de langue déclarée sur les runs, pas d'alt text). Les slides existantes sont construites à la main dans PowerPoint — chaque modification oblige à retoucher manuellement la mise en forme, les pieds de page, la numérotation.

À 131 slides, ce modèle artisanal ne tient plus : les corrections typographiques en cascade (remplacement « pilier » par « thème » sur 21 fichiers), les ajustements de grille après un changement de calibration, le maintien de la cohérence DSFR sur chaque slide — tout ça exige un pipeline programmatique ou une équipe dédiée. L'équipe n'existe pas.

*Sources : commits initiaux `d5cd1693`, `7cbb3483`, `474152ff` ; `CLAUDE.md` section Contexte ; `lessons.md` ; `_source/passation-session-2026-05-03.md`.*

---

## Pourquoi maintenant, pourquoi cette approche

**Kairos** : la formation est programmée pour le 4 juin 2026 (date visible dans `assemble.py` : `DATE_DEFAULT = "4 juin 2026"`). Le RGAA impose l'accessibilité des supports de formation produits par l'administration. Le template IGPDE existe et fournit les layouts institutionnels (logos, footer, ligne séparatrice) — il manque la couche DSFR et le pipeline de génération.

**Nécessitation** : la chaîne de contraintes qui rend cette architecture inévitable :

1. **131 slides** avec cohérence visuelle obligatoire → génération manuelle = dérive certaine
2. **Accessibilité PPTX** (ordre de lecture, `lang=fr-FR`, alt text, métadonnées) → impossible à garantir manuellement sur chaque slide
3. **Modifications fréquentes** (retours pédagogiques entre sessions, ajouts de contenu) → chaque modification doit être rejouable sans re-formater
4. **Template IGPDE imposé** (logos, grille, footer institutionnel) → la solution doit hériter du template, pas le remplacer
5. **Public non-technique** → le PPTX final doit être un fichier PowerPoint standard, pas un export web ou PDF

Ces 5 contraintes simultanées excluent les alternatives : un générateur Markdown-vers-PPTX générique ne respecte pas le template IGPDE ; une édition manuelle ne garantit ni la cohérence ni l'accessibilité à l'échelle ; un outil no-code type Canva ne produit pas du PPTX OOXML avec ordre de lecture.

*Sources : `contraintes.md` sections 2 et 4 ; `CLAUDE.md` section Comment je travaille ; `build_template.py` (rescaling 10" → 13,33") ; `assemble.py` ligne 35.*

---

## Comment le pipeline est construit

**Pattern** : pipeline programmatique à 3 couches — un assembleur orchestre des modules de contenu qui consomment une bibliothèque de composants DSFR, et un post-processeur garantit l'accessibilité.

**Composants** :

- **`scripts/assemble.py`** (orchestrateur) — résout la contrainte de reproductibilité. Découvre les modules `NN_*.py` par tri alphabétique, les exécute séquentiellement avec un contexte injecté (`page_num`, `date`, `footer_base`), appelle `finalize_pptx()` en sortie. Supporte `--only NN` pour tester une slide en isolation.

- **`scripts/slides/NN_*.py`** (131 modules) — résout la contrainte de modularité. Chaque module expose `build(prs, layouts, ctx)` et contient le contenu pédagogique d'une slide. Le nommage `NN` + suffixe alphabétique (`02ma_`, `05a_`) permet d'insérer des slides sans renuméroter.

- **`scripts/igpde_dsfr_components.py`** (55 Ko, 16 composants) — résout la contrainte de cohérence DSFR. Palette de couleurs, grille IGPDE (13,33" x 7,5"), helpers de composition (`add_callout`, `add_alert`, `add_stepper`, etc.), système de positionnement vertical (`Stack`, `_safe_top`, estimateurs de hauteur).

- **`finalize_pptx()`** (dans igpde_dsfr_components.py) — résout la contrainte d'accessibilité. Post-traitement XML : réordonnancement des shapes (titre → contenu → footer → décoratifs), `lang=fr-FR` sur chaque run, alt text vide sur les décoratifs, métadonnées `core_properties`, retrait du flag macOS `com.apple.quarantine`.

- **`scripts/build_template.py`** — résout la contrainte d'héritage institutionnel. Rescale le template IGPDE natif de 10" à 13,33" (facteur 1.3333), DSFRise les layouts (sommaire, chapitre), sauvegarde le template de base.

**Ce que la solution ne fait PAS intentionnellement** :
- Pas de rendu pixel — le pipeline manipule du XML OOXML, pas un moteur de rendu
- Pas de versionnement des retouches manuelles — les slides retouchées dans PowerPoint après génération sont dans un régime séparé
- Pas de CI/CD — la génération est locale, déclenchée par le formateur

**Générateurs secondaires** (hors pipeline slides principal) :
- `generate_exercice_sami.py` → 3 DOCX Word (inaccessible / aide / accessible) + PNG
- `generate_easy_checks_site_skeleton.py` → site d'exercice HTML DSFR en 3 variantes
- `generate_grille_audit.py` → grille XLSX 16 onglets
- `generate_wcag_langage_clair.py` → deck WCAG condensé (13 slides, dans `wcag/`)
- `validate.py` → validation automatisée du site d'exercice (contrat YAML, assets, liens)

*Sources : `scripts/assemble.py`, `scripts/slides/__init__.py`, `scripts/igpde_dsfr_components.py` (lignes 1-200, 302, 445-580, 631-1408), `architecture-c4-slides.md`.*

---

## Ce qui reste non résolu

**Exclusions assumées** :

- **Pas de tests unitaires** sur la bibliothèque de composants. La validation repose sur `validate.py` (site easy checks uniquement) et une passe visuelle manuelle dans PowerPoint. Choix délibéré : le coût de maintenance de tests sur du XML OOXML positionnel dépasse le bénéfice pour un projet à un seul développeur.

- **Pas de réconciliation entre les deux régimes de slides** (générées par script vs retouchées manuellement). La règle est documentée dans `CLAUDE.md` : « identifier le régime avant toute régénération ». Une régénération aveugle écrase les corrections manuelles.

- **Estimation heuristique des hauteurs** (`_estimate_height`). Le calcul approxime les caractères par pouce sans moteur de rendu texte. Les cas limites (texte long, polices variables) peuvent déborder — d'où la passe visuelle obligatoire avant livraison.

**Dettes tracées** :

- **`_safe_top` masque les débordements** au lieu de les signaler. Il remonte le composant pour éviter de sortir de la zone utile, mais peut créer un chevauchement avec le composant précédent. Le warning footer est le seul signal (`todo.md` : « ne jamais traiter comme un simple bruit console »).

- **Le template PPTX est généré une seule fois** par `build_template.py` et jamais régénéré automatiquement. Si le template source IGPDE change, il faut relancer manuellement le script de build du template avant de régénérer les slides.

- **Dépendance implicite à macOS** pour le retrait de quarantine Gatekeeper. Le pipeline fonctionne sur Linux mais le post-traitement `xattr -d` est spécifique à macOS (échoue silencieusement ailleurs).

*Sources : `todo.md`, `lessons.md`, `contraintes.md` sections 7 et 8, `CLAUDE.md` section Modes d'échec connus.*

---

## Références

| Ressource | Fichier |
|-----------|---------|
| Architecture C4 | `architecture-c4-slides.md` |
| Protocole agent Claude | `CLAUDE.md` |
| Protocole agent Codex | `AGENTS.md` |
| Contraintes compilées | `contraintes.md` |
| Leçons techniques | `lessons.md` |
| Tâches en cours | `todo.md` |
| Spec exercice Sami | `_source/exercice-sami-spec.md` |
| Passation derniere session | `_source/passation-session-2026-05-03.md` |
