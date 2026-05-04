# Exercice « Ministère de l'Accessibilité numérique » - Spécification

Formation 102638 - Support de la section 3 « Les 13 points de contrôle rapides du W3C ».

Statut : cadrage fonctionnel et contrat d'évaluation prêts avant production.

---

## Contexte pédagogique

L'exercice consiste à faire remplir la grille d'audit des points de contrôle rapides à partir d'un faux site public DSFR : le **Ministère de l'Accessibilité numérique**.

Le site doit ressembler à un vrai site institutionnel, inspiré de l'univers éditorial RGAA et de `accessibilite.numerique.gouv.fr`, sans copier le site officiel. Il doit contenir des composants DSFR correctement stylés visuellement, mais volontairement mal implémentés dans la version inaccessible pour révéler les problèmes d'accessibilité numérique.

- **Public** : communicants, agents publics, profils métier, niveau initiation.
- **Format** : exercice en binôme, 30 minutes.
- **Modalité** : chaque binôme audite 3 pages rapides, puis restitution collective pour couvrir les 13 points de contrôle rapides.
- **Livrable stagiaire** : grille `grille-audit-easy-checks.xlsx` remplie avec verdict, sévérité, constat, correctif et preuve.
- **Niveau visé** : pré-diagnostic exploitable, pas audit RGAA complet.

Phrase-clé à retenir : **un défaut utilement remonté est un défaut prouvé, qualifié et corrigeable**.

Terminologie des verdicts à respecter strictement dans le corrigé et les exemples :

- `C` = Conforme ;
- `NC` = Non conforme ;
- `NA` = Non applicable.

Terminologie des sévérités à respecter strictement :

- `Bloquant` ;
- `Gênant` ;
- `Mineur` ;
- `Info`.

La sévérité est renseignée uniquement pour les constats `NC`.

---

## Principe d'exercice

L'exercice reprend la logique de l'exercice Sami :

1. Une version volontairement inaccessible.
2. Une version intermédiaire d'aide à la correction.
3. Une version accessible corrigée.
4. Un corrigé Markdown public après l'exercice.

Les trois versions doivent avoir le même contenu éditorial et la même structure générale pour permettre la comparaison.

### Versions attendues

| Version | Rôle | Aides visibles |
|---|---|---|
| `site-inaccessible/` | Site à auditer | Non |
| `site-aide-correction/` | Même site avec guidage pédagogique | Oui, en haut de page |
| `site-accessible/` | Site corrigé et conforme DSFR/accessibilité | Non |

### Version aide à la correction

La version intermédiaire contient, en haut de chaque page d'exercice, une zone **Aide à la correction** sous forme de groupe d'accordéons DSFR.

Le groupe d'accordéons doit fournir une aide progressive en trois niveaux :

1. **Indice** : signe observable ou outil utile pour détecter l'erreur.
2. **Ce qui pose problème** : défaut, impact utilisateur et lien avec le Point de contrôle rapide.
3. **Comment corriger** : méthode de correction, preuve attendue et référence à renseigner dans la grille.

### Version accessible

La version `site-accessible/` doit rester sobre, comme un vrai site ministériel corrigé. Elle ne doit pas afficher de comparaison avant/après, de commentaire pédagogique, de consigne d'audit ou de bloc de correction visible. Les explications pédagogiques restent dans `site-aide-correction/`, `manifest.md` et `corrige-easy-checks.md`.

Les accordéons doivent être implémentés selon la fiche officielle DSFR :

- Composant : https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/accordeon
- Code : https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/accordeon/code-de-l-accordeon
- Accessibilité : https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/accordeon/accessibilite-de-l-accordeon

---

## Contraintes DSFR et techniques

### DSFR non négociable

La version accessible doit respecter les composants DSFR et leurs exigences d'accessibilité. Aucun composant DSFR ne doit être implémenté sans consultation préalable de sa fiche officielle, notamment les onglets **Code** et **Accessibilité**.

Référence générale :

- Composants DSFR : https://www.systeme-de-design.gouv.fr/version-courante/fr/composants
- Liste projet des références **Code** et **Accessibilité** : `03-easy-checks/dsfr-component-links.md`
- Règles projet d'implémentation **Code** et **Accessibilité** : `03-easy-checks/dsfr-implementation-rules.md`

La version inaccessible peut contenir des composants visuellement proches du DSFR mais volontairement mal implémentés, uniquement pour créer une erreur pédagogique claire.

Des défauts visuels évidents sont acceptés lorsqu'ils servent directement l'apprentissage : contraste insuffisant, focus invisible, contenu tronqué au zoom, information portée uniquement par la couleur, etc. Ils doivent rester ciblés sur le Point de contrôle rapide concerné et ne pas transformer le site en caricature.

Les erreurs invisibles à l'oeil sont aussi autorisées et même souhaitables lorsque le Point de contrôle rapide l'exige : titre de page générique, langue absente ou erronée, label non associé, alternative absente dans le code, etc. L'exercice doit montrer que l'accessibilité ne se vérifie pas uniquement au rendu visuel.

### Skill DSFR à utiliser

La production doit s'appuyer sur le skill local `dsfr-components` pour cadrer les composants, les gabarits, les points de vigilance et la checklist de conformité :

- chemin fourni : `/Volumes/MacStudio/Claude/.claude/skills/dsfr-components/SKILL.md` ;
- miroir disponible dans cet environnement : `/Users/alex/Claude/.claude/skills/dsfr-components/SKILL.md`.

Le skill sert de guide de production, mais les règles propres à ce projet priment en cas de conflit :

