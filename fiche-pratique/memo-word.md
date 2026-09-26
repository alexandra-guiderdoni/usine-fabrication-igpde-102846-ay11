---
title: "Mémo accessibilité - Microsoft Word"
author: "IGPDE - Formation 102846"
lang: fr
---

# Mémo accessibilité - Microsoft Word

Aide-mémoire des bonnes pratiques pour créer des documents Word accessibles.
Formation 102846 - Juin 2026

---

## Thème 1 - Structure du document

La structure permet aux lecteurs d'écran de naviguer dans le document. Sans elle, le contenu est un bloc de texte plat sans repère.

### Styles de titre

**Erreur** : simuler un titre en mettant du texte en gras et en changeant la taille (ex : gras Arial 16, gras Arial 14, gras souligné Arial 12). Le lecteur d'écran ne détecte aucun titre : l'utilisateur ne peut pas naviguer entre les sections.

**Procédure** : sélectionner le texte > onglet **Accueil** > zone **Styles** > choisir **Titre 1**, **Titre 2** ou **Titre 3**.

- Commencer par un Titre 1, ne pas sauter de niveau (pas de Titre 3 après un Titre 1)
- Le style **Titre** (sans numéro) est réservé au titre principal du document, différent du titre dans les propriétés

**Vérifier** : onglet **Affichage** > cocher **Volet de navigation** > onglet **Titres** pour visualiser la hiérarchie.

![Volet de navigation Word montrant la hiérarchie des titres](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-volet-navigation.png)

### Listes natives

**Erreur** : taper des puces (-, *) ou des numéros (1. 2. 3.) au clavier et indenter manuellement. Le lecteur d'écran lit chaque ligne comme un paragraphe ordinaire au lieu d'annoncer "liste de 3 éléments, élément 1 sur 3".

**Procédure** : sélectionner les paragraphes > **Accueil** > bouton **Puces** ou **Numérotation**.

