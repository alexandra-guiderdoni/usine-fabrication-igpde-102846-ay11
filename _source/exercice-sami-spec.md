# Exercice « Les erreurs de Sami » - Spécification

Formation 102638 - Support de la slide 32.
Amendé suite au Devil Council du 2026-05-02.

---

## Contexte pédagogique

Sami, chargé de communication à la Direction des affaires juridiques, envoie son rapport trimestriel « Bilan T1 2025 » à 40 destinataires. Le document mobilise 21 critères d'accessibilité couvrant les 5 thèmes, avec parfois plusieurs occurrences d'un même problème. Une erreur ambiguë force le jugement. Les critères des thèmes 4 et 5 sont révélés après l'enseignement de ces thèmes (slide 37, effet Zeigarnik).

- **Public** : communicants, niveau initiation
- **Format** : exercice en binôme, 25 minutes (3 phases)
- **Modalité** : identifier d'abord, corriger ensuite, discuter en restitution
- **Livrables** : `tp-doc-inaccessible.docx` + `tp-doc-aide-correction.docx` + `tp-doc-accessible.docx`

---

## Les 21 critères et leurs corrections

Les 21 entrées ci-dessous sont des **critères à vérifier**, pas un comptage strict d'occurrences. Un même critère peut apparaître plusieurs fois dans le document, par exemple les faux titres visuels. En animation, on valorise donc la bonne catégorie d'erreur et la correction proposée, sans piéger les stagiaires sur un nombre exact d'anomalies.

Ordre de correction prescrit : Structure (thème 1) puis Couleurs (thème 2) puis Contenus (thème 3).

### Critère 1 - Faux Titre 1 (Thème 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| « Introduction » en **gras Arial 16** (formatage direct) | « Introduction » avec le **style Titre 1** natif Word |

Pourquoi : sans style, le lecteur d'écran voit un bloc plat sans repère de navigation.

### Critère 2 - Faux Titre 2 (Thème 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| « Résultats du trimestre » en **gras Arial 14** (formatage direct) | « Résultats du trimestre » avec le **style Titre 2** natif Word |

Pourquoi : la hiérarchie ne se limite pas au titre principal. Un sous-titre non balisé casse la navigation par niveaux.

### Critère 3 - Faux Titre 3 (Thème 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| « Détail par canal » en **gras Arial 12 souligné** (formatage direct) | « Détail par canal » avec le **style Titre 3** natif Word |

Pourquoi : le soulignement donne un indice visuel mais aucun indice sémantique. Le lecteur d'écran ne distingue pas ce sous-titre du texte courant.

### Critère 4 - Tableau sans en-tête (Thème 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| Tableau de résultats sans ligne d'en-tête identifiée | Onglet Création > cocher **Ligne d'en-tête** |

Contenu du tableau :

| Indicateur | T4 2024 | T1 2025 | Évolution |
|---|---|---|---|
| Visiteurs uniques | 45 200 | 50 600 | +12 % |
| Pages vues | 128 000 | 142 000 | +11 % |
| Taux de rebond | 42 % | 38 % | -4 pts |

Pourquoi : sans en-tête balisé, le lecteur d'écran ne peut pas associer chaque cellule à sa colonne.

### Critère 5 - Couleur seule (Thème 2 - Couleurs)

| Inaccessible | Accessible |
|---|---|
| URGENT en rouge (sans gras, sans autre indication) | **URGENT - Retour attendu avant le 30 juin 2025** (gras + texte explicatif + couleur) |

Pourquoi : sans gras et sans texte complémentaire, la seule distinction est la couleur rouge. Une personne daltonienne ou utilisant un écran monochrome ne perçoit aucune urgence — le mot se fond dans le texte courant. Illustration pure du critère WCAG 1.4.1.

### Critère 6 - Contraste ambigu (Thème 2 - Couleurs)

| Inaccessible | Accessible |
|---|---|
| Note de bas de page en **gris #767676 sur fond blanc** (ratio 4,48:1 - insuffisant pour du texte normal) | Texte en **gris #595959** (ratio 7:1) ou en noir |

Pourquoi : le ratio 4,48:1 est en dessous du seuil 4,5:1 pour le texte normal (WCAG 1.4.3). L'erreur est subtile : le texte semble lisible mais échoue de justesse au test. C'est l'erreur ambiguë qui force le jugement - les stagiaires doivent mesurer, pas deviner.

**Rôle pédagogique** : cette erreur n'a pas de réponse évidente visuellement. Elle oblige à utiliser un outil de mesure (CCA ou vérificateur) et à trancher sous incertitude. C'est la seule erreur que le formateur doit explicitement débriefer.

