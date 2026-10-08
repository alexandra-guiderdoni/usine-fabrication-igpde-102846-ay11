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

Table: Atelier web - vérifications et personas

| Vérification web | Principe | Qui est bloqué ? | Réflexe |
|--------------------|--------------------|---------------------------|---------------------------------|
| Images | Percevoir | Amir ne sait pas ce que l'image montre | Une image informative doit avoir une alternative |
| Titre de page | Comprendre + Utiliser | Amir et Anatole ne savent pas où ils sont | Une page doit avoir un titre clair et unique |
| Titres | Comprendre + Compatible | Amir et Anatole perdent la structure | Les titres doivent organiser la page |
| Contrastes | Percevoir | Anaïs ne peut pas lire | Le contraste doit être suffisant |
| Clavier et focus | Utiliser | Agathe ne peut pas naviguer | Le clavier doit permettre de naviguer, le focus doit être visible |
| Langue | Comprendre + Compatible | Amir entend une prononciation fausse | Le changement de langue doit être indiqué |
| Zoom | Percevoir + Utiliser | Anaïs ne peut pas lire même agrandi | Le contenu doit rester lisible et utilisable à 200 % |
| Sous-titres | Percevoir | Justine ne comprend pas la vidéo | Les vidéos doivent avoir des sous-titres synchronisés |
| Transcription | Percevoir | Justine n'a pas accès au contenu audio | Le contenu audio doit exister en texte |
| Libellés | Comprendre + Compatible | Anatole ne sait pas quoi remplir | Chaque champ doit dire ce qui est attendu |
| Erreurs | Comprendre | Anatole ne sait pas comment corriger | L'erreur doit expliquer comment corriger |

## Pendant les réseaux sociaux

Table: Réseaux sociaux et personas

| Cas | Principe | Qui est bloqué ? | Réflexe |
|--------------------|--------------------|---------------------------|---------------------------------|
| Image sans alternative | Percevoir | Amir ne sait pas ce qu'elle contient | Ajouter un texte alternatif utile |
| Texte dans une image | Percevoir + Compatible | Amir n'a pas accès au texte | Remettre l'info essentielle dans le texte du post |
| Hashtag illisible | Comprendre | Paul et le lecteur d'écran d'Amir | Utiliser le CamelCase (#AccessibiliteNumerique) |
| Emojis en série | Comprendre | Amir entend chaque emoji vocalisé | Limiter, placer en fin, ne pas remplacer les mots |
| Caractères fantaisie Unicode | Compatible | Amir entend du charabia | Éviter les polices décoratives non interprétées |
| Ordre de lecture confus | Comprendre + Utiliser | Amir et Paul perdent le fil | Relire le post linéairement, comme il sera vocalisé |

## Pour formuler une preuve

Pour chaque problème repéré, notez :

1. Ce que j'observe.
2. Qui est bloqué (quel persona, quel usage).
3. Le principe concerné : percevoir, utiliser, comprendre ou compatible.
4. La correction possible.
5. La preuve que c'est corrigé : test, mesure, comparaison ou relecture.

## Phrase de contrôle

Si je retire la vue, le son, la souris ou le contexte, est-ce que le contenu fonctionne encore ?
