# Réexporter le deck PPTX

Mode opératoire du projet pour régénérer le support `support-formation-102846-2026-IGPDE.pptx` et vérifier qu'il ne contient pas de nouvelle régression géométrique ou textuelle. Ce document est un runbook : une procédure exécutable et vérifiable, pas un modèle à recopier ni une simple recommandation.


Dans les commandes ci-dessous, `python` désigne l'interpréteur de l'usine : `.venv/bin/python` après `make installer`, sinon `/opt/homebrew/bin/python3.12`.

Avant une première utilisation ou après recréation de l'environnement :

```bash
make installer
```

## Principe

Le deck est généré par les scripts Python du projet. Ne jamais modifier le fichier `.pptx` dans PowerPoint : toute retouche serait écrasée à la régénération suivante. Les corrections se font dans `scripts/slides/` (voir `AGENTS.md`).

La boucle QA du deck travaille sur une copie dans `.qa/formation-test-qa.pptx`. Elle sert à vérifier le deck avant de régénérer ou livrer le fichier stable.

## Relever les corrections pendant la relecture

Ouvrir le fichier livré :

```text
livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx
```

Pour chaque observation, noter :

```text
Position dans PowerPoint :
Titre ou texte visible :
Type : texte | mise en page | image | accessibilité | notes
Problème observé :
Résultat attendu :
Capture d'écran : facultative, recommandée pour un défaut visuel
```

La position dans PowerPoint ne correspond pas nécessairement au préfixe du fichier Python. Le titre ou le texte visible permet de retrouver la bonne source. Ne pas enregistrer de correction, de commentaire ou d'annotation dans le PPTX livré : fermer sans enregistrer s'il a été modifié par erreur.

## Traiter un lot de corrections

1. Vérifier que l'arbre Git ne contient pas de changement étranger au lot.
2. Retrouver la source avec `scripts/slides/README.md` ou une recherche du texte visible :

   ```bash
   rg -n "texte visible" scripts/slides
   ```

3. Corriger le fichier `scripts/slides/NN_*.py` correspondant. Pour un défaut isolé, ne pas modifier un composant partagé. Modifier `scripts/igpde_dsfr_components.py` seulement si le problème est réellement commun à plusieurs slides.
4. Relire le diff source. Les textes, notes, images, textes alternatifs et ordres de lecture se corrigent dans les scripts, jamais dans PowerPoint.
5. Si utile, générer une slide seule pour un diagnostic rapide :

   ```bash
   .venv/bin/python scripts/assemble.py --only NN
   ```

   Cette commande produit un deck partiel à la racine. Elle ne met jamais à jour le PPTX du pack et ne remplace pas la génération complète.
6. Quand le lot est prêt, lancer la boucle QA depuis la racine du projet :

   ```bash
   make qa
   ```

Si la sortie indique :

```text
[QA-PPTX] status=CONVERGED
[QA-PPTX] new=0
```

alors la copie de travail `.qa/formation-test-qa.pptx` ne contient aucune nouvelle violation connue par les tests de la boucle QA.

Si le statut n'est pas `CONVERGED`, lire `.qa/qa-corrections.md`, corriger les scripts, puis relancer `make qa`. Ne pas régénérer le livrable stable tant que les violations nouvelles ne sont pas comprises.

## Réexporter le deck stable

Quand la QA est conforme, régénérer le fichier final :

```bash
make deck
make verifier
unzip -t livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx
```

`make deck` met aussi à jour la copie du deck dans le pack livrable, qui est la version versionnée et remise à l'IGPDE. Cette copie refuse un deck partiel (produit par `--only`, `--from` ou `--to`) : le livrable reste alors inchangé. Pour régénérer en plus les PDF et les supports : `make pack`.

Avant livraison, ouvrir ce PPTX du pack dans PowerPoint et effectuer une relecture visuelle humaine. La QA automatique ne détecte pas tous les chevauchements fins ni tous les défauts esthétiques.

Contrôler en priorité chaque slide corrigée, la slide qui la précède, celle qui la suit, puis les slides qui utilisent le même composant partagé. Une nouvelle observation ouvre un nouveau tour de la même boucle ; le PPTX n'est la source d'aucune correction.

Le fichier à livrer est la copie du pack :

```text
livrables-IGPDE-2026-102846/Formateur/support-formation-102846-2026-IGPDE.pptx
```

## Critère de fin d'un lot

Le lot est terminé uniquement lorsque :

- les corrections demandées sont présentes dans les scripts source ;
- le diff ne contient aucune modification étrangère ;
- `.qa/qa-pptx-report.md` indique `status=CONVERGED` et `new=0` ;
- `make deck` a régénéré le deck complet et sa copie dans le pack ;
- `make verifier` réussit ;
- `unzip -t` confirme l'intégrité du PPTX du pack ;
- la relecture humaine du fichier du pack confirme les corrections sans nouvelle régression visible.

Le commit et le push viennent après cette validation. Aucun outil de la chaîne ne les effectue automatiquement.

## Place de ShipGuard

ShipGuard est utile comme garde-fou, pas comme générateur du deck :

- le verrou de mission borne un lot aux slides signalées, aux sources correspondantes et aux contrôles attendus ;
- une vérification ShipGuard complète peut être pertinente si le générateur, les composants partagés ou la chaîne de fabrication changent ;
- la revue visuelle ShipGuard actuelle vise des captures de pages web et ne remplace pas la relecture du PPTX dans PowerPoint ; la recette ShipGuard du projet reste dédiée au site.

Décision au 2026-09-30 : conserver ce mode opératoire comme runbook du projet, sans créer de skill interne. Un skill ne serait reconsidéré que si plusieurs agents échouent malgré ce guide ou si une chaîne automatisée de rendu et de comparaison des slides est ajoutée.

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
