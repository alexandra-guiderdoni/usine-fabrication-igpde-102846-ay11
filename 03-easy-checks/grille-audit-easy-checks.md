# IGPDE - Formation 102638 - Grille d'audit 13 Easy Checks du W3C

Grille opérationnelle pour la formation IGPDE 102638 « L'accessibilité numérique pour la bureautique et le web ». Inspirée méthodologiquement de la grille Easy Checks de beta.gouv.fr et alignée sur le RGAA 4.1.2.

> **Avertissement**
> Cet outil est un **outil de sensibilisation et de pré-diagnostic**. Il ne remplace en aucun cas un audit RGAA formel (106 critères sur 13 thématiques) réalisé par un expert certifié. Le « Taux de conformité Easy Checks » calculé ici n'est PAS le taux de conformité RGAA officiel publié en déclaration d'accessibilité.

---

## Mode d'emploi

### Préparer l'audit

1. Constituer l'échantillon de pages à auditer selon le RGAA 4.1.2 (voir section ci-dessous)
2. Ouvrir chaque page dans un navigateur récent (Chrome, Firefox, Edge)
3. Installer la boîte à outils a11y : https://a11y-tools.netlify.app/
4. Préparer un casque audio pour tester un lecteur d'écran (VoiceOver sur Mac, NVDA gratuit sur Windows)

### Échantillon RGAA 4.1.2 - pages obligatoires

La méthode technique du RGAA impose un échantillon minimal pour déclarer la conformité d'un site public. Source officielle : [accessibilite.numerique.gouv.fr](https://accessibilite.numerique.gouv.fr/).

