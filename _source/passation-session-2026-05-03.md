# Passation session du 3 mai 2026

Projet : Formation 102638 (IGPDE / Carinne C.) - 90 slides PPTX.

---

## Ce qui a ete fait dans cette session

### Exercice de Sami

- Renommage Karine -> Sami sur tous les fichiers et slides
- Script `generate_exercice_sami.py` produit 2 DOCX + 5 images PNG
- **21 erreurs** dans le document inaccessible couvrant les 5 themes :

| Theme | Erreurs |
|-------|---------|
| Structure | 3 faux titres (H1/H2/H3), tableau sans en-tete, 2 fausses listes, faux sommaire, tableau fusionne |
| Couleurs | Urgent couleur seule (#FF0000), contraste ambigu (#767676) |
| Contenus | Graphique sans alt, organigramme alt inadapte, icone redondante, lien non descriptif, texte en image, filigrane invisible |
| Langue/lisibilite | Passage anglais non balise, texte justifie, paragraphes vides, majuscules tapees |
| Finalisation | Proprietes document vides |

- Spec complete dans `_source/exercice-sami-spec.md`
- Diff des 21 erreurs dans `_source/exercice-sami-diff.md`
- Slide 32 : exercice (30 min, 3 phases)
- Slide 37 : retour sur Sami apres piliers 4-5 (effet Zeigarnik, remplace Sophie)

### Slides modifiees

- **Slide 21** : layout corrige (titre_contenu au lieu de titre_soustitre)
- **Slide 25** : cartes reaerees, espacement ameliore
- **Slide 29** : illustration daltonisme (pastilles 3 colonnes, Marianne 14pt)
- **Slide 30** : tableau alt text corrige (icone redondante)
- **Slide 31** : filigranes en minuscules
- **Slide 32** : exercice Sami 21 erreurs, gras sur themes, 30 min
- **Slide 33** : Marianne au lieu de Calibri
- **Slide 37** : retour Sami (remplace Sophie)
- **Slide 38** : 3 reflexes au lieu de matrice impact/effort
- **Slide 39** : quiz reformule (mise en situation, liste numerotee)
- **Slide 40** : correction reformulee (pourquoi + solution)
- **Slide 41-42** : faites le point scinde (questions + reponses)
- **Slide 43-46** : checklist scindee en 4 slides (exercice + autres)
- **Slide 48** : layout corrige
- **Slide 59** : layout corrige

### Changements globaux

- Mot « pilier » remplace par « theme » sur toutes les slides (21 fichiers)
- Fil d'Ariane coherent ajoute sur 28 slides manquantes
- Typographie : espace avant les `...` sur 6 fichiers
- Insight-forge initialise sur le projet

---

## Fichiers cles

| Fichier | Role |
|---------|------|
| `scripts/generate_exercice_sami.py` | Generateur DOCX + images (rejouable) |
| `scripts/generate_pastilles_daltonisme.py` | Image daltonisme slide 29 |
| `_source/exercice-sami-spec.md` | Spec 21 erreurs |
| `_source/exercice-sami-diff.md` | Diff accessible/inaccessible |
| `formation-102638-juin-2026.pptx` | PPTX 90 slides |

---

## Ce qui reste a faire

- Verifier les DOCX dans Word (ouvrir, tester le filigrane, le sommaire, le rendu)
- Eventuellement un 3e exercice pour les points non couverts
- Nouvelles slides potentielles pour detailler les 4 derniers points (justifie, paragraphes vides, majuscules, filigrane)
- Verifier que la checklist (slides 43-46) couvre bien les 21 erreurs
- Relire les modules 3 (points de contrôle rapides) et 4 (Reseaux sociaux) qui n'ont pas ete touches dans cette session
