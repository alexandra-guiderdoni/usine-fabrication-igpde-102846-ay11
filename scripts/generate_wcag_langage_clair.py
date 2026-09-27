"""Génère le deck distinct "WCAG en langage clair".

Source éditoriale principale :
AAArdvark, "WCAG in Plain English", CC BY-SA 4.0.
https://aaardvarkaccessibility.com/wcag-plain-english/

Source d'inspiration secondaire :
WCAG 2.2 Card Deck, Johannes Lehner et contributeurs, version française,
CC BY-SA 4.0.
https://github.com/johanneslehner/wcag2.2-card-deck

Le contenu ci-dessous est une adaptation pédagogique en français, pas une
traduction littérale. La référence normative reste WCAG 2.2 du W3C/WAI.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from math import ceil
from pathlib import Path

import yaml
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from igpde_dsfr_components import (  # noqa: E402
    BLEU_FRANCE,
    COL_R,
    COL_W,
    CONTENT_W,
    GAP,
    GRIS_CLAIR,
    MARGIN_L,
    ROUGE_MARIANNE,
    TOP_CONTENT,
    add_alert,
    add_callout,
    add_card,
    add_highlight,
    add_image,
    add_notes,
    add_pave_chiffre,
    add_stepper,
    add_tableau,
    add_texte_libre,
    compose_chapitre,
    create_presentation,
    estimate_card_height,
    estimate_highlight_height,
    finalize_pptx,
    new_slide,
)

OUTPUT_DEFAULT = PROJECT_ROOT / "wcag" / "WCAG en langage clair.pptx"
OUTPUT_CONDENSED = PROJECT_ROOT / "wcag" / "WCAG en langage clair - condensé.pptx"
DATE_DEFAULT = yaml.safe_load((PROJECT_ROOT / "config.yml").read_text(encoding="utf-8"))["formation"]["date"]
FOOTER_BASE = "WCAG en langage clair"
AUTHOR = "Alex Guiderdoni"

PRINCIPLE_DESCRIPTIONS = {
    "Percevoir l’information": (
        "Les contenus doivent rester disponibles sous plusieurs formes : "
        "texte, audio, image, structure, contraste."
    ),
    "Utiliser sans obstacle": (
        "Toutes les actions doivent rester possibles sans piège : clavier, "
        "temps suffisant, navigation claire, gestes alternatifs."
    ),
    "Comprendre sans effort inutile": (
        "Les textes, parcours et formulaires doivent rester prévisibles, "
        "explicites et réparables en cas d’erreur."
    ),
    "Rester compatible": (
        "L’interface doit pouvoir être comprise par les aides techniques, "
        "les navigateurs et les outils de lecture."
    ),
}

PERCEVOIR_CARDS = [
    (
        "Contenu non textuel",
        "Toutes les images et contenus non textuels (icônes, graphiques, sons, "
        "CAPTCHA, commandes) doivent être accompagnés d'une alternative textuelle "
        "décrivant leur signification. Le contenu purement esthétique peut être "
        "masqué pour les technologies d'assistance (par exemple, en utilisant un "
        "attribut alt vide).",
    ),
    (
        "Contenus seulement audio et seulement vidéo (pré-enregistré)",
        "Les contenus seulement audio pré-enregistrés doivent disposer d'une "
        "transcription.\nLes contenus seulement vidéo pré-enregistrés doivent "
        "disposer d'une description textuelle ou d'une audiodescription.",
    ),
    (
        "Sous-titres (pré-enregistré)",
        "Les contenus vidéo pré-enregistrés contenant de l'audio doivent disposer "
        "de sous-titres synchronisés comprenant l'intégralité des paroles, et les "
        "sons pertinents (la musique, les alarmes ou les rires, entre autres).",
    ),
    (
        "Audio-description ou version de remplacement (pré-enregistré)",
        "Les éléments visuels importants apparaissant dans des contenus vidéo "
        "pré-enregistrés doivent être décrits via une audiodescription, ou une "
        "alternative textuelle.",
    ),
    (
        "Sous-titres (en direct)",
        "Les contenus vidéo diffusés en direct contenant de l'audio doivent "
        "disposer d'un sous-titrage en temps réel reprenant les paroles, et les "
        "sons importants (la musique, les alarmes ou les rires, entre autres).",
    ),
    (
        "Audio-description (pré-enregistré)",
        "Les éléments visuels importants apparaissant dans des contenus vidéo "
        "pré-enregistrés contenant de l'audio doivent être décrits via une "
        "audio-description, sauf s'ils sont déjà explicités dans la bande sonore "
        "principale.",
    ),
    (
        "Langue des signes (pré-enregistré)",
        "Tous les contenus vidéo pré-enregistrés contenant de l'audio doivent "
        "disposer d'une interprétation en langue des signes.",
    ),
    (
        "Audio-description étendue (pré-enregistré)",
        "Les contenus vidéo pré-enregistrés doivent disposer d'une "
        "audio-description étendue s'ils possèdent des éléments visuels "
        "importants tels que des détails visuels essentiels, du texte "
        "apparaissant à l'écran sans être prononcé à voix haute, ou des scènes "
        "dépourvues de pauses sonores et qui ne peuvent donc pas être décrites "
        "durant la lecture.",
    ),
    (
        "Texte sous forme d'image",
        "Le contenu textuel doit être codé comme du texte, et non comme des "
        "images, sauf si une représentation visuelle spécifique est indispensable "
        "(par exemple, un logo).",
    ),
    (
        "Contraste (amélioré)",
        "Le contraste du texte par rapport à son arrière-plan doit être d'au "
        "moins 7:1 pour un texte classique, ou 4,5:1 pour un texte de grande "
        "taille (supérieur à 24px, ou en gras et supérieur à 19px).",
    ),
    (
        "Texte sous forme d'image (sans exception)",
        "Le contenu textuel doit toujours être codé comme du texte, et non comme "
        "des images (sans exception, même pour des raisons esthétiques).",
    ),
    (
        "Redistribution",
        "Le contenu doit rester fonctionnel et lisible lorsqu'il est zoomé à "
        "400 %, ou affiché sur une largeur de 320 px, sans recourir à aucun "
        "défilement, qu'il soit vertical ou horizontal (sauf pour les tableaux, "
        "les cartes et les contenus similaires).",
    ),
    (
        "Arrière-plan sonore de faible volume ou absent",
        "Pour les contenus audio pré-enregistrés contenant des paroles, tout "
        "bruit de fond doit être au minimum 20 dB plus faible que les dialogues, "
        "ou pouvoir être désactivé.",
    ),
    (
        "Présentation visuelle",
        "Les blocs de textes (tels que les paragraphes) doivent avoir une hauteur "
        "de ligne d'au moins 1.5, ne pas être justifiés, rester limités à 80 "
        "caractères par ligne (ou 40 pour des scripts CJK), et permettre aux "
        "utilisateurs d'ajuster l'espacement et les couleurs du texte à l'aide de "
        "styles personnalisés.",
    ),
    (
        "Contraste du contenu non textuel",
        "Les éléments interactifs (boutons, champs de saisie, indicateurs de "
        "focus, par exemple) et graphiques porteurs de sens (icônes, tableaux, "
        "courbes graphiques, par exemple) doivent présenter un rapport de "
        "contraste d'au moins 3:1 avec les couleurs adjacentes.",
    ),
    (
        "Espacement du texte",
        "Le texte doit rester lisible et fonctionnel lorsque l'espacement est "
        "modifié à l'aide de styles personnalisés, pour au moins 1,5x la hauteur "
        "de ligne, 2x l'espacement entre les paragraphes, 0,12x l'espacement des "
        "lettres, 0,16x l'espacement entre les mots, sans que le contenu ne soit "
        "caché ou coupé.",
    ),
]

UTILISER_CARDS = [
    (
        "Trois flashs",
        "Le contenu ne doit pas clignoter plus de trois fois par seconde "
        "(sans exception, même s'il respecte les seuils de sécurité).",
    ),
    (
        "Animation résultant d'interactions",
        "Les animations déclenchées par une interaction (par exemple, un clic, "
        "un survol, un tapotement) doivent pouvoir être désactivées via les "
        "paramètres système (par exemple, \"réduire les mouvements\") ou "
        "désactivées via une option disponible sur le site.",
    ),
    (
        "Parcours du focus",
        "Le focus doit suivre un ordre logique qui préserve les relations et "
        "qui correspond à la façon dont la page se lit naturellement, "
        "indépendamment de la mise en page ou du sens de lecture.",
    ),
    (
        "Fonction du lien (selon le contexte)",
        "La fonction de chaque lien doit être compréhensible à partir du texte "
        "du lien, ou du contexte environnant.",
    ),
    (
        "Contourner des blocs",
        "Les blocs de contenu répétés sur plusieurs pages doivent pouvoir être "
        "ignorés (par exemple, la navigation, l'en-tête) pour accéder "
        "directement à la partie principale de la page.",
    ),
    (
        "Titre de page",
        "Chaque page doit posséder un attribut <title> unique et explicite qui "
        "reflète sa thématique ou son objectif.",
    ),
    (
        "Accès multiples",
        "Il est essentiel de proposer au moins deux méthodes différentes pour "
        "accéder aux pages ou au contenu (par exemple, via des menus de "
        "navigation, des liens sur la page ou une recherche sur le site).",
    ),
    (
        "En-têtes et étiquettes",
        "Les en-têtes doivent décrire le contenu qui suit.\nLes étiquettes et "
        "les boutons doivent permettre d'identifier sans ambiguïté l'information "
        "à saisir ou l'action déclenchée.",
    ),
    (
        "Modalités d'entrées concurrentes",
        "Il doit être possible de passer d'une méthode de saisie à une autre "
        "(souris, clavier, écran tactile, commande vocale) tout en conservant "
        "l'accès à toutes les fonctionnalités.",
    ),
    (
        "Mouvements de glissement",
        "Les actions nécessitant un glissement (comme le réarrangement "
        "d'éléments) doivent également être réalisables à l'aide de boutons ou "
        "d'une autre méthode qui ne nécessite pas de glissement.",
    ),
]

COMPRENDRE_CARDS = [
    (
        "Langue de la page",
        "Chaque page doit comporter un attribut <html lang=\"\"> correspondant "
        "à la langue principale de la page.",
    ),
    (
        "Langue d'un passage",
        "Chaque passage d'un contenu rédigé dans une autre langue doit être "
        "notifié à l'aide de l'attribut lang approprié. Les expressions "
        "empruntées à une autre langue (comme \"week-end\", par exemple) n'ont "
        "pas besoin de cet attribut, sauf si la prononciation ou la "
        "compréhension est affectée.",
    ),
    (
        "Mots rares",
        "Les termes utilisés de manière inhabituelle, le jargon et les "
        "expressions idiomatiques doivent être évités dans la mesure du "
        "possible, ou être expliqués dès leur première occurrence.",
    ),
    (
        "Prononciation",
        "Lorsque la prononciation d'un mot peut varier et changer sa "
        "signification, il est nécessaire de clarifier le sens voulu pour "
        "éviter toute confusion ou ambiguïté.",
    ),
    (
        "Au focus",
        "Lorsqu'un élément reçoit le focus, aucun changement imprévu ne doit "
        "se produire (comme l'ouverture d'une fenêtre contextuelle, le "
        "déplacement du focus ou la validation d'un formulaire).",
    ),
    (
        "Abréviations",
        "Les abréviations et acronymes doivent être évités dans la mesure du "
        "possible, ou être expliqués lors de leur première occurrence.",
    ),
    (
        "Lisibilité du texte",
        "Si le contenu nécessite une capacité de lecture plus avancée que le "
        "premier cycle de l'enseignement secondaire (autrement dit la classe "
        "de 3e), il est essentiel de fournir une version simplifiée, un résumé, "
        "un support visuel ou une version audio pour faciliter la compréhension.",
    ),
    (
        "Prévention des erreurs (toutes)",
        "Avant de valider l'envoi d'un formulaire, il doit être possible de "
        "vérifier les informations saisies et corriger les erreurs.",
    ),
    (
        "Saisie redondante",
        "Ne demandez pas les mêmes informations deux fois au cours d'un même "
        "processus. Proposez des champs préremplis ou des options de sélection "
        "si les informations ont déjà été fournies au préalable.",
    ),
    (
        "Authentification accessible (minimum)",
        "L'authentification ne doit pas reposer uniquement sur la mémoire. "
        "Elle doit autoriser le copier-coller, les gestionnaires de mots de "
        "passe ou d'autres options (comme la vérification par e-mail).",
    ),
    (
        "Authentification accessible (améliorée)",
        "L'authentification ne doit pas reposer sur la mémoire ou la "
        "reconnaissance (comme résoudre des énigmes, se souvenir d'images "
        "ou utiliser des CAPTCHA).",
    ),
]

COMPATIBLE_CARDS = [
    (
        "Analyse syntaxique (obsolète et supprimé)",
        "Ce critère nécessitait un code HTML correctement structuré et sans "
        "erreurs critiques (telles que des balises manquantes ou des "
        "identifiants en double). Bien que cette exigence ait été supprimée, "
        "elle reste utile en termes de compatibilité.",
    ),
    (
        "Nom, rôle et valeur",
        "Les éléments interactifs doivent disposer d'un nom clair (ce qu'ils "
        "sont), d'un rôle approprié (ce qu'ils font), et de toute valeur ou "
        "état actuel, afin que les technologies d'assistance puissent les "
        "interpréter et interagir correctement avec eux.",
    ),
    (
        "Messages d'état",
        "Les mises à jour d'état (telles que \"formulaire envoyé\" ou "
        "\"5 articles dans le panier\") doivent être codées avec des rôles "
        "appropriés (tels que role=\"status\" ou role=\"alert\"), être "
        "détectables par les technologies d'assistance, et ne pas nécessiter "
        "de déplacement du focus.",
    ),
]

CARD_DECK_FR_TITLES = {
    "1.1.1": "Contenu non textuel",
    "1.2.1": "Contenus seulement audio et seulement vidéo (pré-enregistré)",
    "1.2.2": "Sous-titres (pré-enregistré)",
    "1.2.3": "Audio-description ou version de remplacement pour un média temporel (pré-enregistré)",
    "1.2.4": "Sous-titres (en direct)",
    "1.2.5": "Audio-description (pré-enregistré)",
    "1.2.6": "Langue des signes (pré-enregistré)",
    "1.2.7": "Audio-description étendue (pré-enregistré)",
    "1.2.8": "Version de remplacement pour un média temporel (pré-enregistré)",
    "1.2.9": "Contenu seulement audio (en direct)",
    "1.3.1": "Informations et relations",
    "1.3.2": "Ordre séquentiel logique",
    "1.3.3": "Caractéristiques sensorielles",
    "1.3.4": "Orientation",
    "1.3.5": "Identifier la finalité de la saisie",
    "1.3.6": "Identifier la fonction",
    "1.4.1": "Utilisation de la couleur",
    "1.4.2": "Contrôle du son",
    "1.4.3": "Contraste (minimum)",
    "1.4.4": "Redimensionnement du texte",
    "1.4.5": "Texte sous forme d’image",
    "1.4.6": "Contraste (amélioré)",
    "1.4.7": "Arrière-plan sonore de faible volume ou absent",
    "1.4.8": "Présentation visuelle",
    "1.4.9": "Texte sous forme d’image (sans exception)",
    "1.4.10": "Redistribution",
    "1.4.11": "Contraste du contenu non textuel",
    "1.4.12": "Espacement du texte",
    "1.4.13": "Contenu au survol ou au focus",
    "2.1.1": "Clavier",
    "2.1.2": "Pas de piège au clavier",
    "2.1.3": "Clavier (pas d’exception)",
    "2.1.4": "Raccourcis clavier utilisant des caractères",
    "2.2.1": "Réglage du délai",
    "2.2.2": "Mettre en pause, arrêter, masquer",
    "2.2.3": "Pas de délai d’exécution",
    "2.2.4": "Interruptions",
    "2.2.5": "Nouvelle authentification",
    "2.2.6": "Délais d’expiration",
    "2.3.1": "Pas plus de trois flashs ou sous le seuil critique",
    "2.3.2": "Trois flashs",
    "2.3.3": "Animation résultant d’interactions",
    "2.4.1": "Contourner des blocs",
    "2.4.2": "Titre de page",
    "2.4.3": "Parcours du focus",
    "2.4.4": "Fonction du lien (selon le contexte)",
    "2.4.5": "Accès multiples",
    "2.4.6": "En-têtes et étiquettes",
    "2.4.7": "Visibilité du focus",
    "2.4.8": "Localisation",
    "2.4.9": "Fonction du lien (lien uniquement)",
    "2.4.10": "En-têtes de section",
    "2.4.11": "Focus non masqué (minimum)",
    "2.4.12": "Focus non masqué (amélioré)",
    "2.4.13": "Apparence du focus",
    "2.5.1": "Gestes pour le contrôle du pointeur",
    "2.5.2": "Annulation de l’action du pointeur",
    "2.5.3": "Étiquette dans le nom",
    "2.5.4": "Activation par le mouvement",
    "2.5.5": "Taille de la cible (amélioré)",
    "2.5.6": "Modalités d’entrées concurrentes",
    "2.5.7": "Mouvements de glissement",
    "2.5.8": "Taille de la cible (minimum)",
    "3.1.1": "Langue de la page",
    "3.1.2": "Langue d’un passage",
    "3.1.3": "Mots rares",
    "3.1.4": "Abréviations",
    "3.1.5": "Lisibilité du texte",
    "3.1.6": "Prononciation",
    "3.2.1": "Au focus",
    "3.2.2": "À la saisie",
    "3.2.3": "Navigation cohérente",
    "3.2.4": "Identification cohérente",
    "3.2.5": "Changement à la demande",
    "3.2.6": "Aide cohérente",
    "3.3.1": "Identification des erreurs",
    "3.3.2": "Étiquettes ou instructions",
    "3.3.3": "Suggestion après une erreur",
    "3.3.4": "Prévention des erreurs (juridiques, financières, de données)",
    "3.3.5": "Aide",
    "3.3.6": "Prévention des erreurs (toutes)",
    "3.3.7": "Saisie redondante",
    "3.3.8": "Authentification accessible (minimum)",
    "3.3.9": "Authentification accessible (améliorée)",
    "4.1.1": "Analyse syntaxique (obsolète et supprimé)",
    "4.1.2": "Nom, rôle et valeur",
    "4.1.3": "Messages d’état",
}


@dataclass(frozen=True)
class Criterion:
    code: str
    title: str
    plain: str


@dataclass(frozen=True)
class Guideline:
    code: str
    title: str
    question: str
    section: str
    criteria: tuple[Criterion, ...]


class DeckContext:
    def __init__(self, prs, layouts, date=DATE_DEFAULT, footer_base=FOOTER_BASE):
        self.prs = prs
        self.layouts = layouts
        self.date = date
        self.footer_base = footer_base
        self.page_num = 0

    def slide(self, layout_name="titre_contenu", titre=None, fil_ariane=None,
              footer_suffix=""):
        self.page_num += 1
        footer_text = self.footer_base
        if footer_suffix:
            footer_text = f"{footer_text} / {footer_suffix}"
        return new_slide(
            self.prs,
            self.layouts,
            layout_name=layout_name,
            titre=titre,
            fil_ariane=fil_ariane,
            footer_text=footer_text,
            date_text=self.date,
            page_num=self.page_num,
        )


GUIDELINES = (
    Guideline(
        "1.1",
        "Équivalents texte",
        "Si l’on ne voit pas le contenu, que reste-t-il ?",
        "1. Percevoir l’information",
        (
            Criterion(
                "1.1.1", "Équivalents texte",
                "Images, sons, graphiques et boutons ont une description utile. Le décoratif peut être ignoré.",
            ),
        ),
    ),
    Guideline(
        "1.2",
        "Médias temporels",
        "Si l’on n’entend pas ou ne voit pas la vidéo, peut-on comprendre ?",
        "1. Percevoir l’information",
        (
            Criterion(
                "1.2.1", "Audio ou vidéo seuls",
                "Un audio a besoin d’une transcription. Une vidéo sans son a besoin d’une description.",
            ),
            Criterion(
                "1.2.2", "Sous-titres vidéo",
                "Les vidéos avec son ont des sous-titres synchronisés avec paroles et sons utiles.",
            ),
            Criterion(
                "1.2.3", "Visuels décrits",
                "Les informations visuelles importantes sont décrites dans l’audio ou dans un texte.",
            ),
            Criterion(
                "1.2.4", "Sous-titres en direct",
                "Le direct vidéo avec son propose des sous-titres en temps réel.",
            ),
            Criterion(
                "1.2.5", "Audiodescription",
                "Les visuels importants d’une vidéo enregistrée sont décrits si la piste son ne suffit pas.",
            ),
            Criterion(
                "1.2.6", "Langue des signes",
                "Les vidéos enregistrées avec son ont une interprétation en langue des signes.",
            ),
            Criterion(
                "1.2.7", "Description étendue",
                "Si l’audio ne laisse pas le temps de décrire, une version avec pauses est prévue.",
            ),
            Criterion(
                "1.2.8", "Alternative complète",
                "Une vidéo enregistrée a une version texte complète : paroles, sons utiles et actions visibles.",
            ),
            Criterion(
                "1.2.9", "Audio direct",
                "Un direct audio seul propose une transcription ou des sous-titres en temps réel.",
            ),
        ),
    ),
    Guideline(
        "1.3",
        "Adaptable",
        "Si la présentation change, le sens reste-t-il intact ?",
        "1. Percevoir l’information",
        (
            Criterion(
                "1.3.1", "Relations visibles",
                "Titres, listes, étiquettes et groupes restent compréhensibles par les aides techniques.",
            ),
            Criterion(
                "1.3.2", "Ordre logique",
                "L’ordre de lecture garde le sens même si la mise en page change.",
            ),
            Criterion(
                "1.3.3", "Pas seulement sensoriel",
                "Ne pas dire seulement « le bouton rouge » ou « à droite ». Ajouter un nom clair.",
            ),
            Criterion(
                "1.3.4", "Orientation",
                "Le contenu marche en portrait et en paysage, sauf si une orientation est vraiment essentielle.",
            ),
            Criterion(
                "1.3.5", "Champs connus",
                "Les champs courants comme nom, mail ou adresse peuvent être reconnus et aidés.",
            ),
            Criterion(
                "1.3.6", "Zones identifiables",
                "Les grandes zones et éléments courants peuvent être reconnus et simplifiés par les aides.",
            ),
        ),
    ),
    Guideline(
        "1.4",
        "Visible et lisible",
        "Est-ce assez visible, lisible et stable pour différents usages ?",
        "1. Percevoir l’information",
        (
            Criterion(
                "1.4.1", "Couleur seule",
                "La couleur ne suffit jamais. Ajouter texte, icône, soulignement, forme ou motif.",
            ),
            Criterion(
                "1.4.2", "Son automatique",
                "Un son automatique de plus de 3 secondes peut être pausé, stoppé ou baissé.",
            ),
            Criterion(
                "1.4.3", "Contraste texte",
                "Le texte est assez contrasté : 4,5:1, ou 3:1 pour du grand texte.",
            ),
            Criterion(
                "1.4.4", "Zoom texte",
                "Le texte reste lisible et utilisable quand il est agrandi à 200 %.",
            ),
            Criterion(
                "1.4.5", "Texte natif",
                "Le texte reste du vrai texte, pas une image, sauf besoin visuel indispensable comme un logo.",
            ),
            Criterion(
                "1.4.6", "Contraste renforcé",
                "Le contraste visé est 7:1 pour texte normal et 4,5:1 pour grand texte.",
            ),
            Criterion(
                "1.4.7", "Fond sonore bas",
                "Dans un audio parlé, le fond sonore est faible ou peut être coupé.",
            ),
            Criterion(
                "1.4.8", "Présentation lisible",
                "Paragraphes aérés, non justifiés, lignes courtes et couleurs ajustables par l’utilisateur.",
            ),
            Criterion(
                "1.4.9", "Aucune image de texte",
                "Le texte reste du vrai texte, même pour des raisons esthétiques.",
            ),
            Criterion(
                "1.4.10", "Reflow",
                "À 400 % ou sur petit écran, on lit sans défilement dans deux directions.",
            ),
            Criterion(
                "1.4.11", "Contraste non texte",
                "Boutons, champs, focus, icônes et graphiques utiles ont un contraste d’au moins 3:1.",
            ),
            Criterion(
                "1.4.12", "Espacement du texte",
                "Le texte reste lisible si l’utilisateur augmente interligne, mots, lettres et paragraphes.",
            ),
            Criterion(
                "1.4.13", "Survol et focus",
                "Un contenu qui apparaît au survol ou au focus reste visible et peut être fermé.",
            ),
        ),
    ),
    Guideline(
        "2.1",
        "Clavier",
        "Peut-on tout faire sans souris ?",
        "2. Utiliser sans obstacle",
        (
            Criterion(
                "2.1.1", "Tout au clavier",
                "Toute fonction marche au clavier seul, sauf geste libre indispensable comme dessiner.",
            ),
            Criterion(
                "2.1.2", "Pas de piège",
                "On peut entrer et sortir de chaque composant au clavier sans rester bloqué.",
            ),
            Criterion(
                "2.1.3", "Clavier sans exception",
                "Tout marche au clavier, même les actions souvent pensées pour la souris ou le toucher.",
            ),
            Criterion(
                "2.1.4", "Raccourcis simples",
                "Les raccourcis à une seule touche peuvent être désactivés, modifiés ou limités au bon contexte.",
            ),
        ),
    ),
    Guideline(
        "2.2",
        "Assez de temps",
        "La personne a-t-elle le temps de lire et d’agir ?",
        "2. Utiliser sans obstacle",
        (
            Criterion(
                "2.2.1", "Délais réglables",
                "Éviter les limites de temps. Sinon, permettre de les couper, ajuster ou prolonger.",
            ),
            Criterion(
                "2.2.2", "Mettre en pause, arrêter, masquer",
                "Ce qui bouge ou se met à jour plus de 5 secondes peut être pausé, stoppé ou caché.",
            ),
            Criterion(
                "2.2.3", "Pas de limite",
                "Aucune limite de temps pour lire ou agir, sauf événement en direct ou activité minutée.",
            ),
            Criterion(
                "2.2.4", "Interruptions",
                "Notifications et interruptions peuvent être retardées ou coupées, sauf urgence.",
            ),
            Criterion(
                "2.2.5", "Reconnexion",
                "Après reconnexion, les données déjà saisies restent disponibles.",
            ),
            Criterion(
                "2.2.6", "Expiration",
                "Avant de perdre des données, la personne est prévenue et peut prolonger la session.",
            ),
        ),
    ),
    Guideline(
        "2.3",
        "Crises et réactions physiques",
        "Le contenu évite-t-il les effets qui peuvent provoquer une réaction ?",
        "2. Utiliser sans obstacle",
        (
            Criterion(
                "2.3.1", "Trois flashs max",
                "Rien ne clignote plus de trois fois par seconde, sauf si le seuil de sécurité est respecté.",
            ),
            Criterion(
                "2.3.2", "Aucun flash risqué",
                "Rien ne clignote plus de trois fois par seconde, sans exception.",
            ),
            Criterion(
                "2.3.3", "Animations",
                "Les animations déclenchées par l’action peuvent être réduites ou désactivées.",
            ),
        ),
    ),
    Guideline(
        "2.4",
        "Navigation",
        "La personne sait-elle où elle est et comment avancer ?",
        "2. Utiliser sans obstacle",
        (
            Criterion(
                "2.4.1", "Éviter les blocs",
                "On peut passer les menus répétés et aller directement au contenu principal.",
            ),
            Criterion(
                "2.4.2", "Titre de page",
                "Chaque page a un titre unique et descriptif.",
            ),
            Criterion(
                "2.4.3", "Ordre du focus",
                "Le parcours au clavier suit un ordre logique et compréhensible.",
            ),
            Criterion(
                "2.4.4", "Liens en contexte",
                "La destination ou l’action d’un lien est claire avec son texte ou son contexte.",
            ),
            Criterion(
                "2.4.5", "Plusieurs chemins",
                "Il existe au moins deux moyens de trouver une page : menu, recherche, plan, liens.",
            ),
            Criterion(
                "2.4.6", "Titres et étiquettes",
                "Les titres annoncent le contenu. Les boutons et champs disent clairement l’action ou l’attendu.",
            ),
            Criterion(
                "2.4.7", "Focus visible",
                "Au clavier, on voit toujours quel élément est actif.",
            ),
            Criterion(
                "2.4.8", "Localisation",
                "La personne comprend où elle se trouve dans l’ensemble de pages.",
            ),
            Criterion(
                "2.4.9", "Lien seul",
                "Le texte du lien suffit à comprendre sa destination ou son action.",
            ),
            Criterion(
                "2.4.10", "Sections claires",
                "Les contenus liés sont regroupés sous des titres utiles.",
            ),
            Criterion(
                "2.4.11", "Focus non masqué",
                "Quand un élément reçoit le focus, il reste au moins partiellement visible.",
            ),
            Criterion(
                "2.4.12", "Focus entièrement visible",
                "Le focus reste entièrement visible et non recouvert.",
            ),
            Criterion(
                "2.4.13", "Apparence du focus",
                "Le focus est épais, contrasté et clairement rattaché à l’élément actif.",
            ),
        ),
    ),
    Guideline(
        "2.5",
        "Modes d’interaction",
        "L’action reste-t-elle possible avec un autre geste ou un autre outil ?",
        "2. Utiliser sans obstacle",
        (
            Criterion(
                "2.5.1", "Gestes complexes",
                "Un geste comme glisser ou pincer a aussi une alternative simple : clic, bouton, appui.",
            ),
            Criterion(
                "2.5.2", "Annulation du clic",
                "L’action ne part pas au toucher initial, mais au relâchement ou avec annulation possible.",
            ),
            Criterion(
                "2.5.3", "Nom visible repris",
                "Le nom entendu par une aide vocale reprend le texte visible du bouton ou du champ.",
            ),
            Criterion(
                "2.5.4", "Mouvement appareil",
                "Secouer ou incliner l’appareil n’est jamais le seul moyen d’agir.",
            ),
            Criterion(
                "2.5.5", "Grande cible",
                "Les cibles souris ou tactiles font au moins 44 x 44 pixels, sauf cas limites.",
            ),
            Criterion(
                "2.5.6", "Entrées multiples",
                "On peut passer de la souris au clavier, au toucher ou à la voix sans perdre de fonction.",
            ),
            Criterion(
                "2.5.7", "Glisser-déposer",
                "Une action par glisser-déposer a aussi une méthode sans glisser.",
            ),
            Criterion(
                "2.5.8", "Taille minimale",
                "Les cibles font au moins 24 x 24 pixels ou ont assez d’espace autour.",
            ),
        ),
    ),
    Guideline(
        "3.1",
        "Lisible",
        "Le texte est-il clair pour les personnes et les outils de lecture ?",
        "3. Comprendre sans effort inutile",
        (
            Criterion(
                "3.1.1", "Langue de page",
                "La langue principale est indiquée pour la bonne prononciation.",
            ),
            Criterion(
                "3.1.2", "Changement de langue",
                "Un passage dans une autre langue est signalé quand cela change la lecture.",
            ),
            Criterion(
                "3.1.3", "Mots rares",
                "Les termes inhabituels, images ou jargons sont évités ou expliqués.",
            ),
            Criterion(
                "3.1.4", "Abréviations",
                "Les sigles et abréviations sont évités ou expliqués à la première occurrence.",
            ),
            Criterion(
                "3.1.5", "Lisibilité du texte",
                "Si le texte est difficile, proposer résumé, version simple, visuel ou oral.",
            ),
            Criterion(
                "3.1.6", "Prononciation",
                "Si un mot se prononce de plusieurs façons, le sens voulu est clarifié.",
            ),
        ),
    ),
    Guideline(
        "3.2",
        "Prévisible",
        "Le site se comporte-t-il comme la personne s’y attend ?",
        "3. Comprendre sans effort inutile",
        (
            Criterion(
                "3.2.1", "Au focus",
                "Recevoir le focus ne déclenche pas une action surprise.",
            ),
            Criterion(
                "3.2.2", "À la saisie",
                "Changer une valeur ne valide pas, ne recharge pas et ne déplace pas sans prévenir.",
            ),
            Criterion(
                "3.2.3", "Navigation stable",
                "Menus, recherche et liens récurrents restent au même endroit et dans le même ordre.",
            ),
            Criterion(
                "3.2.4", "Même fonction, même nom",
                "Les éléments qui font la même chose ont le même nom et le même comportement.",
            ),
            Criterion(
                "3.2.5", "Changement demandé",
                "Un changement majeur arrive seulement après une demande explicite.",
            ),
            Criterion(
                "3.2.6", "Aide cohérente",
                "Les options d’aide restent au même endroit sur les pages concernées.",
            ),
        ),
    ),
    Guideline(
        "3.3",
        "Aide à la saisie",
        "La personne peut-elle éviter, comprendre et corriger ses erreurs ?",
        "3. Comprendre sans effort inutile",
        (
            Criterion(
                "3.3.1", "Erreur identifiée",
                "Les erreurs sont décrites en texte, pas seulement en couleur ou surbrillance.",
            ),
            Criterion(
                "3.3.2", "Libellés clairs",
                "Chaque champ a un libellé ou une consigne qui aide à remplir correctement.",
            ),
            Criterion(
                "3.3.3", "Suggestion",
                "Le message d’erreur explique le problème et propose une correction.",
            ),
            Criterion(
                "3.3.4", "Actions sensibles",
                "Avant paiement, signature ou envoi important, on peut vérifier, corriger ou confirmer.",
            ),
            Criterion(
                "3.3.5", "Aide disponible",
                "Quand le libellé ne suffit pas, une aide supplémentaire est disponible.",
            ),
            Criterion(
                "3.3.6", "Tous formulaires",
                "Avant tout envoi, on peut vérifier, corriger ou confirmer les informations.",
            ),
            Criterion(
                "3.3.7", "Pas de ressaisie",
                "Ne pas redemander une information déjà donnée dans le même parcours.",
            ),
            Criterion(
                "3.3.8", "Connexion accessible",
                "La connexion ne repose pas seulement sur la mémoire : copier-coller et gestionnaires marchent.",
            ),
            Criterion(
                "3.3.9", "Connexion renforcée",
                "La connexion n’impose pas puzzle, image à reconnaître ou test cognitif.",
            ),
        ),
    ),
    Guideline(
        "4.1",
        "Compatible",
        "Les aides techniques peuvent-elles comprendre l’interface ?",
        "4. Rester compatible",
        (
            Criterion(
                "4.1.1", "Structure propre",
                "Critère obsolète en WCAG 2.2. Une structure propre reste utile pour la compatibilité.",
            ),
            Criterion(
                "4.1.2", "Nom, rôle, valeur",
                "Chaque élément interactif expose son nom, son rôle et son état aux aides techniques.",
            ),
            Criterion(
                "4.1.3", "Messages d’état",
                "Les messages comme « formulaire envoyé » sont perçus sans déplacer le focus.",
            ),
        ),
    ),
)


def add_title_suffix(slide, text):
    add_texte_libre(
        slide,
        text,
        top=1.85,
        left=MARGIN_L,
        width=CONTENT_W,
        height=0.28,
        size=12,
        bold=True,
        color=BLEU_FRANCE,
    )


def add_card_grid(slide, cards, top=2.45, cols=2, strict=False):
    rows = ceil(len(cards) / cols)
    card_w = (CONTENT_W - GAP * (cols - 1)) / cols
    row_gap = 0.22 if strict else 0.26
    available_h = 6.76 - top - row_gap * (rows - 1)
    card_h = available_h / rows
    if strict:
        card_h = min(card_h, 2.30)
    else:
        card_h = min(card_h, 2.12)
    card_h = max(card_h, 1.50)
    extra = {}
    if strict:
        extra = {"title_size": 12, "body_size": 12}
    for index, (title, body) in enumerate(cards):
        row = index // cols
        col = index % cols
        left = MARGIN_L + col * (card_w + GAP)
        y = top + row * (card_h + row_gap)
        if strict:
            height = card_h
        else:
            needed = estimate_card_height(title, body, card_w)
            height = max(card_h, needed)
            if y + height > 6.76:
                height = card_h
        add_card(slide, title, body, top=y, left=left, width=card_w,
                 height=height, **extra)


def slide_cover(ctx, subtitle="Adaptation pédagogique DSFR d’après AAArdvark",
                note_suffix=""):
    slide = ctx.slide(
        layout_name="couverture",
        titre="WCAG en langage clair",
        footer_suffix="Accueil",
    )
    add_texte_libre(
        slide,
        subtitle,
        top=5.35,
        left=5.8,
        width=7.1,
        height=0.45,
        size=14,
        bold=True,
        color=ROUGE_MARIANNE,
        align=PP_ALIGN.RIGHT,
    )
    note = (
        "Accueil du groupe. Préciser que ce support transforme les critères WCAG en langage clair, "
        "sans remplacer la norme officielle. Source principale : AAArdvark, WCAG in Plain English, "
        "licence CC BY-SA 4.0."
    )
    if note_suffix:
        note = f"{note} {note_suffix}"
    add_notes(slide, note)


def slide_intention(ctx):
    slide = ctx.slide(
        titre="Ce que ce deck fait",
        fil_ariane="Mode d’emploi",
        footer_suffix="Mode d’emploi",
    )
    texte = (
        "Objectif : passer d’une règle WCAG à une question simple "
        "que l’on peut poser avant de publier."
    )
    add_highlight(slide, texte, top=TOP_CONTENT)
    add_card_grid(
        slide,
        [
            ("Comprendre", "Voir l’intention de la règle avant le vocabulaire technique."),
            ("Traduire", "Transformer chaque critère en geste concret de publication."),
            ("Vérifier", "Repérer rapidement ce qui bloque lecture, action ou correction."),
            ("Orienter", "Savoir qui mobiliser : contenu, design ou technique."),
        ],
        top=3.55,
    )
    add_notes(
        slide,
        "Cette slide fixe le contrat pédagogique. Le deck sert à comprendre et à agir. "
        "Pour un audit formel, renvoyer vers WCAG 2.2 et le RGAA 4.1.2.",
    )


def slide_source(ctx):
    slide = ctx.slide(
        titre="La source : WCAG en langage simple",
        fil_ariane="Mode d’emploi",
        footer_suffix="Sources",
    )
    add_callout(
        slide,
        "Corpus principal",
        [
            "AAArdvark, WCAG in Plain English, licence CC BY-SA 4.0",
            "WCAG 2.2 Card Deck, version française, licence CC BY-SA 4.0",
            "Adaptation française pédagogique, non littérale",
            "Référence normative : WCAG 2.2 du W3C/WAI",
        ],
        top=2.32,
        left=MARGIN_L,
        width=COL_W,
    )
    add_alert(
        slide,
        "Point de prudence",
        [
            "Ce support aide à comprendre les critères.",
            "Il ne remplace ni la norme WCAG officielle, ni la méthode RGAA pour le cadre français.",
        ],
        top=2.32,
        left=COL_R,
        width=COL_W,
    )
    add_texte_libre(
        slide,
        "Licence visible en fin de deck : attribution AAArdvark, WCAG 2.2 Card Deck et partage CC BY-SA 4.0 pour les contenus adaptés.",
        top=5.55,
        height=0.70,
        size=14,
        bold=True,
        color=BLEU_FRANCE,
    )
    add_notes(
        slide,
        "Source : https://aaardvarkaccessibility.com/wcag-plain-english/. "
        "WCAG 2.2 Card Deck : https://github.com/johanneslehner/wcag2.2-card-deck. "
        "Licence : https://creativecommons.org/licenses/by-sa/4.0/. "
        "Référence W3C : https://www.w3.org/WAI/standards-guidelines/wcag/.",
    )


def slide_structure(ctx, fil_ariane="Mode d’emploi", qr_code=False):
    slide = ctx.slide(
        titre="Comment comprendre les principes WCAG",
        fil_ariane=fil_ariane,
        footer_suffix="Carte mentale",
    )
    add_stepper(
        slide,
        [
            "4 principes : percevoir, utiliser, comprendre, rester compatible",
            "13 lignes directrices : les grands sujets à traiter",
            "Critères de succès : les exigences testables",
            "Preuves : test, mesure, exemple corrigé ou contenu modifié",
        ],
        top=2.40,
        height=1.75,
    )
    if qr_code:
        callout_w = COL_W + GAP + COL_W * 0.35
        add_callout(
            slide,
            "Le bon réflexe",
            [
                "Ne pas apprendre la liste par cœur.",
                "Savoir transformer un critère en question : "
                "que doit pouvoir faire la personne ?",
            ],
            top=4.65,
            left=MARGIN_L,
            width=callout_w,
        )
        qr_left = MARGIN_L + callout_w + GAP
        qr_w = CONTENT_W - callout_w - GAP
        qr_img_size = 1.30
        qr_img_left = qr_left + (qr_w - qr_img_size) / 2
        add_image(
            slide,
            str(PROJECT_ROOT / "_assets" / "qr-wcag-plain-english.png"),
            top=4.55,
            left=qr_img_left,
            width=qr_img_size,
            height=qr_img_size,
            alt_text="QR code vers WCAG in Plain English par AAArdvark",
        )
        add_texte_libre(
            slide,
            "WCAG 2.2 - Mise en FALC",
            top=5.88,
            left=qr_left,
            width=qr_w,
            height=0.22,
            size=11,
            bold=True,
            color=BLEU_FRANCE,
            align=PP_ALIGN.CENTER,
        )
        add_texte_libre(
            slide,
            "Scannez-moi !",
            top=6.10,
            left=qr_left,
            width=qr_w,
            height=0.20,
            size=10,
            bold=False,
            color=BLEU_FRANCE,
            align=PP_ALIGN.CENTER,
        )
        add_texte_libre(
            slide,
            "aaardvarkaccessibility.com/wcag-plain-english",
            top=6.30,
            left=qr_left,
            width=qr_w,
            height=0.18,
            size=8,
            bold=False,
            color=BLEU_FRANCE,
            align=PP_ALIGN.CENTER,
        )
        add_texte_libre(
            slide,
            "WCAG 2.2 Card Deck - Johannes Lehner - CC BY-SA 4.0",
            top=6.48,
            left=qr_left,
            width=qr_w,
            height=0.18,
            size=7,
            bold=False,
            color=BLEU_FRANCE,
            align=PP_ALIGN.CENTER,
        )
    else:
        add_callout(
            slide,
            "Le bon réflexe",
            [
                "Ne pas apprendre la liste par cœur.",
                "Savoir transformer un critère en question : "
                "que doit pouvoir faire la personne ?",
                "Chercher la preuve : exemple, capture, test clavier, "
                "mesure ou contenu corrigé.",
            ],
            top=4.65,
        )
    add_notes(
        slide,
        "D’après le W3C, WCAG 2.2 compte 13 lignes directrices organisées sous 4 principes. "
        "Les critères de succès déterminent la conformité.\n\n"
        "Sources :\n"
        "- AAArdvark, WCAG in Plain English : https://aaardvarkaccessibility.com/wcag-plain-english/\n"
        "- WCAG 2.2 Card Deck (Figma), Johannes Lehner, CC BY-SA 4.0 : "
        "https://www.figma.com/design/jz3JeECjm0KbH3Z2ztA2bv/WCAG-2.2-Card-Deck--Community-"
        "?node-id=191-244960&t=qOThv51tj0Arkga8-0",
    )


def slide_summary(ctx, fil_ariane="Mode d’emploi"):
    slide = ctx.slide(
        titre="Les 4 grandes questions",
        fil_ariane=fil_ariane,
        footer_suffix="Questions",
    )
    add_card_grid(
        slide,
        [
            ("Percevoir", "L’information reste disponible si je ne vois pas ou n’entends pas comme prévu."),
            ("Utiliser", "Je peux naviguer, agir et terminer sans piège ni geste imposé."),
            ("Comprendre", "Les mots, formulaires et comportements restent prévisibles."),
            ("Compatible", "Les aides techniques peuvent comprendre l’interface aujourd’hui et demain."),
        ],
        top=2.50,
    )
    add_notes(
        slide,
        "Faire reformuler les quatre questions par les participants. "
        "Insister sur le vocabulaire courant : percevoir, utiliser, comprendre, compatible.",
    )


def add_chapter(ctx, number, title, description=None):
    slide = ctx.slide(
        layout_name="chapitre",
        footer_suffix=title,
    )
    compose_chapitre(slide, number, title)
    if description:
        add_highlight(slide, description, top=5.15)
        add_notes(slide, f"Ouverture de section : {title}. Descriptif : {description}")
    else:
        add_notes(slide, f"Ouverture de section : {title}.")


def add_guideline_slides(ctx, guideline):
    chunks = [
        guideline.criteria[i:i + 4]
        for i in range(0, len(guideline.criteria), 4)
    ]
    for idx, chunk in enumerate(chunks, start=1):
        suffix = f" ({idx}/{len(chunks)})" if len(chunks) > 1 else ""
        slide = ctx.slide(
            titre=f"{guideline.code} - {guideline.title}{suffix}",
            fil_ariane=guideline.section,
            footer_suffix=guideline.code,
        )
        add_title_suffix(slide, guideline.question)
        cards = [
            (
                f"{item.code} {item.title}",
                item.plain,
            )
            for item in chunk
        ]
        add_card_grid(slide, cards, top=2.55)
        codes = ", ".join(item.code for item in chunk)
        add_notes(
            slide,
            f"Adaptation française de la page AAArdvark WCAG in Plain English pour les critères {codes}. "
            "Faire lire les cartes comme des questions de vérification avant publication.",
        )


def principle_title(section):
    if ". " in section:
        return section.split(". ", 1)[1]
    return section


def iter_principle_blocks():
    current_section = None
    current_criteria = []
    for guideline in GUIDELINES:
        if guideline.section != current_section:
            if current_section is not None:
                yield current_section, tuple(current_criteria)
            current_section = guideline.section
            current_criteria = []
        current_criteria.extend(guideline.criteria)
    if current_section is not None:
        yield current_section, tuple(current_criteria)


def condensed_criterion_title(criterion):
    return CARD_DECK_FR_TITLES.get(criterion.code, criterion.title).strip()


def add_condensed_title_card(slide, title, top, left, width, height):
    card = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left),
        Inches(top),
        Inches(width),
        Inches(height),
    )
    card.name = "DSFR-condensed-card"
    card.fill.solid()
    card.fill.fore_color.rgb = GRIS_CLAIR
    card.line.fill.background()
    card.shadow.inherit = False

    accent = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left),
        Inches(top),
        Inches(0.08),
        Inches(height),
    )
    accent.name = "DSFR-condensed-card-accent"
    accent.fill.solid()
    accent.fill.fore_color.rgb = BLEU_FRANCE
    accent.line.fill.background()
    accent.shadow.inherit = False

    size = 12
    if len(title) <= 34:
        size = 14
    elif len(title) <= 58:
        size = 13

    add_texte_libre(
        slide,
        title,
        top=top + 0.20,
        left=left + 0.26,
        width=width - 0.42,
        height=height - 0.40,
        size=size,
        bold=True,
        color=BLEU_FRANCE,
    )


def add_condensed_criterion_grid(slide, criteria, top=2.55):
    cols = 3
    rows = 2
    card_w = (CONTENT_W - GAP * (cols - 1)) / cols
    row_gap = 0.30
    card_h = (6.76 - top - row_gap) / rows
    for index, criterion in enumerate(criteria):
        row = index // cols
        col = index % cols
        left = MARGIN_L + col * (card_w + GAP)
        y = top + row * (card_h + row_gap)
        add_condensed_title_card(
            slide,
            condensed_criterion_title(criterion),
            top=y,
            left=left,
            width=card_w,
            height=card_h,
        )


def add_principle_criterion_slides(ctx, section, criteria, description=None):
    title = principle_title(section)
    chunks = [
        criteria[i:i + 6]
        for i in range(0, len(criteria), 6)
    ]
    for idx, chunk in enumerate(chunks, start=1):
        suffix = f" ({idx}/{len(chunks)})" if len(chunks) > 1 else ""
        slide = ctx.slide(
            titre=f"{title} - critères{suffix}",
            fil_ariane="Principes WCAG et critères condensés",
            footer_suffix=title,
        )
        if idx == 1 and description:
            add_title_suffix(slide, description)
        add_condensed_criterion_grid(slide, chunk)
        criterion_titles = ", ".join(condensed_criterion_title(item) for item in chunk)
        add_notes(
            slide,
            f"Version condensée inspirée du WCAG 2.2 Card Deck français : titres des critères, sans numérotation visible. "
            f"Critères couverts : {criterion_titles}.",
        )


def add_percevoir_description_slides(ctx, description=None):
    _add_description_slides(ctx, "Percevoir l'information", PERCEVOIR_CARDS, description)


def add_utiliser_description_slides(ctx, description=None):
    _add_description_slides(ctx, "Utiliser sans obstacle", UTILISER_CARDS, description)


def add_comprendre_description_slides(ctx, description=None):
    _add_description_slides(ctx, "Comprendre sans effort inutile", COMPRENDRE_CARDS, description)


def add_compatible_description_slides(ctx, description=None):
    _add_description_slides(ctx, "Rester compatible", COMPATIBLE_CARDS, description)


def _add_description_slides(ctx, title, cards, description=None):
    chunks = [
        cards[i:i + 4]
        for i in range(0, len(cards), 4)
    ]
    for idx, chunk in enumerate(chunks, start=1):
        suffix = f" ({idx}/{len(chunks)})" if len(chunks) > 1 else ""
        slide = ctx.slide(
            titre=f"{title} - critères{suffix}",
            fil_ariane="Principes WCAG et critères condensés",
            footer_suffix=title,
        )
        has_desc = idx == 1 and description
        if has_desc:
            add_title_suffix(slide, description)
        grid_top = 2.25 if has_desc else 2.15
        add_card_grid(slide, chunk, top=grid_top, strict=True)
        card_titles = ", ".join(t for t, _ in chunk)
        add_notes(
            slide,
            f"Descriptions inspirées du WCAG 2.2 Card Deck français. "
            f"Critères couverts : {card_titles}.",
        )


def slide_roles(ctx):
    slide = ctx.slide(
        titre="Qui doit agir ?",
        fil_ariane="Synthèse",
        footer_suffix="Rôles",
    )
    add_card_grid(
        slide,
        [
            ("Contenu", "Textes, images, médias, liens, titres, consignes, messages d’erreur."),
            ("Design", "Contrastes, taille des cibles, focus visible, organisation et lisibilité."),
            ("Technique", "Structure, clavier, formulaires, messages d’état et compatibilité."),
            ("Pilotage", "Arbitrer l’objectif visé, suivre les corrections, documenter les preuves."),
        ],
        top=2.45,
    )
    add_notes(
        slide,
        "Le but est d’éviter le renvoi de responsabilité. Chaque critère peut avoir un responsable principal, "
        "mais la conformité se construit en équipe.",
    )


def slide_exercise(ctx):
    slide = ctx.slide(
        titre="Exercice : traduire une règle",
        fil_ariane="Mise en pratique",
        footer_suffix="Exercice",
    )
    add_stepper(
        slide,
        [
            "Choisir une carte WCAG du deck",
            "Reformuler en question utilisateur",
            "Donner un exemple conforme et un contre-exemple",
            "Nommer la preuve à produire",
        ],
        top=2.35,
        height=1.75,
    )
    add_callout(
        slide,
        "Exemple de sortie attendue",
        [
            "Critère : 1.4.1 Couleur seule",
            "Question : puis-je comprendre le message sans voir la couleur ?",
            "Preuve : capture avec texte ou icône en plus de la couleur",
        ],
        top=4.65,
    )
    add_notes(
        slide,
        "Faire travailler en binômes. L’objectif n’est pas de citer le critère, mais de formuler une question "
        "qui aide à corriger un vrai contenu.",
    )


def slide_final_recap(ctx):
    slide = ctx.slide(
        titre="Les 3 réflexes à garder",
        fil_ariane="Synthèse",
        footer_suffix="Récapitulatif",
    )
    item_w = (CONTENT_W - GAP * 2) / 3
    kpis = [
        ("1", "Toujours demander : qui est bloqué si ce contenu disparaît ?"),
        ("2", "Tester sans souris, sans son, en zoom, avec erreur de formulaire."),
        ("3", "Documenter une preuve, pas seulement une intention."),
    ]
    for i, (value, label) in enumerate(kpis):
        add_pave_chiffre(
            slide,
            valeur=value,
            label=label,
            top=2.45,
            left=MARGIN_L + i * (item_w + GAP),
            width=item_w,
            height=1.85,
        )
    add_highlight(
        slide,
        "Une WCAG comprise est une règle que l’on peut expliquer à quelqu’un qui publie demain.",
        top=5.15,
    )
    add_notes(
        slide,
        "Conclusion pédagogique. Demander à chaque participant de choisir le réflexe qu’il appliquera "
        "sur sa prochaine publication.",
    )


def slide_sources(ctx):
    slide = ctx.slide(
        titre="Sources et licence",
        fil_ariane="Sources",
        footer_suffix="Sources",
    )
    add_tableau(
        slide,
        ["Source", "Rôle dans le support"],
        [
            [
                "AAArdvark - WCAG in Plain English",
                "Corpus principal adapté en français, licence CC BY-SA 4.0",
            ],
            [
                "WCAG 2.2 Card Deck - Johannes Lehner et contributeurs",
                "Inspiration cartes et libellés français, licence CC BY-SA 4.0",
            ],
            [
                "W3C/WAI - WCAG 2 Overview et WCAG 2.2",
                "Référence normative pour les principes, lignes directrices et critères",
            ],
            [
                "RGAA 4.1.2 - accessibilite.numerique.gouv.fr",
                "Cadre français de référence pour les services publics",
            ],
        ],
        top=2.35,
        col_widths=[4.8, 7.48],
        row_h=0.52,
    )
    add_alert(
        slide,
        "Attribution",
        [
            "Adaptation française : WCAG en langage clair.",
            "Sources : AAArdvark et WCAG 2.2 Card Deck.",
            "Licence des contenus dérivés : CC BY-SA 4.0.",
        ],
        top=5.00,
    )
    add_notes(
        slide,
        "AAArdvark WCAG in Plain English : https://aaardvarkaccessibility.com/wcag-plain-english/. "
        "WCAG 2.2 Card Deck : https://github.com/johanneslehner/wcag2.2-card-deck. "
        "Licence : https://creativecommons.org/licenses/by-sa/4.0/. "
        "W3C WCAG : https://www.w3.org/WAI/standards-guidelines/wcag/. "
        "RGAA : https://accessibilite.numerique.gouv.fr/methode/introduction/.",
    )


def build_deck(output=OUTPUT_DEFAULT, date=DATE_DEFAULT):
    prs, layouts = create_presentation()
    ctx = DeckContext(prs, layouts, date=date)

    slide_cover(ctx)
    slide_intention(ctx)
    slide_source(ctx)
    slide_structure(ctx)
    slide_summary(ctx)

    current_section = None
    chapter_number = 0
    for guideline in GUIDELINES:
        if guideline.section != current_section:
            current_section = guideline.section
            chapter_number += 1
            add_chapter(ctx, str(chapter_number), current_section)
        add_guideline_slides(ctx, guideline)

    slide_roles(ctx)
    slide_exercise(ctx)
    slide_final_recap(ctx)
    slide_sources(ctx)

    finalize_pptx(
        prs,
        str(output),
        title="WCAG en langage clair",
        author=AUTHOR,
        subject=(
            "Support de formation DSFR - adaptation française de "
            "WCAG in Plain English par AAArdvark"
        ),
    )
    return output, ctx.page_num


def build_condensed_deck(output=OUTPUT_CONDENSED, date=DATE_DEFAULT):
    prs, layouts = create_presentation()
    ctx = DeckContext(prs, layouts, date=date)
    fil = "Principes WCAG et critères condensés"

    slide_structure(ctx, fil_ariane=fil, qr_code=True)
    slide_summary(ctx, fil_ariane=fil)

    for _chapter_number, (section, criteria) in enumerate(iter_principle_blocks(), start=1):
        title = principle_title(section)
        description = PRINCIPLE_DESCRIPTIONS.get(title)
        if title == "Percevoir l’information":
            add_percevoir_description_slides(ctx, description=description)
        elif title == "Utiliser sans obstacle":
            add_utiliser_description_slides(ctx, description=description)
        elif title == "Comprendre sans effort inutile":
            add_comprendre_description_slides(ctx, description=description)
        elif title == "Rester compatible":
            add_compatible_description_slides(ctx, description=description)

    finalize_pptx(
        prs,
        str(output),
        title="WCAG en langage clair - condensé",
        author=AUTHOR,
        subject=(
            "Support de formation DSFR condensé - adaptation française de "
            "WCAG in Plain English par AAArdvark"
        ),
    )
    return output, ctx.page_num


def main():
    parser = argparse.ArgumentParser(
        description="Génère le deck WCAG en langage clair."
    )
    parser.add_argument(
        "--condensed",
        action="store_true",
        help="Générer la version condensée centrée sur les 4 principes.",
    )
    args = parser.parse_args()

    if args.condensed:
        output, slide_count = build_condensed_deck()
    else:
        output, slide_count = build_deck()
    print(f"[OK] {output.name} généré ({slide_count} slides)")


if __name__ == "__main__":
    main()
