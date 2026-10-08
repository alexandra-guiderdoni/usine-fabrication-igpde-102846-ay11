# Vérifications rapides d'accessibilité (points de contrôle rapides)

Guide basé sur les points de contrôle rapides du W3C WAI, traduit en français avec les équivalences RGAA 4.1.2.

Source : https://www.w3.org/WAI/test-evaluate/easy-checks/

---

## Vérifications de base

### 1. Texte alternatif des images

**Résumé** : Le texte alternatif (« alt text ») est une courte description qui communique la finalité d'une image. Il est utilisé par les personnes qui ne voient pas l'image.

**Pourquoi c'est important** : Le texte alternatif est indispensable pour :

- Les personnes aveugles qui utilisent un lecteur d'écran pour accéder au contenu
- Les personnes malvoyantes qui agrandissent l'écran et utilisent la synthèse vocale
- Certaines personnes ayant des troubles de l'apprentissage ou de la lecture qui bénéficient de l'information audio

**Comment vérifier** :

1. Ouvrir la barre de favoris du navigateur (Ctrl/Cmd+Maj+B)
2. Glisser le bookmarklet « Check images » dans la barre de favoris
3. Se rendre sur la page à évaluer
4. Cliquer sur le bookmarklet

**Ce qu'il faut vérifier** :

- **Alt manquant** : les images porteuses d'information doivent avoir une alternative
- **Images décoratives** : doivent avoir un attribut alt vide (`alt=""`)
- **Images fonctionnelles** : les liens ou boutons-images doivent décrire la destination ou la fonction
- **Images complexes** : les graphiques et diagrammes nécessitent une description brève et une description détaillée ailleurs sur la page

**Critère WCAG** : 1.1.1 Contenu non textuel

**Équivalences RGAA** :

- 1.1 — Chaque image porteuse d'information a-t-elle une alternative textuelle ?
- 1.2 — Chaque image de décoration est-elle correctement ignorée par les technologies d'assistance ?
- 1.3 — Pour chaque image porteuse d'information ayant une alternative textuelle, cette alternative est-elle pertinente ?
- 1.6 — Chaque image porteuse d'information a-t-elle, si nécessaire, une description détaillée ?
- 1.7 — Pour chaque image porteuse d'information ayant une description détaillée, cette description est-elle pertinente ?
- 1.8 — Chaque image texte porteuse d'information, en l'absence d'un mécanisme de remplacement, doit-elle être remplacée par du texte stylé ?
- 1.9 — Chaque image porteuse d'information a-t-elle, si nécessaire, une alternative textuelle structurée ?

---

### 2. Titre de page

**Résumé** : Les titres de page s'affichent dans la barre de titre ou l'onglet du navigateur. Ils sont la première chose lue par les lecteurs d'écran et aident les utilisateurs à savoir où ils se trouvent.

**Pourquoi c'est important** : Le titre de page est la première information annoncée par les lecteurs d'écran à l'ouverture d'une page. Il aide à comprendre quelle page se charge. Les titres dans les onglets du navigateur aident également à naviguer entre les pages ouvertes.

**Comment vérifier** :

1. Glisser le bookmarklet « Check page title » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet

**Ce qu'il faut vérifier** :

- Un titre existe et décrit brièvement le contenu de la page
- Le titre est différent de celui des autres pages du site
- L'information unique et importante est placée en premier (« front-loading »)

**Bonnes pratiques** :

- Mauvais : « Bienvenue sur le site de Acme Solutions »
- Bon : « Acme Solutions — Accueil »

**Critère WCAG** : 2.4.2 Titre de page

**Équivalences RGAA** :

- 8.5 — Chaque page web a-t-elle un titre de page ?
- 8.6 — Pour chaque page web ayant un titre de page, ce titre est-il pertinent ?

---

### 3. Titres et hiérarchie

**Résumé** : Les titres organisent le contenu de la page comme une table des matières. Ils doivent être imbriqués par niveau : le titre principal est généralement `<h1>`, suivi des niveaux 2 à 6. Les niveaux ne doivent pas être sautés.

**Pourquoi c'est important** : Les titres sont des outils de navigation essentiels :

- Les utilisateurs de lecteurs d'écran peuvent sauter d'un titre à l'autre avec une seule touche
- Les personnes malvoyantes s'appuient sur les titres visuellement plus grands pour comprendre les sujets
- Les personnes ayant des troubles cognitifs ou de lecture se repèrent grâce à l'organisation des titres

