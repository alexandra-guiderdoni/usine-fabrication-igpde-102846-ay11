---
title: "Mémo accessibilité - LibreOffice Writer"
author: "IGPDE - Formation 102846"
lang: fr
---

# Mémo accessibilité - LibreOffice Writer

Aide-mémoire des bonnes pratiques pour créer des documents Writer accessibles.
Formation 102846 - Juin 2026

---

## Thème 1 - Structure du document

La structure permet aux lecteurs d'écran de naviguer dans le document. Sans elle, le contenu est un bloc de texte plat sans repère.

### Styles de titre

**Erreur** : simuler un titre en mettant du texte en gras et en changeant la taille (ex : gras Arial 16, gras Arial 14, gras souligné Arial 12). Le lecteur d'écran ne détecte aucun titre : l'utilisateur ne peut pas naviguer entre les sections.

**Procédure** : sélectionner le texte > dans la barre de formatage, ouvrir la liste des styles (ou **F11** pour le panneau Styles) > choisir **Titre 1**, **Titre 2** ou **Titre 3**.

- Commencer par un Titre 1, ne pas sauter de niveau (pas de Titre 3 après un Titre 1)
- Le style **Titre principal** est réservé au titre du document, différent du titre dans les propriétés

**Vérifier** : appuyer sur **F5** pour ouvrir le **Navigateur** et visualiser la hiérarchie des titres.

![Panneau Propriétés et Navigateur dans LibreOffice Writer](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-navigateur.png)

### Listes natives

**Erreur** : taper des puces (-, *) ou des numéros (1. 2. 3.) au clavier et indenter manuellement. Le lecteur d'écran lit chaque ligne comme un paragraphe ordinaire au lieu d'annoncer "liste de 3 éléments, élément 1 sur 3".

**Procédure** : sélectionner les paragraphes > barre de formatage > bouton **Puces** ou **Numérotation**.

