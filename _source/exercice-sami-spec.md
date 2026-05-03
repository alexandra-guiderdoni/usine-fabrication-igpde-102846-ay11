# Exercice « Les erreurs de Sami » - Spécification

Formation 102638 - Support de la slide 32.
Amendé suite au Devil Council du 2026-05-02.

---

## Contexte pédagogique

Sami, charge de communication a la Direction des affaires juridiques, envoie son rapport trimestriel « Bilan T1 2025 » a 40 destinataires. Le document contient 18 erreurs d'accessibilite couvrant les 5 piliers, dont une erreur ambigue qui force le jugement. Les erreurs des piliers 4 et 5 sont revelees apres l'enseignement de ces piliers (slide 37, effet Zeigarnik).

- **Public** : communicants, niveau initiation
- **Format** : exercice en binôme, 25 minutes (3 phases)
- **Modalité** : identifier d'abord, corriger ensuite, discuter en restitution
- **Livrables** : `sami-doc-inaccessible.docx` + `sami-doc-accessible.docx`

---

## Les 8 erreurs et leurs corrections

Ordre de correction prescrit : Structure (Pilier 1) puis Couleurs (Pilier 2) puis Contenus (Pilier 3).

### Erreur 1 - Faux Titre 1 (Pilier 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| « Introduction » en **gras Arial 16** (formatage direct) | « Introduction » avec le **style Titre 1** natif Word |

Pourquoi : sans style, le lecteur d'écran voit un bloc plat sans repère de navigation.

### Erreur 2 - Faux Titre 2 (Pilier 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| « Résultats du trimestre » en **gras Arial 14** (formatage direct) | « Résultats du trimestre » avec le **style Titre 2** natif Word |

Pourquoi : la hiérarchie ne se limite pas au titre principal. Un sous-titre non balisé casse la navigation par niveaux.

### Erreur 3 - Faux Titre 3 (Pilier 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| « Détail par canal » en **gras Arial 12 souligné** (formatage direct) | « Détail par canal » avec le **style Titre 3** natif Word |

Pourquoi : le soulignement donne un indice visuel mais aucun indice sémantique. Le lecteur d'écran ne distingue pas ce sous-titre du texte courant.

### Erreur 4 - Tableau sans en-tête (Pilier 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| Tableau de résultats sans ligne d'en-tête identifiée | Onglet Création > cocher **Ligne d'en-tête** |

Contenu du tableau :

| Indicateur | T4 2024 | T1 2025 | Evolution |
|---|---|---|---|
| Visiteurs uniques | 45 200 | 50 600 | +12 % |
| Pages vues | 128 000 | 142 000 | +11 % |
| Taux de rebond | 42 % | 38 % | -4 pts |

Pourquoi : sans en-tête balisé, le lecteur d'écran ne peut pas associer chaque cellule à sa colonne.

### Erreur 5 - Couleur seule (Pilier 2 - Couleurs)

| Inaccessible | Accessible |
|---|---|
| URGENT en rouge (sans gras, sans autre indication) | **URGENT - Retour attendu avant le 30 juin 2025** (gras + texte explicatif + couleur) |

Pourquoi : sans gras et sans texte complémentaire, la seule distinction est la couleur rouge. Une personne daltonienne ou utilisant un écran monochrome ne perçoit aucune urgence — le mot se fond dans le texte courant. Illustration pure du critère WCAG 1.4.1.

### Erreur 6 - Contraste ambigu (Pilier 2 - Couleurs)

| Inaccessible | Accessible |
|---|---|
| Note de bas de page en **gris #767676 sur fond blanc** (ratio 4,48:1 - insuffisant pour du texte normal) | Texte en **gris #595959** (ratio 7:1) ou en noir |

Pourquoi : le ratio 4,48:1 est en dessous du seuil 4,5:1 pour le texte normal (WCAG 1.4.3). L'erreur est subtile : le texte semble lisible mais échoue de justesse au test. C'est l'erreur ambiguë qui force le jugement - les stagiaires doivent mesurer, pas deviner.

