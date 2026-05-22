# Réexporter le deck PPTX

Mode d'emploi court pour régénérer le support `formation-102638-juin-2026.pptx` et vérifier qu'il ne contient pas de nouvelle régression géométrique ou textuelle.

## Principe

Le deck est généré par les scripts Python du projet. Il ne faut pas modifier le fichier `.pptx` directement dans PowerPoint si l'objectif est de produire une version reproductible.

La boucle QA PRD-119 travaille sur une copie dans `.qa/formation-test-qa.pptx`. Elle sert à vérifier le deck avant de régénérer ou livrer le fichier stable.

## Commande recommandée

Depuis la racine du projet :

```bash
cd /Users/alex/Claude/projets-formations/IGPDE-Carinne-C
python3 scripts/qa_pptx.py . --max-iterations 5 --clean
```

Si la sortie indique :

```text
[QA-PPTX] status=CONVERGED
[QA-PPTX] new=0
```

alors la copie de travail `.qa/formation-test-qa.pptx` ne contient aucune nouvelle violation connue par les tests PRD-119.

## Réexporter le deck stable

Quand la QA est conforme, régénérer le fichier final :

```bash
python3 scripts/assemble.py
python3 -m pytest tests/ -q
unzip -t formation-102638-juin-2026.pptx
```

Le fichier à livrer reste :

```text
formation-102638-juin-2026.pptx
```

## Corriger les accents sûrs

Si la QA signale des violations `accent_fr` nouvelles et que le rapport propose des patchs sûrs, appliquer uniquement ces corrections :

```bash
python3 scripts/qa_pptx.py . --max-iterations 5 --apply-accents
git diff
python3 scripts/assemble.py
python3 -m pytest tests/ -q
```

Vérifier le diff avant de committer. Le correcteur ne doit modifier que des chaînes Python avec accents manquants.

## Lire les rapports

Les rapports utiles sont écrits dans `.qa/` :

- `.qa/qa-pptx-report.md` : statut de la boucle, itérations, commandes exécutées.
- `.qa/qa-report.json` : violations détaillées avec fingerprints.
- `.qa/qa-corrections.md` : actions proposées ou skips du correcteur.
- `.qa/source-map.json` : lien entre shapes PPTX et appels Python quand disponible.

Lire le champ `status` du rapport. L'exit code seul ne suffit pas comme verdict métier en v1.

## Interpréter les statuts

| Statut | Sens | Action |
|--------|------|--------|
| `CONVERGED` | Aucune violation nouvelle | Réexport stable possible |
| `DRY_RUN_PENDING` | Violations nouvelles détectées, aucun patch appliqué | Lire `.qa/qa-corrections.md` |
| `SKIPPED_UNSAFE` | Violation nouvelle sans correction automatique sûre | Corriger manuellement dans les scripts |
| `OSCILLATION` | Fingerprints déjà vus après correction | Ne pas insister, analyser le diff |
| `NO_PROGRESS` | Plusieurs itérations sans amélioration | Corriger manuellement |
| `ASSEMBLE_FAILED` | La génération PPTX a échoué | Lire la sortie `assemble` |
| `TEST_FAILED_NO_REPORT` | Les tests n'ont pas produit de rapport QA | Relancer les tests géométriques directement |

## Ce que la v1 ne fait pas

- Elle ne corrige pas automatiquement le layout.
- Elle ne rédige pas les alt-text.
- Elle ne valide pas le rendu visuel comme un humain.
- Elle ne committe rien automatiquement.

Les débordements footer, chevauchements, tailles de police et alt-text restent des signaux à traiter dans les scripts source.

## Diagnostic rapide

Relancer uniquement les tests géométriques sur la copie `.qa` :

```bash
QA_PPTX_PATH=.qa/formation-test-qa.pptx python3 -m pytest tests/test_deck_geometry.py -q
```

Vérifier le PPTX stable :

```bash
unzip -t formation-102638-juin-2026.pptx
```

Vérifier les tirets interdits dans les scripts :

```bash
grep -rn $'—\|–' scripts/ || true
```