### Critère 7 - Image sans alternative + couleurs seules (Thème 3 + Thème 2)

| Inaccessible | Accessible |
|---|---|
| Graphique sans texte alternatif, barres différenciées uniquement par la couleur (vert/rouge/orange, sans motif ni étiquette) | Alt text : « Graphique d'évolution du trafic web T1 2025 : visiteurs uniques en hausse de 12 %, pages vues +11 %, taux de rebond en baisse de 4 points ». Barres avec motifs distincts (hachures, points, plein) + étiquettes sur chaque barre |

Pourquoi : double erreur. (1) Le lecteur d'écran annonce « image » sans description. (2) Même pour un voyant daltonien, les barres vert/rouge/orange sont indiscernables sans motif ni légende textuelle. Ce graphique est inutilisable pour ~8 % de la population masculine.

**Rôle pédagogique** : montre que l'accessibilité d'une image ne se limite pas à l'alt text — le contenu visuel lui-même doit être lisible sans couleur.

### Critère 8 - Lien non descriptif (Thème 3 - Contenus)

| Inaccessible | Accessible |
|---|---|
| « cliquez ici » pour les annexes | « Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo) » |

Pourquoi : « cliquez ici » ne donne aucune information hors contexte visuel. Le lecteur d'écran liste les liens par intitulé.

### Critère 9 - Organigramme avec alt inadapté (Thème 3 - Contenus)

| Inaccessible | Accessible |
|---|---|
| Organigramme avec alt="image.png" (nom de fichier par défaut) | alt="Organigramme de la Direction des affaires juridiques (description ci-dessous)." + description textuelle détaillée sous l'image |

Pourquoi : le nom de fichier ne donne aucune information. Pour une image complexe (RGAA 1.6 et 1.7), l'alt doit rester court (~80 caractères) et renvoyer vers une description détaillée présente dans le document. Ne pas tout mettre dans l'alt.

**Rôle pédagogique** : montre la différence entre image simple (alt descriptif) et image complexe (alt court + description adjacente). Illustre aussi le piège du nom de fichier automatique.

### Critère 10 - Icône redondante avec alt non vide (Thème 3 - Contenus)

| Inaccessible | Accessible |
|---|---|
| Icône enveloppe avec alt="E-mail" (redondant avec le texte adjacent) | Icône marquée comme décorative (case « Marquer comme décoratif » cochée) |

Pourquoi : l'icône est placée juste à côté du mot « e-mail ». Si on écrit « E-mail » dans l'alternative, le lecteur d'écran lit « E-mail, e-mail » — redondance qui pollue la lecture. Toute image qui n'apporte pas d'information supplémentaire doit être ignorée. Dans Word, on coche « Marquer comme décoratif » au lieu d'écrire alt="".

**Rôle pédagogique** : montre que l'accessibilité des images ne se limite pas à « mettre un alt text partout ». Certaines images doivent être explicitement ignorées.

### Critère 11 - Fausse liste à puces (Thème 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| Puces tapées au clavier et indentées manuellement | Liste à puces native (Accueil > Puces) |

Texte : « Objectifs du trimestre : augmenter le trafic de 10 %, publier 3 articles par semaine, réduire le taux de rebond sous 40 % »

Pourquoi : les puces tapées et les retraits manuels donnent l'illusion visuelle d'une vraie liste, mais ne sont pas reconnus comme une liste par le lecteur d'écran. Il lit chaque ligne comme un paragraphe ordinaire au lieu de « liste de 3 éléments, élément 1 sur 3 ».

### Critère 12 - Fausse liste numérotée (Thème 1 - Structure)

| Inaccessible | Accessible |
|---|---|
| Numéros tapés à la main (1. 2. 3.) et indentés manuellement | Liste numérotée native (Accueil > Numérotation) |

Texte : « Priorités pour le prochain trimestre : refonte de la page d'accueil, mise en conformité accessibilité, déploiement de la newsletter »

Pourquoi : même problème que les fausses puces. La numérotation semble correcte visuellement, mais la structure de liste est invisible pour le lecteur d'écran et la navigation par élément est impossible.

### Critère 13 - Passage anglais sans balisage de langue (thème 4 - langue)

| Inaccessible | Accessible |
|---|---|
| Phrase en anglais sans balisage de langue | Passage sélectionné > Révision > Langue > Définir en anglais |

Texte : « The quarterly report is available upon request. Please contact the communication department for further details. »

Pourquoi : sans balisage, le lecteur d'écran lit le passage anglais avec la prononciation française, ce qui le rend incompréhensible.

