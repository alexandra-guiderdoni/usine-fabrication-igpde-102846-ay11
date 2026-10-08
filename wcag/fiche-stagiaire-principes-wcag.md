# Principes WCAG - fiche stagiaire

<!-- Contournement WeasyPrint 68 : un tableau fragmenté entre deux pages fait
     échouer la génération PDF/UA-1 (« Table wrapper without a table »).
     Ce style garde chaque tableau entier sur une page. La largeur des colonnes est
     fixée par les tirets de la ligne de séparation de chaque tableau : colonnes
     courtes étroites, colonnes de phrases larges, pour des tableaux moins hauts.
     Pas de césure dans les en-têtes ni dans les deux colonnes de mots-clés : le
     gabarit Pandoc l'active partout et coupait « Cou-leur » ou « Com-prendre ». -->
<style>table { break-inside: avoid; } th, td:nth-child(-n+2) { hyphens: manual; }</style>

<!-- Sommaire sur la première page : le gabarit formation place la page de garde
     (header#title-block-header) seule sur une page. Ici elle n'impose plus de saut
     de page et son espace haut est réduit : bandeau, titre et sommaire tiennent sur
     la page 1. Le sous-titre est masqué : le générateur y met le premier intertitre
     (« L'idée à retenir »), qui figure déjà dans le sommaire.
     Pied de page « Page X / Y » sur toutes les pages, première comprise. -->
<style>header#title-block-header { break-after: avoid; padding: 2em 0 0.5em 0; } header#title-block-header .subtitle { display: none; } @page { @bottom-center { content: "Page " counter(page) " / " counter(pages); } } @page :first { @bottom-center { content: "Page " counter(page) " / " counter(pages); } }</style>

<!-- La boussole, ses exemples et le décodage doivent rester ensemble sur la
     page 2. Le tableau et les deux encarts sont donc légèrement resserrés,
     sans réduire la taille du texte courant du reste de la fiche. -->
<style>.questions-table table { font-size: 0.78em; } .questions-table th, .questions-table td { line-height: 1.2; padding: 0.35em 0.45em; } .questions-note { font-size: 0.86em; margin: 0.3em 0 0.4em; } .wcag-bridge { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2em; break-inside: avoid; font-size: 0.78em; line-height: 1.15; hyphens: manual; } .wcag-bridge h3 { font-size: 1.08em; margin: 0 0 0.25em; } .wcag-bridge ul, .wcag-bridge p { margin-top: 0; margin-bottom: 0; } .wcag-bridge li { margin-bottom: 0.1em; }</style>

<!-- Le fil de l'atelier Word est réparti en cinq tableaux courts : chaque
     tableau reste entier sur une page, conformément au contournement
     WeasyPrint ci-dessus, tout en conservant une taille de texte lisible. -->
<style>.word-journey table { font-size: 0.82em; } .word-journey th, .word-journey td { line-height: 1.2; padding: 0.38em 0.45em; } .word-journey h4 { break-after: avoid; margin-bottom: 0.35em; } .word-journey p { margin-top: 0.35em; margin-bottom: 0.65em; }</style>

<!-- Le parcours web suit les 13 points du site dans quatre tableaux courts.
     Les intitulés complets et les références WCAG restent lisibles sans
     fragmenter un tableau entre deux pages. -->
<style>.web-journey table { font-size: 0.78em; } .web-journey th, .web-journey td { line-height: 1.18; padding: 0.34em 0.42em; hyphens: manual; } .web-journey h3 { break-after: avoid; margin-bottom: 0.35em; } .web-journey p { margin-top: 0.35em; margin-bottom: 0.65em; }</style>

<!-- Le parcours réseaux sociaux reprend les trois temps de la checklist
     projetée. Les références sont qualifiées et cliquables : WCAG lorsqu'une
     correspondance A ou AA existe, Opquast pour la qualité éditoriale, ou
     pratique éditoriale quand aucun critère direct n'est retenu. -->
<style>.social-journey table { font-size: 0.78em; } .social-journey th, .social-journey td { line-height: 1.17; padding: 0.34em 0.42em; hyphens: manual; } .social-journey h3 { break-after: avoid; margin-bottom: 0.35em; } .social-journey p { margin-top: 0.35em; margin-bottom: 0.65em; }</style>

Formation 102846 - L'accessibilité numérique pour la bureautique et le web

## L'idée à retenir

Un contenu accessible reste utilisable quand la situation de la personne change.

Il ne dépend pas d'une seule façon de voir, d'entendre, de lire, de comprendre ou d'agir.

Pour comprendre les difficultés rencontrées, explorez le site de test :  
[« L'accessibilité numérique, et si nous agissions ? »](https://atalan.fr/agissons/fr/index.html).

## Les 4 questions

::: {.questions-table}
Table: Les 4 principes WCAG

| Repère | Principe et action | Question à se poser | Qui est bloqué si c'est absent ? |
|---|---------------------|------------------------------------------|-----------------------------------|
| 1.x | Perceptible → percevoir | L'information existe-t-elle encore si je ne vois pas, n'entends pas ou lis difficilement ? | Amir - ne perçoit pas l'image ; Anaïs - distingue mal le texte ; Justine - ne perçoit pas le son |
| 2.x | Utilisable → utiliser | Puis-je aller jusqu'au bout sans souris, sans geste précis et sans piège ? | Agathe - ne peut pas utiliser la souris |
| 3.x | Compréhensible → comprendre | Sais-je quoi faire, quoi corriger et ce qui va se passer ? | Anatole - ne comprend pas la consigne ; Paul - perd le fil |
| 4.x | Robuste → fonctionner avec les outils | Les outils d'assistance comprennent-ils la structure et les actions ? | Amir - son lecteur d'écran perd la structure ; autres utilisateurs d'outils d'assistance |
:::

::: {.questions-note}
*Un persona peut être concerné par plusieurs principes selon l'obstacle rencontré.*
:::

:::: {.wcag-bridge}
::: {.wcag-examples}
### Quatre exemples pour démarrer

- **Amir** - image sans alternative → **1.x Perceptible** → carte **1.1.1**
- **Agathe** - navigation impossible sans souris → **2.x Utilisable** → carte **2.1.1**
- **Anaïs** - contraste insuffisant → **1.x Perceptible** → carte **1.4.3**
- **Anatole** - consigne de formulaire peu claire → **3.x Compréhensible** → carte **3.3.2**
:::

::: {.wcag-decoder}
### 1.1.1 - Décoder une carte

`1` indique le principe **Perceptible** ;  
`1.1`, la directive **Alternatives textuelles** ;  
`1.1.1`, le critère **Contenu non textuel**.  
La couleur indique le niveau de conformité, pas le principe.  
Les étiquettes sont des repères de tri par publics, métiers ou usages.
:::
::::

## Pendant l'atelier Word

### Les réflexes essentiels

Table: Corrections Word, principes, personas et réflexes

| Correction Word | Principe | Qui est bloqué ? | Réflexe |
|--------------------|--------------------|---------------------------|---------------------------------|
| Styles de titres | Compatible + Utiliser | Amir ne peut pas naviguer dans le document | Un titre doit être un vrai style de titre, pas du texte gros et gras |
| Listes natives | Compatible + Comprendre | Amir et Anatole perdent la structure | Une liste doit être une vraie liste, pas des tirets manuels |
| Texte alternatif | Percevoir | Amir ne sait pas ce que l'image contient | Une image utile doit avoir une alternative textuelle |
| Contraste | Percevoir | Anaïs ne peut pas lire le texte | Le contraste doit permettre de lire sans effort (ratio 4.5:1) |
| Liens explicites | Comprendre + Utiliser | Amir et Anatole ne savent pas où mène le lien | Un lien doit annoncer clairement sa destination |
| Langue du document | Comprendre + Compatible | Amir entend une prononciation incorrecte | La langue du document doit être indiquée |
| Export PDF | Compatible | Amir perd toute la structure du document | L'export PDF doit conserver la structure Word |

### Le fil de l'atelier Word

Suivez les slides dans l'ordre. Après chaque séquence, réalisez l'action dans le document puis renseignez les points indiqués dans la checklist.

Les cartes citées sont des correspondances pédagogiques avec WCAG 2.2 ; elles ne constituent pas une évaluation directe du fichier Word selon WCAG. Les correspondances retiennent les critères de niveaux A et AA. « Pas de carte directe » signifie qu'aucune correspondance directe n'a été retenue dans ce périmètre.

::: {.word-journey}
#### Station 1 - Structurer et naviguer

Table: Slides 61 et 62 - actions, checklist et cartes WCAG

| Slide / point présenté | Action dans Word | Checklist | Carte(s) WCAG |
|-------------------------|------------------------------------------|------------|--------------------------------|
| **61 - Titres, hiérarchie et sommaire** | Appliquer les styles adaptés, vérifier le plan dans le volet de navigation et générer le sommaire automatique. | **P-01 à P-03** | **P-01 et P-02** → **1.3.1** - Informations et relations ; **2.4.6** - En-têtes et étiquettes.<br>**P-03** → **2.4.5** - Accès multiples. |
| **62 - Listes et mise en page robuste** | Remplacer les listes et mises en page simulées par les fonctions natives ; afficher les marques pour contrôler le résultat. | **P-04 et P-05** | **1.3.1** - Informations et relations ; **1.3.2** - Ordre séquentiel logique |

#### Station 2 - Rendre les contenus et les liens compréhensibles

Table: Slides 64 à 66 - actions, checklist et cartes WCAG

| Slide / point présenté | Action dans Word | Checklist | Carte(s) WCAG |
|-------------------------|------------------------------------------|------------|--------------------------------|
| **64 - Choisir le bon traitement pour chaque image** | Identifier la fonction de chaque image : alternative simple, description détaillée ou traitement décoratif. | **P-06 à P-08** | **1.1.1** - Contenu non textuel |
| **65 - Vrai texte et liens compréhensibles** | Remettre l'information en vrai texte ; rendre les liens autonomes et décrire les téléchargements. | **P-09 et P-10** | **1.4.5** - Texte sous forme d'image ; **2.4.4** - Fonction du lien (selon le contexte) |
| **66 - L'information essentielle reste dans le corps** | Reprendre dans le corps toute information essentielle portée seulement par un en-tête, un filigrane ou un arrière-plan. | **P-11** | Pas de carte directe |

#### Station 3 - Sécuriser couleurs, graphiques et tableaux

Table: Slides 68 à 70 - actions, checklist et cartes WCAG

| Slide / point présenté | Action dans Word | Checklist | Carte(s) WCAG |
|-------------------------|------------------------------------------|------------|--------------------------------|
| **68 - Le contraste se mesure** | Mesurer le contraste du texte et des éléments graphiques, puis corriger les couleurs insuffisantes. | **P-12** | **1.4.3** - Contraste (minimum) ; **1.4.11** - Contraste du contenu non textuel |
| **69 - Un graphique compréhensible sans la couleur** | Ajouter des étiquettes et des motifs, ou fournir un équivalent textuel complet. | **P-13** | **1.4.1** - Utilisation de la couleur |
| **70 - Un tableau de données simple** | Simplifier la grille, titrer le tableau, identifier et répéter les en-têtes, puis empêcher le fractionnement des lignes. | **P-14** | **1.3.1** - Informations et relations |

#### Station 4 - Régler langues et lisibilité

Table: Slides 72 et 73 - actions, checklist et cartes WCAG

| Slide / point présenté | Action dans Word | Checklist | Carte(s) WCAG |
|-------------------------|------------------------------------------|------------|--------------------------------|
| **72 - Langues et styles typographiques** | Définir la langue principale et celle des passages étrangers ; régler la typographie dans le style du corps. | **P-15 et P-16** | **P-15** → **3.1.1** - Langue de la page ; **3.1.2** - Langue d'un passage.<br>**P-16** → Pas de carte directe. |
| **73 - Casse, accents et sigles** | Rétablir la saisie accentuée, appliquer les majuscules par la mise en forme et développer les sigles. | **P-17 et P-18** | Pas de carte directe |

#### Station 5 - Finaliser, vérifier, exporter et contrôler

Table: Slides 75, 76 et 79 - actions, checklist et cartes WCAG

| Slide / point présenté | Action dans Word | Checklist | Carte(s) WCAG |
|-------------------------|------------------------------------------|------------|--------------------------------|
| **75 - Propriétés et vérificateur Word** | Renseigner les propriétés et le nom du fichier ; exécuter le vérificateur et expliquer les alertes restantes. | **P-19 et C-01** | **P-19**, titre et langue → **2.4.2** - Titre de page ; **3.1.1** - Langue de la page.<br>Auteur, nom de fichier et **C-01** → Pas de carte directe. |
| **76 - Exporter puis contrôler le PDF** | Exporter avec les propriétés, les balises et les signets ; contrôler ensuite le PDF avec un outil et la checklist humaine. | **P-20 et C-02** | **P-20** → **1.3.1** - Informations et relations.<br>**C-02** → Pas de carte directe. |
| **79 - Checklist progressive - Station 5 et points signalés** | Vérifier, sans manipulation obligatoire pendant l'atelier : protection, clignotement, formulaire Word, objets flottants et tableaux de mise en page. | **S-01 à S-05** | **S-02** → **2.3.1** - Pas plus de trois flashs ou sous le seuil critique.<br>**S-04** → **1.3.2** - Ordre séquentiel logique ; **S-05** → **1.3.1** - Informations et relations.<br>**S-01 et S-03** → Pas de carte directe. |
:::

## Pendant l'atelier web

Parcourez les scénarios dans l'ordre. Chaque intitulé ouvre directement la page correspondante du site à auditer.

::: {.web-journey}
### #1 à #4 - Contenus et structure

Table: Points 1 à 4 - contenus, structure, personas et cartes WCAG

| Point du site | Ce que je vérifie | Qui est bloqué ? | Carte(s) WCAG |
|------------------------------|----------------------------------------|-----------------------------|-----------------------------|
| **[#1 - Texte alternatif des images](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec01-images.html)**<br>Slides 84 à 86 | Chaque image reçoit-elle le traitement adapté à son rôle : informative, décorative, fonctionnelle ou complexe ? | Amir - ne perçoit pas l'image | **1.1.1 - Contenu non textuel** |
| **[#2 - Titre de page](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec02-page-title.html)**<br>Slide 87 | L'onglet annonce-t-il une page au titre clair et unique ? | Amir et Anatole - ne savent pas où ils sont | **2.4.2 - Titre de page** |
| **[#3 - Titres et hiérarchie](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec03-headings.html)**<br>Slides 88 et 89 | Les titres sont-ils balisés et organisés selon une hiérarchie logique ? | Amir et Anatole - perdent la structure | **2.4.6 - En-têtes et étiquettes**<br>Associé : **1.3.1** |
| **[#4 - Contraste des couleurs](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec04-contrast.html)**<br>Slides 90 et 91 | Le texte et les éléments utiles sont-ils suffisamment contrastés ? | Anaïs - distingue mal l'information | **1.4.3 - Contraste (minimum)**<br>Associé : **1.4.11** |

### #5 à #8 - Navigation et lecture

Table: Points 5 à 8 - navigation, lecture, personas et cartes WCAG

| Point du site | Ce que je vérifie | Qui est bloqué ? | Carte(s) WCAG |
|------------------------------|----------------------------------------|-----------------------------|-----------------------------|
| **[#5 - Lien d'évitement](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec05-skiplinks.html)**<br>Slide 92 | La première touche Tab révèle-t-elle un lien vers le contenu ? | Agathe - doit traverser toute la navigation | **2.4.1 - Contourner des blocs** |
| **[#6 - Focus et navigation clavier](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec06-keyboard-focus.html)**<br>Slides 93 à 96 | Tout fonctionne-t-il au clavier avec un focus visible et logique ? | Agathe - ne peut pas utiliser la souris | **2.4.7 - Visibilité du focus**<br>Associés : **2.1.1, 2.1.2, 2.4.3** |
| **[#7 - Langue de la page](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec07-language.html)**<br>Slide 97 | La langue de la page et des passages étrangers est-elle indiquée ? | Amir - entend une prononciation incorrecte | **3.1.1 - Langue de la page**<br>Associé : **3.1.2** |
| **[#8 - Zoom à 200 %](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec08-zoom.html)**<br>Slide 98 | À 200 % et dans une fenêtre étroite, le contenu reste-t-il lisible et utilisable sans perte ? | Anaïs - ne peut pas lire la page agrandie | **1.4.4 - Redimensionnement du texte**<br>Associé : **1.4.10** |

### #9 à #11 - Médias

Table: Points 9 à 11 - médias, personas et cartes WCAG

| Point du site | Ce que je vérifie | Qui est bloqué ? | Carte(s) WCAG |
|------------------------------|----------------------------------------|-----------------------------|-----------------------------|
| **[#9 - Sous-titres vidéo](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec09-captions.html)**<br>Slides 99 et 100 | La vidéo propose-t-elle des sous-titres synchronisés et complets ? | Justine - ne perçoit pas les paroles | **1.2.2 - Sous-titres (pré-enregistrés)** |
| **[#10 - Transcriptions audio et vidéo](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec10-transcript.html)**<br>Slide 101 | Une transcription complète est-elle disponible près du média ? | Justine - n'accède pas au contenu sonore | **1.2.1 - Contenus seulement audio et seulement vidéo pré-enregistrés** |
| **[#11 - Audiodescription](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec11-audio-description.html)**<br>Slide 102 | L'information visuelle essentielle reste-t-elle disponible sans la vue, par l'audio principal, une audiodescription ou une alternative ? | Amir - ne perçoit pas l'action visuelle | **1.2.5 - Audiodescription (pré-enregistrée)**<br>Associé : **1.2.3** |

### #12 à #13 - Formulaires

Table: Points 12 et 13 - formulaires, personas et cartes WCAG

| Point du site | Ce que je vérifie | Qui est bloqué ? | Carte(s) WCAG |
|------------------------------|----------------------------------------|-----------------------------|-----------------------------|
| **[#12 - Étiquettes de champs de formulaire](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec12-form-labels.html)**<br>Slides 105 à 107 | Chaque champ possède-t-il une étiquette visible et correctement associée ? | Anatole - ne sait pas quoi saisir ; Amir - n'entend pas l'étiquette | **3.3.2 - Étiquettes ou instructions**<br>Associés : **1.3.1, 2.5.3** |
| **[#13 - Champs obligatoires et erreurs](https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/site-inaccessible/ec13-required-errors.html)**<br>Slide 108 | Avant l'envoi, les champs obligatoires sont-ils indiqués ; après la soumission, les erreurs expliquent-elles comment corriger ? | Anatole - ne comprend pas comment corriger | **3.3.2 - Étiquettes ou instructions**<br>Associés : **3.3.1, 3.3.3** |
:::

## Pendant les réseaux sociaux

Choisissez deux obstacles prioritaires. Pour chacun, identifiez la personne bloquée, la correction et la preuve.

Les références distinguent les critères WCAG, les règles Opquast et les pratiques éditoriales. « Pas de critère A/AA direct » signifie que le réflexe reste utile, sans correspondance directe retenue dans ce périmètre.

Boussole des quatre réflexes : **slide 118**. Consigne de l'exercice : **slide 129**.

::: {.social-journey}
### Anticiper - slide 130

Table: Réseaux sociaux - anticiper, questions, personas et références

| Point présenté | Question à se poser | Qui est bloqué ? | Référence(s) |
|--------------------------|------------------------------------------|-------------------------------|--------------------------------|
| **Alternatives prévues selon le média**<br>Détail images : slides 119 à 121 | Le traitement est-il prévu selon le média : texte alternatif utile ou option décorative pour l'image, transcription pour l'audio, sous‑titres pour la vidéo ? | Amir - ne perçoit pas l'image ; Justine - ne perçoit pas le son | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** - Contenu non textuel ; **[1.2.1](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html)** - Audio seul préenregistré ; **[1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html)** - Sous‑titres préenregistrés |
| **Représentations inclusives**<br>Détails : slides 126 et 127 | Qui est visible ou absent, dans quel rôle, et le visuel correspond-il à la réalité accessible de l'action ? | Pas de persona unique - les publics représentés ou oubliés | **Pratique éditoriale**<br>Pas de critère A/AA direct |
| **Visuel chargé et version complète**<br>Détails : slide 120 | Les chiffres et messages clés existent-ils aussi dans le post ou dans une version complète ? | Amir - ne perçoit pas le visuel ; Anaïs - ne peut pas l'agrandir confortablement | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** - Contenu non textuel<br>Si le visuel contient du texte : **[1.4.5](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html)** - Texte sous forme d'image |
| **Lisibilité du visuel** | Le texte est-il lisible sur mobile, avec une police adaptée et un contraste d'au moins 4,5:1 ? | Anaïs - distingue mal un texte petit ou peu contrasté ; Paul - lit plus difficilement | **WCAG [1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)** - Contraste minimum<br>Police lisible : **pratique éditoriale** |

### Rédiger - slide 131

Table: Réseaux sociaux - rédiger, questions, personas et références

| Point présenté | Question à se poser | Qui est bloqué ? | Référence(s) |
|--------------------------|------------------------------------------|-------------------------------|--------------------------------|
| **Ordre et lecture linéaire**<br>Détails : slides 114 à 117 | Lu à voix haute, le post garde-t-il un ordre logique et un sens complet ? | Amir - écoute le post ; Paul - perd le fil | **Correspondance pédagogique : WCAG [1.3.2](https://www.w3.org/WAI/WCAG22/Understanding/meaningful-sequence.html)** - Ordre séquentiel logique |
| **Information essentielle dans le texte**<br>Détails : slide 120 | Le post contient-il les informations indispensables, sans dépendre du visuel ? | Amir - ne perçoit pas le visuel | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** - Contenu non textuel<br>Si le visuel contient du texte : **[1.4.5](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html)** - Texte sous forme d'image |
| **Paragraphes courts et texte natif, sans faux gras Unicode**<br>Détails : slide 125 | Le post est-il découpé en paragraphes courts et écrit avec les caractères ordinaires et les fonctions natives de la plateforme, sans générateur de style ? | Amir - entend un texte déformé ; Paul - rencontre une lecture inutilement difficile | **Opquast [règle 14](https://checklists.opquast.com/fr/qualite-numerique/les-contenus-ne-detournent-pas-de-caracteres-pour-simuler-une-mise-en-forme-visuelle)** - Caractères détournés<br>Paragraphes courts : **pratique éditoriale**<br>Associé : **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** |
| **Émojis sobres**<br>Détails : slides 122 et 123 | Le message reste-t-il complet sans les émojis ; ceux qui portent du sens sont-ils explicités par des mots ? | Amir - entend chaque émoji vocalisé ; Paul - subit les interruptions de lecture | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** si l'émoji porte une information<br>Quantité et position : **pratique éditoriale** |
| **Hashtags lisibles**<br>Détail : slide 124 | Les hashtags sont-ils écrits en CamelCase, courts, regroupés à la fin et limités à deux ou trois ? | Amir - entend une prononciation ambiguë ; Paul - déchiffre difficilement le bloc | **Pratique éditoriale**<br>Pas de critère A/AA direct |
| **Langage inclusif clair**<br>Détail : slide 128 | La formulation reste-t-elle claire à voix haute et lors d'une lecture rapide ? | Anatole - comprend difficilement une formulation complexe ; Paul - lit plus lentement | **Pratique éditoriale**<br>Pas de critère A/AA direct |

### Publier - slide 132

Table: Réseaux sociaux - publier, questions, personas et références

| Point présenté | Question à se poser | Qui est bloqué ? | Référence(s) |
|--------------------------|------------------------------------------|-------------------------------|--------------------------------|
| **Texte alternatif finalisé**<br>Détails : slides 119 à 121 | Chaque image informative possède-t-elle un texte alternatif utile et propre à son contenu ? | Amir - ne sait pas ce que montre l'image | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** - Contenu non textuel |
| **Infographie ou carrousel**<br>Détail : slide 120 | Les chiffres et messages clés sont-ils repris dans le post ou dans une version complète liée ? | Amir - ne perçoit pas les visuels ; Anaïs - ne peut pas les agrandir confortablement | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** - Contenu non textuel ; **[1.4.5](https://www.w3.org/WAI/WCAG22/Understanding/images-of-text.html)** - Texte sous forme d'image |
| **Audio préenregistré** | Une transcription écrite, relue et facile à trouver accompagne-t-elle le contenu audio ? | Justine - ne perçoit pas le contenu sonore | **WCAG [1.2.1](https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded.html)** - Contenus seulement audio préenregistrés |
| **Vidéo préenregistrée** | Les sous‑titres sont-ils synchronisés, complets et relus ; l'information visuelle essentielle est-elle déjà donnée par l'audio, une audiodescription ou une alternative ; une transcription est-elle ajoutée si nécessaire ? | Justine - ne perçoit pas le son ; Amir - ne perçoit pas l'action visuelle | **WCAG [1.2.2](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html)** - Sous‑titres préenregistrés<br>Associés : **[1.2.3](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-or-media-alternative-prerecorded.html), [1.2.5](https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded.html)** |
| **Code QR et lien visible** | Le code à réponse rapide (QR) est-il accompagné d'un lien visible et explicite, avec une taille et un contraste suffisants ? | Amir - ne perçoit pas le code QR ; toute personne qui ne peut pas le scanner | **WCAG [1.1.1](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)** - Contenu non textuel<br>Associé : **[2.4.4](https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html)** - Fonction du lien<br>Taille et contraste : **pratique de scannabilité** |
:::

## Pour formuler une preuve

Pour chaque problème repéré, notez :

1. Ce que j'observe.
2. Qui est bloqué (quel persona, quel usage).
3. Le principe concerné : percevoir, utiliser, comprendre ou compatible.
4. La correction possible.
5. La preuve que c'est corrigé : test, mesure, comparaison ou relecture.

## Phrase de contrôle pour une publication

Si l'image, le son ou la mise en forme disparaît, le message reste-t-il complet et compréhensible ?
