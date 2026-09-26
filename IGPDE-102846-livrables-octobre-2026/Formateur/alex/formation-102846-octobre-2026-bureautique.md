# Documents bureautiques accessibles

Mise en pratique

## Diapositive 1 - Le lecteur d'écran en action

Texte, texte, texte, texte, texte, texte ...
Pendant 4 minutes. Sans titre. Sans repère.
Sans pouvoir naviguer vers la section qui le concerne.
-> C'est ce qu'entend une personne malvoyante face à votre document Word.

15 % de vos destinataires sont concernés

• 80 % de ces handicaps sont invisibles
• Dans une réunion de 12 personnes : au moins 1 daltonien
• Parmi 30 destinataires : 4 ou 5 ont un handicap

## Diapositive 2 - Quiz - lequel de ces deux documents est accessible ?

Ils sont visuellement identiques. Lequel préférez-vous pour NVDA ?

Document A

• Titres mis en gras, police Arial 16
• Image sans description
• Fichier nommé Document1.docx

Document B

• Titres avec le style « Titre 1 »
• Image avec texte alternatif
• Fichier nommé rapport-bilan-2024.docx

Votre réponse ?

## Diapositive 3 - Pourquoi ça vous concerne

15 % de vos destinataires sont concernés par un handicap

80 % de ces handicaps sont invisibles - rien ne le montre

0 ligne de code nécessaire - uniquement des réflexes dans le ruban Word

Réponse au quiz : Document B

• Le style Titre 1 crée une structure de navigation
• Le texte de remplacement décrit la fonction de l'image
• Le nom de fichier permet de retrouver le document

## Diapositive 4 - 5 thèmes, 21 critères

Chaque thème = des critères actionnables immédiatement dans le ruban Word.

| Thème | Ce que vous allez apprendre |
| --- | --- |
| 1. Structure | Titres, listes, colonnes, tableaux, sauts de page |
| 2. Couleurs | Rapport de contraste, couleur porteuse de sens |
| 3. Contenu alternatif | Texte alternatif, objets alignés, liens descriptifs |
| 4. Langue et lisibilité | Balisage linguistique, majuscules, espaces répétés |
| 5. Finalisation | Vérificateur d'accessibilité, propriétés du document, export PDF |

## Diapositive 5 - Les styles de titre : le fondement de tout

Comment un lecteur d'écran repère-t-il les titres dans Word ?

Sans styles de titre

• Un bloc plat, sans repère de navigation
• Le lecteur d'écran ne peut pas aller de titre en titre
• L'utilisateur doit écouter tout le document

Avec Titre 1, Titre 2, Titre 3

• Titre 1 : Rapport annuel
• Titre 2 : Budget / Titre 3 : Prévisions
• Navigation rapide, comme une table des matières

Comment faire

• Appliquer : Accueil > Styles > Titre 1, Titre 2 ou Titre 3
• Vérifier : Ctrl+F > onglet Titres

## Diapositive 6 - Listes natives

✓ Liste accessible

• Le lecteur annonce : liste de 3 éléments, élément 1 sur 3
• Navigation par élément avec les touches flèches
• Créer avec : Accueil > Paragraphe > Puces ou Numérotation

✗ Liste inaccessible

• Tirets manuels : le lecteur lit tiret Premier élément
• Tabulations pour simuler une numérotation
• Réseaux d'espaces pour aligner visuellement

Vérification

• Maj+F1 (Révéler la mise en forme) > Puces et numérotation doit apparaître

## Diapositive 7 - Tableaux et objets flottants

Règle d'or : ne jamais utiliser Tab, Espace ou Entrée pour simuler une mise en page.
Vous créez un obstacle de structure pour les technologies d'assistance.

Tableaux de mise en page

• Insertion > Tableau > colonnes et lignes
• Habillage : Propriétés > Aucun
• Un tableau flottant (Autour) est lu au mauvais moment

Objets flottants : zones de texte et images

• Lus dans un ordre aléatoire - solution : colonnes Word ou habillage En ligne

## Diapositive 8 - Contraste : un seuil chiffré, pas une opinion

1. Ouvrir le Colour Contrast Analyser (CCA) de TPGi - gratuit Windows et macOS

2. Pipette Premier plan sur la couleur du texte

3. Pipette Arrière-plan sur la couleur du fond

4. Lire le ratio : conforme si >= 4,5:1 pour le texte normal

5. >= 3:1 pour le grand texte (18 pt+ ou 14 pt gras) 
4,5:1 Texte normal
3:1 Grand texte

