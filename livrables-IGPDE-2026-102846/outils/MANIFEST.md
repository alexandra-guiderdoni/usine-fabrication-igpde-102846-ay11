# Manifeste des outils - formation 102846

Installeurs déposés dans le dossier partagé de la formation, puis installés sur chaque poste, formateur et stagiaires, avant la session. Ils ne sont pas versionnés : trop volumineux, et redistribuables depuis leurs sources officielles. La liste de référence, avec empreintes, est `outils.json`.

## Récupérer et vérifier

```bash
make outils-telecharger  # récupère les trois fichiers avec adresse directe
make outils              # vérifie les quatre fichiers, PAC compris
```

PAC doit être téléchargé manuellement depuis sa page officielle et déposé dans
ce dossier. La vérification contrôle ensuite la taille et l'empreinte SHA-256 de
chaque fichier ; une empreinte différente est refusée.

## Liste

- **NVDA 2024.4.1** (`nvda_2024.4.1.exe`, 38 Mo) : lecteur d'écran pour Windows, téléchargement direct depuis nvaccess.org.
- **Colour Contrast Analyser 3.5.4** (`CCA-Setup-3.5.4.msi`, 87 Mo) : contrôle des contrastes pour Windows, téléchargement direct depuis GitHub (TPGi).
- **Focus Highlight 6.6** (`focusHighlight-6.6.nvda-addon.zip`, 163 Ko) : extension NVDA qui rend le focus visible, téléchargement direct depuis GitHub.
- **PAC 24.3.1.0** (`PAC_24.3.1.0.zip`, 74 Mo) : PDF Accessibility Checker. Pas d'adresse directe : télécharger depuis https://pac.pdf-accessibility.org/en/download, déposer le fichier dans ce dossier, puis relancer `make outils` pour vérifier son empreinte.