**Comment vérifier** :

1. Glisser le bookmarklet « Check headings » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet
3. L'outil affiche le niveau, le texte et signale les niveaux sautés ou le contenu masqué

**Ce qu'il faut vérifier** :

- La page contient-elle des titres ?
- Commence-t-elle par un H1 ?
- Des niveaux de titres sont-ils sautés ?
- Y a-t-il des titres vides ou stylés visuellement mais non balisés sémantiquement ?
- Les titres reflètent-ils fidèlement le contenu qui suit ?
- La structure des titres représente-t-elle l'organisation du contenu ?

**Critère WCAG** : 2.4.6 En-têtes et étiquettes

**Équivalences RGAA** :

- 9.1 — Dans chaque page web, l'information est-elle structurée par l'utilisation appropriée de titres ?
- 9.2 — Dans chaque page web, la structure du document est-elle cohérente ?

---

### 4. Contraste des couleurs

**Résumé** : Le contraste des couleurs désigne la différence entre des couleurs adjacentes : typiquement le texte et son arrière-plan. Il concerne aussi les éléments interactifs et les éléments de graphiques. Certaines personnes ne peuvent pas lire le texte si le contraste est insuffisant.

**Pourquoi c'est important** : Un bon contraste est essentiel pour les personnes malvoyantes ayant une acuité de contraste réduite. Les personnes daltoniennes ont aussi souvent besoin d'un bon contraste.

**Comment vérifier** :

- **Vérification rapide** : convertir la page en niveaux de gris avec le bookmarklet « Convert to grayscale »
- **Vérification précise** : utiliser un outil comme le Color Contrast Analyser (CCA) de TPGi pour mesurer les ratios

**Ratios requis** :

- Texte normal : 4.5:1 minimum (AA)
- Grand texte (24px ou 18.5px gras) : 3:1 minimum (AA)
- Composants d'interface et éléments graphiques : 3:1 minimum

**Critères WCAG** :

- 1.4.3 Contraste (minimum)
- 1.4.11 Contraste du contenu non textuel

**Équivalences RGAA** :

- 3.2 — Dans chaque page web, le contraste entre la couleur du texte et la couleur de son arrière-plan est-il suffisamment élevé ?
- 3.3 — Dans chaque page web, les couleurs utilisées dans les composants d'interface ou les éléments graphiques porteurs d'informations sont-elles suffisamment contrastées ?

---

### 5. Lien d'évitement (skip link)

**Résumé** : Le lien d'évitement est le premier élément interactif de la page. Il permet aux utilisateurs de contourner les blocs de contenu répétitifs (notamment les menus de navigation) pour accéder directement au contenu principal.

**Pourquoi c'est important** : Les liens d'évitement sont utiles aux personnes qui naviguent au clavier : utilisateurs de lecteurs d'écran, personnes avec un handicap moteur, utilisateurs de dispositifs comme les contacteurs ou les tiges buccales. Sans lien d'évitement, il faut tabuler à travers toute la navigation à chaque page.

**Comment vérifier** :

1. Glisser le bookmarklet « Check skip link » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet
3. L'outil met en surbrillance le lien et sa cible

**Ce qu'il faut vérifier** :

- Le premier lien interne de la page est bien un lien d'évitement
- Intitulés acceptables : « Aller au contenu », « Accéder au contenu principal », « Skip to content »

**Critère WCAG** : 2.4.1 Contourner des blocs

**Équivalences RGAA** :

- 12.7 — Dans chaque page web, un lien d'évitement ou d'accès rapide à la zone de contenu principal est-il présent ?

---

### 6. Focus et navigation clavier

**Résumé** : Le focus clavier est un indicateur visuel qui identifie l'élément ayant le focus lorsqu'on navigue avec la touche Tab. Pour les personnes qui utilisent le clavier pour naviguer, il est essentiel de savoir quel lien ou champ de formulaire a le focus.

**Pourquoi c'est important** : Les personnes qui naviguent au clavier ou avec des technologies vocales ont besoin d'une indication claire de l'élément sur lequel elles se trouvent. Cela concerne :

- Les personnes tétraplégiques
- Les personnes avec une dextérité réduite
- Les personnes avec des tremblements (ex : maladie de Parkinson)

**Comment vérifier** :

1. Glisser le bookmarklet « Check keyboard focus » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet

**Ce qu'il faut vérifier** :

