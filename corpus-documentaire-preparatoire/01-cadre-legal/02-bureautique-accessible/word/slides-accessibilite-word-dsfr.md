---
title: "Rendre un document Word accessible"
subtitle: "22 critères en 5 piliers"
author: Alex
date: 2026-04-02
template: dsfr
lang: fr
footer: "Accessibilité Word — avril 2026"
---

# Rendre un document Word accessible

## Slide 1 — Ce document est-il accessible ?

::: {.columns}
::: {.column width="50%"}
::: {.alert type="error"}
**Document A**

- Titres en gras manuellement
- Image sans texte alternatif
- Tableau avec cellules fusionnées
- Nom : « Document1.docx »
:::
:::
::: {.column width="50%"}
::: {.alert type="success"}
**Document B**

- Titres avec styles Titre 1, Titre 2
- Image avec description fonctionnelle
- Tableau simple avec en-tête identifié
- Nom : « rapport-accessibilite-2024.docx »
:::
:::
:::

### Notes pour l'orateur

- Afficher les 2 colonnes, demander au public : "Lequel choisissez-vous ?" (R9 — deviner avant)
- Laisser 10 secondes puis révéler : visuellement ils sont identiques, seule la structure change (R8 — surprise)
- "Le document A est illisible pour un lecteur d'écran. Le B est parfaitement navigable."
- Timing : 2 min

---

## Slide 2 — Pourquoi ça vous concerne

::: {.kpi}
| 15 % | 80 % | 0 |
|------|------|---|
| de la population en situation de handicap | des handicaps sont invisibles | ligne de code nécessaire |
:::

::: {.highlight}
L'accessibilité Word est 100 % éditoriale : pas de code, pas d'outil spécial, juste les bons réflexes dans le ruban.
:::

### Notes pour l'orateur

- Insister : ce n'est pas une compétence technique, c'est une compétence rédactionnelle (R12 — WIIFM)
- "Vous produisez déjà des documents Word — il s'agit d'utiliser les bonnes fonctionnalités"
- Timing : 2 min

---

## Slide 3 — Quiz : vrai ou faux ?

::: {.stepper}
1. "Un texte en gras taille 16 est un titre pour le lecteur d'écran" → ?
2. "Un tableau créé avec des tabulations est lisible par les TA" → ?
3. "Le vérificateur d'accessibilité de Word détecte tous les problèmes" → ?
:::

### Notes pour l'orateur

- Faire voter à main levée pour chaque affirmation (R14 — récupération active)
- Réponses : 1. FAUX (seuls les styles de titre comptent), 2. FAUX (fonctionnalité Tableau obligatoire), 3. FAUX (premier filtre utile mais incomplet)
- "Si vous avez eu au moins un faux, cette formation va vous faire gagner du temps" (R18 — sécurité psychologique)
- Timing : 3 min

---

## Slide 4 — 5 piliers, 22 critères

::: {.cards}
::: {.card}
**Structure**

Titres, listes, colonnes, tableaux, sauts de page

*6 critères*
:::
::: {.card}
**Couleurs**

Contraste et signification visuelle

*2 critères*
:::
::: {.card}
**Contenus**

Images, liens, zones de texte, informations essentielles

*5 critères*
:::
::: {.card}
**Langue et médias**

Balisage linguistique, transcriptions, clignotement

*4 critères*
:::
::: {.card}
**Finalisation**

Propriétés, nom, formulaires, vérificateur

*5 critères*
:::
:::

### Notes pour l'orateur

