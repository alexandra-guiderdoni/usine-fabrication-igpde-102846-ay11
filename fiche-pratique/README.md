# Fiches pratiques - Formation 102638

Mémos accessibilité distribués aux stagiaires après la formation. Deux versions : une pour Microsoft Word, une pour LibreOffice Writer.

---

## Livrables

| Fichier | Contenu |
|---------|---------|
| `memo-word-accessibilite.pdf` | Mémo accessibilité Microsoft Word |
| `memo-libreoffice-writer-accessibilite.pdf` | Mémo accessibilité LibreOffice Writer |

---

## Comment régénérer les PDF

### Prérequis

- Python 3.12 avec `weasyprint`, `pikepdf`, `pandoc` installés
- Skill `/accessible-pdf` (script `~/.claude/skills/accessible-pdf/scripts/md2pdf.py`)
- Vérifier les dépendances : `python3 ~/.claude/skills/accessible-pdf/scripts/md2pdf.py --check`

### Commandes

```bash
cd /Users/alex/Claude/projets-formations/IGPDE-Carinne-C/fiche-pratique

# Mémo Word
python3 ~/.claude/skills/accessible-pdf/scripts/md2pdf.py \
  memo-word.md \
  --template formation \
  --lang fr \
  --logo bandeau-igpde-logos.jpg \
  --logo-alt "République française - IGPDE" \
  --header-text "Mémo accessibilité - Microsoft Word" \
  -o memo-word-accessibilite.pdf

# Mémo LibreOffice Writer
python3 ~/.claude/skills/accessible-pdf/scripts/md2pdf.py \
  memo-libreoffice-writer.md \
  --template formation \
  --lang fr \
  --logo bandeau-igpde-logos.jpg \
  --logo-alt "République française - IGPDE" \
  --header-text "Mémo accessibilité - LibreOffice Writer" \
  -o memo-libreoffice-writer-accessibilite.pdf
```

### Options utilisées

| Option | Valeur | Rôle |
|--------|--------|------|
| `--template formation` | Template CSS pédagogique | Titres bleus, interligne 1,55, sommaire encadré |
| `--lang fr` | Français | Langue du document dans les métadonnées PDF |
| `--logo` | `bandeau-igpde-logos.jpg` | Logos Marianne + IGPDE sur la couverture |
| `--logo-alt` | Texte alternatif du bandeau | Accessibilité PDF/UA |
| `--header-text` | Titre dans l'en-tête de page | Affiché en haut de chaque page sauf la couverture |

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
- Métadonnées : titre, auteur "IGPDE - Formation 102638", langue `fr`
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

Les chemins d'images dans les fichiers Markdown sont **absolus** (nécessaire car le script `md2pdf.py` génère le HTML dans un fichier temporaire, et WeasyPrint résout les chemins relatifs depuis ce fichier temporaire, pas depuis le répertoire source).

---

## Alignement pédagogique

Les deux mémos reprennent les 21 bonnes pratiques de l'exercice "Les erreurs de Sami" (`_source/exercice-sami-spec.md`), organisées en 5 thèmes :

1. **Structure** : styles de titre, listes natives, table des matières automatique, en-têtes de tableau, pas de cellules fusionnées
2. **Couleurs** : pas d'information par la couleur seule, contraste minimum 4,5:1, graphiques avec motifs
3. **Contenus** : alt text, images complexes, images décoratives, liens explicites, filigrane, texte en image
4. **Langue et lisibilité** : balisage langue étrangère, alignement à gauche, espacement par les styles, majuscules par mise en forme
5. **Finalisation** : propriétés du document, vérification d'accessibilité, export PDF accessible

Les procédures sont spécifiques à chaque suite (Word ou Writer). Les différences notables sont documentées dans chaque mémo (ex : Writer n'a pas d'option "Marquer comme décoratif", l'ancrage d'images diffère).

---

## Modification du contenu

1. Éditer le fichier `.md` source (pas le PDF)
2. Régénérer le PDF avec la commande ci-dessus
3. Vérifier visuellement le rendu (images embarquées, mise en page)
4. Vérifier l'accessibilité : `python3 md2pdf.py --check` + ouvrir dans PAC si possible