- Tous les éléments interactifs ont un style visuel de focus évident
- Aucun espace vide n'est mis en surbrillance (ce qui indiquerait un lien sans texte)

**Critère WCAG** : 2.4.7 Visibilité du focus

**Équivalences RGAA** :

- 10.7 — Dans chaque page web, pour chaque élément recevant le focus, la prise de focus est-elle visible ?

---

### 7. Langue de la page

**Résumé** : Les pages web doivent identifier la langue principale de la page. Cela permet aux lecteurs d'écran et aux technologies de synthèse vocale de prononcer correctement les mots.

**Pourquoi c'est important** : La langue de la page doit être déclarée pour que les lecteurs d'écran et autres technologies qui convertissent le texte en voix synthétique puissent prononcer correctement le contenu.

**Comment vérifier** :

1. Glisser le bookmarklet « Check page language » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet

**Ce qu'il faut vérifier** :

- La langue principale est correctement identifiée (ex : `lang="fr"` pour le français)
- Si aucune langue n'est définie, l'outil affiche : « Page language is not specified »
- Note : cette vérification ne détecte pas les changements de langue dans le contenu de la page

**Critères WCAG** :

- 3.1.1 Langue de la page
- 3.1.2 Langue d'un passage

**Équivalences RGAA** :

- 8.3 — Dans chaque page web, la langue par défaut est-elle présente ?
- 8.4 — Pour chaque page web ayant une langue par défaut, le code de langue est-il pertinent ?
- 8.7 — Dans chaque page web, chaque changement de langue est-il indiqué dans le code source ?
- 8.8 — Dans chaque page web, le code de langue de chaque changement de langue est-il valide et pertinent ?

---

### 8. Zoom à 200 %

**Résumé** : Le zoom est utilisé pour agrandir le texte et les images des pages web afin de les rendre plus lisibles. Certaines personnes ont besoin d'agrandir le contenu pour pouvoir le lire. Le contenu agrandi doit rester lisible et utilisable.

**Pourquoi c'est important** : Le zoom est essentiel pour les personnes malvoyantes qui ont besoin d'agrandir le contenu. Les besoins varient : certains ont besoin d'un léger agrandissement, d'autres jusqu'à 200 % ou plus.

**Comment vérifier** :

1. Redimensionner le navigateur à une largeur étroite
2. Appuyer sur Ctrl/Cmd + « + » cinq fois pour atteindre 200 %
3. Vérifier que le texte s'adapte dans la zone visible
4. Confirmer qu'aucun défilement horizontal n'est nécessaire
5. Activer le bookmarklet « 10.12 Espacement » et vérifier qu'aucun contenu n'est perdu ou superposé

**Ce qu'il faut vérifier** :

- Tout le texte reste lisible
- Le texte n'est pas caché derrière d'autres éléments
- Pas de défilement horizontal nécessaire (pour les contenus en écriture horizontale)
- Les menus de navigation peuvent se réduire en icônes (acceptable)

**Critères WCAG** : 1.4.4 Redimensionnement du texte ; 1.4.10 Redistribution ; 1.4.12 Espacement du texte

**Équivalences RGAA** :

- 10.4 — Dans chaque page web, le texte reste-t-il lisible lorsque la taille des caractères est augmentée jusqu'à 200 % ?
- 10.11 — Pour chaque page web, les contenus peuvent-ils être présentés sans perte d'information ou de fonctionnalité et sans avoir recours à un défilement horizontal pour une fenêtre de 320 CSS px ?
- 10.12 — Dans chaque page web, les propriétés d'espacement du texte peuvent-elles être redéfinies sans perte de contenu ou de fonctionnalité ?

---

## Vérifications audio/vidéo

### 9. Sous-titres vidéo

**Résumé** : Les sous-titres sont une version textuelle de la parole et des informations sonores non vocales nécessaires pour comprendre la vidéo. Ils sont affichés dans le lecteur média et synchronisés avec l'audio. Les sous-titres peuvent être activables (closed) ou permanents (open).

**Pourquoi c'est important** : Les sous-titres sont destinés aux personnes sourdes ou malentendantes en fournissant un texte à l'écran des dialogues et éléments sonores. Ils aident également les personnes ayant des troubles de l'apprentissage ou des difficultés de concentration.

**Comment vérifier** :

- **Disponibilité** :
  - Lire la vidéo et chercher des sous-titres visibles ou un bouton [CC]
  - Activer les sous-titres et vérifier qu'ils existent dans la langue de l'audio
  - Les sous-titres générés automatiquement seuls ne répondent pas aux exigences d'accessibilité

