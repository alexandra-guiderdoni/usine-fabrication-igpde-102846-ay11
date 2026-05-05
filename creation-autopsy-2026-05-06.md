# Autopsie de création — IGPDE-Carinne-C

## Contexte

- **Projet** : `/Users/alex/Claude/projets-formations/IGPDE-Carinne-C`
- **Sessions analysées** : 182 fichiers Claude Code du workspace parent, du 4 avril 2026 au 4 mai 2026
- **Volume total** : 241 Mo de transcripts dans `/Users/alex/.claude/projects/-Users-alex-Claude`
- **Sessions principales retenues** : `94f3c1ee`, `ccdd1fae`, `09764225`
- **Limite méthodologique** : le projet n'a pas de dossier Claude dédié `-Users-alex-Claude-projets-formations-IGPDE-Carinne-C`. Les échanges ont été retrouvés dans le workspace parent. Les travaux Codex postérieurs au 4 mai ne sont pas couverts par cette autopsie Claude.

## Genèse

Le projet naît comme un support de formation IGPDE déjà orienté DSFR, mais sans encore de mécanique stable pour travailler slide par slide. Le premier prompt structurant est très opérationnel : « J'ai mon template `/Users/alex/Claude/projets-formations/IGPDE-Carinne-C/demo-template-dsfr.pptx` au fur et à mesure je te donnerai des slides. Comment faire pour ne pas tout régénérer à chaque fois mais juste les slides dont j'ai besoin ? »

La réponse fondatrice est le passage à un deck piloté par code : un module Python par slide, un `assemble.py`, des modes `--only`, `--from` et `--to`, puis une bibliothèque de composants IGPDE-DSFR. Le besoin initial n'était pas seulement de produire des slides : il fallait rendre le deck modifiable sans perdre la pagination, la cohérence graphique et les corrections manuelles.

Le second mouvement est pédagogique. Le guide de navigation clavier devient une première séquence, puis il est replacé dans l'Easy Check n° 6 du W3C. De là, le périmètre s'élargit : traiter les 13 points de contrôle rapides du W3C, créer une grille d'audit, puis fabriquer un site d'entraînement. Le deck cesse d'être un simple support et devient une séquence complète : présentation, exercice, grille, site, documents Word accessibles/inaccessibles.

## Chronologie

### Session `94f3c1ee` — 17 avril 2026

Cette session pose l'architecture. La question de départ concerne la régénération partielle du deck, et la décision devient : `scripts/slides/NN_nom.py` pour les modules, `scripts/assemble.py` pour l'assemblage, et `SlideContext` pour préserver date, numéro de page et pied de page.

Le travail bascule ensuite vers la navigation clavier. Alex demande d'utiliser le skill pédagogie sur `guide-test-accessibilite-clavier.md`, puis recadre : « la séquence de la navigation clavier aura sa place dans les easy check ». La nuance méthodologique apparaît tout de suite : l'Easy Check 6 du W3C cible le focus visible, mais la formation l'élargit volontairement à la navigation clavier, l'activation clavier et les signaux d'alerte.

La même session voit apparaître la grille d'audit Easy Checks. Elle est évaluée, enrichie avec un échantillon RGAA, configurée pour l'impression, puis validée. Le deck passe alors d'une poignée de slides à un support organisé autour des 13 points de contrôle rapides.

Une grande partie de la fin de session est consacrée au rendu. Les problèmes ne sont pas cosmétiques : fil d'Ariane parasité par une numérotation automatique, trop de blanc entre titre et contenu, cartes qui débordent ou laissent trop d'espace, alertes de couleurs hétérogènes. Les corrections produisent des invariants durables : neutraliser la numérotation du placeholder, resserrer le titre, unifier les accents à 0,08", calculer automatiquement les hauteurs et utiliser un `Stack` pour empiler les composants.

### Session `ccdd1fae` — 2 mai 2026

La session démarre par une reprise de contexte : « Je veux retravailler et continuer mes slides ». À ce moment, le projet compte 86 slides réparties en quatre modules, avec deux tâches restantes : le site d'entraînement clavier et la distribution de la grille.

Le pivot majeur concerne la relation entre PowerPoint et le code. Alex veut figer certaines slides et ajouter des images à la main. La solution retenue n'est pas de renoncer au code, mais de capturer les corrections PowerPoint dans les scripts : lire les positions, extraire les images, créer `add_image`, puis intégrer les placements dans les modules Python.

Cette logique sert tout de suite sur les slides d'intervenants : photos alignées, texte modifié, espaces de listes ajustés. Puis elle s'étend globalement : contenus en 14 pt minimum, interligne recalibré, débordements repris. Le choix initial d'un interligne 2,0 se révèle trop lourd ; il est ramené à 1,5, avec exceptions à 1,0 sur les slides serrées.

La fin de session fait naître l'exercice Word. D'abord nommé Karine, il part d'un document trimestriel avec quelques erreurs d'accessibilité : faux titres, tableau sans en-tête, couleur seule, image sans alternative, lien non descriptif. Alex demande une validation critique par `avocat-du-diable` et `connu-inconnu`, puis le Devil Council attaque l'idée d'une checklist trop procédurale. L'exercice est amendé : plus de compréhension, moins de talisman, un déroulé en phases, et une erreur ambiguë de contraste.

