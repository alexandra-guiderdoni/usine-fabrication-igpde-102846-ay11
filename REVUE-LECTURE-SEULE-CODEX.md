---
type: Concept
title: "Passation de la revue Codex en lecture seule"
description: "Constats statiques sur l'usine de fabrication IGPDE, à transmettre à Claude."
tags: [revue, passation, lecture-seule]
timestamp: "2026-09-27"
---

# Passation de la revue Codex en lecture seule

## Périmètre et méthode

Revue statique effectuée depuis la racine de l'usine, sans exécuter de
générateur, de test, de publication ni de commande Git mutante.

Les affirmations ci-dessous proviennent des fichiers de consigne, du `Makefile`
et des scripts directement concernés. Les binaires PPTX et DOCX n'ont pas été
ouverts : aucun constat ne dépend de leur contenu interne.

## Réponses opérationnelles

- **Coquille dans une slide** : ne pas retoucher le PPTX dans PowerPoint. Modifier
  `scripts/slides/NN_*.py`, puis lancer `make deck`. Sources : `AGENTS.md:35-40`,
  `REEXPORTER-DECK-PPTX.md:10`.

- **Mise à jour du site** : modifier les pages dans `docs/`. Ne pas relancer
  `scripts/generate_easy_checks_site_skeleton.py` sans nécessité exceptionnelle
  et relecture intégrale du diff, car le générateur réécrit `docs/`. Sources :
  `AGENTS.md:23,43`, `scripts/generate_easy_checks_site_skeleton.py:2321-2352`.

- **Portée de `make pack`** : la cible régénère le deck, les PDF, les supports
  et vérifie les outils, mais ne relance ni `make sami` ni `make grille`. Les
  DOCX Sami existants sont seulement copiés dans le pack. Sources :
  `AGENTS.md:47-55`, `Makefile:73-74`, `scripts/pack_supports.py:54-58`.

- **Constante du haut de la zone de contenu** : `TOP_CONTENT`, à `2.68`.
  Source : `scripts/igpde_dsfr_components.py:76`.

- **QR code** : le composant `add_qrcode(...)` existe. Il produit aussi un appel
  à l'action et une URL visible. Source :
  `scripts/igpde_dsfr_components.py:1128-1191`.

- **Horaires de session dans `todo.md`** : ne pas les ajouter. La logistique de
  session doit rester hors du dépôt public. Source : `AGENTS.md:83`.

- **Chemins d'images des mémos** : les conserver relatifs dans les Markdown.
  `scripts/pack_supports.py` ne les rend absolus que dans une copie temporaire
  utilisée pour le PDF. Sources : `fiche-pratique/README.md:80`,
  `scripts/pack_supports.py:95-107`.

- **Deck et Git** : Git ne génère pas le deck. Le PPTX généré à la racine est
  ignoré ; la copie placée dans le pack est suivie. Sources : `.gitignore:17`,
  `contraintes.md:152-154`.

- **Liste des commandes** : `make aide`. Source : `Makefile:11-26`.

- **Date de session** : si la question tronquée concernait la date, la modifier
  dans `config.yml:3`. La partie demandant un éventuel générateur n'était pas
  assez complète pour recevoir une réponse fiable.

## Écarts documentaires vérifiés

### 1. Portée trop large de « source unique »

**Gravité : moyenne.** `AGENTS.md:8` et `README.md:16` présentent `config.yml`
comme l'unique fichier à modifier pour une nouvelle session. C'est exact pour
les paramètres consommés par l'exécution, mais pas pour toute la documentation :
`REEXPORTER-DECK-PPTX.md:3` nomme le deck courant et `contraintes.md:290`
demande explicitement de rechercher les références périmées dans les Markdown
structurants. Risque : une passation peut laisser des consignes de session
obsolètes.

### 2. Règle « tout passe par make » et exceptions directes

**Gravité : faible.** `AGENTS.md:31` dit que toutes les commandes passent par
`make`, mais `AGENTS.md:40` et `REEXPORTER-DECK-PPTX.md:54,57,99` prescrivent
des appels Python directs. Le `Makefile` ne fournit pas les équivalents
paramétrés de ces diagnostics. La règle devrait distinguer les commandes
standard des exceptions documentées.

### 3. Repli d'interpréteur incomplet dans la documentation

**Gravité : faible.** `AGENTS.md:31` indique qu'en l'absence de `.venv`,
le `Makefile` utilise Python 3.12 Homebrew. Or `Makefile:4` prévoit aussi un
repli sur `python3` lorsque cet interpréteur n'est pas disponible. Risque :
l'environnement réellement utilisé peut différer de celui annoncé.

### 4. Limite de zone de contenu divergente dans un commentaire source

**Gravité : faible.** Le commentaire de
`scripts/igpde_dsfr_components.py:4` donne une zone de contenu allant jusqu'à
`6.97`, alors que `BOTTOM_CONTENT = 6.80` dans le même fichier (`:78`) et que
`AGENTS.md:103` fixe la même limite. `6.97` correspond à la ligne séparatrice,
pas à la limite de contenu.

## Limites à conserver

- La revue prouve des incohérences de texte et de configuration par inspection
  statique ; elle ne prouve pas un rendu visuel PowerPoint, la génération du
  pack, la réussite des tests ou la publication web.
- Aucun fichier existant n'a été modifié. Ce document est la seule addition de
  cette passation.
