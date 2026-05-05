# TODO - Formation 102638 (IGPDE / Carinne C.)

## En cours

- [ ] **Distribuer la grille d'audit aux stagiaires pour la mission finale** (slide `scripts/slides/52_mission-13-checks.py`) :
  - Fichier source : `03-easy-checks/grille-audit-easy-checks.xlsx` (16 onglets)
  - Version téléchargeable depuis le site : `docs/assets/downloads/grille-audit-easy-checks.xlsx`
  - Point d'entrée site : `docs/index.html`
  - Structure : 12 onglets pré-remplis, un par page obligatoire de l'échantillon RGAA (Accueil, Mentions légales, Déclaration a11y, Plan du site, Contact, Aide, Authentification, Recherche, Document, Article, Formulaire, Liste)
  - Chaque stagiaire saisit les URL et remplit les verdicts C/NC/NA sur chaque onglet
  - L'onglet Synthèse agrège automatiquement les 12 pages et calcule le taux global
  - 20 min audit individuel + 5 min binôme + 5 min restitution
  - Livrable stagiaire : classeur rempli + 3 actions priorisées + 1 engagement personnel
## Fait

- [x] Slides 01-27 assemblées dans `formation-102638-juin-2026.pptx` (27 slides couvrant les 13 points de contrôle rapides W3C)
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
