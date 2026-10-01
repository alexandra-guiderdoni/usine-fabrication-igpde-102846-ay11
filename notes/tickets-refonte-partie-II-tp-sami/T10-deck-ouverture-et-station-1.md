# T10 — Reconstruire l’ouverture du deck et la station 1

**Statut :** `ready-for-agent`

**PRD :** [Refonte de la partie II et du TP Sami](../prd-refonte-partie-II-tp-sami.md)

**Bloqué par :** aucun. T09a a été annulé faute de binôme disponible et Alex a
explicitement autorisé le démarrage de T10.

**Débloque :** [T11](T11-deck-station-2.md).

## À construire

Recomposer l’entrée de la partie II et la station « Structurer et naviguer » à
partir de l’inventaire validé, de la matrice et des supports stabilisés.
Avant d’ajouter ou supprimer une slide, migrer les tests absolus affectés par la
renumérotation vers des assertions relatives.

## Critères d’acceptation

- [ ] La slide de partie annonce le TP guidé et ses cinq stations.
- [ ] Le quiz diagnostic Documents A/B et sa réponse sont conservés comme
  amorce brève du préambule.
- [ ] Le message « l’accessibilité ne se voit pas : elle se manipule et se
  vérifie » est explicite dans le support ou ses notes.
- [ ] Les productions attendues, les deux fichiers de départ, la checklist et
  les cartes WCAG sont présentés sans dépasser les cinq minutes du préambule.
- [ ] La station 1 relie règle, défaut Sami, procédure Word, encadré Writer,
  manipulation et preuve pour `P-01` à `P-05`.
- [ ] Les identifiants, libellés, niveaux et ordre de la station sont consommés
  directement depuis la matrice, sans liste normative recopiée dans le module.
- [ ] Les notes formateur portent les consignes, le minutage et les variantes
  guidée et autonome.
- [ ] Les modules supprimés ou fusionnés suivent l’inventaire de T01 ; aucune
  suppression supplémentaire n’est décidée par l’agent.
- [ ] Les assertions absolues sont migrées avant le premier ajout de slide dans
  `tests/test_plan_partie_1.py`, `tests/test_plan_partie_2.py`,
  `tests/test_plan_partie_3.py`, `tests/test_plan_partie_4.py`,
  `tests/test_slide_99_site_entrainement.py` et
  `tests/test_quiz_documents_sequence.py`.
- [ ] L’assertion qui impose le maintien de
  `scripts/slides/23b_quiz-final-reponses.py` est retirée ; le quiz final et sa
  correction peuvent ainsi être supprimés dans T14 sans casser un contrat
  intermédiaire.
- [ ] Les tests repèrent l’ordre relativement aux modules voisins, sans total
  global ni numéro absolu de slide.

## Preuves attendues

- [ ] Les tests ciblés du plan, du quiz A/B et de la station 1 passent.
- [ ] Un test structurel échoue si un module de slide recopie les identifiants,
  les libellés normatifs ou l’ordre de la station au lieu de consommer la
  matrice.
- [ ] Une génération ciblée puis un `make deck` complet ne produisent aucun
  avertissement de pied de page.
- [ ] La relecture visuelle confirme l’absence de chevauchement et la présence
  d’alternatives pertinentes.

## À préserver

- Les composants DSFR-IGPDE, les logos et la ligne de pied.
- Les parties I, III et IV, hors adaptation de tests devenus relatifs.

## Hors périmètre

- Construire les stations 2 à 5.
- Recopier le guide complet dans le deck.
