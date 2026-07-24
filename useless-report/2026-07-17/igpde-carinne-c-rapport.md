# Rapport projet - Formation IGPDE Carinne C. - depuis la création visible - 17 juillet 2026

Périmètre : sous-dossier projet `/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/`, dans le dépôt Git racine `/Users/alex/Claude`.

Période : depuis la création visible du projet dans Git local, premier commit scoped `325b30b7` du 11 avril 2026, jusqu'au 17 juillet 2026.

Focus : formation accessibilité numérique 102638, deck PPTX, exercices Sami, site Easy Checks, livrables IGPDE, audits et validations disponibles localement.

## 1. Introduction au projet et état à l'instant T

Le projet porte une formation accessibilité numérique d'une journée pour l'IGPDE, commanditée par Carinne C. Le public visé est constitué de communicants et d'agents non développeurs. Le coeur du chantier est un support PowerPoint de formation, complété par des exercices Word, un site d'entraînement aux points de contrôle rapides W3C, une grille d'audit XLSX et des fiches pratiques.

L'état local au 17 juillet 2026 montre un projet largement livré et outillé : le deck principal `formation-102638-juin-2026.pptx` est présent, le pack `IGPDE-102638-livrables-juin-2026/` contient les livrables formateur, le site d'exercice est publié via GitHub Pages, et les scripts de génération/QA sont documentés. Le `README.md` conserve toutefois un statut de relecture finale avant diffusion, avec une échéance du 4 juin 2026 désormais passée ; ce point doit être lu comme un écart documentaire à arbitrer, pas comme une preuve que la session n'a pas eu lieu.

État Git avant création du présent rapport : branche globale `main`, remote `origin` sur `git@github.com:Alexmacapple/claude-workflow-perso.git`, branche locale en avance de `1` commit sur `origin/main`. Le sous-dossier projet ne présentait pas de modification locale suivie ou non suivie ; des entrées non suivies existaient hors périmètre ou dans d'autres projets du monorepo.

## 2. Dates structurantes

| Date | Élément | Lecture pour le rapport |
|---|---|---|
| 11 avril 2026 | Premier commit scoped `325b30b7` | Début visible du projet dans l'historique Git local. |
| 17 avril 2026 | Commits de template et composants IGPDE-DSFR | Mise en place de la génération PPTX, des layouts et des composants réutilisables. |
| 3 mai 2026 | Passation exercice Sami | L'exercice Word passe à `21` erreurs pédagogiques documentées dans `_source/exercice-sami-spec.md` et `_source/exercice-sami-diff.md`. |
| 4-5 mai 2026 | Construction du site Easy Checks | Les trois variantes du site sont consolidées : `site-inaccessible/`, `site-aide-correction/`, `site-accessible/`. |
| 16-17 mai 2026 | Consolidation des livrables | Passage au deck `138` slides, fiches pratiques, documentation C4, README causal et livrables formateur. |
| 22 mai 2026 | QA PPTX PRD-119 | Ajout de l'orchestrateur QA, du correcteur conservateur, de la source map et des tests géométriques. |
| 4 juillet 2026 | Audit RGAA ciblé et recette visuelle site | Ajout des audits locaux sur le site corrigé, consignes de site, lanceur local et résultats ShipGuard. |
| 5-6 juillet 2026 | Lots de slides IA et raffinement alt | Ajout de lots `outputs/ia-slides/`, dont `alt raffinement v2` le 6 juillet. |
| 17 juillet 2026 | Date du présent rapport | État à l'instant T depuis les fichiers et l'historique Git local. |

## 3. Résumé exécutif

