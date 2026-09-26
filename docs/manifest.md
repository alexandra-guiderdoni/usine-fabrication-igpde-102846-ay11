# Manifeste des erreurs injectées

Généré depuis `03-easy-checks/evaluation_contract.yml`.

Chaque section décrit une page de l'exercice, le Point de contrôle rapide visé, les erreurs injectées et la correction attendue.

## 1. Actualité illustrée

**Point de contrôle rapide :** Texte alternatif des images

### Repère pédagogique

Niveau 1 - Observer le rôle de chaque image et la structure HTML des liens. Identifiez les 4 cas : image informative, image décorative, lien image pur et lien composite.

### Erreurs injectées

- Image informative sans alternative ou avec alt vide.
- Image décorative trop bavarde.
- Image-lien courriel avec alternative qui décrit l'image au lieu d'indiquer l'action.
- Lien composite SMS dont l'icône décorative a une alternative qui ajoute du bruit.

### Outils de détection

- WAVE
- ANDI
- Inspection HTML

### Correction attendue

Image informative : alternative courte reprenant l'information. Image décorative : alt vide. Image-lien courriel : alternative indiquant l'action. Lien composite SMS : icône décorative avec alt vide si le texte visible suffit.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 2. Résultats de recherche RGAA

**Point de contrôle rapide :** Titre de page

### Repère pédagogique

Regarder l'onglet du navigateur, le title HTML et le résultat WAVE. La page affiche déjà la requête, le tri, la page courante et le nombre de résultats : ces informations doivent aussi guider le titre.

### Erreurs injectées

- Titre non informatif de type Sans titre.
- Titre identique sur plusieurs pages de résultats.
- Information spécifique placée trop tard après le nom long du ministère.

### Outils de détection

- Onglet navigateur
- Code source
- WAVE

### Correction attendue

Titre unique, spécifique et ordonné du particulier vers le général, par exemple Recherche "RGAA" - Page 2/3 - Formation 102846 - Accessibilité numérique.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 3. Guide du RGAA

**Point de contrôle rapide :** Titres et hiérarchie

### Repère pédagogique

Afficher le plan de titres avec HeadingsMap, puis le comparer au plan visuel. Chercher les titres visibles qui n'apparaissent pas dans le plan, et les titres du plan qui ne correspondent pas à une vraie rubrique.

### Erreurs injectées

- Plusieurs titres visuels non balisés.
- Balise de titre détournée pour un effet visuel.
- Titre de niveau 1 utilisé au milieu du contenu, à analyser avec nuance.

### Outils de détection

- HeadingsMap
- WAVE
- DevTools

### Correction attendue

Titre visuel balisé avec un élément de titre natif ou `role="heading"`/`aria-level` si nécessaire ; balise de titre réservée aux vrais titres ; hiérarchie globalement pertinente et niveaux continus par bonne pratique.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 4. Charte de publication

**Point de contrôle rapide :** Contraste des couleurs

### Repère pédagogique

Mesurer un texte, un lien ou un bouton avec un outil de contraste.

### Erreurs injectées

- Texte courant gris clair sur blanc.
- Lien ou bouton d'action trop pâle.
- Information de statut transmise par une couleur faible.

### Outils de détection

- WebAIM Contrast Checker
- Colour Contrast Analyser
- WCAG Contrast Checker
- Vispero Color Contrast Checker
- WAVE

### Correction attendue

Ratio conforme : 4,5:1 pour texte normal ; 3:1 pour texte large et composants.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 5. Accès rapide aux contenus

**Point de contrôle rapide :** Lien d'évitement

### Repère pédagogique

Appuyer une fois sur Tab au chargement de la page. Vérifier ensuite que le lien affiché est visible, compréhensible et activable sans souris.

### Erreurs injectées

- Lien d'évitement absent.
- Lien présent mais invisible au focus.
- Lien présent mais cible d'ancre invalide ou inexistante.

### Outils de détection

- Clavier
- Premier appui sur Tab
- Vérification de l'ancre cible

### Correction attendue

Utiliser le composant DSFR Liens d'évitement : bloc placé tout en haut de page, avant l'en-tête ; navigation aria-label Accès rapide ; liste de liens simples ; premier lien vers le contenu principal ; ancres valides.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 6. Parcours clavier

**Point de contrôle rapide :** Focus et navigation clavier

### Repère pédagogique

Laisser la souris de côté et parcourir toute la page avec Tab, Shift+Tab, Entrée et Espace. À chaque arrêt, demander : où suis-je, quelle action puis-je lancer, puis-je revenir en arrière ?

### Erreurs injectées

- Liens d'action secondaires activables à la souris mais absents de l'ordre de tabulation.
- Focus visible supprimé sur un bouton.
- Focus visible supprimé sur une carte cliquable.
- Focus visible supprimé ou très peu perceptible sur un accordéon DSFR mal surchargé.
- Bouton Publier la session atteignable au clavier, mais la modale de publication piège ensuite le clavier : Tab reste bloqué et Échap ne referme pas la fenêtre.

### Outils de détection

- Clavier
- Tab
- Shift+Tab
- ANDI

### Correction attendue

Focus visible DSFR conservé sur boutons, liens/cartes, accordéons et modale ; ordre de tabulation logique ; aucun piège clavier ; comportement clavier des accordéons et de la modale conforme aux fiches DSFR.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 7. Atelier international

**Point de contrôle rapide :** Langue de la page

### Repère pédagogique

