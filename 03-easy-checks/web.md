# Partie 3 - Web et points de contrôle rapides

Source : `support-formation-102846-2026-IGPDE.pptx`.

Périmètre : diapositives 84 à 114 du deck, correspondant à la partie 3 sur les points de contrôle rapides W3C pour le web.

## Diapositive 84 - 3. Les 13 points de contrôle rapides du W3C

84
9 octobre 2026
Formation 102846 / points de contrôle rapides

## Diapositive 85 - WebAIM Million 2026 : le constat

3. points de contrôle rapides | WebAIM Million 2026
85
95,9 %
des pages d’accueil ont au moins une erreur WCAG détectée
56,1
erreurs détectées en moyenne par page d’accueil
1 437
éléments par page en moyenne : la complexité augmente
Comment lire ces chiffres
• WebAIM analyse automatiquement les pages d’accueil : c’est un thermomètre, pas un audit RGAA complet.
• L’absence d’erreur détectée ne prouve pas qu’une page est accessible.
• Mais la présence d’erreurs détectées révèle des barrières très probables pour les utilisateurs.
9 octobre 2026
Formation 102846 / points de contrôle rapides - WebAIM

## Diapositive 86 - Six erreurs qui justifient les points de contrôle rapides

3. points de contrôle rapides | WebAIM Million 2026
86
Erreur fréquente
Pages concernées
Point d’entrée
Texte à faible contraste
83,9 %
Contraste
Texte alternatif d’image manquant
53,1 %
Images
Étiquette de formulaire manquante
51 %
Formulaires
Liens vides
46,3 %
Images / clavier (partiel)
Boutons vides
30,6 %
Clavier / formulaires (partiel)
Langue du document absente
13,5 %
Langue
À retenir
• Ces six familles représentent 96 % des erreurs détectées par WebAIM.
• Les points de contrôle rapides donnent une méthode courte pour les repérer sans audit complet.
9 octobre 2026
Formation 102846 / points de contrôle rapides - WebAIM

## Diapositive 87 - Texte alternatif : 4 types d’images, 4 décisions

3. points de contrôle rapides | 1. Texte alternatif des images
87
Le texte alternatif est le sous-titre de l’image - sans lui, une partie du message devient muette.
Informative
Apporte une info : photo d’un bâtiment, graphique.
→ texte alternatif court.
Décorative
Pure ambiance : séparateur, icône floue.
→ alt="" (vide).
Fonctionnelle
Dans un lien ou un bouton : logo cliquable, picto.
→ nommer l’action attendue.
Complexe
Diagramme, schéma, infographie.
→ texte court + description longue à part.
9 octobre 2026
Formation 102846 / points de contrôle rapides - Texte alternatif des images
1
2
3
4

## Diapositive 88 - Rédiger un texte alternatif qui sert vraiment

3. points de contrôle rapides | 1. Texte alternatif des images
88
5 règles pour un texte alternatif utile :
• Concis : une phrase courte, centrée sur l’information utile
• Objectif : décrit, ne commente pas
• Pas de « photo de » ni « image de » - le lecteur d’écran le dit déjà
• Contextuel : ce qui compte dans cette page, pas tout ce qui est visible
• Ponctué : point final, pour que le lecteur marque la pause
Piège fréquent
• Un nom de fichier (IMG_4578.jpg) en guise de texte alternatif = information perdue
• Un texte alternatif qui décrit la décoration au lieu du contenu utile
9 octobre 2026
Formation 102846 / points de contrôle rapides - Texte alternatif des images

## Diapositive 89 - Texte alternatif : passe ou échoue ?

