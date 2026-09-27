# Site des TP IGPDE 102846 - consignes pour les agents

Ce dépôt est une copie de publication, pas une source. Tout agent (Claude, Codex ou autre) qui l'ouvre doit aller travailler dans l'usine.

## Règle

- **MUST NOT** : modifier, commiter ou pousser quoi que ce soit ici. Chaque publication resynchronise ce dépôt avec suppression : une modification faite ici serait effacée, et un commit poussé d'ici ferait échouer la publication suivante.
- **MUST** : faire toute modification dans l'usine, puis la publier depuis l'usine.

## Où est l'usine

- En ligne : https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11
- En local, selon le clone ouvert :
  - clone de consultation `tp-fabrication-igpde-102846-ay11/` : l'usine est le dossier voisin `../usine-fabrication-igpde-102846-ay11/` ;
  - clone de publication `tp-easy-check-site-web-igpde/`, rangé dans le pack livrable : l'usine est trois niveaux au-dessus (`../../../`).
- Protocole de travail : l'`AGENTS.md` de l'usine, section « Deux dépôts liés ».

## Correspondance des fichiers

- Chaque fichier de ce dépôt vient de `docs/<même chemin>` dans l'usine.
- `README.md`, `AGENTS.md` et `CLAUDE.md` viennent de `publication-site/` dans l'usine, où ils s'appellent `README.md`, `agents-site.md` et `claude-site.md`.

## Modifier le site

Dans l'usine : éditer `docs/`, lancer `make verifier`, puis `make publier-site`. La commande valide le site, met à jour ce dépôt, le pousse et avance le clone de consultation. GitHub Pages reconstruit le site en une à deux minutes : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/

## Lire ce dépôt

Un clone local peut être en retard. Avant d'en tirer une conclusion, lancer `git pull --ff-only`, ou lire directement `docs/` dans l'usine.