![Barre d'outils des listes dans LibreOffice Writer](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-listes-toolbar.png)

**Numérotation des titres** : **Outils** > **Numérotation des chapitres** pour associer un schéma de numérotation aux styles de titre.

### Table des matières automatique

**Erreur** : taper un sommaire à la main avec des points de suite et des numéros de page en dur. Ce sommaire n'est pas navigable : le lecteur d'écran ne peut pas sauter directement à une section, et il ne se met pas à jour.

**Procédure** : **Insertion** > **Table des matières et index** > **Table des matières, index ou bibliographie**.

![Boîte de dialogue Table des matières dans LibreOffice Writer](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-table-matieres.png)

### En-têtes de tableau

**Erreur** : créer un tableau de données sans identifier la ligne d'en-tête. Le lecteur d'écran ne peut pas associer chaque cellule à sa colonne : les données deviennent incompréhensibles.

**Procédure** : lors de la création via **Tableau** > **Insérer un tableau**, cocher **En-tête**. Pour un tableau existant : sélectionner la première ligne > **Tableau** > **Propriétés** > onglet **Enchaînements** > cocher **Répéter le titre**.

### Cellules fusionnées

**Erreur** : fusionner des cellules pour créer des mises en page complexes (ex : première ligne fusionnée sur 3 colonnes, libellés en gras visuels). Les cellules fusionnées cassent la logique de lecture : le lecteur d'écran ne peut plus associer chaque cellule à son en-tête. Des libellés en gras ne suffisent pas.

**Bonne pratique** : privilégier les tableaux simples en grille sans fusion, avec l'en-tête déclaré. Si un tableau est trop complexe, le scinder en plusieurs tableaux simples.

---

## Thème 2 - Couleurs et contrastes

### Information par la couleur seule

**Erreur** : écrire "URGENT" en rouge sans autre indication visuelle (pas de gras, pas de texte explicatif). Une personne daltonienne ou utilisant un écran monochrome ne perçoit aucune urgence : le mot se fond dans le texte courant (WCAG 1.4.1).

**Bonne pratique** : ajouter du **gras** et un texte explicatif en complément de la couleur. Exemple : **URGENT - Retour attendu avant le 30 juin 2025**.

### Contraste minimum

**Erreur** : utiliser du gris clair sur fond blanc (ex : #767676 = ratio 4,48:1, insuffisant pour du texte normal). L'erreur est subtile : le texte semble lisible mais échoue de justesse au test WCAG 1.4.3. Seul un outil de mesure permet de trancher.

**Seuils WCAG** : texte normal **4,5:1** minimum - grand texte (18 pt ou 14 pt gras) **3:1** - icônes et éléments graphiques **3:1**.

**Correction** : remplacer par un gris plus foncé (ex : #595959, ratio 7:1) ou du noir.

**Outil** : Colour Contrast Analyser (CCA), application gratuite. C'est le type d'erreur qu'on ne peut pas détecter visuellement : il faut systématiquement mesurer le contraste avec un outil, surtout pour les gris clairs et les couleurs proches du seuil.

**Appliquer une couleur précise** : sélectionner le texte > bouton **Couleur de police** > **Couleur personnalisée** > saisir le code hexadécimal.

### Graphiques lisibles sans couleur

**Erreur** : différencier les barres d'un graphique uniquement par la couleur (vert/rouge/orange sans motif ni étiquette). Environ 8 % des hommes sont daltoniens : les barres deviennent indiscernables.

**Bonne pratique** : ajouter des **motifs distincts** (hachures, points, plein) et des **étiquettes** sur chaque barre.

---

## Thème 3 - Contenus

### Alternative textuelle des images informatives

**Erreur** : image informative sans texte alternatif. Le lecteur d'écran annonce "image" sans aucune description.

**Procédure** : clic droit sur l'image > **Propriétés** > onglet **Options** > remplir le champ **Alternative (texte seul)** avec 1 à 2 phrases décrivant l'information portée par l'image.

![Menu contextuel Propriétés dans LibreOffice Writer](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-menu-proprietes.png)

Ne jamais laisser le nom de fichier par défaut comme alternative (ex : "image.png" n'apporte aucune information).

### Images complexes

**Erreur** : laisser le nom de fichier par défaut (ex : alt="image.png") ou mettre une longue description dans le champ alt (organigramme, graphique détaillé).

**Bonne pratique** : remplir **Alternative** avec un texte court (~80 caractères) et utiliser le champ **Description** pour le détail, ou ajouter la description dans le corps du texte sous l'image. Exemple : Alternative="Organigramme de la direction (description ci-dessous)."

![Boîte de dialogue Propriétés de l'image avec champs Alternative et Description](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-alt-text-dialog.png)

### Images décoratives

**Erreur** : mettre un alt "E-mail" sur une icône enveloppe placée juste à côté du mot "e-mail". Le lecteur d'écran lit "E-mail, e-mail" : redondance qui pollue la lecture. L'accessibilité des images ne se limite pas à "mettre un alt partout" : certaines images doivent être explicitement ignorées.

**Procédure** : clic droit > **Propriétés** > onglet **Options** > laisser le champ **Alternative** vide.

Writer n'a pas d'option "Marquer comme décoratif" comme Word. Laisser le champ vide suffit : lors de l'export PDF, l'image sera traitée comme décorative.

### Liens explicites

**Erreur** : "cliquez ici" ou "en savoir plus" comme intitulé de lien. Le lecteur d'écran liste les liens par intitulé : "cliquez ici" ne donne aucune information hors contexte visuel.

**Bonne pratique** : intitulé qui décrit la destination. Pour un lien de téléchargement, préciser le titre, le format et le poids. Exemple : "Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo)".

### Filigrane invisible

**Erreur** : insérer un filigrane "CONFIDENTIEL" via **Format** > **Filigrane**. Les filigranes sont des objets graphiques non lus par les lecteurs d'écran. Un utilisateur aveugle ne sait pas que le document est confidentiel.

**Bonne pratique** : ajouter la mention "Document confidentiel" en texte dans le corps du document.

### Texte sous forme d'image

**Erreur** : insérer une capture d'écran contenant du texte (ex : "Avis important : les indicateurs du T2 2025 seront transmis avant le 15 septembre 2025."). Ce texte ne peut être ni lu par la synthèse vocale, ni agrandi, ni sélectionné, ni recherché.

**Bonne pratique** : toujours saisir le texte directement dans Writer. Seuls les logos peuvent rester en image.

---

## Thème 4 - Langue et lisibilité

### Balisage des passages en langue étrangère

**Erreur** : insérer un passage en anglais sans changer la langue du texte. Le lecteur d'écran lit le passage avec la prononciation française, ce qui le rend incompréhensible.

**Procédure** : sélectionner le passage > cliquer sur la **langue dans la barre d'état** (en bas à gauche) > choisir la langue du passage (ex : Anglais).

### Alignement à gauche

**Erreur** : justifier tout le document. Le texte justifié crée des espaces inégaux entre les mots (lézardes) qui rendent la lecture difficile pour les personnes dyslexiques ou malvoyantes.

**Procédure** : barre de formatage > **Aligner à gauche** (ou **Ctrl+L**).

### Espacement par les styles

**Erreur** : insérer des paragraphes vides (touche Entrée) pour créer de l'espace. Le lecteur d'écran lit "vide, vide, vide, vide" à chaque paragraphe vide.

**Procédure** : gérer l'espacement par les propriétés du style. Clic droit > **Modifier le style** > onglet **Retraits et espacement** > ajuster **Au-dessus du paragraphe** et **En dessous du paragraphe**.

**Vérifier** : **Affichage** > cocher **Marques de formatage** (ou **Ctrl+F10**) pour visualiser les paragraphes vides, sauts de ligne, tabulations et espaces.

![Bouton marques de formatage dans LibreOffice Writer](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-marques-formatage.png)

### Majuscules par la mise en forme

**Erreur** : taper "ANNEXES" en majuscules au clavier. Le lecteur d'écran peut épeler lettre par lettre les mots tapés en majuscules.

**Procédure** : taper "Annexes" en minuscules > sélectionner > **Format** > **Caractère** > onglet **Effets de caractère** > choisir **MAJUSCULES**. Le texte s'affiche en majuscules visuellement mais le lecteur d'écran lit le mot normalement.

---

## Thème 5 - Finalisation

### Propriétés du document

**Erreur** : laisser les propriétés Titre et Auteur vides. Les propriétés du document sont la première information lue par un lecteur d'écran. Sans titre, l'utilisateur ne sait pas ce qu'il ouvre.

**Procédure** : **Fichier** > **Propriétés** > onglet **Description** > renseigner **Titre**. Onglet **Général** > renseigner **Auteur**. Vérifier aussi que la langue du document est définie en **Français** (barre d'état).

![Propriétés du document dans Writer - onglet Description](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-proprietes-titre.png)

### Vérification de l'accessibilité

**Procédure** : **Outils** > **Vérification de l'accessibilité**. L'outil est un guide, pas une preuve de conformité : il détecte les problèmes courants (images sans alt, textes flottants) mais peut rater certaines erreurs (contraste, faux titres visuels, fausses listes).

![Fenêtre de vérification de l'accessibilité dans Writer](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-verification-a11y.png)

### Export PDF accessible (PDF/UA)

1. **Fichier** > **Exporter au format PDF**
2. Onglet **Général**, cocher :
   - **Accessibilité Universelle (PDF/UA)**
   - **Exporter le plan et autres éléments de structure**

![Options d'export PDF dans Writer - PDF/UA et structure](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/writer-export-pdf-ua.png)

### Ancrage des images

**Point spécifique Writer** : pour garantir l'ordre de lecture correct, ancrer les images **Comme caractère** (clic droit > **Ancrage** > **Comme caractère**). C'est plus fiable que l'ancrage "Au paragraphe" ou "A la page" qui peut décorréler la position visuelle de l'ordre de lecture.

### Vérification post-export

Utiliser **PAC** (PDF Accessibility Checker), outil gratuit, pour vérifier la conformité PDF/UA du document exporté.

![Interface de PAC 2024](/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique/images-memo-writer/pac-interface.png)

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
- Les images décoratives ont le champ alternatif vide
- Les liens ont un intitulé explicite (pas "cliquez ici"), avec format et poids si téléchargement
- Pas de filigrane sans équivalent textuel dans le corps du document
- Pas de texte inséré sous forme d'image (saisir le texte directement)

### Langue et lisibilité

- Les passages en langue étrangère sont balisés dans la bonne langue
- Le texte est aligné à gauche (pas justifié)
- Pas de paragraphes vides : l'espacement est géré par les styles
- Les majuscules sont appliquées par la mise en forme Caractère, pas tapées au clavier

### Finalisation

- Le titre, l'auteur et la langue sont renseignés dans les propriétés du document
- La vérification d'accessibilité intégrée ne remonte pas d'erreur bloquante
- Le PDF est exporté en PDF/UA avec le plan et les éléments de structure

---

## Ressources

- **Colour Contrast Analyser (CCA)** : https://www.tpgi.com/color-contrast-checker/
- **PAC - PDF Accessibility Checker** : https://pac.pdf-accessibility.org/
- **Site d'entraînement** : https://alexmacapple.github.io/easy-check-igpde/
