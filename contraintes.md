# Contraintes — Usine IGPDE 102846

- **Compilé le** : 2026-09-28
- **Mise à jour ciblée** : 2026-10-04
- **Compilateur** : `contraintes-vivantes` v1
- **Portée** : fabrication locale du pack de formation et publication contrôlée du site d'exercice.
- **Sources de compilation** : `AGENTS.md`, `Makefile`, `config.yml`, `requirements.txt`, `requirements.lock`, `scripts/`, `tests/`, `docs/`, `publication-site/`, `validate.py`, `PUBLIER-SITE.md`, `architecture-c4-slides.md` et l'état vérifié par `make verifier` et `make qa`.

Ce document décrit les contraintes effectives de l'usine. Il ne remplace ni les consignes opérationnelles d'`AGENTS.md`, ni l'historique et les pistes de travail de `todo.md`.

## 1. Environnement et dépendances

### Dépendances Python verrouillées

- **Date** : 2026-09-28
- **Source** : `requirements.txt`, `requirements.lock`, `Makefile`.
- **Statut** : active et vérifiée.
- **Contrainte** : la fabrication s'appuie sur Python 3.12 et sur des dépendances aux versions verrouillées : `python-pptx` 1.0.2, `lxml` 6.0.2, `openpyxl` 3.1.5, `python-docx` 1.2.0, `PyYAML` 6.0.3, `matplotlib` 3.10.9, `numpy` 2.4.4, `Pillow` 12.1.1, `WeasyPrint` 68.1, `pikepdf` 10.6 et `pytest` 9.0.3.
- **Impact** : une dépendance installée hors de ces versions peut changer la génération des PPTX, DOCX, XLSX ou PDF, ou invalider les contrôles.
- **Décision / prochaine vérification** : installer avec `make installer`, qui crée `.venv` et exécute `uv pip sync --require-hashes --python .venv/bin/python requirements.lock`.
- **Composants affectés** : `.venv/`, `requirements.txt`, `requirements.lock`, scripts de fabrication et tests.

### Outillage hôte

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `Makefile`.
- **Statut** : active.
- **Contrainte** : macOS est l'environnement de référence. La chaîne attend `uv`, `/opt/homebrew/bin/python3.12`, Pandoc, Pango et GLib. LibreOffice sert aux vérifications et exports manuels ; les cibles de fabrication du pack ne l'appellent pas.
- **Impact** : sans l'outillage hôte, les commandes de fabrication concernées échouent ou ne garantissent pas le même résultat.
- **Décision / prochaine vérification** : privilégier `.venv/bin/python` après `make installer`. Le repli sur Python système n'offre pas de garantie de dépendances.
- **Composants affectés** : `Makefile`, `scripts/`, génération PDF et vérifications manuelles dans LibreOffice.

### Recette visuelle autonome

- **Date** : 2026-09-28
- **Source** : `Makefile`, `recette/installer-recette.sh`, `recette/package.json`.
- **Statut** : active.
- **Contrainte** : `make installer-recette` prépare les dépendances de recette sans plugin Codex ni dépendance globale : ShipGuard `v2.14.0` est cloné à son commit vérifié dans `.tools/shipguard/`, `agent-browser` 0.38.1 est installé dans `recette/node_modules/` et Chrome for Testing est téléchargé sous `.tools/` avec une empreinte SHA-256 vérifiée.
- **Impact** : `make recette` est reproductible depuis un clone de l'usine après cette installation, sans dépendre du cache personnel d'un agent.
- **Décision / prochaine vérification** : conserver le tag, le commit et le verrou npm alignés ; lancer `make installer-recette`, puis `make recette` après toute mise à jour de cette chaîne.
- **Composants affectés** : `Makefile`, `recette/`, `.tools/`, `.gitignore`.

### Assets DSFR embarqués

- **Date** : 2026-09-28
- **Source** : `docs/assets/dsfr/`, `validate.py`.
- **Statut** : active et vérifiée.
- **Contrainte** : le site d'exercice embarque ses assets DSFR localement, notamment les feuilles de style et scripts de la bibliothèque.
- **Impact** : une copie incomplète de `docs/assets/dsfr/` dégrade le rendu ou les comportements interactifs et fait échouer la validation du site.
- **Décision / prochaine vérification** : conserver les assets dans le dépôt et lancer la validation du site après toute mise à jour DSFR.
- **Composants affectés** : `docs/assets/dsfr/`, `docs/**/*.html`, `validate.py`.

