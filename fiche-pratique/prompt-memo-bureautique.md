# Prompt de production : Memo Word + Memo LibreOffice Writer

Formation 102846 (IGPDE / Carinne C.) - Fiches annexes distribuees separement

---

## Contexte

La formation "Accessibilite numerique pour les communicants" (1 jour, 131 slides PPTX) porte principalement sur Word. Les stagiaires recoivent en complement **deux fiches memo PDF accessibles** :
- **Memo Word** : aide-memoire des manipulations Word pour l'accessibilite
- **Memo LibreOffice Writer** : equivalent pour les agents qui utilisent LibreOffice

Ces memos sont distribues apres la formation comme reference. Ils ne remplacent pas les slides ni l'exercice Sami - ils permettent de retrouver rapidement la procedure quand le stagiaire est de retour a son poste.

---

## Sources disponibles

### PPTX sources (contenu + captures)

| Fichier | Slides | Images | Role |
|---------|--------|--------|------|
| `fiche-pratique/IGPDE-2024-11-25_Charges_Com-Seq6-Bureautique-v2.pptx` | 57 | 64 PNG dans `/tmp/pptx-bureautique-images/` | Support cours Word+Writer, 11 exercices |
| `fiche-pratique/L'accessibilite numerique - Travaux pratique - deuxieme partie.pptx` | 24 | 50 PNG dans `/tmp/pptx-tp-images/` | Pas-a-pas visuel Word+Writer |

### Exercice de Sami (alignement pédagogique)

| Fichier | Role |
|---------|------|
| `_source/exercice-sami-spec.md` | 21 criteres en 5 themes - structure de reference des memos |

### Cartographie des 21 criteres Sami et slides sources

