"""Génère la grille d'audit d'accessibilité - 13 points de contrôle rapides du W3C.

Sortie : 03-easy-checks/grille-audit-easy-checks.xlsx

Classeur à 17 onglets :
- Mode d'emploi : conventions, verdicts, sévérité, outils
- Exercice - 13 pages : correspondance slides, site d'exercice et lignes de grille
- Échantillon RGAA : rappel des pages obligatoires et représentatives
- 12 grilles de page : 13 critères à auditer avec validation de données
- Exemple : audit fictif sur une page type service public
- Synthèse : décompte automatique et taux de conformité

Typographie française irréprochable (accents, apostrophes, guillemets).
Taille de police minimale : 14 pt (14 cellules, 16 sections, 20 titre).

Usage :
    python3 scripts/generate_grille_audit.py
"""

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.page import PageMargins

from config import load_formation_config


FORMATION = load_formation_config()

# ---------------------------------------------------------------------------
# Palette DSFR
# ---------------------------------------------------------------------------

BLEU_FRANCE = "000091"
BLEU_CLAIR = "E3E3FD"
ROUGE_MARIANNE = "E1000F"
GRIS_CLAIR = "F6F6F6"
GRIS_MOYEN = "E5E5E5"
VERT_SUCCES = "18753C"
ORANGE_WARN = "B34000"
BLANC = "FFFFFF"

# Couleurs verdicts
VERDICT_COLORS = {
    "C": "C8E6C9",  # vert clair
    "NC": "FFCDD2",  # rouge clair
    "NA": "E0E0E0",  # gris
}

SEVERITE_COLORS = {
    "Bloquant": "FFCDD2",
    "Gênant": "FFE0B2",
    "Mineur": "FFF9C4",
    "Info": "E1F5FE",
}

# ---------------------------------------------------------------------------
# Tailles de police (minimum 14 pt)
# ---------------------------------------------------------------------------

SIZE_TITLE = 20
SIZE_SECTION = 16
SIZE_HEADER = 14
SIZE_CELL = 14

# ---------------------------------------------------------------------------
# Données des 13 points de contrôle rapides
# ---------------------------------------------------------------------------

CHECKS = [
    {
        "id": 1,
        "titre": "Texte alternatif des images",
        "wcag": "1.1.1",
        "rgaa": "1.1, 1.2, 1.3, 1.6, 1.7, 1.8, 1.9",
        "methode": "Bookmarklet « Check images », ou clic droit Inspecter sur chaque image.",
        "verifier": "Alt présent. Alt vide pour les décoratives. Alt explicite (action attendue) pour les images-liens. Description longue pour les graphiques et schémas complexes.",
    },
    {
        "id": 2,
        "titre": "Titre de page",
        "wcag": "2.4.2",
        "rgaa": "8.5, 8.6",
        "methode": "Survoler l'onglet du navigateur, lire la balise <title>.",
        "verifier": "Titre présent, unique par page, information prioritaire placée en premier (front-loading).",
    },
    {
        "id": 3,
        "titre": "Titres et hiérarchie",
        "wcag": "1.3.1, 2.4.6",
        "rgaa": "9.1",
        "methode": "Extension HeadingsMap ou bookmarklet « Check headings ».",
        "verifier": "Un seul <h1> par page. Niveaux emboîtés sans saut (H1 vers H2 vers H3). Titres balisés <h1> à <h6>, pas seulement stylés en CSS.",
    },
    {
        "id": 4,
        "titre": "Contraste des couleurs",
        "wcag": "1.4.3, 1.4.11",
        "rgaa": "3.2, 3.3",
        "methode": "Pipette DevTools, WebAIM Contrast Checker, Colour Contrast Analyser (CCA).",
        "verifier": "Texte normal : ratio >= 4,5:1. Texte large (18 pt ou 14 pt gras) : ratio >= 3:1. Composants graphiques porteurs d'information : >= 3:1.",
    },
    {
        "id": 5,
        "titre": "Lien d'évitement",
        "wcag": "2.4.1",
        "rgaa": "12.7",
        "methode": "Charger la page, appuyer une fois sur Tab.",
        "verifier": "1er élément focus = lien « Aller au contenu ». Visible au focus même s'il est masqué par défaut. Ancre valide (#contenu, #main).",
    },
    {
        "id": 6,
        "titre": "Focus et navigation clavier",
        "wcag": "2.4.7, 2.1.1, 2.1.2, 2.4.3",
        "rgaa": "10.7, 12.13, 12.14, 10.3",
        "methode": "Cacher la souris. Parcours complet au clavier uniquement (Tab, Maj+Tab, Entrée, Espace, flèches).",
        "verifier": "Focus visible sur tous les éléments interactifs. Ordre de tabulation logique. Pas de piège clavier. État (coché, développé, sélectionné) annoncé.",
    },
    {
        "id": 7,
        "titre": "Langue de la page",
        "wcag": "3.1.1, 3.1.2",
        "rgaa": "8.3, 8.4",
        "methode": 'Clic droit « Afficher le code source », chercher <html lang="…">.',
        "verifier": 'Attribut lang présent avec code ISO 639 (fr, en, de…). Passages dans une autre langue balisés <span lang="…">.',
    },
    {
        "id": 8,
        "titre": "Zoom à 200 %",
        "wcag": "1.4.4, 1.4.10",
        "rgaa": "10.4, 10.11",
        "methode": "Ctrl + (Cmd + sur Mac) jusqu'à 200 %, parcourir la page complète.",
        "verifier": "Aucun texte coupé ni superposé. Pas de défilement horizontal forcé. Menus, boutons et formulaires restent utilisables.",
    },
    {
        "id": 9,
        "titre": "Sous-titres vidéo",
        "wcag": "1.2.2",
        "rgaa": "4.3, 4.4",
        "methode": "Lancer la vidéo, couper le son, activer les sous-titres (bouton CC).",
        "verifier": "Sous-titres synchronisés présents. Paroles + informations sonores importantes ((rires), (sonnerie)). Qualité éditoriale (pas auto-générés non relus).",
    },
    {
        "id": 10,
        "titre": "Transcriptions audio et vidéo",
        "wcag": "1.2.1",
        "rgaa": "4.1, 4.2",
        "methode": "Chercher un lien « Transcription » ou « Lire le texte » visible près du média.",
        "verifier": "Transcription accessible à un clic. Complète (paroles + bruits utiles). Navigable (titres, paragraphes).",
    },
    {
        "id": 11,
        "titre": "Audiodescription",
        "wcag": "1.2.3, 1.2.5",
        "rgaa": "4.5, 4.6",
        "methode": "Vérifier la présence d'une piste audiodécrite (bouton AD).",
        "verifier": "AD disponible pour les vidéos informatives à contenu visuel essentiel. Intercalée dans les silences, sans couvrir les dialogues.",
    },
    {
        "id": 12,
        "titre": "Étiquettes de formulaire",
        "wcag": "3.3.2, 1.3.1, 2.5.3",
        "rgaa": "11.1, 11.2, 11.3",
        "methode": "Cliquer sur le libellé (le focus doit sauter dans le champ). Tester au lecteur d'écran.",
        "verifier": 'Étiquette visible et persistante. Association <label for="…"> ou aria-labelledby. Placeholder = exemple, jamais étiquette unique. Fieldset/legend pour les groupes (radios, cases).',
    },
    {
        "id": 13,
        "titre": "Champs obligatoires et erreurs",
        "wcag": "3.3.2, 3.3.1, 3.3.3",
        "rgaa": "11.10, 11.11",
        "methode": "Observer l'état initial, puis soumettre un formulaire incomplet. Vérifier au clavier et au lecteur d'écran.",
        "verifier": "Avant envoi : obligatoires indiqués textuellement, astérisque expliqué si utilisé, required ou aria-required présent. Après envoi : pas d'erreur prématurée, message précis relié au champ avec aria-describedby, aria-invalid si erreur, focus guidé vers le récapitulatif ou le premier champ en erreur.",
    },
]

