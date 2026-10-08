# Vérifications simples — Un premier bilan de l'accessibilité Web

Source : [W3C WAI — points de contrôle rapides](https://www.w3.org/WAI/test-evaluate/easy-checks/) (traduit de l'anglais)
Éditeurs : Kevin White, Andrew Arch, Shawn Lawton Henry

---

Cette page vous aide à commencer à évaluer l'accessibilité d'une page Web. Grâce à ces vérifications simples, vous pouvez déterminer si l'accessibilité est prise en compte, même de manière basique.

> **Avertissement** : ces vérifications ne couvrent que quelques problèmes d'accessibilité et sont conçues pour être rapides et faciles, plutôt qu'exhaustives. Une page Web peut sembler passer ces vérifications tout en présentant des obstacles significatifs à l'accessibilité. Une évaluation plus approfondie est nécessaire pour évaluer l'accessibilité de manière complète.

## Table des matières

1. [Texte alternatif des images](#1-texte-alternatif-des-images)
2. [Titre de page](#2-titre-de-page)
3. [Titres et hiérarchie](#3-titres-et-hiérarchie)
4. [Contraste des couleurs](#4-contraste-des-couleurs)
5. [Lien d'évitement](#5-lien-dévitement)
6. [Focus et navigation clavier](#6-focus-et-navigation-clavier)
7. [Langue de la page](#7-langue-de-la-page)
8. [Zoom à 200 %](#8-zoom-à-200-)
9. [Sous-titres vidéo](#9-sous-titres-vidéo)
10. [Transcriptions audio et vidéo](#10-transcriptions-audio-et-vidéo)
11. [Audiodescription](#11-audiodescription)
12. [Étiquettes de champs de formulaire](#12-étiquettes-de-champs-de-formulaire)
13. [Champs obligatoires et erreurs](#13-champs-obligatoires-et-erreurs)
14. [Index des liens](#index-des-liens)

---

## Vérifications courantes

### 1. Texte alternatif des images

#### Qu'est-ce que le texte alternatif des images ?

Le texte alternatif des images (« alt text ») est une courte description qui transmet l'objectif d'une image.

#### Pourquoi le texte alternatif est-il important ?

Le texte alternatif fournit des informations sur l'image aux personnes qui ne peuvent pas la voir ou qui peuvent avoir des difficultés à la comprendre. Cela inclut :

- Les personnes aveugles qui utilisent un lecteur d'écran pour accéder aux informations d'une page
- Les personnes malvoyantes qui agrandissent l'écran et utilisent également la synthèse vocale
- Certaines personnes ayant des troubles de l'apprentissage ou de la lecture qui se font lire les informations à haute voix

#### Ce qu'il faut vérifier

- Les images contenant des informations pertinentes pour le contenu de la page doivent avoir un texte alternatif décrivant ces informations importantes
- Les images contenant du texte doivent avoir ce texte dans le texte alternatif
- Les images décoratives doivent avoir un attribut alt vide
- Les images fonctionnelles (lien, bouton) doivent avoir un texte alternatif décrivant la page de destination ou la fonction du bouton
- Les images complexes (graphiques, diagrammes) doivent avoir un texte alternatif court décrivant le type d'image et un résumé du point clé, avec le détail décrit ailleurs sur la page ou sur une page séparée

#### Pour en savoir plus

- Astuce : [Rédiger des textes alternatifs pertinents pour les images](https://www.w3.org/WAI/tips/writing/#write-meaningful-text-alternatives-for-images)
- Tutoriel : [Images](https://www.w3.org/WAI/tutorials/images/) dans les tutoriels W3C
- [Comprendre le critère 1.1.1 : Contenu non textuel](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)

---

### 2. Titre de page

#### Qu'est-ce que le titre de page ?

Les titres de page sont :

- Affichés dans la barre de titre de la fenêtre de certains navigateurs
- Affichés dans les onglets des navigateurs lorsque plusieurs pages Web sont ouvertes
- Affichés dans les résultats des moteurs de recherche
- Utilisés pour les marque-pages/favoris du navigateur
- Lus par les lecteurs d'écran

#### Pourquoi le titre de page est-il important ?

Le titre de page est la première information énoncée par les lecteurs d'écran à l'ouverture d'une page. Il aide les utilisateurs de lecteurs d'écran à comprendre quelle page se charge. Les titres de page sont également reflétés dans les noms des onglets du navigateur et aident les utilisateurs à naviguer entre les onglets ouverts.

#### Ce qu'il faut vérifier

- Vérifier qu'il existe un titre qui décrit adéquatement et brièvement le contenu de la page
- Vérifier que le titre est différent de celui des autres pages du site

#### Conseils

Un bon titre de page place les informations importantes et uniques en premier (« front-loading »). Par exemple :

- Titres médiocres :
  - Bienvenue sur la page d'accueil de Solutions Web Acme, Inc.
  - Solutions Web Acme, Inc. - À propos
- Meilleurs titres :
  - Page d'accueil de Solutions Web Acme
  - À propos - Solutions Web Acme

#### Pour en savoir plus

- Astuce : [Fournir des titres de page informatifs et uniques](https://www.w3.org/WAI/tips/writing/#provide-informative-unique-page-titles)
- [Comprendre le critère 2.4.2 : Titre de page](https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html)

---

### 3. Titres et hiérarchie

#### Que sont les titres et la hiérarchie ?

Les titres communiquent l'organisation du contenu sur la page, comme une table des matières. Ils doivent être imbriqués par leur rang ou niveau, ce qui fournit un résumé de la structure et du contenu de la page.

Les titres peuvent avoir 6 niveaux (`<h1>` à `<h6>`) et doivent être imbriqués sans sauter de niveaux, comme la table des matières d'un livre. Les titres doivent être succincts et décrire la section de la page qui suit.

#### Pourquoi les titres et la hiérarchie sont-ils importants ?

Les titres servent de navigation dans la page pour de nombreuses personnes :

- Les utilisateurs de lecteurs d'écran peuvent sauter d'un titre à l'autre avec une seule touche et accéder à la structure des titres dans une boîte de dialogue pour un aperçu de la page
- Les personnes malvoyantes s'appuient souvent sur les titres visuellement plus grands pour comprendre les sujets et sous-sujets avant de zoomer pour lire le texte plus petit
- Les titres aident également les personnes ayant des troubles cognitifs, d'apprentissage ou de lecture à comprendre et se concentrer sur les sujets d'une page

#### Ce qu'il faut vérifier

- La page a-t-elle des titres ?
- La liste commence-t-elle par un H1 ?
- Des niveaux de titres sont-ils sautés ?
- Des niveaux de titres sont-ils vides (sans texte) ?
- Du texte ressemble-t-il à un titre sans être balisé comme tel ?
- Le texte du titre reflète-t-il le contenu qui suit ?
- Les titres représentent-ils la structure du contenu, en particulier le contenu imbriqué ?

#### Pour en savoir plus

- Astuce : [Utiliser les titres pour transmettre le sens et la structure](https://www.w3.org/WAI/tips/writing/#use-headings-to-convey-meaning-and-structure)
- Astuce : [Utiliser les titres et l'espacement pour regrouper le contenu associé](https://www.w3.org/WAI/tips/designing/#use-headings-and-spacing-to-group-related-content)
- Tutoriel : [Titres](https://www.w3.org/WAI/tutorials/page-structure/headings/)
- [Comprendre le critère 2.4.6 : Titres et étiquettes](https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html)

---

### 4. Contraste des couleurs

#### Qu'est-ce que le contraste des couleurs ?

Le contraste des couleurs fait référence au contraste entre :

- Le texte et la couleur de fond
- Les éléments interactifs (comme les indicateurs de focus) et leur arrière-plan
- Les éléments dans un graphique, un diagramme ou une carte qui doivent être compris

Techniquement, le contraste des couleurs est la luminance relative de deux couleurs ou plus l'une par rapport à l'autre, en particulier entre le texte et son arrière-plan.

#### Pourquoi le contraste des couleurs est-il important ?

Un bon contraste est important pour de nombreuses personnes malvoyantes qui ont une acuité de contraste réduite. Les personnes avec des déficiences de la vision des couleurs (« daltonisme ») ont souvent besoin d'un bon contraste également.

#### Ce qu'il faut vérifier

**Vérification rapide** : afficher la page en niveaux de gris pour repérer les problèmes de contraste.

**Vérification précise** : utiliser des outils qui calculent les rapports de contraste. Chercher « color » ou « colour » dans la [liste des outils d'évaluation](https://www.w3.org/WAI/ER/tools/).

#### Pour en savoir plus

- Astuce : [Fournir un contraste suffisant entre le premier plan et l'arrière-plan](https://www.w3.org/WAI/tips/designing/#provide-sufficient-contrast-between-foreground-and-background)
- [Comprendre le critère 1.4.3 : Contraste (minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)
- [Comprendre le critère 1.4.6 : Contraste (amélioré)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced)
- [Comprendre le critère 1.4.11 : Contraste du contenu non textuel](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)

---

### 5. Lien d'évitement

#### Qu'est-ce qu'un lien d'évitement ?

Les liens d'évitement aident les utilisateurs à passer rapidement au-delà de blocs de contenu qu'ils ne souhaitent pas parcourir. Le plus important est le lien d'évitement de la navigation : c'est un lien au début de la page qui permet aux utilisateurs de clavier d'accéder directement au contenu principal, en contournant les éléments de navigation communs (recherche, menu, etc.).

Idéalement, le lien d'évitement est visible dès le chargement de la page. Cependant, certains designers le masquent jusqu'à ce qu'il reçoive le focus clavier. C'est acceptable tant qu'il devient clairement visible au focus.

#### Pourquoi les liens d'évitement sont-ils importants ?

Un lien d'évitement en début de page permet aux personnes navigant au clavier d'accéder rapidement au contenu principal, en contournant la navigation. Cela inclut :

- Les utilisateurs de lecteurs d'écran
- Les personnes avec une dextérité réduite
- Les personnes avec divers handicaps moteurs
- Les personnes utilisant des baguettes buccales ou des pointeurs de tête
- Les personnes utilisant des contacteurs

#### Ce qu'il faut vérifier

- Vérifier que le premier lien interactif de la page permet de sauter au contenu principal
- Les formulations courantes incluent : « Aller au contenu », « Aller au contenu principal », « Passer la navigation »

#### Pour en savoir plus

- [Comprendre le critère 2.4.1 : Contourner des blocs](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html)

---

### 6. Focus et navigation clavier

#### Que sont le focus et la navigation clavier ?

Le focus clavier visible est un indicateur qui identifie l'élément interactif (lien, bouton, champ de formulaire) sur lequel on se trouve en utilisant la touche Tab. Le contrôle rapide couvre aussi le parcours au clavier : ordre logique, activation possible et absence de piège.

#### Pourquoi le focus et la navigation clavier sont-ils importants ?

Les personnes qui naviguent au clavier ou à la voix ont besoin d'une indication sur l'élément qui a le focus. De nombreux utilisateurs voyants ayant des handicaps physiques utilisent le clavier pour naviguer, notamment :

- Les personnes atteintes de tétraplégie
- Les personnes avec une dextérité limitée
- Les personnes avec des tremblements (maladie de Parkinson)

#### Ce qu'il faut vérifier

- Vérifier que tous les éléments interactifs ont un style visuel évident au focus
- Vérifier qu'aucun espace vide n'est mis en surbrillance (ce qui indiquerait un lien sans texte)

#### Pour en savoir plus

- Astuce : [S'assurer que les éléments interactifs sont faciles à identifier](https://www.w3.org/WAI/tips/designing/#ensure-that-interactive-elements-are-easy-to-identify)
- [Les fonctionnalités sont disponibles au clavier](https://www.w3.org/WAI/fundamentals/accessibility-principles/#keyboard)
- [Comprendre le critère 2.4.7 : Visibilité du focus](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible)

---

### 7. Langue de la page

#### Comment la langue est-elle identifiée ?

Les pages Web doivent identifier la langue principale de la page dans le code HTML.

#### Pourquoi l'identification de la langue est-elle importante ?

La langue de la page doit être déclarée pour que les lecteurs d'écran et les autres technologies qui convertissent le texte en voix de synthèse sachent comment prononcer correctement les mots.

#### Ce qu'il faut vérifier

- Vérifier que la langue principale est correctement identifiée
- Si aucune langue n'est définie, l'outil affichera : « La langue de la page n'est pas spécifiée »

Note : cette vérification ne détecte pas les changements de langue au sein d'une page.

#### Pour en savoir plus

- [Comprendre le critère 3.1.1 : Langue de la page](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html)
- [Comprendre le critère 3.1.2 : Langue d'un passage](https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts)

---

### 8. Zoom à 200 %

#### Qu'est-ce que le zoom ?

Le zoom est utilisé pour agrandir le texte et les images des pages Web afin de les rendre plus lisibles. Dans la plupart des navigateurs, « Ctrl » ou « Cmd » avec « + » augmente le zoom. « Ctrl » ou « Cmd » avec « - » réduit le zoom et « Ctrl » ou « Cmd » avec « 0 » le réinitialise.

#### Pourquoi le zoom est-il important ?

Le zoom est utilisé pour agrandir le texte et les autres éléments afin qu'ils deviennent lisibles pour les personnes malvoyantes. Certaines personnes n'ont besoin que d'un léger agrandissement, d'autres ont besoin d'agrandir jusqu'à 200 % ou plus.

#### Ce qu'il faut vérifier

- Redimensionner la fenêtre du navigateur de façon assez étroite
- Appuyer sur « Ctrl/Cmd » + « + » cinq fois pour atteindre un zoom de 200 %
- Vérifier que :
  - Tout le texte est toujours lisible
  - Le texte n'est pas masqué derrière d'autres textes ou images
  - Le défilement horizontal n'est pas nécessaire pour un contenu en écriture horizontale
  - Les menus de navigation peuvent se transformer en icône cliquable — c'est acceptable
- Activer le bookmarklet « 10.12 Espacement » et vérifier qu'aucun contenu n'est tronqué, masqué ou superposé

#### Pour en savoir plus

- [Comprendre le critère 1.4.4 : Redimensionnement du texte](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- [Comprendre le critère 1.4.10 : Redistribution](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [Comprendre le critère 1.4.12 : Espacement du texte](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)

---

## Vérifications audio/vidéo

### 9. Sous-titres vidéo

#### Que sont les sous-titres ?

Les sous-titres (« captions » en anglais) sont une version texte de la parole et des autres informations sonores nécessaires à la compréhension du contenu. Ils sont affichés dans le lecteur multimédia et synchronisés avec l'audio.

La plupart sont des sous-titres « fermés » qui peuvent être masqués ou affichés par l'utilisateur. Ils peuvent aussi être « ouverts » (toujours affichés et non désactivables).

#### Pourquoi les sous-titres sont-ils importants ?

Les sous-titres fournissent une version texte à l'écran des dialogues et autres sons pour les personnes sourdes ou malentendantes. Ils aident également certaines personnes ayant des troubles de l'apprentissage ou des difficultés de concentration à suivre la vidéo.

#### Ce qu'il faut vérifier

**Disponibilité :**

- Lancer la vidéo. Si des sous-titres apparaissent, ce sont peut-être des sous-titres ouverts
- Chercher un bouton de sous-titres dans le lecteur (souvent « [CC] »)
- Vérifier que les sous-titres sont disponibles dans la langue de l'audio
- Si seuls des sous-titres générés automatiquement sont disponibles, les sous-titres ne sont pas suffisants. [Pourquoi les sous-titres auto-générés ne suffisent pas](https://www.w3.org/WAI/media/av/captions/#automatic-captions-are-not-sufficient)

**Qualité :**

- Les sous-titres ont-ils une ponctuation et une capitalisation appropriées ?
- Les sous-titres sont-ils synchronisés avec le contenu parlé ?
- Si plusieurs personnes parlent, la personne qui parle est-elle identifiée ?
- Les autres sons importants (applaudissements, tonnerre, etc.) sont-ils inclus ?

#### Pour en savoir plus

- [Sous-titres, dans Rendre les médias audio et vidéo accessibles](https://www.w3.org/WAI/media/av/captions/)
- [Comprendre le critère 1.2.2 : Sous-titres (pré-enregistrés)](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html)

---

### 10. Transcriptions audio et vidéo

#### Que sont les transcriptions ?

Les **transcriptions de base** sont une version texte de la parole et des informations sonores non verbales nécessaires à la compréhension du contenu multimédia. Elles sont similaires aux sous-titres, mais dans un format qui peut être facilement ouvert et lu.

Les **transcriptions descriptives** pour les vidéos incluent également les informations visuelles nécessaires à la compréhension du contenu.

Pour les vidéos avec des informations visuelles et audio, idéalement une transcription descriptive est fournie, et une transcription de base séparée n'est pas nécessaire.

#### Pourquoi les transcriptions sont-elles importantes ?

Les transcriptions sont importantes pour les personnes sourdaveugles. Les utilisateurs de lecteurs d'écran peuvent également préférer la transcription à l'écoute de l'audio.

#### Ce qu'il faut vérifier

- Vérifier la présence d'une transcription avec le média ou d'un lien vers une transcription
- Les transcriptions doivent être faciles à trouver à proximité de l'audio ou de la vidéo
- Si la vidéo contient du contenu visuel important, vérifier qu'il est décrit dans la transcription

**Qualité :**

- Tout le discours est-il fidèlement reflété dans la transcription ?
- Tous les locuteurs sont-ils identifiés ?
- Tous les autres sons sont-ils décrits (« applaudissements légers », « crissement de pneus ») ?
- Tout le contenu visuel important est-il décrit dans la transcription ?

#### Pour en savoir plus

- [Transcriptions, dans Rendre les médias audio et vidéo accessibles](https://www.w3.org/WAI/media/av/transcripts/)
- [Comprendre le critère 1.2.8 : Version de remplacement pour un média temporel (pré-enregistré)](https://www.w3.org/WAI/WCAG22/Understanding/media-alternative-prerecorded.html)

---

### 11. Audiodescription

#### Qu'est-ce que l'audiodescription ?

La description des informations visuelles est appelée « audiodescription », « vidéodescription » ou « vidéo décrite » selon les pays. L'audiodescription explique les informations visuelles nécessaires à la compréhension du contenu vidéo. Par exemple : « Pat ouvre une petite boîte, regarde une bague de fiançailles en diamant et pleure. »

L'audiodescription peut être fournie sous forme de :

- **Description intégrée** : la description est incluse dans les scripts des intervenants principaux
- **Vidéo alternative** : la description est incluse dans une vidéo séparée
- **Fichier séparé** : la description est dans un fichier texte synchronisé supporté par le lecteur multimédia

#### Pourquoi l'audiodescription est-elle importante ?

L'audiodescription est importante pour les personnes qui ne peuvent pas voir la vidéo de manière adéquate, y compris les personnes aveugles et certaines personnes malvoyantes.

#### Ce qu'il faut vérifier

1. Déterminer si la description est nécessaire : y a-t-il des éléments visuels importants pour comprendre la vidéo ?
2. Si oui, vérifier si une description est fournie :
   - Les informations visuelles importantes sont-elles incluses dans l'audio principal ? L'intervenant explique-t-il les informations visuelles ?
   - Une vidéo décrite séparée est-elle disponible ?
3. Généralement, tout le texte dans la vidéo doit être inclus dans l'audio principal ou une description séparée (titres au début, liens et adresses e-mail à la fin, noms des intervenants, texte dans une présentation)

#### Pour en savoir plus

- [Description des informations visuelles, dans Rendre les médias audio et vidéo accessibles](https://www.w3.org/WAI/media/av/description/)
- [Comprendre le critère 1.2.5 : Audiodescription (pré-enregistrée)](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)

---

## Vérifications des formulaires

### 12. Étiquettes de champs de formulaire

#### Que sont les étiquettes de champs de formulaire ?

Les étiquettes de champs de formulaire sont le texte à côté ou au-dessus des champs de formulaire. Elles doivent indiquer quelles informations saisir ou quelle case à cocher sélectionner.

#### Pourquoi les étiquettes de champs sont-elles importantes ?

Les étiquettes correctement codées sont importantes pour que les personnes utilisant un lecteur d'écran sachent comment remplir un formulaire. Les personnes avec une dextérité réduite utilisant une souris ont besoin que l'étiquette visuelle soit associée au champ de formulaire dans le code pour créer une zone cliquable plus grande, en particulier pour les boutons radio et les cases à cocher.

#### Ce qu'il faut vérifier

- Cliquer sur une étiquette : si le champ de formulaire est correctement codé, il devrait recevoir le focus clavier
- Vérifier qu'il n'y a pas de champs marqués « Étiquette manquante »
- Vérifier les étiquettes marquées « Étiqueté (via ARIA) » : ce n'est pas une erreur mais c'est moins utile qu'une étiquette `<label>` standard

#### Pour en savoir plus

- Astuce : [S'assurer que les éléments de formulaire incluent des étiquettes clairement associées](https://www.w3.org/WAI/tips/designing/#ensure-that-form-elements-include-clearly-associated-labels)
- Astuce : [Associer une étiquette à chaque contrôle de formulaire](https://www.w3.org/WAI/tips/developing/#associate-a-label-with-every-form-control)
- Tutoriel : [Étiquetage des contrôles](https://www.w3.org/WAI/tutorials/forms/labels/)
- [Comprendre le critère 3.3.2 : Étiquettes ou instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)

---

### 13. Champs obligatoires et erreurs

#### Qu'est-ce qu'un champ obligatoire ?

Un champ de formulaire obligatoire doit être rempli avant de soumettre le formulaire.

La meilleure façon d'indiquer un champ obligatoire est d'inclure le mot « obligatoire » dans l'étiquette. De nombreux formulaires utilisent un astérisque rouge « * » dans l'étiquette, mais celui-ci n'est souvent pas annoncé par les lecteurs d'écran (car considéré comme de la ponctuation) et peut être manqué par les personnes malvoyantes en raison de sa petite taille.

Certains formulaires ne marquent pas les champs obligatoires mais indiquent que tous les champs sont obligatoires sauf ceux marqués « optionnel ».

#### Pourquoi les champs obligatoires sont-ils importants ?

Indiquer visuellement les champs obligatoires est important pour que tout le monde sache quelles parties du formulaire doivent être remplies.

#### Ce qu'il faut vérifier

- Vérifier que les champs marqués comme obligatoires ont un indicateur visuel
- Si les champs sont marqués « optionnel » plutôt qu'« obligatoire », vérifier qu'un message indique que tous les champs sont obligatoires sauf indication contraire
- Soumettre le formulaire et vérifier que les champs attendus comme obligatoires sont bien signalés

#### Pour en savoir plus

- Astuce : [Fournir des instructions claires](https://www.w3.org/WAI/tips/writing/#provide-clear-instructions)
- [Comprendre le critère 3.3.2 : Étiquettes ou instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html)

---

## Index des liens

| # | Texte du lien | URL |
|---|---------------|-----|
| 1 | Rédiger des textes alternatifs pertinents pour les images | https://www.w3.org/WAI/tips/writing/#write-meaningful-text-alternatives-for-images |
| 2 | Tutoriel : Images | https://www.w3.org/WAI/tutorials/images/ |
| 3 | Comprendre 1.1.1 : Contenu non textuel | https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html |
| 4 | Fournir des titres de page informatifs et uniques | https://www.w3.org/WAI/tips/writing/#provide-informative-unique-page-titles |
| 5 | Comprendre 2.4.2 : Titre de page | https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html |
| 6 | Utiliser les titres pour transmettre le sens et la structure | https://www.w3.org/WAI/tips/writing/#use-headings-to-convey-meaning-and-structure |
| 7 | Utiliser les titres et l'espacement pour regrouper le contenu | https://www.w3.org/WAI/tips/designing/#use-headings-and-spacing-to-group-related-content |
| 8 | Tutoriel : Titres | https://www.w3.org/WAI/tutorials/page-structure/headings/ |
| 9 | Comprendre 2.4.6 : Titres et étiquettes | https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html |
| 10 | Fournir un contraste suffisant | https://www.w3.org/WAI/tips/designing/#provide-sufficient-contrast-between-foreground-and-background |
| 11 | Comprendre 1.4.3 : Contraste (minimum) | https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum |
| 12 | Comprendre 1.4.6 : Contraste (amélioré) | https://www.w3.org/WAI/WCAG22/Understanding/contrast-enhanced |
| 13 | Comprendre 1.4.11 : Contraste du contenu non textuel | https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html |
| 14 | Liste des outils d'évaluation | https://www.w3.org/WAI/ER/tools/ |
| 15 | Comprendre 2.4.1 : Contourner des blocs | https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html |
| 16 | Éléments interactifs faciles à identifier | https://www.w3.org/WAI/tips/designing/#ensure-that-interactive-elements-are-easy-to-identify |
| 17 | Fonctionnalités disponibles au clavier | https://www.w3.org/WAI/fundamentals/accessibility-principles/#keyboard |
| 18 | Comprendre 2.4.7 : Visibilité du focus | https://www.w3.org/WAI/WCAG22/Understanding/focus-visible |
| 19 | Comprendre 3.1.1 : Langue de la page | https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html |
| 20 | Comprendre 3.1.2 : Langue d'un passage | https://www.w3.org/WAI/WCAG22/Understanding/language-of-parts |
| 21 | Comprendre 1.4.4 : Redimensionnement du texte | https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html |
| 22 | Sous-titres auto-générés insuffisants | https://www.w3.org/WAI/media/av/captions/#automatic-captions-are-not-sufficient |
| 23 | Sous-titres (Making Audio and Video Accessible) | https://www.w3.org/WAI/media/av/captions/ |
| 24 | Comprendre 1.2.2 : Sous-titres (pré-enregistrés) | https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html |
| 25 | Transcriptions (Making Audio and Video Accessible) | https://www.w3.org/WAI/media/av/transcripts/ |
| 26 | Comprendre 1.2.8 : Version de remplacement | https://www.w3.org/WAI/WCAG22/Understanding/media-alternative-prerecorded.html |
| 27 | Expériences utilisateurs et bénéfices | https://www.w3.org/WAI/media/av/users-orgs/ |
| 28 | Description des informations visuelles | https://www.w3.org/WAI/media/av/description/ |
| 29 | Comprendre 1.2.5 : Audiodescription (pré-enregistrée) | https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html |
| 30 | Étiquettes clairement associées aux formulaires | https://www.w3.org/WAI/tips/designing/#ensure-that-form-elements-include-clearly-associated-labels |
| 31 | Associer une étiquette à chaque contrôle | https://www.w3.org/WAI/tips/developing/#associate-a-label-with-every-form-control |
| 32 | Tutoriel : Étiquetage des contrôles | https://www.w3.org/WAI/tutorials/forms/labels/ |
| 33 | Comprendre 3.3.2 : Étiquettes ou instructions | https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html |
| 34 | Fournir des instructions claires | https://www.w3.org/WAI/tips/writing/#provide-clear-instructions |