| # | Critere | Theme Sami | Slides Bureautique | Slides TP |
|---|---------|------------|-------------------|-----------|
| 1 | Faux Titre 1 (gras au lieu de style) | Structure | 8-10, 12-13 | 9-10 |
| 2 | Faux Titre 2 | Structure | 8-10, 12-13 | 9-10 |
| 3 | Faux Titre 3 | Structure | 8-10, 12-13 | 9-10 |
| 4 | Tableau sans en-tete | Structure | 20-21 | 21 |
| 5 | Couleur seule (URGENT rouge) | Couleurs | 44 | 3 |
| 6 | Contraste ambigu (#767676) | Couleurs | 41-43 | 3 |
| 7 | Image sans alt + couleurs seules | Contenus + Couleurs | 47-50 | 4-5 |
| 8 | Lien non descriptif ("cliquez ici") | Contenus | 35-38 | 16 |
| 9 | Organigramme avec alt inadapte | Contenus | 47-50 | 4-5 |
| 10 | Icone redondante avec alt non vide | Contenus | 47-50 | 4-5 |
| 11 | Fausse liste a puces | Structure | 18-19 | 14 |
| 12 | Fausse liste numerotee | Structure | 18-19 | 14 |
| 13 | Passage anglais sans balisage | Langue | 31-32 | 8 |
| 14 | Proprietes du document vides | Finalisation | 5-7 | 6-7 |
| 15 | Texte justifie | Lisibilite | 27 | 17 |
| 16 | Paragraphes vides | Lisibilite | 23-25 | 15 |
| 17 | Majuscules tapees au clavier | Lisibilite | 28-29 | - |
| 18 | Filigrane invisible | Contenus | - | - |
| 19 | Faux sommaire tape a la main | Structure | 16-17 | 13 |
| 20 | Texte sous forme d'image | Contenus | 47-50 | - |
| 21 | Tableau cellules fusionnees | Structure | 20-22 | 21 |

---

## Structure commune des deux memos

### Page de couverture (page 1)

- Titre : "Memo accessibilite - [Word / LibreOffice Writer]"
- Sous-titre : "Aide-memoire des bonnes pratiques"
- Logo IGPDE + DSFR
- Mention : "Formation 102846 - Accessibilite numerique pour les communicants"
- Date : juin 2026

### Organisation par les 5 themes Sami (pages 2 a 7-8)

Chaque theme occupe 1 a 2 pages. Pour chaque critere dans le theme :

```
[Numero] [Nom du critere]
-----------------------------------------
Erreur typique : [description courte]
Impact : [ce que vit l'utilisateur en situation de handicap - 1 phrase]
Procedure :
  [Icone menu] Chemin > Menu > Action
  [Capture d'ecran recadree si pertinente]
```

#### Theme 1 - Structure (criteres 1-4, 11-12, 19, 21) - 2 pages

- Criteres 1-3 : Styles de titre (Titre 1/2/3 au lieu de gras)
- Critere 4 : Tableau avec en-tete declare
- Critere 11 : Listes a puces natives
- Critere 12 : Listes numerotees natives
- Critere 19 : Table des matieres automatique
- Critere 21 : Tableaux sans fusion de cellules

#### Theme 2 - Couleurs (criteres 5-6, partie du 7) - 1 page

- Critere 5 : Information non vehiculee par la couleur seule
- Critere 6 : Contraste minimum (ratio 4,5:1 texte normal, 3:1 grand texte)
- Critere 7 (volet couleur) : Graphiques avec motifs + etiquettes

#### Theme 3 - Contenus (criteres 7-10, 18, 20) - 1 a 2 pages

- Critere 7 (volet image) : Alternative textuelle des images informatives
- Critere 8 : Liens explicites (pas "cliquez ici")
- Critere 9 : Images complexes (alt court + description adjacente)
- Critere 10 : Images decoratives (marquer comme decoratif)
- Critere 18 : Filigrane = pas lu par le lecteur d'ecran
- Critere 20 : Jamais de texte sous forme d'image

#### Theme 4 - Langue et lisibilite (criteres 13, 15-17) - 1 page

- Critere 13 : Balisage de langue pour les passages en langue etrangere
- Critere 15 : Alignement a gauche (pas de justification)
- Critere 16 : Espacement par les styles, pas par les paragraphes vides
- Critere 17 : Majuscules via la mise en forme, pas au clavier

#### Theme 5 - Finalisation (critere 14 + export) - 1 page

- Critere 14 : Proprietes du document (titre, auteur, langue)
- Bonus : Verification de l'accessibilite avec l'outil integre
- Bonus : Export PDF accessible (PDF/UA pour Writer, signets+balises pour Word)
- Bonus : Verification post-export (PAC, Acrobat Pro)

### Page finale

- Checklist rapide : les 21 criteres sous forme de cases a cocher
- Ressources : liens vers CCA (outil de contraste), PAC, guide Tanaguru
- QR code vers le site d'exercice : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/

---

## Différences entre Word et LibreOffice Writer

Les deux memos suivent la meme structure mais les procedures different :

| Action | Word | LibreOffice Writer |
|--------|------|-------------------|
| Proprietes du document | Fichier > Informations > Proprietes | Fichier > Proprietes > Description |
| Volet de navigation | Affichage > Volet de navigation | F5 (Navigateur) |
| Table des matieres | References > Table des matieres | Insertion > Table des matieres et index |
| Listes a puces | Accueil > Puces | Formatage > Listes |
| En-tete de tableau | Creation > Ligne d'en-tete | Tableau > Inserer > En-tete |
| Colonnes | Mise en page > Colonnes | Format > Colonnes |
| Marques de formatage | Accueil > Afficher tout | Affichage > Marques de formatage |
| Majuscules correctes | Police > Tout en majuscules | Caractere > Majuscules |
| Langue passage | Barre d'etat > Langue | Barre d'etat > Langue |
| Orthographe majuscules | Options > Verification | Outils > Options > Linguistique |
| Alt text image | Clic droit > Modifier texte de remplacement | Clic droit > Proprietes > Option |
| Image decorative | Case "Marquer comme decoratif" | Laisser alt vide (pas d'option native) |
| Ancrage image | Ancre + position (attention : decorrelees) | Comme caractere (plus fiable) |
| Verification a11y | Revision > Verifier l'accessibilite | Outils > Verification |
| Export PDF | Fichier > Exporter > PDF/XPS + Options | Fichier > Exporter en PDF > PDF/UA |

---

## Selection des captures d'ecran

### Pour le Memo Word (captures depuis `/tmp/pptx-bureautique-images/` et `/tmp/pptx-tp-images/`)

| Theme | Capture | Source | Usage |
|-------|---------|--------|-------|
| Proprietes | `slide07_img7.png` | Bureautique | Boite proprietes Word |
| Volet navigation | `slide14_img7.png` ou `slide14_img8.png` | Bureautique | Volet de navigation |
| Styles | Slide TP 9 ou 12 | TP | Barre de styles |
| Table des matieres | `slide17_img7.png` | Bureautique | Menu References |
| Listes | `slide19_img7.png` a `slide19_img9.png` | Bureautique | Barre d'outils listes |
| Tableaux | `slide21_img7.png` | Bureautique | Proprietes du tableau |
| Colonnes | `slide22_img8.png` | Bureautique | Menu Colonnes |
| Marques formatage | `slide25_img8.png` | Bureautique | Bouton Afficher tout |
| Majuscules | `slide29_img8.png` | Bureautique | Options verification |
| Langue | `slide32_img7.png` | Bureautique | Selection langue |
| Contraste | `slide43_img7.png` a `slide43_img9.png` | Bureautique | Selecteur couleur RVB |
| Alt text | `slide50_img7.png` | Bureautique | Boite alt text |
| Verification | `slide54_img7.png` | Bureautique | Verifier l'accessibilite |
| Export PDF | `slide55_img9.png` ou `slide55_img10.png` | Bureautique | Options export PDF |
| PAC | `slide56_img7.png` | Bureautique | Interface PAC |

### Pour le Memo LibreOffice Writer (captures depuis les memes sources)

| Theme | Capture | Source | Usage |
|-------|---------|--------|-------|
| Proprietes | `slide07_img10.png` | Bureautique | Boite proprietes Writer |
| Styles | Slides TP ou Bureautique (Writer) | TP | Barre de styles Writer |
| Navigateur | `slide14_img11.png` | Bureautique | Navigateur F5 |
| Table des matieres | `slide17_img10.png` | Bureautique | Menu Insertion > TDM |
| Listes | `slide19_img14.png` a `slide19_img17.png` | Bureautique | Outils listes Writer |
| Tableaux | `slide21_img9.png` ou `slide21_img10.png` | Bureautique | Insertion tableau Writer |
| Colonnes | `slide22_img10.png` ou `slide22_img11.png` | Bureautique | Format > Colonnes |
| Marques formatage | `slide25_img9.png` | Bureautique | Affichage marques Writer |
| Majuscules | `slide29_img9.png` | Bureautique | Options linguistique Writer |
| Langue | `slide32_img10.png` ou `slide32_img11.png` | Bureautique | Barre d'etat langue Writer |
| Alt text | `slide50_img11.png` ou `slide50_img12.png` | Bureautique | Proprietes image Writer |
| Verification | `slide54_img10.png` | Bureautique | Verification Writer |
| Export PDF | `slide55_img10.png` | Bureautique | Export PDF/UA Writer |

---

## Etapes de production

### Etape 1 : Preparation du contenu Markdown

1. Creer `fiche-pratique/memo-word.md` avec la structure des 5 themes
2. Creer `fiche-pratique/memo-libreoffice-writer.md` avec la meme structure
3. Pour chaque critere Sami (1 a 21) :
   - Lire la spec dans `_source/exercice-sami-spec.md`
   - Lire les slides sources correspondantes (voir cartographie ci-dessus)
   - Rediger : erreur typique + impact + procedure specifique (Word OU Writer)
4. Ajouter les bonus Theme 5 (verification + export + PAC)
5. Ajouter la checklist finale des 21 criteres
6. Ajouter les ressources et QR code

### Etape 2 : Selection et preparation des images

1. Identifier les 12 a 15 captures cles par memo (voir tableaux ci-dessus)
2. Verifier visuellement chaque capture selectionnee
3. Recadrer si necessaire (ne garder que la zone pertinente)
4. Nommer les images de facon descriptive (ex : `word-proprietes-titre.png`)
5. Copier dans `fiche-pratique/images-memo-word/` et `fiche-pratique/images-memo-writer/`

### Etape 3 : Generation PDF accessible

1. Utiliser le skill `/accessible-pdf` pour chaque memo
2. Template DSFR, police Marianne (fallback Arial)
3. Verifier les metadonnees PDF : titre, auteur, langue fr
4. Verifier la structure de balises (titres, listes, images avec alt)
5. Noms des fichiers : `memo-word-accessibilite.pdf` et `memo-libreoffice-writer-accessibilite.pdf`

### Etape 4 : Validation

Voir checklist ci-dessous.

---

## Checklist de validation

### Contenu

- [ ] Les 21 criteres Sami sont couverts dans chaque memo
- [ ] L'ordre des themes est respecte (Structure > Couleurs > Contenus > Langue/Lisibilite > Finalisation)
- [ ] Les procedures sont specifiques a la suite (pas de melange Word/Writer)
- [ ] Pas de jargon developpeur (pas de ARIA, DOM, CSS, HTML)
- [ ] Les chemins de menu sont exacts et a jour (verifies sur Word 365 et LibreOffice 7.x)
- [ ] Le contraste ambigu (critere 6) mentionne explicitement le ratio 4,5:1 et l'outil CCA
- [ ] Le critere 10 (image decorative) mentionne la difference Word vs Writer (pas d'option native dans Writer)
- [ ] L'export PDF (theme 5) distingue PDF/XPS (Word) de PDF/UA (Writer)

### Images

- [ ] Chaque capture est lisible a la taille imprimee (pas de texte trop petit)
- [ ] Chaque capture a un alt text descriptif dans le Markdown source
- [ ] Les captures Word sont dans le memo Word, les captures Writer dans le memo Writer (pas de melange)
- [ ] Les icones de repere (toolbar) sont visibles et reconnaissables

### Accessibilite du PDF lui-meme

- [ ] Structure de titres hierarchique (H1 > H2 > H3, pas de saut)
- [ ] Langue du document declaree (`fr`)
- [ ] Titre et auteur dans les metadonnees
- [ ] Images avec texte alternatif
- [ ] Listes balisees comme listes (pas de puces tapees)
- [ ] Contraste du texte conforme (4,5:1 minimum)
- [ ] Le PDF est navigable avec un lecteur d'ecran (test VoiceOver rapide)

### Coherence avec la formation

- [ ] Les 5 themes Sami correspondent aux themes de la formation (slides 02pb a 03)
- [ ] Les procedures correspondent a ce qui est montre en classe (pas de raccourci inconnu)
- [ ] La checklist finale reprend exactement les 21 criteres de `exercice-sami-spec.md`
- [ ] Le QR code pointe vers le bon site (https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/)
- [ ] Aucune reference a des themes non couverts en formation (pas de PowerPoint, pas de PDF natif)

### Forme

- [ ] 4 a 8 pages par memo (pas plus)
- [ ] Police Marianne (ou Arial si Marianne indisponible)
- [ ] Mise en page aere : marges suffisantes, espacement entre criteres
- [ ] Pas de tirets cadratins ni demi-cadratins (tiret simple uniquement)
- [ ] Accents francais corrects partout (dans le PDF final, pas dans les noms de fichiers)
- [ ] Pas d'emojis

---

## Definition du Done

Le livrable est considere comme termine quand :

1. **Deux fichiers PDF** existent dans `fiche-pratique/` :
   - `memo-word-accessibilite.pdf`
   - `memo-libreoffice-writer-accessibilite.pdf`

2. **Contenu complet** : les 21 criteres Sami sont presents dans chaque memo, organises par les 5 themes, avec procedure specifique a la suite ciblee

3. **Images incluses** : 12 a 15 captures d'ecran cles par memo, toutes avec alt text

4. **Accessibilite PDF verifiee** : structure de balises, langue, metadonnees, alt text - chaque PDF est lui-meme accessible (le cordonnier bien chausse)

5. **Coherence pedagogique** : un stagiaire qui a suivi la formation et fait l'exercice Sami retrouve ses reperes dans le memo

6. **Validation checklist** : toutes les cases de la checklist ci-dessus sont cochees

7. **Sources Markdown** conservees : `memo-word.md` et `memo-libreoffice-writer.md` sont versionnees dans `fiche-pratique/` pour maintenance future

8. **todo.md mis a jour** : la tache "Fiche Memo LibreOffice" est cochee, une nouvelle ligne "Fiche Memo Word" ajoutee et cochee

---

## Risques et points d'attention

- **Captures obsoletes** : les PPTX sources datent de novembre 2024. Les interfaces Word 365 et LibreOffice evoluent. Verifier que les menus sont toujours d'actualite
- **Taille des images** : trop de captures rendent le PDF lourd et illegible. Privilegier les captures de zones de menu ciblees (pas de screenshot plein ecran)
- **Critere 18 (filigrane)** : aucune slide source ne couvre ce critere. Rediger la procedure a partir de la documentation officielle Word/Writer
- **Writer : pas d'option "decoratif"** : le memo Writer doit expliquer le contournement (laisser alt vide, marquer en PDF apres export)
- **Ancrage des images dans Writer** : preciser "Comme caractere" comme recommandation par defaut (slide 52 du PPTX Bureautique)
