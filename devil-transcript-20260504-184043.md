# Devil Council - PRD exercice site Easy Checks

Date : 2026-05-04 18:40:43

## Proposition originale

Relire le PRD `03-easy-checks/exercice-site-easy-checks-spec.md` avec le skill Devil Council.

## Cible cadrée

La proposition à attaquer : produire un exercice web pour la session 3 de la formation IGPDE, sous forme d'un faux site DSFR `Ministère de l'Accessibilité numérique`, publié ensuite sur GitHub Pages, avec trois versions :

- `site-inaccessible/` pour l'audit ;
- `site-aide-correction/` avec aides progressives en accordéons DSFR ;
- `site-accessible/` sobre, corrigée et conforme DSFR/accessibilité.

Le site contient 13 pages, une par Easy Check du W3C. Chaque page reste réaliste, courte, ciblée, et comporte une erreur principale, parfois déclinée en plusieurs occurrences. Les stagiaires, communicants ou agents publics débutants, travaillent en binômes pendant 30 minutes, auditent 3 pages chacun, remplissent la grille Excel Easy Checks avec `C`, `NC`, `NA`, sévérité, constat, correctif et preuve, puis restituent collectivement.

Contraintes majeures : DSFR local sans CDN, composants DSFR officiels vérifiés, architecture statique Python sans Node, sortie `docs/`, page racine avec cartes des 13 pages, grille téléchargeable, manifeste et corrigé publics après l'exercice.

Hypothèses implicites :

- 13 pages peuvent rester faisables en 30 minutes via répartition en binômes.
- Trois versions restent maintenables sans dérive.
- Les erreurs multiples par page ne brouilleront pas le principe pédagogique.
- La version accessible peut atteindre un niveau DSFR/RGAA suffisamment solide.
- Les outils WAVE, ANDI, clavier, HeadingsMap et CCA seront disponibles et utilisables par le public.
- Le public comprendra la différence entre pré-diagnostic Easy Checks et audit RGAA.

Enjeu : si ce PRD est mal calibré, l'exercice deviendra trop long, trop technique, fragile à maintenir, ou pédagogiquement confus.

Clarification apportée après l'attaque initiale : les stagiaires sont répartis en plusieurs groupes, chaque groupe audite seulement un lot de pages, et une seule occurrence correctement prouvée suffit à invalider le critère ciblé. Les occurrences multiples sont des chances supplémentaires de détection, pas une exigence d'exhaustivité.

---

## Le Falsificationniste

Le test décisif est simple : donnez la page racine, la grille et 3 pages à deux binômes représentatifs du public cible, sans aide orale, avec 15 minutes strictes. Si chaque binôme ne produit pas au moins un constat correctement qualifié par page avec preuve, sévérité et correctif, le PRD est faux. Pas discutable : l'exercice n'est pas calibré pour sa cible.

Deuxième test : prenez une seule page enrichie avec trois cas, par exemple images, titres, formulaires ou langue. Si les stagiaires remontent trois erreurs comme trois Easy Checks différents, ou s'ils confondent faute RGAA, mauvaise pratique et faux-ami, l'hypothèse "une page = une erreur principale" est invalidée. Le PRD dit une erreur principale, mais décrit parfois une mini-leçon complète.

Troisième test : auditez la version accessible avec clavier, WAVE, ANDI et revue DSFR composant par composant. Si une seule page accessible échoue sur un composant DSFR standard, la promesse "version corrigée conforme" devient dangereuse. Elle ne peut plus servir de référence pédagogique.

Quatrième test : vérifiez que `validate.py` peut détecter les erreurs de cohérence entre les trois versions. S'il ne détecte que les liens et les titres, il ne protège pas la vraie fragilité : divergence de contenu, erreurs injectées au mauvais endroit, corrigé désynchronisé.

Si ces quatre tests échouent, l'idée s'effondre non pas conceptuellement, mais opérationnellement.

## Le Pré-mortem

On est en juin 2026. L'exercice est prêt visuellement, mais il échoue en salle. Les stagiaires ouvrent la page racine, voient 13 cartes, trois versions, une grille Excel, des outils multiples, un corrigé public, et perdent les cinq premières minutes à comprendre par où commencer. Le formateur compense oralement. Le temps d'audit réel tombe à 8 minutes.

Les pages ont été enrichies avec trois cas chacune. Sur le papier, c'était pédagogique. En réalité, les binômes ne savent plus s'ils doivent remonter une ligne, trois lignes, ou tous les défauts qu'ils voient. La page 3 sur les titres piège une moitié du groupe : ils marquent le saut de niveau comme `NC` alors que le corrigé dit "faux-ami". La restitution devient un débat de référentiel au lieu d'un entraînement au pré-diagnostic.

La production a aussi créé une dette : trois versions du site, 13 pages, DSFR local, médias placeholders, manifeste, corrigé, grille, GitHub Pages. À chaque ajustement, il faut synchroniser 39 pages générées et vérifier que la version accessible ne contient pas les erreurs de la version inaccessible. Une correction de contenu casse une ancre de skiplink ou une association `aria-describedby`.

Le jour J, les outils automatiques ne détectent pas les médias ou l'audiodescription. Les stagiaires pensent que la page est conforme parce que WAVE ne crie pas. L'exercice enseigne malgré lui une confiance excessive dans l'automatique.

L'échec n'est pas le concept. L'échec est l'ambition non bornée.

## L'Inverseur

L'opposé rigoureux du plan serait meilleur : ne pas construire un faux site complet en 13 pages. Construire un parcours court de 5 pages très maîtrisées, avec une matrice de cas dans le corrigé et les slides pour couvrir les 13 checks collectivement.

Pourquoi ? Parce que l'objectif n'est pas de produire un site. L'objectif est d'entraîner un public non développeur à observer, prouver, qualifier et formuler un correctif. Un faux ministère de 13 pages risque de déplacer l'attention vers la navigation, la crédibilité éditoriale, les outils et la mécanique GitHub Pages. On fabrique un environnement, alors qu'il faut fabriquer des décisions d'audit.

L'exact inverse serait aussi de supprimer la version accessible publique au départ. Garder seulement `site-inaccessible/` et `site-aide-correction/` pendant l'exercice, puis révéler la version corrigée après. Une version accessible immédiatement accessible sur la page racine crée une tentation de comparaison au lieu d'observation. Même si elle est placée "Après l'exercice", elle existe et peut court-circuiter l'effort.

Enfin, l'inverse de "trois cas par page" serait "un cas central par page, un seul piège bonus en corrigé". Le public débutant a besoin d'un signal net. Les subtilités RGAA sont précieuses, mais pas toutes dans le temps d'audit. Elles appartiennent à l'animation et au corrigé, pas forcément à la page à auditer.

## Le Contraintes-First

Ressources manquantes critiques :

1. Les vrais médias ne sont pas disponibles. Les pages 9, 10 et 11 dépendent de fichiers vidéo/audio, sous-titres, transcription et audiodescription. Tant qu'ils sont placeholders, l'exercice média est partiellement fictif.

2. La validation accessible n'est pas assez outillée. Le PRD liste `validate.py`, mais ses contrôles minimaux ne prouvent ni la conformité DSFR, ni les comportements clavier, ni la validité des erreurs injectées. WAVE et ANDI ne sont pas automatisés dans le pipeline.

3. Les assets DSFR locaux ne sont pas cadrés précisément : version exacte, fichiers nécessaires, fonts, pictogrammes, structure des chemins, licences, mise à jour future. La contrainte "pas de CDN" augmente fortement le travail d'intégration.

4. Les composants DSFR par page ne sont encore qu'une cartographie "pressentie". Or le PRD exige 100 % de respect des fiches. Cela impose une phase de recherche composant par composant avant production, non budgétée.

5. Le temps pédagogique est contradictoire. 30 minutes, 5 binômes, 13 pages, 3 pages par binôme, plusieurs occurrences par page, une grille à remplir, des preuves à produire, et une restitution collective : ce volume est trop serré.

6. La règle de publication GitHub Pages n'est pas complète : base path, liens relatifs, cache assets, accès au corrigé, indexation publique, risque de confusion avec un vrai ministère fictif.

7. Le propriétaire de la maintenance n'est pas défini. Qui met à jour DSFR, RGAA, la grille, le corrigé, les médias et les slides lorsque l'un change ?

## Le Second-Ordre

Effet de deuxième ordre : parce que la racine affiche clairement l'Easy Check ciblé sur chaque carte, les stagiaires ne cherchent plus "quel problème d'accessibilité existe ici". Ils cherchent "l'erreur correspondant au libellé annoncé". Cela accélère l'exercice, mais réduit la compétence de diagnostic transversal. La grille devient un jeu d'association.

Effet de troisième ordre : en enrichissant chaque page avec trois occurrences, la restitution collective se transforme en correction exhaustive. Le formateur doit arbitrer quels constats étaient attendus, lesquels étaient bonus, lesquels étaient faux-amis. Les participants retiennent que l'accessibilité est pleine d'exceptions et de pièges, pas qu'ils ont une méthode simple d'entrée.

Cascade de maintenance : une modification DSFR ou une correction RGAA dans la version accessible doit se répercuter sur l'aide, le manifeste, le corrigé, la grille, les slides et les liens GitHub Pages. Plus le site est pédagogiquement riche, plus chaque évolution future coûte cher. Le risque n'est pas le build initial, c'est la seconde session.

Cascade publique : le corrigé et la version accessible sont publics. Des stagiaires futurs peuvent les trouver avant la session. L'exercice perd alors sa force de récupération active. À long terme, le formateur devra soit accepter que les réponses circulent, soit maintenir plusieurs variantes.

Cascade de confiance : si la version accessible est présentée comme corrigée et qu'un participant avancé trouve une faille DSFR/RGAA, la crédibilité du module baisse. Le standard que le PRD impose devient aussi le standard sur lequel l'exercice sera jugé.

---

# Verdict du Devil Council

## Convergence des attaques

Trois attaques convergent sur la même faiblesse : le scope est trop riche pour le temps pédagogique. Le Falsificationniste le teste par un pilote de 15 minutes, le Pré-mortem raconte l'échec en salle, et le Contraintes-First montre que le volume réel dépasse largement une activité de 30 minutes.

Deuxième convergence : les trois versions multiplient la valeur pédagogique, mais aussi la surface de dérive. Pré-mortem, Contraintes-First et Second-Ordre convergent sur le même risque : désynchronisation entre site inaccessible, aide, version accessible, manifeste, corrigé, grille et slides.

Troisième convergence : le principe "une page = une erreur principale" reste fragile si la règle d'évaluation n'est pas écrite. La clarification résout une partie du risque : une seule occurrence suffit. Il faut maintenant que le PRD l'impose partout pour éviter que les occurrences bonus soient interprétées comme de l'exhaustivité attendue.

## Divergences méthodologiques

L'Inverseur attaque la forme même du projet : il suggère de réduire le site, voire de ne pas faire un faux site complet. Les autres attaquants acceptent le faux site mais exigent des garde-fous. Cette divergence est utile : elle montre que le concept est défendable si le scope est borné, mais qu'il n'est pas évident que 13 pages soient le format optimal.

Le Falsificationniste demande des tests réels avant décision. Le Contraintes-First demande des prérequis avant production. Ce ne sont pas les mêmes temporalités : l'un veut prouver vite que l'exercice marche en salle, l'autre veut sécuriser l'industrialisation.

## Angles morts collectifs

Le principal angle mort est la gouvernance du corrigé. Le PRD dit quoi produire, mais pas qui arbitre les cas discutables RGAA, qui valide la sévérité indicative, et qui maintient la cohérence lorsque le référentiel, DSFR ou la grille évoluent.

Deuxième angle mort : le risque de guidage excessif. La page racine affiche l'Easy Check ciblé. C'est pratique pour tenir 30 minutes, mais cela transforme l'audit en recherche d'une erreur annoncée. Le PRD ne dit pas comment compenser cela dans l'animation.

Troisième angle mort : la preuve attendue. La grille demande une preuve, mais la spec ne définit pas encore, page par page, la preuve minimale acceptable : sélecteur CSS, capture, extrait HTML, mesure de contraste, comportement clavier, résultat ANDI, etc.

## Diagnostic

L'idée résiste comme concept pédagogique. Avec la clarification "une occurrence suffit" et "les groupes se répartissent les pages", elle résiste mieux comme scénario de classe. Elle ne résiste pas encore totalement comme PRD de production.

Le format est pertinent, aligné avec Sami, cohérent avec la session 3, et fort pédagogiquement. Mais le PRD actuel est trop généreux : il décrit un exercice, un site de démonstration, un corrigé public, une mini-bibliothèque DSFR et une base de maintenance. Sans bornage supplémentaire, la production risque de livrer un objet impressionnant mais trop dense pour l'usage en salle.

Le projet doit passer par une étape de durcissement : définir pour chaque page un "noyau audit" obligatoire, des "cas bonus" éventuels, une preuve minimale, une sévérité attendue et une limite de temps. Ensuite seulement, produire le site.

## Le point de rupture

Le point de rupture est l'ambiguïté résiduelle entre **constat minimal attendu** et **occurrences bonus**.

Si cette ambiguïté n'est pas résolue, tout le reste devient secondaire : certains binômes chercheront l'exhaustivité, d'autres s'arrêteront au premier défaut, et le corrigé semblera arbitraire.

Correctif prioritaire : ajouter au PRD une table page par page avec :

- constat attendu principal ;
- cas bonus autorisés ;
- nombre de lignes attendues dans la grille ;
- preuve minimale ;
- sévérité indicative ;
- temps cible ;
- ce qui ne doit pas être pénalisé.

Tant que cette table n'existe pas, ne pas lancer la production HTML.