EXERCICE_PAGES = [
    {
        "id": "ec01-images",
        "title": "Actualité illustrée",
        "slides": "53-55",
        "recommended_sheet": "10. Article",
        "minimal_task": "Qualifier le rôle de chaque image puis vérifier si l'alternative transmet l'information ou l'action utile.",
    },
    {
        "id": "ec02-page-title",
        "title": "Résultats de recherche RGAA",
        "slides": "56",
        "recommended_sheet": "8. Recherche",
        "minimal_task": "Vérifier que le titre de page identifie la requête, la pagination et le site dans un ordre utile.",
    },
    {
        "id": "ec03-headings",
        "title": "Guide du RGAA",
        "slides": "57-58",
        "recommended_sheet": "10. Article",
        "minimal_task": "Comparer le plan visuel et le plan technique des titres.",
    },
    {
        "id": "ec04-contrast",
        "title": "Charte de publication",
        "slides": "59-60",
        "recommended_sheet": "10. Article",
        "minimal_task": "Mesurer le contraste d'un texte, d'un lien, d'un bouton ou d'un statut.",
    },
    {
        "id": "ec05-skiplinks",
        "title": "Accès rapide aux contenus",
        "slides": "61",
        "recommended_sheet": "1. Accueil",
        "minimal_task": "Appuyer sur Tab au chargement et vérifier la présence, la visibilité et la cible du lien d'évitement.",
    },
    {
        "id": "ec06-keyboard-focus",
        "title": "Parcours clavier",
        "slides": "62-65",
        "recommended_sheet": "11. Formulaire",
        "minimal_task": "Parcourir la page au clavier : focus visible, ordre logique, activation clavier, absence de piège.",
    },
    {
        "id": "ec07-language",
        "title": "Atelier international",
        "slides": "66",
        "recommended_sheet": "10. Article",
        "minimal_task": "Vérifier la langue principale et les changements de langue ou de sens de lecture.",
    },
    {
        "id": "ec08-zoom",
        "title": "Ressources à zoomer",
        "slides": "67",
        "recommended_sheet": "12. Liste",
        "minimal_task": "Zoomer à 200 % et vérifier qu'aucun contenu utile n'est coupé, masqué ou inutilisable.",
    },
    {
        "id": "ec09-captions",
        "title": "Vidéo de sensibilisation",
        "slides": "68-69",
        "recommended_sheet": "10. Article",
        "minimal_task": "Couper le son et vérifier la présence de sous-titres synchronisés et relus.",
    },
    {
        "id": "ec10-transcript",
        "title": "Écouter un podcast",
        "slides": "70",
        "recommended_sheet": "10. Article",
        "minimal_task": "Vérifier qu'une transcription proche du lecteur permet de comprendre le contenu sans écouter l'audio.",
    },
    {
        "id": "ec11-audio-description",
        "title": "Démonstration vidéo",
        "slides": "71",
        "recommended_sheet": "10. Article",
        "minimal_task": "Commencer par la version audiodécrite et vérifier quelles informations visuelles deviennent disponibles sans voir l'image.",
    },
    {
        "id": "ec12-form-labels",
        "title": "Inscription à un webinaire",
        "slides": "72-74",
        "recommended_sheet": "11. Formulaire",
        "minimal_task": "Vérifier l'étiquette visible, son association au champ et les légendes des groupes.",
    },
    {
        "id": "ec13-required-errors",
        "title": "Formulaire de contact",
        "slides": "75",
        "recommended_sheet": "5. Contact",
        "minimal_task": "Soumettre le formulaire et vérifier l'annonce des champs obligatoires et des erreurs.",
    },
]

# Exemple : (verdict, sévérité, constat, correctif, preuve)
# ---------------------------------------------------------------------------
# Échantillon RGAA 4.1.2 - pages obligatoires et représentatives
# Source : méthode technique RGAA 4.1.2, DINUM
# https://accessibilite.numerique.gouv.fr/
# ---------------------------------------------------------------------------