- Le projet est un support de formation complet, pas seulement un deck : il combine PPTX, site d'exercice, DOCX pédagogiques, grille XLSX, fiches mémo, audits et procédure de publication.
- Le deck principal est présent sous `formation-102638-juin-2026.pptx`; `unzip -t` ne détecte pas d'erreur dans le fichier.
- Le site Easy Checks est structuré en `3` variantes de `14` pages chacune : index + `13` points de contrôle rapides.
- La livraison formateur est conservée dans `IGPDE-102638-livrables-juin-2026/`, avec deck, supports PDF, TP Word et outils.
- Les contrôles Python n'ont pas pu être relancés dans l'environnement global courant, faute de dépendances installées (`PyYAML`, `pytest`, `python-pptx`).
- Les audits du 4 juillet documentent une page corrigée sans non-conformité confirmée dans le périmètre testé, mais avec limites explicites : pas de certification externe, pas de lecteur d'écran réel, contrastes à mesurer manuellement.
- La recette visuelle ShipGuard du site indique `10` réussites et `4` échecs sur `14` pages, principalement liés à des ressources média locales manquantes et à une page possiblement blanche.

## 4. Livrables et preuves visibles

### Livrables de formation

| Fichier ou dossier | Rôle | État visible localement |
|---|---|---|
| `formation-102638-juin-2026.pptx` | Deck principal de formation | Présent, archive PPTX valide selon `unzip -t`. |
| `IGPDE-102638-livrables-juin-2026/` | Pack formateur remis ou préparé pour l'IGPDE | Présent, avec deck, documents source, fiches, TP Word et outils. |
| `_source/sami-doc-inaccessible.docx` | Exercice Sami version à auditer | Présent. |
| `_source/sami-doc-aide-correction.docx` | Exercice Sami avec aide | Présent. |
| `_source/sami-doc-accessible.docx` | Exercice Sami version corrigée | Présent. |
| `03-easy-checks/grille-audit-easy-checks.xlsx` | Grille d'audit source | Présente. |
| `docs/assets/downloads/grille-audit-easy-checks.xlsx` | Grille téléchargeable depuis le site | Présente, même taille que la grille source. |
| `fiche-pratique/memo-word-accessibilite.pdf` | Mémo Word | Présent. |
| `fiche-pratique/memo-libreoffice-writer-accessibilite.pdf` | Mémo LibreOffice Writer | Présent. |
| `wcag/WCAG en langage clair - condensé.pptx` | Deck WCAG condensé | Présent. |

### Architecture de génération

| Élément | Rôle | Point de vigilance |
|---|---|---|
| `scripts/assemble.py` | Assemble le deck principal depuis les modules Python | Toute modification durable doit passer par les scripts, pas par une édition directe du PPTX. |
| `scripts/slides/` | Modules de slides | `139` fichiers Python visibles ; le deck stable est documenté comme `138` slides. |
| `scripts/igpde_dsfr_components.py` | Bibliothèque de composants et post-traitement accessibilité PPTX | `finalize_pptx()` est obligatoire avant livraison. |
| `scripts/qa_pptx.py` | Boucle QA PRD-119 | Travaille sur une copie `.qa/`, pas directement sur le deck stable. |
| `REEXPORTER-DECK-PPTX.md` | Mode d'emploi de réexport | Source clé avant toute régénération finale. |

## 5. Deck PPTX et pédagogie

Le support principal est construit pour une formation d'une journée en `4` modules, dans un ordre impératif : introduction/cadre légal, Word accessible, points de contrôle rapides W3C, puis réseaux sociaux. Les consignes projet interdisent d'inverser cet ordre.

Le pipeline est programmatique : chaque slide est produite par un module Python, l'assembleur injecte la numérotation et le contexte, puis le post-traitement finalise l'accessibilité du PPTX. Cette architecture répond à trois contraintes fortes : volume du support, cohérence visuelle IGPDE/DSFR et capacité à rejouer les corrections.

Les règles projet rappellent deux limites importantes :

- les contrôles automatisés ne remplacent pas une passe visuelle PowerPoint ;
- les slides générées par script et les slides retouchées manuellement ne doivent pas être mélangées sans identifier leur régime de maintenance.

## 6. Exercice Sami

L'exercice Sami est un exercice Word centré sur `21` critères à vérifier dans `3` DOCX. La passation du 3 mai 2026 documente une montée en richesse progressive : fausses listes, faux titres, tableau sans en-tête, texte en image, passage anglais non balisé, paragraphes vides, propriétés document absentes et autres défauts pédagogiques.

Les sources de vérité sont :