### Services externes autorisés

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `Makefile`, `PUBLIER-SITE.md`.
- **Statut** : active.
- **Contrainte** : GitHub héberge l'usine et le dépôt du site ; GitHub Pages sert le site d'exercice. Les hôtes HTTP(S) du site sont limités à la liste blanche `ALLOWED_EXTERNAL_HOSTS` de `validate.py`. Les téléchargements d'outils sont contrôlés par le manifeste du pack.
- **Impact** : la publication et la récupération d'outils dépendent du réseau et des accès GitHub, sans modifier la source locale du site. Une nouvelle référence externe hors liste blanche fait échouer la validation.
- **Décision / prochaine vérification** : conserver les URL, dépôts et empreintes dans leurs fichiers de configuration ou manifestes dédiés ; ajouter explicitement tout hôte pédagogique légitime à la liste blanche avant son usage.
- **Composants affectés** : `validate.py`, `docs/**/*.html`, `PUBLIER-SITE.md`, `livrables-IGPDE-2026-102846/outils/`, dépôt GitHub Pages.

## 2. Chaîne de fabrication

### Orchestration courante par Make

- **Date** : 2026-09-28
- **Source** : `Makefile`, `AGENTS.md`.
- **Statut** : active et vérifiée.
- **Contrainte** : `make` est le point d'entrée courant : `make installer`, `make deck`, `make sami`, `make grille`, `make wcag`, `make pdf`, `make supports`, `make fraicheur-pack`, `make pack`, `make verifier`, `make qa`, `make recette` et `make publier-site` portent les étapes documentées.
- **Impact** : les cibles préservent l'ordre de production, les chemins des livrables et les contrôles associés.
- **Décision / prochaine vérification** : les diagnostics ou tests explicitement hors cible `make` utilisent le même interpréteur que l'usine et respectent les consignes d'`AGENTS.md`.
- **Composants affectés** : `Makefile`, `.venv/`, `scripts/`, `tests/`, livrables.

### Deck et composants de présentation

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `scripts/assemble.py`, `scripts/slides/`, `scripts/igpde_dsfr_components.py`.
- **Statut** : active et vérifiée.
- **Contrainte** : toutes les slides sont générées par les modules Python de `scripts/slides/` ; leur total est une sortie de fabrication. Le PPTX ne doit jamais être modifié directement : une régénération l'écraserait. Les composants de la grille IGPDE-DSFR sont centralisés dans `scripts/igpde_dsfr_components.py` et `finalize_pptx()` finalise langue, ordre de lecture, métadonnées et quarantaine macOS.
- **Impact** : toute correction de contenu ou de mise en page doit être faite dans le module source, puis régénérée par `make deck`.
- **Décision / prochaine vérification** : conserver les paramètres de session lus depuis `config.yml` et vérifier les avertissements de pied de page lors de toute modification visuelle.
- **Composants affectés** : `scripts/slides/`, `scripts/assemble.py`, `scripts/igpde_dsfr_components.py`, `config.yml`, PPTX du pack.

### Production du pack

- **Date** : 2026-09-28
- **Source** : `Makefile`, `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : `make pack` régénère les PDF, puis vérifie avec `make fraicheur-pack` que les documents Sami, les checklists, la grille XLSX et le deck WCAG ne sont ni absents ni plus anciens que leurs sources. Il régénère ensuite le deck, copie les supports et vérifie les outils, sans relancer `make sami`, `make checklist`, `make grille` ni `make wcag`.
- **Impact** : aucun pack ne peut être construit avec une version silencieusement dépassée de ces ressources.
- **Décision / prochaine vérification** : lorsque le contrôle bloque, exécuter uniquement la commande indiquée (`make sami`, `make checklist`, `make pdf`, `make grille` ou `make wcag`), vérifier son résultat, puis relancer `make pack`.
- **Composants affectés** : `_source/`, `03-easy-checks/`, `wcag/`, `livrables-IGPDE-2026-102846/`.

## 3. Sources, livrables et patrimoine pédagogique

### Paramètres de session

- **Date** : 2026-09-28
- **Source** : `config.yml`, `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : le code, la date, le pied de page, le nom du deck, le dossier de livraison et l'URL du site lus par la fabrication sont centralisés dans `config.yml`.
- **Impact** : un changement de session demande aussi de renommer le dossier du pack, de mettre à jour les documents administratifs et de rechercher les anciennes valeurs dans `docs/` et les Markdown structurants.
- **Décision / prochaine vérification** : traiter un changement de session comme une migration documentaire complète, pas comme une seule modification de configuration.
- **Composants affectés** : `config.yml`, `docs/`, Markdown structurants, documents administratifs et pack.