- **Qualité** :
  - La ponctuation et les majuscules sont correctes
  - Les sous-titres sont synchronisés avec le dialogue
  - L'identification des locuteurs apparaît quand plusieurs personnes parlent
  - Les sons ambiants importants (applaudissements, tonnerre, etc.) sont sous-titrés

**Critère WCAG** : 1.2.2 Sous-titres (pré-enregistrés)

**Équivalences RGAA** :

- 4.3 — Chaque média temporel synchronisé pré-enregistré a-t-il des sous-titres synchronisés ?
- 4.4 — Pour chaque média temporel synchronisé pré-enregistré ayant des sous-titres synchronisés, ces sous-titres sont-ils pertinents ?

---

### 10. Transcriptions audio et vidéo

**Résumé** : Les transcriptions sont une version textuelle de la parole et des informations sonores non vocales dans un contenu audio, disponibles séparément de la vidéo. Les transcriptions descriptives pour les vidéos incluent en plus les informations visuelles nécessaires à la compréhension.

**Pourquoi c'est important** : Les transcriptions sont utilisées par les personnes sourdaveugles pour accéder au contenu vidéo. Les personnes utilisant des lecteurs d'écran préfèrent souvent les transcriptions à l'écoute directe de l'audio.

**Comment vérifier** :

- **Localisation** :
  - Vérifier qu'une transcription existe à proximité du média ou qu'un lien y mène
  - Pour les vidéos avec des éléments visuels significatifs, confirmer que ces détails figurent dans la transcription

- **Qualité** :
  - Tout le contenu parlé est fidèlement transcrit
  - Tous les locuteurs sont clairement identifiés
  - Les sons non vocaux (« applaudissements », « crissement de pneus ») sont documentés
  - Tout le contenu visuel important pour la compréhension est décrit

**Critère WCAG** : 1.2.1 Contenus seulement audio et seulement vidéo (pré-enregistrés)

**Équivalences RGAA** :

- 4.1 — Chaque média temporel pré-enregistré a-t-il, si nécessaire, une transcription textuelle ou une audiodescription ?
- 4.2 — Pour chaque média temporel pré-enregistré ayant une transcription textuelle ou une audiodescription synchronisée, celles-ci sont-elles pertinentes ?

---

### 11. Audiodescription

**Résumé** : L'audiodescription décrit les informations visuelles nécessaires à la compréhension du contenu vidéo. Par exemple : « Pat ouvre une petite boîte, regarde une bague de fiançailles en diamant et pleure. » Trois modes de diffusion existent : description intégrée au script du locuteur, version alternative de la vidéo avec description séparée, ou fichiers synchronisés séparés.

**Pourquoi c'est important** : L'audiodescription est importante pour les personnes qui ne peuvent pas voir la vidéo de manière adéquate, notamment les personnes aveugles et certaines personnes malvoyantes.

**Comment vérifier** :

1. **Déterminer la nécessité** : évaluer si les éléments visuels sont essentiels à la compréhension du contenu
2. **Vérifier la disponibilité** : si nécessaire, confirmer que la description existe :
   - Les informations visuelles importantes sont-elles dans l'audio principal ou l'explication du locuteur ?
   - Une vidéo avec audiodescription séparée est-elle disponible (lien ou contrôle du lecteur) ?

**Remarque** : tout texte apparaissant dans les vidéos doit être inclus dans l'audio principal ou l'audiodescription : titres, liens, adresses e-mail, noms des intervenants, texte des présentations.

**Critère WCAG** : 1.2.5 Audiodescription (pré-enregistrée)

**Équivalences RGAA** :

- 4.5 — Chaque média temporel pré-enregistré a-t-il, si nécessaire, une audiodescription synchronisée ?
- 4.6 — Pour chaque média temporel pré-enregistré ayant une audiodescription synchronisée, celle-ci est-elle pertinente ?

---

## Vérifications des formulaires

### 12. Étiquettes de champs de formulaire

**Résumé** : Les étiquettes de champs de formulaire sont le texte à côté ou au-dessus des champs. Elles indiquent quelle information saisir ou quelle case cocher. Tout le monde a besoin d'étiquettes pour comprendre comment interagir avec un formulaire.

**Pourquoi c'est important** : Des étiquettes correctement codées remplissent deux fonctions essentielles :