**Rôle pédagogique** : critère révélé uniquement après l'enseignement du thème 4 (slide 37). Crée un effet Zeigarnik : les stagiaires pensaient avoir trouvé toutes les catégories de problèmes.

### Critère 14 - Propriétés du document vides (thème 5 - finalisation)

| Inaccessible | Accessible |
|---|---|
| Propriétés Titre et Auteur vides | Titre : « Rapport trimestriel - Bilan T1 2025 », Auteur : « Sami Dupont » |

Pourquoi : les propriétés du document sont la première information lue par un lecteur d'écran. Sans titre, l'utilisateur ne sait pas ce qu'il ouvre.

**Rôle pédagogique** : erreur révélée en même temps que l'erreur 13 après le thème 5. Correction en 30 secondes (Fichier > Informations).

### Critère 15 - Texte justifié (thème 4 - lisibilité)

| Inaccessible | Accessible |
|---|---|
| Tout le document en texte justifié | Texte aligné à gauche |

Pourquoi : le texte justifié crée des espaces inégaux entre les mots (lézardes) qui rendent la lecture difficile pour les personnes dyslexiques ou malvoyantes.

### Critère 16 - Paragraphes vides (thème 4 - lisibilité)

| Inaccessible | Accessible |
|---|---|
| 4 paragraphes vides entre le tableau et les listes | Espacement géré par les styles de paragraphe |

Pourquoi : le lecteur d'écran lit « vide, vide, vide, vide » à chaque paragraphe vide. L'espacement doit être géré par les propriétés Avant/Après du style de paragraphe.

### Critère 17 - Majuscules tapées au clavier (thème 4 - lisibilité)

| Inaccessible | Accessible |
|---|---|
| « ANNEXES » tapé en majuscules | « Annexes » en minuscules avec propriété Police > Tout en majuscules |

Pourquoi : le lecteur d'écran peut épeler lettre par lettre les mots en majuscules. La propriété CSS/Word « Tout en majuscules » affiche visuellement en majuscules mais le lecteur lit le mot normalement.

### Critère 18 - Filigrane invisible (thème 3 - contenus)

