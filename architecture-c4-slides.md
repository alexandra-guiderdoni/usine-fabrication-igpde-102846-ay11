# Architecture C4 de l'usine IGPDE 102846

> État observé le 28 septembre 2026. Ce document décrit l'usine entière : la fabrication du pack, les contrôles et la publication du site des travaux pratiques. Il ne décrit pas seulement le générateur de slides.

## Objet, périmètre et conventions

L'usine fabrique les ressources de la formation IGPDE « L'accessibilité numérique pour la bureautique et le web » (code 102846, session du 9 octobre 2026). Elle produit un pack versionné pour l'IGPDE et alimente le site public des travaux pratiques. Les paramètres de session utilisés par la fabrication sont centralisés dans `config.yml`.

Cette vue adopte C4 de manière pragmatique :

- C1 montre les personnes, l'usine et les systèmes externes utiles ;
- C2 montre les exécutables locaux et les stockages qui participent réellement au flux ;
- C3 détaille uniquement l'assembleur de deck, partie où la décomposition en composants aide à modifier sans casser la chaîne ;
- les vues dynamiques et de déploiement décrivent les commandes et emplacements effectivement employés.

Les bibliothèques Python, le gabarit PPTX, les modules de slides et les fichiers Markdown ne sont pas des conteneurs C4 : ce sont des dépendances ou des données internes. Ils apparaissent donc comme tels, sans les faire passer pour des applications autonomes.

```text
Limite du système : dépôt usine-fabrication-igpde-102846-ay11
  Sources versionnées -> commandes locales Make/Python -> livrables et publication
```

## C1 - Contexte du système

| Élément | Type C4 | Rôle et relation avec l'usine |
|---|---|---|
| Formateur ou mainteneur | Personne | Modifie les sources, lance les fabrications, interprète les contrôles et effectue la relecture humaine. |
| Usine de formation 102846 | Système logiciel | Fabrique le deck, les ressources du pack, les documents PDF et le site des TP depuis ses sources versionnées. |
| IGPDE | Organisation | Reçoit le pack de formation préparé pour la session. |
| Stagiaire | Personne | Consulte les travaux pratiques publiés et utilise les ressources distribuées pendant la formation. |
| Dépôt des TP et GitHub Pages | Système externe | Reçoit une copie de publication du site et l'expose sur le Web. Il n'est jamais une source de retour pour l'usine. |

```text
                    modifie, fabrique et vérifie
[Formateur ou mainteneur] -------------------------> [Usine de formation 102846]
                                                          |
                                       fabrique le pack   | publie une copie du site
                                                          v
                                                    [IGPDE] ---- remet ----> [Stagiaire]
                                                          \
                                                           \ synchronise
                                                            v
                                      [Dépôt des TP et GitHub Pages] <--- consulte --- [Stagiaire]
```

Le flux est volontairement à sens unique : les pages modifiées dans `docs/` sont validées puis copiées vers le dépôt des TP. Le dépôt publié et ses deux clones locaux sont des destinations de publication, jamais des sources à modifier.

## C2 - Conteneurs et stockages de l'usine

### Éléments internes

| Élément | Nature | Responsabilité | Entrées et sorties principales |
|---|---|---|---|
| Orchestrateur local | Application en ligne de commande : `make` et le `Makefile` | Choisit l'interpréteur, enchaîne les cibles et porte les points d'entrée de l'usine. | Reçoit `make deck`, `make pack`, `make verifier`, `make publier-site` et les autres cibles ; lance les scripts Python. |
| Assembleur de deck | Application Python en ligne de commande : `scripts/assemble.py` | Découvre les modules, construit les 138 slides, applique les composants IGPDE-DSFR et finalise le PPTX. | Lit la configuration, le gabarit et les modules ; écrit le deck de travail puis le deck du pack par `make deck`. |
| Fabrication des ressources du pack | Applications Python : `scripts/fabriquer_pack.py` et `scripts/pack_supports.py` | Copie le deck complet, produit les PDF autorisés, prépare la démo hors ligne et rassemble les supports. | Lit les sources, les DOCX Sami et le deck complet ; écrit dans `livrables-IGPDE-2026-102846/`. |
| Vérification et recette | Commandes locales : `pytest`, `validate.py`, hooks Git, QA PPTX et ShipGuard | Détecte les régressions de dépôt, de site, de géométrie et de rendu avant livraison ou publication. | Lit les sources et les livrables ; écrit, selon la commande, les rapports sous `.qa/` ou `recette/reports/`. |
| Publication du site | Procédure locale portée par `make publier-site` | Valide, synchronise la source du site, copie les trois fichiers racine de publication puis pousse la copie vers le dépôt des TP. | Lit `docs/` et `publication-site/` ; écrit uniquement dans le clone de publication et avance le clone de consultation. |
| Sources versionnées | Stockage de fichiers Git | Conserve les paramètres, contenus, scripts, gabarits, tests, recette et ressources nécessaires à la fabrication. | Inclut notamment `config.yml`, `scripts/`, `docs/`, `_source/`, `fiche-pratique/`, `wcag/`, `03-easy-checks/` et le corpus préparatoire. |
| Pack de livraison | Stockage de fichiers versionné | Réunit les livrables destinés à l'IGPDE. | Dossier `livrables-IGPDE-2026-102846/`, alimenté par les commandes de fabrication. |