- pas de CDN ;
- assets DSFR localisés dans le dépôt ;
- pages statiques compatibles GitHub Pages ;
- pas de Node, pas de bundler, pas de framework ;
- consultation obligatoire des fiches officielles DSFR, en particulier les onglets **Code** et **Accessibilité**.

Avant de produire ou modifier un composant, appliquer la méthode suivante :

1. identifier le composant DSFR concerné ;
2. consulter le skill `dsfr-components` pour le gabarit et les contraintes générales ;
3. consulter la fiche officielle DSFR du composant ;
4. appliquer les règles projet `03-easy-checks/dsfr-implementation-rules.md` ;
5. documenter dans `manifest.md` la fiche consultée, l'écart volontaire de la version inaccessible et la correction attendue ;
6. vérifier la version accessible au clavier, au zoom 200 %, avec les outils prévus et par revue HTML.

### Checklist qualité accessible

La version `site-accessible/` doit être validée avec deux sources obligatoires.

#### 1. RGAA

La validation doit couvrir au minimum :

- structure HTML et landmarks ;
- titres ;
- liens ;
- images ;
- tableaux si utilisés ;
- formulaires ;
- langue ;
- navigation clavier ;
- focus visible ;
- contrastes ;
- médias ;
- zoom 200 % et reflow ;
- erreurs de saisie ;
- absence d'information transmise uniquement par la couleur, la forme, la position ou le son.

#### 2. Fiches accessibilité DSFR

Pour chaque composant DSFR utilisé, il faut consulter et respecter :

1. la fiche composant ;
2. l'onglet **Code** ;
3. l'onglet **Accessibilité**.

Exemple obligatoire pour les accordéons d'aide :

- https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/accordeon/accessibilite-de-l-accordeon

Un composant ne doit pas être considéré comme conforme uniquement parce qu'il ressemble visuellement au DSFR. Sa structure HTML, ses attributs, son comportement clavier et son état restitué doivent aussi être conformes.

### Charte et identité

Le site doit utiliser une identité fictive :

- Nom de site : **Ministère de l'Accessibilité numérique**
- Baseline dans le header : **Formation IGPDE - Exercice points de contrôle rapides**
- Univers éditorial : RGAA, accessibilité numérique publique, démarches et ressources institutionnelles

Le header DSFR doit rester cohérent avec un site d'État :

- Marianne / République française.
- Nom du site.
- Baseline.
- Navigation claire vers les pages à auditer.

### Assets DSFR

Les assets DSFR doivent être localisés dans le dépôt. Aucun CDN ne doit être utilisé.

Exigences :

- CSS DSFR local.
- JavaScript DSFR local.
- Fonts, icônes, pictogrammes et assets nécessaires localisés si utilisés.
- Chemins relatifs compatibles GitHub Pages.
- Aucune dépendance externe au runtime.

### Architecture statique

Le site doit être simple, modulaire et maintenable.

Contraintes :

- Pas de Node.
- Pas de bundler.
- Pas de framework lourd.
- Génération statique par script Python simple.
- Sources modulaires : header, footer, contenu.
- Sortie publiable dans `docs/` pour GitHub Pages.

Architecture cible :

```text
exercice-easy-checks/
  README.md
  build.py
  validate.py
  manifest.md
  corrige-easy-checks.md
  ressources/
    grille-audit-easy-checks.xlsx
  assets/
    dsfr/
    shared/
      media/
        video-demo.mp4
        audio-demo.mp3
        sous-titres-demo.vtt
        transcription-demo.html
        audiodescription-demo.vtt
        video-demo-ad.mp4
  src/
    partials/
      header.html
      footer.html
      aide-correction.html
    pages/
      01-actualite-illustree.html
      ...
      13-demande-audit.html
  docs/
    index.html
    assets/
    ressources/
    site-inaccessible/
    site-aide-correction/
    site-accessible/
```

Commandes attendues :

```bash
python3 build.py
python3 validate.py
```

`build.py` génère le site statique dans `docs/`.

`validate.py` vérifie au minimum :

- absence de CDN ;
- présence des assets DSFR locaux ;
- liens internes ;
- présence d'un titre de page ;
- cohérence des trois versions ;
- présence de la grille et du corrigé ;
- présence des 13 pages dans chaque version.

Les validations automatiques restent légères. L'accessibilité de l'exercice doit être vérifiée par revue DSFR, WAVE, ANDI, clavier, outils navigateur et lecture humaine.

---

## Page racine GitHub Pages

La racine `docs/index.html` sert de page de lancement de l'exercice.

Elle contient :

1. Présentation courte de l'exercice.
2. Avertissement pédagogique : pré-diagnostic, pas audit RGAA.
3. Carte de téléchargement de la grille.
4. Liste ou cartes accessibles des 13 pages à auditer.
5. Liens accessibles vers les trois versions.
6. Section « Après l'exercice » avec lien vers le corrigé public.

La page racine doit permettre d'entrer directement dans les 13 pages de la version `site-inaccessible/`, car c'est le point de départ de l'exercice. Les accès à `site-aide-correction/` et `site-accessible/` restent disponibles, mais ils doivent être présentés comme ressources de comparaison après ou pendant la correction, pas comme parcours principal.

Chaque carte de page doit indiquer :

- numéro de page ;
- titre réaliste de la page ;
- Point de contrôle rapide ciblé, affiché clairement dès la page racine ;
- lot de binôme recommandé si utile ;
- lien explicite vers la page à auditer.

### Carte de téléchargement

Le composant « Téléchargement de fichier » DSFR est déprécié. Il ne doit pas être utilisé.

La grille doit être présentée via une **carte DSFR de téléchargement** :

