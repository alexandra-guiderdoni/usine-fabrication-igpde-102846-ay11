# Publier le site d'exercice

Le site des points de contrôle rapides est fabriqué dans `docs/` et publié par GitHub Pages depuis un dépôt séparé.

---

## Où il vit

- **Source** : `docs/` de cette usine (seule à modifier).
- **Dépôt publié** : `git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git`, branche `main`, racine `/`, mode legacy.
- **Adresse** : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/
- **Clone de travail** : `IGPDE-102846-livrables-octobre-2026/Formateur/tp-easy-check-site-web-igpde/`, ignoré par l'usine.

## Publier une modification

```bash
make publier-site
```

La commande valide le site (`validate.py`), synchronise `docs/` vers le clone (sans les fichiers `.md` internes ni `.DS_Store`), commite et pousse. GitHub Pages reconstruit le site en une à deux minutes.

Si le clone est absent :

```bash
git clone git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git IGPDE-102846-livrables-octobre-2026/Formateur/tp-easy-check-site-web-igpde
```

## Points de vigilance

- `docs/.nojekyll` doit rester présent : la synchronisation supprime dans le clone ce qui n'existe pas dans `docs/`, et sans ce fichier GitHub Pages filtre une partie des ressources.
- Le cache du navigateur garde une page jusqu'à 10 minutes : vérifier une publication avec un rechargement forcé (Cmd + Maj + R) ou une fenêtre privée.
- Les pages de `docs/` sont maintenues à la main. Relancer `scripts/generate_easy_checks_site_skeleton.py` écraserait les corrections faites depuis juillet : ne le faire qu'en relisant le diff complet.
- Le menu du site est le même sur toutes les pages : toute nouvelle entrée doit être ajoutée partout, et dans le générateur.

## Historique de l'hébergement

- **2026-05-15** : première publication depuis le dépôt personnel `Alexmacapple/easy-check-igpde` (https://alexmacapple.github.io/easy-check-igpde/), GitHub Pages en mode legacy, branche `main`, racine.
- **2026-09-27** : déménagement vers `alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11`, avec l'historique complet du site. L'ancienne adresse reste en ligne jusqu'après la session du 9 octobre 2026, puis sera décommissionnée.

Activer GitHub Pages sur un nouveau dépôt demande le droit administrateur : Settings > Pages, source « Deploy from a branch », branche `main`, dossier `/ (root)`.