- Les utilisateurs de lecteurs d'écran dépendent des étiquettes pour comprendre les exigences du formulaire lorsque le contenu est lu à voix haute
- Les utilisateurs avec une dextérité réduite ont besoin d'étiquettes associées programmatiquement aux champs pour agrandir la zone cliquable, en particulier pour les cases à cocher et les boutons radio

**Comment vérifier** :

1. Glisser le bookmarklet « Check field labels » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet

**Ce qu'il faut vérifier** :

- Les éléments de formulaire marqués « Labelled » avec le texte de l'étiquette associé
- Cliquer sur les étiquettes pour vérifier que le champ reçoit le focus
- Identifier les champs affichant « Missing label »
- Les champs marqués « Labelled (using ARIA) » sont fonctionnels mais moins idéaux que les étiquettes standards

**Critère WCAG** : 3.3.2 Étiquettes ou instructions

**Équivalences RGAA** :

- 11.1 — Chaque champ de formulaire a-t-il une étiquette ?
- 11.2 — Chaque étiquette associée à un champ de formulaire est-elle pertinente ?
- 11.3 — Dans chaque formulaire, chaque étiquette associée à un champ de formulaire ayant la même fonction et répété plusieurs fois dans une même page est-elle cohérente ?

---

### 13. Champs obligatoires et erreurs

**Résumé** : Un champ de formulaire obligatoire doit être rempli avant la soumission du formulaire. La bonne pratique consiste à inclure le mot « obligatoire » dans l'étiquette. Beaucoup de formulaires utilisent un astérisque rouge (*), mais celui-ci peut ne pas être annoncé par les lecteurs d'écran ou visible pour les personnes malvoyantes en raison de sa petite taille. Certains formulaires indiquent que tous les champs sont obligatoires sauf ceux marqués « facultatif ».

**Pourquoi c'est important** : Indiquer visuellement les champs obligatoires est important pour que tout le monde sache quelles parties du formulaire doivent être remplies.

**Comment vérifier** :

1. Glisser le bookmarklet « Check required fields » dans la barre de favoris
2. Se rendre sur la page à évaluer et cliquer sur le bookmarklet

**Ce qu'il faut vérifier** :

- Les champs marqués comme obligatoires affichent un indicateur visible
- Si l'approche « facultatif » est utilisée, un message indique que tous les champs sont obligatoires sauf mention contraire
- Avant soumission, aucune erreur n'est affichée prématurément
- Soumettre le formulaire et vérifier que les champs obligatoires déclenchent une validation exploitable
- Après soumission, chaque message d'erreur nomme le champ, explique la correction, est relié au champ et accompagne le focus

**Critères WCAG** : 3.3.2 Étiquettes ou instructions, 3.3.1 Identification des erreurs, 3.3.3 Suggestion après erreur

**Équivalences RGAA** :

- 11.10 — Dans chaque formulaire, le contrôle de saisie est-il utilisé de manière pertinente ?
- 11.11 — Dans chaque formulaire, le contrôle de saisie est-il accompagné, si nécessaire, de suggestions facilitant la correction des erreurs de saisie ?

---

## Tableau récapitulatif

| # | Vérification | WCAG | RGAA |
|---|---|---|---|
| 1 | Texte alternatif des images | 1.1.1 | 1.1 à 1.9 |
| 2 | Titre de page | 2.4.2 | 8.5, 8.6 |
| 3 | Titres et hiérarchie | 2.4.6 | 9.1, 9.2 |
| 4 | Contraste des couleurs | 1.4.3, 1.4.11 | 3.2, 3.3 |
| 5 | Lien d'évitement | 2.4.1 | 12.7 |
| 6 | Focus et navigation clavier | 2.4.7 | 10.7 |
| 7 | Langue de la page | 3.1.1, 3.1.2 | 8.3, 8.4, 8.7, 8.8 |
| 8 | Zoom à 200 % | 1.4.4 | 10.4, 10.11 |
| 9 | Sous-titres vidéo | 1.2.2 | 4.3, 4.4 |
| 10 | Transcriptions audio et vidéo | 1.2.1 | 4.1, 4.2 |
| 11 | Audiodescription | 1.2.5 | 4.5, 4.6 |
| 12 | Étiquettes de formulaire | 3.3.2 | 11.1, 11.2, 11.3 |
| 13 | Champs obligatoires et erreurs | 3.3.2 | 11.10, 11.11 |