ECHANTILLON = [
    # (n°, type de page, caractère, commentaire de sélection, nom d'onglet court)
    (
        1,
        "Page d'accueil",
        "Obligatoire",
        "Toujours auditée, même si une page de connexion précède.",
        "1. Accueil",
    ),
    (
        2,
        "Page « Mentions légales »",
        "Obligatoire",
        "Page réglementaire, présente sur tous les sites publics.",
        "2. Mentions légales",
    ),
    (
        3,
        "Déclaration d'accessibilité",
        "Obligatoire",
        "Page qui décrit l'état de conformité du site (article 47 de la loi de 2005).",
        "3. Déclaration a11y",
    ),
    (
        4,
        "Page « Plan du site »",
        "Obligatoire",
        "Si présente ; sinon, mentionner NA dans l'audit.",
        "4. Plan du site",
    ),
    (
        5,
        "Page « Contact »",
        "Obligatoire",
        "Formulaire ou page avec coordonnées de l'organisme.",
        "5. Contact",
    ),
    (
        6,
        "Page « Aide » / FAQ",
        "Obligatoire",
        "Si présente ; sinon, mentionner NA.",
        "6. Aide",
    ),
    (
        7,
        "Page d'authentification / connexion",
        "Obligatoire si existante",
        "Auditée uniquement si le site propose un espace personnel.",
        "7. Authentification",
    ),
    (
        8,
        "Page de résultats de recherche",
        "Obligatoire si moteur",
        "Auditée avec un jeu de résultats réel, pas une page vide.",
        "8. Recherche",
    ),
    (
        9,
        "Document téléchargeable (PDF, DOCX, ODT)",
        "Obligatoire si présent",
        "Au moins un document représentatif. Attention : les 13 points de contrôle rapides web ne couvrent qu'en partie les documents. Pour un audit complet, utiliser PAC 2024 (gratuit), Acrobat Pro ou Axes4.",
        "9. Document",
    ),
    (
        10,
        "Page type : article, actualité ou contenu rédactionnel",
        "Représentative",
        "Une page représentative du gabarit éditorial le plus fréquent.",
        "10. Article",
    ),
    (
        11,
        "Page type : formulaire de démarche ou saisie multi-étape",
        "Représentative",
        "Processus critique (inscription, demande, déclaration).",
        "11. Formulaire",
    ),
    (
        12,
        "Page type : liste / rubrique / résultats de navigation",
        "Représentative",
        "Gabarit qui affiche plusieurs éléments triés ou filtrés.",
        "12. Liste",
    ),
]

# Position (ligne) du bloc recap dans chaque onglet de page.
# Aligné sur build_grille : header_row=8, last_row=21, sr=24.
# Recap L25=Conforme, L26=Non conforme, L27=Non applicable, L28=Taux.
RECAP_ROW_CONFORME = 25
RECAP_ROW_NC = 26
RECAP_ROW_NA = 27
RECAP_ROW_TAUX = 28


EXEMPLE = {
    1: (
        "NC",
        "Gênant",
        "3 images porteuses d'information sans alt sur la page d'accueil.",
        "Ajouter un alt descriptif concis aux images 1, 4 et 7.",
        "accueil.html, sélecteurs img.bandeau",
    ),
    2: ("C", "", "Titre présent et unique.", "", ""),
    3: (
        "NC",
        "Mineur",
        "Saut de H2 vers H4 dans la section actualités.",
        "Réintroduire un H3 ou promouvoir le H4 en H3.",
        "accueil.html, section #actu",
    ),
    4: (
        "NC",
        "Bloquant",
        "Texte gris #999 sur fond blanc : ratio 2,85:1.",
        "Relever la couleur à #6C6C6C (ratio 4,5:1 minimum).",
        "Capture contraste.png",
    ),
    5: ("C", "", "Lien « Aller au contenu » présent au 1er Tab.", "", ""),
    6: (
        "NC",
        "Bloquant",
        "Focus invisible sur les 4 boutons de la barre d'action.",
        "Ajouter un style :focus-visible avec outline 2 px.",
        "Vidéo demo.webm",
    ),
    7: ("C", "", '<html lang="fr"> présent.', "", ""),
    8: (
        "NC",
        "Gênant",
        "Le menu déroulant devient inutilisable à 200 %.",
        "Refactoriser en menu accordéon.",
        "Capture zoom200.png",
    ),
    9: ("NA", "", "Pas de vidéo sur la page.", "", ""),
    10: ("NA", "", "Pas de média nécessitant une transcription.", "", ""),
    11: ("NA", "", "Pas de vidéo informative.", "", ""),
    12: (
        "NC",
        "Bloquant",
        "Formulaire de contact : placeholder utilisé comme seule étiquette.",
        "Ajouter un <label> visible au-dessus de chaque champ.",
        "contact.html, form#contact",
    ),
    13: (
        "NC",
        "Bloquant",
        "Après soumission, les erreurs ne sont pas reliées aux champs et le focus reste sans guidage.",
        'Relier chaque erreur avec aria-describedby, poser aria-invalid="true" et déplacer le focus vers le récapitulatif d\'erreurs.',
        "contact.html, form#contact",
    ),
}

# ---------------------------------------------------------------------------
# Helpers de style
# ---------------------------------------------------------------------------

THIN = Side(border_style="thin", color=GRIS_MOYEN)
BORDER_ALL = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

FONT_HEADER = Font(name="Calibri", size=SIZE_HEADER, bold=True, color=BLANC)
FILL_HEADER = PatternFill(
    fill_type="solid", start_color=BLEU_FRANCE, end_color=BLEU_FRANCE
)
ALIGN_HEADER = Alignment(horizontal="center", vertical="center", wrap_text=True)

FONT_TITLE = Font(name="Calibri", size=SIZE_TITLE, bold=True, color=BLEU_FRANCE)
FONT_SECTION = Font(name="Calibri", size=SIZE_SECTION, bold=True, color=BLEU_FRANCE)
FONT_CELL = Font(name="Calibri", size=SIZE_CELL)
FONT_CELL_BOLD = Font(name="Calibri", size=SIZE_CELL, bold=True)
FONT_LINK = Font(name="Calibri", size=SIZE_CELL, color=BLEU_FRANCE, underline="single")
FONT_VERDICT = Font(name="Calibri", size=SIZE_CELL, bold=True)
ALIGN_WRAP = Alignment(horizontal="left", vertical="top", wrap_text=True)
ALIGN_CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)


def style_header_row(ws, row, cols):
    for col in range(1, cols + 1):
        cell = ws.cell(row=row, column=col)
        cell.font = FONT_HEADER
        cell.fill = FILL_HEADER
        cell.alignment = ALIGN_HEADER
        cell.border = BORDER_ALL


def set_widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def configure_print(ws, orientation="landscape"):
    """Configure l'impression : orientation paysage, ajustement a la largeur.

    Sans cette config, l'export PDF des onglets de grille est eclate sur
    plusieurs pages car la largeur utile (colonnes texte riches) depasse
    une page A4 portrait.
    """
    ws.page_setup.orientation = orientation  # "landscape" | "portrait"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4  # 9 = A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0  # hauteur libre
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.horizontalCentered = True
    ws.page_margins = PageMargins(
        left=0.4,
        right=0.4,
        top=0.5,
        bottom=0.5,
        header=0.3,
        footer=0.3,
    )


