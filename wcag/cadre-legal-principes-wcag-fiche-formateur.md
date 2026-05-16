# Cadre légal et principes WCAG - fiche formateur

Formation : 102638 - L'accessibilité numérique pour la bureautique et le web

Public : communicants et producteurs de contenus numériques, niveau initiation.

Position dans la journée : Module 1, après la sensibilisation et les idées reçues, au moment où l'on introduit le cadre légal, le RGAA et la logique des principes WCAG.

Usage : installer une boussole que les stagiaires gardent sous la main pendant les ateliers Word et web.

## Intention pédagogique

Ne pas présenter WCAG comme une liste de critères à apprendre.

Faire comprendre que le cadre légal repose sur une logique simple :

> Un service ou un contenu public doit rester accessible quand la situation de la personne change.

Les principes WCAG servent de boussole pour poser les bonnes questions avant de corriger.

## Phrase à faire retenir

> Accessible, c'est quand l'information reste perceptible, utilisable, compréhensible et lisible par les outils.

Cette phrase doit revenir pendant :

- l'atelier Word Sami ;
- l'atelier web Easy Checks ;
- le module réseaux sociaux ;
- la clôture et le plan d'action.

## Placement précis dans le Module 1

Moment recommandé : après les idées reçues et avant l'analyse de la déclaration d'accessibilité.

Durée : 15 à 20 minutes.

Déroulé :

1. Partir du cadre légal : les acteurs publics ont une obligation d'accessibilité.
2. Expliquer que le RGAA est le référentiel français de contrôle.
3. Dire que le RGAA s'appuie sur la logique WCAG.
4. Introduire les 4 principes comme une grille humaine, pas comme une grille technique.
5. Donner la fiche aux stagiaires : ils la gardent ouverte ou imprimée pour les ateliers.

## Les 4 principes sous forme de questions

| Principe | Question stagiaire | Reformulation métier |
|---|---|---|
| Percevoir | Est-ce que l'information existe encore si je ne vois pas, n'entends pas ou lis difficilement ? | Images, sons, vidéos, contrastes, structure visible. |
| Utiliser | Est-ce que je peux aller jusqu'au bout sans souris, sans geste précis, sans piège ? | Clavier, focus, liens, navigation, temps, actions possibles. |
| Comprendre | Est-ce que je sais quoi faire, quoi corriger et ce qui va se passer ? | Titres, libellés, langage clair, erreurs, aide, cohérence. |
| Compatible | Est-ce que les outils peuvent comprendre le contenu ? | Styles natifs, structure, noms accessibles, rôles, états, export propre. |

## Ce que les stagiaires gardent sous la main

La fiche n'est pas un cours à lire.

C'est une aide pour se poser la bonne question pendant les exercices :

1. Quel est le problème observé ?
2. Quelle personne ou quel usage est bloqué ?
3. Quel principe WCAG est touché ?
4. Quelle preuve montre que c'est corrigé ?

Cette logique vaut pour Word et pour le web.

## Lien avec l'atelier Word

Dans l'atelier Word, les stagiaires travaillent sur :

- `Stagiaire/tp-word-igpde/sami-doc-inaccessible.docx`
- `Stagiaire/tp-word-igpde/sami-doc-aide-correction.docx`
- `Stagiaire/tp-word-igpde/sami-doc-accessible.docx`

Faire utiliser la fiche ainsi :

| Correction Word | Principe principal | Question à poser |
|---|---|---|
| Styles de titres | Compatible + Utiliser | Le lecteur d'écran et le volet de navigation comprennent-ils la structure ? |
| Listes natives | Compatible + Comprendre | La liste est-elle reconnue comme une liste, pas seulement comme des lignes avec tirets ? |
| Texte alternatif | Percevoir | L'information de l'image existe-t-elle pour une personne qui ne la voit pas ? |
| Contraste | Percevoir | Le texte reste-t-il lisible pour une personne malvoyante ou fatiguée ? |
| Liens explicites | Comprendre + Utiliser | Le lien dit-il clairement où il mène ? |
| Langue du document | Comprendre + Compatible | La synthèse vocale prononce-t-elle correctement le texte ? |
| Export PDF | Compatible | La structure Word survit-elle dans le PDF ? |