### Relations C2

```text
                                  +--------------------------------------------+
                                  |             Usine locale                    |
                                  |                                            |
 [Sources versionnées] ---------->| [Orchestrateur Make]                       |
        |                         |       |            |                       |
        |                         |       |            +--> [Vérification]     |
        |                         |       v                                    |
        |                         | [Assembleur de deck] --> deck de travail   |
        |                         |       |                                    |
        |                         |       v                                    |
        |                         | [Fabrication du pack] --> [Pack]           |
        |                         |                                            |
        +------------------------>| [Publication du site]                      |
                                  +------------------|-------------------------+
                                                     |
                                                     v
                             [Dépôt des TP et GitHub Pages, système externe]
```

Le générateur PDF contenu dans `vendor/` est une bibliothèque appelée par la fabrication des ressources du pack. Il ne constitue pas un conteneur : il n'a ni point d'entrée utilisateur ni cycle de déploiement propre.

### Points d'entrée effectifs

| Intention | Commande | Résultat attendu |
|---|---|---|
| Préparer l'environnement | `make installer` | Crée `.venv` depuis `requirements.lock` et active les hooks versionnés. |
| Générer le deck | `make deck` | Deck complet de 138 slides à la racine puis copie dans le pack. |
| Générer les dépendances ciblées | `make sami`, `make grille`, `make wcag` | Ressources Sami, grille XLSX ou deck WCAG avant un pack si leurs sources ont changé. |
| Fabriquer les documents et supports | `make pdf`, `make supports`, `make pack` | PDF/UA-1 contrôlés, démo hors ligne, documents du pack et deck copié. |
| Vérifier | `make verifier`, puis si nécessaire `make qa` et `make recette` | Tests, validation du site, contrôles Git, QA de deck et recette visuelle. |
| Publier le site | `make publier-site` | Validation, synchronisation, commit et push dans le dépôt des TP. |

`make pack` relance le deck et la fabrication du pack, mais ne régénère pas les documents Sami, la grille ni le deck WCAG. Ces trois cibles doivent donc être lancées au préalable lorsque leurs sources ont changé.

## C3 - Composants de l'assembleur de deck

L'assembleur est le seul conteneur qui mérite une vue interne détaillée : il concentre l'ordre des modules, les règles de composition, l'accessibilité du fichier et les garde-fous de génération.

| Composant | Fichier ou interface | Responsabilité |
|---|---|---|
| Chargeur de configuration | `scripts/config.py`, `config.yml` | Valide et expose le code de formation, la date, le pied de page, le nom du deck et le dossier de livraison aux générateurs et au Makefile. |
| Découverte et chargement des slides | `scripts/slides/__init__.py` | Trie les fichiers `NN_*.py` et leurs intercalaires alphabétiques, importe chaque module et exige une fonction `build(...)`. |
| Modules pédagogiques | `scripts/slides/*.py` | Produisent les 138 slides des quatre modules dans leur ordre lexical contrôlé. |
| Composants IGPDE-DSFR | `scripts/igpde_dsfr_components.py` | Crée les six layouts, les 17 composants `add_*`, les deux compositions `compose_*` et applique la grille visuelle. |
| Contexte de génération | `SlideContext` | Porte le numéro de slide, la date et le pied de page calculés au lieu de valeurs répétées dans les modules. |
| Carte de traçabilité QA | `scripts/qa_source_map.py` | Associe, si disponible, des éléments générés à leurs sources pour la boucle QA. |
| Finalisation accessible | `finalize_pptx()` | Fixe la langue, l'ordre de lecture, les éléments décoratifs, les métadonnées et la quarantaine macOS. |

```text
[config.yml] --> [Chargeur de configuration] --\
                                             |  \
[scripts/slides/] --> [Découverte / chargement] --> [Modules pédagogiques]
                                                       |
[Gabarit IGPDE] --------------------------------------> [Composants IGPDE-DSFR]
                                                       |
                                       [SlideContext] -+
                                                       v
                                            [Présentation en mémoire]
                                                       |
                    [qa_source_map, facultatif] ------>|
                                                       v
                                            [finalize_pptx()]
                                                       |
                                                       v
                              support-formation-102846-2026-IGPDE.pptx
```

La reconstruction du gabarit n'appartient pas au chemin normal : `scripts/rebuild_template_from_demo.py` n'est utilisé que si le gabarit IGPDE manque. `scripts/build_template.py` est historique et sa source IGPDE native n'est plus dans le dépôt ; il ne doit pas être modélisé comme une dépendance active de `assemble.py`.

## Vues dynamiques

### Produire et contrôler le pack

