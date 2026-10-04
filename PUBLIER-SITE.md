# Publier le site d'exercice

Le site des points de contrôle rapides est fabriqué dans `docs/` et publié par GitHub Pages depuis un dépôt séparé.

---

## Où il vit

- **Source** : `docs/` de cette usine (seule à modifier), et `publication-site/` pour le `README.md`, l'`AGENTS.md` et le `CLAUDE.md` du dépôt publié (sources : `README.md`, `agents-site.md`, `claude-site.md`, renommés à la copie). Ces deux derniers renvoient vers l'usine tout agent qui ouvre un clone du site.
- **Dépôt publié** : `git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git`, branche `main`, racine `/`.
- **Adresse** : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/
- **Clone de publication** : `livrables-IGPDE-2026-102846/Livrables-Stagiaires/tp-easy-check-site-web-igpde/`, ignoré par l'usine, écrit par `make publier-site` (variable `SITE_CLONE`).
- **Clone de consultation** : `../tp-fabrication-igpde-102846-ay11/`, à côté de l'usine, facultatif, avancé à la fin de `make publier-site` (variable `SITE_CONSULTATION`).
- Les deux clones sont en lecture seule : ne jamais y modifier, commiter ni pousser quoi que ce soit.

## Publier une modification

```bash
make verifier
make publier-site
```

Lancer `make publier-site` uniquement après le succès de `make verifier`, qui exécute les tests, la validation du site et les contrôles du dépôt. La commande de publication revalide ensuite le site (`validate.py`), effectue la synchronisation de `docs/` vers le clone (sans les fichiers `.md` internes ni `.DS_Store`), copie les trois fichiers de `publication-site/` à la racine du clone, commite et pousse, puis avance le clone de consultation s'il existe. Ces fichiers sont publics, et GitHub Pages les sert aussi en texte brut : n'y mettre que des informations publiables.

Si le clone est absent :

```bash
git clone git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git livrables-IGPDE-2026-102846/Livrables-Stagiaires/tp-easy-check-site-web-igpde
```

## Points de vigilance

- `docs/.nojekyll` doit rester présent : la synchronisation efface dans le clone ce qui n'existe pas dans `docs/`, et sans ce fichier GitHub Pages filtre une partie des ressources.
- Le cache du navigateur peut conserver une page jusqu'à 10 minutes : attendre la mise à disposition du site, puis vérifier une publication avec un rechargement forcé (Cmd + Maj + R) ou une fenêtre privée.
- Les pages de `docs/` sont maintenues à la main. Relancer `scripts/generate_easy_checks_site_skeleton.py` écraserait les corrections faites depuis juillet : ne le faire qu'en relisant le diff complet.
- Le menu du site est le même sur toutes les pages : toute nouvelle entrée doit être ajoutée partout, et dans le générateur.

## Historique de l'hébergement

- **2026-05-15** : première publication depuis le dépôt personnel `Alexmacapple/easy-check-igpde` (https://alexmacapple.github.io/easy-check-igpde/), branche `main`, racine.
- **2026-09-27** : déménagement vers `alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11`, avec l'historique complet du site et l'étiquette `site-2026-07-04`. Le dépôt `Alexmacapple/easy-check-igpde` a été supprimé le même jour : l'ancienne adresse ne répond plus.

Activer GitHub Pages sur un nouveau dépôt demande le droit administrateur : Settings > Pages, source « Deploy from a branch », branche `main`, dossier `/ (root)`.
