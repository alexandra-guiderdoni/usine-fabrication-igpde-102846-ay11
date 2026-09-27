# Livrables formation 102846 — octobre 2026

Pack livrable complet pour la session du 9 octobre 2026 (reprogrammation sous le code 102846 de la formation 102638 remise pour la session du 4 juin 2026).

Les fiches administratives ont été renumérotées 102846 localement le 2026-09-26 (contenu, pieds de page et métadonnées) à partir des versions 102638.

## Structure

```
Formateur/
  documents-administratifs-igpde/
    102846FiCat-v2.docx                     Fiche catalogue
    102846FiTechn-v2.docx                   Fiche technique (équipement, outils, accès internet)
    102846PL-v2.docx                        Programme de la formation (une page)
    Derped-deroule-pedagogique-102846-v2.docx  Déroulé pédagogique détaillé
    convocation-intervenants.pdf            Convocation IGPDE du 9 octobre 2026 (sur disque uniquement, non versionnée)
  support-formation-102846-2026-IGPDE.pptx      Deck principal (138 slides DSFR)
  _alex/                         Notes formateur (transcriptions du deck, checklists, PDF du deck)
  fil-rouge-principes-wcag-igpde/  Fiche formateur + fiche stagiaire WCAG
  ice-breaker-idées-recues-cartes-igpde/  6 cartes PDF idées reçues a11y
  tp-word-igpde/                 Exercice Sami (3 DOCX) + fiches mémo PDF
  tp-easy-check-site-web-igpde/  Site d'exercice points de contrôle rapides (clone git du site)
  tp-reseaux-sociaux-igpde/      Démo de mauvaise restitution des emojis
  liens-tp-en-ligne.pdf          Liens en ligne des deux TP (une page)

outils/
  CCA-Setup-3.5.4.msi           Colour Contrast Analyser (Windows)
  focusHighlight-6.6.nvda-addon.zip   Extension NVDA FocusHighlight
  nvda_2024.4.1.exe             Lecteur d'écran NVDA (Windows)
  PAC_24.3.1.0.zip              PDF Accessibility Checker
```

## Relation avec le dépôt

Ce dossier est un **snapshot livrable** : il contient les fichiers finaux tels que remis à l'IGPDE. Deux cas :

- **Fichiers générés ou récupérés** (deck, PDF, documents Sami, démo hors ligne ; installeurs récupérés par `make outils-telecharger`) : ne pas les modifier ici. Corriger la source à la racine de l'usine, puis lancer la commande indiquée dans « Qui fabrique quoi dans le pack » (`AGENTS.md`) : en général `make pack`, précédé de `make sami`, `make grille` ou `make wcag` si leurs sources ont changé.
- **Fichiers édités sur place** (documents administratifs de `Formateur/documents-administratifs-igpde/`, notes `Formateur/_alex/*.md`) : ils n'ont pas de générateur, on les modifie directement ici.
