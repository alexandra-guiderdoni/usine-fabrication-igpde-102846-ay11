# Outils Windows et liens d’installation - formation 102846

Vérification des sources : 4 octobre 2026. Inventaire établi à partir des six présentations PPTX de `Livrables-Stagiaires/supports-projections/`, de leurs notes de présentation et des autres livrables stagiaires, notamment la fiche « Liens pour les stagiaires » et le site d’exercice. Les outils ajoutés explicitement par Alex figurent aussi ci-dessous.

Les fichiers sont rangés dans trois sous-dossiers : [`application-windows/`](./application-windows/), [`extension-firefox/`](./extension-firefox/) et [`extension-edge/`](./extension-edge/). Le dossier Edge contient des paquets CRX issus des catalogues Microsoft Edge Add-ons et Chrome Web Store ; les quatre fichiers anciens se trouvent dans `application-windows/archives/`. Les 26 paquets courants, le module Focus Highlight fourni pour essai et les deux favoris ANDI sont décrits dans [`outils.json`](./outils.json). Seuls les fichiers Markdown et JSON du dossier `outils/` sont versionnés ; les trois sous-dossiers sont recréés localement.

Pour reconstituer les trois sous-dossiers après un clone neuf, exécuter `make outils-telecharger` depuis la racine du dépôt, puis `make outils` pour vérifier les tailles et empreintes. La commande récupère les 27 paquets depuis les adresses du manifeste et génère les deux favoris ANDI depuis le code d’installation conservé dans ce même manifeste. Les quatre anciennes versions du dossier `archives/` ne sont pas restaurées : elles ne sont pas nécessaires à la préparation des postes. Un catalogue peut fournir une nouvelle version d’une extension ; si son empreinte diffère, la commande refuse le paquet. Il faut alors vérifier la nouvelle version et actualiser le manifeste avant de la retenir.

## Préparer les postes

Word, LibreOffice Writer, Firefox et Edge sont déjà installés sur les postes selon Alex. Les fichiers ci-dessous se trouvent dans `application-windows/`. Les quatre anciens fichiers conservés pour mémoire sont signalés dans la section « Vérification et limites ».

