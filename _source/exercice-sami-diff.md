# Exercice Sami - liste des différences

Comparaison entre `sami-doc-inaccessible.docx` et `sami-doc-accessible.docx`.
Le fichier `sami-doc-aide-correction.docx` reprend volontairement la version
inaccessible et ajoute des commentaires Word pédagogiques sur les points à
corriger : problème, impact et méthode. Il ne corrige pas le document.

---

## Pilier 1 - Structure

| N | Élément | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 1 | « Introduction » | Gras Arial 16 bleu (formatage direct) | Style Titre 1 natif Word |
| 2 | « Résultats du trimestre » | Gras Arial 14 bleu (formatage direct) | Style Titre 2 natif Word |
| 3 | « Détail par canal » | Gras Arial 12 souligné bleu (formatage direct) | Style Titre 3 natif Word |
| 4 | Tableau de résultats | Pas de ligne d'en-tête balisée | Onglet Création > Ligne d'en-tête cochée |

## Pilier 2 - Couleurs

| N | Élément | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 5 | Mention urgente | Rouge #FF0000 sans gras (couleur seule, ratio 4:1) | Rouge #C00000 en gras (ratio 6,5:1 + gras) |
| 6 | Note de bas de page | Gris #767676 (ratio 4,48:1 - insuffisant) | Gris #595959 (ratio 7:1 - conforme) |

## Pilier 3 - Contenus

| N | Élément | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 7 | Graphique | Pas de texte alternatif, barres différenciées par couleur seule (vert/rouge) | Texte alternatif descriptif, barres avec motifs distincts + étiquettes |
| 8 | Lien annexes | « cliquez ici » | « Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo) » |
| 9 | Organigramme | alt="image.png" (nom de fichier par défaut) | Alternative courte renvoyant vers une description détaillée sous l'image |
| 10 | Icône enveloppe | alt="E-mail" (redondant avec texte adjacent) | Marquée comme décorative |
| 11 | Fausse liste à puces | Puces tapées et indentées manuellement | Liste à puces native (Accueil > Puces) |
| 12 | Fausse liste numérotée | Numéros tapés et indentés manuellement (1. 2. 3.) | Liste numérotée native (Accueil > Numérotation) |
| 19 | Faux sommaire | Points de suite et numéros tapés à la main | Table des matières automatique (Références > Table des matières) |
| 21 | Tableau fusionné | Grille avec cellules fusionnées, en-têtes visuels en gras, sans Ligne d'en-tête cochée | Tableau simple en grille sans fusion, avec Ligne d'en-tête cochée |

## Pilier 4 - Langue

| N | Élément | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 13 | Passage anglais | Texte en anglais sans balisage de langue | Passage balisé en anglais (Révision > Langue > Définir) |
| 15 | Texte justifié | Tout le document en texte justifié | Texte aligné à gauche |
| 16 | Paragraphes vides | 4 paragraphes vides pour simuler un espacement | Espacement géré par les styles de paragraphe |
| 17 | Majuscules | ANNEXES tapé en majuscules | Annexes avec propriété Tout en majuscules |

## Pilier 5 - Finalisation

| N | Élément | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 14 | Propriétés document | Titre et auteur vides | Titre et auteur renseignés |

## Contenus (complément)

| N | Élément | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 18 | Filigrane | Filigrane CONFIDENTIEL (invisible lecteur d'écran) | Mention Document confidentiel dans le corps du texte |
| 20 | Texte en image | Avis important inséré comme image | Même contenu en vrai texte |

## Métadonnées

| Élément | Inaccessible | Accessible |
|---------|-------------|------------|
| Titre du document | Non renseigné | « Rapport trimestriel - Bilan T1 2025 » |
| Auteur | Non renseigné | « Sami Dupont » |
| Langue | Anglais (par défaut) | Français (fr-FR) |
| Police | Arial | Arial |