| Inaccessible | Accessible |
|---|---|
| Filigrane « CONFIDENTIEL » (invisible au lecteur d'écran) | Mention « Document confidentiel » en texte dans le corps |

Pourquoi : les filigranes sont des objets graphiques dans l'en-tête, non lus par les lecteurs d'écran. Un utilisateur aveugle ne sait pas que le document est confidentiel.

### Critère 19 - Faux sommaire tapé à la main (thème 1 - structure)

| Inaccessible | Accessible |
|---|---|
| Sommaire avec points de suite tapés manuellement et numéros de page en dur | Table des matières automatique générée depuis les styles de titre |

Pourquoi : un sommaire tapé à la main n'est pas lié aux titres du document. Il ne se met pas à jour, n'est pas navigable et le lecteur d'écran ne peut pas sauter directement à une section.

### Critère 20 - Texte sous forme d'image (thème 3 - contenus)

| Inaccessible | Accessible |
|---|---|
| Avis important inséré comme image (capture d'écran) | Même contenu en vrai texte dans le document |

Texte : « Avis important : les indicateurs du T2 2025 seront transmis avant le 15 septembre 2025. »

Pourquoi : le texte dans une image ne peut pas être lu par la synthèse vocale, ni agrandi proprement, ni sélectionné, ni recherché. Il faut toujours saisir le texte directement dans Word, sauf pour les logos.

### Critère 21 - Tableau avec cellules fusionnées (thème 1 - structure)

| Inaccessible | Accessible |
|---|---|
| Tableau en grille avec première ligne fusionnée sur 3 colonnes, libellés en gras seulement visuels, sans option Word **Ligne d'en-tête** | Tableau simple en grille sans fusion, avec option Word **Ligne d'en-tête** cochée |

Pourquoi : les cellules fusionnées cassent la logique de lecture des aides techniques. Le lecteur d'écran ne peut plus associer chaque cellule à sa colonne. Des libellés en gras ne suffisent pas : il faut une structure simple et une ligne d'en-tête déclarée dans Word.

---

## Structure du document

```
[En-tête : Direction des affaires juridiques - Rapport trimestriel T1 2025]

Rapport trimestriel - Bilan T1 2025          <-- Titre du document (propriétés)

Introduction                                  <-- Critère 1 : gras Arial 16 au lieu de Titre 1
Paragraphe d'introduction (2-3 phrases sur le contexte du trimestre).

URGENT                                        <-- Critère 5 : rouge sans gras, sans texte
La direction demande un retour rapide sur les indicateurs.

Résultats du trimestre                        <-- Critère 2 : gras Arial 14 au lieu de Titre 2
[Tableau 4x4 sans en-tête balisé]            <-- Critère 4

Détail par canal                              <-- Critère 3 : gras Arial 12 souligné au lieu de Titre 3
[Graphique barres couleurs seules, sans alt]  <-- Critère 7 (double : alt + couleurs)

Organisation du service                       <-- Faux titre (gras Arial 14 bleu)
[Organigramme avec alt="image.png"]           <-- Critère 9

Contact                                       <-- Faux titre (gras Arial 14 bleu)
Pour toute question, contactez-nous par       <-- Critère 10 : icône enveloppe alt="E-mail"
[icone enveloppe] e-mail pour plus d'infos.
The quarterly report is available upon...     <-- Critère 13 : anglais sans balisage

Annexes                                       <-- Faux titre (gras Arial 14 bleu)
Pour accéder aux annexes, cliquez ici.        <-- Critère 8

Note : les données sont provisoires.*         <-- Critère 6 : gris #767676 (ratio 4,48:1)
```

---

## Déroulement en classe (25 minutes, 3 phases)

### Phase 1 - Identification (10 min)

| Temps | Action |
|---|---|
| 0-2 min | Distribution du fichier `tp-doc-inaccessible.docx`. Consigne : « Identifiez les critères d'accessibilité qui posent problème. Notez-les sur une feuille, sans corriger. » |
| 2-10 min | Chaque binôme explore le document et liste les problèmes identifiés |

Pas de checklist distribuée à cette phase. Les stagiaires doivent mobiliser ce qu'ils ont appris.

### Phase 2 - Correction (10 min)

| Temps | Action |
|---|---|
| 10-12 min | Le formateur peut distribuer `tp-doc-aide-correction.docx` si le groupe a besoin d'un guidage. Les commentaires Word expliquent le problème, l'impact et la méthode, sans corriger le document. |
| 12-20 min | Chaque binôme corrige les problèmes dans l'ordre prescrit (thème 1 puis 2 puis 3) |

Le vérificateur Word est utilisé comme **outil de découverte** (« que détecte-t-il ? que rate-t-il ? »), pas comme preuve de conformité.
La version d'aide à la correction reste volontairement fautive : elle sert de support de remédiation guidée, pas de corrigé.

### Phase 3 - Restitution et transfert (5 min)

| Temps | Action |
|---|---|
| 20-22 min | Le formateur débrief le critère 6 (contraste ambigu) : montrer le CCA, expliquer le seuil 4,5:1 |
| 22-25 min | Question de transfert : « Sur votre dernier document envoyé, lequel de ces 21 critères avez-vous probablement oublié ? » Tour de table rapide (1 phrase par binôme) |

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
- En-tête : les deux versions contiennent « Direction des affaires juridiques - Rapport trimestriel T1 2025 ». C'est un repere de page, pas le substitut aux propriétés du document.
- Pied de page : les deux versions contiennent le nom du document suivi de champs Word natifs `PAGE` et `NUMPAGES` : « Rapport trimestriel - Bilan T1 2025 - Page X / Y ». Les valeurs affichées peuvent rester à `1 / 1` tant que Word n'a pas recalculé les champs.
- Mention urgente accessible : le gras est volontaire. Il ajoute une emphase textuelle pour que l'information d'urgence ne repose pas uniquement sur la couleur rouge.
- Audit automatique : les paragraphes sans texte qui portent une image peuvent être signalés comme « paragraphes vides » dans le DOCX accessible. Ce sont des faux positifs acceptables ; le critère 16 vise les paragraphes réellement vides utilisés comme espaceurs dans la version inaccessible.
- Audit automatique : l'icône e-mail de la version accessible est marquée décorative dans le XML Office. Un audit qui ne lit que l'attribut `descr` peut la signaler à tort comme image sans alternative ; elle ne doit pas être comptée comme une erreur.

---

## Amendements devil council (2026-05-02)

Trois corrections appliquées suite au Devil Council :

1. **Durée rallongée de 15 à 25 min** avec 3 phases distinctes : identification sans aide (10 min), correction guidée (10 min), restitution et transfert (5 min). Corrige le problème du binôme dominant et du temps impossible.

2. **Vérificateur Word repositionné** comme outil de découverte (« que détecte-t-il ? que rate-t-il ? ») au lieu de preuve de conformité. La checklist n'est plus distribuée - les stagiaires identifient d'abord sans filet. Corrige le talisman procédural.

3. **Erreur ambiguë ajoutée** (contraste #767676, ratio 4,48:1) pour forcer le jugement sous incertitude. Seule erreur qui nécessite un outil de mesure. Corrige l'absence de friction cognitive.