- intitulé explicite : `Télécharger la grille d'audit des points de contrôle rapides` ;
- format visible : `XLSX` ;
- poids visible ;
- lien accessible ;
- pas de libellé générique du type « cliquez ici ».

Avant implémentation, consulter les références DSFR `Code` et `Accessibilité` du composant Carte, et vérifier que le lien de téléchargement reste explicite :

- `03-easy-checks/dsfr-component-links.md`

### Avertissement à afficher

Texte attendu :

> Cet exercice est un pré-diagnostic pédagogique. Il ne constitue pas un audit RGAA et ne permet pas de publier un taux de conformité.

---

## Déroulement en classe

Durée cible : 30 minutes.

Organisation :

| Temps | Activité |
|---|---|
| 3 min | Présentation de la page racine, de la grille et des outils |
| 15 min | Audit en binômes sur 3 pages attribuées |
| 7 min | Restitution collective des constats |
| 5 min | Comparaison rapide avec la version aide/corrigée et choix de 3 actions prioritaires |

Les binômes ne doivent pas auditer toutes les pages. Chaque binôme travaille sur un lot limité, puis la restitution collective permet de couvrir l'ensemble des 13 points de contrôle rapides.

Répartition par défaut :

| Binôme | Pages |
|---|---|
| A | 1 à 3 |
| B | 4 à 6 |
| C | 7 à 9 |
| D | 10 à 12 |
| E | 13 + vérification croisée / synthèse |

Si 6 binômes sont présents, le sixième binôme audite un lot déjà attribué pour comparer les constats.

Outils recommandés :

- navigateur récent ;
- clavier seul ;
- WAVE ;
- ANDI ;
- HeadingsMap ;
- Web Developer ;
- WebAIM Contrast Checker ou Colour Contrast Analyser ;
- DevTools ;
- NVDA ou VoiceOver en option.

Principe de détection :

- privilégier WAVE / ANDI lorsque c'est pertinent ;
- équilibrer outils automatiques et tests manuels ;
- rappeler qu'aucun outil automatique ne remplace un jugement humain.

---

## Cartographie des pages

Les pages visibles doivent porter des titres réalistes de ministère. La correspondance avec les points de contrôle rapides apparaît dans l'accueil, l'aide à la correction, le manifeste et la grille, mais pas forcément comme titre principal de la page.

Chaque page contient une seule erreur principale. La même erreur peut être reproduite à plusieurs endroits sur la page pour créer un constat réaliste.

Une seule occurrence correctement prouvée suffit pour invalider le critère ciblé sur la page. Les occurrences multiples servent à rendre le défaut plus réaliste et à augmenter les chances de détection, pas à exiger une collecte exhaustive.

La grille et le corrigé peuvent contenir plusieurs lignes pour une même page lorsque la même erreur principale est répétée à plusieurs endroits. Ces lignes doivent rester optionnelles ou illustratives sauf mention contraire. Le corrigé doit distinguer clairement :

- le constat minimal attendu ;
- les occurrences bonus possibles ;
- les faux-amis ou mauvaises pratiques à ne pas pénaliser.

Les pages d'exercice ne doivent pas afficher de bloc pédagogique visible du type « Objectif de l'audit » en haut de page. Elles doivent rester crédibles comme pages ministérielles. Les consignes pédagogiques sont réservées à la page racine et à la version `site-aide-correction/`.

Les contenus doivent rester courts et très ciblés. L'objectif est de permettre l'audit de 3 pages par binôme en 15 minutes, pas de reproduire toute la profondeur éditoriale d'un vrai site ministériel. Chaque page doit contenir uniquement ce qui est nécessaire pour rendre l'erreur détectable, réaliste et corrigeable.

### Contrat d'évaluation

Source unique désormais : `03-easy-checks/evaluation_contract.yml`.

Ce tableau fait foi pour la grille, le manifeste, le corrigé et les aides. Pour une page donnée, le binôme n'a pas à trouver toutes les occurrences : le **constat minimal attendu**, correctement prouvé, suffit à renseigner `NC`.

Le tableau ci-dessous est une vue lisible du contrat. En cas d'écart lors de la production, le fichier YAML doit être corrigé en premier, puis les livrables doivent être régénérés depuis lui.

