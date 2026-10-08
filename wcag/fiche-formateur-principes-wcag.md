# Cadre légal et principes WCAG - fiche formateur

<!-- Contournement WeasyPrint 68 : un tableau fragmenté entre deux pages fait
     échouer la génération PDF/UA-1 (« Table wrapper without a table »).
     Ce style garde chaque tableau entier sur une page, en police de 9 pt. La largeur
     des colonnes est fixée par les tirets de la ligne de séparation de chaque
     tableau : colonnes courtes étroites, colonnes de phrases larges. Dans les
     sections Word et Easy Checks, intertitre, introduction, liste, tableau et
     consigne restent attachés : sans cela, l'introduction restait seule en bas de
     page et le tableau partait à la page suivante. Pas de césure dans les en-têtes
     ni dans les deux colonnes de mots-clés : le gabarit Pandoc l'active partout et
     coupait « Cou-leur » ou « Com-prendre ». -->
<style>table { break-inside: avoid; font-size: 9pt; } section#lien-avec-latelier-word > ul, section#lien-avec-latelier-web-easy-checks > ul { break-inside: avoid; } section#lien-avec-latelier-word > h2, section#lien-avec-latelier-word > p, section#lien-avec-latelier-word > ul, section#lien-avec-latelier-web-easy-checks > h2, section#lien-avec-latelier-web-easy-checks > p, section#lien-avec-latelier-web-easy-checks > ul { break-after: avoid; } th, td:nth-child(-n+2) { hyphens: manual; }</style>

