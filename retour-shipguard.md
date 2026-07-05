# Retour ShipGuard - améliorations proposées

## Objectif

Rendre ShipGuard directement exploitable comme outil de recette autonome, indépendamment du modèle, de l'agent ou du harnais qui l'appelle.

## Implémenter une CLI native unique

À implémenter :

```bash
shipguard run --profile site-accessible --serve
shipguard review --serve
shipguard stop
```

Pourquoi :

Une recette ne doit pas dépendre d'une suite de gestes implicites : lire une compétence, copier des assets, démarrer un serveur, lancer des tests, puis construire un tableau. Une commande unique réduit les erreurs, rend le résultat reproductible et permet à n'importe quel agent ou humain de relancer la même preuve.

## Ajouter un fichier de configuration projet

À implémenter :

```yaml
version: 1

app:
  type: static-site
  root: docs
  start: "python3 -m http.server {port} --bind 127.0.0.1"
  healthcheck: "/site-accessible/index.html"

profiles:
  site-accessible:
    scope: "site-accessible"
    checks:
      - page-load
      - local-assets
      - browser-errors
      - screenshots
```

Pourquoi :

Le périmètre de recette doit être une donnée déclarée, pas une décision cachée dans un script ou une conversation. Un fichier `.shipguard.yml` rend explicites le serveur, le healthcheck, le scope, les checks attendus et les profils réutilisables.

## Standardiser le scope

À implémenter :

```bash
shipguard run --scope site-accessible
shipguard run --scope site-inaccessible
shipguard run --scope all
```

Pourquoi :

Les sites pédagogiques, documentaires ou applicatifs ont souvent plusieurs périmètres valides. Un scope officiel évite de tester trop large, trop étroit ou le mauvais dossier. Il rend aussi le rapport compréhensible sans connaître l'historique du projet.

## Gérer le cycle de vie serveur

À implémenter :

- allocation automatique d'un port libre ;
- démarrage du serveur déclaré ;
- attente d'un healthcheck HTTP ;
- arrêt propre du serveur après recette ;
- conservation optionnelle du serveur de revue.

Pourquoi :

La recette doit posséder son environnement d'exécution. Si le serveur est lancé à côté, le résultat dépend du terminal, du harnais ou de l'état local. ShipGuard doit distinguer une erreur produit d'une erreur d'infrastructure.

## Générer tous les artefacts attendus en une passe

À implémenter :

- `visual-results.json` pour les tests visuels ;
- `audit-results.json` pour les constats ;
- `process-results.json` quand une simulation comportementale existe ;
- `report.md` pour la lecture humaine ;
- `review.html` pour la revue visuelle.

Pourquoi :

Le tableau de revue ne doit pas afficher des onglets vides quand une recette a bien été exécutée. Si une piste n'est pas applicable, elle doit être déclarée comme non applicable. Si des constats dynamiques existent, ils doivent pouvoir alimenter une vue commune des problèmes.

## Unifier les constats autour de l'évidence

À implémenter :

```json
{
  "id": "SG-001",
  "title": "Ressource média absente",
  "severity": "high",
  "evidence": "measured",
  "source": "browser",
  "route": "/site-accessible/ec09-captions.html"
}
```

Pourquoi :

Le libellé "Code Audit" peut créer une confusion quand le constat vient d'une recette navigateur. Le critère principal devrait être la nature de la preuve : `measured`, `reasoned` ou `manual`. Cela rend le rapport lisible par tous les agents et par les humains.

## Fournir un mode statique HTML natif

À implémenter :

- découverte automatique des fichiers HTML ;
- vérification des liens et assets locaux ;
- détection des médias manquants ;
- capture complète de chaque page ;
- génération de manifestes si absents.

Pourquoi :

Tous les projets ne sont pas des applications React ou Next.js. Les sites statiques sont un cas courant de livraison. ShipGuard doit les traiter sans wrapper projet spécifique.

## Stabiliser les sorties navigateur

À implémenter :

- mode `eval --json` garanti ;
- parsing robuste des résultats navigateur ;
- erreurs navigateur normalisées ;
- captures validées comme fichiers non vides.

Pourquoi :

Une recette ne doit pas casser parce qu'un outil renvoie une chaîne JSON échappée au lieu d'un objet. ShipGuard doit offrir une couche de compatibilité stable au-dessus de l'automatisation navigateur.

## Initialiser l'hygiène des artefacts

À implémenter :

```gitignore
.DS_Store
_results/
_regressions.yaml
```

Pourquoi :

Les artefacts de recette sont utiles mais souvent locaux, volumineux ou temporaires. `shipguard init` devrait créer les bons garde-fous pour éviter de committer des fichiers de session par accident.

## Adapter le tableau de revue

À implémenter :

- ouvrir par défaut sur la piste contenant des résultats ;
- afficher "non applicable" plutôt qu'un onglet vide ;
- regrouper les constats sous une vue "Findings" indépendante de leur origine ;
- garder les onglets spécialisés pour le détail.

Pourquoi :

Un tableau qui s'ouvre sur un onglet vide donne l'impression que la recette n'a pas tourné. La revue doit d'abord présenter l'état réel du run, puis permettre de filtrer par origine : visuel, audit, process ou manuel.

## Définir des codes de sortie stables

À implémenter :

- `0` : aucune anomalie ;
- `1` : recette exécutée avec constats ;
- `2` : erreur d'infrastructure ;
- `3` : configuration invalide.

Pourquoi :

Les humains, CI et agents doivent pouvoir interpréter le résultat sans parser le Markdown. Un échec produit ne doit pas être confondu avec un serveur indisponible ou une configuration cassée.

## Résultat attendu

ShipGuard devient un moteur de recette portable :

- même commande pour humain, CI ou agent ;
- même contrat de sortie quel que soit le modèle ;
- preuves séparées des raisonnements ;
- périmètre explicite ;
- tableau de revue immédiatement exploitable.