- `_source/exercice-sami-spec.md` ;
- `_source/exercice-sami-diff.md` ;
- `scripts/generate_exercice_sami.py` ;
- les trois DOCX Sami versionnés.

La règle pédagogique importante est de ne pas distribuer la checklist au moment de l'identification : les stagiaires doivent d'abord diagnostiquer sans filet, puis utiliser la checklist pour consolider leur jugement.

## 7. Site Easy Checks et publication

Le site d'exercice vit dans `docs/` et sert de source pour le dépôt standalone public `easy-check-igpde`.

URL publique documentée : <https://alexmacapple.github.io/easy-check-igpde/>

Le contenu publié comprend :

- `docs/index.html` ;
- `docs/site-inaccessible/` : site à auditer, avec erreurs volontaires ;
- `docs/site-aide-correction/` : version avec indices et aide ;
- `docs/site-accessible/` : témoin corrigé ;
- pages légales : accessibilité, mentions légales, données personnelles, plan du site ;
- assets DSFR embarqués localement ;
- grille XLSX téléchargeable.

Le dossier `docs/` contient `14` pages HTML par variante de site : une page d'index et `13` pages de points de contrôle rapides. La procédure de publication impose de régénérer, valider puis synchroniser `docs/` vers le dépôt standalone.

## 8. Audits, QA et validations

Contrôles exécutés pendant cette passe :

| Commande | Résultat |
|---|---|
| `unzip -t formation-102638-juin-2026.pptx` | OK, aucune erreur détectée dans l'archive PPTX. |
| `python3 validate.py` | Non exécuté jusqu'au bout : `ModuleNotFoundError: No module named 'yaml'`. |
| `python3 -m pytest tests/ -q` | Non exécuté : module `pytest` absent. |
| Inspection PPTX via `python-pptx` | Non exécutée : module `pptx` absent. |

Preuves déjà présentes dans le projet :

- `audit-rgaa-index-2026-07-04.md` : audit ciblé de la page d'accueil exercice, aucune non-conformité RGAA avérée sur cette passe, avec limites.
- `audit-rgaa-106-site-accessible-index-2026-07-04.md` : page `site-accessible/index.html`, `33` critères conformes, `0` non conforme, `60` non applicables, `13` non testés dans le périmètre documenté.
- `docs/visual-tests/_results/report.md` : recette ShipGuard du site corrigé, `14` pages, `10` réussites, `4` échecs.
- `docs/visual-tests/_results/audit-results.json` : `3` bugs high severity en accessibilité, report-only, `0` fichier modifié.

Conclusion de validation : le fichier PPTX stable est intègre au niveau archive. Les validations Python du projet doivent être rejouées dans un environnement avec les dépendances de `requirements.txt` avant toute nouvelle diffusion.

## 9. Sorties IA de juillet

Le dossier `outputs/ia-slides/` contient des lots d'images générées ou récupérées en juillet :

| Dossier | Slides PNG |
|---|---:|
| `2026-07-04-bureautique-21-slides` | 21 |
| `2026-07-04-checklist-bureautique` | 4 |
| `2026-07-04-checklist-reseaux-sociaux` | 3 |
| `2026-07-05-cadre-legal-53-slides` | 53 |
| `2026-07-05-travaux-pratique-bureautique` | 27 |
| `2026-07-05-web-31-slides` | 31 |
| `2026-07-06-alt-raffinement-v2` | 6 |

Ces sorties ne remplacent pas le deck principal. Elles constituent des artefacts de travail ou de raffinement visuel à rattacher explicitement au pipeline de formation si une nouvelle version du support est demandée.

## 10. Reste à faire côté projet