Inspecter la balise html, puis les expressions réellement rédigées dans une autre langue. Vérifier aussi que les codes utilisés sont des codes de langue, pas des noms complets ou des codes pays.

### Erreurs injectées

- Attribut lang invalide sur html.
- Passage en anglais non balisé dans une page française.
- Code langue invalide sur un passage anglais.
- Passage en arabe sans langue ni sens de lecture déclarés.

### Outils de détection

- Web Developer
- Code source
- WAVE

### Correction attendue

lang fr sur la page ; codes langue ISO 639 valides ; passages anglais avec lang en si nécessaire ; passage arabe avec lang ar et dir rtl ; pas de sur-balisage des noms propres ou mots entrés dans l'usage courant.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 8. Ressources à zoomer

**Point de contrôle rapide :** Zoom à 200 %

### Repère pédagogique

Passer le navigateur à 200 % et réduire la largeur de fenêtre.

### Erreurs injectées

- Cartes avec hauteur fixe.
- Grille avec largeur minimale rigide qui force un défilement horizontal.
- Overflow masqué provoquant texte tronqué, boutons sortis ou superposition au zoom 200 %.

### Outils de détection

- Zoom navigateur 200 %
- Fenêtre étroite

### Correction attendue

Cartes DSFR fluides ; grille responsive ; contenu visible ; reflow sans perte ; composants utilisables.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 9. Vidéo de sensibilisation

**Point de contrôle rapide :** Sous-titres vidéo

### Repère pédagogique

Lire la vidéo sans le son et vérifier la présence d'une piste de sous-titres exploitable.

### Erreurs injectées

- Vidéo sans sous-titres.
- Sous-titres automatiques non relus.

### Outils de détection

- Lecteur vidéo
- Bouton sous-titres
- Écoute sans son

### Correction attendue

Sous-titres synchronisés, relus, ponctués, avec sons utiles.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 10. Écouter un podcast

**Point de contrôle rapide :** Transcriptions audio et vidéo

### Repère pédagogique

Chercher un lien de transcription immédiatement proche du lecteur audio.

### Erreurs injectées

- Audio sans lien visible vers une transcription.

### Outils de détection

- Revue humaine
- Inspection des liens proches du média

### Correction attendue

Lien proche du média vers une transcription structurée et complète.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 11. Démonstration vidéo

**Point de contrôle rapide :** Audiodescription

### Repère pédagogique

Commencer par la présence : la vidéo propose-t-elle une piste de sous-titres, une transcription proche du lecteur et une version ou piste audiodécrite ? Ensuite seulement, juger leur pertinence.

### Erreurs injectées

- Information visuelle essentielle non décrite dans l'audio principal.
- Absence de piste ou version audiodécrite.

### Outils de détection

- Revue humaine de la vidéo
- Comparaison audio / information visuelle

### Correction attendue

Description intégrée, piste audiodécrite ou version alternative selon faisabilité.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 12. Inscription à un webinaire

**Point de contrôle rapide :** Étiquettes de formulaire

### Repère pédagogique

Vérifier uniquement le nom accessible des champs et des groupes avec ANDI, WAVE ou l'arbre d'accessibilité. Tester aussi le clic sur les libellés visibles. Les champs obligatoires et les erreurs seront traités dans le point 13.

### Erreurs injectées

- Placeholder utilisé comme seule étiquette.
- Étiquette visible non associée au champ.
- Groupe de boutons radio ou cases à cocher présenté avec des classes DSFR mais sans fieldset/legend natifs.

### Outils de détection

- ANDI
- WAVE
- Clic sur le label
- Test clavier
- DevTools Accessibility Tree
- Lecteur d'écran si disponible

### Correction attendue

Étiquette visible et persistante ; association label for/id ; placeholder utilisé seulement comme exemple ; nom accessible qui reprend le nom visible ; aide à la saisie reliée avec aria-describedby ; groupes DSFR structurés avec fieldset.fr-fieldset, legend.fr-fieldset__legend, `fr-fieldset__element` et fr-messages-group.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 13. Formulaire de contact

**Point de contrôle rapide :** Champs obligatoires et erreurs

### Repère pédagogique

Observer d'abord le formulaire avant envoi, puis le soumettre vide. Comparer l'état initial et l'état après soumission. Ici, les libellés doivent déjà être compréhensibles : le test porte sur l'obligation, les messages et le guidage après erreur.

### Erreurs injectées

- Champs obligatoires indiqués uniquement par couleur, bordure rouge ou astérisque non expliqué.
- Absence de required ou aria-required.
- Message d'erreur trop vague.
- Message d'erreur non associé au champ.
- Focus non ramené vers le récapitulatif ou le premier champ en erreur.

### Scénario de test

- Avant soumission : Vérifier l'état initial : les champs obligatoires du formulaire de contact doivent être annoncés avant l'envoi, sans afficher d'erreur prématurée.
- Après soumission : Soumettre le formulaire vide, puis vérifier l'aide à la correction : message précis, relié au champ, et focus accompagné.

### Outils de détection

- Soumission du formulaire
- Clavier
- Lecteur d'écran
- Inspection HTML
- Vérification aria-describedby
- Vérification aria-invalid
- Vérification required
- Déplacement de focus

### Correction attendue

Mention textuelle obligatoire ou règle claire sur les champs optionnels ; required ou aria-required ; astérisque expliqué si utilisé ; message d'erreur précis avec exemple ou format attendu ; erreur associée au champ ; aria-invalid true si pertinent ; focus placé sur le récapitulatif d'erreurs ou le premier champ en erreur.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.