**Rôle pédagogique** : cette erreur n'a pas de réponse évidente visuellement. Elle oblige à utiliser un outil de mesure (CCA ou vérificateur) et à trancher sous incertitude. C'est la seule erreur que le formateur doit explicitement débriefer.

### Erreur 7 - Image sans alternative + couleurs seules (Pilier 3 + Pilier 2)

| Inaccessible | Accessible |
|---|---|
| Graphique sans texte alternatif, barres différenciées uniquement par la couleur (vert/rouge/orange, sans motif ni étiquette) | Alt text : « Graphique d'évolution du trafic web T1 2025 : visiteurs uniques en hausse de 12 %, pages vues +11 %, taux de rebond en baisse de 4 points ». Barres avec motifs distincts (hachures, points, plein) + étiquettes sur chaque barre |

Pourquoi : double erreur. (1) Le lecteur d'écran annonce « image » sans description. (2) Même pour un voyant daltonien, les barres vert/rouge/orange sont indiscernables sans motif ni légende textuelle. Ce graphique est inutilisable pour ~8 % de la population masculine.

**Rôle pédagogique** : montre que l'accessibilité d'une image ne se limite pas à l'alt text — le contenu visuel lui-même doit être lisible sans couleur.

### Erreur 8 - Lien non descriptif (Pilier 3 - Contenus)

| Inaccessible | Accessible |
|---|---|
| « cliquez ici » pour les annexes | « Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo) » |

Pourquoi : « cliquez ici » ne donne aucune information hors contexte visuel. Le lecteur d'écran liste les liens par intitulé.

### Erreur 9 - Organigramme avec alt inadapte (Pilier 3 - Contenus)

| Inaccessible | Accessible |
|---|---|
| Organigramme avec alt="image.png" (nom de fichier par defaut) | alt="Organigramme de la Direction des affaires juridiques (description ci-dessous)." + description textuelle detaillee sous l'image |

Pourquoi : le nom de fichier ne donne aucune information. Pour une image complexe (RGAA 1.6 et 1.7), l'alt doit rester court (~80 caracteres) et renvoyer vers une description detaillee presente dans le document. Ne pas tout mettre dans l'alt.

**Role pedagogique** : montre la difference entre image simple (alt descriptif) et image complexe (alt court + description adjacente). Illustre aussi le piege du nom de fichier automatique.

### Erreur 10 - Icone redondante avec alt non vide (Pilier 3 - Contenus)

| Inaccessible | Accessible |
|---|---|
| Icone enveloppe avec alt="E-mail" (redondant avec le texte adjacent) | Icone marquee comme decorative (case « Marquer comme decoratif » cochee) |

Pourquoi : l'icone est placee juste a cote du mot « e-mail ». Si on ecrit « E-mail » dans l'alternative, le lecteur d'ecran lit « E-mail, e-mail » — redondance qui pollue la lecture. Toute image qui n'apporte pas d'information supplementaire doit etre ignoree. Dans Word, on coche « Marquer comme decoratif » au lieu d'ecrire alt="".

**Role pedagogique** : montre que l'accessibilite des images ne se limite pas a « mettre un alt text partout ». Certaines images doivent etre explicitement ignorees.

### Erreur 11 - Fausse liste a puces (Pilier 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| Tirets manuels (- item) tapes au clavier | Liste a puces native (Accueil > Puces) |

Texte : « Objectifs du trimestre : augmenter le trafic de 10 %, publier 3 articles par semaine, reduire le taux de rebond sous 40 % »

Pourquoi : les tirets manuels ne sont pas reconnus comme une liste par le lecteur d'ecran. Il lit « tiret Augmenter... » au lieu de « liste de 3 elements, element 1 sur 3 ».

### Erreur 12 - Fausse liste numerotee (Pilier 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| Numeros tapes a la main (1. 2. 3.) | Liste numerotee native (Accueil > Numerotation) |

Texte : « Priorites pour le prochain trimestre : refonte de la page d'accueil, mise en conformite accessibilite, deploiement de la newsletter »

