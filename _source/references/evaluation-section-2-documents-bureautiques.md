---
title: "Evaluation de la section 2 - Documents bureautiques accessibles"
subtitle: "Formation 102638 - IGPDE / Carinne C."
author: "Alex Guiderdoni"
date: "2026-05-04"
lang: "fr"
keywords: "accessibilité numérique, Word, PDF accessible, formation, IGPDE"
---

# Evaluation de la section 2 - Documents bureautiques accessibles

## Verdict global

La section **2. Documents bureautiques accessibles**, slides **20 à 49**, est maintenant très solide, exploitable en formation et cohérente avec le public cible : des communicants, non développeurs, qui doivent repartir avec des gestes Word et DOCX immédiatement applicables.

**Note réévaluée : 19 / 20.**

Cette note tient compte du fait que la densité de certaines slides, notamment les checklists et la correction finale, est volontaire. Ce n'est donc pas un défaut : c'est un choix pédagogique assumé pour fournir un support de référence après la formation. La réévaluation intègre aussi la passe technique globale : la section et l'assemblage complet ne produisent plus de warning footer.

## Ce qui fonctionne très bien

### Progression pédagogique

La progression est claire et mieux verrouillée qu'à la première évaluation :

1. Ouverture empathique avec le lecteur d'écran.
2. Quiz de perception entre document visuellement correct et document réellement accessible.
3. Vue d'ensemble des 5 thèmes.
4. Apprentissage par critères actionnables dans Word.
5. Exercice Sami pour mobiliser les acquis.
6. Finalisation, vérificateur Word et export PDF accessible.
7. Retour différé, quiz final, rappel actif et engagement.

La section n'est pas seulement informative : elle force les stagiaires à juger, comparer, vérifier, puis s'engager.

### Couverture des gestes critiques Word

Les points essentiels sont couverts :

- styles de titre ;
- listes natives ;
- tableaux et objets flottants ;
- contraste ;
- couleur non porteuse de sens seule ;
- texte alternatif ;
- liens descriptifs ;
- informations essentielles hors en-têtes, pieds de page et filigranes ;
- langue, majuscules et lisibilité ;
- espaces parasites et objets clignotants ;
- propriétés du document ;
- vérificateur d'accessibilité ;
- export Word vers PDF accessible.

L'ajout de la slide sur l'export PDF ferme un trou important : elle rappelle qu'un Word accessible peut perdre son accessibilité si l'export PDF est mal fait.

### Cohérence visuelle

La mise en page DSFR est homogène :

- titres cohérents ;
- fil d'Ariane présent ;
- composants récurrents mais variés ;
- alternance entre highlights, tableaux, cartes, stepper et callouts ;
- footer stable ;
- progression lisible.

Les corrections récentes améliorent notamment :

- la slide 25, dont les cartes sont mieux espacées ;
- la slide 33, qui ne chevauche plus les blocs ;
- la slide 39, dont le message est plus juste ;
- la slide 40, dont la liste numérotée n'a plus de puces doublons ;
- la slide 42, également nettoyée des puces doublons ;
- les warnings footer de la section 2, désormais éliminés ;
- les warnings footer du deck complet, également éliminés, ce qui réduit le risque de remontées automatiques non vues.

## Points assumés

### Densité des checklists

Les slides de checklist sont denses, mais c'est volontaire. Elles ont une double fonction :

- support d'animation pendant la formation ;
- aide-mémoire réutilisable après la journée.

Il ne faut donc pas les alléger automatiquement. Leur densité est acceptable parce qu'elles arrivent après l'exercice et après la consolidation.

### Correction finale détaillée

La correction finale est également dense, mais elle joue le rôle de synthèse structurante :

- erreur ;
- impact utilisateur ;
- correction concrète dans Word.

Elle sert de référence. Le niveau de détail est justifié.

## Risques restants

### Rythme oral

Le principal risque n'est plus la mise en page, mais le rythme d'animation. La section couvre beaucoup de gestes en peu de temps. Le formateur devra :

- annoncer que tout ne sera pas mémorisé immédiatement ;
- insister sur les 3 premiers réflexes ;
- utiliser les checklists comme support de référence, pas comme liste à réciter ;
- laisser du temps à l'exercice Sami.

### Vérification native PowerPoint

Le deck a été régénéré et contrôlé via rendu PDF. Une dernière vérification dans PowerPoint reste utile avant diffusion officielle, car PowerPoint et LibreOffice peuvent rendre certains espacements légèrement différemment.

## Note détaillée

<table>
  <caption>Notes détaillées de l'évaluation de la section Documents bureautiques accessibles</caption>
  <tr>
    <th scope="col">Dimension</th>
    <th scope="col">Note</th>
    <th scope="col">Commentaire</th>
  </tr>
  <tr>
    <th scope="row">Cohérence pédagogique</th>
    <td>19 / 20</td>
    <td>Progression claire, rappels actifs, exercice structurant et export PDF ajouté au bon endroit.</td>
  </tr>
  <tr>
    <th scope="row">Couverture des critères Word</th>
    <td>19 / 20</td>
    <td>Les gestes essentiels sont couverts, y compris l'export PDF.</td>
  </tr>
  <tr>
    <th scope="row">Mise en page</th>
    <td>19 / 20</td>
    <td>Cohérente, stable, sans warning footer sur la section.</td>
  </tr>
  <tr>
    <th scope="row">Actionnabilité</th>
    <td>19 / 20</td>
    <td>Les stagiaires savent quoi faire dans Word dès le lendemain.</td>
  </tr>
  <tr>
    <th scope="row">Robustesse technique</th>
    <td>19 / 20</td>
    <td>Zéro warning footer sur la section 2 et sur l'assemblage complet du deck.</td>
  </tr>
</table>

## Note globale

**19 / 20**

La section est prête pour une utilisation en formation. Le dernier point qui empêche de parler d'un 20 / 20 est la validation native PowerPoint sur le fichier final, car PowerPoint peut rendre certains espacements légèrement différemment de la chaîne de génération.

## Synthèse insight-forge

Dernière relance `insight-forge` :

- 7 sessions Codex traitées ;
- 2 observations stagées ;
- 4 cristallisations ;
- proposition générée : `.insight-forge/proposals/2026-05-04.md`.

### Enseignement principal pour cette section

Le point le plus utile extrait des cristallisations est le suivant : le mécanisme `_safe_top` protège contre le débordement bas, mais peut créer des chevauchements si le positionnement initial est trop optimiste.

Conséquence pratique pour les prochaines passes :

- ne pas se contenter de l'absence de débordement ;
- vérifier que les composants n'ont pas été remontés au point de toucher le bloc précédent ;
- traiter les warnings par slide, pas globalement ;
- garder les corrections ciblées sur le module évalué.
