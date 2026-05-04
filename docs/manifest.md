# Manifeste des erreurs injectées

Généré depuis `03-easy-checks/evaluation_contract.yml`.

Chaque section décrit une page de l'exercice, le Point de contrôle rapide visé, les erreurs injectées et la correction attendue.

## 1. Actualité illustrée

**Point de contrôle rapide :** Texte alternatif des images

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

### Erreurs injectées

- Titre non informatif de type Sans titre.
- Titre identique sur plusieurs pages de résultats.
- Information spécifique placée trop tard après le nom long du ministère.

### Outils de détection

- Onglet navigateur
- Code source
- WAVE

### Correction attendue

Titre unique, spécifique et ordonné du particulier vers le général, par exemple Recherche "RGAA" - Page 2/3 - Ministère de l'Accessibilité numérique.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 3. Guide du RGAA

**Point de contrôle rapide :** Titres de rubriques

### Erreurs injectées

- Plusieurs titres visuels non balisés.
- Balise de titre détournée pour un effet visuel.
- Titre de niveau 1 utilisé au milieu du contenu, à analyser avec nuance.

### Outils de détection

- HeadingsMap
- WAVE
- DevTools

### Correction attendue

Titre visuel balisé avec un élément de titre natif ou role heading/aria-level si nécessaire ; balise de titre réservée aux vrais titres ; hiérarchie globalement pertinente et niveaux continus par bonne pratique.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 4. Charte de publication

**Point de contrôle rapide :** Contraste

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

**Point de contrôle rapide :** Focus clavier visible

### Erreurs injectées

- Focus visible supprimé sur un bouton.
- Focus visible supprimé sur une carte cliquable.
- Focus visible supprimé ou très peu perceptible sur un accordéon DSFR mal surchargé.

### Outils de détection

- Clavier
- Tab
- Shift+Tab
- ANDI

### Correction attendue

Focus visible DSFR conservé sur boutons, liens/cartes et accordéons ; ordre de tabulation logique ; aucun piège clavier ; comportement clavier des accordéons conforme à la fiche DSFR.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 7. Atelier international

**Point de contrôle rapide :** Langue de la page

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

**Point de contrôle rapide :** Zoom 200 %

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

**Point de contrôle rapide :** Sous-titres

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

## 10. Podcast RGAA

**Point de contrôle rapide :** Transcriptions

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

Étiquette visible et persistante ; association label for/id ; placeholder utilisé seulement comme exemple ; nom accessible qui reprend le nom visible ; aide à la saisie reliée avec aria-describedby ; groupes DSFR structurés avec fieldset.fr-fieldset, legend.fr-fieldset__legend, fr-fieldset__element et fr-messages-group.

### Aide associée

La page d'aide reprend les trois niveaux : indice, ce qui pose problème, comment corriger.

## 13. Demande d'audit

**Point de contrôle rapide :** Champs obligatoires

### Erreurs injectées

- Champs obligatoires indiqués uniquement par couleur, bordure rouge ou astérisque non expliqué.
- Absence de required ou aria-required.
- Message d'erreur trop vague.
- Message d'erreur non associé au champ.
- Focus non ramené vers le récapitulatif ou le premier champ en erreur.

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