```text
1. Le mainteneur modifie une source versionnée.
2. Si nécessaire, il régénère Sami, la grille ou le deck WCAG.
3. `make deck` lance l'assembleur ; celui-ci charge la configuration,
   trie les modules, compose les slides et exécute `finalize_pptx()`.
4. `make pack` relance le deck puis appelle la fabrication du pack.
5. La fabrication refuse un deck partiel et compare le contenu OOXML
   avant de remplacer la copie livrée.
6. Les PDF ne remplacent le livrable précédent que lorsqu'ils déclarent PDF/UA-1.
7. `make verifier` exécute les tests, valide le site et les contrôles de dépôt.
8. `make qa` et une relecture visuelle humaine complètent le verdict si le deck a changé.
```

### Publier le site des travaux pratiques

```text
1. Le mainteneur modifie uniquement `docs/` et, si besoin, `publication-site/`.
2. `make verifier` contrôle le site source ; `make recette` apporte une recette visuelle.
3. `make publier-site` revalide le site.
4. La commande synchronise `docs/` vers le clone de publication,
   puis y installe `README.md`, `AGENTS.md` et `CLAUDE.md` depuis
   `publication-site/` sous leurs noms publics.
5. Elle crée le commit et le push du dépôt des TP, puis avance le clone local de consultation.
6. GitHub Pages sert la version poussée aux stagiaires.
```

Les clones locaux du site sont donc des sorties contrôlées : aucun humain ni agent ne les édite, ne les commit ni ne les pousse directement.

## Déploiement et dépendances d'exécution

```text
Poste macOS du mainteneur
  - dépôt Git de l'usine
  - Python 3.12, environnement `.venv` créé par `uv`
  - Make, Git et hooks `.githooks`
  - pandoc, pango et glib pour les PDF
  - LibreOffice pour les exports nécessaires
  - ShipGuard pour la recette visuelle
  - répertoires de travail, pack et deux clones locaux du site
          |
          | SSH, uniquement par `make publier-site`
          v
GitHub
  - dépôt `tp-fabrication-igpde-102846-ay11`
  - GitHub Pages : https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11/
```

Il n'y a pas de chaîne CI déclarée dans ce dépôt : l'installation, la génération, les contrôles et la publication sont aujourd'hui exécutés localement. Le dépôt Git de l'usine conserve les sources et le pack, tandis que le dépôt GitHub Pages ne conserve que la copie de publication du site.

## Qualité, limites connues et garde-fous

| Sujet | Garde-fou actuel | Limite à connaître |
|---|---|---|
| Régression fonctionnelle | `make verifier` exécute la suite de tests, la validation du site et les contrôles de dépôt. | Un succès atteste l'absence de régression détectée, pas une relecture pédagogique ou visuelle exhaustive. |
| Mise en page du deck | `make qa`, contrôles géométriques et relecture humaine. | Les superpositions fines exigent toujours une inspection visuelle. |
| Pied de page | La génération limite les composants à la zone de contenu et les tests imposent désormais zéro forme de contenu sous `BOTTOM_CONTENT` (6,80 pouces). | `_safe_top()` reste un filet de sécurité : son avertissement signale une mise en page à corriger et une relecture visuelle reste nécessaire pour exclure un chevauchement. |
| PDF | La fabrication vérifie la déclaration PDF/UA-1 avant de remplacer un PDF livré. | Les tableaux Markdown doivent rester composables sur une page, sinon la production est bloquée. |
| Site | `validate.py` contrôle le contrat de l'exercice, les liens, les ressources et les règles d'accessibilité ciblées. | La recette visuelle s'installe localement par `make installer-recette` et ne remplace pas un contrôle humain. |
| Publication | Une seule commande synchronise, commit et pousse vers le dépôt des TP. | Toute modification directe d'un clone local serait écrasée ou ferait échouer une publication ultérieure. |

## Règles de maintenance qui découlent de l'architecture

1. Modifier une slide dans `scripts/slides/`, jamais directement dans le PPTX ; régénérer ensuite avec `make deck`.
2. Modifier les pages des TP dans `docs/`, jamais dans les clones du site ; vérifier puis publier avec les cibles prévues.
3. Utiliser `config.yml` pour les paramètres lus par la fabrication ; une nouvelle session demande aussi les mises à jour manuelles documentées dans `AGENTS.md`.
4. Réutiliser les composants de `scripts/igpde_dsfr_components.py` plutôt que d'ajouter des formes PowerPoint directes.
5. Ne considérer un livrable comme vérifié qu'après les commandes adaptées à sa nature : tests, validation, QA, recette visuelle et relecture humaine si nécessaire.
6. Conserver le sens unique usine vers site publié ; la copie publique ne sert jamais à reconstruire une source de l'usine.

## Sources de vérité de cette vue

- `AGENTS.md` et `CLAUDE.md` : protocole de travail et invariants ;
- `config.yml` et `Makefile` : paramètres et points d'entrée effectifs ;
- `scripts/assemble.py`, `scripts/slides/__init__.py` et `scripts/igpde_dsfr_components.py` : assemblage du deck ;
- `scripts/fabriquer_pack.py`, `scripts/pack_supports.py` et `vendor/README.md` : pack, PDF et supports ;
- `validate.py`, `tests/`, `recette/` et `.qa/` : contrôles ;
- `PUBLIER-SITE.md`, `docs/README.md` et `publication-site/` : flux de publication du site.
