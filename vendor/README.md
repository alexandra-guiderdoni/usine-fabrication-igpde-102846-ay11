# Outils embarqués

Copies figées d'outils externes, pour que l'usine fonctionne sans l'espace de travail d'origine.

## Contenu

- `accessible-pdf/` : générateur Markdown vers PDF accessible (PDF/UA-1), avec ses gabarits CSS. Utilisé pour les mémos bureautique, les fiches WCAG et la fiche des liens des TP.
- `a11y-shared-references/` : module d'audit éditorial (acronymes, liens génériques, paragraphes vides) chargé par le générateur s'il est présent.

La disposition reproduit celle des skills d'origine : le script retrouve ses gabarits et le module partagé par chemins relatifs, sans modification.

## Provenance

Copiés le 2026-09-27 depuis les skills `accessible-pdf` et `a11y-shared-references` de l'espace de travail d'Alexandra Guiderdoni. Empreintes SHA-256 (12 premiers caractères) :

- `a11y-shared-references/scripts/a11y_editorial.py` : `eeda69f38455`
- `accessible-pdf/scripts/md2pdf.py` : `6862216a11e2`
- `accessible-pdf/templates/formation.css` : `61792402baee`

Pour resynchroniser : recopier les fichiers depuis la source, puis mettre à jour ces empreintes dans le même commit.

## Prérequis

Pandoc (`brew install pandoc`), WeasyPrint et pikepdf (voir `requirements.txt`), Pango et GLib (`brew install pango glib`). Vérification : `python3 vendor/accessible-pdf/scripts/md2pdf.py --check`.

L'option `--via-docx` du générateur n'est pas embarquée : elle dépend d'un autre skill, et l'usine ne l'utilise pas.
