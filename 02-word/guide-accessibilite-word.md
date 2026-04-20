# Guide : rendre un document Word accessible

Référence opérationnelle pour créer et vérifier l'accessibilité d'un document Microsoft Word. Toutes les méthodes s'appliquent à Word pour PC.

---

## Principes

Les personnes aveugles, malvoyantes, sourdes, malentendantes ou avec un handicap cognitif/physique utilisent des **technologies d'assistance** (TA) : lecteurs d'écran, synthèse vocale, navigation clavier. Un document accessible fonctionne en partenariat avec ces outils.

**Prérequis** : fichier au format **.docx** (obligatoire pour que les tests d'accessibilité fonctionnent). Enregistrer au bon format dès la création du document. Les formats .doc et .docm ne sont pas couverts.

**Hors périmètre** : documents avec macros (.docm, .dotm), documents protégés (lever les restrictions via Révision > Restreindre la modification > Désactiver la protection), formulaires interactifs Word (non rendus accessibles — utiliser une autre application).

---

## 1. Structure du document

### Styles de titre

Les titres organisent le contenu et permettent la navigation par les TA. Un texte simplement mis en gras ou en grande taille **n'est pas** un titre pour les TA.

- Appliquer les styles intégrés : **Accueil > Styles** (ou Ctrl+Alt+Maj+S)
- Utiliser un style distinct par niveau de titre : Titre 1, Titre 2, Titre 3, etc.
- La hiérarchie des styles doit refléter la structure logique du document (pas de saut de niveau)
- Deux méthodes : sélectionner le style puis saisir, ou saisir puis appliquer le style

**Vérification** : ouvrir le **volet de navigation** (Affichage > Volet de navigation, ou Ctrl+F > onglet « Titres »). Tous les titres doivent y apparaître et refléter la structure visuelle du document.

### Listes

Toujours utiliser **Puces**, **Numérotation** ou **Liste à plusieurs niveaux** (Accueil > Paragraphe). Les tirets, astérisques ou chiffres saisis manuellement ne sont pas interprétés comme des listes par les TA.

**Vérification** : curseur sur un élément de liste > ouvrir le volet « Révéler la mise en forme » (Maj+F1). La catégorie « Puces et numérotation » doit apparaître avec les informations de liste.

### Colonnes

Toujours utiliser l'outil intégré : **Mise en page > Colonnes**. Les tabulations et espaces pour simuler des colonnes sont invisibles aux TA — le contenu sera lu dans le désordre.

**Méthode** : sélectionner le contenu à formater > Mise en page > Colonnes > choisir le nombre de colonnes.

**Vérification** : curseur sur le texte en colonnes > Révéler la mise en forme (Maj+F1) > la mention « Colonnes » doit apparaître sous « Section ».

### Sauts de page

Utiliser **Insertion > Saut de page** (ou Ctrl+Entrée) pour passer à la page suivante. Ne jamais utiliser des retours chariot (Entrée) répétés pour créer un saut visuel — les TA lisent chaque ligne vide.

### Tableaux de mise en page

Les tableaux de mise en page servent à organiser le contenu visuellement, sans en-têtes de lignes ou de colonnes.

- Créer via **Insertion > Tableau > Insérer un tableau** (jamais d'image de tableau)
- L'ordre de lecture suit l'ordre de tabulation : gauche à droite, haut en bas
- L'habillage du texte doit être sur **Aucun** (aligné avec le texte)

**Vérification** :

| Test | Comment | Échec si |
|------|---------|----------|
| Ordre de lecture ? | Curseur dans la 1re cellule > Tab pour parcourir | L'ordre de tabulation ne correspond pas à la disposition visuelle |
| Aligné avec le texte ? | Clic droit > Propriétés du tableau > onglet Tableau | Habillage du texte sur « Autour » au lieu de « Aucun » |

### Tableaux de données

Les tableaux de données nécessitent des en-têtes de lignes et/ou de colonnes pour que les TA associent chaque cellule à son contexte.

- Créer via **Insertion > Tableau** (jamais d'image de tableau)
- **Ne pas fusionner** ni diviser de cellules (tableau simple uniquement)
- Identifier la ligne d'en-tête : sélectionner la 1re ligne > clic droit > **Propriétés du tableau > onglet Ligne** > cocher **Répéter en tant que ligne d'en-tête en haut de chaque page**
- Habillage du texte sur **Aucun**

**Limitation** : les tableaux complexes (plusieurs lignes d'en-tête, cellules fusionnées/divisées) ne peuvent pas être rendus accessibles dans Word. Les convertir en **PDF accessible**.

**Vérification** :

| Test | Comment | Échec si |
|------|---------|----------|
| Vrai tableau ? | Sélectionner > l'onglet « Outils Image » apparaît | C'est une image de tableau |
| Cellules fusionnées ? | Outils de tableau > Mise en page > Afficher le quadrillage | Des cellules s'étendent sur plusieurs colonnes/lignes |
| En-tête identifié ? | Curseur sur la 1re ligne > Révéler la mise en forme (Maj+F1) | « Répéter en tant que ligne d'en-tête » absent |
| Aligné ? | Clic droit > Propriétés du tableau > onglet Tableau | Habillage du texte sur « Autour » |

---

## 2. Couleurs et contraste

### Rapport de contraste

| Type de texte | Ratio minimum |
|---------------|---------------|
| Standard (12 pt régulier) | **4,5:1** |
| Grande taille (14 pt gras ou 18 pt régulier) | **3:1** |

Exclusions : textes accessoires, textes sur images, logos. Texte noir sur fond blanc = test passé automatiquement.

**Méthode** : utiliser un analyseur de contraste (Colour Contrast Analyser de TPGi ou équivalent). Pipette premier plan sur le texte, pipette arrière-plan sur le fond. Ajuster si le ratio est insuffisant.

### Couleur porteuse de sens

Toute information véhiculée par la couleur, la taille, la forme ou l'emplacement doit **aussi** être exprimée en texte. Exemple : un tableau de statut rouge/jaune/vert doit aussi indiquer « En retard », « En cours », « Terminé » en texte.

**Vérification** : identifier chaque passage où la couleur ou une caractéristique visuelle porte une signification. Un texte explicite doit reproduire cette signification.

---

## 3. Contenu alternatif

### Texte alternatif (images et objets)

Objets concernés : photos, illustrations, images de texte, images de tableaux, formes, icônes avec hyperliens, graphiques, diagrammes.

**Rédaction** : penser à la **fonction** de l'image, pas à son apparence. Test : remplacer l'image par le texte alt — aucune information clé ne doit être perdue. Rester concis.

**Méthode** : sélectionner l'objet > clic droit (ou Maj+F10) > **Format de l'image > Texte de remplacement** :
- Objet significatif : saisir une description dans le champ « Description »
- Objet décoratif : insérer des espaces vides dans le champ (ou cocher « Marquer comme décoratif » si disponible)

### Alignement des objets

Les images, objets et zones de texte doivent être **alignés avec le texte** pour que les TA puissent y accéder.

**Méthode** : sélectionner l'objet > **Outils Image > Format > Position > Aligné sur le texte**.

**Vérification** : lancer le vérificateur d'accessibilité (Fichier > Vérifier la présence de problèmes > Vérifier l'accessibilité). Les avertissements « Objet non aligné » signalent un échec.

### Zones de texte

Les zones de texte flottantes sont inaccessibles aux TA si elles ne sont pas alignées avec le texte. Même alignées, leur contenu peut être lu dans un ordre inattendu.

**Recommandation** : éviter les zones de texte quand c'est possible. Si nécessaire, les aligner avec le texte et vérifier l'ordre de lecture.

### Liens hypertextes

- Chaque lien doit avoir un **nom unique et descriptif** (pas « cliquez ici », « en savoir plus », URL brute)
- L'objectif doit être discernable dans le contexte environnant

**Méthode** : sélectionner le texte descriptif > clic droit > **Lien hypertexte** (ou Ctrl+K) > coller l'URL dans le champ Adresse. Pour modifier : clic droit sur le lien > **Modifier le lien hypertexte** > champ « Texte à afficher ».

Attention : supprimer le dernier caractère du texte d'un lien supprime le lien entier.

Pour les documents imprimés ET numériques : inclure l'URL et la description (ex : « Accessibilité numérique (www.exemple.fr/accessibilite) »).

### Informations essentielles (en-têtes, pieds de page, filigranes)

Le contenu placé dans les en-têtes, pieds de page et filigranes est **inaccessible** aux TA. Les informations essentielles (« Confidentiel », « Ne pas diffuser », « Répondre avant le [date] ») doivent être reproduites dans le corps du document, idéalement au début.

**Vérification** : identifier toute information essentielle dans les en-têtes, pieds de page et filigranes. Vérifier qu'elle est reproduite dans le corps du document.

---

## 4. Langue

### Langue du document

Définir la langue principale du document : **Fichier > Options > Langue** (ou Révision > Langue > Définir la langue de vérification).

### Passages en langue étrangère

Si le document contient des mots ou passages dans une **langue différente** de la langue principale, les baliser explicitement. Sans balisage, le lecteur d'écran applique la mauvaise prononciation.

**Méthode** : sélectionner le texte en langue étrangère > **Révision > Langue > Définir la langue de vérification** > choisir la langue.

**Vérification** : curseur sur le texte étranger > Révéler la mise en forme (Maj+F1) > vérifier sous Police > Langue que la langue affichée correspond à la langue réelle.

---

## 5. Médias intégrés

| Type | Alternative requise |
|------|---------------------|
| Audio seul | Transcription textuelle précise et complète |
| Vidéo seule (sans audio) | Description textuelle précise et complète |
| Multimédia (audio + vidéo) | Sous-titres synchronisés ET description audio |

Toutes les alternatives doivent être précises, complètes et synchronisées le cas échéant.

---

## 6. Objets clignotants

**Interdit.** Les objets clignotants provoquent des crises d'épilepsie. Aucune exception : animations de clignotement, GIF avec flashs, vidéos avec séquences de flashs rapides (>3 Hz). Un document contenant un objet clignotant ne peut jamais être considéré comme accessible.

---

## 7. Propriétés du document

Renseigner les métadonnées du fichier pour faciliter l'identification et le classement par les TA et les moteurs de recherche.

**Méthode** : **Fichier > Informations** (ou Fichier > Propriétés > Propriétés avancées) :
- **Titre** : titre du document (différent du nom de fichier)
- **Auteur** : auteur ou organisation
- **Objet** : description courte du contenu

---

## 8. Nom de fichier

- Format : **.docx** (prérequis aux tests d'accessibilité)
- Nom **descriptif** identifiant le contenu ou l'objectif

Non conforme : `Document1.docx`. Conforme : `rapport-accessibilite-2024.docx`.

---

## 9. Vérificateur d'accessibilité intégré

Word intègre un vérificateur d'accessibilité qui détecte automatiquement certains problèmes courants.

**Méthode** : **Fichier > Vérifier la présence de problèmes > Vérifier l'accessibilité** (ou onglet Révision > Vérifier l'accessibilité selon la version).

Le vérificateur signale trois niveaux : erreurs (bloquantes), avertissements (à corriger), conseils (recommandations). Il ne détecte pas tous les problèmes — il ne remplace pas une vérification manuelle mais constitue un premier filtre utile.

**Problèmes détectés** : texte alt manquant, objets non alignés, contraste insuffisant, styles de titre absents, ordre de lecture, tableaux sans en-tête.

**Problèmes non détectés** : qualité du texte alt, pertinence des noms de liens, couleur porteuse de sens, langue des passages étrangers.

---

## Checklist rapide

| # | Critère | Réf. |
|---|---------|------|
| 1 | Fichier enregistré en .docx avec nom descriptif | S.8 |
| 2 | Document non protégé (restrictions levées) | S.8 |
| 3 | Titres créés avec les styles intégrés (Titre 1, 2, 3...) | S.1 |
| 4 | Hiérarchie des titres cohérente dans le volet de navigation | S.1 |
| 5 | Listes créées avec Puces/Numérotation (pas tirets manuels) | S.1 |
| 6 | Colonnes créées avec l'outil Colonnes (pas tabulations) | S.1 |
| 7 | Sauts de page avec Insertion > Saut de page (pas retours chariot) | S.1 |
| 8 | Tableaux de mise en page : ordre de lecture correct et alignés | S.1 |
| 9 | Tableaux de données simples, en-têtes identifiés, alignés | S.1 |
| 10 | Contraste >= 4,5:1 (standard) ou >= 3:1 (grande taille) | S.2 |
| 11 | Couleur porteuse de sens doublée en texte | S.2 |
| 12 | Texte alt sur chaque image/objet significatif ; décoratifs marqués | S.3 |
| 13 | Images, objets et zones de texte alignés avec le texte | S.3 |
| 14 | Liens avec noms descriptifs uniques | S.3 |
| 15 | Informations essentielles reproduites dans le corps du document | S.3 |
| 16 | Passages en langue étrangère balisés | S.4 |
| 17 | Médias avec transcription/sous-titres/description audio | S.5 |
| 18 | Aucun objet clignotant | S.6 |
| 19 | Propriétés du document renseignées (titre, auteur) | S.7 |
| 20 | Aucun formulaire interactif Word | Principes |
| 21 | Vérificateur d'accessibilité intégré exécuté sans erreur | S.9 |
