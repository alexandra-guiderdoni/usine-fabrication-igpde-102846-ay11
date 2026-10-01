# Usine de fabrication de la formation accessibilité numérique IGPDE.
# Point d'entrée unique, pour un humain comme pour un agent : make aide

PYTHON ?= $(shell if [ -x .venv/bin/python ]; then echo .venv/bin/python; elif [ -x /opt/homebrew/bin/python3.12 ]; then echo /opt/homebrew/bin/python3.12; else echo python3; fi)
CONFIG ?= config.yml
ifneq ($(strip $(MAKECMDGOALS)),installer)
LIVRABLES := $(shell $(PYTHON) scripts/config.py --config "$(CONFIG)" --value livrables)
ifeq ($(strip $(LIVRABLES)),)
$(error Impossible de lire livrables depuis $(CONFIG))
endif
endif
SITE_CLONE ?= $(LIVRABLES)/Formateur/tp-easy-check-site-web-igpde
SITE_CONSULTATION ?= ../tp-fabrication-igpde-102846-ay11

.PHONY: aide installer installer-recette deck qa tests valider controles verifier grille sami checklist wcag pdf supports outils outils-telecharger fraicheur-pack pack apercu recette publier-site

aide:
	@echo "Usine IGPDE - commandes principales (Python : $(PYTHON))"
	@echo "  make installer           environnement Python verrouillé + hooks git"
	@echo "  make installer-recette   dépendances locales ShipGuard et navigateur de recette"
	@echo "  make deck                régénère le deck PPTX depuis scripts/slides/ et met à jour sa copie dans le pack"
	@echo "  make qa                  boucle qualité du deck (lire .qa/qa-pptx-report.md)"
	@echo "  make verifier            tests + validation du site + contrôles du dépôt"
	@echo "  make grille              régénère la grille d'audit XLSX et la copie dans le site"
	@echo "  make sami                régénère les 3 documents Word de l'exercice Sami"
	@echo "  make checklist           régénère le DOCX et la source Markdown de la checklist Sami"
	@echo "  make wcag                régénère le deck WCAG en langage clair (condensé) dans wcag/"
	@echo "  make fraicheur-pack      vérifie la fraîcheur des ressources du pack"
	@echo "  make pdf                 régénère les PDF accessibles du pack"
	@echo "  make supports            démo hors ligne et documents Sami dans le pack"
	@echo "  make pack                PDF + fraîcheur + deck + supports + outils"
	@echo "  make outils-telecharger  récupère et vérifie les installeurs"
	@echo "  make apercu              site d'exercice en local"
	@echo "  make recette             recette visuelle ShipGuard du site corrigé"
	@echo "  make publier-site        publie docs/ et publication-site/ sur le dépôt du site (GitHub Pages)"

installer:
	uv venv .venv --python /opt/homebrew/bin/python3.12
	uv pip sync --require-hashes --python .venv/bin/python requirements.lock
	git config core.hooksPath .githooks
	@echo "Environnement prêt. Prérequis Homebrew pour les PDF : pandoc pango glib"

installer-recette:
	bash recette/installer-recette.sh

deck:
	$(PYTHON) scripts/assemble.py
	$(PYTHON) scripts/fabriquer_pack.py deck

qa:
	$(PYTHON) scripts/qa_pptx.py . --max-iterations 5 --clean

tests:
	$(PYTHON) -m pytest tests/ -q

valider:
	$(PYTHON) validate.py

controles:
	bash .githooks/pre-commit --tout

verifier: tests valider controles

grille:
	$(PYTHON) scripts/generate_grille_audit.py
	cp 03-easy-checks/grille-audit-easy-checks.xlsx docs/assets/downloads/grille-audit-easy-checks.xlsx

sami:
	$(PYTHON) scripts/generate_exercice_sami.py

checklist:
	$(PYTHON) scripts/generate_exercice_sami.py --checklist

wcag:
	$(PYTHON) scripts/generate_wcag_langage_clair.py --condensed

pdf:
	$(PYTHON) scripts/fabriquer_pack.py pdf

supports:
	$(PYTHON) scripts/fabriquer_pack.py supports

outils:
	$(PYTHON) scripts/fabriquer_pack.py outils

outils-telecharger:
	$(PYTHON) scripts/fabriquer_pack.py outils --telecharger

fraicheur-pack:
	$(PYTHON) scripts/verifier_fraicheur_pack.py

pack:
	$(MAKE) pdf
	$(MAKE) fraicheur-pack
	$(MAKE) deck
	$(PYTHON) scripts/fabriquer_pack.py supports
	$(PYTHON) scripts/fabriquer_pack.py outils

apercu:
	bash recette/lancer-site-local.sh

recette:
	bash recette/recette-site-accessible.sh

publier-site:
	@test -d "$(SITE_CLONE)/.git" || { echo "Clone du site absent : git clone git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git $(SITE_CLONE)"; exit 1; }
	$(PYTHON) validate.py
	rsync -a --delete --exclude='.DS_Store' --exclude='*.md' --exclude='.git' docs/ "$(SITE_CLONE)/"
	cp publication-site/README.md "$(SITE_CLONE)/README.md"
	cp publication-site/agents-site.md "$(SITE_CLONE)/AGENTS.md"
	cp publication-site/claude-site.md "$(SITE_CLONE)/CLAUDE.md"
	git -C "$(SITE_CLONE)" add -A
	git -C "$(SITE_CLONE)" diff --cached --quiet || git -C "$(SITE_CLONE)" commit -m "Mise à jour du site depuis l'usine"
	git -C "$(SITE_CLONE)" push origin main
	@if [ -d "$(SITE_CONSULTATION)/.git" ]; then \
		if git -C "$(SITE_CONSULTATION)" pull --ff-only --quiet; then echo "Clone de consultation à jour : $(SITE_CONSULTATION)"; \
		else echo "Avertissement : clone de consultation non avancé ($(SITE_CONSULTATION)), vérifier qu'il n'a pas été modifié"; fi; \
	fi
