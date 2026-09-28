# Réexporter le deck PPTX

Mode d'emploi court pour régénérer le support `support-formation-102846-2026-IGPDE.pptx` et vérifier qu'il ne contient pas de nouvelle régression géométrique ou textuelle.


Dans les commandes ci-dessous, `python` désigne l'interpréteur de l'usine : `.venv/bin/python` après `make installer`, sinon `/opt/homebrew/bin/python3.12`.

Avant une première utilisation ou après recréation de l'environnement :

```bash
make installer
```

## Principe

Le deck est généré par les scripts Python du projet. Ne jamais modifier le fichier `.pptx` dans PowerPoint : toute retouche serait écrasée à la régénération suivante. Les corrections se font dans `scripts/slides/` (voir `AGENTS.md`).

La boucle QA du deck travaille sur une copie dans `.qa/formation-test-qa.pptx`. Elle sert à vérifier le deck avant de régénérer ou livrer le fichier stable.

## Commande recommandée

Depuis la racine du projet :

```bash
make qa
```

Si la sortie indique :

```text
[QA-PPTX] status=CONVERGED
[QA-PPTX] new=0
```

alors la copie de travail `.qa/formation-test-qa.pptx` ne contient aucune nouvelle violation connue par les tests de la boucle QA.

## Réexporter le deck stable

Quand la QA est conforme, régénérer le fichier final :

```bash
make deck
make verifier
unzip -t livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx
```

`make deck` met aussi à jour la copie du deck dans le pack livrable, qui est la version versionnée et remise à l'IGPDE. Cette copie refuse un deck partiel (produit par `--only`, `--from` ou `--to`) : le livrable reste alors inchangé. Pour régénérer en plus les PDF et les supports : `make pack`.

Avant livraison, ouvrir ce PPTX du pack dans PowerPoint et effectuer une relecture visuelle humaine. La QA automatique ne détecte pas tous les chevauchements fins ni tous les défauts esthétiques.

Le fichier à livrer est la copie du pack :

```text
livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx
```

## Corriger les accents sûrs

Si la QA signale des violations `accent_fr` nouvelles et que le rapport propose des patchs sûrs, appliquer uniquement ces corrections :

```bash
python scripts/qa_pptx.py . --max-iterations 5 --apply-accents
git diff
make deck
make verifier
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
QA_PPTX_PATH=.qa/formation-test-qa.pptx python -m pytest tests/test_deck_geometry.py -q
```

Vérifier le PPTX stable :

```bash
unzip -t livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx
```

Vérifier les tirets interdits dans les scripts :

```bash
grep -rn $'—\|–' scripts/ || true
```