### Ressources pédagogiques

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `_source/exercice-sami-matrice.yml`, `03-easy-checks/evaluation_contract.yml`.
- **Statut** : active.
- **Contrainte** : les documents Sami sont générés depuis `_source/`; la grille d'audit est générée dans `03-easy-checks/` et dans le site ; le deck WCAG condensé est régénéré par `make wcag`. Les cartes, bandeaux et autres ressources fixes ne sont pas régénérés.
- **Impact** : il faut distinguer les ressources à reconstruire, les sources éditées à la main et les ressources fournies, afin de ne pas écraser un livrable ou une correction pédagogique.
- **Décision / prochaine vérification** : consulter la section « Qui fabrique quoi dans le pack » d'`AGENTS.md` avant toute modification d'un livrable.
- **Composants affectés** : `_source/`, `03-easy-checks/`, `wcag/`, `livrables-IGPDE-2026-102846/`.

### Contrat des points de contrôle rapides

- **Date** : 2026-09-28
- **Source** : `03-easy-checks/evaluation_contract.yml`, `validate.py`, `AGENTS.md`.
- **Statut** : active et vérifiée.
- **Contrainte** : le contrat d'évaluation décrit les 13 pages des points de contrôle rapides et le schéma minimal que `validate.py` applique au site. Le générateur de squelette a servi à amorcer les pages, mais elles sont maintenues à la main depuis juillet 2026.
- **Impact** : un contrat ou une page incohérente fait échouer la validation ; relancer aveuglément le générateur écraserait des corrections éditoriales réalisées depuis sa première génération.
- **Décision / prochaine vérification** : modifier les pages à la main et ne relancer `scripts/generate_easy_checks_site_skeleton.py` qu'après comparaison du diff complet.
- **Composants affectés** : `03-easy-checks/evaluation_contract.yml`, `scripts/generate_easy_checks_site_skeleton.py`, `validate.py`, `docs/`.

### Site d'exercice et publication à sens unique

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `Makefile`, `PUBLIER-SITE.md`.
- **Statut** : active et vérifiée.
- **Contrainte** : `docs/` est l'unique source du site d'exercice. `publication-site/` fournit ses trois fichiers racine adaptés. Le dépôt public `git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git` est une copie de publication, servie à l'adresse `https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/`.
- **Impact** : le flux va de l'usine vers le site, jamais dans l'autre sens. Les deux clones locaux du site sont des destinations de publication, non des sources éditables.
- **Décision / prochaine vérification** : modifier `docs/`, lancer `make verifier`, puis `make publier-site`. Ne jamais modifier, commiter ou pousser un clone du site.
- **Composants affectés** : `docs/`, `publication-site/`, clone de publication dans le pack, clone de consultation voisin, dépôt GitHub Pages.

## 4. Fonctionnalités et capacité de l'usine

| Fonctionnalité | État | Source de preuve | Limite ou contrainte |
|---|---|---|---|
| Environnement reproductible et hooks Git | Disponible | `Makefile`, `requirements.lock`, `.githooks/` | Requiert l'outillage macOS et `uv`. |
| Deck IGPDE-DSFR généré | Disponible | `scripts/assemble.py`, `scripts/slides/` | Sources Python uniquement ; total déterminé par la génération ; aucune retouche directe du PPTX. |
| Finalisation accessible du PPTX | Disponible | `finalize_pptx()` | Une relecture visuelle humaine demeure nécessaire. |
| Documents Sami, grille XLSX et deck WCAG | Disponible | cibles `sami`, `grille`, `wcag` | À régénérer avant `make pack` si leurs sources changent. |
| PDF générés et démo hors ligne | Disponible | cibles `pdf`, `supports` | Les six PDF générés doivent être PDF/UA-1. Les deux jeux de cartes externes sont destinés à l'impression et ne déclarent pas PDF/UA-1 ; LibreOffice n'est pas appelé par ces cibles. |
| Validation et recette du site | Disponible | `validate.py`, `make recette` | La recette visuelle requiert l’installation locale verrouillée via `make installer-recette`. |
| Publication GitHub Pages | Disponible | `make publier-site` | Publication contrôlée depuis `docs/` ; aucun édit direct du clone. |

