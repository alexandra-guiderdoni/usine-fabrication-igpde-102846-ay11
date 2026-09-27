# PDF accessibles : pourquoi sont-ils encore si rares ?

## Constat initial

On rencontre rarement un document PDF réellement accessible.

Cela soulève une question inconfortable : les PDF accessibles sont-ils encore si rares parce qu’ils sont presque impossibles à créer ?

Par « PDF accessible », on parle d’un document qui est réellement :

- structuré ;
- correctement balisé ;
- navigable par titres ;
- lisible dans le bon ordre ;
- utilisable au clavier ;
- idéalement accompagné d’une alternative HTML accessible lorsque le contenu est important.

## Problèmes les plus fréquents

La plupart des PDF qu'on évalue présentent les mêmes problèmes :

- des titres qui ne sont que visuels ;
- des balises cassées ou manquantes ;
- un ordre de lecture incorrect ;
- des images sans texte alternatif ;
- des tableaux inaccessibles ;
- des champs de formulaire sans libellé ;
- une langue ou un titre de document manquant ;
- aucune version alternative accessible.

## Pourquoi cela arrive-t-il encore ?

### 1. L’accessibilité des PDF commence généralement trop tard

L’une des plus grandes idées reçues consiste à penser que l’accessibilité peut être « corrigée dans Acrobat à la fin ».

Les recommandations d’Adobe sont pourtant très claires : le meilleur endroit pour rendre un PDF accessible est d’abord le document source - Word, PowerPoint, InDesign, Google Docs - en utilisant de vrais titres, listes, tableaux, textes alternatifs et structures correctes avant l’export.

### 2. La remédiation des PDF est réellement difficile

Une publication Adobe Research de 2025 a montré que la remédiation des formulaires PDF est souvent peu intuitive, répétitive et écrasante, à cause de la densité d’information et de la complexité des formulaires PDF.

Dans cette étude, un outil prototype a aidé les personnes à remédier les formulaires 2,8 fois plus vite qu’avec Acrobat, tout en produisant des résultats plus précis.

### 3. Les PDF sont souvent utilisés là où HTML serait un meilleur choix

Un PDF est un format de destination. Ce n’est pas un très bon format pour du contenu fréquemment mis à jour, orienté service ou destiné au public sur le web.

Si un document contient des consignes, des informations réglementaires, des formulaires ou du contenu que les personnes doivent lire sur mobile ou avec des technologies d’assistance, HTML est souvent le choix le plus accessible dès le départ.

## Autres faits à retenir

- Adobe indique que plus de 90 % des PDF sont aujourd’hui au moins partiellement inaccessibles.
- Un PDF scanné n’est pas seulement « moins pratique » : s’il s’agit essentiellement d’une image de texte sans OCR ni structure, il peut être fondamentalement inutilisable pour de nombreuses personnes utilisant un lecteur d’écran.
- L’ordre de lecture est l’une des défaillances cachées les plus fréquentes.
- Un PDF peut sembler parfait visuellement et être malgré tout lu dans le mauvais ordre par les technologies d’assistance.

## Checklist pratique pour créer un PDF plus accessible

- Se demander d’abord : ce contenu doit-il vraiment être un PDF, ou HTML servirait-il mieux les utilisateurs ?
- Commencer dans le fichier source, pas dans Acrobat.
- Utiliser de vrais styles de titres, pas seulement du texte en gras.
- Ajouter un texte alternatif aux images porteuses d’information.
- Garder les tableaux simples et marquer correctement les lignes d’en-tête.
- Définir la langue et le titre du document.
- Exporter en PDF balisé.
- Dans Acrobat Pro, vérifier les balises, l’ordre de lecture, les liens et les champs de formulaire.
- Lancer un vérificateur d’accessibilité, mais ne pas s’arrêter là.
- Tester la navigation dans le PDF par titres, au clavier et avec un lecteur d’écran.

## Source

Article : FormA11y - A tool for remediating PDF forms for accessibility
- Auteurs : Sparsh Paliwal, Joshua Hoeflich, J. Bern Jordan, Rajiv
- Jain, Vlad I. Morariu, Alexa Siu, Jonathan Lazar
- Revue : ACM Transactions on Computer-Human Interaction
- DOI : https://doi.org/10.1145/3702317
- Page Adobe Research : https://research.adobe.com/publication/forma11y-research-and-development-of-a-tool-for-remediating-pdf-forms-for-accessibility/