Pourquoi : meme probleme que les fausses puces. La structure de liste est invisible pour le lecteur d'ecran, la navigation par element est impossible.

### Erreur 13 - Passage anglais sans balisage de langue (pilier 4 - langue)

| Inaccessible | Accessible |
|---|---|
| Phrase en anglais sans balisage de langue | Passage selectionne > Revision > Langue > Definir en anglais |

Texte : « The quarterly report is available upon request. Please contact the communication department for further details. »

Pourquoi : sans balisage, le lecteur d'ecran lit le passage anglais avec la prononciation francaise, ce qui le rend incomprehensible.

**Role pedagogique** : erreur revelee uniquement apres l'enseignement du pilier 4 (slide 37). Cree un effet Zeigarnik : les stagiaires pensaient avoir trouve toutes les erreurs.

### Erreur 14 - Proprietes du document vides (pilier 5 - finalisation)

| Inaccessible | Accessible |
|---|---|
| Proprietes Titre et Auteur vides | Titre : « Rapport trimestriel - Bilan T1 2025 », Auteur : « Sami Dupont » |

Pourquoi : les proprietes du document sont la premiere information lue par un lecteur d'ecran. Sans titre, l'utilisateur ne sait pas ce qu'il ouvre.

**Role pedagogique** : erreur revelee en meme temps que l'erreur 13 apres le pilier 5. Correction en 30 secondes (Fichier > Informations).

### Erreur 15 - Texte justifie (pilier 4 - lisibilite)

| Inaccessible | Accessible |
|---|---|
| Tout le document en texte justifie | Texte aligne a gauche |

Pourquoi : le texte justifie cree des espaces inegaux entre les mots (lezardes) qui rendent la lecture difficile pour les personnes dyslexiques ou malvoyantes.

### Erreur 16 - Paragraphes vides (pilier 4 - lisibilite)

| Inaccessible | Accessible |
|---|---|
| 4 paragraphes vides entre le tableau et les listes | Espacement gere par les styles de paragraphe |

Pourquoi : le lecteur d'ecran lit « vide, vide, vide, vide » a chaque paragraphe vide. L'espacement doit etre gere par les proprietes Avant/Apres du style de paragraphe.

### Erreur 17 - Majuscules tapees au clavier (pilier 4 - lisibilite)

| Inaccessible | Accessible |
|---|---|
| « ANNEXES » tape en majuscules | « Annexes » en minuscules avec propriete Police > Tout en majuscules |

Pourquoi : le lecteur d'ecran peut epeler lettre par lettre les mots en majuscules. La propriete CSS/Word « Tout en majuscules » affiche visuellement en majuscules mais le lecteur lit le mot normalement.

### Erreur 18 - Filigrane invisible (pilier 3 - contenus)

