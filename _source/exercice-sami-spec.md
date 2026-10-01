# Exercice Sami — contrat de génération

La source normative de l’exercice est
[`_source/exercice-sami-matrice.yml`](exercice-sami-matrice.yml). Elle fixe les
identifiants, les libellés, les niveaux, l’ordre, les procédures, les preuves et
les surfaces pédagogiques. Ce fichier sert de point d’entrée ; il ne duplique
pas cette liste.

## Finalité

L’exercice permet de manipuler les principales fonctions de mise en
accessibilité d’un document Word, puis d’en vérifier le résultat avant
publication. Les participants peuvent partir du fichier inaccessible ou du
fichier avec pistes et comparer leur production au guide corrigé.

## Trois variantes synchronisées

- `tp-doc-inaccessible.docx` porte les défauts praticables déclarés dans la
  matrice, sans commentaire d’aide.
- `tp-doc-aide-correction.docx` conserve le même corps et les mêmes défauts,
  puis ajoute une piste à chaque occurrence prévue.
- `tp-doc-accessible.docx` applique les corrections et devient le guide
  pratique autonome remis à la fin du TP.

Le corps éditorial, les informations et l’ordre restent identiques. Une
différence textuelle entre la source et le corrigé n’est admise que si sa
transformation est déclarée dans la matrice.

## Chaîne de production

Le générateur unique est `scripts/generate_exercice_sami.py`. La commande
`make sami` régénère les trois variantes et leurs ressources. Les DOCX générés
ne sont jamais modifiés manuellement.

Les tests inspectent notamment la structure OOXML, les commentaires, les
styles, les listes, les tableaux, les images, les liens, les langues, la
typographie et les propriétés. Les contrôles dépendant de Word, Writer, PAC ou
Acrobat restent complétés par une recette humaine.

## Historique

L’ancien contrat détaillé a été retiré lorsque la matrice a pris en charge
toutes les sorties. Son contenu reste consultable dans l’historique Git.