<!-- Sommaire sur la première page : le gabarit formation place la page de garde
     (header#title-block-header) seule sur une page. Ici elle n'impose plus de saut
     de page et son espace haut est réduit : bandeau, titre et sommaire tiennent sur
     la page 1. Le sous-titre est masqué : le générateur y met le premier intertitre
     (« Intention pédagogique »), qui figure déjà dans le sommaire.
     Pied de page « Page X / Y » sur toutes les pages, première comprise. -->
<style>header#title-block-header { break-after: avoid; padding: 2em 0 0.5em 0; } header#title-block-header .subtitle { display: none; } @page { @bottom-center { content: "Page " counter(page) " / " counter(pages); } } @page :first { @bottom-center { content: "Page " counter(page) " / " counter(pages); } }</style>

Formation : 102846 - L'accessibilité numérique pour la bureautique et le web

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

Moment recommandé : après les personas (slide matrice personas x WCAG) et avant l'analyse de la déclaration d'accessibilité.

Durée : 15 à 20 minutes.

Déroulé :

1. Partir du cadre légal : les acteurs publics ont une obligation d'accessibilité.
2. Expliquer que le RGAA est le référentiel français de contrôle.
3. Dire que le RGAA s'appuie sur la logique WCAG.
4. Introduire les 4 principes comme une grille humaine, pas comme une grille technique.
5. Relier chaque principe aux personas vus dans la séquence précédente.
6. Donner la fiche aux stagiaires : ils la gardent ouverte ou imprimée pour les ateliers.

## Les 4 principes sous forme de questions

Table: Les 4 principes WCAG et les personas concernés

| Repère | Principe | Question stagiaire | Reformulation métier | Personas concernés |
|--------------|-----------------|------------------------------|----------------------|-----------------|
| 1.x | Percevoir | Est-ce que l'information existe encore si je ne vois pas, n'entends pas ou lis difficilement ? | Images, sons, vidéos, contrastes, structure visible. | Amir, Anaïs, Justine |
| 2.x | Utiliser | Est-ce que je peux aller jusqu'au bout sans souris, sans geste précis, sans piège ? | Clavier, focus, liens, navigation, temps, actions possibles. | Agathe |
| 3.x | Comprendre | Est-ce que je sais quoi faire, quoi corriger et ce qui va se passer ? | Titres, libellés, langage clair, erreurs, aide, cohérence. | Anatole, Paul |
| 4.x | Compatible | Est-ce que les outils peuvent comprendre le contenu ? | Styles natifs, structure, noms accessibles, rôles, états, export propre. | Amir (lecteur d'écran), tous les utilisateurs de technologies d'assistance |

### Conseil formateur : vocabulaire

Ne pas utiliser le mot « robuste » (traduction officielle de Robust). Les stagiaires non-techniques décrochent. Dire « lisible par les outils » ou « compatible avec les technologies d'assistance ». Le mot « compatible » est celui qui passe le mieux à l'oral.

### Repères des cartes

Le premier chiffre du critère indique le principe WCAG : 1 pour Perceptible, 2 pour Utilisable, 3 pour Compréhensible et 4 pour Robuste, reformulé ici « Compatible ». La couleur d'une carte indique son niveau de conformité A, AA ou AAA, jamais son principe. Les badges colorés des slides personas restent de simples repères visuels et ne doivent pas être présentés comme le code couleur des principes WCAG.

## Ce que les stagiaires gardent sous la main

La fiche n'est pas un cours à lire.

C'est une aide pour se poser la bonne question pendant les exercices :

1. Quel est le problème observé ?
2. Quel persona est bloqué (quel usage concret) ?
3. Quel principe WCAG est touché ?
4. Quelle preuve montre que c'est corrigé ?

Cette logique vaut pour Word et pour le web.

## Lien avec l'atelier Word

Dans l'atelier Word, les stagiaires travaillent sur :

- `Livrables-Stagiaires/tp-word-igpde/tp-doc-inaccessible.docx`
- `Livrables-Stagiaires/tp-word-igpde/tp-doc-aide-correction.docx`
- `Livrables-Stagiaires/tp-word-igpde/tp-doc-accessible.docx`

Faire utiliser la fiche ainsi :

Table: Corrections Word et principes WCAG

| Correction Word | Principe principal | Qui est bloqué ? | Question à poser |
|--------------------|--------------------|--------------------|----------------------------------------|
| Styles de titres | Compatible + Utiliser | Amir (lecteur d'écran) | Le lecteur d'écran et le volet de navigation comprennent-ils la structure ? |
| Listes natives | Compatible + Comprendre | Amir, Anatole | La liste est-elle reconnue comme une liste, pas seulement comme des lignes avec tirets ? |
| Texte alternatif | Percevoir | Amir (aveugle) | L'information de l'image existe-t-elle pour une personne qui ne la voit pas ? |
| Contraste | Percevoir | Anaïs (malvoyante) | Le texte reste-t-il lisible pour une personne malvoyante ou fatiguée ? |
| Liens explicites | Comprendre + Utiliser | Amir, Anatole | Le lien dit-il clairement où il mène ? |
| Langue du document | Comprendre + Compatible | Amir (synthèse vocale) | La synthèse vocale prononce-t-elle correctement le texte ? |
| Export PDF | Compatible | Amir (lecteur d'écran) | La structure Word survit-elle dans le PDF ? |

Consigne atelier Word :

> Pour chaque correction, ne dites pas seulement « c'est mieux ». Dites quel persona serait bloqué, quel principe WCAG est touché, et quelle preuve montre que le document est devenu plus accessible.

## Lien avec l'atelier web Easy Checks

Point d'entrée :

- `Livrables-Stagiaires/tp-easy-check-site-web-igpde/index.html`

Les 13 points rapides se rattachent aux 4 principes.

Table: Easy Checks et principes WCAG

| Pages Easy Checks | Principe principal | Qui est bloqué ? | Question à poser |
|--------------------|--------------------|--------------------|----------------------------------------|
| #1 Images | Percevoir | Amir (aveugle) | L'information portée par l'image existe-t-elle en texte ? |
| #2 Titre de page | Comprendre + Utiliser | Amir, Anatole | La page est-elle identifiable dans un onglet, un historique ou un lecteur d'écran ? |
| #3 Titres | Comprendre + Compatible | Amir, Anatole | La structure de la page est-elle lisible par l'humain et par les outils ? |
| #4 Contrastes | Percevoir | Anaïs (malvoyante) | Le contenu reste-t-il lisible dans des conditions dégradées ? |
| #5 Liens d'évitement | Utiliser | Agathe (clavier) | Peut-on contourner les blocs répétés ? |
| #6 Clavier et focus | Utiliser | Agathe (motrice) | Peut-on agir sans souris et voir où l'on se trouve ? |
| #7 Langue | Comprendre + Compatible | Amir (synthèse vocale) | Le passage change-t-il de langue pour la restitution vocale ? |
| #8 Zoom | Percevoir + Utiliser | Anaïs (malvoyante) | Le contenu reste-t-il lisible et utilisable agrandi ? |
| #9 Sous-titres | Percevoir | Justine (sourde) | Le son utile existe-t-il en texte synchronisé ? |
| #10 Transcription | Percevoir | Justine (sourde) | Le contenu audio existe-t-il en texte ? |
| #11 Audio-description | Percevoir | Amir (aveugle) | Les informations visuelles importantes sont-elles restituées ? |
| #12 Libellés | Comprendre + Compatible | Anatole (cognitif) | Chaque champ dit-il ce qui est attendu ? |
| #13 Erreurs | Comprendre | Anatole, Paul | L'erreur explique-t-elle comment corriger ? |

Consigne atelier web :

> Une non-conformité n'est validée que si le binôme donne une observation, un persona bloqué, un principe touché et une correction possible.

## Lien avec les réseaux sociaux

La même fiche sert au module réseaux sociaux :

Table: Réseaux sociaux et principes WCAG

| Cas réseaux sociaux | Principe principal | Qui est bloqué ? | Réflexe |
|------------------------|--------------------|------------------------|--------------------------------|
| Image sans alternative | Percevoir | Amir (aveugle) | Ajouter un texte alternatif utile. |
| Texte dans une image | Percevoir + Compatible | Amir (lecteur d'écran) | Remettre l'information essentielle dans le texte du post. |
| Hashtag illisible | Comprendre | Amir (synthèse vocale), Paul | Utiliser le CamelCase. |
| Emojis en série | Comprendre | Amir (chaque emoji est vocalisé) | Limiter, placer en fin, ne pas remplacer les mots utiles. |
| Caractères fantaisie Unicode | Compatible | Amir (charabia vocalisé) | Éviter les polices décoratives non interprétées correctement. |
| Ordre de lecture confus | Comprendre + Utiliser | Amir, Paul | Relire le post linéairement, comme il sera vocalisé. |

## Ce qu'il faut éviter

- Ne pas faire apprendre les critères WCAG par cœur.
- Ne pas dérouler le deck condensé comme un catalogue.
- Ne pas commencer par les niveaux A, AA, AAA.
- Ne pas enfermer les stagiaires dans une discussion juridique abstraite.
- Ne pas ajouter de jargon développeur inutile.
- Ne pas utiliser le mot « robuste » — dire « compatible » ou « lisible par les outils ».

## Ce qu'il faut faire vivre

Le cadre légal donne l'obligation.

Le RGAA donne la méthode française de vérification.

WCAG donne la logique de fond.

Les personas donnent le visage humain.

Les ateliers donnent la preuve.

## Formule de transition vers les ateliers

Dire aux stagiaires :

> Vous n'avez pas besoin de retenir tout WCAG aujourd'hui. Gardez les 4 questions et les 6 visages sous la main. À chaque anomalie Word ou web, demandez-vous : qui est bloqué, et est-ce un problème pour percevoir, utiliser, comprendre ou être lu par les outils ?

## Sources et références

- AAArdvark : WCAG en anglais clair — https://aaardvarkaccessibility.com/wcag-plain-english/
- Cartes WCAG 2.2 (Figma) — https://www.figma.com/community/file/1409436654182046971/wcag-2-2-card-deck
- Fiche stagiaire PDF : `Livrables-Stagiaires/fil-rouge-principes-wcag-igpde/fiche-stagiaire-principes-wcag.pdf`
- TP Word : `Livrables-Stagiaires/tp-word-igpde/`
- TP web : `Livrables-Stagiaires/tp-easy-check-site-web-igpde/index.html`
- Cartes idées reçues : `Livrables-Stagiaires/ice-breaker-idées-recues-cartes-igpde/`