## 5. Sécurité, Git et dépôt public

### Contenu public et données sensibles

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : le dépôt est public. Il ne doit contenir ni coordonnées personnelles de tiers, ni convocation nominative, ni transcription de conversation d'agent, ni informations logistiques de session. Les secrets restent hors versionnement et sont fournis par variables d'environnement si nécessaire.
- **Impact** : les notes, scripts, Markdown et documents de travail doivent être relus avant ajout au dépôt.
- **Décision / prochaine vérification** : conserver convocations et informations nominatives hors du dépôt ; vérifier le diff avant commit.
- **Composants affectés** : tout fichier versionné, `Codex.local.md` ignoré, documents administratifs du pack.

### Contrôles Git

- **Date** : 2026-09-28
- **Source** : `.githooks/pre-commit`, `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : le hook bloque les verrous Office, les fichiers de plus de 50 Mo, les convocations, les installeurs `.msi` et `.exe`, les tirets cadratins dans `scripts/` et les chemins personnels absolus dans les zones surveillées. Il ne se contourne jamais avec `--no-verify`.
- **Impact** : la conformité du contenu et des fichiers est contrôlée avant chaque commit.
- **Décision / prochaine vérification** : installer les hooks avec `make installer`, utiliser SSH pour Git et corriger la cause d'un rejet au lieu de contourner le hook.
- **Composants affectés** : `.githooks/`, `.gitignore`, fichiers suivis par Git.

### Artefacts temporaires et livrables suivis

- **Date** : 2026-09-28
- **Source** : `.gitignore`, `AGENTS.md`.
- **Statut** : active et vérifiée.
- **Contrainte** : `.gitignore` exclut la QA, les temporaires, les verrous Office et le deck généré à la racine. Le deck copié dans le pack et les DOCX livrés ne sont pas concernés et restent versionnés.
- **Impact** : la présence d'un fichier sur le disque ne prouve pas son suivi par Git ; le deck de travail à la racine peut être régénéré sans apparaître dans l'état Git.
- **Décision / prochaine vérification** : vérifier un livrable attendu avec `git ls-files`, en particulier après une modification d'ignore globale ou locale.
- **Composants affectés** : `.gitignore`, `.qa/`, `tmp/`, deck de travail à la racine, `livrables-IGPDE-2026-102846/`.

## 6. Données, droits et sobriété

### Absence de service applicatif persistant

- **Date** : 2026-09-28
- **Source** : `architecture-c4-slides.md`, `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : l'usine est une chaîne locale de fichiers et le site d'exercice est statique. Aucun backend ni stockage applicatif persistant n'est prévu.
- **Impact** : la confidentialité dépend avant tout du contenu publié et de la maîtrise des dépôts, plutôt que d'un modèle de données ou de comptes utilisateurs.
- **Décision / prochaine vérification** : ne pas introduire de collecte ou de persistance de données sans cadrage explicite.
- **Composants affectés** : `docs/`, scripts locaux, dépôts GitHub.

### Information sur les données personnelles

- **Date** : 2026-09-28
- **Source** : `docs/donnees-personnelles.html`, `docs/mentions-legales.html`.
- **Statut** : active et vérifiée.
- **Contrainte** : le site comporte des pages dédiées aux données personnelles et aux mentions légales, cohérentes avec son absence de collecte applicative prévue.
- **Impact** : toute évolution qui introduirait une collecte, des mesures d'audience ou une soumission vers un serveur devrait être cadrée et répercutée dans ces pages.
- **Décision / prochaine vérification** : relire ces informations avant toute évolution du parcours ou des données traitées.
- **Composants affectés** : `docs/donnees-personnelles.html`, `docs/mentions-legales.html`, `docs/`.

