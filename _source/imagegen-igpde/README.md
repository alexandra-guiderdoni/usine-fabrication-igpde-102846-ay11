# Preset ImageGen IGPDE Accessibilité

Ce dossier est la source de vérité du style d'images de slides validé à partir de la présentation « Publier de façon accessible sur les réseaux sociaux », version 4.

Il complète le workflow générique du skill `generer-images-slides-ia`. Il ne remplace ni les sources pédagogiques du deck, ni la matrice PowerPoint, ni la matrice de publication HTML.

## Déclenchement obligatoire

Pour toute demande de génération, régénération ou extension d'images de slides IGPDE avec ImageGen ou Imagine, l'agent doit, avant de rédiger un prompt :

1. lire le présent fichier ;
2. lire [guide-style.md](guide-style.md) et [style-preset.yml](style-preset.yml) ;
3. lire [prompt-base.md](prompt-base.md) et [storyboard-template.md](storyboard-template.md) ;
4. inspecter en résolution originale les images de [references/](references/) correspondant aux familles de mise en page utiles ;
5. lire les slides PPTX sources et le corpus métier concerné ;
6. appliquer le workflow du skill `generer-images-slides-ia`.

Le pointeur placé dans `AGENTS.md` rend cette lecture obligatoire pour tous les agents qui travaillent dans le dépôt.

## Hiérarchie des sources

En cas de divergence, appliquer cet ordre :

1. demande explicite de l'utilisateur ;
2. contenu et ordre du PPTX source ;
3. présent preset IGPDE ;
4. workflow du skill `generer-images-slides-ia` ;
5. conventions génériques d'un outil de génération.

Le preset local prévaut donc sur le guide visuel générique du skill. En particulier, cette famille accepte les dégradés bleus très légers et les cartes aux angles arrondis observés dans les références.

Le skill historique `style-igpde` ne convient pas à cette famille : il produit un tableau blanc dessiné en `680x383` avec ERNIE et Pillow. Ne l'utiliser que si l'utilisateur demande explicitement ce style historique.

## Fichiers du kit

- `guide-style.md` : contrat visuel expliqué et critères de cohérence ;
- `style-preset.yml` : version structurée du contrat, facile à relire par une machine ;
- `prompt-base.md` : socle à reprendre dans chaque prompt ImageGen ;
- `storyboard-template.md` : fiche de conception et de contrôle d'une slide ;
- `references/` : quatre images étalons issues de la V4 publiée.

## Workflow d'une nouvelle série

### 1. Établir la correspondance avec le PPTX

- identifier la section exacte du deck ;
- conserver l'ordre pédagogique ;
- produire une ligne de storyboard par slide source ;
- distinguer le texte visible, la transcription descriptive et le discours oral ;
- ne rien inventer pour remplir une composition.

### 2. Définir la série

- choisir une colonne vertébrale narrative ;
- affecter une famille de mise en page à chaque slide ;
- définir un masque commun : titre, marges, couleurs, cartes, callout et progression ;
- inscrire une liste blanche exacte de tous les textes visibles ;
- inscrire les critères de rejet propres à chaque slide.

### 3. Produire les étalons

Pour une série de plus de quatre slides, générer d'abord quatre étalons représentatifs :

- ouverture ou chapitre ;
- explication, processus ou comparaison ;
- contenu structuré ou tableau ;
- synthèse ou checklist.

Faire valider explicitement ces étalons avant une génération massive. Une validation porte sur la famille visuelle, pas seulement sur l'absence de faute.

### 4. Générer avec ImageGen

- créer avant le premier appel `outputs/ia-slides/YYYY-MM-DD-nom-serie/` ;
- copier `storyboard-template.md` dans ce dossier sous le nom `storyboard.md`, puis le remplir ;
- utiliser réellement `image_gen` ou Imagine ;
- transmettre le prompt complet, le texte exact et les références utiles ;
- copier chaque candidate sous `slide-XX.png` sans écraser une version acceptée ;
- ne jamais substituer silencieusement HTML, SVG, Pillow ou PowerPoint à ImageGen.

### 5. Contrôler chaque image

- inspecter l'image seule puis en résolution originale ;
- vérifier tous les caractères, accents, nombres et libellés ;
- refuser tout texte parasite, faux logo, pictogramme ambigu ou contresens ;
- vérifier le test des trois secondes : sujet, objet, action et bénéfice doivent être compris rapidement ;
- corriger uniquement les slides fautives, sans relancer la série acceptée.

### 6. Conserver les preuves

Chaque série doit contenir au minimum :

```text
outputs/ia-slides/YYYY-MM-DD-nom-serie/
├── storyboard.md
├── slide-01.png
├── slide-02.png
├── prompts/
├── imagegen-receipt.tsv
└── contact-sheet.png
```

Le reçu relie chaque image finale à son appel ImageGen, sa source de cache, sa copie projet, son inspection et sa décision. Les prompts doivent être exportés après le dernier remplacement.

### 7. Transmettre au support cible

Une fois les images acceptées :

- copier les images retenues dans le projet qui les publie ou les empaquette ;
- y copier le storyboard définitif sous `<jeu>/source/storyboard.md` ainsi que les prompts utiles à la traçabilité ;
- appliquer les règles propres au dépôt cible ;
- ne pas commiter, pousser ou publier sans l'autorité correspondante.

## Critère de fin

Une série est prête à être transmise seulement si :

- les étalons ont été validés ;
- toutes les images finales proviennent d'ImageGen ou portent une déviation explicite ;
- la planche-contact et au moins une image en pleine résolution par famille ont été inspectées ;
- les textes visibles correspondent à leur liste blanche ;
- les prompts et le reçu sont présents ;
- les alternatives, transcriptions et discours oraux restent distincts dans le support de publication.