Scannez-moi !

https://vispero.com/lp/color-contrast-checker/

## Diapositive 6 - La couleur ne doit pas porter l'information à elle seule

8 % des hommes ne distinguent pas toutes les couleurs

| Inaccessible | Accessible |
| --- | --- |
| Statut : rouge / vert / jaune (couleur seule) | Statut : En retard / Terminé / En cours (texte + couleur) |
| Budget : zone verte = OK (couleur seule) | Budget : OK (vert) / Attention (orange) / Dépassé (rouge) |

Doublez toujours la couleur avec une légende textuelle
et idéalement un motif visuel distinct.

## Diapositive 7 - Texte alternatif sur les images

1 Clic droit sur l'image > Format de l'image > Texte de remplacement

2 Image significative : décrire la fonction, pas l'apparence

3 Image décorative : cocher Marquer comme décoratif

| Mauvais texte alt | Bon texte alt |
| --- | --- |
| Photo d'un graphique en barres colorées | Chiffre d'affaires 2020-2024 : hausse de 15 à 23 % |
| Icône d'enveloppe ou E-mail | alt="" (vide - icône redondante) |
| image.png | Organigramme du service : 4 équipes, 28 agents |

## Diapositive 8 - Liens et informations essentielles

| Inaccessible | Accessible |
| --- | --- |
| Cliquez ici | Consulter le guide d'accessibilité Word |
| En savoir plus | Télécharger le rapport annuel 2024 (PDF, 2 Mo) |
| URL brute | Accéder au formulaire de contact |

Informations essentielles dans les zones non lues

• En-têtes et pieds de page : non lus automatiquement
• Filigranes (Confidentiel, Brouillon) : invisibles
• Solution : reproduire l'info dans le corps du document

Liens de téléchargement

• Titre + format + poids + langue si différente
• Exemple : Rapport annuel 2024 (PDF, 2 Mo, anglais)

## Diapositive 9 - Exercice : les erreurs de Sami

Mise en situation

Sami, chargé de communication, envoie son rapport trimestriel à 40 personnes. 1. Quels critères posent problème ? 2. Quelles corrections proposez-vous ?

Le document de Sami contient

• Titres en gras, fausses listes, faux sommaire, tableaux sans en-tête
• Mention Urgent en rouge, note en gris insuffisant
• Graphique et organigramme sans alt, icône redondante
• Texte en image, lien cliquez ici, filigrane invisible
• Texte justifié, paragraphes vides, majuscules tapées

30 minutes en binôme : repérez les problèmes, puis corrigez-les.

## Diapositive 10 - Langue, majuscules et lisibilité

Balisage de langue

• Langue principale : Fichier > Options > Langue
• Passage en langue étrangère : sélectionner le texte > Révision > Langue > Définir la langue
• Sans balisage de langue, le lecteur d'écran prononce mal le mot

Majuscules : deux problèmes

• Difficiles à lire pour les dyslexiques
• Prononciation ambiguë par les lecteurs d'écran
• Solution : minuscules d'abord, puis Police > Modifier la casse

Lisibilité

• Police sans serif, 12 pt minimum
• Interligne 1,15, paragraphes aérés
• Alignement à gauche, pas de justification
• Contraste mesuré, fond non dégradé

## Diapositive 11 - Espaces et objets clignotants

Activer les marques de formatage : Accueil > Paragraphe > Afficher tout (signe paragraphe)

• Points = espaces successifs > supprimer et ne garder qu'un seul espace
• Flèches = tabulations utilisées pour simuler une mise en page
• Retours à la ligne manuels = utiliser les sauts de page propres à la place

Objets clignotants : tolérance zéro

• Animations, GIF avec flashs, vidéos à plus de 3 Hz : interdits sans exception
• Risque de crise d'épilepsie photosensible
• En cas de doute sur un GIF : remplacer par une image statique

## Diapositive 12 - Avant de publier : 5 vérifications en 2 minutes

1 Propriétés (Titre, Auteur, Objet) : Fichier > Informations > Propriétés

2 Nom de fichier descriptif en .docx (pas Document1.docx)

3 Protection : aucune restriction > Révision > Restreindre la modification

4 Formulaires : aucun champ Word interactif dans le document

5 Vérificateur d'accessibilité : Fichier > Vérifier l'accessibilité

Ces 5 vérifications couvrent 80 % des oublis restants.

## Diapositive 13 - Le vérificateur d'accessibilité Word

