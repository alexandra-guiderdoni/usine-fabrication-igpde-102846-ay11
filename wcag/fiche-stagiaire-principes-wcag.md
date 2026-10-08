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

Table: Atelier Word - corrections et personas

| Correction Word | Principe | Qui est bloqué ? | Réflexe |
|--------------------|--------------------|---------------------------|---------------------------------|
| Styles de titres | Compatible + Utiliser | Amir ne peut pas naviguer dans le document | Un titre doit être un vrai style de titre, pas du texte gros et gras |
| Listes natives | Compatible + Comprendre | Amir et Anatole perdent la structure | Une liste doit être une vraie liste, pas des tirets manuels |
| Texte alternatif | Percevoir | Amir ne sait pas ce que l'image contient | Une image utile doit avoir une alternative textuelle |
| Contraste | Percevoir | Anaïs ne peut pas lire le texte | Le contraste doit permettre de lire sans effort (ratio 4.5:1) |
| Liens explicites | Comprendre + Utiliser | Amir et Anatole ne savent pas où mène le lien | Un lien doit annoncer clairement sa destination |
| Langue du document | Comprendre + Compatible | Amir entend une prononciation incorrecte | La langue du document doit être indiquée |
| Export PDF | Compatible | Amir perd toute la structure du document | L'export PDF doit conserver la structure Word |

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
