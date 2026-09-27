# TP en ligne - formation accessibilité numérique IGPDE

Site statique des travaux pratiques de la formation « L'accessibilité numérique pour la bureautique et le web » de l'IGPDE (code 102846), publié par GitHub Pages.

---

## Accéder aux TP

- **Site d'exercice des points de contrôle rapides** : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/
  - trois versions du même site : à auditer (défauts volontaires), aide à la correction (mêmes pages avec des indices), corrigée (témoin sobre) ;
  - treize pages, une par point de contrôle rapide du W3C : images, titre de page, titres, contraste, liens d'évitement, clavier et focus, langue, zoom, sous-titres, transcription, audiodescription, étiquettes de formulaire, champs obligatoires et erreurs ;
  - grille d'audit au format XLSX, téléchargeable depuis la page d'accueil.
- **Démo émojis et lecteurs d'écran** : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/demo-mauvaise-restitution-emojis.html
  - trois publications de réseaux sociaux où les émojis portent le sens, avec leur restitution possible par un lecteur d'écran et leur version corrigée ;
  - un exercice de réécriture d'une publication institutionnelle ;
  - aussi accessible depuis le menu « Démo #RS » du site d'exercice.

## Contenu du dépôt

- `index.html` : page d'accueil de l'exercice.
- `site-inaccessible/`, `site-aide-correction/`, `site-accessible/` : les trois versions du site à auditer.
- `demo-mauvaise-restitution-emojis.html` : démo émojis et lecteurs d'écran.
- `accessibilite.html`, `mentions-legales.html`, `donnees-personnelles.html`, `plan-du-site.html` : pages légales.
- `assets/` : Système de design de l'État (DSFR), images, vidéos et audio des exercices, grille d'audit.
- `AGENTS.md`, `CLAUDE.md` : consignes pour les agents d'IA, qui les renvoient vers l'usine.

Le site est statique : les formulaires d'exercice rechargent simplement la page, aucune donnée n'est traitée ni enregistrée par le site.

## Ne pas modifier ce dépôt directement

Ce dépôt est une copie de publication. La source du site est le dossier `docs/` de l'usine de fabrication de la formation :

https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11

Toute modification se fait dans l'usine, puis se publie depuis celle-ci avec `make publier-site`, qui valide le site avant de l'envoyer ici. Une modification faite directement dans ce dépôt serait écrasée à la publication suivante.

## L'usine de fabrication

L'usine fabrique, à partir de sources versionnées, tous les supports de la formation :

- le deck de 138 slides au format DSFR, généré par des scripts ;
- ce site d'exercice et la démo ;
- l'exercice Word (trois documents) et la grille d'audit ;
- les fiches PDF accessibles (mémos Word et LibreOffice, fiches WCAG, fiche des liens des TP) ;
- le pack livrable remis à l'IGPDE.

Pour aller plus loin :

- [Présentation et installation de l'usine](https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11/blob/main/README.md)
- [Protocole de travail, pour un humain comme pour un agent](https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11/blob/main/AGENTS.md)
- [Publier le site](https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11/blob/main/PUBLIER-SITE.md)
- [Source du site (`docs/`)](https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11/tree/main/docs)

## Accessibilité

Le site est déclaré **non conforme** au RGAA, volontairement : les versions « à auditer » et « aide à la correction » contiennent des erreurs pédagogiques que les stagiaires doivent trouver. Seule la version corrigée sert de témoin. Détail dans la [déclaration d'accessibilité](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/accessibilite.html).

## Historique

- 2026-05-15 : première publication, sous le compte personnel `Alexmacapple` (dépôt `easy-check-igpde`).
- 2026-09-27 : déménagement dans ce dépôt, avec l'historique complet du site. L'ancien dépôt a été supprimé : seule l'adresse ci-dessus est valable.

## Licence

Contenus publiés sous la Licence Ouverte 2.0 (etalab-2.0), voir la [licence de l'usine](https://github.com/alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11/blob/main/LICENSE).
