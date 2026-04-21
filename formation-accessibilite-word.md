# Rendre un document Word accessible — guide pratique

Un lecteur d'écran vient de recevoir votre compte rendu de réunion. Il entend ceci :

> « Texte, texte, texte, texte, texte, texte... »

Pendant 4 minutes. Sans titre. Sans repère. Sans pouvoir naviguer vers la section qui le concerne.

C'est ce que vit une personne malvoyante face à un document Word sans structure. Ce n'est pas un cas rare : 15 % de vos destinataires sont concernés, et 80 % de ces handicaps sont invisibles.

---

> **Quiz flash** : Lequel de ces deux documents est accessible pour ce lecteur d'écran ?
> - Document A : titres en **gras Arial 16**, image sans description, nom de fichier « Document1.docx »
> - Document B : titres avec le style « Titre 1 », image avec texte de remplacement, nom « rapport-bilan-2024.docx »
>
> Ils sont visuellement identiques. **Réponse après la prochaine section.**

Ce guide vous donne les 21 réflexes pour passer systématiquement de A à B, sans aucune compétence technique : juste Word et les bons gestes dans le ruban.

*Temps de lecture : 20 minutes. Utilisable en autonomie ou comme support de formation. La checklist en fin de document est le seul outil dont vous aurez besoin au quotidien.*

---

## Pourquoi ça vous concerne

**Réponse au quiz** : Document B. Le style Titre 1 crée une structure de navigation, le texte de remplacement décrit l'image, et le nom de fichier permet à l'utilisateur de retrouver le document. Le Document A est visuellement identique — mais invisible pour un lecteur d'écran.

Dans une réunion de 12 personnes, il y a probablement un daltonien. Parmi vos 30 destinataires habituels, 4 ou 5 ont un handicap — dont la majorité invisible.

Rendre un document accessible, c'est **0 ligne de code** : uniquement des réflexes dans le ruban Word.

---

## 5 piliers, 21 critères

Ce guide suit 5 piliers. Chaque pilier contient des critères actionnables immédiatement.

| Pilier | Critères |
|--------|----------|
| **1. Structure** | Titres, listes, colonnes, tableaux, sauts de page |
| **2. Couleurs** | Contraste, couleur seule insuffisante |
| **3. Contenus** | Images, liens, zones de texte, infos essentielles |
| **4. Langue et lisibilité** | Balisage linguistique, majuscules, espaces, médias |
| **5. Finalisation** | Propriétés, nom de fichier, vérificateur |

---

## Pilier 1 — Structure

### Les styles de titre : le fondement de tout

**Devinez** : Comment un lecteur d'écran repère-t-il les titres dans un document Word ?

Sans les styles de titre, le lecteur d'écran voit ceci :

> Texte, texte, texte, texte, texte, texte, texte...

Un bloc plat, sans aucun repère de navigation.

Avec les styles de titre (Titre 1, Titre 2, Titre 3) :

> Titre 1 : Rapport annuel
> Titre 2 : Budget
> Titre 3 : Prévisions 2025

L'utilisateur navigue par titres en quelques secondes, comme une table des matières interactive.

**Comment faire :**
- Clic sur le titre → Accueil > Styles > choisir Titre 1, Titre 2, Titre 3
- Raccourci pour ouvrir le volet Styles : Ctrl+Alt+Maj+S
- Vérification : Ctrl+F > onglet « Titres » — si les titres y apparaissent, c'est bon

*[Visuel recommandé : capture du volet de navigation Ctrl+F — onglet Titres vide à gauche / rempli à droite]*

**Règle** : commencer par un Titre 1. Ne pas sauter de niveau (pas de Titre 3 après Titre 1).

---

### Listes : puces et numérotation natives

**Inaccessible — tirets manuels :**

```
- Premier élément
- Deuxième élément
```

Le lecteur d'écran lit : « tiret Premier élément » — ce n'est pas une liste.

**Accessible — fonctionnalité de liste :**

Le lecteur d'écran annonce : « liste de 3 éléments, élément 1 sur 3 ».

