# 10 choses faciles à vérifier pour un site plus accessible

Source : [beta.gouv.fr — 10 choses faciles à vérifier](https://doc.incubateur.net/communaute/travailler-chez-beta.gouv.fr/se-former/se-former-en-ligne/formation-a-laccessibilite/10-choses-faciles-a-verifier-pour-un-site-plus-accessible)

---

## La grille d'évaluation

Dupliquer le fichier source ci-dessous :

- [Grille d'évaluation (Google Sheets)](https://docs.google.com/spreadsheets/d/1nJxWgodGilWs5k9DOuYVwJi-CysSllgHImCTHOrH5hE/edit#gid=1758993411)

## Les outils

Ces tests peuvent se faire facilement, sans compétences techniques :

- Directement dans le navigateur
- Avec le bookmarklet [ANDI](https://www.ssa.gov/accessibility/andi/help/install.html) qui s'installe sur tous les navigateurs, via un drag and drop dans la barre de raccourci
- Avec le service en ligne [WAVE](http://wave.webaim.org/)

Il existe de nombreux autres outils spécifiques, selon les préférences de chacun, mais ces 3 là permettent d'évaluer déjà un bon nombre de choses.

### Tableau comparatif des outils

| Test | Via le navigateur | Avec ANDI | Avec WAVE |
|------|:-----------------:|:---------:|:---------:|
| Le titre des pages | x | x | |
| Les alternatives aux images | | x | x |
| La hiérarchie de l'information | | x | x |
| Les contrastes des couleurs | | x | x |
| La personnalisation du texte | x | | |
| La navigation au clavier | x | | |
| Les formulaires | x | x | |
| Les contenus animés | x | | |
| Les alternatives aux médias | x | | |
| La structure des pages | | x | x |

Pour aller plus loin : [points de contrôle rapides – A First Review of Web Accessibility (W3C)](https://www.w3.org/WAI/test-evaluate/preliminary/)

---

## 1. Le titre des pages

Le titre de page permet de se situer : c'est la première chose lue par un lecteur d'écran à l'affichage d'une page ou d'un onglet. Les bons titres de pages aident à s'orienter entre plusieurs onglets.

### Le test des onglets

**Ce qu'il faut faire :** ouvrir plusieurs pages du site dans des onglets différents.

**Ce qu'il faut vérifier :**

- Le titre est pertinent
- Le titre décrit brièvement le contenu de la page
- Le titre permet de différencier la page des autres pages du site

Un bon titre commence généralement par les informations importantes et uniques.

---

## 2. Les alternatives aux images

Les alternatives transmettent l'objectif de l'image : elles sont lues par les lecteurs d'écran (ou ressenties sur une plage braille). Parfois, elles sont affichées à la place de l'image quand la connexion est mauvaise.

### Le test des alternatives

**Ce qu'il faut faire :** afficher les textes alternatifs des images avec un outil dédié.

**Ce qu'il faut vérifier :**

- L'alternative doit permettre de comprendre le contenu, pas nécessairement décrire l'image
- Les images décoratives qui n'apportent pas de sens n'ont pas d'alternative

> Un bon texte alternatif est ce que tu dirais à quelqu'un qui interagit avec une page web mais ne la voit pas (par exemple, « recherche » plutôt que « loupe »).

Un texte alternatif approprié n'est pas une science exacte. Certaines personnes préfèrent les descriptions détaillées ; d'autres des descriptions concises.

---

## 3. La hiérarchie de l'information

La structure de la page est balisée : certains éléments de texte sont importants dans la page. Ils sont mis en avant visuellement. Ils doivent l'être aussi dans le code via les balises dédiées.

### Le test du plan

**Ce qu'il faut faire :** lire le plan de la page avec un outil dédié.

**Ce qu'il faut vérifier :**

- Sauf exception, la page possède un ou plusieurs titres de rubriques
- Les textes mis en valeur visuellement sont bien marqués comme des titres
- La hiérarchie des titres a du sens

---

## 4. Les contrastes des couleurs

Les couleurs du site n'entravent pas la lecture : certaines personnes ont besoin d'un contraste suffisant pour lire (trouble de vision lié à la vieillesse par exemple). D'autres ont besoin d'une faible luminance (certains types de dyslexie) ou d'une luminance élevée.

Chaque personne a des besoins différents : le site doit permettre à l'utilisateur de s'adapter.

### Le test des couleurs

**Ce qu'il faut faire :** vérifier les contrastes de la page avec un outil dédié.

**Ce qu'il faut vérifier :**

- Le contraste minimum par défaut est respecté pour les textes de taille normale
- Les utilisateurs peuvent surcharger la couleur de texte ou du fond

---

## 5. La personnalisation du texte

Le texte est adaptable : un texte peut être adapté de multiples façons (couleur, taille, police, interlignes…) via les préférences du navigateur.

Si le site est mal conçu, il devient inutilisable, ou le contenu illisible.

### Le test du zoom

**Ce qu'il faut faire :** agrandir le texte à 200 % et naviguer sur le site.

**Ce qu'il faut vérifier :**

- Tout le texte est agrandi
- Le texte ne disparaît pas ou n'est pas coupé
- Le texte, les images et les autres contenus ne se chevauchent pas
- Tous les éléments des formulaires sont visibles et utilisables
- Le défilement horizontal n'est pas nécessaire pour lire le contenu

---

## 6. La navigation au clavier

L'interface est utilisable sans souris : certaines personnes utilisent le clavier ou la saisie vocale (qui utilise des commandes clavier).

L'ensemble du contenu et des fonctionnalités doit donc être accessible via le clavier : liens, formulaires, pause/play sur les lecteurs médias, menus...

### Le test de la souris perdue

**Ce qu'il faut faire :** utiliser le site sans manipuler la souris.

**Ce qu'il faut vérifier :**

- Le focus du clavier est visible
- L'ordre de navigation est logique
- L'accès à tous les éléments (liens, champs de formulaire, boutons et commandes du lecteur multimédia…) est possible
- Le focus ne reste pas coincé (on peut sortir d'une vidéo par exemple)

---

## 7. Les formulaires

Les formulaires sont balisés correctement : un formulaire est composé de champs, qui doivent être correctement balisés pour pouvoir être remplis au clavier, par commande vocale ou via un lecteur d'écran.

Les aides à la saisie et messages d'erreurs doivent être placés de manière pertinente pour être visibles (et utiles) pour tous.

C'est l'un des tests les plus compliqués mais aussi celui qui a le plus d'impact.

### Le test des formulaires

**Ce qu'il faut faire :** identifier tous les formulaires du site (même les petits, comme un formulaire de recherche ou d'inscription à une newsletter).

**Ce qu'il faut vérifier :**

- Les formulaires sont accessibles au clavier (et toutes les options d'un menu déroulant sont accessibles)
- Les champs ont un label (et un clic sur le label active le champ)
- Les champs obligatoires sont indiqués (pas seulement par la couleur rouge)
- Les instructions d'aide sont avant le champ concerné
- Les formats spécifiques (par exemple les dates) sont explicités dans le label
- Les erreurs sont explicites (quel champ est concerné, comment corriger)

---

## 8. Les contenus animés

Les animations ne perturbent pas la lecture : les utilisateurs doivent pouvoir contrôler le contenu en mouvement, pour avoir le temps de traiter une information (vidéo, carrousel) ou pour pouvoir se concentrer sur le contenu sans être distraits par un élément.

Plus spécifiquement, certains contenus clignotants peuvent déclencher une crise d'épilepsie chez certaines personnes.

### Le test des animations

**Ce qu'il faut faire :** identifier les contenus qui bougent ou clignotent.

**Ce qu'il faut vérifier :**

- Si des informations défilent ou bougent automatiquement, elles ne durent pas plus de 5 secondes, ou le mouvement peut être arrêté
- L'utilisateur peut mettre en pause ou cacher les mouvements
- L'utilisateur peut régler la fréquence de mise à jour des informations animées
- Si des informations se mettent à jour en temps réel, l'utilisateur peut les mettre en pause ou contrôler la fréquence de mise à jour
- Aucun contenu ne clignote ou ne se met à clignoter plus de trois fois en une seconde

---

## 9. Les alternatives aux médias

Les médias ont des alternatives : les podcasts ou formats audios ne sont pas accessibles aux personnes sourdes ou malentendantes, sauf si fournis dans un format alternatif (transcription par exemple).

Les informations visuelles d'une vidéo ne sont pas accessibles aux personnes aveugles ou malvoyantes, sauf si elles sont fournies dans un format alternatif tel que l'audio ou le texte.

### Le test des médias

**Ce qu'il faut faire :** identifier les médias (vidéos et audio) du service.

**Ce qu'il faut vérifier :**

- Les contrôles du lecteur vidéo/audio sont accessibles au clavier
- Le son ne démarre pas seul
- Les informations audios sont accessibles au format texte (sous-titres, transcript)
- Les informations visuelles sont accessibles au format texte ou au format audio (audiodescription ou transcript)

---

## 10. La structure des pages

La page est linéaire : tout le monde ne « voit » pas une page de la même manière. Un site a souvent une structure complexe visuellement (sidebar, éléments graphiques...) mais pour certains utilisateurs, il sera perçu de manière linéaire.

### Le test du site tout nu

**Ce qu'il faut faire :** désactiver les images et les styles.

**Ce qu'il faut vérifier :**

- Les informations sont affichées dans le bon sens
- Les textes alternatifs fournissent des informations pertinentes

---

## Et après ?

Intégrer l'accessibilité dans votre équipe :

- **Auto-diagnostic régulier** pour chaque nouveau composant / fonctionnalité / sprint…
- **Prise en compte en amont** : faire sa propre checklist, selon son métier

Pour aller plus loin : [points de contrôle rapides – A First Review of Web Accessibility (W3C)](https://www.w3.org/WAI/test-evaluate/preliminary/)

Envie d'être accompagné ? Faisons cet atelier ensemble avec votre équipe ! Contact : #domaine-accessibilité

---

## Index des liens

| # | Texte du lien | URL |
|---|---------------|-----|
| 1 | Grille d'évaluation (Google Sheets) | https://docs.google.com/spreadsheets/d/1nJxWgodGilWs5k9DOuYVwJi-CysSllgHImCTHOrH5hE/edit#gid=1758993411 |
| 2 | ANDI (bookmarklet) | https://www.ssa.gov/accessibility/andi/help/install.html |
| 3 | WAVE (service en ligne) | http://wave.webaim.org/ |
| 4 | points de contrôle rapides – W3C | https://www.w3.org/WAI/test-evaluate/preliminary/ |