**Pages obligatoires** (auditer systématiquement, mentionner NA si la fonction n'existe pas) :

| # | Type de page | Caractère | Commentaire |
|---|--------------|-----------|-------------|
| 1 | Page d'accueil | Obligatoire | Toujours auditée, même si une page de connexion précède |
| 2 | Page « Mentions légales » | Obligatoire | Page réglementaire, présente sur tous les sites publics |
| 3 | Déclaration d'accessibilité | Obligatoire | Décrit l'état de conformité (article 47 de la loi de 2005) |
| 4 | Page « Plan du site » | Obligatoire | Si présent ; sinon mentionner NA |
| 5 | Page « Contact » | Obligatoire | Formulaire ou page avec coordonnées de l'organisme |
| 6 | Page « Aide » / FAQ | Obligatoire | Si présente ; sinon mentionner NA |
| 7 | Page d'authentification / connexion | Obligatoire si existante | Auditée uniquement si espace personnel |
| 8 | Page de résultats de recherche | Obligatoire si moteur | Auditée avec un jeu de résultats réel |
| 9 | Document téléchargeable (PDF, DOCX, ODT) | Obligatoire si présent | Au moins un document représentatif. Pour un audit formel des documents, utiliser PAC 2024 (gratuit), Acrobat Pro ou Axes4 — les 13 Easy Checks web ne couvrent que partiellement les documents |

**Pages représentatives** (au moins une par type de gabarit du site) :

| # | Type de page | Exemples |
|---|--------------|----------|
| 10 | Article, actualité, contenu rédactionnel | Page de news, fiche thématique, billet de blog |
| 11 | Formulaire de démarche ou saisie multi-étape | Inscription, demande de rendez-vous, dépôt de dossier |
| 12 | Liste / rubrique / résultats de navigation | Liste de publications, catalogue, annuaire filtrable |

**Règle pratique** : un audit RGAA ne peut être publié qu'après avoir audité au minimum l'ensemble des pages obligatoires existantes + au moins une page par gabarit représentatif.

### Pour chaque critère, répondre aux 5 questions

1. **Verdict** : le critère passe-t-il ? (Conforme / Non conforme / Non applicable)
2. **Sévérité** : si non conforme, quel impact sur l'utilisateur ? (Bloquant / Gênant / Mineur / Info)
3. **Constat** : qu'avez-vous observé concrètement ?
4. **Correctif** : quelle action l'équipe web devra-t-elle mener ?
5. **Preuve** : URL précise, capture d'écran, sélecteur CSS, extrait de code

### Règle pour l'exercice en binômes

Les pages sont réparties entre plusieurs groupes : chaque binôme audite uniquement les pages qui lui sont attribuées. Pour une page donnée, **une seule occurrence correctement prouvée suffit à renseigner `NC`** sur le critère ciblé. Les autres occurrences éventuelles sont des bonus utiles pour la restitution, mais elles ne sont pas exigées pour invalider le critère.

### Conventions de verdict

| Code | Libellé | Définition |
|------|---------|------------|
| C | Conforme | Le critère est respecté sans réserve |
| NC | Non conforme | Un défaut objectif a été constaté |
| NA | Non applicable | Le critère ne s'applique pas à cette page (ex. pas de vidéo) |

### Conventions de sévérité

| Niveau | Impact utilisateur |
|--------|--------------------|
| Bloquant | Certaines personnes sont exclues du service |
| Gênant | Certaines personnes ont des difficultés importantes |
| Mineur | L'ergonomie peut être améliorée, mais l'accès reste possible |
| Info | Observation pour améliorer sans blocage |

---

## Métadonnées de l'audit

| Champ | Valeur |
|-------|--------|
| Auditeur / auditrice | |
| Date | |
| Organisme | |
| URL de la page auditée | |
| Intitulé de la page | |
| Navigateur + version | |
| Système d'exploitation | |
| Outils utilisés | |
| Contexte (desktop, mobile, tablette) | |

---

## Grille détaillée - 13 critères

### 1. Alternatives textuelles des images

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 1. Alternatives textuelles des images |
| WCAG 2.2 | 1.1.1 Contenu non textuel |
| RGAA 4.1.2 | 1.1, 1.2, 1.3, 1.6, 1.7, 1.8, 1.9 |
| Méthode de test | Bookmarklet « Check images » OU clic droit « Inspecter » sur chaque image, examiner l'attribut `alt` |
| Outils recommandés | Bookmarklet Check images, extension WAVE, Accessibility Tree des DevTools |
| Ce qu'il faut vérifier | (a) alt présent pour chaque `<img>` ; (b) alt vide (`alt=""`) pour les décoratives ; (c) alt explicite (action attendue) pour les images dans liens/boutons ; (d) description longue pour graphiques/schémas complexes |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve (URL, sélecteur, capture) | |

### 2. Titre de page

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 2. Titre de page |
| WCAG 2.2 | 2.4.2 Titre de page |
| RGAA 4.1.2 | 8.5, 8.6 |
| Méthode de test | Survoler l'onglet du navigateur, lire la balise `<title>` via « Afficher le code source » |
| Outils recommandés | Bookmarklet Check page title, DevTools |
| Ce qu'il faut vérifier | (a) titre présent ; (b) titre unique pour chaque page du site ; (c) information prioritaire en premier (front-loading) ; (d) titre change quand le contenu principal change |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 3. Titres et hiérarchie

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 3. Titres (headings) |
| WCAG 2.2 | 1.3.1 Information et relations, 2.4.6 En-têtes et étiquettes |
| RGAA 4.1.2 | 9.1 Hiérarchie de titres |
| Méthode de test | Extension HeadingsMap ou bookmarklet Check headings ; parcourir l'arbre des titres |
| Outils recommandés | HeadingsMap, WAVE, outil d'arbre ARIA |
| Ce qu'il faut vérifier | (a) un seul `<h1>` par page reprenant le sujet ; (b) niveaux emboîtés sans saut (H1 > H2 > H3) ; (c) titres balisés avec `<h1>` à `<h6>`, pas uniquement avec du CSS ; (d) chaque section significative porte un titre |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 4. Contraste des couleurs

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 4. Contraste |
| WCAG 2.2 | 1.4.3 Contraste (minimum), 1.4.11 Contraste non textuel |
| RGAA 4.1.2 | 3.2, 3.3 |
| Méthode de test | Pipette DevTools, WebAIM Contrast Checker, Colour Contrast Analyser (app desktop) |
| Outils recommandés | DevTools, WebAIM Contrast Checker, CCA (TPGi), extension Stark |
| Ce qu'il faut vérifier | (a) texte normal ≥ 4,5:1 ; (b) texte large (≥ 18 pt ou ≥ 14 pt gras) ≥ 3:1 ; (c) composants d'interface et éléments graphiques porteurs d'information ≥ 3:1 ; (d) mesurer sur la zone la moins contrastée (dégradés, images en arrière-plan) |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 5. Lien d'évitement

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 5. Lien d'évitement |
| WCAG 2.2 | 2.4.1 Contourner des blocs |
| RGAA 4.1.2 | 12.7 |
| Méthode de test | Charger la page, appuyer une fois sur `Tab` : un lien « Aller au contenu » doit apparaître |
| Outils recommandés | Clavier uniquement |
| Ce qu'il faut vérifier | (a) lien présent comme 1er élément focus de la page ; (b) visible quand il a le focus (même s'il est masqué par défaut) ; (c) cible une ancre valide (#contenu, #main) ; (d) libellé explicite (« Aller au contenu », « Passer la navigation ») |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 6. Focus et navigation clavier (Easy Check 6 élargi)

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 6. Focus clavier visible (élargi à la navigation complète) |
| WCAG 2.2 | 2.4.7 Visibilité du focus, 2.1.1 Clavier, 2.1.2 Pas de piège au clavier, 2.4.3 Parcours du focus |
| RGAA 4.1.2 | 10.7 Focus visible, 12.13 Fonctionnalités au clavier, 12.14 Pas de piège, 10.3 Ordre de tabulation |
| Méthode de test | Cacher la souris ; naviguer uniquement au clavier (Tab, Shift+Tab, Entrée, Espace, flèches) sur un parcours complet |
| Outils recommandés | Clavier uniquement, éventuellement extension « Focus Outline » |
| Ce qu'il faut vérifier | (a) indicateur de focus visible sur tous les éléments interactifs ; (b) ordre de tabulation logique (haut-bas, gauche-droite) ; (c) tous les composants interactifs atteignables et activables au clavier ; (d) pas de piège au clavier (focus bloqué dans une zone) ; (e) état (coché, développé, sélectionné) annoncé |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 7. Langue de la page

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 7. Langue de la page |
| WCAG 2.2 | 3.1.1 Langue de la page, 3.1.2 Langue d'un passage |
| RGAA 4.1.2 | 8.3, 8.4 |
| Méthode de test | Clic droit « Afficher le code source », chercher `<html lang="…">` |
| Outils recommandés | Extension Web Developer > Information > View Document Language, DevTools |
| Ce qu'il faut vérifier | (a) `<html lang="fr">` (ou code ISO 639 valide) présent ; (b) passages dans une autre langue balisés `<span lang="en">…</span>` ; (c) pas de valeur farfelue comme `lang="français"` |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 8. Zoom 200 %

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 8. Redimensionnement du texte |
| WCAG 2.2 | 1.4.4 Redimensionnement du texte, 1.4.10 Redistribution |
| RGAA 4.1.2 | 10.4, 10.11 |
| Méthode de test | Ctrl + (ou Cmd +) jusqu'à 200 %, parcourir la page |
| Outils recommandés | Navigateur uniquement ; DevTools responsive pour simuler 320 CSS px |
| Ce qu'il faut vérifier | (a) aucun texte coupé, superposé ou tronqué à 200 % ; (b) pas de défilement horizontal forcé sur une page classique ; (c) menus, boutons et formulaires restent utilisables ; (d) pas de texte en image qui ne se redimensionne pas |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 9. Sous-titres (vidéos préenregistrées)

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 9. Sous-titres |
| WCAG 2.2 | 1.2.2 Sous-titres (pré-enregistrés) |
| RGAA 4.1.2 | 4.3, 4.4 |
| Méthode de test | Lancer la vidéo, vérifier la présence d'un bouton CC ; couper le son et vérifier la compréhension |
| Outils recommandés | Lecteur vidéo |
| Ce qu'il faut vérifier | (a) sous-titres synchronisés présents et activables ; (b) couvrent les paroles et les informations sonores importantes ((rires), (musique)) ; (c) qualité éditoriale (pas uniquement auto-générés non relus) ; (d) 2 lignes max à l'écran, timing respirable |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 10. Transcriptions audio et vidéo

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 10. Transcriptions |
| WCAG 2.2 | 1.2.1 Contenus seulement audio et seulement vidéo pré-enregistrés |
| RGAA 4.1.2 | 4.1, 4.2 |
| Méthode de test | Chercher un lien « Transcription » ou « Lire le texte » visible près du média |
| Outils recommandés | Navigation visuelle |
| Ce qu'il faut vérifier | (a) transcription accessible depuis la même page ou à un clic visible ; (b) contenu complet (paroles + bruits utiles) ; (c) pour les vidéos muettes ou documentaires : transcription descriptive incluant l'action à l'écran ; (d) structure navigable (titres, paragraphes) |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 11. Audiodescription

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 11. Audiodescription |
| WCAG 2.2 | 1.2.3, 1.2.5 Audiodescription (pré-enregistrée) |
| RGAA 4.1.2 | 4.5, 4.6 |
| Méthode de test | Vérifier la présence d'une piste audiodécrite (bouton AD) ou d'une version décrite téléchargeable |
| Outils recommandés | Lecteur vidéo |
| Ce qu'il faut vérifier | (a) audiodescription disponible pour les vidéos informatives avec contenu visuel essentiel ; (b) intercalée dans les silences (ne couvre pas les dialogues) ; (c) pertinente (décrit ce qui importe) ; (d) exception : si la vidéo est entièrement narrée en voix off, AD souvent superflue |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 12. Étiquettes de formulaire

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 12. Étiquettes et instructions de formulaire |
| WCAG 2.2 | 3.3.2 Étiquettes ou instructions, 1.3.1 Information et relations, 2.5.3 Étiquette dans le nom |
| RGAA 4.1.2 | 11.1, 11.2, 11.3 |
| Méthode de test | Tester « clic sur le libellé » : le focus doit sauter dans le champ ; parcourir le formulaire au clavier ; activer VoiceOver ou NVDA |
| Outils recommandés | Clavier, lecteur d'écran, DevTools Accessibility Tree |
| Ce qu'il faut vérifier | (a) chaque champ a une étiquette visible et persistante ; (b) association programmatique (`<label for="…">` ou `aria-labelledby`) ; (c) placeholder utilisé comme exemple de format, jamais comme étiquette unique ; (d) groupes de champs encadrés par `<fieldset>` + `<legend>` (radios, checkboxes, adresse multi-champs) |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

### 13. Champs obligatoires et erreurs de saisie

| Champ | Valeur |
|-------|--------|
| Easy Check W3C | 13. Champs obligatoires |
| WCAG 2.2 | 3.3.2 Étiquettes, 3.3.1 Identification des erreurs, 3.3.3 Suggestion après erreur |
| RGAA 4.1.2 | 11.10, 11.11 |
| Méthode de test | Soumettre un formulaire incomplet ; activer un lecteur d'écran et vérifier l'annonce ; zoomer à 200 % |
| Outils recommandés | Lecteur d'écran, clavier, DevTools |
| Ce qu'il faut vérifier | (a) champs obligatoires indiqués textuellement (pas uniquement par astérisque rouge) ; (b) légende « * champ obligatoire » présente ; (c) attribut `required` ou `aria-required="true"` ; (d) messages d'erreur identifient le champ par son libellé (« Votre adresse électronique est obligatoire », pas « Erreur champ 3 ») ; (e) erreurs annoncées par le lecteur d'écran (via `aria-live` ou focus) |
| Verdict | ☐ C ☐ NC ☐ NA |
| Sévérité | ☐ Bloquant ☐ Gênant ☐ Mineur ☐ Info |
| Constat | |
| Correctif suggéré | |
| Preuve | |

---

## Synthèse de l'audit

### Décompte par verdict

| Verdict | Nombre de critères | Pourcentage |
|---------|-------------------:|------------:|
| Conforme (C) | | / 13 |
| Non conforme (NC) | | / 13 |
| Non applicable (NA) | | / 13 |

**Taux de conformité Easy Checks** : (C) / (C + NC) × 100 = ___ %

### Répartition des non-conformités par sévérité

| Sévérité | Nombre |
|----------|-------:|
| Bloquant | |
| Gênant | |
| Mineur | |
| Info | |

### Top 3 actions prioritaires

| # | Critère concerné | Action | Échéance proposée |
|---|------------------|--------|-------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Engagement personnel

**La première action que je mettrai en œuvre dès demain 9 h** :

---

## Références

- Easy Checks W3C WAI : https://www.w3.org/WAI/test-evaluate/easy-checks/
- Corpus traduit : `03-easy-checks/w3c-easy-checks-fr.md`
- Correspondance WCAG / RGAA : `03-easy-checks/correspondance-wcag-rgaa.md`
- Inspiration méthodologique : grille Easy Checks de beta.gouv.fr
- Boîte à outils a11y : https://a11y-tools.netlify.app/
