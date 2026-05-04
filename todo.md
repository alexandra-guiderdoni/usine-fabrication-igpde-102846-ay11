# TODO - Formation 102638 (IGPDE / Carinne C.)

## En cours

- [ ] **Fabriquer le site d'entraînement avec pièges clavier** - support de l'exercice final (slide 16 `16_mission-clavier.py`). La slide y renvoie sans le nommer (« le site d'entraînement qui vous sera fourni »). Pièges à prévoir pour couvrir les 3 signaux vus en slide 15 :
  - Focus qui disparaît (contour absent sur certains éléments)
  - Ordre de tabulation illogique (saut droite → gauche)
  - État non annoncé (case à cocher sans annonce)
  - Bonus : bouton activable à la souris mais pas au clavier, lien vide, focus invisible

- [ ] **Distribuer la grille d'audit aux stagiaires pour la mission finale** (slide 27) :
  - Fichier source : `03-easy-checks/grille-audit-easy-checks.xlsx` (16 onglets)
  - Structure : 12 onglets pré-remplis, un par page obligatoire de l'échantillon RGAA (Accueil, Mentions légales, Déclaration a11y, Plan du site, Contact, Aide, Authentification, Recherche, Document, Article, Formulaire, Liste)
  - Chaque stagiaire saisit les URL et remplit les verdicts C/NC/NA sur chaque onglet
  - L'onglet Synthèse agrège automatiquement les 12 pages et calcule le taux global
  - 20 min audit individuel + 5 min binôme + 5 min restitution
  - Livrable stagiaire : classeur rempli + 3 actions priorisées + 1 engagement personnel

## Fait

- [x] Slides 01-27 assemblées dans `formation-102638-juin-2026.pptx` (27 slides couvrant les 13 points de contrôle rapides W3C)
- [x] Grille d'audit MD documentaire (`03-easy-checks/grille-audit-easy-checks.md`)
- [x] **Grille d'audit XLSX validée** (`03-easy-checks/grille-audit-easy-checks.xlsx`) - 16 onglets, 12 pages pré-remplies, avertissement sensibilisation, mention PAC pour documents, renommage « Taux de conformité points de contrôle rapides », évaluée 8/10 (adéquation points de contrôle rapides 9, initiation 8, pédagogie 7,5). Validée par Alex le 2026-04-17.
- [x] Rattrapage typographique : remplacement des tirets cadratins par tirets simples dans tous les scripts Python (29 fichiers touchés + règle documentée dans CLAUDE.md)