| # | Page | Constat minimal attendu | Preuve minimale | Sévérité indicative | Occurrences bonus | À ne pas pénaliser |
|---|---|---|---|---|---|---|
| 1 | Actualité illustrée | Au moins une image n'a pas d'alternative adaptée à son rôle réel. | Capture WAVE/ANDI ou extrait HTML montrant `alt` absent, vide ou inadapté sur l'image concernée. | Gênant | Image décorative bavarde ; image-lien mal nommée ; lien composite dont l'icône ajoute du bruit au nom accessible. | Image purement décorative avec `alt=""`. |
| 2 | Résultats de recherche RGAA | Le titre de page ne permet pas d'identifier précisément la page ou son état. | Onglet navigateur ou extrait `<title>` montrant un titre générique, dupliqué ou mal ordonné. | Gênant | Pagination absente du titre ; requête de recherche absente ; nom du ministère placé avant l'information spécifique. | Titre long si l'information spécifique est présente en premier. |
| 3 | Guide du RGAA | Un texte qui est visuellement un titre n'est pas balisé comme titre, ou une balise de titre est utilisée pour un simple effet visuel. | HeadingsMap/WAVE ou extrait HTML montrant un faux titre ou un titre décoratif. | Gênant | Comparer le plan visuel et le plan technique ; repérer un titre non pertinent. | Saut de niveau ou plusieurs `h1` si la hiérarchie reste cohérente au sens RGAA. |
| 4 | Charte de publication | Au moins un texte, lien, bouton ou statut présente un contraste insuffisant. | Mesure CCA/WebAIM/WAVE avec couleurs et ratio inférieur au seuil attendu. | Bloquant | Texte gris clair ; bouton pâle ; statut transmis par couleur faible. | Usage d'une couleur DSFR conforme et information de statut aussi disponible en texte ou icône nommée. |
| 5 | Accès rapide aux contenus | Le lien d'évitement vers le contenu principal est absent, invisible au focus ou non fonctionnel. | Test clavier au premier `Tab`, puis activation du lien et vérification de l'ancre cible. | Bloquant | Lien vers menu ou pied de page cassé ; cible mal orthographiée. | Composant DSFR masqué hors écran par défaut s'il apparaît bien au focus. |
| 6 | Parcours clavier | Le focus clavier n'est pas visible sur au moins un composant interactif. | Parcours `Tab` / `Shift+Tab` montrant le composant focusable sans indicateur visible. | Bloquant | Bouton, carte cliquable ou accordéon touché par la même surcharge CSS. | Variation visuelle DSFR du focus si elle reste perceptible et conforme. |
| 7 | Atelier international | La langue principale ou un changement de langue utile n'est pas déclaré correctement. | Extrait HTML montrant `lang` absent/vide/invalide ou passage anglais non balisé. | Gênant | Code langue erroné ; expression anglaise non balisée ; mauvaise régionalisation. | Noms propres et mots étrangers passés dans l'usage courant non balisés. |
| 8 | Ressources à zoomer | À 200 % de zoom, une carte perd du contenu ou devient difficilement utilisable. | Capture à 200 % montrant texte tronqué, bouton sorti, superposition ou défilement horizontal non nécessaire. | Gênant | Plusieurs cartes cassées ; hauteur fixe ; `overflow: hidden`. | Reflow vertical normal et augmentation de hauteur des cartes. |
| 9 | Vidéo de sensibilisation | La vidéo ne propose pas de sous-titres exploitables pour le contenu oral. | Vérification du lecteur : absence de piste, bouton sous-titres absent, ou sous-titres automatiques non relus signalés. | Bloquant | Sous-titres non synchronisés ; sons utiles non indiqués. | Vidéo strictement décorative sans information orale utile, si elle est correctement ignorée ou décrite ailleurs. |
| 10 | Podcast RGAA | Le contenu audio n'a pas de transcription accessible à proximité. | Revue de la page montrant absence de lien de transcription proche du média. | Bloquant | Transcription incomplète ; lien peu explicite ; transcription non structurée. | Résumé éditorial court en complément, s'il existe aussi une transcription complète. |
| 11 | Démonstration vidéo | Une information visuelle essentielle n'est pas disponible autrement que par l'image. | Revue humaine de la vidéo montrant une action ou information visuelle non décrite dans l'audio ni dans une version alternative. | Bloquant | Absence de version audiodécrite ; description trop vague ; lien vers version décrite absent. | Vidéo où toutes les informations visuelles essentielles sont déjà dites dans l'audio. |
| 12 | Inscription à un webinaire | Au moins un champ ou groupe de champs n'a pas de nom accessible fiable. | ANDI/WAVE, clic label ou extrait HTML montrant placeholder seul, label non associé ou groupe sans `fieldset`/`legend`. | Bloquant | Nom visible différent du nom accessible ; aide non reliée ; label masqué avec `display:none`. | Placeholder utilisé comme exemple si une étiquette visible et associée existe. |
| 13 | Formulaire de contact | L'obligation ou l'erreur de saisie n'est pas annoncée et reliée de manière exploitable. | État initial puis soumission du formulaire vide + inspection HTML montrant obligation non balisée, message vague/non relié ou focus non accompagné. | Bloquant | Absence de `required`/`aria-required` ; erreur sans `aria-describedby` ; `aria-invalid` absent si pertinent. | Astérisque utilisé s'il est expliqué et complété par une information technique et textuelle. |

### Vue d'ensemble

| # | Page réaliste | Point de contrôle rapide ciblé | Détection principale |
|---|---|---|---|
| 1 | Actualité illustrée | Texte alternatif des images | WAVE / ANDI |
| 2 | Résultats de recherche RGAA | Titre de page | Navigateur / code source / WAVE |
| 3 | Guide du RGAA | Titres de rubriques | HeadingsMap / WAVE |
| 4 | Charte de publication | Contraste | CCA / WebAIM Contrast Checker / WAVE |
| 5 | Accès rapide aux contenus | Lien d'évitement | Clavier |
| 6 | Parcours clavier | Focus clavier visible | Clavier / ANDI |
| 7 | Atelier international | Langue de la page | Web Developer / code source / WAVE |
| 8 | Ressources à zoomer | Zoom 200 % | Navigateur |
| 9 | Vidéo de sensibilisation | Sous-titres | Lecteur vidéo |
| 10 | Podcast RGAA | Transcription | Revue humaine |
| 11 | Démonstration vidéo | Audiodescription | Revue humaine |
| 12 | Inscription à un webinaire | Étiquettes de formulaire | ANDI / WAVE / clavier |
| 13 | Formulaire de contact | Champs obligatoires | Formulaire / lecteur d'écran / clavier |

---

## Détail des 13 pages

### 1. Actualité illustrée