**Comment faire :** Accueil > Paragraphe > Puces, Numérotation ou Liste à plusieurs niveaux.

Vérification : Maj+F1 (Révéler la mise en forme) > « Puces et numérotation » doit apparaître.

---

### Colonnes, tableaux et sauts de page

**La règle d'or :**

> Si vous touchez à Tab, Espace ou Entrée pour simuler une mise en page, vous créez une barrière invisible pour les technologies d'assistance.

**Tableaux de mise en page** (pour aligner du texte) :
- Insertion > Tableau > choisir le nombre de colonnes et lignes
- Vérifier l'ordre de lecture : Tab dans la 1re cellule, parcourir avec Tab
- Habillage : clic droit > Propriétés > **Habillage = Aucun** (un tableau « Autour » flotte et le lecteur d'écran ne le lit pas au bon moment)

**Tableaux de données** :
- Les tableaux complexes (cellules fusionnées, multi-niveaux d'en-têtes) ne peuvent pas être rendus accessibles dans Word. Solution : exporter en PDF accessible.
- Pour identifier la ligne d'en-tête : onglet Outils de tableau > Création > cocher « Ligne d'en-tête »

**Zones de texte et objets flottants** : un objet flottant (zone de texte, image en habillage « Devant le texte ») est invisible pour le lecteur d'écran ou lu dans un ordre aléatoire. Les éviter — préférer les colonnes intégrées Word ou l'habillage « En ligne avec le texte ».

---

## Pilier 2 — Couleurs

### Contraste : le ratio minimum

Outil gratuit : **Colour Contrast Analyser (CCA)** de TPGi (Windows et macOS).

Méthode en 4 étapes :
1. Ouvrir le CCA
2. Pipette « Premier plan » sur la couleur du texte
3. Pipette « Arrière-plan » sur la couleur du fond
4. Lire le ratio : >= 4,5:1 pour le texte standard, >= 3:1 pour le grand texte (>= 18 pt ou >= 14 pt gras)

**Texte noir sur fond blanc = toujours conforme.** Le test ne s'applique qu'aux textes colorés.

| Avant | Après |
|-------|-------|
| Texte gris clair (#999) sur fond blanc — ratio 2,85:1 — ÉCHEC | Texte gris foncé (#595959) sur fond blanc — ratio 7,0:1 — CONFORME |

---

### La couleur ne suffit jamais

**8 % des hommes sont daltoniens.** Dans une réunion de 12 personnes, il y en a probablement un.

| Inaccessible | Accessible |
|-------------|-----------|
| Statut : rouge / vert / jaune (couleur seule) | Statut : En retard / Terminé / En cours (texte + couleur) |

**Règle** : le texte porte l'information, la couleur la renforce.

---

## Pilier 3 — Contenus

### Texte alternatif sur les images

**Comment faire :**
1. Clic droit sur l'image > Format de l'image > Texte de remplacement
2. Image significative : décrire la **fonction**, pas l'apparence
3. Image décorative : cocher « Marquer comme décoratif » (ou laisser le champ Description vide avec des espaces)

*[Visuel recommandé : capture du volet « Texte de remplacement » Word — champ Description rempli vs case « Marquer comme décoratif »]*

| Mauvais texte alt | Bon texte alt |
|------------------|--------------|
| « Photo d'un graphique en barres colorées » | « Chiffre d'affaires 2020-2024 : hausse de 15 % à 23 % » |
| « Logo de l'entreprise » | « » (décoratif — laisser vide) |

**Qu'est-ce qu'un objet décoratif ?** Filets, séparateurs, icônes purement visuelles, images d'ambiance qui n'apportent aucune information que le texte ne contient pas déjà. Les marquer comme décoratifs évite que le lecteur d'écran annonce « Image, image, séparateur... » en interrompant la lecture du contenu.

---

### Liens descriptifs

| Inaccessible | Accessible |
|-------------|-----------|
| « Cliquez ici » | « Consulter le guide d'accessibilité Word » |
| « En savoir plus » | « Télécharger le rapport annuel 2024 (PDF, 2 Mo) » |
| URL brute | « Accéder au formulaire de contact » |

Pour les liens de téléchargement, intégrer : titre + format + poids + langue si elle diffère.

**Comment faire :** sélectionner le texte descriptif > clic droit > Lien hypertexte (Ctrl+K).

---

### Informations essentielles invisibles

Les technologies d'assistance **ne lisent pas automatiquement** :
- En-têtes de page
- Pieds de page
- Filigranes

Si une information est essentielle (« CONFIDENTIEL », « BROUILLON — Ne pas diffuser », « Répondre avant le 15 avril »), **reproduire cette information dans le corps du document.**

---

## Exercice cross-piliers : les erreurs de Karine

Karine, chargée de communication, envoie son rapport trimestriel à 40 personnes. Il contient :
- Un titre « Introduction » en gras Arial 16
- Un graphique de résultats sans description
- La mention « URGENT » écrite uniquement en rouge dans le corps du texte
- Un lien « cliquez ici pour les annexes »

**Quels piliers sont concernés ? Quelles corrections, dans quel ordre ?**

*Réponse :*
- *Pilier 1 — Appliquer le style Titre 1 sur « Introduction »*
- *Pilier 2 — Doubler « URGENT » en texte : « URGENT — Répondre avant le 15 mai »*
- *Pilier 3 — Texte alt sur le graphique : « Résultats T1 2025 : hausse de 12 % » + renommer le lien en « Consulter les annexes du rapport T1 »*

*3 piliers, 4 corrections, 6 minutes.*

---

## Pilier 4 — Langue et lisibilité

### Balisage de langue

Sans balisage, le lecteur d'écran prononce « meeting » comme « mé-é-ting ».

- Langue principale : Fichier > Options > Langue
- Passage étranger : sélectionner le texte > Révision > Langue > Définir la langue de vérification

---

### Majuscules et acronymes

**Les textes en majuscules posent deux problèmes :**
1. Difficiles à lire pour les dyslexiques
2. Prononciation ambiguë par les lecteurs d'écran (« UN INTERNE TUE ! » se prononce comme une phrase, pas comme des mots en majuscules)

**Solution :** écrire en minuscule et appliquer une mise en forme majuscule : Accueil > Police > Modifier la casse > MAJUSCULES.

**Acronymes et abréviations :** expliciter à la première occurrence dans le document.

> Exemple : DGFiP (Direction générale des finances publiques)

---

### Lisibilité du texte

Ces réglages concernent tous les lecteurs, pas seulement ceux qui utilisent des technologies d'assistance :

- **Police** : sans sérif (Arial, Calibri) — plus lisible à l'écran
- **Taille minimale** : 12 pt
- **Interligne** : 1,15 minimum, 1,5 si possible
- **Justification** : ne pas justifier — crée des espaces irréguliers difficiles à suivre

---

### Gestion des espaces et formatage

Activer les marques de formatage : Accueil > Paragraphe > Afficher tout (¶).

Repérer et supprimer :
- Espaces successifs (points au lieu d'un seul espace)
- Tabulations utilisées pour simuler une mise en page
- Retours à la ligne manuels au lieu de sauts de page propres

---

**Objets clignotants : tolérance zéro.** Animations, GIF avec flashs, vidéos > 3 Hz — interdit sans exception. Risque de crise d'épilepsie. En cas de doute sur un GIF : remplacez-le par une image statique.

---

## Pilier 5 — Avant de publier

Ces 5 vérifications prennent 2 minutes et attrapent 80 % des oublis restants.

| # | Quoi vérifier | Où |
|---|--------------|-----|
| 1 | **Propriétés** (Titre, Auteur, Objet) | Fichier > Informations > Propriétés |
| 2 | **Nom de fichier** descriptif en .docx | Lors de l'enregistrement |
| 3 | **Protection** : aucune restriction | Révision > Restreindre |
| 4 | **Formulaires** : aucun champ Word | — |
| 5 | **Vérificateur d'accessibilité** | Fichier > Vérifier l'accessibilité |

---

### Le vérificateur : allié imparfait

| Ce qu'il détecte | Ce qu'il ne détecte PAS |
|-----------------|------------------------|
| Texte alt manquant | Qualité du texte alt |
| Styles de titre absents | Pertinence des noms de liens |
| Ordre de lecture | Couleur porteuse de sens seule |
| Tableaux sans en-tête | Langue des passages étrangers |
| — | Contraste insuffisant |

**Le vérificateur est un premier filtre, pas un certificat de conformité.**

---

### Export PDF accessible

Si votre document final doit être en PDF, l'export doit conserver les balises de structure :

Fichier > Exporter > Créer PDF/XPS > Options :
- Cocher « Créer des signets à l'aide de titres »
- Cocher « Propriétés du document »
- Cocher « Balises de structure de document »

---

## Étude de cas : le compte rendu de Sophie

Sophie, assistante de direction, doit publier un compte rendu de réunion.

**Son document contient :**
- 3 niveaux de titres mis en **gras manuellement**
- 2 tableaux avec la 1re ligne en gras (sans ligne d'en-tête identifiée)
- 1 organigramme sans texte alternatif
- 1 lien « cliquez ici pour le formulaire »
- Le filigrane « CONFIDENTIEL »

**Erreurs à corriger :**
1. Remplacer le gras manuel par les styles Titre 1, Titre 2, Titre 3
2. Identifier la ligne d'en-tête dans chaque tableau (onglet Création > Ligne d'en-tête)
3. Ajouter un texte alt sur l'organigramme : « Organigramme du service — 4 équipes »
4. Renommer le lien : « Accéder au formulaire de demande »
5. Ajouter « CONFIDENTIEL » en première ligne du document

**Temps estimé : 8 minutes.**

---

## Par où commencer ?

Le quadrant haut-gauche : effort faible, impact fort.

| | Effort faible | Effort élevé |
|---|---|---|
| **Impact fort** | Styles de titre + Texte alt + Nom de fichier + Vérificateur | Retravailler un document existant entier |
| **Impact faible** | Propriétés (Titre, Auteur) | Corriger le contraste sur des centaines de pages |

**Commencez par les 4 actions à effort faible :**
1. Styles de titre sur tous les titres
2. Texte alt sur chaque image
3. Lancer le vérificateur d'accessibilité
4. Vérifier les propriétés du document

---

## Quiz final : trouvez les 5 erreurs

Un document Word contient :
1. Un titre « Introduction » mis en gras Arial 16 (sans style)
2. Un tableau de 3 colonnes avec la 1re ligne en gras (sans « Ligne d'en-tête »)
3. Un lien « cliquez ici pour le formulaire »
4. Un filigrane « PROJET » sans mention dans le corps du document
5. Une photo de l'équipe sans texte alternatif

**Réponses** : 5 erreurs — une par point.
1. Appliquer le style Titre 1
2. Activer la ligne d'en-tête (onglet Création)
3. Renommer en « Accéder au formulaire de demande RH »
4. Ajouter « PROJET » en première ligne du document
5. Ajouter le texte alt : « Équipe du service communication, 8 personnes »

---

## Faites le point

Avant de regarder la réponse, notez sans relire :

1. La règle la plus importante pour les lecteurs d'écran : _______________
2. La vérification à faire en 30 secondes sur n'importe quel document : _______________
3. Le geste que vous ferez dès demain sur votre prochain document : _______________

*Si vous avez répondu « styles de titre », « Ctrl+F > onglet Titres » et « vérifier le texte alternatif » — vous avez retenu l'essentiel. Sinon, relisez les piliers 1 et 3 avant de continuer.*

---

## Demain à 9h

**Quelle est la première chose que vous ferez sur votre prochain document Word ?**

**Réflexe 1** — Ctrl+F > onglet Titres : vérifier que tous les titres apparaissent dans le volet de navigation.

**Réflexe 2** — Clic droit > Texte de remplacement : décrire la fonction de chaque image.

**Réflexe 3** — Fichier > Vérifier l'accessibilité : corriger les erreurs avant d'envoyer.

---

## Checklist : vos 21 critères

### Structure et couleurs

- [ ] 1. Fichier .docx + nom descriptif (pas « Document1 »)
- [ ] 2. Document non protégé
- [ ] 3. Titres avec styles intégrés (pas du gras manuel)
- [ ] 4. Hiérarchie des titres cohérente (pas de saut de niveau)
- [ ] 5. Listes avec Puces/Numérotation (pas de tirets manuels)
- [ ] 6. Colonnes intégrées (pas de tabulations pour simuler)
- [ ] 7. Sauts de page propres (pas de retours à la ligne répétés)
- [ ] 8. Tableaux de mise en page avec habillage « Aucun »
- [ ] 9. Tableaux de données avec ligne d'en-tête identifiée
- [ ] 10. Contraste >= 4,5:1 pour le texte standard, >= 3:1 pour grand texte
- [ ] 11. Couleur doublée en texte (jamais la couleur seule comme information)

### Contenus, langue, finalisation

- [ ] 12. Texte alt sur toutes les images significatives / décoratifs marqués
- [ ] 13. Pas de zones de texte flottantes
- [ ] 14. Liens descriptifs (pas « cliquez ici »)
- [ ] 15. Infos essentielles reproduites dans le corps (pas seulement en filigrane)
- [ ] 16. Langue principale balisée dans les propriétés
- [ ] 17. Passages en langue étrangère balisés
- [ ] 18. Aucun objet clignotant
- [ ] 19. Propriétés renseignées (Titre, Auteur, Objet)
- [ ] 20. Aucun formulaire Word interactif
- [ ] 21. Vérificateur d'accessibilité sans erreur résiduelle

---

## Revenez dans 7 jours

Refaites le quiz final sans rouvrir ce guide. Notez combien d'erreurs vous trouvez parmi les 5.

- **5/5** — les réflexes sont installés. Passez à la checklist sur un vrai document.
- **3-4/5** — relisez les piliers correspondant aux erreurs manquées.
- **< 3/5** — reprenez les piliers 1 et 3, qui couvrent 80 % des cas.

À J+30 : ouvrez votre prochain document Word et parcourez la checklist de haut en bas. C'est le seul test qui compte.

---

## Métadonnées pédagogiques

**Règles appliquées :** 1 (quiz flash ouverture), 2 (primauté/récence), 3 (WIIFM), 4 (charge cognitive réduite — sections orphelines fusionnées), 5 (chunking — 5 piliers), 7 (storytelling — Sophie + Karine), 8 (analogies — bloc plat, table des matières interactive, barrière invisible), 9 (émotion — narratif lecteur d'écran en ouverture), 10 (Zeigarnik — réponse quiz différée), 11 (prédictions — « Devinez », quiz flash, quiz final), 12 (récupération active — quiz final + « Faites le point »), 13 (répétitions espacées — parcours J1/J+7/J+30 section « Revenez dans 7 jours »), 14 (interleaving — exercice Karine cross-piliers 1+2+3), 15 (jargon traduit), 16 (tableaux avant/après systématiques), 17 (variation stimuli — narrative/quiz/tableau/règle d'or/cas/métacognition), 19 (feedback immédiat), 21 (scaffolding — pilier 1 fondements → pilier 5 vérification + quadrant impact/effort corrigé), 24 (plan d'action — « Demain à 9h »), 25 (métacognition — « Faites le point » avant le plan d'action), 26 (transformation — phrase-clé à 6 mois)

**Avant/Après :**
- Avant : « cliquez ici » → Après : « Accéder au formulaire de demande RH »
- Avant : tirets manuels → Après : listes natives (annonce « liste de 3 éléments, élément 1 sur 3 »)

**Score pédagogique :** 22 règles appliquées sur 26 (hors présentiel uniquement : 22/22)

**Phrase-clé à 6 mois :** « Titres avec styles, images avec texte alt, vérificateur avant d'envoyer. »

**Verdict :** `[★]` Transformatif — émotion incarnée, Zeigarnik, interleaving Karine, métacognition avant plan d'action, répétitions espacées J1/J+7/J+30