![Barre d'outils des listes dans Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-listes-toolbar.png)

### Table des matières automatique

**Erreur** : taper un sommaire à la main avec des points de suite et des numéros de page en dur. Ce sommaire n'est pas navigable : le lecteur d'écran ne peut pas sauter directement à une section, et il ne se met pas à jour.

**Procédure** : onglet **Références** > **Table des matières** > **Table des matières personnalisée**.

![Boîte de dialogue Table des matières dans Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-table-matieres.png)

### En-têtes de tableau

**Erreur** : créer un tableau de données sans identifier la ligne d'en-tête. Le lecteur d'écran ne peut pas associer chaque cellule à sa colonne : les données deviennent incompréhensibles.

**Procédure** :

1. Cliquer dans le tableau > onglet **Création** > cocher **Ligne d'en-tête**
2. Clic droit > **Propriétés du tableau** > onglet **Ligne** > cocher **Répéter en haut de chaque page en tant que ligne d'en-tête**

![Option Répéter la ligne d'en-tête dans les propriétés du tableau Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-tableau-entete.png)

### Cellules fusionnées

**Erreur** : fusionner des cellules pour créer des mises en page complexes (ex : première ligne fusionnée sur 3 colonnes, libellés en gras visuels). Les cellules fusionnées cassent la logique de lecture : le lecteur d'écran ne peut plus associer chaque cellule à son en-tête. Des libellés en gras ne suffisent pas.

**Bonne pratique** : privilégier les tableaux simples en grille sans fusion, avec la **Ligne d'en-tête** cochée. Si un tableau est trop complexe, le scinder en plusieurs tableaux simples.

---

## Thème 2 - Couleurs et contrastes

### Information par la couleur seule

**Erreur** : écrire "URGENT" en rouge sans autre indication visuelle (pas de gras, pas de texte explicatif). Une personne daltonienne ou utilisant un écran monochrome ne perçoit aucune urgence : le mot se fond dans le texte courant (WCAG 1.4.1).

**Bonne pratique** : ajouter du **gras** et un texte explicatif en complément de la couleur. Exemple : **URGENT - Retour attendu avant le 30 juin 2025**.

### Contraste minimum

**Erreur** : utiliser du gris clair sur fond blanc (ex : #767676 = ratio 4,48:1, insuffisant pour du texte normal). L'erreur est subtile : le texte semble lisible mais échoue de justesse au test WCAG 1.4.3. Seul un outil de mesure permet de trancher.

**Seuils WCAG** : texte normal **4,5:1** minimum - grand texte (18 pt ou 14 pt gras) **3:1** - icônes et éléments graphiques **3:1**.

**Correction** : remplacer par un gris plus foncé (ex : #595959, ratio 7:1) ou du noir.

**Outil** : Colour Contrast Analyser (CCA), application gratuite pour mesurer le ratio. C'est le type d'erreur qu'on ne peut pas détecter visuellement : il faut systématiquement mesurer le contraste avec un outil, surtout pour les gris clairs et les couleurs proches du seuil.

### Graphiques lisibles sans couleur

**Erreur** : différencier les barres d'un graphique uniquement par la couleur (vert/rouge/orange sans motif ni étiquette). Environ 8 % des hommes sont daltoniens : les barres deviennent indiscernables.

**Bonne pratique** : ajouter des **motifs distincts** (hachures, points, plein) et des **étiquettes** sur chaque barre.

---

## Thème 3 - Contenus

### Alternative textuelle des images informatives

**Erreur** : image informative sans texte alternatif. Le lecteur d'écran annonce "image" sans aucune description.

**Procédure** : clic droit sur l'image > **Modifier le texte de remplacement** > saisir 1 à 2 phrases décrivant l'information portée par l'image.

![Menu contextuel Word pour modifier le texte de remplacement](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-menu-alt-text.png)

Ne jamais utiliser la génération automatique de description (rarement pertinente). Ne jamais laisser le nom de fichier par défaut comme alternative (ex : "image.png" n'apporte aucune information).

### Images complexes

**Erreur** : laisser le nom de fichier par défaut (ex : alt="image.png") ou mettre une longue description dans le champ alt (organigramme, graphique détaillé).

**Bonne pratique** : pour une image complexe, l'alt doit rester court (~80 caractères) et renvoyer vers une description détaillée dans le corps du document. Exemple : alt="Organigramme de la direction (description ci-dessous)." suivi d'une description textuelle adjacente.

### Images décoratives

**Erreur** : mettre un alt "E-mail" sur une icône enveloppe placée juste à côté du mot "e-mail". Le lecteur d'écran lit "E-mail, e-mail" : redondance qui pollue la lecture. L'accessibilité des images ne se limite pas à "mettre un alt partout" : certaines images doivent être explicitement ignorées.

**Procédure** : clic droit > **Modifier le texte de remplacement** > cocher **Marquer comme décoratif**.

![Boîte de dialogue alt text Word avec option Marquer comme décoratif](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-alt-text-dialog.png)

### Liens explicites

**Erreur** : "cliquez ici" ou "en savoir plus" comme intitulé de lien. Le lecteur d'écran liste les liens par intitulé : "cliquez ici" ne donne aucune information hors contexte visuel.

**Bonne pratique** : intitulé qui décrit la destination. Pour un lien de téléchargement, préciser le titre, le format et le poids. Exemple : "Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo)".

### Filigrane invisible

**Erreur** : insérer un filigrane "CONFIDENTIEL" dans l'en-tête du document. Les filigranes sont des objets graphiques non lus par les lecteurs d'écran. Un utilisateur aveugle ne sait pas que le document est confidentiel.

**Bonne pratique** : ajouter la mention "Document confidentiel" en texte dans le corps du document.

### Texte sous forme d'image

**Erreur** : insérer une capture d'écran contenant du texte (ex : "Avis important : les indicateurs du T2 2025 seront transmis avant le 15 septembre 2025."). Ce texte ne peut être ni lu par la synthèse vocale, ni agrandi, ni sélectionné, ni recherché.

**Bonne pratique** : toujours saisir le texte directement dans Word. Seuls les logos peuvent rester en image.

---

## Thème 4 - Langue et lisibilité

### Balisage des passages en langue étrangère

**Erreur** : insérer un passage en anglais sans changer la langue du texte. Le lecteur d'écran lit le passage avec la prononciation française, ce qui le rend incompréhensible.

**Procédure** : sélectionner le passage > onglet **Révision** > **Langue** > **Définir la langue de vérification** > choisir la langue (ex : Anglais). Alternative rapide : cliquer sur la langue affichée dans la barre d'état (en bas) et choisir la langue.

![Sélection de la langue dans la barre d'état Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-selection-langue.png)

### Alignement à gauche

**Erreur** : justifier tout le document. Le texte justifié crée des espaces inégaux entre les mots (lézardes) qui rendent la lecture difficile pour les personnes dyslexiques ou malvoyantes.

**Procédure** : **Accueil** > **Aligner à gauche**.

### Espacement par les styles

**Erreur** : insérer des paragraphes vides (touche Entrée) pour créer de l'espace. Le lecteur d'écran lit "vide, vide, vide, vide" à chaque paragraphe vide.

**Procédure** : gérer l'espacement par les propriétés du style de paragraphe. Clic droit > **Modifier** > **Format** > **Paragraphe** > ajuster les valeurs **Avant** et **Après**.

**Vérifier** : **Accueil** > bouton **Afficher tout** pour visualiser les marques de formatage (paragraphes vides, sauts de ligne, tabulations, espaces).

![Bouton Afficher tout dans la barre d'outils Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-marques-formatage.png)

### Majuscules par la mise en forme

**Erreur** : taper "ANNEXES" en majuscules au clavier. Le lecteur d'écran peut épeler lettre par lettre les mots tapés en majuscules.

**Procédure** : taper "Annexes" en minuscules > sélectionner > **Accueil** > **Police** > cocher **Tout en majuscules**. Le texte s'affiche en majuscules visuellement mais le lecteur d'écran lit le mot normalement.

---

## Thème 5 - Finalisation

### Propriétés du document

**Erreur** : laisser les propriétés Titre et Auteur vides. Les propriétés du document sont la première information lue par un lecteur d'écran. Sans titre, l'utilisateur ne sait pas ce qu'il ouvre.

**Procédure** : **Fichier** > **Informations** > **Propriétés** > renseigner **Titre** et **Auteur**. Vérifier aussi que la langue du document est définie en **Français** (barre d'état).

![Propriétés du document dans Word - champ Titre](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-proprietes-titre.png)

### Vérification de l'accessibilité

**Procédure** : onglet **Révision** > **Vérifier l'accessibilité**. L'outil est un guide, pas une preuve de conformité : il détecte les problèmes courants (images sans alt, tableaux sans en-tête) mais peut rater certaines erreurs (contraste, faux titres visuels, fausses listes).

![Volet de vérification de l'accessibilité dans Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-verification-a11y.png)

### Export PDF accessible

1. **Fichier** > **Exporter** > **Créer PDF/XPS**
2. Cliquer sur **Options**, cocher :
   - **Créer des signets à l'aide de : Titres**
   - **Propriétés du document**
   - **Balises de structure de document pour l'accessibilité**

![Options d'export PDF dans Word](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/word-export-pdf.png)

### Vérification post-export

Utiliser **PAC** (PDF Accessibility Checker), outil gratuit, pour vérifier la conformité PDF/UA du document exporté.

![Interface de PAC 2024](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-word/pac-interface.png)

---

## Checklist des bonnes pratiques

### Structure

- Les titres utilisent les styles Titre 1, Titre 2, Titre 3 (pas de gras/taille)
- Les listes utilisent les puces ou la numérotation natives (pas de puces tapées)
- La table des matières est générée automatiquement (pas de sommaire tapé)
- Les tableaux ont une ligne d'en-tête déclarée et répétée
- Les tableaux n'ont pas de cellules fusionnées

### Couleurs

- L'information n'est pas véhiculée par la couleur seule (gras + texte en complément)
- Le contraste est suffisant : 4,5:1 texte normal, 3:1 grand texte (vérifier avec CCA)
- Les graphiques ont des motifs distincts et des étiquettes (pas uniquement des couleurs)

### Contenus

- Les images informatives ont un texte alternatif pertinent (pas le nom de fichier)
- Les images complexes ont un alt court + une description adjacente dans le document
- Les images décoratives sont marquées comme décoratives
- Les liens ont un intitulé explicite (pas "cliquez ici"), avec format et poids si téléchargement
- Pas de filigrane sans équivalent textuel dans le corps du document
- Pas de texte inséré sous forme d'image (saisir le texte directement)

### Langue et lisibilité

- Les passages en langue étrangère sont balisés dans la bonne langue
- Le texte est aligné à gauche (pas justifié)
- Pas de paragraphes vides : l'espacement est géré par les styles
- Les majuscules sont appliquées par la mise en forme Police, pas tapées au clavier

### Finalisation

- Le titre, l'auteur et la langue sont renseignés dans les propriétés du document
- La vérification d'accessibilité intégrée ne remonte pas d'erreur bloquante
- Le PDF est exporté avec signets, propriétés et balises de structure

---

## Ressources

- **Colour Contrast Analyser (CCA)** : https://www.tpgi.com/color-contrast-checker/
- **PAC - PDF Accessibility Checker** : https://pac.pdf-accessibility.org/
- **Site d'entraînement** : https://alexmacapple.github.io/easy-check-igpde/
