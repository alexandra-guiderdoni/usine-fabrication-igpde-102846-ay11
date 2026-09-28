# Recette du site d'exercice

Ce dossier regroupe les moyens de vérifier visuellement le site d'exercice avant sa publication. Il ne produit aucun livrable stagiaire.

## Prévisualiser le site

Depuis la racine de l'usine, lancez :

```bash
make apercu
```

La commande sert `docs/` en local et affiche les adresses des versions inaccessible, d'aide à la correction et accessible. Arrêtez le serveur avec `Ctrl+C`.

## Installer la recette autonome

Depuis la racine de l'usine, lancez une fois :

```bash
make installer-recette
```

La cible demande `git`, Node.js 24 ou plus et npm. Elle clone le tag ShipGuard `v2.14.0` dans `.tools/shipguard/`, après vérification de son commit, installe `agent-browser` 0.38.1 dans `recette/node_modules/` et télécharge Chrome for Testing sous `.tools/` après vérification de son empreinte SHA-256. Ces trois répertoires sont ignorés par Git : la recette ne lit ni plugin Codex ni cache global. Le navigateur verrouillé couvre macOS Apple Silicon et Intel. Pour changer de version, modifier le bootstrap, son empreinte et le verrou npm ensemble, puis vérifier toute la recette.

## Lancer la recette visuelle

Depuis la racine de l'usine, lancez :

```bash
make recette
```

La recette cible par défaut `docs/site-accessible/`. Elle démarre un serveur local, exécute les manifestes ShipGuard, produit des captures et ouvre un tableau de revue local. Après l'installation locale, elle nécessite seulement `node`, `python3` et `curl` accessibles dans le terminal.

Les manifestes sont dans `visual-tests/pages/`. Les captures, journaux et le tableau généré se trouvent dans `visual-tests/_results/`. La commande reste active pour servir le tableau ; arrêtez-la avec `Ctrl+C`.

## Rapports

`rapports/` conserve les audits et comptes rendus historiques. Ils documentent des constats passés et ne remplacent pas une nouvelle recette après une modification du site.

## Place dans la chaîne

La recette visuelle complète `make verifier` : elle ne remplace ni la validation automatisée ni la relecture humaine. Après une modification du site, exécutez `make verifier`, puis `make recette` avant `make publier-site`.