| Outil | Fichier local | Source officielle | Utilisation sans droits d’administration |
| --- | --- | --- | --- |
| NVDA 2026.2 | [nvda_2026.2.exe](./application-windows/nvda_2026.2.exe) | [NV Access](https://www.nvaccess.org/post/nvda-2026-2/) | Lancer l’exécutable et choisir « Créer une copie portable » dans un dossier utilisateur. |
| Focus Highlight 6.6, complément NVDA à tester | [focusHighlight-6.6.nvda-addon](./application-windows/focusHighlight-6.6.nvda-addon) | [Publication officielle](https://github.com/nvdajp/focusHighlight/releases/tag/6.6) | Dans NVDA, choisir « Installer depuis une source externe » dans le magasin des modules complémentaires, puis sélectionner ce fichier. L’installation et le fonctionnement sans droits d’administration restent à vérifier avec NVDA 2026.2. |
| Colour Contrast Analyser 3.5.5, Windows x64 | [CCA-Portable-x64-3.5.5.exe](./application-windows/CCA-Portable-x64-3.5.5.exe) | [Page officielle Vispero](https://vispero.com/lp/color-contrast-checker/) et [publication CCAe](https://github.com/ThePacielloGroup/CCAe/releases/tag/v3.5.5) | Lancer l’exécutable portable. |
| PAC 24.4.4.0 | [PAC_24.4.4.0.zip](./application-windows/PAC_24.4.4.0.zip) | [Téléchargement PAC](https://pac.pdf-accessibility.org/en/download) | Extraire l’archive dans un dossier utilisateur, puis lancer `PAC.exe`. Nécessite .NET Framework 4.8 ou supérieur. |

La version courante de PAC publiée par l’éditeur est 26.1.0.0, fournie sous forme d’installeur. L’archive 24.4.4.0 est la **dernière version portable officielle**, conformément au choix d’Alex. [Notes de publication PAC](https://pac.pdf-accessibility.org/en/resources/release-notes).

Pour CCA, [Vispero](https://vispero.com/lp/color-contrast-checker/) indique la version courante 3.5.5 et renvoie vers [CCAe](https://github.com/ThePacielloGroup/CCAe) pour Windows. Le dépôt [CCA-Win](https://github.com/ThePacielloGroup/CCA-Win) correspond à l’ancienne édition « Classic » et est archivé depuis 2018. L’exécutable portable 3.5.5 est déposé ci-dessus ; le fichier `CCA-Setup-3.5.4.msi` conservé de l’année précédente est un installeur plus ancien. La fiche [Microsoft Store « Analyseur de contraste de couleur »](https://apps.microsoft.com/detail/9p198gcw02l1?hl=fr-FR&gl=FR) concerne une autre application : ce n’est pas la source retenue pour CCA.

Le fichier Focus Highlight fourni par Alex est identique à celui de la publication officielle (SHA-256 : `73b93e77aa1b8fce4e7c9db516af24acd3a7af5dfd51c17442ddb6375e62c68a`). Son manifeste déclare une compatibilité testée jusqu’à **NVDA 2023.1**. La [documentation NVDA 2026.2](https://download.nvaccess.org/releases/2026.2/documentation/userGuide.html) explique qu’un module plus ancien peut être signalé comme incompatible et que son activation forcée peut causer des dysfonctionnements. Tester Focus Highlight sur un poste représentatif avant de le déployer dans les profils des stagiaires. NVDA 2026.2 dispose aussi d’un [surlignage visuel intégré](https://download.nvaccess.org/releases/2026.2/documentation/userGuide.html#Vision).

## Extensions Firefox : fichiers signés dans le dossier

Dans Firefox, ouvrir « Modules complémentaires et thèmes », puis « Installer un module depuis un fichier » et choisir le `.xpi` correspondant. Les fichiers de `extension-firefox/` proviennent directement du catalogue Mozilla ; chaque archive contient les métadonnées de signature Mozilla. L’installation dans le profil utilisateur dépend des règles appliquées au navigateur par la DSI.

| Extension | Version Firefox | Fichier local | Page Mozilla |
| --- | --- | --- | --- |
| HeadingsMap | 4.10.12 | [headingsmap-4.10.12.xpi](./extension-firefox/headingsmap-4.10.12.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/headingsmap/) |
| Web Developer | 3.0.1 | [web_developer-3.0.1.xpi](./extension-firefox/web_developer-3.0.1.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/web-developer/) |
| Stylus | 2.4.14 | [styl_us-2.4.14.xpi](./extension-firefox/styl_us-2.4.14.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/styl-us/) |
| WCAG Contrast Checker | 3.8.5 | [wcag_contrast_checker-3.8.5.xpi](./extension-firefox/wcag_contrast_checker-3.8.5.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/wcag-contrast-checker/) |
| WAVE Accessibility Extension | 3.3.1.0 | [wave_accessibility_tool-3.3.1.0.xpi](./extension-firefox/wave_accessibility_tool-3.3.1.0.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/wave-accessibility-tool/) |
| Assistant RGAA, Boscop | 2.1.2 | [assistant_rgaa-2.1.2.xpi](./extension-firefox/assistant_rgaa-2.1.2.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/assistant-rgaa/) |
| ARC Toolkit, TPGi | 5.7.11 | [arc_toolkit-5.7.11.xpi](./extension-firefox/arc_toolkit-5.7.11.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/arc-toolkit/) |
| Tanaguru webext | 5.1.1 | [tanaguru_webext-5.1.1.xpi](./extension-firefox/tanaguru_webext-5.1.1.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/tanaguru-webext/) |
| axe DevTools, Deque | 4.117.1 | [axe_devtools-4.117.1.xpi](./extension-firefox/axe_devtools-4.117.1.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/axe-devtools/) |
| RGAA Checker, Arneo | 0.28.0 | [rgaa_checker-0.28.0.xpi](./extension-firefox/rgaa_checker-0.28.0.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/rgaa-checker/) |
| RGAA Checker Companion, rgaa-checker.com | 0.2.5 | [rgaa_checker_companion-0.2.5.xpi](./extension-firefox/rgaa_checker_companion-0.2.5.xpi) | [Catalogue](https://addons.mozilla.org/firefox/addon/rgaa-checker-companion/) |

Tanaguru 5.1.1 est la dernière version **publiée pour Firefox**, bien qu’elle soit plus ancienne que la version Chromium 6.0.1. [axe DevTools sur Firefox possède moins de fonctions](https://docs.deque.com/devtools-for-web/4/en/devtools-extension/) que son édition Edge. Silktide ne publie pas d’extension Firefox : son éditeur annonce [Chrome et Edge](https://silktide.com/toolbar/).

## Extensions Edge : fichiers CRX et catalogues

Les 12 fichiers `.crx` du sous-dossier `extension-edge/` ont été téléchargés depuis les services de distribution des catalogues officiels. Pour une installation ordinaire sans droits d’administration, ouvrir le lien du catalogue dans Edge et choisir « Obtenir » ou « Ajouter ». Pour les extensions du Chrome Web Store, Edge peut demander d’autoriser les extensions d’un autre magasin ; [Microsoft décrit cette procédure](https://support.microsoft.com/fr-fr/edge/add-turn-off-or-remove-extensions-in-microsoft-edge). Les fichiers CRX servent à préparer une installation locale ou par la DSI, sous réserve des politiques Edge du poste. Leur installation directe sans droits d’administration n’a pas été vérifiée sur Windows. Les fichiers `.xpi` Firefox ne s’installent pas dans Edge.

| Fonction | Extension et version | Fichier CRX local | Catalogue |
| --- | --- | --- | --- |
| Plan des titres | HeadingsMap 4.10.12 | [headingsmap-4.10.12.crx](./extension-edge/headingsmap-4.10.12.crx) | [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/headingsmap/bokekiiaddinealohkmhjcgfanndmcgo) |
| Contrôles Web rapides | Web Developer 3.0.1 | [web-developer-3.0.1.crx](./extension-edge/web-developer-3.0.1.crx) | [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/web-developer/ilbdhapjffldgngebmnkdodohjapjccm) |
| Styles de page | Stylus 2.4.14 | [stylus-2.4.14.crx](./extension-edge/stylus-2.4.14.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/stylus/clngdbkpkpeebahjckkjfobafhncgmne) |
| Contraste dans la page | WCAG Color Contrast Check 3.8.5 | [wcag-color-contrast-check-3.8.5.crx](./extension-edge/wcag-color-contrast-check-3.8.5.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/wcag-color-contrast-check/plnahcmalebffmaghcpcmpaciebdhgdf) |
| Évaluation visuelle | WAVE Evaluation Tool 3.3.1.0 | [wave-evaluation-tool-3.3.1.0.crx](./extension-edge/wave-evaluation-tool-3.3.1.0.crx) | [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/wave-evaluation-tool/khapceneeednkiopkkbgkibbdoajpkoj) |
| Aide au RGAA | Assistant RGAA 2.1.2 | [assistant-rgaa-2.1.2.crx](./extension-edge/assistant-rgaa-2.1.2.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/assistant-rgaa/cgpmofepeeiaaljkcclfldhaalfpcand) |
| Contrôles WCAG | ARC Toolkit 5.7.11 | [arc-toolkit-5.7.11.crx](./extension-edge/arc-toolkit-5.7.11.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/arc-toolkit/chdkkkccnlfncngelccgbgfmjebmkmce) |
| Contrôles RGAA partiels | Tanaguru webext 6.0.1 | [tanaguru-webext-6.0.1.crx](./extension-edge/tanaguru-webext-6.0.1.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/tanaguru-webext/hhopdkekcmkdfpdjbpajmmfbheglcaac) |
| Contrôles automatisés | axe DevTools 4.138.0 | [axe-devtools-4.138.0.crx](./extension-edge/axe-devtools-4.138.0.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd) |
| Contrôles complémentaires | Silktide Accessibility Checker 3.0.9 | [silktide-accessibility-checker-3.0.9.crx](./extension-edge/silktide-accessibility-checker-3.0.9.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/silktide-accessibility-ch/mpobacholfblmnpnfbiomjkecoojakah) |
| RGAA Checker d’Arneo | RGAA Checker Arneo 0.28.0 | [rgaa-checker-arneo-0.28.0.crx](./extension-edge/rgaa-checker-arneo-0.28.0.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/rgaa-checker/eenibcgdpolkdophaaiikdcofgkjlllm) |
| RGAA Checker Companion | RGAA Checker Companion 0.2.5 | [rgaa-checker-companion-0.2.5.crx](./extension-edge/rgaa-checker-companion-0.2.5.crx) | [Chrome Web Store](https://chromewebstore.google.com/detail/rgaa-checker-companion/ignlacbeeoohadiojeajmnnghbpokllj) |

Les deux RGAA Checker ont des éditeurs et des interfaces distincts. Ils sont tous deux inclus à la demande d’Alex. Pour éviter la confusion pendant une démonstration, vérifier le nom complet affiché dans Edge ou Firefox avant de lancer un contrôle.

Pour Silktide, voir aussi le [site officiel de l’éditeur](https://silktide.com/) et sa [page consacrée à l’extension gratuite](https://silktide.com/toolbar/). Le site présente également la plateforme Silktide ; l’outil à ajouter dans Edge pour la formation est l’extension « Silktide Accessibility Checker » liée dans le tableau.

## Outils déjà intégrés

- **Lighthouse** : dans Edge, ouvrir les outils de développement avec `F12`, puis l’onglet « Lighthouse ». [Documentation Microsoft](https://learn.microsoft.com/en-us/microsoft-edge/devtools/lighthouse/lighthouse-tool). Aucun installeur supplémentaire n’est nécessaire pour Edge.
- **Web Developer Tools** : les outils de développement d’Edge et de Firefox s’ouvrent avec `F12`. Ils sont distincts de l’extension « Web Developer » listée plus haut.
- **Narrateur Windows** : lecteur d’écran de secours déjà intégré à Windows. Dans les notes de présentation, son raccourci est `Win + Ctrl + Entrée`.
- **Vérificateurs d’accessibilité de Word et Writer** : fonctions des logiciels déjà installés sur les postes.

## Outils accessibles en ligne

- [ANDI, outil officiel de la Social Security Administration](https://www.ssa.gov/accessibility/andi/) : cité dans l’aide à la correction du site d’exercice pour vérifier les noms accessibles des champs. Importer le fichier [favori ANDI pour Edge](./extension-edge/ANDI-favori-a-importer.html) ou [favori ANDI pour Firefox](./extension-firefox/ANDI-favori-a-importer.html). Dans Edge : Paramètres > Profils > Importer les données de navigateur > Fichier HTML de favoris ([aide Microsoft](https://support.microsoft.com/en-us/edge/import-your-favorites-and-passwords-in-microsoft-edge)). Dans Firefox : Marque-pages > Gérer les marque-pages > Importation et sauvegarde > Importer des marque-pages au format HTML ([aide Mozilla](https://support.mozilla.org/fr/kb/importer-marque-pages-fichier-html)). Le favori reprend le code fourni par [l’éditeur sur GitHub](https://github.com/SSAgov/ANDI/blob/master/andi/help/install.html) et charge ANDI depuis `ssa.gov` à chaque utilisation : un accès réseau est nécessaire. Il n’existe pas de paquet XPI ou CRX pour cet outil ; la politique du navigateur ou du site testé peut empêcher son lancement.
- [axesCheck](https://check.axes4.com/en) : alternative en ligne de l’éditeur de PAC pour les vérifications automatisables des PDF selon PDF/UA et WCAG. Limite affichée : 10 Mo. Le PDF est transmis à axes4 ; utiliser le service seulement si le transfert du document est autorisé. PAC portable permet un contrôle local sans téléversement.
- [WAVE en ligne](https://wave.webaim.org/) : contrôle d’une page publique par adresse. L’[extension WAVE](https://wave.webaim.org/extension/) travaille localement dans le navigateur et convient également aux pages privées ou dynamiques.
- Mesure des contrastes : [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/), [Contrast Finder](https://app.contrast-finder.org/) et [Vispero](https://vispero.com/lp/color-contrast-checker/).
- [InstaFont](https://instafonts.io/) : démonstration des faux caractères gras dans les publications de réseaux sociaux.

## Autres outils et ressources nommés dans la formation

| Noms relevés | Statut pour les postes Windows |
| --- | --- |
| JAWS, Adobe Acrobat Pro | Logiciels sous licence évoqués comme exemples ou solutions de repli ; aucun installeur libre à joindre. |
| VoiceOver, TalkBack | Lecteurs d’écran Apple et Android ; pas d’installeur Windows. |
| Chrome, PowerPoint | Nommés dans les supports ou liens ; aucun installeur demandé pour les exercices sur les postes équipés d’Edge, Firefox, Word et Writer. |
| Figma, Obligally, Mentor, LinkedIn, X, Opquast | Plateformes ou ressources à ouvrir dans un navigateur. |
| W3C, RGAA, WebAIM Million, AAArdvark | Références et ressources pédagogiques en ligne. |

## Vérification et limites

Les fichiers `application-windows/archives/nvda_2024.4.1.exe`, `application-windows/archives/CCA-Setup-3.5.4.msi`, `application-windows/archives/PAC_24.3.1.0.zip` et `application-windows/archives/focusHighlight-6.6.nvda-addon.zip` sont conservés comme archives de la session précédente. La copie de Focus Highlight sans suffixe `.zip`, à côté de NVDA, est celle à sélectionner pour l’essai ; les trois autres archives ne servent pas à préparer les postes.

Les tailles et empreintes des 26 paquets courants, de Focus Highlight et des deux favoris ANDI figurent dans [`outils.json`](./outils.json). `make outils` vérifie ces 29 fichiers après reconstitution. Les empreintes de NVDA et CCA correspondent à celles publiées par leurs éditeurs ; celles des XPI correspondent aux métadonnées du catalogue Mozilla. Les empreintes des CRX ont été calculées à partir des paquets récupérés par les services officiels des catalogues. PAC ne publie pas d’empreinte de référence sur sa page de téléchargement : son SHA-256 dans le manifeste a été calculé après récupération depuis l’adresse officielle. Les archives ZIP, XPI et CRX ont passé leur contrôle d’intégrité ; les exécutables portent l’en-tête Windows attendu. Pour les 12 CRX, la version, l’identifiant d’extension et la signature cryptographique du paquet ont également été vérifiés. Ces contrôles ont été effectués sur macOS. **Le démarrage effectif sans droits d’administration, les politiques d’extensions et la présence de .NET 4.8 restent à vérifier sur un poste Windows représentatif.**

## Journal des décisions « cuisine-moi »

### Q1 - Catalogues des navigateurs

- Capture : Edge est prioritaire ; Alex souhaite installer les mêmes fonctions sous Firefox lorsque cela est possible. Les deux navigateurs sont déjà présents sur les postes. Les extensions Edge peuvent être installées depuis les catalogues si la politique DSI les autorise ; leurs paquets CRX sont aussi conservés localement.

### Q2 - PAC

- Capture : Alex choisit la dernière version portable officielle, soit PAC 24.4.4.0. La version 26.1.0.0 exige un programme d’installation et n’est pas retenue dans le dossier courant.

### Q3 - Logiciels de base

- Capture : Word, LibreOffice Writer, Firefox et Edge sont déjà installés ; Alex demande de ne pas fournir leurs installeurs.

### Q4 - Extensions supplémentaires

- Capture : Alex ajoute explicitement HeadingsMap, Web Developer Tools, WCAG Contrast Checker, Silktide, WAVE, Assistant RGAA, ARC Toolkit, Tanaguru, axe DevTools, Lighthouse et RGAA Checker. Chaque nom est inventorié dans ce guide selon sa forme disponible.

### Q5 - RGAA Checker

- Capture : Alex ne connaît pas les éditeurs et demande de mettre les deux extensions distinctes, celle d’Arneo et RGAA Checker Companion de rgaa-checker.com.

### Q6 - Site officiel de Silktide

- Capture : Alex rappelle explicitement l’adresse https://silktide.com/. Le site officiel, la page de l’extension gratuite, le lien d’installation Edge et le paquet CRX sont ajoutés au guide.

### Q7 - Source du CCA Windows

- Capture : Alex cite le dépôt `thepaciellogroup/cca-win` et demande un exécutable CCA Windows. Le dépôt est archivé depuis 2018 et oriente vers son successeur `CCAe` ; le fichier courant est déjà `CCA-Portable-x64-3.5.5.exe`, issu de la publication officielle CCAe et vérifié par SHA-256.

### Q8 - Page officielle du CCA

- Capture : après avoir proposé une fiche Microsoft Store, Alex confirme que l’outil demandé est celui de Vispero à l’adresse `https://vispero.com/lp/color-contrast-checker/`. Cette page est ajoutée comme source officielle ; elle renvoie vers CCAe pour Windows. Le fichier portable 3.5.5 déjà récupéré correspond à ce produit.

### Q9 - Classement et paquets Edge

- Capture : Alex demande un rangement physique par type, avec trois sous-dossiers et un guide, puis précise vouloir télécharger les versions Edge. Les 12 CRX disponibles depuis les catalogues officiels sont déposés dans `extension-edge/`.

### Q10 - Relecture du site d’exercice

- Capture : la vérification de complétude révèle ANDI dans l’aide à la correction du site. Son mode de distribution officiel est le favori de navigateur ; le guide donne son lien d’installation pour Edge et Firefox.

### Q11 - Favori ANDI dans le pack

- Capture : Alex demande d’ajouter ANDI au dossier. Deux fichiers HTML de favoris, issus du code d’installation officiel, sont placés dans les dossiers Edge et Firefox ; leur SHA-256 commun est `47c5400ef7e73d66b6d3e11c73db8d82fea6e7468c5a99134aeacd859061fa04`.

### Q12 - Focus Highlight avec NVDA

- Capture : Alex demande de remettre le fichier `focusHighlight-6.6.nvda-addon.zip` du Bureau avec NVDA. Son contenu correspond à la publication officielle ; une copie nommée `focusHighlight-6.6.nvda-addon` est placée à côté de NVDA. Son fonctionnement avec NVDA 2026.2 reste à tester, car son manifeste indique NVDA 2023.1 comme dernière version testée.

### Points à vérifier sur les postes

- Droits d’exécution des programmes dans un dossier utilisateur et possibilité d’installer les extensions dans les profils Edge et Firefox, notamment à partir des CRX locaux si cette voie est nécessaire.
- Présence de .NET Framework 4.8 ou supérieur pour PAC.
- Essai de Focus Highlight 6.6 avec NVDA 2026.2 avant toute installation dans les profils des stagiaires.
- Vérification pratique des extensions Firefox anciennes ou limitées, notamment Tanaguru et axe DevTools.