### Session `09764225` — 3 mai 2026

Cette session transforme l'exercice en livrables. Le premier objectif est clair : « On était sur l'exercice de Karine. il faudrait faire le word non accessible, et le word accessible et corriger slide 32 ». Le script `generate_exercice_karine.py`, puis `generate_exercice_sami.py`, produit les DOCX et les images pédagogiques.

Le prénom change aussi : Karine devient Sami. Le titre de slide devient « Exercice : les erreurs de Sami ». Les fichiers sont renommés, la spec est mise à jour, le contenu est harmonisé, et le document inaccessible doit rester visuellement crédible. Alex demande par exemple que les faux titres utilisent les mêmes couleurs que les vrais titres : l'erreur doit être structurelle, pas grossièrement visible.

L'exercice s'enrichit par couches successives. D'abord 8 erreurs, puis 10 avec les cas d'images, puis 12 avec langue et propriétés, 14 avec fausses listes, 18 avec lisibilité, enfin 21 avec sommaire, texte sous forme d'image et tableau simplifié. Le principe pédagogique est de faire correspondre ce qui est enseigné dans les slides avec ce que les stagiaires pratiquent dans le document.

Un pivot important supprime le doublon avec l'étude de cas Sophie. La slide Sophie est remplacée par un retour sur le document de Sami, qui révèle les erreurs cachées. C'est un basculement vers une séquence plus intégrée : un même support d'exercice sert à découvrir, corriger, revenir, et ancrer.

La session se termine par une hygiène du harnais. Le `CLAUDE.md` projet a grossi à 316 lignes ; Alex demande s'il aurait fallu utiliser un skill, puis valide `/distiller-claude-md`. Le fichier est réduit à 74 lignes, avec un protocole agent centré sur les comportements utiles. Cela devient un invariant du projet : la mémoire doit aider l'agent à agir, pas raconter l'histoire du projet.

## Pivots et décisions clés

1. **Code plutôt que manipulation PowerPoint directe** — le deck est généré par scripts, avec tests ciblés et assemblage complet.
2. **Correction visuelle capturée dans le code** — les images placées dans PowerPoint servent de référence de position, puis sont réintégrées dans les scripts.
3. **Easy Check 6 élargi** — le focus visible devient une séquence plus large sur navigation clavier, activation et signaux d'alerte.
4. **13 points W3C comme ossature pédagogique** — chaque point devient une unité de formation, avec grille d'audit et site d'exercice.
5. **Karine devient Sami** — l'exercice se stabilise comme support central, plus neutre et plus extensible.
6. **Sophie supprimée** — le cas séparé est remplacé par un retour sur Sami, pour éviter la redondance pédagogique.
7. **De "pilier" à "thème"** — le vocabulaire est simplifié et harmonisé dans les slides et commentaires.
8. **CLAUDE.md distillé** — la mémoire projet passe d'un historique dense à un protocole court.

## Choix abandonnés

- **Régénérer tout sans stratégie de protection** : remplacé par un pipeline modulaire avec test de slides isolées.
- **Interligne 2,0 global** : jugé trop destructeur pour la mise en page ; remplacé par 1,5 par défaut.
- **Matrice impact fort/faible** : abandonnée car elle hiérarchisait implicitement des obligations d'accessibilité.
- **Étude de cas Sophie** : supprimée car redondante avec Sami.
- **Colonnes simulées par tabulations et zones flottantes** : explicitement laissées hors du DOCX Sami.
- **CLAUDE.md narratif** : remplacé par une version distillée.

## État final

Le projet contient aujourd'hui un support de formation complet autour de l'accessibilité numérique pour communicants :

- `formation-102638-juin-2026.pptx` — deck final observé à 106 slides dans le protocole projet actuel.
- `scripts/slides/` — modules Python de génération des slides.
- `scripts/assemble.py` — assemblage du deck, avec test ciblé par slide.
- `scripts/generate_exercice_sami.py` — génération des DOCX et images de l'exercice Sami.
- `_source/sami-doc-inaccessible.docx`, `_source/sami-doc-aide-correction.docx`, `_source/sami-doc-accessible.docx` — trio de documents d'exercice.
- `_source/exercice-sami-spec.md` et `_source/exercice-sami-diff.md` — contrat pédagogique et liste des différences.
- `03-easy-checks/grille-audit-easy-checks.xlsx` — grille d'audit issue des 13 Easy Checks.
- `docs/` — site d'exercice points de contrôle rapides, enrichi après les sessions Claude analysées.
- `CLAUDE.md` — protocole projet distillé.

## Annexe — Conversations restituées

Les conversations principales sont restituées dans une page HTML filtrée du bruit technique, au format iMessage.

- [`94f3c1ee` — 17 avril 2026 — Genèse du pipeline slides et des Easy Checks](./creation-autopsy-2026-05-06-conversations.html#s94f3c1ee)
- [`ccdd1fae` — 2 mai 2026 — Reprise du deck, images, typographie et naissance de Karine](./creation-autopsy-2026-05-06-conversations.html#sccdd1fae)
- [`09764225` — 3 mai 2026 — Exercice Sami, DOCX, enrichissements et distillation](./creation-autopsy-2026-05-06-conversations.html#s09764225)
