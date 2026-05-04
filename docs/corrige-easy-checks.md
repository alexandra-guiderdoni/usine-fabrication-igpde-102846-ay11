# Corrigé points de contrôle rapides

Généré depuis `03-easy-checks/evaluation_contract.yml`.

## 1. Actualité illustrée

- Point de contrôle rapide : Texte alternatif des images
- Constat minimal attendu : Au moins une image n'a pas d'alternative adaptée à son rôle réel.
- Sévérité indicative : Gênant
- Preuve possible : Capture WAVE/ANDI ou extrait HTML montrant alt absent, vide ou inadapté sur l'image concernée.
- Correction : Image informative : alternative courte reprenant l'information. Image décorative : alt vide. Image-lien courriel : alternative indiquant l'action. Lien composite SMS : icône décorative avec alt vide si le texte visible suffit.
- Occurrences bonus : Image décorative bavarde. ; Image-lien dont l'alternative décrit l'image au lieu de l'action. ; Lien composite dont l'icône ajoute du bruit dans le nom accessible.
- À ne pas pénaliser : Image purement décorative avec alt vide.

## 2. Résultats de recherche RGAA

- Point de contrôle rapide : Titre de page
- Constat minimal attendu : Le titre de page ne permet pas d'identifier précisément la page ou son état.
- Sévérité indicative : Gênant
- Preuve possible : Onglet navigateur ou extrait title montrant un titre absent, générique, dupliqué ou mal ordonné.
- Correction : Titre unique, spécifique et ordonné du particulier vers le général, par exemple Recherche "RGAA" - Page 2/3 - Ministère de l'Accessibilité numérique.
- Occurrences bonus : Titre absent ou intitulé Sans titre. ; Pagination absente du titre. ; Requête de recherche absente. ; Nom du ministère placé avant l'information spécifique.
- À ne pas pénaliser : Titre long si l'information spécifique est présente en premier.

## 3. Guide du RGAA

- Point de contrôle rapide : Titres de rubriques
- Constat minimal attendu : Un ou plusieurs textes visuellement présentés comme titres ne sont pas balisés comme titres, ou une balise de titre est utilisée pour une simple mise en valeur.
- Sévérité indicative : Gênant
- Preuve possible : HeadingsMap/WAVE ou extrait HTML montrant les faux titres en paragraphes, ou le titre détourné pour la présentation.
- Correction : Titre visuel balisé avec un élément de titre natif ou role heading/aria-level si nécessaire ; balise de titre réservée aux vrais titres ; hiérarchie globalement pertinente et niveaux continus par bonne pratique.
- Occurrences bonus : Comparer le plan visuel et le plan technique. ; Repérer un titre non pertinent. ; Qualifier le h1 interne comme incohérence de plan, sans perdre les deux erreurs principales.
- À ne pas pénaliser : Plusieurs h1 si la hiérarchie reste cohérente au sens RGAA.

## 4. Charte de publication

- Point de contrôle rapide : Contraste
- Constat minimal attendu : Au moins un texte, lien, bouton ou statut présente un contraste insuffisant.
- Sévérité indicative : Bloquant
- Preuve possible : Mesure CCA/WebAIM/WAVE avec couleurs et ratio inférieur au seuil attendu.
- Correction : Ratio conforme : 4,5:1 pour texte normal ; 3:1 pour texte large et composants.
- Occurrences bonus : Texte gris clair. ; Bouton pâle. ; Statut transmis par couleur faible.
- À ne pas pénaliser : Usage d'une couleur DSFR conforme et information de statut aussi disponible en texte ou icône nommée.

## 5. Accès rapide aux contenus

- Point de contrôle rapide : Lien d'évitement
- Constat minimal attendu : Le lien d'évitement vers le contenu principal est absent, invisible au focus ou non fonctionnel.
- Sévérité indicative : Bloquant
- Preuve possible : Test clavier au premier Tab, puis activation du lien et vérification de l'ancre cible.
- Correction : Utiliser le composant DSFR Liens d'évitement : bloc placé tout en haut de page, avant l'en-tête ; navigation aria-label Accès rapide ; liste de liens simples ; premier lien vers le contenu principal ; ancres valides.
- Occurrences bonus : Lien vers menu ou pied de page cassé. ; Cible mal orthographiée.
- À ne pas pénaliser : Composant DSFR masqué hors écran par défaut s'il apparaît bien au focus.

## 6. Parcours clavier

- Point de contrôle rapide : Focus clavier visible
- Constat minimal attendu : Le focus clavier n'est pas visible sur au moins un composant interactif.
- Sévérité indicative : Bloquant
- Preuve possible : Parcours Tab / Shift+Tab montrant le composant focusable sans indicateur visible.
- Correction : Focus visible DSFR conservé sur boutons, liens/cartes et accordéons ; ordre de tabulation logique ; aucun piège clavier ; comportement clavier des accordéons conforme à la fiche DSFR.
- Occurrences bonus : Bouton, carte cliquable ou accordéon touché par la même surcharge CSS.
- À ne pas pénaliser : Variation visuelle DSFR du focus si elle reste perceptible et conforme.

## 7. Atelier international