### Droits des médias et accessibilité éditoriale

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, ressources du pack.
- **Statut** : active.
- **Contrainte** : les médias, cartes et ressources fixes conservent leurs crédits et licences à proximité. Les documents accessibles déclarent une langue cohérente en français ; les défauts des versions inaccessibles sont intentionnels et pédagogiques.
- **Impact** : une ressource ajoutée sans licence, crédit ou alternative adaptée ne peut pas être intégrée au pack public.
- **Décision / prochaine vérification** : documenter les crédits au plus près de la ressource et conserver les distinctions entre versions accessibles et versions d'exercice.
- **Composants affectés** : `docs/`, `livrables-IGPDE-2026-102846/`, `_source/`, cartes et médias.

### Sous-titres et transcriptions locales

- **Date** : 2026-09-28
- **Source** : `docs/assets/shared/media/`, `03-easy-checks/evaluation_contract.yml`.
- **Statut** : active et vérifiée.
- **Contrainte** : les parcours média du site s'appuient sur des fichiers locaux de sous-titres et de transcription, notamment au format `.vtt`.
- **Impact** : supprimer ou désynchroniser ces fichiers dégrade l'accessibilité et la cohérence des exercices sur les médias.
- **Décision / prochaine vérification** : vérifier les sous-titres et transcriptions lors de chaque remplacement de média ou d'URL intégrée.
- **Composants affectés** : `docs/assets/shared/media/`, pages EC09 à EC11 du site, `03-easy-checks/evaluation_contract.yml`.

## 7. Qualité et vérification

### Vérification automatisée du dépôt et du site

- **Date** : 2026-09-28
- **Source** : `Makefile`, `tests/`, `validate.py`, résultat vérifié de `make verifier`.
- **Statut** : active et vérifiée.
- **Contrainte** : `make verifier` exécute la suite de tests, valide le site, contrôle les PDF livrés et lance les vérifications de dépôt. Le code de sortie porte le verdict.
- **Impact** : une modification de source ou de configuration doit être vérifiée avant livraison ou publication.
- **Décision / prochaine vérification** : lancer `make verifier` après toute modification qui affecte la fabrication, le site ou les contrôles.
- **Composants affectés** : `tests/`, `validate.py`, `docs/`, PDF livrés, hook Git.

### QA sur copie de travail

- **Date** : 2026-09-28
- **Source** : `scripts/qa_pptx.py`, `tests/conftest.py`, `AGENTS.md`.
- **Statut** : active et vérifiée.
- **Contrainte** : `make qa` travaille sur `.qa/formation-test-qa.pptx`, désignée par `QA_PPTX_PATH`, et non directement sur le deck stable du pack.
- **Impact** : tester ou interpréter le mauvais PPTX peut produire une fausse confiance sur le livrable final.
- **Décision / prochaine vérification** : lire `.qa/qa-pptx-report.md` et son statut, puis régénérer le deck de livraison dans le flux normal.
- **Composants affectés** : `scripts/qa_pptx.py`, `tests/conftest.py`, `.qa/formation-test-qa.pptx`, PPTX du pack.

### Qualité du deck et pied de page

- **Date** : 2026-09-28
- **Source** : `scripts/qa_geometry.py`, `tests/baselines/known-geometry-violations.json`, résultat vérifié de `make qa`.
- **Statut** : active et vérifiée.
- **Contrainte** : `make qa` doit produire un rapport `.qa/qa-pptx-report.md` au statut `CONVERGED`. Les composants de contenu sont limités à `BOTTOM_CONTENT` (6,80 pouces) et la base de référence ne tolère plus aucune violation de pied de page.
- **Impact** : un avertissement de pied de page est un défaut de composition à corriger, sans déplacer la ligne ou les logos institutionnels.
- **Décision / prochaine vérification** : lire le rapport QA, corriger à la source puis compléter par une relecture visuelle humaine des slides modifiées.
- **Composants affectés** : `scripts/qa_geometry.py`, `scripts/slides/`, `.qa/`, base de référence géométrique.

### Correcteur QA conservateur et leçons techniques

