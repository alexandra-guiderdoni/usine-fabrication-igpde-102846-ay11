# Audit RGAA 106 critères - site corrigé index

Date : 4 juillet 2026

## Résultat

Page auditée : `http://127.0.0.1:8765/site-accessible/index.html`.

Référentiel : RGAA 4.1.2, 106 critères. Le référentiel AY11 local contient 258 tests associés.

Statuts après correction : 33 conformes, 0 non conforme, 60 non applicables, 13 non testés.

Taux sur critères testés et applicables : 100,0 % (`C / (C + NC)`).

Non-conformité confirmée restante sur cette page : aucune dans le périmètre testé.

## Preuves exécutées

- `curl -I` : page servie en HTTP 200 lors de la passe initiale.
- `ay11 rgaa validate` : référentiel local valide, 13 thématiques, 106 critères, 258 tests.
- `ay11 rgaa profile rgaa-106 --require-executable` : profil strict exécutable.
- `ay11 preaudit capture-browser ... --axe --form-interactions` : capture navigateur, axe-core 4.12.1, arbre d’accessibilité, trace clavier.
- `ay11 preaudit build ... --profile rgaa-106` : signaux candidats restants 8.7 et 12.6, non confirmés en non-conformités.
- Passe DOM locale après correction : titres `h1` puis `h2`, sans saut de niveau.
- Recette Playwright : liens d’évitement, ordre de tabulation, menu mobile, reflow 320 px, aperçu sans styles.

## Synthèse axe-core après correction

- Violations : 0.
- Incomplete : 1 (`color-contrast`, 55 cibles, calcul impossible sur certains arrière-plans DSFR).
- Passes : 39.
- Inapplicable : 50.

## Correction vérifiée

La non-conformité RGAA 9.1 relevée dans la passe initiale est corrigée.

Preuve DOM après correction :

- `h1` : `Site corrigé et conforme DSFR/accessibilité`
- titres de cartes : 13 titres en `h2`, de `#1 Actualité illustrée` à `#13 Formulaire de contact`
- sauts de niveaux détectés : aucun (`BAD_JUMPS []`)
- axe-core : aucune violation, règle `heading-order` absente des violations

## Tableau des 106 critères

