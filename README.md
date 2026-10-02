# Usine de fabrication de la formation accessibilité numérique IGPDE

Dépôt autonome qui fabrique, à partir de sources versionnées, tous les supports de la formation « L'accessibilité numérique pour la bureautique et le web » de l'IGPDE (code 102846) : deck PPTX DSFR, site d'exercice, exercice Word, grille d'audit, fiches PDF accessibles et pack livrable.

**Avant toute action** : un agent lit d'abord [AGENTS.md](AGENTS.md), qui est le protocole canonique ; un humain s'y réfère dès qu'une commande, un livrable ou une publication sort du parcours ci-dessous.

---

## Vue d'ensemble

- **Deck** : support DSFR accessible généré par les scripts Python de `scripts/slides/`, dont le nombre de slides est déterminé à chaque fabrication et jamais figé manuellement.
- **Site d'exercice** : `docs/`, trois versions d'un site à auditer (inaccessible, aide à la correction, corrigée) et une démo « émojis et lecteurs d'écran », publiées sur https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/.
- **Exercice Word** : trois documents Sami générés par `scripts/generate_exercice_sami.py`.
- **Grille d'audit** : classeur XLSX des 13 points de contrôle rapides du W3C.
- **Fiches PDF accessibles** : mémos Word et LibreOffice, fiches WCAG, fiche des liens des TP.
- **Pack livrable** : `livrables-IGPDE-2026-102846/`, remis à l'IGPDE pour la session du 9 octobre 2026.

Une nouvelle session se prépare en modifiant `config.yml` (code, date, pied de page, nom du deck, dossier de livraison et URL du site), puis en relançant la fabrication. Il faut aussi renommer le dossier du pack, mettre à jour les documents administratifs et rechercher l'ancien code dans le site et la documentation (voir `AGENTS.md`).

## Installation

Prérequis sur macOS (Homebrew) : `python@3.12`, `uv`, `pandoc`, `pango`, `glib`.

```bash
make installer
```

La commande crée `.venv` depuis `requirements.lock`, en vérifiant l'empreinte de chaque paquet, et active les contrôles git versionnés du dépôt (`.githooks`).

La recette visuelle est optionnelle pour la fabrication du pack. Elle demande
`git`, Node.js 24 ou plus et npm ; son installation reste intégralement dans le
projet :

```bash
make installer-recette
```

Cette cible place `agent-browser` dans `recette/node_modules/`, Chrome for
Testing dans `.tools/` avec une empreinte vérifiée et clone ShipGuard `v2.14.0`
dans `.tools/shipguard/`. Ces répertoires sont ignorés par Git : aucun plugin
Codex global ni cache de navigateur global n'est requis.

## Usage

```bash
make aide          # liste des commandes
make deck          # régénère le deck et met à jour sa copie dans le pack
make qa            # qualité du deck ; lire le statut CONVERGED dans .qa/qa-pptx-report.md
make verifier      # tests, validation du site, contrôles du dépôt
make fraicheur-pack # contrôle les ressources que pack ne régénère pas
make pack          # PDF accessibles, fraîcheur, deck, supports, outils
make apercu        # site d'exercice en local
make installer-recette # dépendances locales de la recette visuelle
make recette       # recette visuelle du site corrigé
make publier-site  # publication du site, seulement après le succès de make verifier
```

`make pack` ne relance pas `make sami`, `make checklist`, `make grille` ni
`make wcag`. Avant de fabriquer le paquet, régénérer les sources concernées,
puis lancer `make fraicheur-pack`. `make pack` reconstruit ensuite les PDF,
rejoue ce contrôle de fraîcheur, régénère le deck et copie les supports.

Pour modifier le site, éditer exclusivement `docs/`, lancer `make verifier`, puis `make publier-site`. Les deux clones locaux du site sont des destinations de publication : ne jamais les modifier, commiter ou pousser.

Les installeurs remis aux stagiaires (NVDA, Colour Contrast Analyser, Focus Highlight, PAC) ne sont pas versionnés. `make outils-telecharger` récupère les trois outils disposant d'une adresse directe ; PAC doit être téléchargé manuellement. `make outils` vérifie ensuite la présence, la taille et l'empreinte SHA-256 des quatre fichiers (voir `livrables-IGPDE-2026-102846/outils/MANIFEST.md`).

## Structure

- `config.yml` : paramètres de la session, source unique.
- `scripts/` : génération du deck (`assemble.py`, `slides/`, `igpde_dsfr_components.py`), des documents et de la grille, validation et publication du site, contrôle qualité du deck, fabrication du pack.
- `tests/`, `validate.py` : preuves de fonctionnement du deck et du site.
- `docs/` : source du site d'exercice.
- `publication-site/` : `README.md`, `agents-site.md` et `claude-site.md`, copiés par `make publier-site` à la racine du dépôt publié du site sous les noms `README.md`, `AGENTS.md` et `CLAUDE.md` ; les deux derniers renvoient les agents vers l'usine.
- `recette/` : recette visuelle du site (manifestes ShipGuard), prévisualisation locale, rapports d'audit.
- `_source/`, `_assets/` : gabarits IGPDE, présentations et références sources, images.
- `03-easy-checks/` : contrat d'évaluation du site et grille d'audit XLSX.
- `corpus-documentaire-preparatoire/` : contenus pédagogiques des thèmes cadre légal, bureautique, réseaux sociaux, FALC et médias.
- `fiche-pratique/`, `wcag/` : sources Markdown des fiches PDF accessibles.
- `livrables-IGPDE-2026-102846/` : pack livrable de la session.
- `vendor/` : générateur PDF accessible embarqué.
- `notes/` : notes de réflexion, histoire du projet (`readme-causal.md`), cadrage de cette usine.

## Documentation

- Protocole pour les agents et les humains : [AGENTS.md](AGENTS.md)
- Générer des images de slides dans le style IGPDE Accessibilité : [_source/imagegen-igpde/README.md](_source/imagegen-igpde/README.md)
- Réexporter le deck : [REEXPORTER-DECK-PPTX.md](REEXPORTER-DECK-PPTX.md)
- Publier le site : [PUBLIER-SITE.md](PUBLIER-SITE.md)
- Architecture de la chaîne : [architecture-c4-slides.md](architecture-c4-slides.md)
- Contraintes, leçons et suivi : [contraintes.md](contraintes.md), [lessons.md](lessons.md), [todo.md](todo.md)
- Pourquoi ce projet existe : [notes/readme-causal.md](notes/readme-causal.md)

## Licence

Licence Ouverte 2.0 (etalab-2.0), voir [LICENSE](LICENSE). Les documents de tiers rangés dans `_source/` restent la propriété de leurs auteurs.

---

Date de création : 2026-03-11 (projet), 2026-09-27 (usine autonome)
Dernière mise à jour : 2026-10-02
