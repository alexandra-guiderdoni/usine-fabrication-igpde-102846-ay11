# Cartographie accessible

**Auteur** : Pole Numerique Inclusif — accessibilite@beta.gouv.fr
**Mention** : session beta : feedback bienvenus !

[Illustration : main tenant une fenetre de navigateur avec le pictogramme d'accessibilite (personnage vert bras et jambes ecartes). Fond bleu, forme jaune decorative. Logo Marianne.]

---

## Slide 2 — Licence Ouverte 2.0

Ce document est sous Licence Ouverte 2.0.

**Vous etes libre de :**

- le communiquer, le reproduire, le copier
- l'adapter, le modifier, l'extraire et le transformer
- le diffuser, le redistribuer, le publier et le transmettre, de l'exploiter a titre commercial, par exemple en la combinant avec d'autres informations, ou en l'incluant dans votre propre produit ou application.

**Sous reserve de :**

- mentionner la paternite de l'information : sa source (ses auteurs et autrices) et la date de cette presentation.

---

## Slide 3 — A propos du Pole Numerique Inclusif beta.gouv.fr

[Photos de l'equipe :]

- **Romy DUHEM-VERDIERE** — Coach a11y
- **Anne-Sophie TRANCHET** — UX/UI Design
- **Gauthier FIORENTINO** — Dev front-end
- **Sabrina LERUEZ** — Produit

Contactez-nous sur **#domaine-accessibilite** ou par email **accessibilite@beta.gouv.fr**

---

## Slide 4 — Question interactive

**Avez-vous des cas d'usage cartographiques a partager ?**

[Slide jaune, texte centre]

---

## Slide 5 — Eviter le #MapFail

Le MapFail (echec cartographique) designe « toutes formes d'oubli, d'erreur ou d'approximation, en general involontaires mais pas obligatoirement, **qui detournent le message de la carte**. [...] l'explosion du nombre de cartes sur Internet a rendu le probleme particulierement visible. »

Source : https://neocarto.hypotheses.org/4029

---

## Slide 6 — Cas d'etude : bad buzz de la carte du deconfinement

[Capture d'ecran d'un tweet de @isafil (IsafilProfASH) :]

« Hier, mon fils de 24 ans, humilie, m'a demande la couleur de notre departement. ..
Le codage des departements en #vert, #orange et #rouge n'a pas ete pense pour les personnes avec #daltonisme : 2 500 000 personnes en France, 4 % de la population. »

[Deux cartes de France : l'une coloree rouge/orange/vert, l'autre montrant un test d'Ishihara (cercles multicolores). Croix rouge (echec).]

9:16 AM - 1 mai 2020 - Twitter for iPhone
1,1 k Retweets — 2,4 k J'aime

Les cartes de la communication graphique ratee du gouvernement pendant la crise du covid-19 au printemps 2020 sont devenues un cas d'etude pour les journalistes et les cartographes... et pour nous : ce sera notre fil rouge ;)

---

## Slide 7 — Exemple de #MapFail : c-conforme.fr

[Capture d'ecran du site c-conforme.fr montrant une carte interactive de France avec des marqueurs bleus. Croix rouge (echec).]

Site officiel listant les etablissements ouverts au public declares conformes a l'accessibilite sous forme de carte interactive.
De l'avis des personnes concernees : **« la presentation carto, c'est nul pour ceux qui ont des problemes de vue ou de manipulation ».**
Ici, la presentation de l'information sous forme de carte n'est ni pertinente ni adaptee a la cible.

Source : https://c-conforme.fr

---

## Slide 8 — Quelle est l'information a communiquer ?

**Quelle est l'information a communiquer ?**

Une carte est-elle la seule facon de communiquer cette information ?

N'y a-t'il pas plus simple &/o plus approprie ?

[Slide jaune]

---

## Slide 9 — Rappels de cartographie

[Slide de section, fond gris clair]

---

## Slide 10 — Rappels de cartographie : finalite

Toute carte a une finalite : **construire une carte c'est exprimer un message.**

Une carte doit imperativement comporter :

- **Titre** precis (ou, quand, quoi?)
- **Legende** precise et organisee
- **Echelle** (echelle graphique)
- **Orientation** de la carte
- **Sources** des donnees
- **Auteur et date** de realisation

[Schema d'une carte de France avec titre, legende, echelle et source des donnees]

Pour en savoir plus :
- Cours semiologie graphique et SIG #M1 SIGAT CC by sa Boris Mericskay
- Les 8 regles d'or CC by sa CartONG

---

## Slide 11 — Contrastes suffisants

**Contrastes suffisants**
pour les personnes malvoyantes

[Slide de section, fond bleu]

---

## Slide 12 — Exemple d'aplats de couleur pastel insuffisants

[Carte de France avec des aplats de couleur pastel (bleu clair, gris). Croix rouge (echec).]

Ces aplats de couleur pastel ne presentent pas un contraste suffisant avec le fond blanc pour que la carte soit perceptible par tout le monde.

Une delimitation des zones par un trace contraste (des bordures noires plutot que blanches) retablirait sa perception.

Source : https://metabase.incubateur.net/public/dashboard/554ff353-6104-4c25-a261-d8bdc40f75d5?date_d%27arriv%25C3%25A9=past3years~

---

## Slide 13 — Assurer un contraste suffisant

**Assurer un contraste suffisant** pour que la carte soit perceptible par tout le monde

= contraste d'au moins 3:1

- avec le **fond**
- ou avec les **couleurs voisines**

[Capture d'ecran de Color Contrast Analyser (CCA) montrant :]
- Couleur de Premier plan : #8AC4EF
- Couleur d'Arriere plan : #FFFFFF
- Ratio de contraste : 1,9:1
- 1.4.3 Contraste (Minimum) (AA) : Echec (texte normal), Echec (grand texte)
- 1.4.6 Contraste (Augmente) (AAA) : Echec (texte normal), Echec (grand texte)
- **1.4.11 Contrastes des elements graphiques (AA)** : Echec (composants UI et objets graphiques)

Color Contrast Analyser (tpgi.com/color-contrast-checker/) permet de calculer le contraste entre deux couleurs

---

## Slide 14 — Exemple conforme : carte des etablissements penitentiaires

[Carte de France des etablissements penitentiaires avec des cercles de differentes tailles et couleurs (vert, jaune). Coche verte (conforme).]

Les contours des cercles colores presentent un contraste suffisant.

[Capture d'ecran CCA :]
- Couleur de Premier plan : #727D43
- Couleur d'Arriere plan : #D5D7D9
- Ratio de contraste : 3,1:1
- 1.4.11 Contrastes des elements graphiques (AA) : Conforme (composants UI et objets graphiques)

Source : Administration penitentiaire, 2009 — Conception-realisation : G. Milhaud & G. Flessel (UMR RDEG, 2009)

---

## Slide 15 — Exemple conforme : vigilances meteo

[Carte de France des vigilances meteo avec des zones de couleurs contrastees (noir, orange, rose). Coche verte (conforme).]

Inondations, Pluie intense, Vent violent, Risques sensibles, Aucun risque

[Capture d'ecran CCA :]
- Couleur de Premier plan : #000000 (black)
- Couleur d'Arriere plan : #E9BD85
- Ratio de contraste : 12,1:1
- Tous les criteres conformes (AA et AAA)
- 1.4.11 Contrastes des elements graphiques (AA) : Conforme

Source : https://jionotz.wordpress.com/2015/07/24/visualisation-des-vigilances-meteo-round-3/

---

## Slide 16 — Outil de palette carto : ColorBrewer

**Outil de palette carto : https://colorbrewer2.org**

[Capture d'ecran de ColorBrewer 2.0 montrant :]
- Number of data classes : 10
- Nature of your data : diverging (selectionne)
- Pick a color scheme : palette BrBG selectionnee
- Only show : colorblind safe (coche)
- Liste de 10 couleurs HEX (#543005, #8c510a, #bf812d, #dfc27d, #f6e8c3, #c7eae5, #80cdc1, #35978f, #01665e, #003c30)
- Carte a droite avec les zones colorees

Outil facilitant le choix de palettes colorees preservant la lisibilite de plusieurs classes de donnees.

---

## Slide 17 — Ne pas utiliser seulement la couleur

**Ne pas utiliser seulement la couleur**
pour les daltoniens et achromates

[Slide de section, fond bleu]

---

## Slide 18 — Cas d'etude : tweet daltonisme

[Reprise du tweet de @isafil avec la carte rouge/orange/vert et le test d'Ishihara, en plus grand format]

---

## Slide 19 — Il existe differentes formes de daltonisme

**Il existe differentes formes de daltonisme**

- 92% — Normal Vision
- 2,7% — Deuteranomaly
- 0,66% — Protanomaly
- 0,59% — Protanopia
- 0,56% — Deuteranopia
- 0,016% — Tritanopia
- 0,01% — Tritanomaly
- <0,0001% — Achromatopsia

[6 cartes de France montrant la carte du deconfinement vue avec chaque type de daltonisme — les couleurs deviennent indistinguables dans la plupart des cas]

Certaines couleurs cartographiques ne peuvent se distinguer dans tous les cas de daltonisme.
Source : http://romy.tetue.net/Illisible-carte-du-deconfinement

---

## Slide 20 — Comment tester ?

**Comment tester ?**

Des outils permettent de simuler differentes visions daltoniennes :
- Coblis
- Toptal Colorfilter
- etc.

**Le test le plus fiable est de passer en noir et blanc.**
La question a se poser : est-ce comprehensible en cas d'impression N/B ?

[Deux cartes de France en niveaux de gris montrant que les zones deviennent indistinguables]

---

## Slide 21 — Carte corrigee avec motifs

[Deux cartes de France cote a cote :]

Legende :
- Rouge (hachures diagonales)
- Vert (croix)
- Orange (points)

Carte officielle corrigee par les internautes : l'information est vehiculee par la couleur ET des motifs (hachures, points, croix).

[Coche verte (conforme)]

---

## Slide 22 — Ne pas donner l'information uniquement par la couleur

Ce n'est pas en agissant sur les couleurs que l'on peut aider les personnes qui les percoivent pas ou mal =>

**ne pas donner l'information uniquement par la couleur**

(critere 3.1 du RGAA 4)

[Slide jaune]

---

## Slide 23 — Info trafic & daltonisme

**Info trafic** & daltonisme

[Trois captures d'ecran de cartes de trafic a Grenoble :]

- **Open Street Map** — Croix rouge (echec)
- **Google Maps** — Croix rouge (echec)
- **Apple Plans** — Coche verte (conforme)

Source : etude comparative de differentes cartes d'info trafic et temoignage de Didier Lebouc

---

## Slide 24 — Combiner avec d'autres variables visuelles

Astuce : **combiner avec d'autres variables visuelles**

[Schema de semiologie visuelle de Jacques Bertin :]

- **couleur** — palette de couleurs variees
- **grain** — textures plus ou moins denses
- **valeur** — noir, gris fonce, gris clair
- **forme** — carre, triangle, cercle, fleche, croix, tiret
- **taille** — carres de tailles croissantes
- **orientation** — hachures dans differentes directions

Semiologie visuelle de Jacques Bertin — Voir aussi : https://neocarto.hypotheses.org/3940

---

## Slide 25 — Exemples de cartes combinant couleur et autres variables

Exemples de cartes n'utilisant **pas que la couleur** pour informer, mais aussi des symboles, des textures, des tailles, du texte...

[6 cartes de France :]
1. Carte en niveaux de gris avec textures (points, hachures)
2. Carte jaune avec pictogrammes d'animaux
3. Carte avec cercles proportionnels de differentes couleurs
4. Carte schematique avec fleches colorees et noms de regions
5. Carte « serpilliere/torchon/wassingue » avec texte dans chaque region
6. Carte avec etiquettes colorees par region

---

## Slide 26 — Legender !

**Legender !**

[Slide de section, fond bleu]

---

## Slide 27 — Cartes officielles COVID-19 sans legende explicite

Exemple : cartes officielles de communication lors de la crise COVID-19

[Deux cartes cote a cote :]

**Carte 1** — Ministere des Solidarites et de la Sante : carte rouge/jaune avec legende « SYNTHESE / CIRCULATION ACTIVE DU VIRUS / TENSION HOSPITALIERE SUR LES CAPACITES EN REANIMATION »
-> Croix rouge : En l'absence de legende, la carte est incomprehensible.

**Carte 2** — Carte « Circulation du coronavirus: quel est le code couleur de votre departement ? » avec legende « departement classe rouge / departement classe orange / departement classe vert »
-> Croix rouge : La legende n'est pas explicite.

---

## Slide 28 — Version corrigee, avec legende explicite

**Version corrigee, avec legende explicite**

[Carte du Ministere des Solidarites et de la Sante, datee 03/05/2020, avec :]

**SYNTHESE DES 2 INDICATEURS**
- CIRCULATION ACTIVE DU VIRUS
- TENSION HOSPITALIERE SUR LES CAPACITES EN REANIMATION

Legende explicite :
- [cercle rouge avec hachures] Departements dont le deconfinement pourrait etre durci.
- [cercle jaune avec points] Departements incertains.
- [cercle vert avec motif] Departements eligibles au deconfinement selon le protocole annonce.

[Coche verte (conforme)]

Source : https://www.facebook.com/agenceadequat1/photos/a.220523121452949/1398869510284965/

---

## Slide 29 — Exemple : CartoBio

**Exemple : CartoBio**

[Capture d'ecran de CartoBio montrant une carte avec un panneau « Calques » et un pop-in « Calque "Classification" » :]

- Vert : la parcelle est cultivee en Agriculture Biologique (AB) ou est en conversion ;
- Orange : la parcelle est cultivee en agriculture conventionnelle ;

La legende est ici cachee en pop-in.

**La legende doit etre toujours visible a proximite de la carte.**

Source : CartoBio

---

## Slide 30 — Exemple : Geoportail

**Exemple : Geoportail**

[Capture d'ecran du Geoportail montrant une carte de cultures agricoles avec une legende de plus de 20 couleurs : Ble tendre, Mais grain et ensilage, Orge, Autres cereales, Colza, Tournesol, Autre oleagineux, Proteagineux, Plantes a fibres, Semences, Gel, Gel industriel, Autres gels, Legumineuses a grains, Riz, Fourrage, Estives et landes, Prairies permanentes, Prairies temporaires, Vergers, Vignes, Fruit a coque, Oliviers, Autres cultures industrielles, Legumes ou fleurs, Canne a sucre]

La legende doit etre toujours visible [coche verte]

Cette carte des cultures agricoles affiche beaucoup (trop) d'informations differentes, rendant la legende complexe + beaucoup de couleurs difficiles a distinguer pour les daltoniens.

*Quel est l'objectif de cette carte ? Quelle information doit-elle apporter ?*

Source : https://www.geoportail.gouv.fr/carte

---

## Slide 31 — Exemple : Urssaf (legende avec symboles)

[Capture d'ecran de la dataviz Urssaf montrant une carte de France avec des marqueurs et un panneau lateral « Type de sites » :]

- Urssaf
- Urssaf Caisse nationale
- Caisse generale de securite sociale et Caisse de securite sociale
- Caisse commune de Securite sociale de Lozere
- Uniquement les sieges sociaux

Services [point rose]
Activites de gestion interne [point orange]

[Fleche jaune pointant la legende — bonne pratique]

l'Urssaf compte **145** sites au service de **11 021 459 usagers**

Source : https://dataviz-1.urssaf.fr/reseau-et-chiffres-cles/

---

## Slide 32 — Naviguer au clavier

**Naviguer au clavier**
sur les cartes interactives

[Slide de section, fond bleu]

---

## Slide 33 — Naviguer au clavier

**Naviguer au clavier**

Si des elements de la cartographie sont cliquables a la souris, ils devraient aussi etre navigables au clavier.

[Illustration : mains sur un clavier avec un ecran affichant une carte interactive. Croix rouge sur la souris (barree).]

Pour en savoir plus sur la navigation au clavier : https://a11y-guidelines.orange.com/fr/web/outils/methodes-et-outils-de-test/navigation-clavier/

---

## Slide 34 — Carte interactive simple

**Carte interactive simple**

[Capture d'ecran du site info-meningocoque.fr montrant :]

A gauche : structuration en liste de liens (en HTML) par dessus laquelle s'affiche une carte (en CSS).

Liste des regions : Aquitaine, Alsace, Auvergne, Basse-Normandie, Bourgogne, Bretagne, Centre, Champagne-Ardenne, Corse, Franche-Comte, Haute-Normandie, Ile de France, Languedoc-Roussillon, Lorraine, Limousin, Midi-Pyrenees, Nord-Pas-de-Calais, Pays de la Loire, Poitou-Charentes, Picardie, Provence-Alpes-Cote d'Azur, Rhone-Alpes

DOM : Guadeloupe...

A droite : carte cliquable des regions de France (DRASS)

L'usage d'elements natifs preserve la navigation.

Source : https://web.archive.org/web/20090129.../http://info-meningocoque.fr/directions-regionales.html

---

## Slide 35 — Proposer une alternative

**Proposer une alternative**
N'oublions pas les aveugles !

[Slide de section, fond bleu]

---

## Slide 36 — Proposer une alternative

**Proposer une alternative**

La solution la plus simple et la plus efficace pour rendre accessibles les composants complexes tels que les graphiques ou les cartes est de **proposer les memes contenus/informations dans une alternative accessible** plutot que de chercher a travailler sur ces composants dynamiques directement.

[Photo : personne aveugle consultant Internet sur smartphone de facon auditive : a l'aide d'une synthese vocale.]

Source : https://www.systeme-de-design.gouv.fr/elements-d-interface/composants-beta/graphiques-charts/

---

## Slide 37 — Quelle alternative pour la carte du deconfinement ?

**Quelle alternative pour la carte du deconfinement ?**

[3 exemples cote a cote :]

**1. Liste manuscrite sur papier** [coche verte]
Liste informative manuscrite listant les departements et leur couleur.

**2. Liste coloree** [croix rouge]
Liste typographiee avec les departements et leur couleur (ex : « 75 — Paris — Paris — Orange », « 77 — Seine-et-Marne — Melun — Orange ») mais contraste insuffisant.

**3. Liste dynamique** [croix rouge]
Liste des departements (Guadeloupe (971), Martinique (972)... Ain (01), Aisne (02)...) sans mention de la couleur associee.

Sources : une internaute, BFMTV et SortirAParis

---

## Slide 38 — Alternative audio ? inutile : mieux vaut la synthese vocale ;)

**Alternative audio ? inutile : mieux vaut la synthese vocale ;)**

La secretaire d'etat chargee des personnes handicapees propose une version audio de la carte du deconfinement :

[Tweet de Sophie Cluzel @s_cluzel, 30 avril 2020 :]
« #COVID19 #Handicap Attentive a l'acces des informations pour tous nos concitoyens notamment les personnes #malvoyantes voici liste des #departements classes rouge vert orange en version audio. @MinSoliSante @handicap_gouv »

Il aurait ete **plus facile de fournir une liste textuelle** et bien plus pratique pour les personnes concernees, puisque vocalisable a leur gre : « plutot que d'ecouter un fichier son de 2 minutes 48, une personne deficiente visuelle pourrait trouver tout de suite son departement en faisant *Ctrl+F + numero du departement* » explique l'administrateur de l'AVH.

[Photo : personne utilisant un logiciel de synthese vocale qui lit le texte a l'ecran]

Source : https://twitter.com/s_cluzel/status/1255133381077904179

---

## Slide 39 — Exemple : vie-publique.fr

**Exemple : vie-publique.fr**

[Capture d'ecran montrant :]

A gauche : carte du monde « Monde : perception de la corruption » avec une legende coloree.

A droite : transcription textuelle depliable listant les pays par indice de corruption :
- de 70 a 88 (peu corrompu) : Danemark (88), Nouvelle Zelande (87), Finlande (85), Singapour (85)...
- de 55 a 69 : Barbade (68), Bhoutan (68), Chili (67)...
- de 40 a 54 : Malte (54), Namibie (53)...

Sur ce site exemplaire, des transcriptions textuelles sont disponibles a la demande, dans un panneau depliable.

Source : https://www.vie-publique.fr/carte/272238-monde-perception-de-la-corruption-en-20...

---

## Slide 40 — RGAA : la cartographie est exemptee

**RGAA : la cartographie est exemptee**

« Certains contenus sont exemptes de l'obligation d'accessibilite et se situent hors champ de l'obligation legale : [...] Les cartes et les services de cartographie en ligne, **sous reserve que** , s'agissant des cartes destinees a fournir une localisation ou un itineraire, **les informations essentielles soient fournies sous une forme numerique accessible** . »

Source : https://accessibilite.numerique.gouv.fr/obligations/champ-application/

---

## Slide 41 — Alternatives accessibles

**Alternatives accessibles**

- Utiliser un **tableau** :
  presenter les resultats sous forme de tableau est sans doute l'option la plus simple, surtout s'il y a beaucoup de donnees a presenter. Dans le cas des contenus les plus complexes, on privilegiera la creation de plusieurs tableaux simples et non de tableaux avec des cellules fusionnees.

- Utiliser une **liste** :
  lorsqu'il n'y a que quelques donnees a presenter, une liste (simple ou titree) peut suffire ;

- Utiliser du **texte** :
  dans d'autres cas, l'information peut deja etre presente dans le corps de texte adjacent ou l'alternative peut etre un texte (simple ou structure).

L'alternative ou un moyen d'acceder a l'alternative (lien/bouton) doit etre **adjacente a la carte**.

Source : https://www.systeme-de-design.gouv.fr/elements-d-interface/composants-beta/graphiques-charts/

---

## Slide 42 — Exemple : CartoBio (alternative tableau)

[Capture d'ecran de CartoBio montrant cote a cote :]

A gauche : tableau « Parcelles par type de culture » avec colonnes Nom, Certification, Surface, Actions
- 38 parcelles, 45,00 ha
- Arbres forestiers : 4,81 ha
- ilot 1, parcelle 1 — Multi-culture — AB 08/2016 — 2,66 ha
- ilot 1, parcelle 2 — Multi-culture — AB 08/2016 — 0,61 ha
- ilot 1, parcelle 3 — Multi-culture — AB 08/2016 — 1,51 ha
- ilot 19, parcelle 2 — AB 08/2016 — 0,04 ha
- Champignons et truffes — 0,14 ha

A droite : carte avec les parcelles et panneau Calques (Plan, Satellite, RPG 2024, Cadastre)

Source : CartoBio

---

## Slide 43 — Laisser le choix : AccesLibre

**Laisser le choix**

[Capture d'ecran du site AccesLibre (acceslibre.beta.gouv.fr) montrant :]

Recherche : « Rue des Petits champs, Lyon : restau »
379 etablissements correspondant a votre recherche

Boutons : « Masquer la liste » / « Masquer la carte »

Choix possible entre :
- liste seule
- carte seule
- les deux cote a cote

A gauche : liste des etablissements (Namdo, Pharmacie du Serpent, Notre Dame de Lorette, Centre de vaccination municipal...)
A droite : carte interactive avec marqueurs

Source : AccesLibre

---

## Slide 44 — Laisser le choix : Cartographie Nationale

**Laisser le choix**

[Capture d'ecran de la Cartographie Nationale des lieux d'inclusion numerique montrant :]

Page d'accueil : « Bienvenue sur la Cartographie Nationale des lieux d'inclusion numerique »

Deux options :
- « Orienter un beneficiaire — Grace a notre questionnaire en 4 etapes » [fleche verte pointant cette option]
- « ou Acceder directement a la carte »

Filtres : Besoin, Localisation, Accessibilite, Disponibilite

Ce site donne le choix entre naviguer dans une carte interactive ou via un questionnaire.

19171 lieux references sur la carte

Source : https://cartographie.societenumerique.gouv.fr

---

## Slide 45 — Exemple : Cartographie Nationale (liste laterale)

[Capture d'ecran de la Cartographie Nationale avec la vue carte et la liste laterale :]

Regions listees a gauche :
- Auvergne-Rhone-Alpes — 2488 resultats — HINAURA
- Bourgogne-Franche-Comte — 1246 resultats — MedNum BFC
- Bretagne — 798 resultats — HUB
- Centre-Val de Loire — 798 resultats — HUB-LO
- Corse — 157 resultats
- Grand Est — 1238 resultats — HubEst
- Guadeloupe — 92 resultats — LA MEDNUM Hub Antilles

A droite : carte avec bulles numerotees (2620, 838, 1631, 1238, 798, 951, 798, 1246, 2721, 2488, 2142, 971)

La liste laterale permet d'acceder aux memes informations que les points de la carte. [Coche verte]

Source : https://cartographie.societenumerique.gouv.fr/cartographie

---

## Slide 46 — Exemple : VigiEau (onglet Carte/Donnees)

[Capture d'ecran de VigiEau montrant :]

**Carte des restrictions**
Arretes publies avant le 13 mai 2024

Onglets : **Carte** (selectionne) / Donnees

Situation par ressource :
- Eau potable (selectionne)
- Eau superficielle
- Eau souterraine

Raccourcis : Metropole, La Reunion, Guadeloupe, Martinique, Mayotte, Guyane

[Fleche verte pointant les onglets Carte/Donnees]

Niveau de restriction affiche sur la carte :
- PAS DE RESTRICTIONS
- VIGILANCE
- ALERTE
- ALERTE RENFORCEE
- CRISE

Source : https://vigieau.gouv.fr

---

## Slide 47 — Exemple : VigiEau (onglet Donnees)

[Capture d'ecran de VigiEau, onglet **Donnees** selectionne :]

Situation de la secheresse en France (niveau de gravite maximum contaste par departement)

- PAS DE RESTRICTIONS : 95 departements
- VIGILANCE : 0 departements
- ALERTE : 1 departements
- ALERTE RENFORCEE : 3 departements
- CRISE : 2 departements

Tableau « Niveau de gravite maximal observe par departement » avec champ Rechercher :

| N° Departement | Departement | Niveau de gravite |
|---|---|---|
| 01 | Ain | Alerte renforcee |
| 02 | Aisne | Pas de restrictions |
| 03 | Allier | Pas de restrictions |
| 04 | Alpes-de-Haute-Provence | Pas de restrictions |
| 05 | Hautes-Alpes | Pas de restrictions |
| 06 | Alpes-Maritimes | Pas de restrictions |

[Fleche verte + coche verte]

Information disponible sous forme de **tableau**, en alternative a la carte, dans un autre onglet.

Source : https://vigieau.gouv.fr

---

## Slide 48 — Exemple : alternative textuelle pour une carte de localisation

[Capture d'ecran montrant :]

**ADRESSE**
54, boulevard de la liberte
59800 LILLE

**ACCES METRO**
Station "Republique - Beaux Arts" ou "Rihour"

**ACCES BUS**
Arret Nationale - Citadine Lille
Liane 01 et Liane 90
Ligne 12

[Carte Google Maps montrant la localisation a Lille]

Cette carte porteuse d'informations est accompagnee d'une alternative textuelle indiquant l'adresse ainsi que les stations de metro et lignes de bus proches du lieu geolocalise. [Coche verte]

Source : https://www.accede-web.com/notices/editoriale-modele/utiliser-correctement-les-contenus-riches-et-multimedias/associer-une-description-detaillee-aux-contenus-riches/

---

## Slide 49 — Checklist pour une cartographie accessible

**Checklist pour une cartographie accessible**

- [ ] **Eviter le #MapFail** :
  1. Quelle est l'information a communiquer ?
  2. Une carte est-elle la seule facon de communiquer cette information ? N'y a-t-il pas plus simple &/o plus approprie ?

- [ ] Assurer des **contrastes suffisants**
  avec le fond &/o avec les couleurs voisines

- [ ] Assurer la comprehension en l'**absence de couleur**
  associer couleur ET forme, texture, picto...

- [ ] **Legender** !

- [ ] Preserver la **navigation au clavier**

- [ ] Proposer une **alternative**
  a proximite : via liste, tableau ou texte

Comment dire « liste de controle » en LSF ? https://www.sourds.net/2021/09/03/liste-de-controle/

---

## Slide 50 — Nos prochains rendez-vous

**Nos prochains rendez-vous**

Retrouvez nos formations sur l'espace membre ou dans l'infolettre

[Capture d'ecran de la page formations avec les categories : Nouveaux arrivants, Design, Accessibilite (selectionne), Divers, Communication, Marketing, Tech, Produit, E-learning]

Formations listees :
- Atelier « Verifier rapidement l'accessibilite de son service » - 14/04/2025 (14 avril a 10h00)
- (Complete - Liste d'attente) Atelier Cartographie et accessibilite - 15/04/2025 (15 avril a 11h00)
- Automatiser les tests d'accessibilite - 24/04/2025 (24 avril a 14h00)
- Simplification de contenu - 03/06/2025
- Atelier « Verifier rapidement l'accessibilite de son service » - 10/06/2025
- Automatiser les tests d'accessibilite - 16/06/2025

---

## Slide 51 — Bonne route !

**Bonne route !**

[Illustration identique a la slide 1 : main tenant la fenetre de navigateur avec le pictogramme d'accessibilite. Fond bleu, forme jaune, emoji souriant.]

---

## Slide 52 — Cas pratiques

**Cas pratiques**

[Slide de section, fond bleu fonce]

---

## Slide 53 — uMap

**uMap**

[Capture d'ecran de la page d'accueil de uMap :]

**Une solution simple pour creer des cartes en ligne**

uMap est un outil libre et open-source utilise par les collectivites et reference dans le catalogue SILL (Socle Interministeriel des Logiciels Libres).

Boutons : « + Creer une carte » / « Participer a un prochain webinaire »

Chiffres :
- **121 453** comptes utilisateurs
- **1 165 018** cartes creees
- **7 565** utilisateurs actifs par semaine

---

## Slide 54 — uMap : exemple de carte

**uMap**

[Capture d'ecran d'une carte uMap « Memoire des inondations en vallees des gaves » montrant :]

Panneau « Visualiser les donnees » avec onglets Donnees / A propos :
- Reperes historiques (76)
- Reperes normalises (60)
- Territoire du PAPI (1)

Option : « Lister seulement les elements visibles »

Carte avec marqueurs violets numerotes (6, 9, 17, 2, 2) sur une zone des Pyrenees.

https://umap.incubateur.anct.gouv.fr/fr/map/memoire-des-inondations-en-vallees-des-gaves_273#10/42.9132/-0.0755

---

## Slide 55 — Panoramax (presentation)

**Panoramax**

[Capture d'ecran de la page d'accueil de Panoramax :]

**L'alternative libre pour photo-cartographier les territoires**

Panoramax est une ressource numerique permettant la mise en commun et l'exploitation de photos de terrain. Toute personne peut photographier des lieux visibles depuis la voie publique afin d'alimenter la base de donnees de Panoramax. Ces donnees sont ensuite librement accessibles et reutilisables.

Bouton : « Voir le catalogue de photos »

**Comment ca marche ?**

Panoramax federe les initiatives d'une large communaute (collectivites, contributeurs OSM, IGN, services publics) participant au geocommun de bases de vues de terrain.

- Un geocommun
- Une architecture
- Une gouvernance

---

## Slide 56 — Panoramax (carte)

**Panoramax**

[Capture d'ecran de la carte Panoramax montrant la couverture photographique en Europe, concentree sur la France (zones orange). Barre de recherche, filtres, calques.]

https://api.panoramax.xyz/#focus=map&map=3.83/52.75/8.58&speed=250

---

## Slide 57 — Panoramax (vue immersive)

**Panoramax**

[Capture d'ecran de la vue immersive Panoramax : photo d'une route de campagne au crepuscule avec des fleches de navigation bleues. Mini-carte en bas a gauche.]

PanierAvide - 26 aout 2018

---

## Slide 58 — Carte complexe (exemple de wargame)

[Carte hexagonale complexe type wargame/simulation militaire avec de nombreux elements superposees : routes, rivieres, zones urbaines (rose), voies ferrees, hexagones numerotes. Tres dense visuellement.]

---

## Slide 59 — Bonne route ! (bis)

**Bonne route !**

[Illustration identique a la slide 1 et 51 : main tenant la fenetre de navigateur avec le pictogramme d'accessibilite. Fond bleu, forme jaune, emoji souriant.]
