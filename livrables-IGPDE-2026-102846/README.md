# Livrables formation 102846 — octobre 2026

Snapshot du pack pour la session du 9 octobre 2026, sous le code 102846. Les
quatre installeurs externes du dossier `outils/` doivent encore être déposés et
vérifiés avant la remise à l'IGPDE.

## Structure

```
Formateur/
  documents-administratifs-igpde/
    102846FiCat-v2.docx                     Fiche catalogue
    102846FiTechn-v2.docx                   Fiche technique (équipement, outils, accès internet)
    102846PL-v2.docx                        Programme de la formation (une page)
    Derped-deroule-pedagogique-102846-v2.docx  Déroulé pédagogique détaillé
  support-formation-102846-2026-IGPDE.pptx      Deck principal DSFR
  _alex/                         Notes formateur (transcriptions du deck, checklists)
  fil-rouge-principes-wcag-igpde/  Fiches formateur et stagiaire WCAG, cartes des critères WCAG 2.2 (voir son README)
  ice-breaker-idées-recues-cartes-igpde/  6 cartes PDF idées reçues a11y
  tp-word-igpde/
    tp-doc-inaccessible.docx             Document de départ sans aide
    tp-doc-aide-correction.docx          Document de départ avec pistes
    tp-doc-accessible.docx               Corrigé de référence remis à la fin
    checklist-accessibilite-bureautique.docx  Checklist remplissable
    checklist-accessibilite-bureautique.pdf   Checklist imprimable
    memo-word-accessibilite.pdf          Procédures Microsoft Word
    memo-libreoffice-writer-accessibilite.pdf  Procédures LibreOffice Writer
  tp-reseaux-sociaux-igpde/      Démo de mauvaise restitution des emojis
  liens-tp-en-ligne.pdf          Liens en ligne des deux TP (une page)

outils/
  CCA-Setup-3.5.4.msi           Attendu avant remise, externe à Git
  focusHighlight-6.6.nvda-addon.zip   Attendu avant remise, externe à Git
  nvda_2024.4.1.exe             Attendu avant remise, externe à Git
  PAC_24.3.1.0.zip              Attendu avant remise, téléchargement manuel
```

## Site d'exercice

Le site d'exercice est maintenu dans le dépôt séparé
[`tp-fabrication-igpde-102846-ay11`](https://github.com/alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11).
Dans cet espace de travail, son clone est placé au même niveau que l'usine, sous
`../tp-fabrication-igpde-102846-ay11`. Il ne fait pas partie du snapshot livré.

## Relation avec le dépôt

Ce dossier est un **snapshot livrable** : il contient les fichiers finaux tels que remis à l'IGPDE. Deux cas :

- **Fichiers générés ou récupérés** (deck, PDF, documents Sami, démo hors ligne ; installeurs récupérés par `make outils-telecharger`) : ne pas les modifier ici. Corriger la source à la racine de l'usine, puis lancer la commande indiquée dans « Qui fabrique quoi dans le pack » (`AGENTS.md`) : en général `make pack`, précédé de `make sami`, `make checklist`, `make grille` ou `make wcag` si leurs sources ont changé.
- **Fichiers édités sur place** (documents administratifs de `Formateur/documents-administratifs-igpde/`, notes `Formateur/_alex/*.md`) : ils n'ont pas de générateur ; leur modification se fait directement ici.

La checklist du TP Word est livrée sous les noms
`checklist-accessibilite-bureautique.docx` et
`checklist-accessibilite-bureautique.pdf`. `make checklist` fabrique le DOCX et
la source `_source/checklist-accessibilite-bureautique.md` depuis la matrice
canonique ; `make pdf` fabrique le PDF/UA-1 depuis cette source.

## Distribution du TP Word

Au début du TP, remettre à chaque binôme un seul document de départ, au choix :
`tp-doc-aide-correction.docx` pour le parcours guidé ou
`tp-doc-inaccessible.docx` pour l’essai autonome. Distribuer aussi la checklist
DOCX ou sa version papier, les cartes WCAG et un dossier vide pour le DOCX
corrigé et le PDF contrôlé.

À la fin seulement, remettre `tp-doc-accessible.docx` comme corrigé de
référence, avec les deux mémos. Le graphique se reconstruit directement dans
Word à partir des valeurs visibles dans le document ; sa procédure figure dans
les mémos, sans ressource graphique séparée.

## Ordre de fabrication

`make pack` ne régénère ni les documents Sami ni la checklist DOCX. Après une
modification de leur matrice ou de leur générateur, lancer `make sami`, puis
`make checklist`, puis `make fraicheur-pack`. Lancer ensuite `make pack`, qui
régénère les PDF et le deck, contrôle de nouveau la fraîcheur et copie les
supports attendus.