| Critère | Statut | Observation |
|---|---:|---|
| 1.1 | C | Deux images informatives IGPDE avec alternative textuelle. |
| 1.2 | NA | Aucune image décorative observée. |
| 1.3 | C | Alternatives observées pertinentes pour les logos IGPDE. |
| 1.4 | NA | Aucune image complexe nécessitant une description détaillée. |
| 1.5 | NA | Aucune image complexe nécessitant une description détaillée. |
| 1.6 | NA | Aucune image complexe nécessitant une description détaillée. |
| 1.7 | NA | Aucune image complexe nécessitant une description détaillée. |
| 1.8 | NA | Aucune image texte hors logo institutionnel à remplacer par du texte stylé. |
| 1.9 | NA | Aucune légende d’image observée. |
| 2.1 | NA | Aucun cadre ou iframe observé. |
| 2.2 | NA | Aucun cadre ou iframe observé. |
| 3.1 | C | Aucune information observée comme donnée uniquement par la couleur. |
| 3.2 | NT | axe-core signale color-contrast en incomplete : mesure manuelle nécessaire. |
| 3.3 | NT | Contraste des composants graphiques non mesuré de manière instrumentée. |
| 4.1 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.2 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.3 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.4 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.5 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.6 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.7 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.8 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.9 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.10 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.11 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.12 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 4.13 | NA | Aucun média temporel ou non temporel observé sur cette page. |
| 5.1 | NA | Aucun tableau HTML observé. |
| 5.2 | NA | Aucun tableau HTML observé. |
| 5.3 | NA | Aucun tableau HTML observé. |
| 5.4 | NA | Aucun tableau HTML observé. |
| 5.5 | NA | Aucun tableau HTML observé. |
| 5.6 | NA | Aucun tableau HTML observé. |
| 5.7 | NA | Aucun tableau HTML observé. |
| 5.8 | NA | Aucun tableau HTML observé. |
| 6.1 | C | Les liens visibles ont des intitulés explicites dans leur contexte. |
| 6.2 | C | Les liens activables ont un intitulé accessible ; le fil d’Ariane courant sans href n’est pas un lien activable. |
| 7.1 | NT | Composants DSFR scriptés observés, mais compatibilité technologies d’assistance non testée avec lecteur d’écran réel. |
| 7.2 | NA | Aucune alternative à un script nécessaire observée. |
| 7.3 | C | Menu mobile et navigation testés au clavier ; pas de blocage observé. |
| 7.4 | C | Aucun changement de contexte non averti ou non contrôlable observé. |
| 7.5 | NA | Aucune alerte non sollicitée observée. |
| 8.1 | C | Doctype HTML5 présent. |
| 8.2 | NT | Validation complète du code source non exécutée avec validateur HTML ; pas d’anomalie bloquante détectée par axe-core. |
| 8.3 | C | Attribut html lang="fr" présent. |
| 8.4 | C | Code langue fr pertinent pour le contenu principal. |
| 8.5 | C | Balise title présente. |
| 8.6 | C | Titre de page pertinent pour identifier la page. |
| 8.7 | C | Aucun passage en langue étrangère nécessitant balisage observé ; signaux AY11 non confirmés. |
| 8.8 | C | Langue de restitution cohérente avec la langue déclarée. |
| 8.9 | C | Aucune balise de présentation type font, center, b/i de présentation observée. |
| 8.10 | NA | Aucun changement de direction de lecture observé. |
| 9.1 | C | Hiérarchie corrigée : h1 suivi de h2 pour les 13 cartes, aucun saut de niveau observé. |
| 9.2 | C | Zones header, navigation, main, breadcrumb et footer structurées. |
| 9.3 | C | Listes de navigation et de footer structurées avec ul/ol/li. |
| 9.4 | NA | Aucune citation observée. |
| 10.1 | C | Aucune information observée comme donnée uniquement par forme, taille ou position. |
| 10.2 | C | Contenu principal encore présent dans l’aperçu sans styles. |
| 10.3 | C | Ordre DOM compréhensible dans l’aperçu sans styles. |
| 10.4 | NT | Zoom 200 % non testé exhaustivement ; reflow 320 px vérifié séparément. |
| 10.5 | NT | Déclarations de couleurs CSS non auditées exhaustivement. |
| 10.6 | C | Les liens sont visuellement identifiables dans leur contexte de navigation ou de carte. |
| 10.7 | C | Focus visible : skiplinks/nav outline 2 px ; cartes via pseudo-élément a::before outline 2 px. |
| 10.8 | NT | Contenus masqués DSFR non vérifiés dans l’arbre d’accessibilité lecteur d’écran. |
| 10.9 | C | Aucune information observée comme donnée uniquement par forme, taille ou position. |
| 10.10 | C | Aucun contenu visible reposant uniquement sur du positionnement CSS observé. |
| 10.11 | C | Viewport 320 px : aucun débordement horizontal observé. |
| 10.12 | NT | Espacement utilisateur personnalisé non testé. |
| 10.13 | NT | Contenus additionnels au survol/focus non testés exhaustivement ; composants principaux sans défaut observé. |
| 10.14 | NA | Aucun contenu additionnel uniquement CSS observé. |
| 11.1 | NA | Aucun formulaire observé sur cette page. |
| 11.2 | NA | Aucun formulaire observé sur cette page. |
| 11.3 | NA | Aucun formulaire observé sur cette page. |
| 11.4 | NA | Aucun formulaire observé sur cette page. |
| 11.5 | NA | Aucun formulaire observé sur cette page. |
| 11.6 | NA | Aucun formulaire observé sur cette page. |
| 11.7 | NA | Aucun formulaire observé sur cette page. |
| 11.8 | NA | Aucun formulaire observé sur cette page. |
| 11.9 | NA | Aucun formulaire observé sur cette page. |
| 11.10 | NA | Aucun formulaire observé sur cette page. |
| 11.11 | NA | Aucun formulaire observé sur cette page. |
| 11.12 | NA | Aucun formulaire observé sur cette page. |
| 11.13 | NA | Aucun formulaire observé sur cette page. |
| 12.1 | C | Deux accès de navigation observés sur la page : navigation principale et lien vers le plan du site. |
| 12.2 | NT | Cohérence inter-pages non vérifiée dans cette passe page seule. |
| 12.3 | NT | Pertinence de la page plan du site non auditée dans cette passe. |
| 12.4 | NT | Accès au plan du site sur l’ensemble des pages non vérifié ici. |
| 12.5 | NA | Aucun moteur de recherche sur cette page. |
| 12.6 | C | Liens d’évitement vers contenu, menu principal et footer ; ancres présentes et activation testée. |
| 12.7 | C | Lien d’évitement vers le contenu présent et fonctionnel. |
| 12.8 | C | Ordre de tabulation cohérent sur le parcours testé. |
| 12.9 | C | Aucun piège clavier observé ; menu mobile ouvert puis fermé par Échap avec retour focus. |
| 12.10 | NA | Aucun raccourci clavier caractère unique observé. |
| 12.11 | C | Menu mobile atteignable et refermable au clavier ; pas de contenu additionnel bloquant observé. |
| 13.1 | NA | Aucune limite de temps observée. |
| 13.2 | C | Aucune ouverture automatique de nouvelle fenêtre ; les liens externes s’ouvrent après action utilisateur. |
| 13.3 | NA | Aucun document bureautique à télécharger observé sur cette page. |
| 13.4 | NA | Aucun document bureautique à télécharger observé sur cette page. |
| 13.5 | NA | Aucun contenu cryptique nécessitant alternative observé. |
| 13.6 | NA | Aucun contenu en mouvement, clignotant ou flash observé. |
| 13.7 | NA | Aucun contenu en mouvement, clignotant ou flash observé. |
| 13.8 | NA | Aucun contenu en mouvement, clignotant ou flash observé. |
| 13.9 | NT | Orientation écran non testée explicitement. |
| 13.10 | NA | Aucun geste complexe requis observé. |
| 13.11 | NA | Aucune fonctionnalité spécifique de pointage sur point unique hors liens standard observée. |
| 13.12 | NA | Aucune fonctionnalité impliquant un mouvement d’appareil observée. |

## Limites

- Cette passe n’est pas une certification par organisme tiers.
- Les critères `NT` restent exclus du taux, conformément au calcul RGAA.
- Aucun test lecteur d’écran réel n’a été exécuté.
- Les contrastes remontés `incomplete` par axe-core doivent être mesurés manuellement pour conclure RGAA 3.2 et 3.3.
- Les critères inter-pages, comme la cohérence du menu ou du plan du site sur l’ensemble du site, exigent un échantillon multi-pages.
