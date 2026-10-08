Validation ShipGuard de la grille et du site : notes cuisine-moi
================================================================

Date : 2026-10-08 | Objectif : décider ensemble, point par point, des corrections relevées par ShipGuard avant toute mise en œuvre.

## Résumé / décisions clés

- Q1 validée : aligner tous les supports sur le nouveau modèle à trois champs. Retirer verdict, sévérité, taux et Top 3. Ajouter l'idée que l'objectif est de documenter un écart et de proposer sa correction, pas de calculer un taux de conformité.
- Q2 validée : corriger le HTML d'EC09, EC10 et EC11, retirer les explications pédagogiques de la version accessible et les conserver dans la version d'aide.
- Q3 validée : corriger les titres des index `site-inaccessible` et `site-aide-correction` en `h2`. Les index et la navigation restent accessibles ; seules les erreurs pédagogiques prévues sont conservées dans les pages d'exercice.
- Q4 validée : conserver l'indication du poids du classeur et remplacer la valeur obsolète par `XLSX - 34 Ko`.
- Q5 validée : utiliser `FORMATION["site_url"]` dans le générateur et vérifier par test que les trois copies XLSX sont identiques. L'URL publique reste exactement `https://alexandra-guiderdoni.github.io/tp-fabrication-igpde-102846-ay11`.
- Q6 validée : corriger toutes les sources localement, régénérer, vérifier, faire repasser ShipGuard et présenter le verdict avant tout commit, push ou publication.

## Journal questions-réponses

### Q1 - Alignement du parcours pédagogique
- Question : faut-il aligner les slides, le contrat d'évaluation et le Markdown sur les trois champs de la nouvelle grille, réintroduire les anciens champs, ou conserver un modèle hybride ?
- Capture : option A validée. Le parcours repose sur `Constat`, `Mise en conformité à réaliser` et `Preuve de l'écart`. Les notions de verdict, sévérité, taux et Top 3 sont retirées des consignes et des sources associées.
- Drapeaux : aucun.

### Q2 - HTML et sobriété des pages accessibles
- Question : faut-il conserver les encarts pédagogiques dans la version accessible, les supprimer, ou les réserver à la version d'aide tout en corrigeant les erreurs HTML ?
- Capture : option C validée. Les erreurs de structure HTML sont corrigées. La version accessible montre uniquement le résultat corrigé ; les explications restent dans la version `site-aide-correction`.
- Drapeaux : vérifier lors de la mise en œuvre que les explications utiles retirées d'EC09, EC10 et EC11 existent bien dans les pages d'aide correspondantes.

### Q3 - Hiérarchie des titres dans les index
- Question : les erreurs doivent-elles aussi rester dans les index des versions inaccessible et aide ?
- Capture : option A validée avec la distinction suivante : les pages d'exercice conservent uniquement leurs défauts intentionnels ; les index, la navigation et l'infrastructure commune restent accessibles. Les `h3` placés directement après le `h1` deviennent donc des `h2` dans les deux index.
- Drapeaux : aucun.

### Q4 - Poids affiché du classeur
- Question : faut-il actualiser le poids, le supprimer ou le calculer automatiquement ?
- Capture : conserver le poids avec la bonne valeur. La page d'accueil affichera `XLSX - 34 Ko`.
- Drapeaux : la valeur devra être revue si une régénération ultérieure modifie sensiblement la taille du fichier.

### Q5 - URL canonique et identité des copies XLSX
- Question : faut-il centraliser l'URL dans `config.yml` et protéger l'identité des trois copies par un test ?
- Capture : option A validée. Le générateur lit `FORMATION["site_url"]` et les tests vérifient les trois fichiers. La valeur de l'URL publique ne change pas.
- Drapeaux : aucun.

### Q6 - Ordre de correction et de publication
- Question : faut-il publier immédiatement la grille, rester uniquement en local, ou corriger et valider tout l'ensemble avant publication ?
- Capture : option A validée. Ordre retenu : corrections locales, régénération de la grille et du deck, tests et recette, nouvelle validation ShipGuard, présentation du verdict, puis commit, push et publication seulement après accord.
- Drapeaux : commit, push et publication restent soumis à une autorisation ultérieure après le verdict ShipGuard.

## Drapeaux ouverts

- Vérifier que les explications retirées des pages accessibles EC09, EC10 et EC11 sont bien présentes dans les pages d'aide.
- Vérifier le poids final du XLSX après régénération avant d'afficher `34 Ko`.
- Le contrôle natif dans Excel et la recette automatisée de reflow/zoom restent à exécuter si les outils sont disponibles.

## Prochaine étape

- Attendre la confirmation de la compréhension partagée.
- Puis mettre en œuvre uniquement les corrections locales validées, sans commit, push ni publication.
