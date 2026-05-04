# Premortem - PRD exercice site des points de contrôle rapides

Date : 2026-05-04 18:58:15

## Contexte récolté

### Ce qu'on premortem

Le PRD `03-easy-checks/exercice-site-easy-checks-spec.md` décrit un exercice web pour la session 3 de la formation IGPDE : un faux site DSFR, `Ministère de l'Accessibilité numérique`, publié ensuite sur GitHub Pages, avec trois versions :

- `site-inaccessible/` pour l'audit ;
- `site-aide-correction/` avec aides progressives en accordéons DSFR ;
- `site-accessible/` sobre et corrigée.

Le site comporte 13 pages, une par Point de contrôle rapide du W3C. Les binômes se répartissent les pages, auditent un lot limité, remplissent la grille Excel et restituent collectivement.

### Public concerné

Communicants, agents publics et profils métier en initiation. Le public n'est pas développeur. La formation dure une journée et la séquence points de contrôle rapides doit rester praticable en 30 minutes.

### Victoire attendue

En 30 minutes, les binômes trouvent au moins un constat `NC` correctement prouvé sur les pages attribuées, utilisent la grille avec les bons verdicts/sévérités, comprennent la limite du pré-diagnostic points de contrôle rapides, puis comparent utilement avec l'aide et la version accessible.

### Contraintes explicitement données

- Les médias réels seront fournis juste après.
- Les composants DSFR seront traités avec les spécifications officielles que l'utilisateur fournira.
- La version accessible doit respecter les composants DSFR et leurs exigences d'accessibilité.
- Pas de CDN, assets DSFR localisés, GitHub Pages via `docs/`.
- Le contrat d'évaluation indique qu'une seule occurrence prouvée suffit à invalider le critère ciblé.

## Cadrage premortem

On est dans 6 mois. L'exercice site des points de contrôle rapides a échoué. La production a bien avancé, le site existe, mais la session n'a pas produit l'apprentissage attendu ou le livrable n'est pas maintenable. On remonte le fil pour comprendre pourquoi.

## Raisons d'échec brutes

1. Le PRD reste trop dispersé entre site, grille, aides, manifeste, corrigé et slides : une modification de contenu ou de règle crée des écarts entre les livrables.
2. La version accessible contient une erreur DSFR/RGAA visible par un participant avancé, ce qui fragilise la crédibilité de toute la séquence.
3. Le public non développeur passe trop de temps à comprendre les outils et les preuves techniques au lieu de produire des constats simples.
4. Les pages médias arrivent tard, les placeholders structurent mal les pages 9 à 11, et les checks sous-titres/transcription/audiodescription deviennent artificiels.
5. La page racine annonce trop clairement le Point de contrôle rapide ciblé : l'exercice devient un jeu de chasse à l'erreur annoncée plutôt qu'un entraînement au diagnostic.
6. Le corrigé public et les trois versions sur GitHub Pages deviennent des spoilers ou créent une confusion entre exercice et site de référence.
7. Le contrat d'évaluation est clair dans le PRD, mais il n'est pas transformé en source structurée : au moment de produire, chacun recopie à la main et des divergences apparaissent.

## Deep dives

### 1. Drift entre site, grille, aides, manifeste, corrigé et slides

#### Histoire de l'échec

La première version du site est produite correctement. Puis une formulation change dans la grille : "une occurrence suffit" devient plus explicite. Le manifeste est mis à jour, mais pas l'accordéon d'aide de la page 4. Ensuite, une preuve minimale change sur la page 12, mais le corrigé garde l'ancien exemple. Le jour de la formation, un binôme remonte une preuve acceptée par la grille mais rejetée par le corrigé.

La restitution devient une discussion de cohérence entre supports. Le formateur doit arbitrer oralement. Les stagiaires comprennent que l'exercice est intéressant, mais sentent que le dispositif n'est pas parfaitement aligné.

#### Hypothèse implicite

On suppose que plusieurs livrables pédagogiques peuvent rester synchronisés par discipline manuelle.

#### Signaux d'alerte précoces

- Une même phrase de règle existe à trois endroits ou plus.
- Une modification du contrat d'évaluation oblige à éditer manuellement plus de deux fichiers.

### 2. La version accessible n'est pas irréprochable

#### Histoire de l'échec