# ---------------------------------------------------------------------------
# Onglet 1 : Mode d'emploi
# ---------------------------------------------------------------------------

SECTION_KEYS = {
    "Objet",
    "Avertissement",
    "Préparer l'audit",
    "Pour chaque critère, renseigner",
    "Conventions de verdict",
    "Conventions de sévérité",
    "Onglets du classeur",
    "Références",
}


def build_mode_emploi(wb):
    ws = wb.create_sheet("Mode d'emploi")
    set_widths(ws, [12, 130])

    ws["A1"] = (
        f"IGPDE - {FORMATION['footer']} - Grille d'audit 13 points de contrôle rapides du W3C"
    )
    ws["A1"].font = FONT_TITLE
    ws.merge_cells("A1:B1")

    sections = [
        ("", ""),
        ("Objet", ""),
        (
            "",
            "Grille de diagnostic rapide sur les 13 points de contrôle rapides du W3C WAI, alignée sur le RGAA 4.1.2.",
        ),
        ("", ""),
        ("Avertissement", ""),
        ("", "Cet outil est un outil de SENSIBILISATION et de pré-diagnostic."),
        (
            "",
            "Il ne remplace en aucun cas un audit RGAA formel (106 critères sur 13 thématiques) réalisé par un expert certifié.",
        ),
        (
            "",
            "Le « Taux de conformité points de contrôle rapides » calculé ici n'est PAS le taux de conformité RGAA officiel publié en déclaration d'accessibilité.",
        ),
        ("", ""),
        ("Préparer l'audit", ""),
        (
            "1.",
            "Choisir 1 à 5 pages représentatives (accueil, formulaire, résultats de recherche, contact).",
        ),
        ("2.", "Ouvrir dans un navigateur récent (Chrome, Firefox, Edge)."),
        ("3.", "Installer la boîte à outils a11y : https://a11y-tools.netlify.app/"),
        (
            "4.",
            "Prévoir un casque audio et un lecteur d'écran (VoiceOver sur Mac, NVDA sur Windows).",
        ),
        ("", ""),
        ("Pour chaque critère, renseigner", ""),
        ("1.", "Verdict : C (Conforme), NC (Non conforme), NA (Non applicable)."),
        ("2.", "Sévérité : Bloquant, Gênant, Mineur, Info (uniquement si NC)."),
        ("3.", "Constat : ce que vous avez observé concrètement."),
        ("4.", "Correctif : action que l'équipe web devra mener."),
        ("5.", "Preuve : URL, capture d'écran, sélecteur CSS, extrait de code."),
        ("", ""),
        ("Conventions de verdict", ""),
        ("C", "Conforme - le critère est respecté sans réserve."),
        ("NC", "Non conforme - un défaut objectif a été constaté."),
        ("NA", "Non applicable - le critère ne s'applique pas à cette page."),
        ("", ""),
        ("Conventions de sévérité", ""),
        ("Bloquant", "Certaines personnes sont exclues du service."),
        ("Gênant", "Certaines personnes ont des difficultés importantes."),
        ("Mineur", "L'ergonomie peut être améliorée mais l'accès reste possible."),
        ("Info", "Observation à des fins d'amélioration, sans blocage."),
        ("", ""),
        ("Onglets du classeur", ""),
        ("", "Mode d'emploi : ce document."),
        (
            "",
            "Exercice - 13 pages : correspondance entre les slides, les pages du site d'exercice et les lignes à remplir dans la grille.",
        ),
        ("", "Onglets de page : 13 critères à remplir pour la page auditée."),
        ("", "Exemple : audit illustratif sur une page type."),
        ("", "Synthèse : décompte automatique et taux de conformité multi-pages."),
        ("", ""),
        ("Références", ""),
        (
            "",
            "points de contrôle rapides W3C : https://www.w3.org/WAI/test-evaluate/easy-checks/",
        ),
        ("", "RGAA 4.1.2 : https://accessibilite.numerique.gouv.fr/"),
        (
            "",
            "Inspiration méthodologique : grille points de contrôle rapides de beta.gouv.fr.",
        ),
    ]

    # Teinte rouge clair pour le bloc « Avertissement » (section + 3 lignes de texte)
    ALERT_FILL = PatternFill(
        fill_type="solid", start_color="FFE5E5", end_color="FFE5E5"
    )
    FONT_ALERT = Font(name="Calibri", size=SIZE_CELL, bold=True, color="9F0000")

    avert_start = None
    for idx, (left, _right) in enumerate(sections):
        if left == "Avertissement":
            avert_start = idx + 3  # offset start=3 dans l'enumerate
            break

    for i, (left, right) in enumerate(sections, start=3):
        left_cell = ws.cell(row=i, column=1, value=left)
        right_cell = ws.cell(row=i, column=2, value=right)
        right_cell.font = FONT_CELL
        right_cell.alignment = ALIGN_WRAP
        left_cell.alignment = ALIGN_WRAP

        if left in SECTION_KEYS:
            left_cell.font = FONT_SECTION
        else:
            left_cell.font = FONT_CELL_BOLD if left else FONT_CELL

        # Coloration du bloc avertissement (la section + 3 lignes de texte qui suivent)
        if avert_start is not None and avert_start <= i <= avert_start + 3:
            left_cell.fill = ALERT_FILL
            right_cell.fill = ALERT_FILL
            if left == "Avertissement":
                left_cell.font = Font(
                    name="Calibri", size=SIZE_SECTION, bold=True, color="9F0000"
                )
            elif right:
                right_cell.font = FONT_ALERT

    ws.row_dimensions[1].height = 38
    for r in range(3, 3 + len(sections)):
        ws.row_dimensions[r].height = 26

    configure_print(ws, orientation="portrait")
    return ws


# ---------------------------------------------------------------------------
# Onglet Exercice - 13 pages
# ---------------------------------------------------------------------------