---

# Skill generer-images-slides-ia

Prompt historique (juin 2026) pour le skill `generer-images-slides-ia` de l'espace de travail d'Alex, hors de ce dépôt.

## Objectif :
générer une série courte de 6 slides image-based PNG 16:9 à partir de ce fichier (`notes/pdf-accessibles-constat-et-checklist.md`).

Dossier de sortie utilisé à l'époque : `outputs/ia-slides/2026-06-22-pdf-accessibles/`, dans l'ancien dossier du projet (non versionné).

## Contraintes :
- utiliser `image_gen`, pas PIL, SVG, HTML, canvas ni PowerPoint éditable ;
- créer d’abord `slide-01.png`, l’inspecter, puis seulement continuer ;
- copier chaque image finale dans le dossier projet sous `slide-01.png` à `slide-06.png` ;
- créer `contact-sheet.png` après les 6 slides ;
- ne pas créer de PPTX sauf demande explicite ;
- garder un reçu de génération par slide ;
- style institutionnel français sobre : fond clair, bleu institutionnel, gris froids, rouge
seulement pour alerte, icônes filaires, personnages plats sobres si utiles ;
- aucun faux logo, aucun emblème officiel, aucune photo, aucune 3D, aucun dégradé décoratif ;
- texte très court, lisible, en français avec accents ;
- ne pas présenter FormA11y comme un outil disponible : seulement comme preuve de recherche.

## Masque commun :
Titre court en haut gauche, repère discret `PDF accessibles` en haut droit, scène centrale large, 3
à 6 labels courts, callout bas discret si utile. Barre de progression 1/6 à 6/6 stable sur toutes les slides.

## Colonne vertébrale :
1. Un PDF peut être beau et inutilisable
Scène : un PDF visuellement propre à gauche ; à droite, un lecteur d’écran reçoit des blocs dans un
ordre brouillé.
Texte : titre `Un PDF peut être beau et inutilisable` ; labels `Apparence correcte`, `Ordre
brouillé`, `Lecture impossible`.

2. Les défauts sont souvent invisibles
Scène : vue radiographie du PDF avec calques révélés : titres visuels, balises cassées, image sans
alternative, champ sans libellé.
Texte : titre `Les défauts sont souvent invisibles` ; labels `Titres visuels`, `Balises cassées`,
`Sans alt`, `Champ sans libellé`.

3. L’accessibilité commence dans le fichier source
Scène : chaîne gauche-droite : document source structuré -> export PDF balisé -> Acrobat en contrôle
final.
Texte : titre `Commencer dans le fichier source` ; labels `Titres`, `Listes`, `Tableaux`, `Alt
text`, `PDF balisé`, `Contrôle final`.

4. La remédiation est un travail de précision
Scène : formulaire PDF dense avec champs reliés à leurs libellés, zones à vérifier, loupe ou poste
de contrôle.
Texte : titre `La remédiation demande de la précision` ; labels `Libellés`, `Champs`, `Ordre`,
`Contrôle` ; callout `Étude FormA11y : 20 participants, 2,8 fois plus vite qu’Acrobat.`

5. Parfois, HTML sert mieux les utilisateurs
Scène : bifurcation de décision : contenu stable à archiver vers PDF ; contenu de service, mobile ou
mis à jour vers HTML.
Texte : titre `HTML est parfois le meilleur choix` ; labels `Archive stable`, `PDF`, `Service`,
`Mobile`, `Mise à jour`, `HTML`.

6. La bonne séquence : produire, exporter, tester
Scène : chaîne courte de validation : source structurée -> export balisé -> contrôle des tags ->
test clavier et lecteur d’écran.
Texte : titre `Produire, exporter, tester` ; labels `Source structurée`, `PDF balisé`, `Tags`,
`Clavier`, `Lecteur d’écran`.

## Après génération :
- créer la contact sheet avec le script du skill ;
- inspecter la contact sheet et au moins une slide pleine résolution ;
- signaler toute slide à régénérer si texte illisible, style incohérent, ratio incorrect ou scène
trop abstraite ;
- ne déclarer terminé qu’avec les chemins projet des PNG et la vérification réalisée.