- Point de contrôle rapide : Langue de la page
- Constat minimal attendu : La langue principale ou un changement de langue utile n'est pas déclaré correctement.
- Sévérité indicative : Gênant
- Preuve possible : Extrait HTML montrant lang absent/vide/invalide ou passage anglais non balisé.
- Correction : lang fr sur la page ; code langue valide ; passages anglais avec lang en si nécessaire ; pas de sur-balisage des noms propres ou mots entrés dans l'usage courant.
- Occurrences bonus : Code langue erroné. ; Expression anglaise non balisée. ; Mauvaise régionalisation.
- À ne pas pénaliser : Noms propres et mots étrangers passés dans l'usage courant non balisés.

## 8. Ressources à zoomer

- Point de contrôle rapide : Zoom 200 %
- Constat minimal attendu : À 200 % de zoom, une carte perd du contenu ou devient difficilement utilisable.
- Sévérité indicative : Gênant
- Preuve possible : Capture à 200 % montrant texte tronqué, bouton sorti, superposition ou défilement horizontal non nécessaire.
- Correction : Cartes DSFR fluides ; grille responsive ; contenu visible ; reflow sans perte ; composants utilisables.
- Occurrences bonus : Plusieurs cartes cassées. ; Hauteur fixe. ; overflow hidden.
- À ne pas pénaliser : Reflow vertical normal et augmentation de hauteur des cartes.

## 9. Vidéo de sensibilisation

- Point de contrôle rapide : Sous-titres
- Constat minimal attendu : La vidéo ne propose pas de sous-titres exploitables pour le contenu oral.
- Sévérité indicative : Bloquant
- Preuve possible : Vérification du lecteur : absence de piste, bouton sous-titres absent, ou sous-titres automatiques non relus signalés.
- Correction : Sous-titres synchronisés, relus, ponctués, avec sons utiles.
- Occurrences bonus : Sous-titres non synchronisés. ; Sons utiles non indiqués.
- À ne pas pénaliser : Vidéo strictement décorative sans information orale utile, si elle est correctement ignorée ou décrite ailleurs.

## 10. Podcast RGAA

- Point de contrôle rapide : Transcriptions
- Constat minimal attendu : Le contenu audio n'a pas de transcription accessible à proximité.
- Sévérité indicative : Bloquant
- Preuve possible : Revue de la page montrant absence de lien de transcription proche du média.
- Correction : Lien proche du média vers une transcription structurée et complète.
- Occurrences bonus : Transcription incomplète. ; Lien peu explicite. ; Transcription non structurée.
- À ne pas pénaliser : Résumé éditorial court en complément, s'il existe aussi une transcription complète.

## 11. Démonstration vidéo

- Point de contrôle rapide : Audiodescription
- Constat minimal attendu : Une information visuelle essentielle n'est pas disponible autrement que par l'image.
- Sévérité indicative : Bloquant
- Preuve possible : Revue humaine de la vidéo montrant une action ou information visuelle non décrite dans l'audio ni dans une version alternative.
- Correction : Description intégrée, piste audiodécrite ou version alternative selon faisabilité.
- Occurrences bonus : Absence de version audiodécrite. ; Description trop vague. ; Lien vers version décrite absent.
- À ne pas pénaliser : Vidéo où toutes les informations visuelles essentielles sont déjà dites dans l'audio.

## 12. Inscription à un webinaire

- Point de contrôle rapide : Étiquettes de formulaire
- Constat minimal attendu : Au moins un champ ou groupe de champs n'a pas de nom accessible fiable.
- Sévérité indicative : Bloquant
- Preuve possible : ANDI/WAVE, clic label ou extrait HTML montrant placeholder seul, label non associé ou groupe DSFR visuel sans fieldset/legend natifs.
- Correction : Étiquette visible et persistante ; association label for/id ; placeholder utilisé seulement comme exemple ; nom accessible qui reprend le nom visible ; aide à la saisie reliée avec aria-describedby ; groupes DSFR structurés avec fieldset.fr-fieldset, legend.fr-fieldset__legend, fr-fieldset__element et fr-messages-group.
- Occurrences bonus : Nom visible différent du nom accessible. ; Aide non reliée. ; Label masqué avec display none.
- À ne pas pénaliser : Placeholder utilisé comme exemple si une étiquette visible et associée existe.

## 13. Demande d'audit

- Point de contrôle rapide : Champs obligatoires
- Constat minimal attendu : L'obligation ou l'erreur de saisie n'est pas annoncée et reliée de manière exploitable.
- Sévérité indicative : Bloquant
- Preuve possible : Soumission du formulaire et inspection HTML montrant obligation non balisée, message vague/non relié ou focus non accompagné.
- Correction : Mention textuelle obligatoire ou règle claire sur les champs optionnels ; required ou aria-required ; astérisque expliqué si utilisé ; message d'erreur précis avec exemple ou format attendu ; erreur associée au champ ; aria-invalid true si pertinent ; focus placé sur le récapitulatif d'erreurs ou le premier champ en erreur.
- Occurrences bonus : Absence de required/aria-required. ; Erreur sans aria-describedby. ; aria-invalid absent si pertinent.
- À ne pas pénaliser : Astérisque utilisé s'il est expliqué et complété par une information technique et textuelle.
