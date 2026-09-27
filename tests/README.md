# Tests automatisés

Ce dossier contient les tests de régression de l'usine. Ils vérifient les composants de slides, les contrôles de qualité du deck, la fabrication du pack et la conformité des PDF livrés.

## Exécution

Depuis la racine de l'usine :

```bash
make tests
```

Cette commande lance `pytest` sur l'ensemble du dossier. `make verifier` l'exécute aussi, puis valide le site et applique les contrôles du dépôt.

Les contrôles qui lisent le deck assemblé utilisent le PPTX de travail à la racine. S'il manque, régénérez-le avec `make deck` avant de lancer la suite complète.

## Couverture

- `test_components.py` et `test_helpers.py` : composants DSFR et calculs de positionnement ;
- `test_finalize.py` : langue, alternatives et ordre de lecture du PPTX ;
- `test_deck_geometry.py` : pied de page, chevauchements, alternatives, taille minimale des polices et accents français ;
- `test_fabriquer_pack.py`, `test_pack_supports.py` et `test_pdf_ua.py` : intégrité du pack, copies et refus des PDF non conformes PDF/UA-1 ;
- `test_qa_*.py` : mécanismes de contrôle qualité et de correction prudente du deck.

## Écarts connus

`baselines/known-geometry-violations.json` documente les écarts géométriques explicitement tolérés. Un test échoue dès qu'un écart nouveau apparaît : la baseline ne doit jamais servir à masquer une régression.

## Limites

Ces tests prouvent des propriétés techniques. Ils ne remplacent ni `make recette` pour la recette visuelle du site, ni une relecture humaine du deck pour les défauts graphiques fins.
