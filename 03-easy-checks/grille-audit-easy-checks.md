# Carnet de diagnostic guidé - 13 points de contrôle rapides

Ce document décrit le classeur `grille-audit-easy-checks.xlsx` utilisé pendant la formation IGPDE 102846 « L'accessibilité numérique pour la bureautique et le web ».

> **Avertissement**
>
> Ce carnet est un outil de sensibilisation et de pré-diagnostic. Il ne remplace pas un audit RGAA formel et ne produit aucun taux de conformité.

## Objectif pédagogique

Pour chaque point de contrôle, le binôme :

1. ouvre la page correspondante du site à auditer ;
2. réalise le test proposé ;
3. documente un écart observé ;
4. propose sa mise en conformité ;
5. conserve une preuve permettant de retrouver l'écart.

Un seul écart correctement prouvé suffit à documenter le point. Les occurrences supplémentaires peuvent enrichir la restitution collective, sans être obligatoires.

## Structure du classeur

Le classeur contient 15 onglets :

- `Démarrer` : consignes, informations communes, accès aux 13 pages d'exercice, puis liens vers l'aide et la version corrigée ;
- 13 fiches verticales : une page du site et un point de contrôle par onglet ;
- `Synthèse` : reprise automatique des trois champs renseignés dans chaque fiche.

Chaque fiche indique :

- la page à auditer ;
- les slides projetées ;
- la question à tester ;
- les références WCAG 2.2 et RGAA 4.1.2 ;
- la méthode de test ;
- ce qu'il faut rendre conforme.

## Les trois champs à renseigner

| Champ | Contenu attendu |
|---|---|
| Constat | Ce qui est observé concrètement sur la page. |
| Mise en conformité à réaliser | Ce que l'équipe doit modifier pour corriger l'écart. |
| Preuve de l'écart | URL, capture, sélecteur ou extrait permettant de retrouver l'écart. |

L'objectif est de documenter l'écart et de proposer sa correction, pas de calculer un score.

## Les 13 fiches

| # | Point testé | WCAG 2.2 | Page d'exercice |
|---|---|---|---|
| 1 | Texte alternatif des images | 1.1.1 - Contenu non textuel | `site-inaccessible/ec01-images.html` |
| 2 | Titre de page | 2.4.2 - Titre de page | `site-inaccessible/ec02-page-title.html` |
| 3 | Titres et hiérarchie | 1.3.1 - Information et relations ; 2.4.6 - En-têtes et étiquettes | `site-inaccessible/ec03-headings.html` |
| 4 | Contraste des couleurs | 1.4.3 - Contraste minimum ; 1.4.11 - Contraste du contenu non textuel | `site-inaccessible/ec04-contrast.html` |
| 5 | Lien d'évitement | 2.4.1 - Contourner des blocs | `site-inaccessible/ec05-skiplinks.html` |
| 6 | Focus et navigation clavier | 2.1.1 ; 2.1.2 ; 2.4.3 ; 2.4.7 | `site-inaccessible/ec06-keyboard-focus.html` |
| 7 | Langue de la page | 3.1.1 - Langue de la page ; 3.1.2 - Langue d'un passage | `site-inaccessible/ec07-language.html` |
| 8 | Zoom à 200 % | 1.4.4 - Redimensionnement du texte ; 1.4.10 - Redistribution ; 1.4.12 - Espacement du texte | `site-inaccessible/ec08-zoom.html` |
| 9 | Sous-titres vidéo | 1.2.2 - Sous-titres pour un média pré-enregistré | `site-inaccessible/ec09-captions.html` |
| 10 | Transcriptions audio et vidéo | 1.2.1 - Contenu seulement audio ou vidéo pré-enregistré | `site-inaccessible/ec10-transcript.html` |
| 11 | Audiodescription | 1.2.3 - Audiodescription ou version de remplacement ; 1.2.5 - Audiodescription | `site-inaccessible/ec11-audio-description.html` |
| 12 | Étiquettes de formulaire | 1.3.1 ; 2.5.3 ; 3.3.2 | `site-inaccessible/ec12-form-labels.html` |
| 13 | Champs obligatoires et erreurs | 3.3.1 ; 3.3.2 ; 3.3.3 | `site-inaccessible/ec13-required-errors.html` |

## Déroulé conseillé

1. Renseigner l'auditeur, la date, le navigateur et les outils dans `Démarrer`.
2. Choisir quelques fiches avec son binôme.
3. Tester d'abord la version volontairement inaccessible.
4. Renseigner les trois champs sans consulter l'aide.
5. Comparer ensuite avec l'aide à la correction et la version corrigée.
6. Utiliser `Synthèse` pour la restitution orale : point contrôlé, constat, preuve et correction proposée.

Une cellule `À renseigner` dans la synthèse signale uniquement qu'aucun constat n'a encore été saisi. Elle ne constitue pas un verdict.

## Références

- Points de contrôle rapides W3C WAI : https://www.w3.org/WAI/test-evaluate/easy-checks/
- WCAG 2.2 : https://www.w3.org/TR/WCAG22/
- RGAA 4.1.2 : https://accessibilite.numerique.gouv.fr/
- Corpus français du dépôt : `03-easy-checks/w3c-easy-checks-fr.md`
- Correspondance WCAG / RGAA : `03-easy-checks/correspondance-wcag-rgaa.md`
