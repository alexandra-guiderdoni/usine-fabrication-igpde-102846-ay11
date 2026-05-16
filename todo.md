# TODO - Formation 102638 (IGPDE / Carinne C.)

## En cours

- [ ] **Impressions papier avant la session** :
  - Imprimer les cartes idées reçues (ice-breaker)
  - Imprimer les cartes WCAG langage clair

- [ ] **Passe visuelle humaine PowerPoint avant diffusion** :
  - Vérifier en priorité les slides 16 à 22, 36, 75 à 76, 82 à 138
  - Objectif : repérer les chevauchements visuels fins que les contrôles XML ne voient pas
  - État technique actuel : génération 138 slides OK, 0 warnings, `unzip -t` OK
- [ ] **Finalisation du deck pour livraison lundi 19 mai** :
  - Relecture complète slide par slide par Alex
  - Corrections et modifications au fil de la relecture
  - Régénération finale via `python3 scripts/assemble.py` + `finalize_pptx()`
  - Livrable : `formation-102638-juin-2026.pptx` prêt à rendre

## Fait

- [x] **Fiches Mémo Word et LibreOffice Writer** : deux PDF accessibles (PDF/UA-1, template formation, 14 pages chacun) couvrant les 21 bonnes pratiques Sami organisées par thème. Captures d'écran extraites des PPTX sources. Générées via `/accessible-pdf` + script `md2pdf.py`. Livrables dans `fiche-pratique/`. Le 2026-05-16.
- [x] **Grille d'audit distribuée aux stagiaires** (slide `scripts/slides/52_mission-13-checks.py`) : grille XLSX téléchargeable depuis `docs/assets/downloads/grille-audit-easy-checks.xlsx`, consigne binômes en place.
- [x] **Documentation projet complète** : architecture C4 (`architecture-c4-slides.md`), README causal (`README.md`), contraintes (`contraintes.md`), 21 leçons techniques (`lessons.md`). Le 2026-05-16.
- [x] **Support PPTX principal livré** : `formation-102638-juin-2026.pptx`, 131 slides, dernière mise à jour le 2026-05-16.
- [x] **Module 1 élargi** : accessibiliser sa communication, handicap/validisme, règles transversales, WCAG/RGAA et déclaration d'accessibilité.
- [x] **Module Word renforcé** : lisibilité, alignement à gauche, paragraphes aérés, contraste mesuré et fonds non dégradés.
- [x] **Module Web easy checks renforcé** : bonus médias, VSME, niveaux de transcription, liens et PDF.
- [x] **Module réseaux sociaux renforcé** : communication inclusive, checklist en binôme, QR code avec lien visible, quiz et plan d'action.
- [x] Grille d'audit MD documentaire (`03-easy-checks/grille-audit-easy-checks.md`)
- [x] **Grille d'audit XLSX validée** (`03-easy-checks/grille-audit-easy-checks.xlsx`) - 16 onglets, 12 pages pré-remplies, avertissement sensibilisation, mention PAC pour documents, renommage « Taux de conformité points de contrôle rapides », évaluée 8/10 (adéquation points de contrôle rapides 9, initiation 8, pédagogie 7,5). Validée par Alex le 2026-04-17.
- [x] **Site d'entraînement des points de contrôle rapides fabriqué** (`docs/index.html`) - support de la mission clavier (`scripts/slides/41_mission-clavier.py`) et de la mission 13 points (`scripts/slides/52_mission-13-checks.py`).
  - Versions générées : `docs/site-inaccessible/`, `docs/site-aide-correction/`, `docs/site-accessible/`
  - Pages de support : déclaration d'accessibilité, mentions légales, données personnelles, plan du site, manifeste des erreurs, corrigé
  - Grille XLSX copiée dans `docs/assets/downloads/`
- [x] **Passe QA UX / navigation clavier réalisée le 2026-05-05** avec `ux-checklist` + vérification navigateur Playwright.
  - `docs/index.html` : verdict conforme pour une page hub d'exercice ; liens d'évitement OK ; ordre de tabulation logique ; focus DSFR visible sur navigation, liens et cartes via pseudo-élément ; densité acceptable malgré 34 arrêts clavier.
  - `docs/site-inaccessible/ec06-keyboard-focus.html` : conforme à l'intention pédagogique, à corriger en production ; `Publier la session` est atteignable au clavier avec focus visible et ouvre une modale ; `Vérifier le formulaire` et `Prévenir les participants` sont des liens simples visibles mais retirés du Tab ; focus invisible sur cartes, accordéons et lien final ; modale DSFR avec piège clavier volontaire (Tab bloqué, Échap neutralisé, `aria-expanded` maintenu à `true`).
  - `docs/site-accessible/ec06-keyboard-focus.html` : témoin corrigé ; bouton de publication et liens d'action focusables ; focus visible conservé ; modale refermable avec Échap et retour du focus sur le bouton d'ouverture.
- [x] Validation locale OK après génération : `python3 scripts/generate_easy_checks_site_skeleton.py` puis `python3 validate.py`.
- [x] Sous-titres YouTube français de la vidéo CAPTCHA récupérés le 2026-05-05 (`docs/assets/shared/media/captcha-le-retour-au-moyen-age-youtube.fr.srt` et `.vtt`) et intégrés au lecteur HTML via `docs/assets/shared/media/captcha-sous-titres.vtt`.
- [x] Rattrapage typographique : remplacement des tirets cadratins par tirets simples dans tous les scripts Python (29 fichiers touchés + règle documentée dans CLAUDE.md)