def build_exercice_pages(wb):
    """Onglet de liaison entre slides, site d'exercice et grille XLSX."""
    ws = wb.create_sheet("Exercice - 13 pages")
    set_widths(ws, [5, 36, 18, 18, 28, 28, 28, 22, 14, 58])

    ws["A1"] = "Exercice - correspondance entre slides, site et grille"
    ws["A1"].font = FONT_TITLE
    ws.merge_cells("A1:J1")
    ws.row_dimensions[1].height = 38

    intro = ws.cell(
        row=3,
        column=1,
        value="Utilisez cet onglet pendant l'exercice : partez de la slide, ouvrez la page à auditer, puis renseignez la ligne correspondante dans l'onglet de grille conseillé. Les pages d'aide et corrigées servent après la recherche en autonomie.",
    )
    intro.font = FONT_CELL
    intro.alignment = ALIGN_WRAP
    ws.merge_cells("A3:J3")
    ws.row_dimensions[3].height = 58

    header_row = 5
    headers = [
        "#",
        "Page d'exercice",
        "Point rapide",
        "Slides",
        "Page à auditer",
        "Aide",
        "Correction",
        "Onglet conseillé",
        "Ligne",
        "Mission minimale",
    ]
    for col, h in enumerate(headers, start=1):
        ws.cell(row=header_row, column=col, value=h)
    style_header_row(ws, header_row, len(headers))
    ws.row_dimensions[header_row].height = 42

    base_url = "http://127.0.0.1:8765"
    for idx, (check, page) in enumerate(zip(CHECKS, EXERCICE_PAGES), start=1):
        r = header_row + idx
        urls = {
            "audit": f"{base_url}/site-inaccessible/{page['id']}.html",
            "help": f"{base_url}/site-aide-correction/{page['id']}.html",
            "corrected": f"{base_url}/site-accessible/{page['id']}.html",
        }
        values = [
            check["id"],
            page["title"],
            check["titre"],
            page["slides"],
            "Ouvrir",
            "Ouvrir",
            "Ouvrir",
            page["recommended_sheet"],
            check["id"],
            page["minimal_task"],
        ]
        for col, val in enumerate(values, start=1):
            cell = ws.cell(row=r, column=col, value=val)
            cell.font = FONT_CELL
            cell.alignment = ALIGN_CENTER if col in (1, 4, 5, 6, 7, 9) else ALIGN_WRAP
            cell.border = BORDER_ALL

        for col, key in ((5, "audit"), (6, "help"), (7, "corrected")):
            link_cell = ws.cell(row=r, column=col)
            link_cell.hyperlink = urls[key]
            link_cell.font = FONT_LINK

        ws.cell(row=r, column=1).font = FONT_CELL_BOLD
        ws.cell(row=r, column=8).fill = PatternFill(
            fill_type="solid", start_color=BLEU_CLAIR, end_color=BLEU_CLAIR
        )
        ws.cell(row=r, column=9).fill = PatternFill(
            fill_type="solid", start_color=BLEU_CLAIR, end_color=BLEU_CLAIR
        )
        ws.row_dimensions[r].height = 78

    note_row = header_row + len(EXERCICE_PAGES) + 2
    note = ws.cell(
        row=note_row,
        column=1,
        value="Rappel : une seule occurrence correctement prouvée suffit pour renseigner NC sur le point ciblé. Les autres occurrences servent à enrichir la restitution collective.",
    )
    note.font = Font(name="Calibri", size=SIZE_CELL, bold=True, color=BLEU_FRANCE)
    note.alignment = ALIGN_WRAP
    note.fill = PatternFill(
        fill_type="solid", start_color=BLEU_CLAIR, end_color=BLEU_CLAIR
    )
    ws.merge_cells(start_row=note_row, start_column=1, end_row=note_row, end_column=10)
    ws.row_dimensions[note_row].height = 48

    configure_print(ws, orientation="landscape")
    return ws


# ---------------------------------------------------------------------------
# Onglet grille (vierge ou exemple)
# ---------------------------------------------------------------------------


