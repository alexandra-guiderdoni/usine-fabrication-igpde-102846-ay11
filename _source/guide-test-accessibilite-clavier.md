# Guide débutant — tester l’accessibilité au clavier

**Auteur** : Ilknur Eren
**Publié dans** : Accessibility — 23 mars 2026
**Traduction et adaptation en français**

---

## Vue d’ensemble

Tester manuellement un site web est une étape critique pour s’assurer que les utilisateurs de lecteurs d’écran peuvent accéder au contenu et le comprendre. Les outils automatisés détectent certaines anomalies, mais ne reproduisent pas l’expérience réelle d’une navigation sans souris.

Les tests au clavier offrent un moyen simple et efficace de simuler la façon dont de nombreux utilisateurs interagissent avec les technologies d’assistance. Cinq commandes fondamentales suffisent aux concepteurs et développeurs pour parcourir un site uniquement au clavier.

En apprenant ce petit jeu de raccourcis, les équipes obtiennent un retour concret sur le fonctionnement de leurs interfaces pour les utilisateurs de lecteurs d’écran et identifient des obstacles qui passeraient autrement inaperçus.

---

## Les cinq commandes fondamentales

### Tab — avancer entre les éléments interactifs

La touche `Tab` déplace le focus en avant sur les éléments interactifs de la page : liens, boutons, champs de saisie, cases à cocher. À chaque appui, le navigateur doit indiquer visuellement la position courante, généralement par un contour ou une surbrillance colorée. Cet indicateur de focus est vital pour les utilisateurs malvoyants qui s’appuient sur un lecteur d’écran en complément de ce qu’ils voient.

**Trois vérifications à effectuer** :

- `Tab` déplace bien le focus vers l’élément interactif suivant
- un indicateur de focus visible entoure l’élément actif
- l’ordre de tabulation suit une logique descendante cohérente avec la page

### Shift + Tab — reculer entre les éléments interactifs

`Shift + Tab` fonctionne comme `Tab` mais en sens inverse : le focus remonte vers l’élément interactif précédent. Il faut s’assurer que ce retour suit un ordre logique.

**Cas d’usage typiques** :

- on est passé trop vite à l’élément suivant et on souhaite revenir en arrière
- dans un formulaire, une faute de frappe oblige à remonter dans un champ précédent

Lors d’un test d’accessibilité, vérifier que `Shift + Tab` fonctionne comme prévu dans les deux sens.

### Entrée — activer l’élément ciblé

La touche `Entrée` active l’élément interactif qui a le focus. En tabulant, si l’utilisateur veut déclencher le lien sur lequel il se trouve, il appuie sur `Entrée`. De même, dans un formulaire, `Entrée` soumet les données.

Lors d’un test manuel, vérifier que `Entrée` déclenche bien l’action associée. Exemple : si le focus est sur un lien, appuyer sur `Entrée` doit ouvrir la page cible. Si l’action ne se produit pas, il y a un défaut à corriger.

### Barre d’espace — modifier l’état d’un élément

Là où `Entrée` sert le plus souvent à « aller quelque part », la barre d’espace sert à « changer quelque chose » sur l’écran courant. Elle s’utilise notamment sur les cases à cocher et les boutons radio.

Un appui sur la barre d’espace coche ou décoche la case. Il est essentiel que ces composants annoncent leur **état courant** (coché ou non) aux utilisateurs de lecteurs d’écran, afin qu’ils puissent décider s’ils souhaitent changer cet état.

### Flèches directionnelles — lire le contenu ligne par ligne

`Tab` et `Shift + Tab` sautent d’un élément interactif à l’autre et ignorent tout ce qui se trouve entre eux. Pour **lire** la page, on utilise les flèches `Haut` et `Bas` : le focus se déplace ligne par ligne, ce qui permet aux utilisateurs de lecteurs d’écran de parcourir le contenu.

Ce mode de navigation permet aussi d’entendre le texte alternatif des images, et donc de donner du contexte à un contenu visuel qui serait autrement inaccessible. S’assurer que toutes les images porteuses de sens disposent d’une alternative textuelle descriptive est un pilier de l’accessibilité, et la navigation aux flèches est l’un des principaux canaux par lesquels les utilisateurs accèdent à cette information.

---

## Conclusion

Ensemble, ces cinq commandes — `Tab`, `Shift + Tab`, `Entrée`, `Barre d’espace` et les flèches directionnelles — forment le socle du test d’accessibilité manuel. Elles permettent aux développeurs d’éprouver leurs sites sous un autre angle et d’identifier des problèmes qu’un simple examen visuel ne révèle pas.

En testant systématiquement avec ces touches, les équipes construisent des expériences numériques plus inclusives et plus utilisables. L’accessibilité n’est pas qu’une exigence technique : c’est l’engagement de garantir que toute personne, quelles que soient ses capacités, puisse interagir avec le web et en tirer parti.