**Contexte éditorial** : annonce d'une nouvelle ressource RGAA illustrée par une image informative.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 1. Texte alternatif des images |
| Erreur inaccessible | Quatre cas complémentaires : image informative sans alternative ou avec `alt=""`, image décorative trop bavarde, image-lien courriel avec alternative visuelle, lien composite SMS dont l'icône décorative a une alternative redondante. |
| Occurrences | Les quatre occurrences sont acceptées car elles relèvent du même Point de contrôle rapide et permettent de distinguer contexte, fonction, décoration et lien composite. |
| Détection | WAVE, ANDI, inspection HTML. |
| Correction accessible | Image informative : alternative courte reprenant l'information. Image décorative : `alt=""`. Image-lien : alternative indiquant la cible ou l'action. Lien composite : si le texte visible indique déjà l'action, l'icône décorative doit avoir `alt=""`. |
| Aide accordéon | Divulgation progressive en trois niveaux : méthode d'identification des 4 cas, indices par type de cas, puis messages de correction ciblés. L'aide distingue explicitement le lien image courriel et le lien composite SMS. |

### 2. Résultats de recherche RGAA

**Contexte éditorial** : page de résultats de recherche pour des ressources RGAA.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 2. Titre de page |
| Erreur inaccessible | Trois cas complémentaires : titre générique, titre identique sur plusieurs pages de résultats, information spécifique placée trop tard après le nom long du ministère. |
| Occurrences | Les trois cas peuvent être illustrés dans la même page de résultats ou dans le corrigé. Ils relèvent du même Point de contrôle rapide : présence, unicité et pertinence du titre de page. |
| Détection | Onglet navigateur, code source, WAVE. |
| Correction accessible | Titre unique, spécifique et ordonné du particulier vers le général, par exemple `Recherche "RGAA" - Page 2 - Ministère de l'Accessibilité numérique`. |
| Aide accordéon | Problème : l'utilisateur ne sait pas quelle page ou quel état est ouvert. Impact : navigation difficile entre onglets, historique et pages de résultats. Méthode : rendre le titre unique, ajouter le contexte utile et placer l'information spécifique en premier. |

### 3. Guide du RGAA

**Contexte éditorial** : page explicative sur le RGAA et ses ressources.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 3. Titres de rubriques |
| Erreur inaccessible | Deux vraies erreurs et un faux-ami pédagogique : titre visuel non balisé, balise de titre détournée pour un effet visuel, puis saut de niveau ou plusieurs `h1` à analyser comme bonne pratique / faux-ami selon la cohérence réelle de la hiérarchie. |
| Occurrences | Les trois cas sont présentés sur la page, mais le corrigé doit distinguer clairement les non-conformités des mauvaises pratiques tolérées par le RGAA. |
| Détection | HeadingsMap, WAVE, DevTools. |
| Correction accessible | Titre visuel balisé avec un élément de titre natif ou `role="heading"` / `aria-level` si nécessaire ; balise de titre réservée aux vrais titres ; hiérarchie globalement pertinente. Une hiérarchie stricte sans saut et un seul `h1` restent recommandés, mais ne doivent pas être présentés comme des exigences RGAA absolues. |
| Aide accordéon | Problème : le plan technique peut être absent, pollué ou mal interprété. Impact : navigation par titres inefficace ou débat d'audit mal qualifié. Méthode : identifier ce qui constitue réellement un titre, vérifier sa sémantique, repérer les titres décoratifs, puis qualifier les sauts de niveau avec nuance. |

### 4. Charte de publication

**Contexte éditorial** : page décrivant les règles de publication des contenus accessibles.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 4. Contraste |
| Erreur inaccessible | Trois occurrences de contraste insuffisant : texte courant gris clair sur blanc, lien ou bouton d'action trop pâle, information de statut transmise par une couleur faible. |
| Occurrences | Les trois occurrences sont acceptées car elles relèvent du même Point de contrôle rapide. |
| Détection | WebAIM Contrast Checker, Colour Contrast Analyser, WAVE. |
| Correction accessible | Ratio conforme : 4,5:1 pour texte normal ; 3:1 pour texte large et composants. |
| Aide accordéon | Problème : lecture ou identification difficile. Impact : malvoyance, luminosité forte, écran médiocre, perception des statuts. Méthode : mesurer, ne pas juger à l'oeil, et ne pas transmettre une information uniquement par une couleur peu contrastée. |

### 5. Accès rapide aux contenus

**Contexte éditorial** : page longue avec menu, recherche et contenu principal.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 5. Lien d'évitement |
| Erreur inaccessible | Trois cas complémentaires : lien d'évitement absent, lien présent mais invisible au focus, lien présent mais cible d'ancre invalide ou inexistante. |
| Occurrences | Les trois cas sont acceptés car ils relèvent du même Point de contrôle rapide : présence, visibilité au focus et fonctionnement réel du lien. |
| Détection | Clavier, premier appui sur `Tab`, activation du lien, vérification du déplacement vers le contenu principal. |
| Correction accessible | Utiliser le composant DSFR **Liens d'évitement** : bloc placé tout en haut de page, avant l'en-tête ; navigation `aria-label="Accès rapide"` ; liste de liens simples ; premier lien vers le contenu principal ; ancres valides. |
| Aide accordéon | Problème : l'utilisateur clavier traverse toute la navigation ou croit avoir évité le menu sans y parvenir. Impact : perte de temps, fatigue, désorientation. Méthode : implémenter le composant DSFR Liens d'évitement sans personnalisation abusive, vérifier qu'il apparaît au focus et tester que chaque cible existe et fonctionne. |

Références DSFR obligatoires pour cette page :

- Code : https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/liens-d-evitement/code-des-liens-d-evitement
- Accessibilité : https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/liens-d-evitement/accessibilite-des-liens-d-evitement

### 6. Parcours clavier

