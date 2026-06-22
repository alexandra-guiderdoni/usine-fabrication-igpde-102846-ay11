# Vision harnais pour une stack analytics agentique

## Contexte

Anthropic vient de publier l'architecture de son agent analytics interne.

OpenAI avait sorti la sienne en janvier.

Les leçons à en tirer pour ta stack :

- l'un laisse l'agent découvrir la donnée tout seul ;
- l'autre interdit à l'IA de définir ce que veut dire un chiffre.

## Analyse

Voici mon analyse.

Le débat n'est pas :

- LLM-as-judge contre évals.

Il est ailleurs.

> LLM-as-judge = LLM qui juge le travail d'un autre LLM.

## Point de départ commun

Les deux approches sont d'accord sur un point de départ :

> Brancher un LLM directement sur ton data warehouse sans contexte produit des résultats faux.

Les erreurs typiques :

- sous-estimation des nombres ;
- vocabulaire métier mal interprété.

> PS : Notre plateforme répond à ce problème.

À partir de là, deux routes opposées apparaissent.

## Route 1 - Anthropic

### Principe

L'humain garde la main sur la définition.

### Résultat annoncé

Les skills font passer Claude de 21 % à 95 % de précision.

### Fonctionnement

La documentation est générée par Claude, mais c'est un humain qui possède la définition de la métrique.

Les skills vivent dans le même repo que les modèles de données.

Conséquence :

- un changement de modèle force la mise à jour du contexte dans la même PR.

### Effet

On obtient un ancrage sémantique plus fort.

## Route 2 - OpenAI

### Principe

La découverte est automatique.

### Fonctionnement

Un pipeline quotidien profile les tables et stocke les corrections.

Codex inspecte :

- les tables ;
- le code des pipelines.

Il en infère :

- les dépendances ;
- la granularité ;
- les clés de jointure.

Une mémoire conserve les corrections d'une conversation à l'autre.

### Effet

On obtient un auto-apprentissage plus poussé.

## Ce qui sépare les deux approches

Ce qui les sépare n'est pas le modèle.

C'est qui gouverne la définition.

Deux logiques s'opposent :

- couche sémantique par l'humain d'un côté ;
- découverte automatique de l'autre.

## Application à ma stack

### 1. Mesure déterministe

Déterministe pour mesurer.

Tu ancres tes évals.

Tu juges la requête, pas seulement le chiffre.

### 2. LLM-as-judge cadré

LLM-as-judge pour challenger la réponse finale.

Pas pour noter tes évals.

### 3. Gouvernance humaine de la métrique

Humain pour définir la métrique.

C'est le seul endroit où l'auto-génération coûte plus cher qu'elle ne rapporte.

### 4. Contexte colocalisé avec la donnée

Contexte colocalisé avec la donnée.

Objectif :

- éviter qu'il pourrisse en deux semaines.

## Conclusion

Un LLM-as-judge ne remplace pas la gouvernance humaine de la définition.

Il la complète, à un endroit précis de la chaîne.

## Appel à action

Enregistre ce post si tu construis une stack analytics agentique.

Reposte si ça peut aider un DSI qui prépare le sujet.

## Liens

- OpenAI : <https://openai.com/fr-FR/index/inside-our-in-house-data-agent/>
- Anthropic : <https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude>
