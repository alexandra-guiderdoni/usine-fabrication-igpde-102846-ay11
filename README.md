# Usine de fabrication de la formation accessibilité numérique IGPDE

Dépôt autonome qui fabrique, à partir de sources versionnées, tous les supports de la formation « L'accessibilité numérique pour la bureautique et le web » de l'IGPDE (code 102846) : deck PPTX DSFR, site d'exercice, exercice Word, grille d'audit, fiches PDF accessibles et pack livrable.

---

## Vue d'ensemble

- **Deck** : 138 slides DSFR accessibles, générées par des scripts Python (`scripts/slides/`), jamais retouchées à la main.
- **Site d'exercice** : `docs/`, trois versions d'un site à auditer (inaccessible, aide à la correction, corrigée) et une démo « émojis et lecteurs d'écran », publiées sur https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/.
- **Exercice Word** : trois documents Sami générés par `scripts/generate_exercice_sami.py`.
- **Grille d'audit** : classeur XLSX des 13 points de contrôle rapides du W3C.
- **Fiches PDF accessibles** : mémos Word et LibreOffice, fiches WCAG, fiche des liens des TP.
- **Pack livrable** : `IGPDE-102846-livrables-octobre-2026/`, remis à l'IGPDE pour la session du 9 octobre 2026.

Une nouvelle session se prépare en modifiant `config.yml` (code, date, pied de page, nom du deck, dossier de livraison), puis en relançant la fabrication.

## Installation

Prérequis sur macOS (Homebrew) : `python@3.12`, `uv`, `pandoc`, `pango`, `glib`.

```bash
make installer
```

La commande crée `.venv` depuis `requirements.lock`, en vérifiant l'empreinte de chaque paquet, et active les contrôles git versionnés du dépôt (`.githooks`).

## Usage

```bash
make aide          # liste des commandes
make deck          # régénère le deck
make verifier      # tests, validation du site, contrôles du dépôt
make pack          # deck, PDF accessibles, vérification des installeurs
make apercu        # site d'exercice en local
make publier-site  # publication du site sur GitHub Pages
```

Les installeurs remis aux stagiaires (NVDA, Colour Contrast Analyser, Focus Highlight, PAC) ne sont pas versionnés : `make outils-telecharger` les récupère et vérifie leur empreinte SHA-256 (voir `IGPDE-102846-livrables-octobre-2026/outils/MANIFEST.md`).

## Structure

- `config.yml` : paramètres de la session, source unique.
- `scripts/` : génération du deck (`assemble.py`, `slides/`, `igpde_dsfr_components.py`), des documents, du site, de la grille, contrôle qualité du deck, fabrication du pack.
- `tests/`, `validate.py` : preuves de fonctionnement du deck et du site.
- `docs/` : source du site d'exercice.
- `publication-site/README.md` : présentation du dépôt publié du site, copiée par `make publier-site`.
- `recette/` : recette visuelle du site (manifestes ShipGuard), prévisualisation locale, rapports d'audit.
- `_source/`, `_assets/` : gabarits IGPDE, présentations et références sources, images.
- `01-cadre-legal/` à `06-medias/`, `fiche-pratique/`, `wcag/` : contenus pédagogiques et sources Markdown des fiches.
- `IGPDE-102846-livrables-octobre-2026/` : pack livrable de la session.
- `vendor/` : générateur PDF accessible embarqué.
- `notes/` : notes de réflexion, histoire du projet (`readme-causal.md`), cadrage de cette usine.

## Documentation

- Protocole pour les agents et les humains : [AGENTS.md](AGENTS.md)
- Réexporter le deck : [REEXPORTER-DECK-PPTX.md](REEXPORTER-DECK-PPTX.md)
- Publier le site : [PUBLIER-SITE.md](PUBLIER-SITE.md)
- Architecture de la chaîne : [architecture-c4-slides.md](architecture-c4-slides.md)
- Contraintes, leçons et suivi : [contraintes.md](contraintes.md), [lessons.md](lessons.md), [todo.md](todo.md)
- Pourquoi ce projet existe : [notes/readme-causal.md](notes/readme-causal.md)

## Licence

Licence Ouverte 2.0 (etalab-2.0), voir [LICENSE](LICENSE). Les documents de tiers rangés dans `_source/` restent la propriété de leurs auteurs.

---

Date de création : 2026-03-11 (projet), 2026-09-27 (usine autonome)
Dernière mise à jour : 2026-09-27