La version accessible respecte visuellement le DSFR. Pourtant, un composant accordéon ou formulaire diffère légèrement de la fiche officielle. Un participant plus technique inspecte le code, remarque un attribut manquant, un état clavier incomplet ou un libellé de champ discutable. Le sujet quitte les points de contrôle rapides et devient : "Votre corrigé est-il vraiment accessible ?"

Le problème est amplifié par l'exigence affichée dans le PRD : 100 % DSFR/accessibilité non négociable. Plus la promesse est haute, plus le moindre écart devient coûteux.

#### Hypothèse implicite

On suppose que la conformité DSFR peut être obtenue sans une revue composant par composant strictement tracée.

#### Signaux d'alerte précoces

- Une page utilise un composant DSFR dont la fiche Code/Accessibilité n'est pas référencée dans `manifest.md`.
- `validate.py` vérifie les fichiers présents, mais pas les patterns HTML obligatoires des composants utilisés.

### 3. L'exercice devient trop technique pour le public

#### Histoire de l'échec

Les stagiaires comprennent la mission, mais butent sur la preuve. Ils ne savent pas quoi copier : sélecteur CSS, capture WAVE, extrait HTML, observation clavier ? Les plus à l'aise techniquement avancent vite ; les autres attendent l'aide ou restent sur des constats vagues comme "le formulaire n'est pas accessible".

La grille est remplie, mais la colonne preuve est hétérogène. En restitution, certains constats sont pédagogiquement bons mais mal prouvés ; d'autres sont techniquement précis mais incompréhensibles pour le groupe.

#### Hypothèse implicite

On suppose que "preuve minimale" dans le PRD suffit à rendre la preuve praticable par des profils non développeurs.

#### Signaux d'alerte précoces

- Dans un pilote, moins de 70 % des lignes `NC` contiennent une preuve réutilisable.
- Les stagiaires demandent "qu'est-ce que je mets dans preuve ?" plus de deux fois en 15 minutes.

### 4. Les médias arrivent tard et les pages 9 à 11 sonnent faux

#### Histoire de l'échec

Les fichiers vidéo/audio sont fournis après la structure. Les durées, les contenus et les informations visuelles ne correspondent pas exactement aux cas prévus. La page audiodescription doit être réécrite parce que la vidéo ne contient finalement pas d'information visuelle essentielle. La page sous-titres montre une erreur trop évidente ou trop artificielle.

Les checks médias deviennent moins convaincants que les autres. Les stagiaires les traitent comme des cas théoriques, pas comme un audit réaliste.

#### Hypothèse implicite

On suppose que les médias pourront s'insérer tard sans changer la structure pédagogique des pages.

#### Signaux d'alerte précoces

- Les médias n'ont pas de transcript brut, de durée et de description des informations visuelles avant intégration.
- Une page média ne peut pas être évaluée sans explication orale du formateur.

### 5. La page racine guide trop l'audit

#### Histoire de l'échec

La page racine affiche pour chaque carte le titre réaliste et le Point de contrôle rapide ciblé. Cela rend la répartition efficace, mais l'exercice se transforme en recherche d'une erreur connue : "Page contraste, je cherche du contraste". Les stagiaires réussissent la grille, mais transfèrent moins bien la méthode sur un vrai site où les défauts ne sont pas étiquetés.

La restitution couvre les 13 checks, mais le diagnostic transversal reste faible. Les participants savent reconnaître les défauts quand on leur donne le thème ; ils sont moins prêts à explorer une page inconnue.

#### Hypothèse implicite

On suppose que l'affichage du Point de contrôle rapide ciblé accélère sans réduire la compétence diagnostique.

#### Signaux d'alerte précoces

- En pilote, les participants trouvent les défauts mais ne savent pas dire quel outil utiliser sans la carte.
- Dans la restitution, les phrases commencent par "comme c'était la page contraste..." plutôt que par "j'ai observé...".

### 6. Le corrigé public court-circuite les futures sessions

#### Histoire de l'échec

Le site est publié sur GitHub Pages avec les trois versions et le corrigé. Pour la première session, tout se passe bien. Pour une session suivante, un stagiaire retrouve le corrigé via la page racine ou une recherche dans le dépôt. Le groupe n'a pas tous les mêmes informations, et l'exercice perd son effet de récupération active.

Même sans triche volontaire, la présence publique de la version accessible pousse certains binômes à comparer trop tôt au lieu d'auditer.

#### Hypothèse implicite

On suppose que placer le corrigé dans "Après l'exercice" suffit à empêcher l'accès prématuré.

#### Signaux d'alerte précoces