| Ce qu'il détecte | Ce qu'il ne détecte PAS |
| --- | --- |
| Texte alt manquant sur les images | Qualité du texte alt (contenu) |
| Styles de titre absents | Pertinence des noms de liens |
| Ordre de lecture problématique | Couleur porteuse de sens seule |
| Tableaux sans en-tête | Langue des passages étrangers |
|  | Contraste insuffisant |

Le vérificateur est un premier filtre, pas un certificat de conformité.

• Il signale ce qu'il peut détecter automatiquement - pas ce qui est vraiment accessible
• Une absence d'erreur ne signifie pas que le document est accessible

## Diapositive 14 - Exporter Word vers PDF sans perdre l'accessibilité

Un Word accessible peut devenir un PDF inaccessible si l'export est mal fait.

1 Vérifier l'accessibilité dans Word

2 Fichier > Enregistrer sous > PDF > Options

3 Cocher les options d'accessibilité avant d'enregistrer

Options à cocher dans Word bureau Windows

• Propriétés du document
• Balises de structure pour l'accessibilité
• Créer des signets à l'aide des titres ou en-têtes
• Ne pas convertir le texte en image bitmap

## Diapositive 15 - Retour sur le document de Sami

Vous vous souvenez ?

Vous avez déjà travaillé la plupart des erreurs de Structure, Couleurs, Contenus et Lisibilité. Il restait 2 erreurs des thèmes Langue et Finalisation que vous n'aviez pas encore les outils pour détecter.

Les 2 erreurs cachées

• Langue : un passage en anglais sans balisage de langue
• Finalisation : les propriétés du document (titre, auteur) sont vides

Les corrections en 2 minutes

• Langue : sélectionner le passage anglais > Révision > Langue > Définir en anglais
• Finalisation : Fichier > Informations > renseigner Titre et Auteur

## Diapositive 16 - Par où commencer ?

Tout est important mais commencez par ce qui est le plus facile.

1 Styles de titre sur tous les titres

2 Texte alternatif sur chaque image

3 Lancer le vérificateur d'accessibilité avant d'envoyer

## Diapositive 17 - Quiz final : saurez-vous trouver les 5 erreurs ?

Un collègue vous partage un document Word pour relecture.
En l'analysant, vous repérez les éléments suivants.

Identifiez les 5 erreurs d'accessibilité :

1. Le titre Introduction est en gras Arial 16 au lieu d'un style de titre
2. Un tableau de suivi utilise uniquement des lignes rouges et vertes
3. Un lien est rédigé : cliquez ici pour le formulaire
4. La langue principale du document n'est pas définie
5. Les propriétés du fichier (Titre et Auteur) sont vides

## Diapositive 18 - Correction : les 5 erreurs et leurs solutions

5 erreurs, 5 solutions

• Structure : le gras n'est pas reconnu par les lecteurs d'écran - appliquer le style Titre 1
• Couleurs : l'information ne doit pas reposer sur la couleur seule - ajouter les étiquettes Conforme / Non conforme
• Contenus : un lien doit être compréhensible hors contexte - renommer en Accéder au formulaire de demande RH
• Langue : sans déclaration, la synthèse vocale prononce avec le mauvais accent - Révision > Langue > Définir : Français
• Finalisation : le titre est la première information lue par le lecteur d'écran - Fichier > Informations > saisir Titre et Auteur

## Diapositive 19 - Faites le point

Sans relire le support, complétez de mémoire :

1. La règle la plus importante pour qu'un lecteur d'écran comprenne la structure de votre document : _______________

2. La vérification à faire en 30 secondes avant d'envoyer n'importe quel document : _______________

3. Le geste que vous ferez dès demain sur votre prochain document : _______________

## Diapositive 20 - Faites le point : les réponses

Les réponses

1. Utiliser les styles de titre (Titre 1, Titre 2) pour structurer le document
2. Lancer le vérificateur d'accessibilité (Révision > Vérifier l'accessibilité)
3. Ajouter un texte alternatif aux images ou renseigner le titre dans les propriétés

Vous avez ces réflexes ? L'essentiel est acquis.
Sinon : relisez Structure et Contenus.

## Diapositive 21 - Dès demain, vos trois premiers réflexes

Ctrl+F > onglet Titres

• Vérifier que tous les titres apparaissent dans le volet de navigation
• Si le volet est vide : appliquer les styles

Clic droit > Texte de remplacement

• Décrire la fonction de chaque image
• Image décorative : cocher Marquer comme décoratif

Fichier > Vérifier l'accessibilité

• Corriger les erreurs avant d'envoyer
• Zéro erreur = premier filtre passé