def build_grille(wb, sheet_name, meta_values, rempli=False):
    """Crée un onglet grille d'audit (13 critères + bloc recap).

    - sheet_name : nom de l'onglet (ex. « 1. Accueil »)
    - meta_values : valeurs des 6 lignes de métadonnées
    - rempli : si True, pré-remplit avec l'exemple type

    Structure fixe (importante pour la Synthèse multi-pages) :
    - Lignes 1-6 : métadonnées
    - Ligne 8 : en-tête de grille
    - Lignes 9-21 : 13 critères
    - Ligne 24 : titre « Synthèse de la page »
    - Ligne 25 : Conforme (B25 = COUNTIF "C")
    - Ligne 26 : Non conforme (B26 = COUNTIF "NC")
    - Ligne 27 : Non applicable (B27 = COUNTIF "NA")
    - Ligne 28 : Taux de conformité
    """
    ws = wb.create_sheet(sheet_name)

    # Métadonnées de l'audit (lignes 1 à 6)
    meta_labels = [
        "Auditeur / auditrice",
        "Date de l'audit",
        "URL de la page auditée",
        "Intitulé de la page",
        "Navigateur et version",
        "Outils utilisés",
    ]
    # Méta : label fusionné sur colonnes 1:3 (lisible), valeur sur colonnes 4:11
    for i, (label, value) in enumerate(zip(meta_labels, meta_values), start=1):
        left_cell = ws.cell(row=i, column=1, value=label)
        left_cell.font = FONT_CELL_BOLD
        left_cell.alignment = ALIGN_WRAP
        left_cell.fill = PatternFill(
            fill_type="solid", start_color=BLEU_CLAIR, end_color=BLEU_CLAIR
        )
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=3)
        # Teinter aussi les cellules fusionnées
        for c in (2, 3):
            ws.cell(row=i, column=c).fill = PatternFill(
                fill_type="solid", start_color=BLEU_CLAIR, end_color=BLEU_CLAIR
            )
        right_cell = ws.cell(row=i, column=4, value=value)
        right_cell.font = FONT_CELL
        right_cell.alignment = ALIGN_WRAP
        ws.merge_cells(start_row=i, start_column=4, end_row=i, end_column=11)
        ws.row_dimensions[i].height = 26

    # Note spécifique pour l'onglet « 9. Document téléchargeable »
    if sheet_name.startswith("9."):
        note = ws.cell(
            row=7,
            column=1,
            value="Attention : les 13 points de contrôle rapides web ne couvrent que partiellement les documents. "
            "Pour un audit formel des PDF / DOCX / ODT, utiliser PAC 2024 (outil gratuit), Acrobat Pro ou Axes4.",
        )
        note.font = Font(name="Calibri", size=SIZE_CELL, bold=True, color="9F0000")
        note.alignment = ALIGN_WRAP
        note.fill = PatternFill(
            fill_type="solid", start_color="FFE5E5", end_color="FFE5E5"
        )
        ws.merge_cells("A7:K7")
        ws.row_dimensions[7].height = 52

    # En-tête grille (ligne 8)
    header_row = 8
    headers = [
        "N",
        "Point de contrôle rapide",
        "WCAG 2.2",
        "RGAA 4.1.2",
        "Méthode de test",
        "Ce qu'il faut vérifier",
        "Verdict",
        "Sévérité",
        "Constat",
        "Correctif suggéré",
        "Preuve (URL, sélecteur, capture)",
    ]
    for col, h in enumerate(headers, start=1):
        ws.cell(row=header_row, column=col, value=h)
    style_header_row(ws, header_row, len(headers))

    # Lignes critères
    for idx, check in enumerate(CHECKS):
        r = header_row + 1 + idx
        row_values = [
            check["id"],
            check["titre"],
            check["wcag"],
            check["rgaa"],
            check["methode"],
            check["verifier"],
            "",  # verdict
            "",  # sévérité
            "",  # constat
            "",  # correctif
            "",  # preuve
        ]
        if rempli:
            verdict, severite, constat, correctif, preuve = EXEMPLE[check["id"]]
            row_values[6] = verdict
            row_values[7] = severite
            row_values[8] = constat
            row_values[9] = correctif
            row_values[10] = preuve

        for col, val in enumerate(row_values, start=1):
            cell = ws.cell(row=r, column=col, value=val)
            cell.font = FONT_CELL
            cell.alignment = ALIGN_WRAP if col >= 5 else ALIGN_CENTER
            cell.border = BORDER_ALL

            # Couleur verdict
            if col == 7 and val in VERDICT_COLORS:
                cell.fill = PatternFill(
                    fill_type="solid",
                    start_color=VERDICT_COLORS[val],
                    end_color=VERDICT_COLORS[val],
                )
                cell.alignment = ALIGN_CENTER
                cell.font = FONT_VERDICT
            # Couleur sévérité
            if col == 8 and val in SEVERITE_COLORS:
                cell.fill = PatternFill(
                    fill_type="solid",
                    start_color=SEVERITE_COLORS[val],
                    end_color=SEVERITE_COLORS[val],
                )

    # Validation de données sur colonne verdict (G) et sévérité (H)
    last_row = header_row + len(CHECKS)
    dv_verdict = DataValidation(
        type="list",
        formula1='"C,NC,NA"',
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Verdict invalide",
        error="Valeurs autorisées : C, NC ou NA.",
    )
    dv_verdict.add(f"G{header_row + 1}:G{last_row}")
    ws.add_data_validation(dv_verdict)

    dv_sev = DataValidation(
        type="list",
        formula1='"Bloquant,Gênant,Mineur,Info"',
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Sévérité invalide",
        error="Valeurs autorisées : Bloquant, Gênant, Mineur ou Info.",
    )
    dv_sev.add(f"H{header_row + 1}:H{last_row}")
    ws.add_data_validation(dv_sev)

    # Hauteurs et largeurs ajustées pour une police 14 pt
    set_widths(ws, [6, 34, 14, 22, 40, 46, 12, 14, 44, 44, 36])
    for r in range(header_row + 1, last_row + 1):
        ws.row_dimensions[r].height = 95
    ws.row_dimensions[header_row].height = 38

    # Bloc synthèse en bas de l'onglet
    sr = last_row + 3
    synth_title = ws.cell(row=sr, column=1, value="Synthèse de la page")
    synth_title.font = FONT_SECTION
    ws.merge_cells(start_row=sr, start_column=1, end_row=sr, end_column=4)
    ws.row_dimensions[sr].height = 30

    recap = [
        ("Conforme (C)", f'=COUNTIF(G{header_row + 1}:G{last_row},"C")'),
        ("Non conforme (NC)", f'=COUNTIF(G{header_row + 1}:G{last_row},"NC")'),
        ("Non applicable (NA)", f'=COUNTIF(G{header_row + 1}:G{last_row},"NA")'),
        (
            "Taux de conformité points de contrôle rapides",
            f'=IFERROR(COUNTIF(G{header_row + 1}:G{last_row},"C")/(COUNTIF(G{header_row + 1}:G{last_row},"C")+COUNTIF(G{header_row + 1}:G{last_row},"NC")),0)',
        ),
        (
            "Non-conformités bloquantes",
            f'=COUNTIFS(G{header_row + 1}:G{last_row},"NC",H{header_row + 1}:H{last_row},"Bloquant")',
        ),
        (
            "Non-conformités gênantes",
            f'=COUNTIFS(G{header_row + 1}:G{last_row},"NC",H{header_row + 1}:H{last_row},"Gênant")',
        ),
        (
            "Non-conformités mineures",
            f'=COUNTIFS(G{header_row + 1}:G{last_row},"NC",H{header_row + 1}:H{last_row},"Mineur")',
        ),
    ]
    # Label de synthèse fusionné sur colonnes 1:5, valeur en colonne 6
    for i, (label, formula) in enumerate(recap, start=1):
        lab = ws.cell(row=sr + i, column=1, value=label)
        lab.font = FONT_CELL_BOLD
        lab.alignment = ALIGN_WRAP
        ws.merge_cells(start_row=sr + i, start_column=1, end_row=sr + i, end_column=5)
        val = ws.cell(row=sr + i, column=6, value=formula)
        val.font = FONT_CELL
        val.alignment = ALIGN_CENTER
        if "Taux" in label:
            val.number_format = "0,0 %"
            val.font = Font(
                name="Calibri", size=SIZE_CELL, bold=True, color=BLEU_FRANCE
            )
        ws.row_dimensions[sr + i].height = 26

    # Actions prioritaires
    er = sr + len(recap) + 2
    priorites = ws.cell(row=er, column=1, value="Top 3 des actions prioritaires")
    priorites.font = FONT_SECTION
    ws.merge_cells(start_row=er, start_column=1, end_row=er, end_column=11)
    ws.row_dimensions[er].height = 30
    for i in range(1, 4):
        ws.cell(row=er + i, column=1, value=f"{i}.").font = FONT_CELL_BOLD
        ws.cell(row=er + i, column=1).alignment = ALIGN_CENTER
        saisie = ws.cell(row=er + i, column=2, value="")
        saisie.font = FONT_CELL
        saisie.alignment = ALIGN_WRAP
        saisie.border = BORDER_ALL
        ws.merge_cells(start_row=er + i, start_column=2, end_row=er + i, end_column=11)
        ws.row_dimensions[er + i].height = 32

    engagement_row = er + 5
    eng = ws.cell(row=engagement_row, column=1, value="Mon engagement pour demain 9 h")
    eng.font = FONT_SECTION
    ws.merge_cells(
        start_row=engagement_row, start_column=1, end_row=engagement_row, end_column=11
    )
    ws.row_dimensions[engagement_row].height = 30
    eng_saisie = ws.cell(row=engagement_row + 1, column=1, value="")
    eng_saisie.font = FONT_CELL
    eng_saisie.alignment = ALIGN_WRAP
    eng_saisie.border = BORDER_ALL
    ws.merge_cells(
        start_row=engagement_row + 1,
        start_column=1,
        end_row=engagement_row + 1,
        end_column=11,
    )
    ws.row_dimensions[engagement_row + 1].height = 40

    configure_print(ws, orientation="landscape")
    return ws