- Clarifier le statut documentaire post-session : `README.md` parle encore de relecture finale avant diffusion et d'une session du 4 juin 2026, alors que la date est passée et qu'un pack livrable complet existe.
- Si une nouvelle diffusion est demandée, installer les dépendances Python, puis rejouer `python3 validate.py`, `python3 -m pytest tests/ -q`, `python3 scripts/qa_pptx.py . --max-iterations 5 --clean` et `unzip -t formation-102638-juin-2026.pptx`.
- Traiter ou documenter les `4` échecs ShipGuard du site corrigé : EC05 possiblement blanche, médias locaux manquants pour EC09, EC10 et EC11.
- Refaire la passe visuelle humaine PowerPoint si le deck est régénéré ou rediffusé.
- Décider si les lots `outputs/ia-slides/` de juillet restent des artefacts de recherche ou deviennent un nouveau livrable intégré.
- Nettoyer ou ignorer explicitement les artefacts locaux visibles dans le dossier projet (`.DS_Store`, `__pycache__`, temporaires Office) lors d'une passe d'hygiène Git.

## 11. Traçabilité Git

Activité Git visible sur le sous-dossier projet :

- `132` commits scoped hors merge ;
- `1` commit de merge scoped ;
- premier commit scoped : `325b30b7`, 11 avril 2026, `Reorganisation racine + routing Tailscale Funnel 5G + page d'index DSFR` ;
- dernier commit scoped : `a901d4bf`, 6 juillet 2026, `Ajoute slides alt raffinement v2` ;
- auteurs visibles : `Alex` sur `107` commits, `Alexandra Guiderdoni` sur `16` commits, `alexmacapple` sur `10` commits ;
- état courant du projet : `2095` fichiers suivis dans le sous-dossier.

Commits structurants :

| Commit | Date | Message |
|---|---|---|
| `325b30b7` | 11 avril 2026 | `Reorganisation racine + routing Tailscale Funnel 5G + page d'index DSFR` |
| `d5cd1693` | 17 avril 2026 | `Ajout template IGPDE-DSFR - formation 102638 accessibilité numérique` |
| `291af59a` | 3 mai 2026 | `feat: exercice Sami 21 erreurs (sommaire, texte-image, tableau fusionne)` |
| `62125a3c` | 4 mai 2026 | `Finalise les points de controle rapides IGPDE` |
| `0717ae0b` | 16 mai 2026 | `Ajout fiches pratiques accessibilite Word et LibreOffice Writer` |
| `7c1466c6` | 17 mai 2026 | `Mise a jour compteur 131 vers 138 slides et ajout tache impressions papier` |
| `c3e1d0ab` | 22 mai 2026 | `feat: Ajout orchestrateur QA PPTX` |
| `40b06231` | 4 juillet 2026 | `Ajoute lanceur local du site IGPDE` |
| `80cc4a4f` | 4 juillet 2026 | `Ajoute consignes du site IGPDE` |
| `a901d4bf` | 6 juillet 2026 | `Ajoute slides alt raffinement v2` |

Sources locales lues ou inspectées :

- `AGENTS.md`
- `README.md`
- `contraintes.md`
- `todo.md`
- `REEXPORTER-DECK-PPTX.md`
- `IGPDE-102638-livrables-juin-2026/README.md`
- `_source/passation-session-2026-05-03.md`
- `_source/passation-session-2026-05-04.md`
- `docs-publication.md`
- `docs/AGENTS.md`
- `audit-rgaa-index-2026-07-04.md`
- `audit-rgaa-106-site-accessible-index-2026-07-04.md`
- `docs/visual-tests/_results/report.md`
- `docs/visual-tests/_results/visual-results.json`
- `docs/visual-tests/_results/audit-results.json`
- `outputs/ia-slides/`

Commandes exécutées pour le rapport :

```text
git status -sb
git status --short -- .
git log --date=short --pretty=format:'%h %ad %an %s' -- .
git rev-list --count --no-merges HEAD -- .
git rev-list --count --merges HEAD -- .
git ls-files -- .
find docs -maxdepth 3 -type f
find outputs/ia-slides -maxdepth 2 -type f
python3 validate.py
python3 -m pytest tests/ -q
unzip -t formation-102638-juin-2026.pptx
```

Limites : le rapport est fondé sur l'état local du disque et l'historique Git local. Les statistiques Git détaillées par fichier touché n'ont pas été calculées jusqu'au bout car la commande a dépassé le délai raisonnable. Les validations Python nécessitent un environnement avec les dépendances de `requirements.txt`.
