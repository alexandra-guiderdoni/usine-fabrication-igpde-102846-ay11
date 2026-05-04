# Exercice Sami - liste des differences

Comparaison entre `sami-doc-inaccessible.docx` et `sami-doc-accessible.docx`.

---

## Pilier 1 - Structure

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 1 | « Introduction » | Gras Arial 16 bleu (formatage direct) | Style Titre 1 natif Word |
| 2 | « Resultats du trimestre » | Gras Arial 14 bleu (formatage direct) | Style Titre 2 natif Word |
| 3 | « Detail par canal » | Gras Arial 12 souligne bleu (formatage direct) | Style Titre 3 natif Word |
| 4 | Tableau de resultats | Pas de ligne d'en-tete balisee | Onglet Creation > Ligne d'en-tete cochee |

## Pilier 2 - Couleurs

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 5 | Mention urgente | Rouge #FF0000 sans gras (couleur seule, ratio 4:1) | Rouge #C00000 en gras (ratio 6,5:1 + gras) |
| 6 | Note de bas de page | Gris #767676 (ratio 4,48:1 - insuffisant) | Gris #595959 (ratio 7:1 - conforme) |

## Pilier 3 - Contenus

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 7 | Graphique | Pas de texte alternatif, barres differenciees par couleur seule (vert/rouge) | Alt text descriptif, barres avec motifs distincts + etiquettes |
| 8 | Lien annexes | « cliquez ici » | « Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo) » |
| 9 | Organigramme | alt="image.png" (nom de fichier par defaut) | Alt court renvoyant vers description detaillee sous l'image |
| 10 | Icone enveloppe | alt="E-mail" (redondant avec texte adjacent) | Marquee comme decorative |
| 11 | Fausse liste a puces | Puces tapees et indentees manuellement | Liste a puces native (Accueil > Puces) |
| 12 | Fausse liste numerotee | Numeros tapes et indentes manuellement (1. 2. 3.) | Liste numerotee native (Accueil > Numerotation) |
| 19 | Faux sommaire | Points de suite et numeros tapes a la main | Table des matieres automatique (References > Table des matieres) |
| 21 | Tableau fusionne | Grille avec cellules fusionnees, en-tetes visuels en gras, sans Ligne d'en-tete cochee | Tableau simple en grille sans fusion, avec Ligne d'en-tete cochee |

## Pilier 4 - Langue

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 13 | Passage anglais | Texte en anglais sans balisage de langue | Passage balise en anglais (Revision > Langue > Definir) |
| 15 | Texte justifie | Tout le document en texte justifie | Texte aligne a gauche |
| 16 | Paragraphes vides | 4 paragraphes vides pour simuler un espacement | Espacement gere par les styles de paragraphe |
| 17 | Majuscules | ANNEXES tape en majuscules | Annexes avec propriete Tout en majuscules |

## Pilier 5 - Finalisation

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 14 | Proprietes document | Titre et Auteur vides | Titre et Auteur renseignes |

## Contenus (complement)

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 18 | Filigrane | Filigrane CONFIDENTIEL (invisible lecteur d'ecran) | Mention Document confidentiel dans le corps du texte |
| 20 | Texte en image | Avis important insere comme image | Meme contenu en vrai texte |

## Metadonnees

| Element | Inaccessible | Accessible |
|---------|-------------|------------|
| Titre du document | Non renseigne | « Rapport trimestriel - Bilan T1 2025 » |
| Auteur | Non renseigne | « Sami Dupont » |
| Langue | Anglais (par defaut) | Francais (fr-FR) |
| Police | Arial | Arial |
