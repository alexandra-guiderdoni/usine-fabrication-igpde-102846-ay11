# Site Easy Check IGPDE - consignes locales

Ce dossier `docs/` est la source du site d'exercice : c'est ici, et nulle part ailleurs, qu'on modifie le site. Les règles complètes sont dans l'`AGENTS.md` de l'usine, section « Deux dépôts liés ».

- Publier une modification : depuis la racine de l'usine, `make verifier` puis `make publier-site`.
- Ne jamais modifier les clones du dépôt publié (`livrables-IGPDE-2026-102846/Formateur/tp-easy-check-site-web-igpde/` dans l'usine, et `tp-fabrication-igpde-102846-ay11/` à côté de l'usine) : ils sont écrasés à chaque publication.
- Les fichiers `.md` de ce dossier ne sont pas publiés.
- Pages maintenues à la main : ne pas relancer `scripts/generate_easy_checks_site_skeleton.py` sans relire le diff complet.

Dépôt publié : https://github.com/alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11 (remote `git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git`).

Adresse publique : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/