| Inaccessible | Accessible |
|---|---|
| Filigrane « CONFIDENTIEL » (invisible au lecteur d'ecran) | Mention « Document confidentiel » en texte dans le corps |

Pourquoi : les filigranes sont des objets graphiques dans l'en-tete, non lus par les lecteurs d'ecran. Un utilisateur aveugle ne sait pas que le document est confidentiel.

---

## Structure du document (2 pages)

```
[En-tête : Direction des affaires juridiques - Logo fictif]

Rapport trimestriel - Bilan T1 2025          <-- Titre du document (propriétés)

Introduction                                  <-- Erreur 1 : gras Arial 16 au lieu de Titre 1
Paragraphe d'introduction (2-3 phrases sur le contexte du trimestre).

URGENT                                        <-- Erreur 5 : rouge sans gras, sans texte
La direction demande un retour rapide sur les indicateurs.

Résultats du trimestre                        <-- Erreur 2 : gras Arial 14 au lieu de Titre 2
[Tableau 4x4 sans en-tête balisé]            <-- Erreur 4

Détail par canal                              <-- Erreur 3 : gras Arial 12 souligné au lieu de Titre 3
[Graphique barres couleurs seules, sans alt]  <-- Erreur 7 (double : alt + couleurs)

Organisation du service                       <-- Faux titre (gras Arial 14 bleu)
[Organigramme avec alt="image.png"]           <-- Erreur 9

Contact                                       <-- Faux titre (gras Arial 14 bleu)
Pour toute question, contactez-nous par       <-- Erreur 10 : icone enveloppe alt="E-mail"
[icone enveloppe] e-mail pour plus d'infos.
The quarterly report is available upon...     <-- Erreur 11 : anglais sans balisage

Annexes                                       <-- Faux titre (gras Arial 14 bleu)
Pour accéder aux annexes, cliquez ici.        <-- Erreur 8

Note : les données sont provisoires.*         <-- Erreur 6 : gris #767676 (ratio 4,48:1)
```

---

## Déroulement en classe (25 minutes, 3 phases)

### Phase 1 - Identification (10 min)

| Temps | Action |
|---|---|
| 0-2 min | Distribution du fichier `sami-doc-inaccessible.docx`. Consigne : « Trouvez toutes les erreurs d'accessibilité. Notez-les sur une feuille, sans corriger. » |
| 2-10 min | Chaque binôme explore le document et liste les erreurs identifiées |

Pas de checklist distribuée à cette phase. Les stagiaires doivent mobiliser ce qu'ils ont appris.

### Phase 2 - Correction (10 min)

| Temps | Action |
|---|---|
| 10-12 min | Le formateur affiche la liste des 16 erreurs. Les binômes comparent avec leur liste |
| 12-20 min | Chaque binôme corrige les erreurs dans l'ordre prescrit (Pilier 1 puis 2 puis 3) |

Le vérificateur Word est utilisé comme **outil de découverte** (« que détecte-t-il ? que rate-t-il ? »), pas comme preuve de conformité.

### Phase 3 - Restitution et transfert (5 min)

| Temps | Action |
|---|---|
| 20-22 min | Le formateur débrief l'erreur 6 (contraste ambigu) : montrer le CCA, expliquer le seuil 4,5:1 |
| 22-25 min | Question de transfert : « Sur votre dernier document envoyé, laquelle de ces 18 erreurs avez-vous probablement faite ? » Tour de table rapide (1 phrase par binôme) |

La question de transfert est le vrai objectif pédagogique. L'exercice Sami n'est que le véhicule.

---

## Notes techniques pour la création des fichiers

- Police : Marianne (fallback Calibri) pour le document accessible, Arial pour l'inaccessible
- Le graphique sera une image PNG avec barres en vert/rouge/orange sans motif ni étiquette (version inaccessible) et avec motifs + étiquettes (version accessible). Pas un graphique Excel natif, pour garantir la reproductibilité
- Mention URGENT : rouge #FF0000 (ratio 4:1, insuffisant en 1.4.3) dans la version inaccessible, rouge #C00000 (ratio 6,5:1, conforme) dans la version accessible
- Note de bas de page en gris #767676 (ratio 4,48:1 mesurable avec CCA)
- Propriétés du document accessible : titre, auteur, langue fr-FR renseignés
- Langue du document accessible : fr-FR au niveau des métadonnées ET du style Normal (propage à tout le texte). Le document inaccessible reste en anglais (langue par défaut de python-docx) - erreur bonus implicite pour le vérificateur
- Le fichier inaccessible n'a PAS de propriétés renseignées (erreur bonus implicite pour le vérificateur)

---

## Amendements devil council (2026-05-02)

Trois corrections appliquées suite au Devil Council :

1. **Durée rallongée de 15 à 25 min** avec 3 phases distinctes : identification sans aide (10 min), correction guidée (10 min), restitution et transfert (5 min). Corrige le problème du binôme dominant et du temps impossible.

2. **Vérificateur Word repositionné** comme outil de découverte (« que détecte-t-il ? que rate-t-il ? ») au lieu de preuve de conformité. La checklist n'est plus distribuée - les stagiaires identifient d'abord sans filet. Corrige le talisman procédural.

3. **Erreur ambiguë ajoutée** (contraste #767676, ratio 4,48:1) pour forcer le jugement sous incertitude. Seule erreur qui nécessite un outil de mesure. Corrige l'absence de friction cognitive.