**Contexte éditorial** : page avec cartes de ressources, boutons d'action et accordéons d'information.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 6. Focus clavier visible |
| Erreur inaccessible | Focus visible supprimé ou très peu perceptible sur trois types d'éléments : boutons, cartes cliquables et accordéons DSFR mal surchargés. |
| Occurrences | Les trois occurrences sont acceptées car elles relèvent du même Point de contrôle rapide. |
| Détection | Clavier, `Tab`, `Shift+Tab`, ANDI en complément. |
| Correction accessible | Focus visible DSFR conservé sur boutons, liens/cartes et accordéons ; ordre de tabulation logique ; aucun piège clavier ; comportement clavier des accordéons conforme à la fiche DSFR. |
| Aide accordéon | Problème : on ne sait plus où l'on est. Impact : navigation impossible au clavier. Méthode : retirer les overrides qui masquent le focus, utiliser les styles DSFR et vérifier chaque composant interactif au clavier. |

### 7. Atelier international

**Contexte éditorial** : annonce d'un atelier avec un passage en anglais.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 7. Langue de la page |
| Erreur inaccessible | Trois cas complémentaires : attribut `lang` absent ou vide sur `<html>`, code langue invalide ou erroné, passage en anglais non balisé dans une page française. |
| Occurrences | Les trois occurrences sont acceptées car elles relèvent du même Point de contrôle rapide et couvrent déclaration principale, validité du code et changement de langue. |
| Détection | Web Developer, code source, WAVE. |
| Correction accessible | `lang="fr"` sur la page ; code langue valide (`fr`, `en`, `es`, etc.) ; passages anglais avec `lang="en"` si nécessaire. Les noms propres et mots étrangers passés dans l'usage courant ne doivent pas être sur-balisés. |
| Aide accordéon | Problème : la synthèse vocale ne sait pas quelle prononciation appliquer. Impact : compréhension dégradée, fatigue, mots étrangers mal prononcés. Méthode : déclarer la langue principale, utiliser un code valide et baliser seulement les vrais changements de langue utiles. |

### 8. Ressources à zoomer

**Contexte éditorial** : page de ressources avec grille de cartes RGAA.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 8. Zoom 200 % |
| Erreur inaccessible | Cartes de ressources avec hauteur fixe, largeur rigide ou `overflow` masqué provoquant texte tronqué, boutons sortis ou superposition au zoom 200 %. |
| Occurrences | Plusieurs cartes peuvent reproduire la même erreur. |
| Détection | Zoom navigateur à 200 %, fenêtre étroite. |
| Correction accessible | Cartes DSFR fluides ; grille responsive ; contenu visible ; reflow sans perte ; composants utilisables. |
| Aide accordéon | Problème : les cartes cassent au zoom. Impact : malvoyance et petits écrans. Méthode : retirer les hauteurs/largeurs fixes, éviter `overflow: hidden`, utiliser la grille DSFR et tester à 200 %. |

### 9. Vidéo de sensibilisation

**Contexte éditorial** : courte vidéo de sensibilisation à l'accessibilité numérique.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 9. Sous-titres |
| Erreur inaccessible | Vidéo sans sous-titres, ou sous-titres automatiques non relus. |
| Assets | `video-demo.mp4`, `sous-titres-demo.vtt` à remplacer par les vrais médias fournis ultérieurement. |
| Détection | Lecteur vidéo, bouton sous-titres, écoute sans son. |
| Correction accessible | Sous-titres synchronisés, relus, ponctués, avec sons utiles. |
| Aide accordéon | Problème : contenu oral indisponible sans son. Impact : personnes sourdes/malentendantes et usages sans audio. Méthode : fournir un fichier VTT relu. |

### 10. Podcast RGAA

**Contexte éditorial** : extrait audio présentant une démarche RGAA.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 10. Transcriptions |
| Erreur inaccessible | Audio sans lien visible vers une transcription. |
| Assets | `audio-demo.mp3`, `transcription-demo.html` à remplacer par les vrais médias fournis ultérieurement. |
| Détection | Revue humaine de la page. |
| Correction accessible | Lien proche du média vers une transcription structurée et complète. |
| Aide accordéon | Problème : contenu audio non disponible en texte. Impact : personnes sourdes, sourdaveugles, recherche/citation impossible. Méthode : ajouter une transcription accessible. |

### 11. Démonstration vidéo

**Contexte éditorial** : vidéo montrant une interface avant/après ou un geste de correction.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 11. Audiodescription |
| Erreur inaccessible | Information visuelle essentielle non décrite dans l'audio principal et absence de piste ou version audiodécrite. |
| Assets | Sources proposées : `Valentin Haüy - CAPTCHA : le retour au Moyen Âge` (`https://www.youtube.com/watch?v=nSZ0xeXapds`) comme version avec transcription, et `CAPTCHA : le retour au Moyen Âge (vidéo audiodécrite)` (`https://www.youtube.com/watch?v=trfLb7xlXjQ`) comme version audiodécrite. Ne pas télécharger ni réhéberger sans vérification des droits ; utiliser ces liens comme références pédagogiques ou remplacer par fichiers locaux autorisés. |
| Détection | Revue humaine de la vidéo. |
| Correction accessible | Description intégrée, piste audiodécrite ou version alternative selon faisabilité. |
| Aide accordéon | Problème : l'image porte une information non disponible autrement. Impact : personnes aveugles ou malvoyantes. Méthode : décrire les informations visuelles essentielles. |

### 12. Inscription à un webinaire

