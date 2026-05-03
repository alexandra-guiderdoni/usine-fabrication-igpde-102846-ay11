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
| 11 | Fausse liste a puces | Tirets manuels (- item) | Liste a puces native (Accueil > Puces) |
| 12 | Fausse liste numerotee | Numeros tapes a la main (1. 2. 3.) | Liste numerotee native (Accueil > Numerotation) |

## Pilier 4 - Langue

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 13 | Passage anglais | Texte en anglais sans balisage de langue | Passage balise en anglais (Revision > Langue > Definir) |

## Pilier 5 - Finalisation

| N | Element | Inaccessible | Accessible |
|---|---------|-------------|------------|
| 14 | Proprietes document | Titre et Auteur vides | Titre et Auteur renseignes |

## Metadonnees

| Element | Inaccessible | Accessible |
|---------|-------------|------------|
| Titre du document | Non renseigne | « Rapport trimestriel - Bilan T1 2025 » |
| Auteur | Non renseigne | « Sami Dupont » |
| Langue | Anglais (par defaut) | Francais (fr-FR) |
| Police | Arial | Arial |
