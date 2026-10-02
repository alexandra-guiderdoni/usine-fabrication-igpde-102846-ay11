# Fiches pratiques - Formation 102846

Mémos accessibilité remis aux stagiaires à la fin du TP. Deux versions : une pour Microsoft Word, une pour LibreOffice Writer.

---

## Livrables

| Fichier | Contenu |
|---------|---------|
| `memo-word-accessibilite.pdf` | Mémo accessibilité Microsoft Word |
| `memo-libreoffice-writer-accessibilite.pdf` | Mémo accessibilité LibreOffice Writer |

---

## Comment régénérer les PDF

Depuis la racine de l'usine :

```bash
make pdf
```

La commande régénère les deux mémos (et les autres PDF du pack) avec le générateur embarqué dans `vendor/accessible-pdf/`, puis copie les mémos dans `Formateur/tp-word-igpde/` du pack. Prérequis : `make installer`, et Pandoc, Pango et GLib (Homebrew).

### Options utilisées

- `--template formation` : gabarit CSS pédagogique (titres bleus, sommaire encadré).
- `--lang fr` : langue du document dans les métadonnées PDF.
- `--logo bandeau-igpde-logos.jpg` et `--logo-alt "République française - IGPDE"` : bandeau des logos, avec son texte alternatif (exigence PDF/UA).
- `--header-text "Mémo accessibilité - Microsoft Word"` (ou « LibreOffice Writer ») : titre en haut de chaque page, sauf la couverture.

Les images sont citées par des chemins relatifs (`images-memo-word/…`, `images-memo-writer/…`) : `scripts/pack_supports.py` les résout au moment de la génération, où que se trouve l'usine.

### Pipeline de conversion

Le script `md2pdf.py` exécute 6 étapes :

1. **Pandoc** : Markdown vers HTML5 sémantique (titres, listes, images avec alt, liens)
2. **Injection CSS** : application du template `formation` + attributs d'accessibilité (lang, aria)
3. **Audit HTML** : vérification des contrastes WCAG et des images sans alt (RGAA 13.8)
4. **WeasyPrint** : HTML vers PDF balisé (PDF/UA-1 quand possible, sinon PDF tagué)
5. **Post-traitement** : injection des balises /Figure + /Alt pour le logo (pikepdf)
6. **Métadonnées XMP** : titre, auteur, langue dans les propriétés du PDF

### Résultat attendu

- Standard : **PDF/UA-1**
- Métadonnées : titre, auteur "IGPDE - Formation 102846", langue `fr`
- Structure : MarkInfo + StructTreeRoot (balises de titres, listes, figures)
- Images : toutes avec texte alternatif
- Taille : 350-450 Ko par PDF

---

## Structure du dossier

```
fiche-pratique/
  memo-word.md                          # Source Markdown du mémo Word
  memo-libreoffice-writer.md            # Source Markdown du mémo Writer
  memo-word-accessibilite.pdf           # PDF généré
  memo-libreoffice-writer-accessibilite.pdf  # PDF généré
  bandeau-igpde-logos.jpg               # Logos Marianne + IGPDE (recadré sans texte)
  images-memo-word/                     # Captures d'écran Word (12 PNG)
  images-memo-writer/                   # Captures d'écran Writer (10 PNG)
  prompt-memo-bureautique.md            # Cahier des charges initial
  README.md                             # Ce fichier
```

### Origine des captures d'écran

Les captures proviennent de deux PPTX sources (formation de novembre 2024) :

- `IGPDE-2024-11-25_Chargés_Com-Seq6-Bureautique-v2.pptx` (57 slides, Word + Writer)
- `L'accessibilité numérique - Travaux pratique - deuxième partie.pptx` (24 slides, pas-à-pas)

Elles ont été extraites via `python-pptx`, triées par suite (Word vs Writer), renommées de façon descriptive et copiées dans les dossiers `images-memo-word/` et `images-memo-writer/`.

Les chemins d'images restent **relatifs** dans les sources Markdown. `md2pdf.py` écrit le HTML dans un fichier temporaire, d'où WeasyPrint ne retrouverait pas un chemin relatif : c'est `scripts/pack_supports.py` qui les rend absolus au moment de la génération, sans jamais les écrire dans les sources. Ne pas y mettre de chemin absolu : le hook du dépôt refuse les chemins personnels (`/Users/…`, `/home/…`), et tout autre chemin absolu casserait la génération sur un autre poste.

---

## Alignement pédagogique

Les deux mémos suivent les cinq stations et les contrôles de la matrice
canonique `_source/exercice-sami-matrice.yml` :

1. **Structurer et naviguer** : titres, sommaire, listes et mise en page robuste.
2. **Rendre les contenus et les liens compréhensibles** : images, textes,
   liens et informations essentielles.
3. **Sécuriser couleurs, graphiques et tableaux** : contrastes, informations
   non portées par la couleur seule et tableaux de données simples.
4. **Régler langues et lisibilité** : langues, styles typographiques, casse,
   accents et sigles.
5. **Finaliser et publier** : propriétés, vérificateur, export PDF et contrôle
   avec PAC ou Acrobat Pro.

Les contrôles signalés sans manipulation obligatoire restent dans la checklist
et les notes formateur ; ils ne créent pas une sixième station.

Les procédures sont spécifiques à chaque suite (Word ou Writer). Les différences notables sont documentées dans chaque mémo : selon la version de Writer, l'option « Marquer comme décoratif » peut être absente ou présentée différemment ; l'ancrage des images diffère également.

---

## Modification du contenu

1. Éditer le fichier `.md` source (pas le PDF)
2. Régénérer le PDF avec `make pdf`
3. Vérifier visuellement le rendu (images embarquées, mise en page)
4. Vérifier l'accessibilité en ouvrant le PDF dans PAC (PDF Accessibility Checker). `vendor/accessible-pdf/scripts/md2pdf.py --check` ne contrôle que les dépendances du générateur, pas le PDF.