**Contexte éditorial** : formulaire d'inscription à un webinaire RGAA.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 12. Étiquettes de formulaire |
| Erreur inaccessible | Trois occurrences principales : placeholder utilisé comme seule étiquette, étiquette visible non associée au champ, groupe de boutons radio ou cases à cocher sans `fieldset`/`legend`. |
| Occurrences | Les trois occurrences sont acceptées car elles relèvent du même Point de contrôle rapide. Elles peuvent être complétées dans le corrigé par des exemples pédagogiques : étiquette orpheline, nom visible différent du nom accessible, aide à la saisie mal reliée, étiquette masquée avec `display:none`. |
| Détection | ANDI, WAVE, clic sur le label, test au clavier, DevTools Accessibility Tree, lecteur d'écran si disponible. |
| Correction accessible | Étiquette visible et persistante ; association `label for` / `id` ; placeholder utilisé seulement comme exemple ; nom accessible qui reprend le nom visible ; aide à la saisie reliée avec `aria-describedby` ; groupes structurés avec `fieldset` et `legend`. |
| Aide accordéon | Problème : le champ ou le groupe n'a pas de nom fiable. Impact : lecteur d'écran muet, commande vocale fragile, mémoire sollicitée, contexte perdu sur les radios/checkboxes. Méthode : relier chaque étiquette au champ, ne pas remplacer le label par un placeholder, structurer les groupes et vérifier le nom accessible. |

### 13. Formulaire de contact

**Contexte éditorial** : formulaire de contact pour poser une question sur l'accessibilité numérique ou signaler une difficulté.

| Élément | Spécification |
|---|---|
| Point de contrôle rapide | 13. Champs obligatoires |
| Scénario | Parcours en deux temps : état initial sans erreur affichée, puis soumission du formulaire vide pour vérifier l'aide à la correction. |
| Erreur inaccessible | Avant soumission : les champs nom, courriel et message sont signalés par astérisque non expliqué, sans `required` ni `aria-required`. Après soumission : message trop vague, message non associé au champ et focus non ramené vers le récapitulatif ou le premier champ en erreur. |
| Occurrences | Plusieurs champs requis peuvent reproduire l'erreur. Les défauts de prévention et de correction sont acceptés car ils décrivent le même parcours de formulaire. |
| Détection | Soumission du formulaire, clavier, lecteur d'écran, inspection HTML, vérification de `aria-describedby`, `aria-invalid`, `required` et du déplacement de focus. |
| Correction accessible | Mention textuelle `obligatoire` ou règle claire sur les champs optionnels ; `required` ou `aria-required` ; astérisque expliqué si utilisé ; message d'erreur précis avec exemple ou format attendu ; erreur associée au champ ; `aria-invalid="true"` si pertinent ; focus placé sur le récapitulatif d'erreurs ou le premier champ en erreur. |
| Aide accordéon | Problème : obligation non annoncée ou correction non accompagnée. Impact : erreurs de saisie, perte de contexte, navigation clavier laborieuse, abandon. Méthode : prévenir avant soumission, expliquer après soumission, relier techniquement les erreurs et guider le focus. |

---

## Cartographie des composants DSFR

Cette cartographie est une première proposition. Avant implémentation, chaque composant doit être vérifié dans la documentation officielle DSFR, y compris son onglet **Accessibilité**.

### Composants transverses

| Zone | Composants DSFR pressentis | Points de vigilance |
|---|---|---|
| Header | En-tête, navigation principale, liens d'accès rapide si pertinents | Structure, intitulé du site, navigation clavier, responsive |
| Haut de page | Liens d'évitement | Composant DSFR obligatoire sur les pages : placé avant l'en-tête, visible au focus, `aria-label="Accès rapide"`, cible de contenu valide |
| Footer | Pied de page | Liens explicites, hiérarchie, absence de doublons inutiles |
| Page racine | Carte, lien, alerte ou mise en avant | Carte de téléchargement non dépréciée, format et poids du fichier indiqués |
| Aide à la correction | Accordéon | Respect strict de l'onglet accessibilité DSFR |
| Toutes pages | Fil d'Ariane si utilisé | Position, intitulés, page courante correctement indiquée |

### Pages d'exercice

| # | Page | Composants DSFR pressentis | Erreur inaccessible simulée | Vigilance version accessible |
|---|---|---|---|---|
| 1 | Actualité illustrée | Carte, image, lien image, lien composite | Image informative muette, image décorative bavarde, image-lien mal nommée, icône décorative bavarde dans un lien composite | Alternative selon le rôle : informative, décorative, fonctionnelle ou silencieuse dans un lien composite redondant |
| 2 | Résultats de recherche RGAA | Barre de recherche, liste de résultats, liens | Titre générique, titre dupliqué, information spécifique trop tardive | `<title>` unique, contexte utile, information spécifique en premier |
| 3 | Guide du RGAA | Sommaire, sections de contenu, éventuellement accordéon | Faux titre, titre décoratif, faux-ami sur saut de niveau ou plusieurs `h1` | Titres sémantiques, titres pertinents, hiérarchie qualifiée avec nuance RGAA |
| 4 | Charte de publication | Mise en avant, alerte, liens | Contraste insuffisant | Couleurs DSFR ou ratios vérifiés |
| 5 | Accès rapide aux contenus | En-tête, navigation, lien d'évitement, contenu long | Premier focus ne mène pas au contenu | Lien d'évitement visible au focus et cible valide |
| 6 | Parcours clavier | Cartes, boutons, accordéons | Focus masqué par CSS sur plusieurs composants interactifs | Focus DSFR visible, ordre logique, accordéons conformes |
| 7 | Atelier international | Carte événement, contenu bilingue | `lang` absent/vide, code langue invalide, passage anglais non balisé | Langue principale valide, changements de langue utiles, pas de sur-balisage |
| 8 | Ressources à zoomer | Cartes, tableau simple si nécessaire | Bloc fixe cassant à 200 % | Layout fluide, reflow sans perte |
| 9 | Vidéo de sensibilisation | Lecteur vidéo HTML, lien ou bouton associé | Sous-titres absents/non relus | Piste VTT correcte, contrôles accessibles |
| 10 | Podcast RGAA | Lecteur audio HTML, lien de transcription | Transcription absente | Lien proche vers transcription structurée |
| 11 | Démonstration vidéo | Lecteur vidéo HTML, lien vers version décrite | Information visuelle non décrite | Audio principal, piste ou version décrite |
| 12 | Inscription à un webinaire | Champ de saisie, cases à cocher, boutons radio, bouton | Placeholder seul, label non associé, groupe sans `fieldset`/`legend` | Labels visibles, `for/id`, `aria-describedby` si aide, `fieldset/legend` si groupe |
| 13 | Formulaire de contact | Formulaire, message d'erreur, alerte | Obligatoire mal annoncé, erreurs vagues/non reliées, focus non accompagné | Texte obligatoire, attributs requis, erreurs explicites reliées, focus guidé |