# ---------------------------------------------------------------------------
# Onglet synthèse multi-pages
# ---------------------------------------------------------------------------


def build_echantillon_rgaa(wb):
    """Onglet qui documente l'échantillon de pages à auditer selon RGAA 4.1.2."""
    ws = wb.create_sheet("Échantillon RGAA")
    set_widths(ws, [5, 44, 22, 28, 46])

    ws["A1"] = "Échantillon RGAA 4.1.2 - pages obligatoires"
    ws["A1"].font = FONT_TITLE
    ws.merge_cells("A1:E1")
    ws.row_dimensions[1].height = 38

    intro_lines = [
        "La méthode technique du RGAA 4.1.2 impose un échantillon minimal de pages à auditer pour déclarer la conformité d'un site public.",
        "Les 9 premières pages sont obligatoires (sauf si la fonction n'existe pas : noter NA).",
        "Les pages 10 à 12 sont représentatives : au moins une page par type de gabarit (article, formulaire, liste).",
        "Source officielle : https://accessibilite.numerique.gouv.fr/",
    ]
    for idx, line in enumerate(intro_lines, start=3):
        c = ws.cell(row=idx, column=1, value=line)
        c.font = FONT_CELL
        c.alignment = ALIGN_WRAP
        ws.merge_cells(start_row=idx, start_column=1, end_row=idx, end_column=5)
        ws.row_dimensions[idx].height = 28

    header_row = 8
    headers = ["N", "Type de page", "Caractère", "URL à auditer", "Commentaire"]
    for col, h in enumerate(headers, start=1):
        ws.cell(row=header_row, column=col, value=h)
    style_header_row(ws, header_row, len(headers))
    ws.row_dimensions[header_row].height = 38

    for idx, (num, type_page, caractere, commentaire, _nom) in enumerate(ECHANTILLON):
        r = header_row + 1 + idx
        values = [num, type_page, caractere, "", commentaire]
        for col, v in enumerate(values, start=1):
            cell = ws.cell(row=r, column=col, value=v)
            cell.font = FONT_CELL
            cell.alignment = ALIGN_WRAP if col in (2, 4, 5) else ALIGN_CENTER
            cell.border = BORDER_ALL
            # Couleur douce pour distinguer obligatoire / representative
            if col == 3:
                if "Obligatoire" in caractere and "si" not in caractere:
                    cell.fill = PatternFill(
                        fill_type="solid", start_color="E3E3FD", end_color="E3E3FD"
                    )
                elif "Représentative" in caractere:
                    cell.fill = PatternFill(
                        fill_type="solid", start_color="FFF9C4", end_color="FFF9C4"
                    )
                else:  # Obligatoire si ...
                    cell.fill = PatternFill(
                        fill_type="solid", start_color="E1F5FE", end_color="E1F5FE"
                    )
        ws.row_dimensions[r].height = 44

    # Legende couleurs
    legend_row = header_row + len(ECHANTILLON) + 2
    ws.cell(row=legend_row, column=1, value="Légende").font = FONT_SECTION
    ws.row_dimensions[legend_row].height = 30
    legendes = [
        (
            "Obligatoire",
            "E3E3FD",
            "Présente sur tout site public, à auditer systématiquement.",
        ),
        (
            "Obligatoire si existante",
            "E1F5FE",
            "À auditer uniquement si la fonction existe sur le site.",
        ),
        ("Représentative", "FFF9C4", "Échantillon représentatif des gabarits du site."),
    ]
    for i, (label, color, desc) in enumerate(legendes, start=1):
        lab = ws.cell(row=legend_row + i, column=2, value=label)
        lab.font = FONT_CELL_BOLD
        lab.fill = PatternFill(fill_type="solid", start_color=color, end_color=color)
        lab.alignment = ALIGN_CENTER
        d = ws.cell(row=legend_row + i, column=3, value=desc)
        d.font = FONT_CELL
        d.alignment = ALIGN_WRAP
        ws.merge_cells(
            start_row=legend_row + i,
            start_column=3,
            end_row=legend_row + i,
            end_column=5,
        )
        ws.row_dimensions[legend_row + i].height = 30

    configure_print(ws, orientation="landscape")
    return ws


