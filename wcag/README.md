# Supports WCAG

Ce dossier réunit les sources et la sortie de travail des supports consacrés aux principes WCAG. Il ne contient pas les cartes WCAG à imprimer : celles-ci sont des ressources fixes du pack.

## Fiches PDF

- `fiche-formateur-principes-wcag.md` : source de la fiche destinée au formateur ;
- `fiche-stagiaire-principes-wcag.md` : source de la fiche destinée aux stagiaires.

Après toute modification d'une fiche, lancez depuis la racine de l'usine :

```bash
make pdf
```

La commande génère des PDF/UA-1 et les écrit dans `livrables-IGPDE-2026-102846/Livrables-Stagiaires/fil-rouge-principes-wcag-igpde/`. Ne modifiez pas directement ces PDF : la génération suivante les remplacerait.

Les tableaux des sources Markdown doivent rester entiers sur une page. Un tableau coupé peut empêcher WeasyPrint de produire un PDF/UA-1 ; dans ce cas, `make pdf` échoue et préserve le livrable précédent.

## Deck condensé

`WCAG en langage clair - condensé.pptx` est un deck de 13 slides généré par `scripts/generate_wcag_langage_clair.py`.

Pour le régénérer :

```bash
make wcag
```

Ne modifiez pas le PPTX directement : corrigez le script générateur, puis régénérez le deck.

## Vérification

Après une régénération de PDF, lancez `make verifier`. Il contrôle notamment que les PDF livrés déclarent le standard PDF/UA-1.