3. points de contrôle rapides | 1. Texte alternatif des images
89
Image
Alt proposé
Verdict
Logo ministère dans l’en-tête (lien vers l’accueil)
alt="Ministère de l’Économie - Accueil"
OK - fonctionnelle, action nommée
Photo d’illustration d’un article sur la fraude
alt="image"
KO - aucune information
Séparateur graphique entre deux sections
alt=""
OK - décorative, alt vide
Graphique de répartition budgétaire
alt="graphique montrant la répartition du budget 2026, voir détail ci-dessous"
OK - alt court + renvoi au détail
Icône loupe dans un bouton de recherche
alt="loupe"
KO - décrit l’image, pas l’action (devrait être « Rechercher »)
9 octobre 2026
Formation 102846 / points de contrôle rapides - Texte alternatif des images

## Diapositive 90 - Titre de page : l’étiquette qui oriente

3. points de contrôle rapides | 2. Titre de page
90
Le titre de page est la 1ʳᵉ chose que lit un lecteur d’écran et la seule chose visible dans l’onglet.
Ce qu’il faut vérifier :
• Chaque page a un titre unique, différent des autres pages du site
• Le titre décrit le contenu puis le nom du site (« Déclarer - impots.gouv.fr »)
• Il change quand le contenu principal change (recherche, étape de formulaire)
Exemples
• OK : « Résultats de recherche : accessibilité - Ministère de la Culture »
• KO : « Accueil » sur chaque page du site
• KO : « Untitled Document » (oubli fréquent sur les PDF)
9 octobre 2026
Formation 102846 / points de contrôle rapides - Titre de page

## Diapositive 91 - Titres : la hiérarchie qui structure

3. points de contrôle rapides | 3. Titres et hiérarchie
91
Un utilisateur de lecteur d’écran navigue de titre en titre comme on navigue dans une table des matières.
3 règles qui font passer le check :
• Un seul H1 par page, qui reprend le sujet principal
• Les niveaux s’emboîtent sans saut : H1 → H2 → H3, jamais H2 → H4
• Un titre n’est pas une simple mise en forme gras/gros - c’est une balise <h1> à <h6>
9 octobre 2026
Formation 102846 / points de contrôle rapides - Titres et hiérarchie

## Diapositive 92 - Titres : 3 façons de vérifier

3. points de contrôle rapides | 3. Titres et hiérarchie
92
Méthode
Comment faire
Ce que vous cherchez
Extension HeadingsMap
Installer l’extension, ouvrir le panneau latéral.
L’arbre complet des titres s’affiche, les anomalies en rouge.
Plan de document
Extension Web Developer → Information → View Document Outline.
Le plan liste les titres réels et signale les niveaux manquants.
Clic droit « Inspecter »
Rechercher `h1`, `h2`, `h3` dans l’onglet Éléments.
Un seul <h1>, pas de saut, pas de titre factice (<div class="titre">).
9 octobre 2026
Formation 102846 / points de contrôle rapides - Titres et hiérarchie

## Diapositive 93 - Contraste : un seuil chiffré, pas une opinion

3. points de contrôle rapides | 4. Contraste des couleurs
93
Ce que vous trouvez « joli gris » peut devenir illisible selon l’écran, la lumière ou la vision de l’utilisateur.
4,5:1
Texte normal (sous 18 pt)
3:1
Texte large (18 pt+ ou 14 pt gras) et composants graphiques
7:1
Niveau AAA - recommandé pour texte dense
Ce qui compte :
• Le rapport entre la couleur du texte et celle du fond (ou l’arrière-plan visible)
• Sur un dégradé ou une image, mesurer à l’endroit le moins contrasté
• Ne pas se fier seulement à l’œil - mesurer avec un outil
9 octobre 2026
Formation 102846 / points de contrôle rapides - Contraste des couleurs

## Diapositive 94 - Contraste : 3 outils à avoir sous la main

