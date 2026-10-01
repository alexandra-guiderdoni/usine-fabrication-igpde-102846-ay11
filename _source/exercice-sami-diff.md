# Exercice Sami — comparaison des variantes

La source normative des différences est
[`_source/exercice-sami-matrice.yml`](exercice-sami-matrice.yml). Elle seule
porte les identifiants, libellés, niveaux et ordre des contrôles. Ce fichier
décrit la logique de comparaison sans maintenir de liste parallèle.

## Version inaccessible

- contient chaque défaut dont l’occurrence est prévue par la matrice ;
- conserve les propriétés fautives nécessaires à la manipulation ;
- ne contient aucun commentaire d’aide.

## Version avec pistes

- reprend le même corps éditorial et les mêmes défauts ;
- ajoute un commentaire par occurrence attendue ;
- donne le problème, l’impact, la règle et la première action sans effectuer la
  correction à la place du binôme.

## Version corrigée

- conserve le même contenu, sauf transformations éditoriales explicitement
  autorisées par la matrice ;
- applique les structures et propriétés accessibles vérifiables dans le DOCX ;
- fournit les procédures Word et Writer ainsi que la preuve attendue ;
- rappelle que les vérificateurs automatiques complètent, sans remplacer, la
  vérification humaine.

## Vérification

`tests/test_exercice_sami_docx.py` compare les trois sorties générées et leur
OOXML. `tests/test_exercice_sami_matrice.py` vérifie la complétude de la source
canonique, l’ordre et les transformations autorisées. Les écarts observables
dans les applications bureautiques sont traités pendant la recette Windows.

L’ancienne comparaison détaillée reste disponible dans l’historique Git.