- Présenter la carte mentale du parcours : "On avance pilier par pilier, du plus structurant au plus fin" (R4 — chunking)
- "Le pilier Structure représente 60 % de l'effort — c'est là qu'on commence" (R11 — vue d'ensemble)
- Timing : 2 min

---

## Slide 5 — Pilier 1 : les styles de titre

::: {.columns}
::: {.column width="50%"}
::: {.alert type="error"}
**Ce que le lecteur d'écran voit**

"Texte, texte, texte, texte, texte, texte..."

Un bloc plat sans repère de navigation.
:::
:::
::: {.column width="50%"}
::: {.alert type="success"}
**Avec les styles de titre**

"Titre 1 : Rapport annuel > Titre 2 : Budget > Titre 3 : Prévisions..."

Navigation par titres en quelques secondes.
:::
:::
:::

::: {.callout}
**Chemin menu**

Accueil > Styles > Titre 1, Titre 2, Titre 3...

Raccourci : Ctrl+Alt+Maj+S pour ouvrir le volet Styles
:::

### Notes pour l'orateur

- "Imaginez lire un livre de 50 pages sans table des matières — c'est l'expérience d'un utilisateur de lecteur d'écran face à un document sans styles" (R7 — analogie)
- Montrer le volet de navigation (Ctrl+F > onglet Titres) : la preuve visible que les styles fonctionnent
- Timing : 3 min

---

## Slide 6 — Listes, colonnes, sauts de page

| Besoin | Fonctionnalité intégrée | Piège courant |
|--------|------------------------|---------------|
| Liste | Accueil > Puces / Numérotation | Tirets ou chiffres manuels |
| Colonnes | Mise en page > Colonnes | Tabulations ou espaces |
| Saut de page | Insertion > Saut de page (Ctrl+Entrée) | Retours chariot (Entrée x15) |

::: {.alert type="warning"}
**Règle d'or**

Si vous touchez à Tab, Espace ou Entrée pour simuler une mise en page, vous créez une barrière invisible.
:::

### Notes pour l'orateur

- Exercice en binôme (2 min) : "Ouvrez un de vos documents récents, ouvrez Maj+F1 (Révéler la mise en forme), cliquez sur une liste — voyez-vous 'Puces et numérotation' ?" (R17 — apprentissage social)
- Vérification listes : le volet doit afficher la catégorie "Puces et numérotation"
- Vérification colonnes : le volet doit afficher "Colonnes" sous "Section"
- Timing : 3 min

---

## Slide 7 — Tableaux de mise en page

::: {.stepper}
1. Insertion > Tableau > nombre de colonnes et lignes
2. Remplir le contenu (gauche à droite, haut en bas)
3. Vérifier l'ordre : Tab dans la 1re cellule, parcourir avec Tab
4. Vérifier l'alignement : clic droit > Propriétés > Habillage = Aucun
:::

::: {.alert type="info"}
**Pourquoi "Aucun" ?**

Un tableau avec habillage "Autour" flotte sur la page — le lecteur d'écran ne le lit pas au bon moment par rapport au reste du contenu.
:::

### Notes pour l'orateur

- Distinguer clairement tableau de mise en page (pas d'en-têtes, juste de l'organisation) et tableau de données (en-têtes nécessaires)
- "Le piège classique : copier-coller un tableau depuis un autre document et ne pas vérifier l'habillage" (R6 — storytelling mini)
- Timing : 2 min

---

## Slide 8 — Tableaux de données

::: {.columns}
::: {.column width="60%"}
| Exigence | Comment |
|----------|---------|
| Créer avec l'outil intégré | Insertion > Tableau (jamais d'image) |
| Pas de cellules fusionnées/divisées | Tableau simple uniquement |
| Identifier la ligne d'en-tête | Clic droit > Propriétés > Ligne > Répéter en tant que ligne d'en-tête |
| Aligner avec le texte | Propriétés > Tableau > Habillage = Aucun |
:::
::: {.column width="40%"}
::: {.alert type="warning"}
**Limitation**

