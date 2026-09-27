# TODO - Formation 102846, ex-102638 (IGPDE / Carine C.)

## En cours

- [ ] **Livraison des livrables à Carine Couplan lundi 2026-09-28** (session du vendredi 9 octobre 2026) :
  - [x] Pack remis à niveau le 2026-09-26 et renommé `IGPDE-102846-livrables-octobre-2026/` : cartes ice-breaker ajoutées (`6-cartes-idees-recues.pdf`), site easy-checks resynchronisé depuis `docs/` (diff vide), README corrigé
  - [x] Deck régénéré pour la session du 9 octobre 2026 sous le code 102846 : `config.yml` mis à jour, boucle QA du deck `CONVERGED new=0`, `support-formation-102846-2026-IGPDE.pptx` (138 slides, 69 tests pytest OK sur le bon fichier après correction du chemin en dur de `tests/conftest.py`, `unzip -t` exit 0, zéro « 102638 » et zéro « juin 2026 » dans tout le paquet), copié dans le pack (md5 identique)
  - [x] Site GitHub Pages republié le 2026-09-26 : corrections RGAA de juillet (commit `ff2b26d`) puis bascule 102846 et grille mise à jour (commit `e2eef6e`) — rendu en ligne vérifié après le premier rebuild
  - [x] Convocation des intervenants copiée dans le pack (`Formateur/documents-administratifs-igpde/convocation-intervenants.pdf`, md5 vérifié, fichier jamais versionné) — session confirmée du vendredi 9 octobre 2026, co-animation Alexandra Guiderdoni et Bertrand Matge ; salle et horaires dans la convocation
  - [ ] **Préparer la salle avant la session** (créneau convenu avec l'IGPDE, voir la convocation)
  - [x] Écart de code formation tranché par Alex le 2026-09-26 : reprogrammation sous le code 102846 ; deck, grille XLSX, site et documents structurants basculés
  - [x] Fiches administratives DOCX du pack renumérotées 102846 le 2026-09-26 (corps, pieds de page, métadonnées ; fichiers renommés, zéro 102638 restant, zips testés, ouverture python-docx vérifiée, quarantine retirée). Les originaux 102638 de la fiche catalogue, du programme et du déroulé restent dans `_source/` ; celui de la fiche technique, seulement dans l'historique git
  - [x] 4 PDF du pack régénérés en 102846 le 2026-09-26 via `/accessible-pdf` (template formation, bandeaux IGPDE restaurés avec alt) : les 2 mémos bureautique (12 pages, PDF/UA-1) et les 2 fiches WCAG (12 et 7 pages, PDF/UA-1). Vérifié par pdftotext (zéro 102638) et marqueur pdfuaid. Bug WeasyPrint 68 contourné sur la fiche formateur : un tableau fragmenté entre deux pages casse le mode PDF/UA-1, `<style>table { break-inside: avoid; }</style>` documenté dans la source `wcag/cadre-legal-principes-wcag-fiche-formateur.md`
  - [x] Dossier `Formateur/_alex/` (ex-`alex/`, renommé le 2026-09-27) nettoyé le 2026-09-27 : export PDF du deck régénéré via LibreOffice headless (`formation-102846-octobre-2026.pdf`, 138 pages, zéro 102638, « 9 octobre 2026 » sur chaque page), note bureautique renommée, rapports JSON a11y de juillet et `slides.json` (contenu original non capitalisé ailleurs) archivés dans `_source/agent-artifacts/` (dossier purgé depuis, à l'extraction de l'usine)
  - [x] Démo emojis refondue en DSFR le 2026-09-27 (skill `dsfr-components`, gabarit du site, accordéons/callouts/badges officiels vérifiés contre `dsfr.min.css`, audit accesslint zéro violation) : version site publiée (`a9a9380`), version TP autonome dans `tp-reseaux-sociaux-igpde/` (assets DSFR locaux 7,5 Mo, navigation en absolu vers le site). Lien Instagram passé en citation non cliquable (politique de liens externes du site). Limites : contrastes non évalués avec le CSS chargé, interaction JS des accordéons non testée au navigateur
  - [x] Fiche `liens-tp-en-ligne.pdf` (ex-`site-web.pdf`) refaite le 2026-09-27 sur une page : liens cliquables vers le site d'exercice et la démo #RS, PDF/UA-1, bandeau IGPDE. Source `liens-tp-en-ligne.md` (page de garde masquée par style local documenté)
  - [x] Livrables binaires du pack versionnés le 2026-09-27 : exceptions `!…/Formateur/**/*.pptx` et `*.docx` dans le `.gitignore` de l'ancien espace de travail (le `.gitignore` autonome de l'usine n'ignore plus que le deck de la racine, ces exceptions n'y sont plus nécessaires). Entrés dans git : le deck, les 4 DOCX administratifs et les 3 DOCX Sami (ces derniers étaient sortis de git au renommage du pack le 2026-09-26). Restent hors git, comme en juin : les 2 `.zip` de `outils/` et le deck généré à la racine
  - [x] Déroulé pédagogique aligné sur la convocation le 2026-09-27 : horaires décalés sur ceux de la convocation, déjeuner porté à 1 h 30, durées et ordre des séquences inchangés ; plage du module 2 corrigée (slides 54 à 73 au lieu de 83, les slides 74 à 83 étant la synthèse). Vérifié : 10 plages calculées justes, continuité sans trou, mise en forme DOCX identique
  - [x] Versions v2 des documents administratifs le 2026-09-27 (originaux rangés alors dans `V1/`, dossier supprimé depuis, voir plus bas) : programme `102846PL-v2.docx` (4 lignes ajoutées, une page vérifiée dans Word), déroulé `Derped-deroule-pedagogique-102846-v2.docx` (mémo LibreOffice ajouté au module 2), fiche technique `102846FiTechn-v2.docx` (nom du deck, NVDA, navigateurs, concepteurs selon la convocation, supports manquants, liens du site et de la démo #RS, Obligally et domaine github.io dans les accès internet, lignes du tableau insécables, 5 pages dans Word). Alignement programme v2 et déroulé v2 vérifié : 20/20
  - [x] Fiche catalogue v2 le 2026-09-27 (`102846FiCat-v2.docx`) : module 3 harmonisé en « Pratiquer » comme le programme et le déroulé, apostrophe typographique dans le libellé, pagination « Page X / Y » ; 2 pages dans Word
  - [ ] Auto-évaluation « en début et fin de formation » promise par la fiche catalogue mais absente du deck : confirmer avec Carine si les fiches d'évaluation IGPDE la couvrent, sinon ajouter deux slides d'auto-positionnement (ouverture et clôture) sur les trois compétences ciblées
  - [ ] Pour 2027 : titre « Fiche catalogue 2026 » à passer en 2027
  - [x] Manifestes ShipGuard sortis du site publié (`docs/visual-tests/` vers `recette/visual-tests/`) le 2026-09-27 : `validate.py` passe au vert
  - [ ] Relecture visuelle humaine du deck par Alex avant remise (les contrôles XML ne voient pas les chevauchements fins)
  - [ ] Choisir le canal de remise (clé USB, dépôt, envoi) et vérifier la taille du dossier `outils/` (environ 200 Mo)
  - [x] Ancien deck de juin archivé le 2026-09-26 sous `archive-oldformation-102638-juin-2026.pptx`, puis retiré de la racine de l'usine : récupérable dans l'historique git (commit `0ab3406`)

- [ ] **Impressions papier avant la session** :
  - Imprimer les cartes idées reçues (ice-breaker)
  - Imprimer les cartes WCAG langage clair

- [ ] **Passe visuelle humaine PowerPoint avant diffusion** :
  - Vérifier en priorité les slides 16 à 22, 36, 75 à 76, 82 à 138
  - Objectif : repérer les chevauchements visuels fins que les contrôles XML ne voient pas
  - État technique actuel : génération 138 slides OK, boucle QA du deck convergée, `unzip -t` OK
- [ ] **Réexport final du deck avant diffusion** :
  - Relecture complète slide par slide par Alex
  - Corrections et modifications au fil de la relecture, dans `scripts/slides/`
  - Régénération stable via `make deck`, puis copie dans le pack via `make pack`
  - Contrôle QA sur copie via `make qa` (lire `.qa/qa-pptx-report.md`)
  - Livrable : `support-formation-102846-2026-IGPDE.pptx` prêt à diffuser

## Fait

- [x] **Fiches Mémo Word et LibreOffice Writer** : deux PDF accessibles (PDF/UA-1, template formation, 14 pages chacun) couvrant les 21 bonnes pratiques Sami organisées par thème. Captures d'écran extraites des PPTX sources. Générées via `/accessible-pdf` + script `md2pdf.py`. Livrables dans `fiche-pratique/`. Le 2026-05-16.
- [x] **Grille d'audit distribuée aux stagiaires** (slide `scripts/slides/52_mission-13-checks.py`) : grille XLSX téléchargeable depuis `docs/assets/downloads/grille-audit-easy-checks.xlsx`, consigne binômes en place.
- [x] **Documentation projet complète** : architecture C4 (`architecture-c4-slides.md`), README causal (aujourd'hui `notes/readme-causal.md`), contraintes (`contraintes.md`), 21 leçons techniques (`lessons.md`). Le 2026-05-16.
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
- [x] Validation locale OK après génération (mai 2026) : `generate_easy_checks_site_skeleton.py` puis `validate.py`. Depuis juillet 2026, le site est maintenu à la main : ne plus relancer ce générateur (voir `AGENTS.md`).
- [x] Sous-titres YouTube français de la vidéo CAPTCHA récupérés le 2026-05-05 (`docs/assets/shared/media/captcha-le-retour-au-moyen-age-youtube.fr.srt` et `.vtt`) et intégrés au lecteur HTML via `docs/assets/shared/media/captcha-sous-titres.vtt`.
- [x] Rattrapage typographique : remplacement des tirets cadratins par tirets simples dans tous les scripts Python (29 fichiers touchés ; règle aujourd'hui dans `AGENTS.md` et contrôlée par le hook)

## Usine autonome (2026-09-27)

- [x] Historique extrait (153 commits depuis mars 2026) et nettoyé : installeurs, convocation, transcriptions d'agents et sorties expérimentales purgés ; coordonnées de Carine et nom de la gestionnaire IGPDE anonymisés ; messages de commit hors sujet neutralisés
- [x] Outillage autonome : `Makefile`, `requirements.lock` avec empreintes, générateur PDF dans `vendor/`, `scripts/fabriquer_pack.py`, hooks `.githooks/`, `.gitignore` autonome, licence etalab-2.0
- [x] `AGENTS.md` protocole unique pour tous les agents, `CLAUDE.md` l'importe ; README d'usine, `PUBLIER-SITE.md`
- [x] Publié sur GitHub le 2026-09-27 (alexandra-guiderdoni/usine-fabrication-igpde-102846-ay11, 159 commits) ; site republié depuis l'usine (make publier-site, commit 5f19e04)
- [ ] Supprimer l'ancien dossier du projet dans l'espace de travail personnel d'Alex (hors de ce dépôt) : uniquement sur GO explicite d'Alex
- [x] Audit des Markdown structurants le 2026-09-27 (contrôles mécaniques et relecture indépendante) puis correction : logistique retirée des fichiers de travail (l'historique public n'est pas réécrit, décision d'Alex), « deux régimes de slides » et démarrage rapide périmé retirés, portée de `make pack` et du hook précisée, `TOP_CONTENT` et composants complétés, `contraintes.md` remis à jour, `notes/readme-causal.md` réduit à l'histoire. Preuve : IA neuve lancée dans l'usine, 10 questions pièges sur 10 justes
- [ ] `scripts/generate_demo.py` (générateur de démonstration hors chaîne) écrit `gabarits-ppt-igpde.pptx` à la racine, homonyme de la source rangée dans `_source/presentations-source/` : à retirer ou à rediriger avant tout usage

## Déménagement du site d'exercice (2026-09-27)

- [x] Sources et livrables pointés vers https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/ : fiche des liens, mémos Word et LibreOffice, fiche technique v2, démo hors ligne, documentation et Makefile ; adresses imprimées sans coupure trompeuse
- [x] Chemins d'images absolus des mémos rendus relatifs (résolus à la génération par `scripts/pack_supports.py`), hook étendu aux sources Markdown et au site
- [x] Dépôt public `alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11` créé, historique du site poussé (9 commits), `.DS_Store` retiré du site, GitHub Pages activé (main, racine) le 2026-09-27
- [x] Nouveau site vérifié en ligne (pages, démo, vidéos, grille : 200 ; outillage interne et corrigé : 404), usine poussée (`fe4fa15`)
- [x] README du dépôt du site (`publication-site/README.md`, copié par `make publier-site`)
- [x] Liens usine et site explicites pour les agents : section « Deux dépôts liés » d'`AGENTS.md`, `AGENTS.md` et `CLAUDE.md` du dépôt publié (sources `publication-site/agents-site.md` et `claude-site.md`), `docs/AGENTS.md` actualisé, clone de consultation `../tp-fabrication-igpde-102846-ay11` avancé par `make publier-site`. Preuve : sessions Claude neuves lancées dans chaque dossier, réponses correctes
- [ ] Non vérifié : avertissement de `make publier-site` quand le clone de consultation a divergé (test refusé le 2026-09-27)
- [x] `Alexmacapple/easy-check-igpde` supprimé par Alex le 2026-09-27, sans attendre la session : historique et étiquette `site-2026-07-04` vérifiés dans le nouveau dépôt avant suppression. Plus aucune trace de l'ancienne adresse dans le pack depuis le retrait de `V1/`
- [x] Dossier `documents-administratifs-igpde/V1/` supprimé le 2026-09-27 à la demande d'Alex : seules les v2 restent dans le pack ; les quatre originaux restent récupérables dans l'historique git (commit précédant leur suppression)