3. points de contrôle rapides | 4. Contraste des couleurs
94
Outil
Usage
Quand l’utiliser
DevTools Chrome / Firefox
Clic droit sur un texte → Inspecter → pastille de couleur.
Mesure ponctuelle pendant la rédaction ou la relecture.
WebAIM Contrast Checker
webaim.org/resources/contrastchecker - coller les deux couleurs hex.
Avant de choisir une charte graphique ou un thème.
Colour Contrast Analyser (CCA)
App desktop - pipette qui mesure n’importe quelle zone d’écran.
Tester des maquettes Figma, des captures d’écran, des PDF.
Piège classique
• Texte gris clair sur fond blanc (#999 sur #FFF) : 2,85:1 - échec même en texte large
• Bouton bleu avec texte bleu marine « moderne » : souvent sous le seuil
9 octobre 2026
Formation 102846 / points de contrôle rapides - Contraste des couleurs

## Diapositive 95 - Lien d’évitement : le raccourci vers le contenu

3. points de contrôle rapides | 5. Lien d'évitement
95
Sans lien d’évitement, un utilisateur clavier doit souvent traverser tout le menu avant d’atteindre le contenu.
Ce qu’il faut vérifier :
• Le premier lien interactif permet d’aller directement au contenu principal
• Il devient visible dès qu’il a le focus, même s’il était masqué
• Il mène au bloc principal via une ancre (#contenu, #main)
Démo en 3 Tab
• Ouvrez gouvernement.fr et appuyez Tab : le lien « Contenu » apparaît en haut
• Entrée → vous voilà au contenu, menu contourné
9 octobre 2026
Formation 102846 / points de contrôle rapides - Lien d’évitement

## Diapositive 96 - Naviguer sans souris : le test qui change tout

3. points de contrôle rapides | 6. Focus et navigation clavier
96
Quand on navigue au clavier, un focus invisible suffit à perdre toute la page.
En 15 minutes, vous saurez :
• Utiliser 5 touches pour tester n’importe quelle page
• Repérer 3 signaux qui trahissent un défaut d’accessibilité
• Reproduire l’expérience d’un lecteur d’écran en 3 minutes
9 octobre 2026
Formation 102846 / points de contrôle rapides - Focus et navigation clavier

## Diapositive 97 - 5 touches, 3 intentions

3. points de contrôle rapides | 6. Focus et navigation clavier
97
Naviguer → Tab / Shift+Tab    Agir → Entrée / Espace    Lire → Flèches ↑ ↓
Touche
À quoi elle sert
Ce qu’il faut vérifier
Tab
Avancer sur l’élément interactif suivant (lien, bouton, champ).
Le focus se déplace et reste visible à chaque étape.
Shift + Tab
Reculer sur l’élément interactif précédent.
L’ordre inverse est logique, sans saut imprévu.
Entrée
Activer un lien ou soumettre un formulaire.
L’action attendue se déclenche immédiatement.
Barre d’espace
Cocher, décocher, sélectionner un bouton radio.
L’état coché / non coché est annoncé vocalement.
Flèches ↑ ↓
Lire le contenu ligne par ligne avec un lecteur d’écran.
Le texte alternatif des images est lu à haute voix.
9 octobre 2026
Formation 102846 / points de contrôle rapides - Focus et navigation clavier

## Diapositive 98 - 3 signaux qui trahissent un défaut

3. points de contrôle rapides | 6. Focus et navigation clavier
98
Le focus disparaît
Plus de contour visible pendant la tabulation. L’utilisateur est perdu dès la 3ᵉ touche Tab.
L’ordre est illogique
Le focus saute à droite avant le menu à gauche. Le lecteur d’écran parcourt la page dans le désordre.
L’état n’est pas annoncé
Une case qui coche sans dire « coché ». L’information est invisible pour qui ne voit pas l’écran.
9 octobre 2026
Formation 102846 / points de contrôle rapides - Focus et navigation clavier
1
2
3

## Diapositive 99 - Votre mission

3. points de contrôle rapides | 6. Focus et navigation clavier
99
Sur le site d’entraînement qui vous sera fourni :
• Cachez votre souris derrière l’écran
• Tabulez 10 fois et notez chaque fois que le focus disparaît
• Essayez Entrée sur un bouton, Espace sur une case à cocher
• Listez les pièges détectés et associez-les aux 3 signaux
Objectif : votre permis clavier
• 1 signal détecté = vous avez l’œil
• 3 signaux détectés = vous êtes auditeur clavier
9 octobre 2026
Formation 102846 / points de contrôle rapides - Focus et navigation clavier

## Diapositive 100 - Langue de la page : l’accent juste du lecteur d’écran

3. points de contrôle rapides | 7. Langue de la page
100
Sans langue déclarée, le lecteur d’écran peut choisir une mauvaise prononciation et rendre le texte pénible à écouter.
Ce qu’il faut vérifier :
• La balise <html> porte un attribut lang (ex. lang="fr")
• Les passages dans une autre langue sont balisés : <span lang="en">workshop</span>
• Le code langue suit la norme ISO 639 : fr, en, de, es - pas « français »
Comment vérifier sans coder
• Clic droit → Afficher le code source → regarder la 1ʳᵉ ligne <html lang="…">
• Ou extension « Web Developer » → Information → View Document Language
9 octobre 2026
Formation 102846 / points de contrôle rapides - Langue de la page

## Diapositive 101 - Zoom à 200 % : tout doit rester lisible

3. points de contrôle rapides | 8. Zoom à 200 %
101
À 200 %, votre site doit rester le même service : lisible, navigable et utilisable.
Ce qu’il faut vérifier :
• À 200 % de zoom, aucun texte n’est coupé ni superposé
• Pas d’apparition d’un défilement horizontal sur une page classique
• Les menus, boutons et formulaires restent utilisables, pas seulement visibles
Comment tester
• Ctrl + (ou Cmd + sur Mac) pour zoomer jusqu’à 200 % - répéter 4 fois depuis 100 %
• Parcourir la page : formulaire, menu, pied de page. Si ça casse, le check échoue
9 octobre 2026
Formation 102846 / points de contrôle rapides - Zoom à 200 %

## Diapositive 102 - Sous-titres : le son que tout le monde lit

3. points de contrôle rapides | 9. Sous-titres vidéo
102
Une vidéo sans sous-titres devient inutilisable dès que le son manque, est coupé ou ne peut pas être entendu.
Ce qu’il faut vérifier :
• La vidéo propose des sous-titres synchronisés (pas seulement une transcription)
• Les sous-titres incluent les paroles ET les informations sonores importantes : « (rires) », « (sonnerie) »
• Ils sont activables/désactivables par l’utilisateur (bouton CC)
9 octobre 2026
Formation 102846 / points de contrôle rapides - Sous-titres vidéo

## Diapositive 103 - Sous-titres auto : brouillon utile, livrable à relire

3. points de contrôle rapides | 9. Sous-titres vidéo
103
Pourquoi l’auto ne suffit pas :
• Les sous-titres automatiques peuvent déformer les mots, surtout les noms propres et acronymes
• Noms propres, acronymes, chiffres : souvent mal reconnus
• Ponctuation absente : « on mange les enfants » vs « on mange, les enfants »
• Pas d’indication sonore non verbale (musique, applaudissements)
Méthode recommandée
• Générer l’auto (YouTube, Whisper, outil interne) pour accélérer le brouillon
• Relire : noms, chiffres, ponctuation et [indications sonores]
• Tester le rendu : 2 lignes max, contraste fort, sous-titres non masqués
9 octobre 2026
Formation 102846 / points de contrôle rapides - Sous-titres vidéo

## Diapositive 104 - Transcription : la version texte qui accompagne

3. points de contrôle rapides | 10. Transcriptions audio et vidéo
104
La transcription est au podcast ce que le script est au film : la version lisible, indexable, citable.
Ce qu'il faut vérifier :
• Toute vidéo / audio propose un lien visible « Lire la transcription »
• La transcription est complète : paroles + informations sonores essentielles
• Elle est sur la même page ou à un clic, pas cachée à deux étages de menu
• Pour une vidéo : la transcription descriptive inclut aussi l’action visible
Bonus souvent oublié
• La transcription rend le contenu plus facile à retrouver, relire et citer
• Elle sert aussi aux personnes qui ne peuvent pas lancer la vidéo ou l’audio
9 octobre 2026
Formation 102846 / points de contrôle rapides - Transcriptions audio et vidéo

## Diapositive 105 - Audiodescription : la voix qui montre

3. points de contrôle rapides | 11. Audiodescription
105
L’audiodescription ajoute une voix off qui décrit les images clés pendant les silences.
Ce qu’il faut vérifier :
• La vidéo propose une piste audiodécrite activable (bouton AD)
• L’audiodescription décrit les éléments visuels essentiels à la compréhension
• Elle s’intercale dans les silences, sans couvrir les dialogues
• Pour une vidéo sans dialogue essentiel : une description textuelle synchronisée suffit
Quand l’image porte l’information, elle doit aussi être disponible autrement que par la vue.
Principe d’accessibilité vidéo
9 octobre 2026
Formation 102846 / points de contrôle rapides - Audiodescription

## Diapositive 106 - Bonus médias : toujours 2 accès

3. points de contrôle rapides | Bonus médias
106
Règle d'or : un média en ligne doit rester compréhensible par au moins deux chemins : voir, lire ou écouter.
Le réflexe
• Image, schéma ou plan -> description ou texte alternatif
• Vidéo -> sous-titres + informations visuelles essentielles
• Audio ou podcast -> transcription visible et relue
Les pièges à repérer
• Sous-titres lisibles : contraste fort, bandeau si besoin
• Format réseau social : sous-titres non masqués par l'interface
• PDF : texte sélectionnable, pas une image scannée
9 octobre 2026
Formation 102846 / points de contrôle rapides - Bonus médias

## Diapositive 107 - Bonus médias : VSME et transcriptions

3. points de contrôle rapides | Bonus médias
107
Quand le son porte de l'information, la transcription des paroles ne suffit pas toujours.
VSME : ce que ça ajoute
• Dialogues visibles et hors champ
• Bruits utiles, effets sonores et musique
• Voix off, narration, pensée intérieure
• Langue étrangère et son venant d'un haut-parleur
Transcription : choisir le niveau
• Semi-intégrale : résumé détaillé + citations
• Intégrale éditée : texte complet, corrigé et lisible
• Verbatim : mot à mot, hésitations et sons inclus
IA utile pour brouillonner. Publication seulement après relecture humaine.
9 octobre 2026
Formation 102846 / points de contrôle rapides - Bonus médias

## Diapositive 108 - Étiquettes : chaque champ a un nom

3. points de contrôle rapides | 12. Étiquettes de formulaire
108
Sans étiquette, un champ est comme une boîte aux lettres sans nom - on ne sait pas ce qu’on glisse dedans.
Ce qu’il faut vérifier :
• Chaque champ (texte, case, menu déroulant) a une étiquette visible à côté
• L’étiquette reste affichée quand on commence à saisir - elle ne disparaît pas
• Cliquer sur l’étiquette déplace le focus dans le champ (test rapide et décisif)
• Le lecteur d’écran annonce l’étiquette ET le type de champ
9 octobre 2026
Formation 102846 / points de contrôle rapides - Étiquettes de formulaire

## Diapositive 109 - Placeholder ≠ étiquette

3. points de contrôle rapides | 12. Étiquettes de formulaire
109
Pourquoi le placeholder ne remplace pas l’étiquette :
• Il disparaît dès qu’on commence à saisir - on oublie ce qu’on remplit
• Son contraste est souvent trop faible pour passer le check 4
• Il peut être annoncé comme exemple, pas comme nom fiable du champ
• Il devient difficile d’y revenir dès que la saisie commence
Pattern recommandé
• Étiquette visible au-dessus du champ (ou à gauche)
• Placeholder optionnel, pour donner un exemple de format : « JJ/MM/AAAA »
• Ne pas mettre l’information essentielle uniquement dans le placeholder
9 octobre 2026
Formation 102846 / points de contrôle rapides - Étiquettes de formulaire

## Diapositive 110 - Groupes de champs : l’étiquette commune

3. points de contrôle rapides | 12. Étiquettes de formulaire
110
Quand regrouper :
• Plusieurs boutons radio qui répondent à la même question (« Civilité : M / Mme / autre »)
• Plusieurs cases à cocher qui partagent un thème (« Jours travaillés »)
• Adresse découpée en plusieurs champs (n°, rue, code postal, ville)
Cas
Code vérifié
Verdict lecteur d’écran
3 radios « Civilité » sans regroupement
Chaque radio a son label seul
« M, bouton radio » - question perdue
3 radios dans un <fieldset> avec <legend>
<fieldset><legend>Civilité</legend>… <input type="radio">…
« Civilité, M, bouton radio » - question claire
9 octobre 2026
Formation 102846 / points de contrôle rapides - Étiquettes de formulaire

## Diapositive 111 - Champs obligatoires : prévenir puis guider

3. points de contrôle rapides | 13. Champs obligatoires et erreurs
111
Test #13 = avant envoi + après soumission vide : l'obligation prévient, l'erreur guide.
Avant soumission
• Obligation écrite : « obligatoire » ou règle « tous sauf téléphone »
• Astérisque expliqué s'il est utilisé
• Attribut required ou aria-required="true" présent
Après soumission
• Aucune erreur ne doit apparaître avant l'envoi
• Message précis relié au champ, avec aria-invalid si erreur
• Focus vers le récapitulatif ou le premier champ en erreur
9 octobre 2026
Formation 102846 / points de contrôle rapides - Champs obligatoires et erreurs

## Diapositive 112 - Ce qu’on remonte dans la grille

3. points de contrôle rapides | Grille d’audit
112
Champ
Ce qu’il faut écrire
Exemple court
Verdict
C, NC ou NA
NC
Sévérité
Bloquant, gênant, mineur ou info
Gênant
Constat
Ce que vous observez concrètement
Le lien d’évitement n’apparaît pas au focus.
Correctif
Ce que l’équipe doit corriger
Rendre le lien visible et cibler #contenu.
Preuve
URL, capture, sélecteur ou extrait
/actualites - premier appui sur Tab
Règle de travail
• Un défaut sans preuve est difficile à traiter.
• Une preuve sans sévérité est difficile à prioriser.
9 octobre 2026
Formation 102846 / points de contrôle rapides - Grille

## Diapositive 113 - Bonus site web : liens et PDF à repérer

3. points de contrôle rapides | Bonus
113
Pendant l'audit, ces points ne remplacent pas les 13 checks. Mais si vous les voyez, notez-les : ils améliorent vraiment l'expérience utilisateur.
Liens
• Éviter les pages saturées de liens sans hiérarchie
• Libellé explicite : « programme de l'exposition photo »
• Éviter « cliquez ici », « en savoir plus », « programme » seul
• Téléchargement : indiquer type et poids du fichier
Documents PDF
• Texte sélectionnable : pas de PDF image ou scanné non navigable
• Structure : titres, sommaire et liens internes si le document est long
• Images avec texte alternatif
• Si possible : proposer aussi un format éditable ou OpenDocument
9 octobre 2026
Formation 102846 / points de contrôle rapides - Bonus web

## Diapositive 114 - Votre mission : audit en binôme (30 min)

3. points de contrôle rapides | Mission finale
114
Le site d’exercice contient 13 pages : 1 page correspond à 1 point de contrôle.
• Choisissez quelques points avec votre binôme : vous n’avez pas à tout couvrir
• Une seule NC prouvée suffit à invalider le critère
• Certains binômes commencent au début, d’autres par la fin
• Bonus si rencontré : lien ou PDF problématique à noter dans la grille
1
Choisir vos points
2
Prouver 1 NC
3
Début / fin
4
Restitution orale
9 octobre 2026
Formation 102846 / points de contrôle rapides - Mission