Les tableaux complexes (multi-niveaux d'en-têtes, cellules fusionnées) ne peuvent pas être rendus accessibles dans Word.

Solution : convertir en PDF accessible.
:::
:::
:::

### Notes pour l'orateur

- Montrer la différence entre "Outils Image" (= image de tableau, inaccessible) et "Outils de tableau" (= vrai tableau)
- "Répéter en tant que ligne d'en-tête" : invisible visuellement mais capital pour les TA sur les tableaux multi-pages
- Timing : 3 min

---

## Slide 9 — Quiz mi-parcours : structure

::: {.callout}
**Votre collègue vous envoie un document Word. Comment vérifiez-vous en 30 secondes si la structure est accessible ?**

A. Vous regardez si les titres sont en gras

B. Vous ouvrez le volet de navigation (Ctrl+F) et vérifiez que les titres y apparaissent

C. Vous lancez le correcteur orthographique

D. Vous vérifiez que le fichier est en .docx
:::

### Notes pour l'orateur

- Faire voter (R14 — récupération active). Bonne réponse : B (le volet de navigation est le test ultime de la structure)
- "D est nécessaire mais pas suffisant — le format .docx est un prérequis, pas une preuve d'accessibilité"
- Feedback immédiat après le vote (R19)
- Timing : 2 min

---

## Slide 10 — Pilier 2 : contraste des couleurs

::: {.columns}
::: {.column width="50%"}
| Type de texte | Ratio minimum |
|---------------|---------------|
| Standard (< 14 pt gras) | **4,5:1** |
| Grande taille (>= 14 pt gras ou >= 18 pt) | **3:1** |
:::
::: {.column width="50%"}
::: {.callout}
**Outil**

Colour Contrast Analyser (CCA) de TPGi

Pipette premier plan (texte) + pipette arrière-plan (fond) = ratio instantané
:::
:::
:::

::: {.highlight}
Texte noir sur fond blanc = toujours conforme. Le test ne s'applique qu'aux textes colorés ou sur fond coloré.
:::

### Notes pour l'orateur

- Si possible, projeter CCA en direct sur un extrait de document (R5 — double codage : la slide montre le ratio, l'oral montre l'outil)
- "Les designers graphiques connaissent ce ratio — votre rôle est de vérifier, pas de deviner" (R21 — scaffolding)
- Timing : 2 min

---

## Slide 11 — La couleur ne suffit jamais

::: {.columns}
::: {.column width="50%"}
::: {.alert type="error"}
**Inaccessible**

| Projet | Statut |
|--------|--------|
| Migration | (rouge) |
| Formation | (vert) |
| Audit | (jaune) |

Un daltonien voit 3 couleurs identiques.
:::
:::
::: {.column width="50%"}
::: {.alert type="success"}
**Accessible**

| Projet | Statut |
|--------|--------|
| Migration | En retard |
| Formation | Terminé |
| Audit | En cours |

Le texte porte l'information, la couleur la renforce.
:::
:::
:::

### Notes pour l'orateur

- "8 % des hommes sont daltoniens — dans une réunion de 12 personnes, il y en a probablement un" (R8 — fait surprenant)
- Règle simple : si vous imprimez en noir et blanc, l'information est-elle toujours compréhensible ?
- Timing : 2 min

---

## Slide 12 — Pilier 3 : texte alternatif

::: {.stepper}
1. Sélectionner l'image > clic droit > Format de l'image > Texte de remplacement
2. Image significative : décrire la **fonction**, pas l'apparence
3. Image décorative : insérer des espaces vides dans le champ Description
:::

::: {.columns}
::: {.column width="50%"}
::: {.alert type="error"}
**Mauvais texte alt**

"Photo d'un graphique en barres colorées"
:::
:::
::: {.column width="50%"}
::: {.alert type="success"}
**Bon texte alt**

"Évolution du chiffre d'affaires 2020-2024 : hausse de 15 % à 23 %"
:::
:::
:::

### Notes pour l'orateur

- Test mental : "Si je remplace l'image par le texte alt, est-ce que le document reste compréhensible ?" (R7 — analogie)
- Exercice rapide : montrer une image, demander au public de rédiger un texte alt en 15 secondes, comparer (R17 — apprentissage social)
- Timing : 3 min

---

## Slide 13 — Alignement et zones de texte

| Objet | Exigence | Chemin menu |
|-------|----------|-------------|
| Images | Aligné sur le texte | Outils Image > Format > Position > Aligné sur le texte |
| Formes | Aligné sur le texte | Idem |
| Zones de texte | Aligné sur le texte (ou éviter) | Idem |

::: {.alert type="warning"}
**Piège des zones de texte**

Même alignées, les zones de texte peuvent être lues dans un ordre inattendu. Les éviter quand c'est possible — préférer les mises en page avec tableaux ou colonnes intégrées.
:::

### Notes pour l'orateur

- "Objet flottant = objet invisible pour le lecteur d'écran" — phrase à retenir (R3 — charge cognitive réduite)
- Le vérificateur d'accessibilité signale les objets non alignés (on le verra dans le pilier 5)
- Timing : 2 min

---

## Slide 14 — Liens descriptifs

::: {.columns}
::: {.column width="50%"}
::: {.alert type="error"}
**Inaccessible**

- "Cliquez ici"
- "En savoir plus"
- "https://www.exemple.fr/page?id=4827&ref=nav"
:::
:::
::: {.column width="50%"}
::: {.alert type="success"}
**Accessible**

- "Consulter le guide d'accessibilité Word"
- "Télécharger le rapport annuel 2024 (PDF, 2 Mo)"
- "Accéder au formulaire de contact"
:::
:::
:::

::: {.callout}
**Méthode**

Sélectionner le texte descriptif > clic droit > Lien hypertexte (Ctrl+K) > coller l'URL

Attention : supprimer le dernier caractère du texte d'un lien supprime le lien entier.
:::

### Notes pour l'orateur

- "Un utilisateur de lecteur d'écran navigue souvent de lien en lien — imaginez entendre 'cliquez ici, cliquez ici, cliquez ici' sans contexte" (R7 — analogie)
- Pour les documents imprimés ET numériques : inclure l'URL entre parenthèses après le texte descriptif
- Timing : 2 min

---

## Slide 15 — Informations essentielles invisibles

::: {.callout}
**Ce que les TA ne lisent pas automatiquement**

- En-têtes de page
- Pieds de page
- Filigranes
:::

::: {.highlight}
Si une information est essentielle ("CONFIDENTIEL", "Répondre avant le 15 avril", "Ne pas diffuser"), elle doit être reproduite dans le corps du document, idéalement au début.
:::

### Notes pour l'orateur

- "Vous mettez 'CONFIDENTIEL' en filigrane pour que tout le monde le voie — sauf que 15 % de vos lecteurs ne le voient pas du tout" (R8 — surprise, R12 — WIIFM)
- Solution simple : une ligne au début du document reprenant l'information du filigrane
- Timing : 2 min

---

## Slide 16 — Pilier 4 : langue et médias

::: {.columns}
::: {.column width="50%"}
::: {.callout}
**Balisage de langue**

1. Langue principale : Fichier > Options > Langue
2. Passage étranger : sélectionner > Révision > Langue > Définir la langue de vérification

Sans balisage, le lecteur d'écran prononce "meeting" comme "mé-é-ting" avec l'accent français.
:::
:::
::: {.column width="50%"}

| Média intégré | Alternative requise |
|---------------|---------------------|
| Audio seul | Transcription textuelle |
| Vidéo seule | Description textuelle |
| Audio + vidéo | Sous-titres ET description audio |

:::
:::
:::

### Notes pour l'orateur

- Faire écouter une synthèse vocale lisant un mot anglais avec le balisage français (si possible) — l'effet est immédiat (R8 — surprise)
- "La plupart de vos documents contiennent au moins un anglicisme — feedback, planning, reporting. Chaque mot mérite son balisage"
- Timing : 3 min

---

## Slide 17 — Objets clignotants : tolérance zéro

::: {.alert type="error"}
**Interdit — aucune exception**

Animations de clignotement, GIF avec flashs, vidéos avec séquences > 3 Hz

Risque : crise d'épilepsie. Un document contenant un objet clignotant ne peut jamais être considéré comme accessible.
:::

::: {.highlight}
Si vous hésitez sur un GIF animé : supprimez-le et remplacez-le par une image statique.
:::

### Notes pour l'orateur

- Court et direct — pas besoin de nuancer, c'est un interdit absolu
- "C'est le seul critère où la sanction est binaire : un seul objet clignotant = document non accessible, point final"
- Timing : 1 min

---

## Slide 18 — Pilier 5 : avant de publier

::: {.stepper}
1. **Propriétés** : Fichier > Informations > renseigner Titre, Auteur, Objet
2. **Nom de fichier** : descriptif + extension .docx (pas "Document1.docx")
3. **Protection** : Révision > Restreindre la modification > aucune restriction active
4. **Formulaires** : aucun champ de formulaire Word (utiliser un autre outil)
5. **Vérificateur** : Fichier > Vérifier la présence de problèmes > Vérifier l'accessibilité
:::

### Notes pour l'orateur

- "Ces 5 vérifications prennent 2 minutes et attrapent 80 % des oublis restants" (R12 — WIIFM)
- Insister sur les propriétés du document : le titre dans les propriétés est celui que les TA annoncent à l'ouverture du fichier — ce n'est pas le nom du fichier
- Timing : 3 min

---

## Slide 19 — Le vérificateur : allié imparfait

::: {.columns}
::: {.column width="50%"}
::: {.alert type="success"}
**Ce qu'il détecte**

- Texte alt manquant
- Objets non alignés
- Styles de titre absents
- Tableaux sans en-tête
- Ordre de lecture
:::
:::
::: {.column width="50%"}
::: {.alert type="warning"}
**Ce qu'il ne détecte PAS**

- Qualité du texte alt
- Pertinence des noms de liens
- Couleur porteuse de sens
- Langue des passages étrangers
- Contraste insuffisant
:::
:::
:::

::: {.highlight}
Le vérificateur est un premier filtre, pas un certificat de conformité. La vérification manuelle reste indispensable.
:::

### Notes pour l'orateur

- "Pensez au vérificateur comme au correcteur orthographique : il attrape les fautes évidentes, mais il ne garantit pas que votre texte est bien écrit" (R7 — analogie)
- Montrer le vérificateur en direct si possible : Fichier > Vérifier la présence de problèmes > Vérifier l'accessibilité
- Timing : 2 min

---

## Slide 20 — Quiz final : trouvez les erreurs

::: {.callout}
**Un document Word contient :**

- Un titre "Introduction" mis en gras Arial 16 (sans style)
- Un tableau de 3 colonnes avec la 1re ligne en gras (sans "Répéter en tant que ligne d'en-tête")
- Un lien "cliquez ici pour le formulaire"
- Un filigrane "PROJET" sans mention dans le corps du document
- Une photo de l'équipe sans texte alternatif

**Combien d'erreurs d'accessibilité comptez-vous ?**
:::

### Notes pour l'orateur

- Faire compter individuellement, puis partager (R14 — récupération active)
- Réponse : 5 erreurs (une par point). Parcourir chacune et rappeler le critère correspondant
- "Si vous les avez toutes trouvées, vous avez intégré les 5 piliers" (R25 — métacognition)
- Timing : 3 min

---

## Slide 21 — Matrice effort/impact

| | Effort faible | Effort modéré |
|---|---------------|---------------|
| **Impact fort** | Styles de titre, listes intégrées, nom de fichier descriptif, propriétés du document | Texte alternatif, liens descriptifs, tableaux de données avec en-têtes |
| **Impact modéré** | Sauts de page, colonnes intégrées, langue des passages étrangers | Contraste couleurs, alignement objets, zones de texte |

::: {.highlight}
Commencez par le quadrant haut-gauche : 5 actions à effort faible qui transforment immédiatement l'accessibilité de vos documents.
:::

### Notes pour l'orateur

- "Si vous ne retenez qu'une chose : les styles de titre. C'est le quick win numéro 1 — 10 secondes par titre, impact maximal" (R2 — primauté et récence)
- La matrice sert de feuille de route personnelle pour les semaines suivantes
- Timing : 2 min

---

## Slide 22 — Checklist : vos 21 critères

| # | Critère | Pilier |
|---|---------|--------|
| 1 | Fichier .docx avec nom descriptif | Finalisation |
| 2 | Document non protégé | Finalisation |
| 3 | Titres avec styles intégrés | Structure |
| 4 | Hiérarchie cohérente dans le volet de navigation | Structure |
| 5 | Listes avec Puces/Numérotation | Structure |
| 6 | Colonnes avec l'outil Colonnes | Structure |
| 7 | Sauts de page (pas retours chariot) | Structure |
| 8 | Tableaux de mise en page : ordre + alignement | Structure |
| 9 | Tableaux de données : en-têtes + alignement | Structure |
| 10 | Contraste >= 4,5:1 ou >= 3:1 | Couleurs |
| 11 | Couleur porteuse de sens doublée en texte | Couleurs |
| 12 | Texte alt sur images/objets significatifs | Contenus |
| 13 | Images et objets alignés sur le texte | Contenus |
| 14 | Liens avec noms descriptifs | Contenus |
| 15 | Infos essentielles reproduites dans le corps | Contenus |
| 16 | Langue des passages étrangers balisée | Langue |
| 17 | Médias avec alternatives | Langue/médias |
| 18 | Aucun objet clignotant | Langue/médias |
| 19 | Propriétés du document renseignées | Finalisation |
| 20 | Aucun formulaire Word | Finalisation |
| 21 | Vérificateur d'accessibilité sans erreur | Finalisation |

### Notes pour l'orateur

- Distribuer la checklist imprimée ou la partager en version numérique
- "Imprimez-la, collez-la à côté de votre écran. Après 2 semaines, la plupart des réflexes seront automatiques" (R26 — transformation)
- Timing : 2 min

---

## Slide 23 — Demain à 9h

::: {.highlight}
Quelle est la première chose que vous ferez sur votre prochain document Word ?
:::

::: {.cards}
::: {.card}
**Réflexe 1**

Ctrl+F > onglet Titres

Vérifier que tous les titres apparaissent dans le volet de navigation
:::
::: {.card}
**Réflexe 2**

Clic droit sur chaque image > Texte de remplacement

Décrire la fonction, pas l'apparence
:::
::: {.card}
**Réflexe 3**

Fichier > Vérifier l'accessibilité

Corriger les erreurs signalées avant d'envoyer
:::
:::

### Notes pour l'orateur

- Demander à chaque participant de choisir SON premier réflexe et de le noter (R24 — plan d'action)
- "3 réflexes, 30 secondes chacun, 90 % des problèmes couverts" (R15 — répétitions espacées : rappel des concepts clés)
- Clôturer avec énergie : "Vous avez maintenant les outils — à vous de jouer" (R22 — neurones miroirs)
- Timing : 2 min
