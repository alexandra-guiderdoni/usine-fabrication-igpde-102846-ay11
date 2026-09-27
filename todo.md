# TODO - Formation 102846, ex-102638 (IGPDE / Carinne C.)

## En cours

- [ ] **Livraison des livrables à Carine Couplan lundi 2026-09-28** (session du vendredi 9 octobre 2026) :
  - [x] Pack remis à niveau le 2026-09-26 et renommé `IGPDE-102846-livrables-octobre-2026/` : cartes ice-breaker ajoutées (`6-cartes-idees-recues.pdf`), site easy-checks resynchronisé depuis `docs/` (diff vide), README corrigé
  - [x] Deck régénéré pour la session du 9 octobre 2026 sous le code 102846 : `config.yml` mis à jour, QA PRD-119 `CONVERGED new=0`, `support-formation-102846-2026-IGPDE.pptx` (138 slides, 69 tests pytest OK sur le bon fichier après correction du chemin en dur de `tests/conftest.py`, `unzip -t` exit 0, zéro « 102638 » et zéro « juin 2026 » dans tout le paquet), copié dans le pack (md5 identique)
  - [x] Site GitHub Pages republié le 2026-09-26 : corrections RGAA de juillet (commit `ff2b26d`) puis bascule 102846 et grille mise à jour (commit `e2eef6e`) — rendu en ligne vérifié après le premier rebuild
  - [x] Convocation des intervenants copiée dans le pack (`Formateur/documents-administratifs-igpde/convocation-intervenants.pdf`, md5 vérifié) — session confirmée du vendredi 9 octobre 2026, salle 3227 Vincennes, 9 h 15-12 h 15 et 13 h 45-16 h 45, co-animation Alexandra Guiderdoni et Bertrand Matge
  - [ ] **Préparer la salle 3227 le vendredi 2 octobre 2026 après-midi** (créneau bloqué par la gestionnaire IGPDE)
  - [x] Écart de code formation tranché par Alex le 2026-09-26 : reprogrammation sous le code 102846 ; deck, grille XLSX, site et documents structurants basculés
  - [x] Fiches administratives DOCX du pack renumérotées 102846 le 2026-09-26 (corps, pieds de page, métadonnées ; fichiers renommés, zéro 102638 restant, zips testés, ouverture python-docx vérifiée, quarantine retirée). Les originaux 102638 restent dans `_source/`
  - [x] 4 PDF du pack régénérés en 102846 le 2026-09-26 via `/accessible-pdf` (template formation, bandeaux IGPDE restaurés avec alt) : les 2 mémos bureautique (12 pages, PDF/UA-1) et les 2 fiches WCAG (12 et 7 pages, PDF/UA-1). Vérifié par pdftotext (zéro 102638) et marqueur pdfuaid. Bug WeasyPrint 68 contourné sur la fiche formateur : un tableau fragmenté entre deux pages casse le mode PDF/UA-1, `<style>table { break-inside: avoid; }</style>` documenté dans la source `wcag/cadre-legal-principes-wcag-fiche-formateur.md`
  - [x] Dossier `Formateur/alex/` nettoyé le 2026-09-27 : export PDF du deck régénéré via LibreOffice headless (`formation-102846-octobre-2026.pdf`, 138 pages, zéro 102638, « 9 octobre 2026 » sur chaque page), note bureautique renommée, rapports JSON a11y de juillet et `slides.json` (contenu original non capitalisé ailleurs) archivés dans `_source/agent-artifacts/`
  - [x] Démo emojis refondue en DSFR le 2026-09-27 (skill `dsfr-components`, gabarit du site, accordéons/callouts/badges officiels vérifiés contre `dsfr.min.css`, audit accesslint zéro violation) : version site publiée (`a9a9380`), version TP autonome dans `tp-reseaux-sociaux-igpde/` (assets DSFR locaux 7,5 Mo, navigation en absolu vers le site). Lien Instagram passé en citation non cliquable (politique de liens externes du site). Limites : contrastes non évalués avec le CSS chargé, interaction JS des accordéons non testée au navigateur
  - [x] Fiche `liens-tp-en-ligne.pdf` (ex-`site-web.pdf`) refaite le 2026-09-27 sur une page : liens cliquables vers le site d'exercice et la démo #RS, PDF/UA-1, bandeau IGPDE. Source `liens-tp-en-ligne.md` (page de garde masquée par style local documenté)
  - [ ] Décider du versionnement des livrables binaires du pack : le deck `support-formation-102846-2026-IGPDE.pptx` et les 4 DOCX de `documents-administratifs-igpde/` sont exclus par les règles `*.pptx` et `*.docx` du `.gitignore` racine (présents sur disque, absents de GitHub). Option : `git add -f` sur les copies du pack uniquement
  - [ ] Corriger ou exclure de la publication `docs/visual-tests/` (outillage interne publié par erreur ; `_review-template.html` fait échouer `validate.py` sur un lien local « , » — préexistant, juillet 2026)
  - [ ] Relecture visuelle humaine du deck par Alex avant remise (les contrôles XML ne voient pas les chevauchements fins)
  - [ ] Choisir le canal de remise (clé USB, dépôt, envoi) et vérifier la taille du dossier `outils/` (environ 200 Mo)
  - [x] Ancien deck de juin archivé le 2026-09-26 : renommé `archive-oldformation-102638-juin-2026.pptx` à la racine (commit `218029ae8`)

- [ ] **Impressions papier avant la session** :
  - Imprimer les cartes idées reçues (ice-breaker)
  - Imprimer les cartes WCAG langage clair

- [ ] **Passe visuelle humaine PowerPoint avant diffusion** :
  - Vérifier en priorité les slides 16 à 22, 36, 75 à 76, 82 à 138
  - Objectif : repérer les chevauchements visuels fins que les contrôles XML ne voient pas
  - État technique actuel : génération 138 slides OK, QA PRD-119 convergée, `unzip -t` OK
- [ ] **Réexport final du deck avant diffusion** :
  - Relecture complète slide par slide par Alex
  - Corrections et modifications au fil de la relecture
  - Régénération stable via `python3 scripts/assemble.py`
  - Contrôle QA sur copie via `python3 scripts/qa_pptx.py . --max-iterations 5 --clean`
  - Livrable : `support-formation-102846-2026-IGPDE.pptx` prêt à diffuser

## Fait

- [x] **Fiches Mémo Word et LibreOffice Writer** : deux PDF accessibles (PDF/UA-1, template formation, 14 pages chacun) couvrant les 21 bonnes pratiques Sami organisées par thème. Captures d'écran extraites des PPTX sources. Générées via `/accessible-pdf` + script `md2pdf.py`. Livrables dans `fiche-pratique/`. Le 2026-05-16.
- [x] **Grille d'audit distribuée aux stagiaires** (slide `scripts/slides/52_mission-13-checks.py`) : grille XLSX téléchargeable depuis `docs/assets/downloads/grille-audit-easy-checks.xlsx`, consigne binômes en place.
- [x] **Documentation projet complète** : architecture C4 (`architecture-c4-slides.md`), README causal (`README.md`), contraintes (`contraintes.md`), 21 leçons techniques (`lessons.md`). Le 2026-05-16.
- [x] **Support PPTX principal généré** : `formation-102638-juin-2026.pptx`, 138 slides, dernière mise à jour technique le 2026-05-22, QA PRD-119 convergée sur copie.
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
