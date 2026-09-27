# Manifeste des outils - formation 102846

Installeurs remis aux stagiaires sur clé USB le jour de la formation. Ils ne sont pas versionnés : trop volumineux, et redistribuables depuis leurs sources officielles. La liste de référence, avec empreintes, est `outils.json`.

## Récupérer et vérifier

```bash
make outils
```

Le script télécharge les installeurs qui ont une adresse directe, puis vérifie la taille et l'empreinte SHA-256 de chacun. Un fichier dont l'empreinte diffère est refusé.

## Liste

- **NVDA 2024.4.1** (`nvda_2024.4.1.exe`, 38 Mo) : lecteur d'écran pour Windows, téléchargement direct depuis nvaccess.org.
- **Colour Contrast Analyser 3.5.4** (`CCA-Setup-3.5.4.msi`, 87 Mo) : contrôle des contrastes pour Windows, téléchargement direct depuis GitHub (TPGi).
- **Focus Highlight 6.6** (`focusHighlight-6.6.nvda-addon.zip`, 163 Ko) : extension NVDA qui rend le focus visible, téléchargement direct depuis GitHub.
- **PAC 24.3.1.0** (`PAC_24.3.1.0.zip`, 74 Mo) : PDF Accessibility Checker. Pas d'adresse directe : télécharger depuis https://pac.pdf-accessibility.org/en/download, déposer le fichier dans ce dossier, puis relancer `make outils` pour vérifier son empreinte.