Consigne atelier Word :

> Pour chaque correction, ne dites pas seulement "c'est mieux". Dites quel usage était bloqué, et quelle preuve montre que le document est devenu plus accessible.

## Lien avec l'atelier web Easy Checks

Point d'entrée :

- `Stagiaire/tp-easy-check-igpde/index.html`

Les 13 points rapides se rattachent aux 4 principes.

| Pages Easy Checks | Principe principal | Question à poser |
|---|---|---|
| #1 Images | Percevoir | L'information portée par l'image existe-t-elle en texte ? |
| #2 Titre de page | Comprendre + Utiliser | La page est-elle identifiable dans un onglet, un historique ou un lecteur d'écran ? |
| #3 Titres | Comprendre + Compatible | La structure de la page est-elle lisible par l'humain et par les outils ? |
| #4 Contrastes | Percevoir | Le contenu reste-t-il lisible dans des conditions dégradées ? |
| #5 Liens d'évitement | Utiliser | Peut-on contourner les blocs répétés ? |
| #6 Clavier et focus | Utiliser | Peut-on agir sans souris et voir où l'on se trouve ? |
| #7 Langue | Comprendre + Compatible | Le passage change-t-il de langue pour la restitution vocale ? |
| #8 Zoom | Percevoir + Utiliser | Le contenu reste-t-il lisible et utilisable agrandi ? |
| #9 Sous-titres | Percevoir | Le son utile existe-t-il en texte synchronisé ? |
| #10 Transcription | Percevoir | Le contenu audio existe-t-il en texte ? |
| #11 Audio-description | Percevoir | Les informations visuelles importantes sont-elles restituées ? |
| #12 Libellés | Comprendre + Compatible | Chaque champ dit-il ce qui est attendu ? |
| #13 Erreurs | Comprendre | L'erreur explique-t-elle comment corriger ? |

Consigne atelier web :

> Une non-conformité n'est validée que si le binôme donne une observation, un principe touché, une personne bloquée et une correction possible.

## Lien avec les réseaux sociaux

La même fiche sert au module réseaux sociaux :

| Cas réseaux sociaux | Principe principal | Réflexe |
|---|---|---|
| Image sans alternative | Percevoir | Ajouter un texte alternatif utile. |
| Texte dans une image | Percevoir + Compatible | Remettre l'information essentielle dans le texte du post. |
| Hashtag illisible | Comprendre | Utiliser le CamelCase. |
| Emojis en série | Comprendre | Limiter, placer, ne pas remplacer les mots utiles. |
| Caractères fantaisie Unicode | Compatible | Éviter les polices décoratives non interprétées correctement. |
| Ordre de lecture confus | Comprendre + Utiliser | Relire le post linéairement, comme il sera vocalisé. |

## Ce qu'il faut éviter

- Ne pas faire apprendre les critères WCAG par coeur.
- Ne pas dérouler le deck condensé comme un catalogue.
- Ne pas commencer par les niveaux A, AA, AAA.
- Ne pas enfermer les stagiaires dans une discussion juridique abstraite.
- Ne pas ajouter de jargon développeur inutile.

## Ce qu'il faut faire vivre

Le cadre légal donne l'obligation.

Le RGAA donne la méthode française de vérification.

WCAG donne la logique de fond.

Les ateliers donnent la preuve.

## Formule de transition vers les ateliers

Dire aux stagiaires :

> Vous n'avez pas besoin de retenir tout WCAG aujourd'hui. Gardez les 4 questions sous la main. À chaque anomalie Word ou web, demandez-vous : est-ce un problème pour percevoir, utiliser, comprendre ou être lu par les outils ?

## Ressources à garder disponibles

- Fiche stagiaire PDF : `Stagiaire/principes-wcag/directives-accessibilite-wcag-anglais-clair.pdf`
- TP Word : `Stagiaire/tp-word-igpde/`
- TP web : `Stagiaire/tp-easy-check-igpde/index.html`
- Cartes idées reçues : `Stagiaire/idées-recues-cartes/`