- La page racine met les trois versions au même niveau visuel.
- Les liens "corrigé" et "site accessible" sont visibles sans friction avant la fin de l'activité.

### 7. Le contrat d'évaluation n'est pas exploité comme source unique

#### Histoire de l'échec

Le contrat d'évaluation existe dans le PRD et il est bon. Mais à la production, les pages HTML, les accordéons, le manifeste et le corrigé sont écrits séparément. Les intitulés ne divergent pas beaucoup, mais assez pour créer des écarts : une occurrence bonus devient attendue dans une aide, un faux-ami est absent du corrigé, une sévérité change.

Le PRD a résolu l'ambiguïté conceptuelle, mais pas la duplication opérationnelle. La maintenance devient fragile dès le premier changement.

#### Hypothèse implicite

On suppose que le PRD peut rester un document de référence passif au lieu de devenir une source de génération.

#### Signaux d'alerte précoces

- Le même constat minimal est recopié à la main dans `manifest.md`, `corrige-easy-checks.md` et `aide-correction.html`.
- Une revue trouve une différence de sévérité ou de preuve entre deux livrables.

## Synthèse

### L'échec le plus probable

Le plus probable est la dérive entre les livrables : site, aide, manifeste, corrigé, grille et slides. Le PRD est maintenant clair, mais si son contrat d'évaluation n'est pas transformé en source structurée, la production va recoller les informations à la main et introduire des divergences.

### L'échec le plus dangereux

Le plus dangereux est une version `site-accessible/` qui contient une erreur DSFR/RGAA. Elle est censée être la référence corrigée ; si elle est contestable, la crédibilité pédagogique du module baisse immédiatement.

### L'hypothèse cachée

L'hypothèse cachée est que la qualité pédagogique peut être maintenue par documentation. En réalité, il faut une source de vérité exploitable par la production : le contrat d'évaluation doit piloter le manifeste, le corrigé, les aides et les contrôles.

### Plan révisé

1. Créer une source structurée unique, par exemple `src/data/evaluation_contract.yml` ou `evaluation_contract.json`, reprenant les 13 lignes du contrat : page, check, constat minimal, preuve, sévérité, bonus, faux-amis, composants DSFR requis.
2. Générer depuis cette source `manifest.md`, le squelette du corrigé et les aides accordéon. Le PRD reste le document de cadrage, mais la source structurée devient la source de production.
3. Ajouter dans `validate.py` des contrôles de cohérence : 13 pages par version, aides présentes dans `site-aide-correction/`, absence d'aides dans `site-accessible/`, absence de CDN, liens d'évitement et ancres, titres, langue, présence médias, références de composants dans le manifeste.
4. Faire un pilote sur 3 pages avant de produire les 13 : page 1 images, page 5 lien d'évitement, page 12 formulaire. Ce trio couvre outil automatique, clavier et formulaire.
5. Geler les médias avant de finaliser les pages 9 à 11 : durée, transcript brut, besoin de sous-titres, informations visuelles essentielles et stratégie d'audiodescription.

### Checklist pré-lancement

- [ ] Le contrat d'évaluation existe en source structurée unique, pas seulement en Markdown.
- [ ] Chaque page liste ses composants DSFR et les fiches Code/Accessibilité consultées.
- [ ] Les trois pages pilotes sont testées par une personne qui n'a pas écrit le PRD.
- [ ] Les médias réels sont disponibles et vérifiés avant finalisation des pages 9 à 11.
- [ ] La page racine rend le parcours d'exercice prioritaire et garde corrigé/version accessible dans une zone clairement "Après l'exercice".
- [ ] `validate.py` détecte au moins une divergence volontaire ou involontaire entre les trois versions.

## Composants DSFR dont les spécifications sont nécessaires

### Indispensables transverses

- En-tête
- Navigation principale
- Liens d'évitement
- Pied de page
- Fil d'Ariane, si on le conserve
- Carte
- Accordéon

### Pages et formulaires

- Barre de recherche
- Champ de saisie
- Formulaire
- Bouton
- Case à cocher
- Bouton radio
- Alerte ou message d'erreur

### Contenus et médias

- Mise en avant
- Lien
- Contenu médias, si utilisé par le DSFR pour les pages audio/vidéo
- Transcription, si le composant DSFR est retenu

### Optionnels à confirmer

- Badge, si on affiche des statuts sur la page contraste
- Tableau, seulement si une page finit par utiliser un vrai tableau de données
- Tuile ou carte de téléchargement, selon le choix final pour la grille

