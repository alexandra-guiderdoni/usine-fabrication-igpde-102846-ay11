# Règles d'implémentation DSFR - Code et accessibilité

Document de travail pour l'exercice « Ministère de l'Accessibilité numérique ».

Objectif : transformer les fiches DSFR **Code** et **Accessibilité** en contraintes vérifiables pendant la production du faux site, de la version d'aide et de la version accessible.

Références sources : `03-easy-checks/dsfr-component-links.md`.

---

## Règle générale projet

- Utiliser les assets DSFR localisés dans le dépôt, sans CDN.
- Ne pas coder un composant DSFR à partir de son rendu visuel uniquement.
- Pour chaque composant utilisé, vérifier la structure HTML, les attributs ARIA, les états clavier, le focus, les contrastes et le comportement responsive.
- La version accessible doit être sobre et conforme ; la version inaccessible ne doit dégrader que l'erreur pédagogique prévue par la page.
- Les composants d'aide visibles ne sont autorisés que dans `site-aide-correction/`.

## Socle transverse

### En-tête

Version accessible :

- Utiliser un `<header class="fr-header" role="banner">`.
- Inclure le bloc marque République française.
- Placer le lien de retour à l'accueil sur le nom du site, la baseline ou le logo selon la structure retenue.
- Renseigner un `title` de lien d'accueil explicite : `Accueil - Ministère de l'Accessibilité numérique`.
- Ne pas masquer le nom du site ni la baseline au zoom ou en mobile.
- Si recherche ou navigation sont incluses dans l'en-tête, appliquer aussi les règles des composants concernés.

À éviter :

- Header visuellement DSFR mais sans `role="banner"`.
- Logo ou image opérateur sans alternative.
- Lien d'accueil ambigu ou intitulé uniquement par une image.

### Navigation principale

Version accessible :

- Utiliser `<nav class="fr-nav" role="navigation" aria-label="Menu principal">`.
- Structurer les entrées dans une liste `<ul class="fr-nav__list">` avec `<li class="fr-nav__item">`.
- Utiliser des liens directs `<a class="fr-nav__link">` pour les entrées simples.
- Indiquer la page active avec `aria-current="page"` sur le lien actif.
- Pour un menu ouvrant, utiliser un `<button type="button" class="fr-nav__btn">` avec `aria-expanded` et `aria-controls`.
- Vérifier `Entrée`, `Espace`, `Tab` et `Maj + Tab`.

À éviter :

- Liste de navigation en simples `<div>`.
- Bouton de menu sans lien technique avec son panneau.
- État actif visible uniquement par la couleur.

### Liens d'évitement

Version accessible :

- Placer le composant tout en haut de page, avant l'en-tête.
- Utiliser `.fr-skiplinks`, puis `<nav role="navigation" aria-label="Accès rapide" class="fr-container">`.
- Structurer plusieurs liens dans `<ul class="fr-skiplinks__list">`.
- Placer le lien vers le contenu principal en premier.
- Vérifier que chaque `href="#..."` pointe vers un `id` réellement présent.
- Vérifier au clavier que les liens apparaissent au focus et déplacent bien la navigation.

À éviter :

- Aucun lien d'évitement.
- Lien présent mais caché par `display:none` ou jamais visible au focus.
- Ancre cassée, par exemple `href="#contenu"` sans `id="contenu"`.

### Pied de page

Version accessible :

- Utiliser `<footer class="fr-footer" role="contentinfo" id="footer">`.
- Garder un `id` stable si un lien d'évitement pointe vers le pied de page.
- Inclure une mention d'accessibilité visible : `Accessibilité : totalement conforme`, `partiellement conforme` ou `non conforme` selon la page de démonstration.
- Structurer les groupes de liens en listes.
- Vérifier que les liens obligatoires restent accessibles au clavier.

À éviter :

- Footer sans rôle ou sans mention d'accessibilité.
- Liens de pied de page en texte non cliquable.
- Mentions ou liens supprimés au zoom.

## Navigation et liens

### Fil d'Ariane

Version accessible :

- Utiliser `<nav role="navigation" class="fr-breadcrumb" aria-label="vous êtes ici :">`.
- Structurer le chemin dans une liste ordonnée `<ol class="fr-breadcrumb__list">`.
- Placer le fil d'Ariane en dehors du `<main>`.
- Identifier la page courante avec `aria-current="page"`.
- Ne pas transformer la page courante en lien cliquable inutile.
- Conserver le même emplacement sur les pages d'une même version.

À éviter :

- Fil d'Ariane en texte linéaire sans liste.
- Page courante seulement distinguée par style visuel.
- Fil d'Ariane placé après le contenu principal.

### Lien

Version accessible :

- Utiliser `<a href="..." class="fr-link">` pour un lien composant.
- Donner un intitulé qui permet de comprendre la destination ou la fonction.
- Pour une succession de liens, structurer en liste `<ul><li>`.
- Pour un lien externe en nouvel onglet : `target="_blank"`, `rel="noopener external"` et indication `nouvelle fenêtre` dans le `title`.
- Pour un téléchargement : libellé commençant par `Télécharger`, détail avec format et poids via `.fr-link__detail`.
- Pour une information complémentaire non visible dans l'intitulé, utiliser `aria-describedby`.

À éviter :

- Lien sans `href`.
- Intitulé générique : `cliquez ici`, `en savoir plus`, `lire la suite` sans contexte.
- Image-lien dont l'alternative décrit l'image au lieu de la destination ou de l'action.
- Lien composite dont l'icône décorative ajoute du bruit au nom accessible.

## Contenus, cartes et affichage

### Carte

Version accessible :

- Utiliser `<div class="fr-card">` dans une grille DSFR responsive.
- Garder `fr-card__body` et `fr-card__content`.
- Le titre est obligatoire, avec un niveau de titre cohérent et la classe `fr-card__title`.
- Placer le lien principal uniquement sur le titre.
- Utiliser `fr-enlarge-link` seulement si la carte ne contient aucun autre élément cliquable.
- Placer les médias, descriptions, badges, détails et actions après le titre dans le code.
- Les images de carte peuvent être décoratives ou informatives selon le contexte ; choisir `alt=""` ou un texte alternatif utile.

À éviter :

- Carte entièrement cliquable avec plusieurs actions concurrentes.
- Titre visuel non balisé en titre.
- Hauteur fixe ou `overflow:hidden` qui coupe le contenu au zoom 200 %.

### Accordéon

Version accessible :

- Utiliser `<section class="fr-accordion">`.
- Placer le bouton dans un titre `h2`, `h3`, etc. cohérent avec la page, classe `fr-accordion__title`.
- Le bouton doit être `<button type="button" class="fr-accordion__btn">`.
- Relier bouton et contenu avec `aria-controls` et un `id` unique sur `.fr-collapse`.
- Synchroniser `aria-expanded="true|false"` avec l'état réel.
- Pour l'aide à la correction, privilégier les accordéons dissociés lorsque plusieurs panneaux doivent pouvoir rester ouverts.
- Vérifier `Entrée`, `Espace`, `Tab` et le parcours dans le contenu ouvert.

À éviter :

- Accordéon simulé avec un lien ou un `<div>` cliquable.
- `aria-controls` vers un `id` inexistant.
- Texte directement dans une `div` sans balises de contenu.

### Mise en avant

Version accessible :

- Utiliser `<div class="fr-callout">`.
- Ajouter un titre `fr-callout__title` lorsque le bloc doit être repérable.
- Utiliser un niveau de titre cohérent avec la page.
- Porter l'information par le texte, pas par la bordure, l'icône ou la couleur.
- Utiliser `fr-callout__text` pour le contenu principal.

À éviter :

- Mise en avant qui transmet un statut uniquement par couleur.
- Icône utilisée comme seule information.
- Citation codée en mise en avant.

### Tuile

Version accessible :

- Utiliser `<div class="fr-tile">` dans une grille responsive.
- Le corps `fr-tile__body` et le titre `fr-tile__title` sont obligatoires.
- Placer le lien sur le titre, avec un intitulé explicite.
- Utiliser `fr-enlarge-link` seulement s'il n'y a pas d'autre élément cliquable.
- Considérer le pictogramme comme décoratif.
- Garder descriptions, badges, tags et détails après le titre dans le code.

À éviter :

- Tuile avec image ou pictogramme porteur d'information non textualisée.
- Tuile dont seule la couleur indique le statut.
- Zone cliquable étendue autour d'une tuile contenant déjà plusieurs liens.

### Badge

Version accessible :

- Utiliser `<p class="fr-badge">` lorsque le badge est autonome.
- Utiliser `<span class="fr-badge">` si le badge est inclus dans un élément ayant déjà une sémantique, par exemple un paragraphe ou un item de liste.
- Structurer plusieurs badges dans une liste.
- L'information de statut doit être dans le texte du badge ; l'icône est décorative.
- Vérifier le contraste si une couleur est personnalisée.

À éviter :

- Badge qui dit seulement `OK`, `Nouveau`, `Urgent` sans contexte.
- Statut transmis uniquement par couleur ou icône.
- Badge interactif déguisé en bouton ou en lien.

### Tableau

À utiliser seulement si un vrai besoin de données apparaît.

Version accessible :

- Utiliser le composant DSFR `.fr-table` avec wrappers `fr-table__wrapper`, `fr-table__container`, `fr-table__content`.
- Utiliser un vrai `<table>`.
- Fournir un `<caption>` pertinent.
- Utiliser `<thead>`, `<tbody>`, `<tr>`, `<th>` et `<td>`.
- Associer les en-têtes simples avec `scope="col"` ou `scope="row"`.
- En cas de tableau complexe avec cellules fusionnées, ajouter un résumé et utiliser `id` / `headers` au lieu de se contenter de `scope`.

À éviter :

- Tableau de mise en page codé comme tableau de données.
- Tableau de données sans en-têtes.
- Cellules fusionnées sans résumé ni associations explicites.

## Recherche et formulaires

### Barre de recherche

Version accessible :

- Utiliser `<div class="fr-search-bar" role="search">`.
- Utiliser `<input type="search" class="fr-input">`.
- Associer le champ à un `<label class="fr-label" for="...">`.
- Garder un bouton `<button type="button" class="fr-btn">` avec intitulé et `title` explicites.
- Relier les messages éventuels avec `aria-describedby`.
- Utiliser `aria-live="polite"` si un groupe de messages est rempli dynamiquement.

À éviter :

- Placeholder comme seule étiquette.
- Bouton icône sans nom accessible.
- Champ de recherche sans rôle `search`.

### Formulaire

Version accessible :

- Regrouper les champs de même nature avec `<fieldset class="fr-fieldset">` et `<legend class="fr-fieldset__legend">`.
- Utiliser `fr-fieldset__element` pour chaque champ.
- Mentionner les champs obligatoires au début du formulaire.
- Utiliser `required` sur les champs obligatoires.
- Rendre les messages d'aide, d'erreur ou de succès accessibles via texte relié au champ, `aria-describedby`, ou live region selon le contexte.
- Après soumission en erreur, placer le focus à un endroit pertinent : résumé d'erreurs ou premier champ en erreur.

À éviter :

- Groupe de radios ou cases à cocher sans `fieldset` / `legend`.
- Obligation transmise seulement par couleur ou astérisque non expliqué.
- Message d'erreur vague ou non relié au champ concerné.

### Champ de saisie

Version accessible :

- Utiliser `<div class="fr-input-group">`.
- Utiliser un `<label class="fr-label" for="...">` explicitement lié à un `id` unique.
- Placer les aides de format dans un `<span class="fr-hint-text">` dans le label ou dans un texte relié au champ.
- Relier le bloc `fr-messages-group` au champ via `aria-describedby`.
- Utiliser `aria-live="polite"` si les messages peuvent apparaître dynamiquement.
- Utiliser `aria-invalid="true"` sur un champ en erreur lorsque l'état est affiché.

À éviter :

- Label visuel non lié au champ.
- Plusieurs labels associés au même champ pour faire une aide de saisie.
- Label masqué avec `display:none`.
- Placeholder seul.

### Bouton

Version accessible :

- Utiliser `<button class="fr-btn" type="button">` pour une action.
- Utiliser `type="submit"` uniquement pour une soumission réelle.
- Donner un intitulé textuel précis.
- Si `aria-label` ou `aria-labelledby` est utilisé sur un bouton textuel, reprendre le nom visible dans le nom accessible.
- Limiter les boutons icône seule aux actions très familières ; dans ce cas, ajouter un nom accessible explicite.
- Vérifier `Entrée` et `Espace`.

À éviter :

- Bouton codé avec un lien ou une `div`.
- Libellé générique : `OK`, `Valider`, `Envoyer` sans contexte lorsque plusieurs actions sont proches.
- Focus supprimé par CSS.

### Case à cocher

Version accessible :

- Utiliser `<div class="fr-checkbox-group">`.
- Utiliser `<input type="checkbox">` avec `id` unique.
- Associer un `<label class="fr-label" for="...">`.
- Pour plusieurs cases liées, utiliser `<fieldset>` et `<legend>`.
- Relier les messages avec `aria-describedby`.
- Vérifier `Espace`, `Tab` et `Maj + Tab`.

À éviter :

- Case visuelle non native.
- Label non lié par `for` / `id`.
- Groupe de choix sans question globale.

### Bouton radio

Version accessible :

- Utiliser les radios uniquement en groupe.
- Chaque option utilise `<div class="fr-radio-group">`, `<input type="radio">` et `<label class="fr-label" for="...">`.
- Le groupe utilise `<fieldset class="fr-fieldset">` et `<legend class="fr-fieldset__legend">`.
- Tous les radios d'un même groupe partagent le même `name`.
- Vérifier `Espace`, flèches haut/bas/gauche/droite et focus initial du groupe.

À éviter :

- Radio isolé hors groupe.
- Options `Oui` / `Non` sans question portée par une légende.
- Label visuel non associé.

### Alerte et messages d'erreur

Version accessible :

- Utiliser `<div class="fr-alert fr-alert--error|warning|success|info">`.
- Si l'alerte a un titre, choisir un niveau cohérent avec la page et utiliser `fr-alert__title`.
- Indiquer textuellement le type d'alerte : `erreur`, `attention`, `succès`, `information`.
- Pour une alerte ajoutée dynamiquement, utiliser `role="alert"` pour erreur/avertissement, `role="status"` pour succès/information si adapté.
- Ne pas faire disparaître une alerte sans action utilisateur.
- Si elle est refermable, le bouton de fermeture doit avoir un intitulé explicite et le focus doit être repositionné.
- Pour un formulaire, ne pas se limiter à l'alerte globale : relier aussi chaque erreur au champ concerné.

À éviter :

- Message rouge sans texte d'erreur explicite.
- Alerte globale sans liens ou associations vers les champs.
- Toast temporaire qui disparaît seul.

## Médias

### Contenu médias

Version accessible :

- Utiliser `<figure class="fr-content-media">`.
- Ajouter `figcaption` pour la description ou la source.
- Si la figure a une légende, reprendre son sens dans `aria-label`.
- Pour une image, l'attribut `alt` est toujours présent : vide si décorative, renseigné si informative.
- Pour une vidéo HTML, utiliser `<video controls class="fr-responsive-vid">`.
- Ne pas lancer la lecture sans action utilisateur.
- Les vidéos hors direct doivent avoir des sous-titres.
- Si l'alternative est longue, utiliser une transcription sous le média.

À éviter :

- Image informative sans `alt`.
- Image décorative bavarde.
- Vidéo sans contrôle, sans sous-titres ou sans alternative au contenu visuel/auditif.

### Transcription

Version accessible :

- Utiliser `<div class="fr-transcription">`.
- Le bouton d'ouverture est `type="button"` avec `aria-expanded` et `aria-controls`.
- Le contenu refermable possède un `id` unique et la classe `fr-collapse`.
- Le bouton d'agrandissement de la transcription a `aria-label="Agrandir la transcription"` et `aria-controls`.
- La modale utilise `<dialog class="fr-modal">`, `aria-modal="true"` et `aria-labelledby`.
- La modale de transcription contient un titre de niveau `h1`.
- Le bouton de fermeture est un vrai bouton de type `button`.

À éviter :

- Transcription fournie dans un fichier introuvable ou lien générique.
- Accordéon de transcription non relié au contenu.
- Modale sans nom accessible.

## Contrôles avant livraison

- Le premier `Tab` atteint bien les liens d'évitement.
- Tous les liens `href="#..."` ont une cible existante.
- Tous les boutons ouvrants ont `aria-expanded`, `aria-controls` et un panneau correspondant.
- Tous les champs ont un nom accessible pertinent, visible ou explicitement relié.
- Tous les groupes de choix ont `fieldset` et `legend`.
- Aucun focus visible n'est supprimé dans `site-accessible/`.
- Aucun message important n'est porté uniquement par la couleur, la forme ou l'icône.
- Zoom 200 % : pas de perte de contenu ni de superposition bloquante.
- Version accessible : pas de texte pédagogique visible.
- Version inaccessible : l'erreur principale reste détectable par la grille, mais le site reste crédible.