- **Date** : 2026-09-28
- **Source** : `scripts/qa_corrector.py`, `tests/test_qa_corrector.py`, `lessons.md`.
- **Statut** : active et vérifiée.
- **Contrainte** : le correcteur QA ne traite automatiquement que les accents français sûrs et localisés dans les chaînes Python. Les défauts de mise en page, d'alternative textuelle ou de taille de police restent des décisions humaines signalées comme omissions structurées.
- **Impact** : aucune correction automatique ne doit recomposer une slide ou inventer une alternative ; les pièges connus documentés dans `lessons.md` restent à consulter avant une évolution du deck.
- **Décision / prochaine vérification** : lire le rapport de corrections et le diff avant toute application ; corriger à la source les omissions de mise en page, d'alternative ou de police.
- **Composants affectés** : `scripts/qa_corrector.py`, `tests/test_qa_corrector.py`, `.qa/`, `lessons.md`, `scripts/slides/`.

### PDFs accessibles

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `Makefile`, contrôles de `make verifier`.
- **Statut** : active.
- **Contrainte** : `make pdf` n'accepte que les sorties PDF/UA-1. En cas d'échec, le générateur s'arrête et laisse le livrable précédent en place.
- **Impact** : la fabrication ne remplace pas silencieusement un PDF accessible par un document non conforme.
- **Décision / prochaine vérification** : conserver les tableaux Markdown entiers sur une page et contrôler l'état PDF/UA-1 avant livraison.
- **Composants affectés** : `fiche-pratique/`, `wcag/`, `liens-tp-en-ligne.md`, PDF du pack.

## 8. Exploitation et continuité

### Installation et reprise locale

- **Date** : 2026-09-28
- **Source** : `Makefile`, `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : `make installer` prépare l'environnement Python verrouillé et active les hooks. Sans `.venv`, les commandes peuvent utiliser un Python de repli sans garantie sur les dépendances.
- **Impact** : une reprise d'usine commence par l'installation, puis par la lecture des règles d'`AGENTS.md` et de la cible concernée.
- **Décision / prochaine vérification** : relancer `make installer` lorsqu'un environnement local est recréé ou que le verrou de dépendances évolue.
- **Composants affectés** : `.venv/`, `requirements.lock`, `.githooks/`, `Makefile`.

### Quarantaine macOS des fichiers générés

- **Date** : 2026-09-28
- **Source** : `scripts/assemble.py`, `AGENTS.md`.
- **Statut** : active.
- **Contrainte** : les fichiers Office générés sous macOS peuvent porter l'attribut `com.apple.quarantine`. La finalisation du PPTX traite ce point avant remise à l'utilisateur.
- **Impact** : sans ce post-traitement, PowerPoint ou Excel peut ouvrir un fichier en mode protégé et empêcher sa sauvegarde.
- **Décision / prochaine vérification** : préserver `finalize_pptx()` dans toute évolution de la chaîne de deck et vérifier l'ouverture des livrables lorsqu'un nouveau type de fichier est ajouté.
- **Composants affectés** : `scripts/assemble.py`, `scripts/igpde_dsfr_components.py`, PPTX et fichiers Office générés.

### Livraison, publication et clones de site

- **Date** : 2026-09-28
- **Source** : `AGENTS.md`, `Makefile`, `PUBLIER-SITE.md`.
- **Statut** : active.
- **Contrainte** : `make publier-site` valide le site puis effectue sa synchronisation vers le clone de publication, copie les trois documents racine adaptés, effectue le commit et le push du dépôt du site, puis avance le clone de consultation lorsqu'il existe. Les installeurs ne sont pas versionnés ; `make outils-telecharger` récupère les trois fichiers disposant d'une adresse directe, tandis que PAC est déposé manuellement ; `make outils` vérifie ensuite leurs empreintes.
- **Impact** : une publication est une opération distincte d'un commit de l'usine et les clones restent des destinations gérées par la cible.
- **Décision / prochaine vérification** : préparer et vérifier l'usine, puis publier uniquement par la cible prévue ; contrôler le manifeste des outils avant constitution du pack.
- **Composants affectés** : `docs/`, `publication-site/`, clones locaux du site, `livrables-IGPDE-2026-102846/outils/`.

## Références opérationnelles

- Règles et parcours de fabrication : `AGENTS.md`.
- Architecture de l'usine : `architecture-c4-slides.md`.
- Cibles et enchaînements : `Makefile`.
- Publication du site : `PUBLIER-SITE.md`.
- Sources et suivi historique : `todo.md`, `lessons.md`, `notes/readme-causal.md`.