### Règle de production

Chaque page doit indiquer dans `manifest.md` :

- les composants DSFR utilisés ;
- les fiches DSFR consultées ;
- l'erreur volontairement introduite ;
- le comportement attendu dans la version accessible ;
- le ou les tests de validation.

---

## Manifeste et corrigé

### `manifest.md`

Le manifeste documente toutes les erreurs injectées.

Format attendu :

| Page | Point de contrôle rapide | Erreur injectée | Outil de détection | Correction attendue | Aide associée |
|---|---|---|---|---|---|

Le manifeste est public dans le dépôt GitHub Pages, mais il doit être présenté comme ressource « après l'exercice » pour ne pas donner les réponses trop tôt.

### `corrige-easy-checks.md`

Le corrigé est public à terme dans le dépôt GitHub Pages, dans une section **Après l'exercice**.

Contenu attendu :

- page ;
- erreur ;
- constat attendu ;
- sévérité indicative ;
- preuve possible ;
- correction ;
- référence à la grille ;
- extrait HTML avant/après si utile.

La version accessible du site ne doit pas contenir le corrigé dans ses pages : elle doit rester un vrai site corrigé, pas un support de correction.

---

## Médias et assets à fournir

Les vrais fichiers vidéo et audio seront fournis ultérieurement, sauf pour la page 11 où deux sources YouTube de référence sont déjà proposées.

Sources page 11 :

- Version avec transcription : https://www.youtube.com/watch?v=nSZ0xeXapds
- Version audiodécrite : https://www.youtube.com/watch?v=trfLb7xlXjQ

Ces liens ne doivent pas être téléchargés ni réhébergés sans vérification des droits. Ils peuvent être utilisés comme références pédagogiques ou remplacés par des fichiers locaux autorisés.

En attendant, prévoir des placeholders légers :

```text
assets/shared/media/
  video-demo.mp4
  audio-demo.mp3
  sous-titres-demo.vtt
  transcription-demo.html
  audiodescription-demo.vtt
  video-demo-ad.mp4
```

Les pages média doivent être conçues pour permettre le remplacement des assets sans modifier la structure HTML.

---

## Critères d'acceptation

### Pédagogie

- Les 13 points de contrôle rapides sont représentés par 13 pages distinctes.
- Une page correspond à une erreur principale.
- Le site inaccessible reste réaliste, pas caricatural.
- La version aide à la correction expose l'aide immédiatement après le titre de page, avant le composant fautif.
- La mission permet de remplir la grille en 30 minutes en binômes.

### Accessibilité

- La version accessible est conforme aux composants DSFR utilisés.
- Chaque composant utilisé est vérifié contre l'onglet **Accessibilité** de sa fiche DSFR.
- Chaque page est vérifiée contre les critères RGAA pertinents.
- Les pages accessibles ont un titre unique, une langue valide, une structure de titres cohérente, un focus visible, des liens explicites et des formulaires correctement étiquetés.
- Les pages accessibles fonctionnent au clavier.
- Les pages accessibles restent utilisables à 200 % de zoom.
- Aucun CDN n'est appelé.

### Technique

- `python3 build.py` génère `docs/` depuis `03-easy-checks/evaluation_contract.yml`.
- `python3 validate.py` passe sans erreur bloquante.
- Les trois versions sont disponibles depuis la page racine.
- La grille est téléchargeable depuis une carte DSFR.
- Le corrigé et le manifeste sont publics mais placés dans la section « Après l'exercice ».
- Le site fonctionne sur GitHub Pages.

---

## Points ouverts

1. Fournir les vrais fichiers vidéo et audio.
2. Choisir les textes définitifs de chaque page ministérielle.
3. Déterminer le poids final de la grille si le fichier XLSX change avant publication.
4. Définir si une version imprimable du corrigé est souhaitée.
5. Définir si la page racine doit proposer une répartition automatique des binômes.

---

## Règles pédagogiques appliquées

- R1 - Engagement immédiat : faux site réaliste à auditer, pas simple lecture.
- R5 - Chunking : une page = une erreur principale.
- R8 - Analogie : pré-diagnostic comme thermomètre, pas audit complet.
- R11 - Prédiction : les stagiaires cherchent avant d'ouvrir l'aide.
- R12 - Récupération active : remplissage de la grille depuis les observations.
- R16 - Visuel : comparaison des trois versions.
- R18 - Sécurité : version aide à la correction pour débloquer sans corriger à la place.
- R24 - Action : produire 3 actions prioritaires.
- R25 - Métacognition : restitution collective sur les checks les plus difficiles.

Score pédagogique visé : **actif**.