def build_synthese(wb):
    ws = wb.create_sheet("Synthèse")
    set_widths(ws, [6, 44, 22, 16, 16, 16, 22])

    ws["A1"] = "Synthèse multi-pages de l'échantillon RGAA"
    ws["A1"].font = FONT_TITLE
    ws.merge_cells("A1:G1")
    ws.row_dimensions[1].height = 38

    intro = ws.cell(
        row=3,
        column=1,
        value="Les décomptes sont récupérés automatiquement depuis les 12 onglets de page. Les totaux et le taux global se recalculent à chaque saisie dans une grille. Les taux par ligne restent vides tant qu'aucun verdict n'a été saisi sur la page correspondante.",
    )
    intro.font = FONT_CELL
    intro.alignment = ALIGN_WRAP
    ws.merge_cells("A3:G3")
    ws.row_dimensions[3].height = 60

    header_row = 5
    headers = [
        "N",
        "Type de page",
        "Caractère",
        "Conforme",
        "Non conforme",
        "Non applicable",
        "Taux de conformité points de contrôle rapides",
    ]
    for col, h in enumerate(headers, start=1):
        ws.cell(row=header_row, column=col, value=h)
    style_header_row(ws, header_row, len(headers))
    ws.row_dimensions[header_row].height = 40

    # Une ligne par onglet : formules qui pointent vers le bloc recap de l'onglet
    for idx, (num, type_page, caractere, _comm, nom_onglet) in enumerate(ECHANTILLON):
        r = header_row + 1 + idx
        ws.cell(row=r, column=1, value=num).font = FONT_CELL
        ws.cell(row=r, column=1).alignment = ALIGN_CENTER
        ws.cell(row=r, column=2, value=type_page).font = FONT_CELL
        ws.cell(row=r, column=2).alignment = ALIGN_WRAP
        ws.cell(row=r, column=3, value=caractere).font = FONT_CELL
        ws.cell(row=r, column=3).alignment = ALIGN_CENTER

        # Formules qui lisent le bloc recap de chaque onglet de page
        f_conforme = f"=IFERROR('{nom_onglet}'!B{RECAP_ROW_CONFORME},0)"
        f_nc = f"=IFERROR('{nom_onglet}'!B{RECAP_ROW_NC},0)"
        f_na = f"=IFERROR('{nom_onglet}'!B{RECAP_ROW_NA},0)"
        for col, formula in zip((4, 5, 6), (f_conforme, f_nc, f_na)):
            cell = ws.cell(row=r, column=col, value=formula)
            cell.font = FONT_CELL
            cell.alignment = ALIGN_CENTER
            cell.border = BORDER_ALL

        # Taux par ligne toujours affiché (0 % tant que rien saisi, % sinon)
        taux_cell = ws.cell(
            row=r,
            column=7,
            value=f"=IFERROR(D{r}/(D{r}+E{r}),0)",
        )
        taux_cell.font = FONT_CELL
        taux_cell.alignment = ALIGN_CENTER
        taux_cell.number_format = "0,0 %"
        taux_cell.border = BORDER_ALL

        # Bordures sur colonnes figées (1,2,3)
        for col in (1, 2, 3):
            ws.cell(row=r, column=col).border = BORDER_ALL
        # Couleur caractère
        if "Représentative" in caractere:
            ws.cell(row=r, column=3).fill = PatternFill(
                fill_type="solid", start_color="FFF9C4", end_color="FFF9C4"
            )
        elif "si" in caractere:
            ws.cell(row=r, column=3).fill = PatternFill(
                fill_type="solid", start_color="E1F5FE", end_color="E1F5FE"
            )
        else:
            ws.cell(row=r, column=3).fill = PatternFill(
                fill_type="solid", start_color="E3E3FD", end_color="E3E3FD"
            )
        ws.row_dimensions[r].height = 44

    last_row = header_row + len(ECHANTILLON)

    # Ligne totaux
    total_row = last_row + 2
    total_label = ws.cell(row=total_row, column=1, value="Total")
    total_label.font = FONT_CELL_BOLD
    ws.merge_cells(start_row=total_row, start_column=1, end_row=total_row, end_column=3)
    ws.cell(row=total_row, column=1).alignment = ALIGN_CENTER
    for col in range(4, 7):
        letter = get_column_letter(col)
        c = ws.cell(
            row=total_row,
            column=col,
            value=f"=SUM({letter}{header_row + 1}:{letter}{last_row})",
        )
        c.font = FONT_CELL_BOLD
        c.alignment = ALIGN_CENTER
        c.border = BORDER_ALL
    taux_global = ws.cell(
        row=total_row,
        column=7,
        value=f"=IFERROR(D{total_row}/(D{total_row}+E{total_row}),0)",
    )
    taux_global.number_format = "0,0 %"
    taux_global.font = FONT_CELL_BOLD
    taux_global.alignment = ALIGN_CENTER
    taux_global.border = BORDER_ALL
    ws.row_dimensions[total_row].height = 32

    configure_print(ws, orientation="landscape")
    return ws


# ---------------------------------------------------------------------------
# Génération
# ---------------------------------------------------------------------------


def main():
    wb = Workbook()
    wb.remove(wb.active)  # supprime la feuille par défaut

    build_mode_emploi(wb)
    build_exercice_pages(wb)
    build_echantillon_rgaa(wb)

    # 12 onglets de page : un par ligne de l'échantillon RGAA.
    # Chaque onglet est pré-rempli avec le type de page dans la méta.
    for num, type_page, caractere, _comm, nom_onglet in ECHANTILLON:
        build_grille(
            wb,
            sheet_name=nom_onglet,
            meta_values=[
                "",  # Auditeur / auditrice
                "",  # Date de l'audit
                "",  # URL de la page auditée
                type_page,  # Intitulé de la page (pré-rempli)
                "",  # Navigateur et version
                "",  # Outils utilisés
            ],
            rempli=False,
        )

    # Onglet Exemple : modèle pédagogique rempli d'un audit fictif
    build_grille(
        wb,
        "Exemple",
        meta_values=[
            "Dupont Jean",
            "4 juin 2026",
            "https://exemple.gouv.fr/accueil",
            "Page d'accueil ministère",
            "Firefox 122 sous Windows 11",
            "HeadingsMap, DevTools, NVDA",
        ],
        rempli=True,
    )

    build_synthese(wb)

    # Métadonnées du classeur (titre, auteur, sujet, mots-clés)
    cp = wb.properties
    cp.title = (
        f"IGPDE - {FORMATION['footer']} - Grille d'audit 13 points de contrôle rapides"
    )
    cp.subject = (
        "Accessibilité numérique - 13 points de contrôle rapides W3C alignés RGAA 4.1.2"
    )
    cp.creator = (
        "IGPDE - Institut de la Gestion publique et du Développement économique"
    )
    cp.keywords = (
        f"IGPDE, {FORMATION['code']}, accessibilité, RGAA, WCAG, points de contrôle rapides, audit"
    )
    cp.language = "fr-FR"

    out = (
        Path(__file__).resolve().parent.parent
        / "03-easy-checks"
        / "grille-audit-easy-checks.xlsx"
    )
    wb.save(out)
    # macOS : retirer le flag com.apple.quarantine pose par Gatekeeper sur
    # les fichiers produits par Python. Sans ce fix, Excel ouvre le XLSX en
    # mode protege et refuse d'enregistrer les modifications.
    import subprocess

    subprocess.run(
        ["xattr", "-d", "com.apple.quarantine", str(out)],
        capture_output=True,
        check=False,
        timeout=5,
    )
    print(f"[OK] Classeur généré : {out}")


if __name__ == "__main__":
    main()
