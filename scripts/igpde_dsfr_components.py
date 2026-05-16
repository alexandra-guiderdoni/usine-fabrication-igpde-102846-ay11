"""Bibliotheque de composants DSFR pour le template IGPDE (13,33" x 7,5").

S'appuie sur les layouts natifs IGPDE (header logos + footer institut + ligne separatrice)
et injecte les composants DSFR dans la zone contenu (top=2.68" a 6.97").

Helpers disponibles :
- create_presentation()       charge le template IGPDE-DSFR
- new_slide(layout, titre)    nouvelle slide avec layout native IGPDE
- add_callout / add_alert / add_highlight / add_quote / add_card
- add_pave_chiffre (KPI)      / add_stepper / add_tableau / add_fleche
- add_texte_libre / add_notes / add_encadre
- finalize_pptx()             post-traitement a11y

Grille IGPDE-DSFR (13,33" x 7,5") :
  MARGIN_L = 0.52"    (marge gauche)
  CONTENT_W = 12.28"  (largeur utile)
  GAP = 0.33"
  COL_W = 5.98"       (colonne 50%)
  COL_R = 6.83"       (position colonne droite)
  TOP_CONTENT = 2.68" (debut zone contenu sous le titre)
  BOTTOM_CONTENT = 6.8"  (fin zone contenu au-dessus du footer)
"""

import math
from pathlib import Path
from copy import deepcopy

from pptx import Presentation
from pptx.util import Inches, Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from lxml import etree


# Namespaces OOXML
NSMAP_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NSMAP_A = "http://schemas.openxmlformats.org/drawingml/2006/main"


# ----------------------------------------------------------------------
# Palette DSFR
# ----------------------------------------------------------------------
BLEU_FRANCE = RGBColor(0x00, 0x00, 0x91)
BLEU_CLAIR = RGBColor(0xF5, 0xF5, 0xFE)
BLEU_MOYEN = RGBColor(0xE3, 0xE3, 0xFD)
ROUGE_MARIANNE = RGBColor(0xE1, 0x00, 0x0F)
BLANC = RGBColor(0xFF, 0xFF, 0xFF)
NOIR = RGBColor(0x16, 0x16, 0x16)
GRIS_FONCE = RGBColor(0x3A, 0x3A, 0x3A)
GRIS_CLAIR = RGBColor(0xF6, 0xF6, 0xF6)
GRIS_MENTION = RGBColor(0x66, 0x66, 0x66)

VERT_SUCCES = RGBColor(0x18, 0x75, 0x3C)
VERT_CLAIR = RGBColor(0xB8, 0xFE, 0xC9)
ORANGE_WARN = RGBColor(0xB3, 0x4E, 0x00)
ORANGE_CLAIR = RGBColor(0xFE, 0xE9, 0xE5)
ROUGE_ERREUR = RGBColor(0xCE, 0x05, 0x00)
ROUGE_CLAIR = RGBColor(0xFF, 0xE8, 0xE5)
BLEU_INFO = RGBColor(0x00, 0x63, 0xCB)
BLEU_INFO_CLAIR = RGBColor(0xE8, 0xED, 0xFF)


# ----------------------------------------------------------------------
# Grille IGPDE-DSFR (13,33" x 7,5")
# ----------------------------------------------------------------------
SLIDE_W = 13.3333
SLIDE_H = 7.5
MARGIN_L = 0.52
CONTENT_W = 12.28
GAP = 0.33
COL_W = (CONTENT_W - GAP) / 2          # ~5.975"
COL_R = MARGIN_L + COL_W + GAP         # ~6.825"
TOP_CONTENT = 2.68                     # debut zone contenu (sous titre)
TOP_CARDS = 2.45                       # debut zone cartes (gap serre au titre)
BOTTOM_CONTENT = 6.80                  # fin zone contenu (au-dessus footer)
FOOTER_Y = 6.98                        # y du footer IGPDE

# Layouts IGPDE (index dans le template)
LAYOUT_COUVERTURE = 0
LAYOUT_TITRE_SOUSTITRE = 1
LAYOUT_SOMMAIRE = 2
LAYOUT_CHAPITRE = 3
LAYOUT_3_COLONNES = 4
LAYOUT_TITRE_CONTENU = 5

PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATE_PATH = PROJECT_ROOT / "_source" / "presentations-source" / "PPT-IGPDE-DSFR-base-intervenant.pptx"


# ----------------------------------------------------------------------
# Utilitaires font / couleur
# ----------------------------------------------------------------------
def detect_font():
    """Marianne si installee, sinon Arial (police IGPDE native)."""
    try:
        import subprocess
        result = subprocess.run(
            ["fc-list", ":family"], capture_output=True, text=True, timeout=2
        )
        if "Marianne" in result.stdout:
            return "Marianne"
    except Exception:
        pass
    return "Arial"


FONT = detect_font()


def _apply_text(tf, texte, font=FONT, size=14, bold=False, italic=False,
                color=NOIR, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = Inches(0.08)
    tf.margin_right = Inches(0.08)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = 1.25
    p.text = ""
    run = p.add_run()
    run.text = str(texte)
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return p


def _plain_text(item):
    """Retourne le texte brut d'un item, y compris s'il est compose de segments riches."""
    if isinstance(item, (list, tuple)) and not isinstance(item, str):
        parts = []
        for segment in item:
            if isinstance(segment, (list, tuple)):
                parts.append(str(segment[0]))
            else:
                parts.append(str(segment))
        return "".join(parts)
    return str(item)


def _add_bullets(tf, items, font=FONT, size=14, color=NOIR, bold_first=False,
                  line_spacing=1.5, bullet_prefix="\u2022 "):
    tf.word_wrap = True
    tf.margin_left = Inches(0.08)
    tf.margin_right = Inches(0.08)
    tf.margin_top = Inches(0.05)
    tf.margin_bottom = Inches(0.05)
    # Vider le paragraphe par defaut
    p0 = tf.paragraphs[0]
    p0.text = ""
    for i, item in enumerate(items):
        if i == 0:
            p = p0
        else:
            p = tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = line_spacing
        segments = item if isinstance(item, (list, tuple)) and not isinstance(item, str) else [(item, False)]
        if bullet_prefix:
            run = p.add_run()
            run.text = bullet_prefix
            run.font.name = font
            run.font.size = Pt(size)
            run.font.color.rgb = color
        for segment in segments:
            if isinstance(segment, (list, tuple)):
                text = str(segment[0])
                is_bold = bool(segment[1]) if len(segment) > 1 else False
            else:
                text = str(segment)
                is_bold = False
            run = p.add_run()
            run.text = text
            run.font.name = font
            run.font.size = Pt(size)
            run.font.color.rgb = color
            run.font.bold = is_bold or (bold_first and i == 0)


# ----------------------------------------------------------------------
# Presentation et slides
# ----------------------------------------------------------------------
def create_presentation():
    """Charge le template IGPDE-DSFR. Retourne (prs, layouts_dict)."""
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(
            f"Template introuvable : {TEMPLATE_PATH}. "
            "Lancer d'abord scripts/build_template.py"
        )
    prs = Presentation(str(TEMPLATE_PATH))
    layouts = {
        "couverture": prs.slide_layouts[LAYOUT_COUVERTURE],
        "titre_soustitre": prs.slide_layouts[LAYOUT_TITRE_SOUSTITRE],
        "sommaire": prs.slide_layouts[LAYOUT_SOMMAIRE],
        "chapitre": prs.slide_layouts[LAYOUT_CHAPITRE],
        "3_colonnes": prs.slide_layouts[LAYOUT_3_COLONNES],
        "titre_contenu": prs.slide_layouts[LAYOUT_TITRE_CONTENU],
    }
    return prs, layouts


def _is_title_placeholder(ph):
    """Detecte le placeholder titre (Title 1 ou Titre X)."""
    name = (ph.name or "").lower()
    if name.startswith("title") or name.startswith("titre"):
        return True
    try:
        if ph.placeholder_format is not None and ph.placeholder_format.idx == 0:
            return True
    except Exception:
        pass
    return False


def _is_title_useless(ph):
    """Titre place en (0,0) avec taille minuscule -> inutilisable (Couverture, Titre-sous-titre)."""
    try:
        return (
            ph.top is not None
            and ph.left is not None
            and Emu(ph.top).inches < 0.1
            and Emu(ph.left).inches < 0.1
            and Emu(ph.width).inches < 0.5
        )
    except Exception:
        return False


def _reposition_shape(sp_element, left, top, width, height):
    """Repositionne un shape clone (element XML) aux coordonnees donnees (pouces)."""
    if sp_element is None:
        return
    xfrm = sp_element.find(".//{%s}xfrm" % NSMAP_A)
    if xfrm is None:
        # Creer xfrm dans spPr
        spPr = sp_element.find(".//{%s}spPr" % NSMAP_P)
        if spPr is None:
            return
        xfrm = etree.SubElement(spPr, "{%s}xfrm" % NSMAP_A)
    # off / ext
    off = xfrm.find("{%s}off" % NSMAP_A)
    if off is None:
        off = etree.SubElement(xfrm, "{%s}off" % NSMAP_A)
    off.set("x", str(int(Inches(left))))
    off.set("y", str(int(Inches(top))))
    ext = xfrm.find("{%s}ext" % NSMAP_A)
    if ext is None:
        ext = etree.SubElement(xfrm, "{%s}ext" % NSMAP_A)
    ext.set("cx", str(int(Inches(width))))
    ext.set("cy", str(int(Inches(height))))


def _add_footer_line(slide):
    """Ajoute la ligne separatrice IGPDE au-dessus du footer (y=6.97")."""
    line = slide.shapes.add_connector(
        1,  # MSO_CONNECTOR.STRAIGHT
        Inches(MARGIN_L), Inches(FOOTER_Y - 0.01),
        Inches(MARGIN_L + CONTENT_W), Inches(FOOTER_Y - 0.01),
    )
    line.name = "IGPDE-footer-ligne-decoratif"
    line.line.color.rgb = RGBColor(0x99, 0x99, 0x99)
    line.line.width = Pt(0.5)
    return line


def _clone_layout_placeholder(slide, layout_ph, text_override=None):
    """Copie un placeholder du layout dans la slide (via clonage XML).

    Utilise quand le placeholder (date, pied de page, n°) existe seulement
    dans le layout et doit apparaitre dans la slide pour s'afficher.
    """
    # Verifier qu'un placeholder avec meme idx n'existe pas deja dans la slide
    try:
        layout_idx = layout_ph.placeholder_format.idx
        for sph in slide.placeholders:
            try:
                if sph.placeholder_format.idx == layout_idx:
                    return None
            except Exception:
                continue
    except Exception:
        pass

    sp_clone = deepcopy(layout_ph._element)
    slide.shapes._spTree.append(sp_clone)
    # Si un text override est fourni, l'appliquer
    if text_override is not None:
        # Retrouver le placeholder clone via slide.placeholders
        for sph in slide.placeholders:
            if sph._element is sp_clone and sph.has_text_frame:
                _apply_text(sph.text_frame, text_override, font=FONT, size=10,
                            bold=False, color=GRIS_MENTION)
                break
    return sp_clone


def new_slide(prs, layouts, layout_name="titre_contenu", titre=None,
              fil_ariane=None, footer_text=None, date_text=None,
              page_num=None):
    """Cree une slide a partir d'un layout IGPDE natif.

    - Recopie les placeholders date/pied de page/n° depuis le layout pour affichage
    - Remplit le titre dans la bonne zone selon le layout :
        * couverture / titre_soustitre : textbox DSFR en zone utile (titre 0,26" inutile)
        * autres layouts : placeholder Title natif
    - Remplit le fil d'Ariane (aligne a droite, pos y<0.5") si fourni
    - Supprime les placeholders de contenu (texte de niveau N, cartes) non utilises
    """
    if layout_name not in layouts:
        raise ValueError(f"Layout inconnu : {layout_name}. Choix : {list(layouts)}")
    layout = layouts[layout_name]
    slide = prs.slides.add_slide(layout)

    # 1. Copier date / pied de page / n° diapo depuis le layout vers la slide
    #    Pour la couverture, le layout IGPDE natif place le pied de page au milieu
    #    de la slide - on repositionne aux coordonnees standard IGPDE (y=6.98")
    cloned_date = None
    cloned_footer = None
    cloned_num = None
    for layout_ph in layout.placeholders:
        name_low = (layout_ph.name or "").lower()
        if "date" in name_low:
            cloned_date = _clone_layout_placeholder(
                slide, layout_ph, text_override=date_text or "")
        elif "pied de page" in name_low:
            default_footer = ("Institut de la Gestion publique "
                              "et du Développement économique")
            cloned_footer = _clone_layout_placeholder(
                slide, layout_ph,
                text_override=footer_text or default_footer)
        elif "numero" in name_low or "num\u00e9ro" in name_low:
            cloned_num = _clone_layout_placeholder(
                slide, layout_ph,
                text_override=str(page_num) if page_num else None)

    # Pour la couverture : forcer les placeholders footer aux positions standard IGPDE
    if layout_name == "couverture":
        _reposition_shape(cloned_footer, left=MARGIN_L, top=FOOTER_Y,
                          width=8.61, height=0.52)
        _reposition_shape(cloned_date, left=11.10, top=FOOTER_Y,
                          width=1.71, height=0.52)
        _reposition_shape(cloned_num, left=9.13, top=FOOTER_Y,
                          width=1.97, height=0.52)
        # Ajouter la ligne separatrice (presente dans les autres layouts)
        _add_footer_line(slide)

    # 2. Parcourir les placeholders de la slide pour titre, fil d'Ariane, nettoyage
    titre_pose = False
    fil_pose = False
    a_supprimer = []
    for ph in slide.placeholders:
        name = ph.name or ""
        is_title = _is_title_placeholder(ph)
        # Titre "utile" (grande zone visible) : ecrire dedans
        if is_title and not _is_title_useless(ph):
            if titre and not titre_pose and ph.has_text_frame:
                # Resserrer le placeholder titre : le layout IGPDE pose un box
                # de ~1,5" de haut a top=1,31" qui laisse ~1" de vide sous le
                # texte du titre. On le reduit a 1,05" de haut a top=1,15",
                # ce qui rapproche le bas du titre de y=2,20" (contre 2,81"
                # avant). Les composants de contenu peuvent alors commencer
                # plus haut sans chevaucher le titre (supporte 1 a 2 lignes).
                #
                # Important : python-pptx ecrit un <a:xfrm> sur le shape des
                # qu'une dimension est modifiee, mais les dimensions non
                # setees tombent a 0 au lieu d'heriter du layout. Il faut
                # donc copier les 4 dimensions explicitement.
                try:
                    current_left = ph.left
                    current_width = ph.width
                    ph.top = Inches(1.15)
                    ph.left = current_left
                    ph.width = current_width
                    ph.height = Inches(1.05)
                except Exception:
                    pass
                _apply_text(ph.text_frame, titre, font=FONT, size=28, bold=True,
                            color=BLEU_FRANCE)
                titre_pose = True
            continue
        # Titre "inutile" (0.26" x 0.26") : le supprimer pour eviter affichage vertical
        if is_title and _is_title_useless(ph):
            a_supprimer.append(ph)
            continue
        # Fil d'Ariane : placeholder texte en haut (y < 0.5")
        if not fil_pose and fil_ariane and ph.has_text_frame:
            try:
                if ph.top is not None and Emu(ph.top).inches < 0.5:
                    tf = ph.text_frame
                    _apply_text(tf, fil_ariane, font=FONT, size=11,
                                bold=False, color=GRIS_MENTION, align=PP_ALIGN.RIGHT)
                    # Neutraliser la numerotation automatique heritee du layout
                    # (lstStyle > lvl1pPr > buAutoNum type="arabicPeriod") qui,
                    # sans cette neutralisation, affiche « 1. » en prefixe du fil
                    # d'Ariane et donne « 1.3. points de contrôle rapides | ... » au rendu.
                    _neutralize_auto_numbering(tf._txBody)
                    fil_pose = True
                    continue
            except Exception:
                pass
        # Preserver les placeholders date/ftr/sldNum qu'on vient de cloner
        low = name.lower()
        if ("date" in low or "pied de page" in low
                or "numero" in low or "num\u00e9ro" in low):
            continue
        # Tout autre placeholder (Text/Content) : retirer
        a_supprimer.append(ph)

    for ph in a_supprimer:
        sp = ph._element
        sp.getparent().remove(sp)

    # 3. Pour couverture/titre_soustitre : poser le titre en textbox DSFR
    #    dans la zone utile (car le placeholder Title etait inutilisable)
    if titre and not titre_pose:
        if layout_name == "couverture":
            # Pied de page IGPDE a (1.05, 5.72) size 4.72x1.31 -> occupe la moitie gauche basse.
            # Logo secondaire a (8.94, 0.85) size 3.43x3.43 -> finit a y=4.28.
            # Zone titre : moitie droite au-dessus du pied de page (x=5.8, y=4.5)
            t_box = slide.shapes.add_textbox(
                Inches(5.8), Inches(4.5),
                Inches(7.1), Inches(1.3),
            )
            t_box.name = "Title-DSFR-couverture"
            _apply_text(t_box.text_frame, titre, font=FONT, size=32, bold=True,
                        color=BLEU_FRANCE, align=PP_ALIGN.RIGHT)
        elif layout_name == "titre_soustitre":
            # Titre remonte pour laisser la zone de contenu libre en dessous
            t_box = slide.shapes.add_textbox(
                Inches(MARGIN_L), Inches(2.5),
                Inches(CONTENT_W), Inches(1.1),
            )
            t_box.name = "Title-DSFR-soustitre"
            _apply_text(t_box.text_frame, titre, font=FONT, size=36, bold=True,
                        color=BLEU_FRANCE, align=PP_ALIGN.LEFT)

    return slide


def add_notes(slide, texte, lang="fr-FR"):
    """Ajoute des notes presentateur en francais (lang=fr-FR par defaut).

    Le texte est decoupe automatiquement : une phrase par paragraphe, pour
    une lecture plus rapide en mode orateur. La decoupe se fait sur toute
    ponctuation finale (. ? ! ...) suivie d'un espace et d'une majuscule
    francaise ou d'un guillemet francais.

    python-pptx cree un run nu via tf.text=..., sans attribut <a:rPr lang>.
    Sans cet attribut, PowerPoint et les lecteurs d'ecran interpretent le
    texte selon la langue systeme (souvent en-US), ce qui produit un
    soulignement rouge du correcteur et une lecture avec accent anglais.
    On pose donc lang=fr-FR sur chaque run des notes des la creation.
    """
    import re
    # Une phrase par ligne : split sur ponctuation finale + espace + majuscule/guillemet
    phrases = re.split(r'(?<=[.!?…])\s+(?=[A-ZÀ-Ÿ«"])', texte.strip())
    phrases = [p.strip() for p in phrases if p.strip()]

    notes = slide.notes_slide
    tf = notes.notes_text_frame
    # Nettoyer le text frame et poser la premiere phrase
    tf.text = phrases[0] if phrases else ""
    for phrase in phrases[1:]:
        p = tf.add_paragraph()
        p.text = phrase
    # Filet de securite : lang=fr-FR sur chaque run
    _set_lang_on_runs(tf._txBody, lang=lang)


# ----------------------------------------------------------------------
# Briques de base
# ----------------------------------------------------------------------
def _safe_top(top, height, component="composant"):
    """Remonte le top si le composant deborderait sur le footer.

    Empeche silencieusement tout debordement au-dela de BOTTOM_CONTENT.
    Affiche un avertissement console pour signaler les slides a corriger.
    """
    if top + height > BOTTOM_CONTENT:
        import sys
        safe = round(BOTTOM_CONTENT - height, 3)
        print(
            f"[WARN footer] {component} : top={top:.2f} + h={height:.2f}"
            f" = {top + height:.2f} > {BOTTOM_CONTENT} - remonte a top={safe}",
            file=sys.stderr,
        )
        return max(safe, 2.3)
    return top


def _estimate_height(content, available_width, size=11, line_height_mult=1.35):
    """Estime la hauteur (pouces) necessaire pour afficher un contenu.

    - content : str (1 texte) ou list[str] (bullets)
    - available_width : largeur utile en pouces APRES padding interne
    - size : taille police en pt (14 pour bullets/contenu, 18 pour highlight)
    - line_height_mult : multiplicateur d'interligne (1,35 = marge de securite)

    Heuristique empirique recalibree : Marianne a 14pt tient ~8,5
    caracteres par pouce (mesure sur PPTX reel). Base 9,0 avec
    scaling lineaire pour marge de securite.
    """
    if content is None:
        return 0.0
    items = [content] if isinstance(content, str) else list(content)
    chars_per_inch = 9.0 * (11.0 / size)
    chars_per_line = max(8, int(available_width * chars_per_inch))
    line_height_inches = (size / 72.0) * line_height_mult
    total_lines = 0
    for item in items:
        if item is None:
            continue
        for segment in _plain_text(item).split("\n"):
            n = max(1, math.ceil(len(segment) / chars_per_line))
            total_lines += n
    return total_lines * line_height_inches


def estimate_callout_height(titre, bullets, width=None, line_spacing=1.5):
    """Hauteur auto d'un callout ou d'une alert (meme formule)."""
    if width is None:
        width = CONTENT_W
    h_titre = 0.55 if titre else 0.15
    adjusted_lhm = 1.35 * (line_spacing / 1.25)
    h_body = _estimate_height(bullets, width - 0.5, size=14, line_height_mult=adjusted_lhm)
    return max(h_titre + h_body + 0.25, 0.90)


# Alias pour les alerts (meme structure que callout)
estimate_alert_height = estimate_callout_height


def estimate_highlight_height(texte, width=None):
    """Hauteur auto d'un highlight."""
    if width is None:
        width = CONTENT_W
    h_text = _estimate_height(texte, width - 0.4, size=18)
    return max(h_text + 0.3, 0.70)


def estimate_quote_height(texte, auteur="", width=None):
    """Hauteur auto d'une quote."""
    if width is None:
        width = CONTENT_W
    h_text = _estimate_height(texte, width - 0.4, size=16)
    h_auteur = 0.50 if auteur else 0
    return max(h_text + h_auteur + 0.30, 0.90)


class Stack:
    """Curseur vertical qui empile les composants avec un gap constant.

    Usage dans une slide :
        stack = Stack(top=2.30, gap=0.30)
        add_highlight(slide, "Texte", top=stack.push(estimate_highlight_height("Texte")))
        add_callout(slide, "Titre", bullets, top=stack.push(estimate_callout_height("Titre", bullets)))

    `push(h)` renvoie le top courant et avance le curseur de (h + gap).
    """

    def __init__(self, top=2.30, gap=0.30):
        self._cursor = float(top)
        self._gap = float(gap)

    def push(self, height):
        t = self._cursor
        self._cursor += float(height) + self._gap
        return round(t, 3)

    @property
    def cursor(self):
        return self._cursor


def estimate_card_height(titre, contenu, width, numero=None):
    """Estime la hauteur necessaire pour une carte DSFR (helper public).

    A utiliser dans une slide qui dispose plusieurs cartes cote a cote :
    calculer `max(estimate_card_height(...) for carte in cartes)` puis
    passer cette valeur a `add_card(height=...)` pour toutes les cartes.
    Assure un alignement visuel uniforme sans debordement.
    """
    h_numero = 0.80 if numero is not None else 0.0
    h_titre = 0.50 if titre else 0.15
    h_body = _estimate_height(contenu, width - 0.5, size=14)
    h_padding = 0.30
    return max(h_numero + h_titre + h_body + h_padding, 1.0)


def _make_box(slide, top, left, width, height, fill_color,
              accent_color=None, accent_w=0.08, border_color=None):
    """Rectangle DSFR : fond couleur, accent gauche optionnel."""
    # Accent vertical
    if accent_color is not None and accent_w > 0:
        accent = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(left), Inches(top),
            Inches(accent_w), Inches(height),
        )
        accent.name = "DSFR-accent-decoratif"
        accent.fill.solid()
        accent.fill.fore_color.rgb = accent_color
        accent.line.fill.background()
        accent.shadow.inherit = False
    # Fond
    box = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left + accent_w), Inches(top),
        Inches(width - accent_w), Inches(height),
    )
    box.name = "DSFR-box"
    box.fill.solid()
    box.fill.fore_color.rgb = fill_color
    if border_color:
        box.line.color.rgb = border_color
        box.line.width = Pt(0.5)
    else:
        box.line.fill.background()
    box.shadow.inherit = False
    return box


# ----------------------------------------------------------------------
# Composants DSFR
# ----------------------------------------------------------------------
def add_callout(slide, titre, bullets, top, left=MARGIN_L, width=CONTENT_W, height=None,
                line_spacing=1.25, bullet_prefix="\u2022 "):
    """Callout bleu : accent gauche Bleu France + fond bleu clair + titre bold + bullets.

    La hauteur est calculee automatiquement a partir du contenu (titre +
    bullets). Le parametre `height`, s'il est passe, sert de minimum :
    la hauteur finale est `max(height, auto)` pour garantir l'absence
    de debordement.
    """
    # Calcul auto TOUJOURS : le parametre height est ignore pour harmoniser
    # le rendu (ni vide a la fin, ni debordement). Pour forcer une hauteur
    # specifique (alignement entre plusieurs composants), utiliser add_card
    # qui respecte max(height, auto).
    h_titre_box = max(_estimate_height(titre, width - 0.35, size=14), 0.35) if titre else 0
    h_titre = (0.10 + h_titre_box + 0.10) if titre else 0.15
    adjusted_lhm = 1.35 * (line_spacing / 1.25)
    h_body = _estimate_height(bullets, width - 0.5, size=14, line_height_mult=adjusted_lhm)
    h_padding = 0.25
    height = max(h_titre + h_body + h_padding, 0.90)
    top = _safe_top(top, height, "add_callout")

    _make_box(slide, top, left, width, height,
              fill_color=BLEU_CLAIR, accent_color=BLEU_FRANCE, accent_w=0.08)
    # Titre
    if titre:
        t_box = slide.shapes.add_textbox(
            Inches(left + 0.25), Inches(top + 0.10),
            Inches(width - 0.35), Inches(h_titre_box),
        )
        t_box.name = "DSFR-callout-titre"
        _apply_text(t_box.text_frame, titre, font=FONT, size=14, bold=True,
                    color=BLEU_FRANCE)
    # Bullets
    if bullets:
        body_top = (top + h_titre) if titre else (top + 0.15)
        body_h = height - (h_titre + 0.10 if titre else 0.25)
        b_box = slide.shapes.add_textbox(
            Inches(left + 0.25), Inches(body_top),
            Inches(width - 0.35), Inches(body_h),
        )
        b_box.name = "DSFR-callout-body"
        _add_bullets(b_box.text_frame, bullets, font=FONT, size=14, color=NOIR,
                     line_spacing=line_spacing, bullet_prefix=bullet_prefix)
    return slide


def add_alert(slide, titre, bullets, top, left=MARGIN_L, width=CONTENT_W, height=None,
              alert_type="info", line_spacing=1.5):
    """Alerte DSFR - rendu uniformise en gris/bleu DSFR.

    Le parametre alert_type (success, warning, error, info) est conserve
    pour la compatibilite mais n'affecte plus les couleurs : toutes les
    alertes utilisent fond gris clair + accent Bleu France DSFR, distinct
    du callout (fond bleu clair) par la seule teinte du fond. Choix adopte
    pour homogeneiser le rendu : pas de rouge / vert / orange dans le deck.

    Hauteur calculee automatiquement a partir du contenu.
    """
    # Palette unifiee : gris clair + accent Bleu France pour toutes les alerts
    fond, accent = GRIS_CLAIR, BLEU_FRANCE
    # Calcul auto TOUJOURS (voir add_callout pour le rationnel)
    h_titre_box = max(_estimate_height(titre, width - 0.35, size=14), 0.35) if titre else 0
    h_titre = (0.10 + h_titre_box + 0.10) if titre else 0.15
    adjusted_lhm = 1.35 * (line_spacing / 1.25)
    h_body = _estimate_height(bullets, width - 0.5, size=14, line_height_mult=adjusted_lhm)
    h_padding = 0.25
    height = max(h_titre + h_body + h_padding, 0.90)
    top = _safe_top(top, height, "add_alert")
    _make_box(slide, top, left, width, height,
              fill_color=fond, accent_color=accent, accent_w=0.08)
    if titre:
        t_box = slide.shapes.add_textbox(
            Inches(left + 0.25), Inches(top + 0.10),
            Inches(width - 0.35), Inches(h_titre_box),
        )
        t_box.name = f"DSFR-alert-{alert_type}-titre"
        _apply_text(t_box.text_frame, titre, font=FONT, size=14, bold=True,
                    color=accent)
    if bullets:
        body_top = (top + h_titre) if titre else (top + 0.15)
        body_h = height - (h_titre + 0.10 if titre else 0.25)
        b_box = slide.shapes.add_textbox(
            Inches(left + 0.25), Inches(body_top),
            Inches(width - 0.35), Inches(body_h),
        )
        b_box.name = f"DSFR-alert-{alert_type}-body"
        _add_bullets(b_box.text_frame, bullets, font=FONT, size=14, color=NOIR,
                     line_spacing=line_spacing)
    return slide


def add_highlight(slide, texte, top, left=MARGIN_L, width=CONTENT_W, height=None, url=None):
    """Highlight : accent bleu gauche + texte emphase 18pt.

    Hauteur calculee automatiquement a partir du texte (ignore `height`
    sauf si passe explicitement et superieur).
    Si `url` est fourni, le texte devient un lien cliquable.
    """
    h_text = _estimate_height(texte, width - 0.4, size=18)
    # Calcul auto TOUJOURS
    height = max(h_text + 0.3, 0.70)
    top = _safe_top(top, height, "add_highlight")
    _make_box(slide, top, left, width, height,
              fill_color=GRIS_CLAIR, accent_color=BLEU_FRANCE, accent_w=0.08)
    t_box = slide.shapes.add_textbox(
        Inches(left + 0.3), Inches(top + 0.1),
        Inches(width - 0.4), Inches(height - 0.2),
    )
    t_box.name = "DSFR-highlight"
    lines = str(texte).split('\n')
    p = _apply_text(t_box.text_frame, lines[0], font=FONT, size=18, bold=True,
                    color=BLEU_FRANCE, anchor=MSO_ANCHOR.MIDDLE)
    for line in lines[1:]:
        new_p = t_box.text_frame.add_paragraph()
        run = new_p.add_run()
        run.text = line
        run.font.name = FONT
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = BLEU_FRANCE
    if url:
        run = p.runs[0]
        run.font.bold = False
        run.font.underline = True
        rId = slide.part.relate_to(
            url,
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
            is_external=True,
        )
        rPr = run._r.get_or_add_rPr()
        hlinkClick = etree.SubElement(
            rPr,
            f"{{{NSMAP_A}}}hlinkClick",
            {"{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id": rId},
        )
    return slide


def add_quote(slide, texte, auteur="", top=TOP_CONTENT, left=MARGIN_L,
              width=CONTENT_W, height=None):
    """Citation italique + auteur. Hauteur calculee automatiquement."""
    h_text = _estimate_height(texte, width - 0.4, size=16)
    h_auteur = 0.50 if auteur else 0
    auto_h = max(h_text + h_auteur + 0.30, 0.90)
    height = max(height, auto_h) if height is not None else auto_h
    _make_box(slide, top, left, width, height,
              fill_color=BLEU_CLAIR, accent_color=BLEU_FRANCE, accent_w=0.08)
    t_box = slide.shapes.add_textbox(
        Inches(left + 0.3), Inches(top + 0.15),
        Inches(width - 0.4), Inches(height - (0.6 if auteur else 0.3)),
    )
    t_box.name = "DSFR-quote-texte"
    segments = str(texte).split("\n")
    _apply_text(t_box.text_frame, segments[0], font=FONT, size=16,
                italic=True, color=NOIR)
    for seg in segments[1:]:
        p = t_box.text_frame.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = 1.25
        run = p.add_run()
        run.text = seg
        run.font.name = FONT
        run.font.size = Pt(16)
        run.font.italic = True
        run.font.color.rgb = NOIR
    if auteur:
        a_box = slide.shapes.add_textbox(
            Inches(left + 0.3), Inches(top + height - 0.5),
            Inches(width - 0.4), Inches(0.4),
        )
        a_box.name = "DSFR-quote-auteur"
        _apply_text(a_box.text_frame, auteur, font=FONT, size=14,
                    bold=True, color=BLEU_FRANCE)
    return slide


def add_card(slide, titre, contenu, top, left, width=3.78, height=None,
             numero=None, title_size=14, body_size=14):
    """Carte DSFR : accent bleu + fond gris clair + titre + contenu.

    Si numero est fourni (1, 2, 3...), affiche une pastille ronde bleue en haut.

    Hauteur : si None, calcul auto. Si passe, prend max(passe, auto) pour
    garantir l'absence de debordement tout en respectant une hauteur
    imposee (utile pour aligner plusieurs cartes cote a cote).
    """
    auto_h = estimate_card_height(titre, contenu, width, numero)
    height = auto_h if height is None else height
    _make_box(slide, top, left, width, height,
              fill_color=GRIS_CLAIR, accent_color=BLEU_FRANCE, accent_w=0.08)
    y_titre = top + 0.15
    if numero is not None:
        pastille = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(left + 0.25), Inches(top + 0.15),
            Inches(0.5), Inches(0.5),
        )
        pastille.name = "DSFR-card-numero"
        pastille.fill.solid()
        pastille.fill.fore_color.rgb = BLEU_FRANCE
        pastille.line.fill.background()
        pastille.shadow.inherit = False
        _apply_text(pastille.text_frame, str(numero), font=FONT, size=16,
                    bold=True, color=BLANC, align=PP_ALIGN.CENTER,
                    anchor=MSO_ANCHOR.MIDDLE)
        y_titre = top + 0.75
    title_h = 0.35 if title_size <= 12 else 0.45
    t_box = slide.shapes.add_textbox(
        Inches(left + 0.25), Inches(y_titre),
        Inches(width - 0.4), Inches(title_h),
    )
    t_box.name = "DSFR-card-titre"
    _apply_text(t_box.text_frame, titre, font=FONT, size=title_size, bold=True,
                color=BLEU_FRANCE)
    if contenu:
        c_top = y_titre + title_h + 0.05
        c_box = slide.shapes.add_textbox(
            Inches(left + 0.25), Inches(c_top),
            Inches(width - 0.4), Inches(height - (c_top - top) - 0.10),
        )
        c_box.name = "DSFR-card-contenu"
        if isinstance(contenu, list):
            _add_bullets(c_box.text_frame, contenu, font=FONT, size=body_size, color=NOIR)
        else:
            _apply_text(c_box.text_frame, contenu, font=FONT, size=body_size, color=NOIR)
    return slide


def add_pave_chiffre(slide, valeur, label, top, left, width=3.78, height=1.5):
    """KPI pave : valeur 36pt blanc sur bleu + label en-dessous."""
    pave = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        Inches(left), Inches(top),
        Inches(width), Inches(height * 0.65),
    )
    pave.name = "DSFR-kpi-pave"
    pave.fill.solid()
    pave.fill.fore_color.rgb = BLEU_FRANCE
    pave.line.fill.background()
    pave.shadow.inherit = False
    _apply_text(pave.text_frame, str(valeur), font=FONT, size=32, bold=True,
                color=BLANC, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    # Label
    l_box = slide.shapes.add_textbox(
        Inches(left), Inches(top + height * 0.7),
        Inches(width), Inches(height * 0.3),
    )
    l_box.name = "DSFR-kpi-label"
    _apply_text(l_box.text_frame, label, font=FONT, size=14, bold=False,
                color=NOIR, align=PP_ALIGN.CENTER)
    return slide


def add_stepper(slide, etapes, top, left=MARGIN_L, width=CONTENT_W, height=2.5):
    """Stepper : pastilles numerotees + texte sous chaque pastille."""
    n = len(etapes)
    if n == 0:
        return slide
    item_w = (width - GAP * (n - 1)) / n
    pastille_size = 0.7
    for i, etape in enumerate(etapes):
        x = left + i * (item_w + GAP)
        # Pastille
        pastille = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            Inches(x + (item_w - pastille_size) / 2), Inches(top),
            Inches(pastille_size), Inches(pastille_size),
        )
        pastille.name = f"DSFR-stepper-pastille-{i+1}"
        pastille.fill.solid()
        pastille.fill.fore_color.rgb = BLEU_FRANCE
        pastille.line.fill.background()
        pastille.shadow.inherit = False
        _apply_text(pastille.text_frame, str(i + 1), font=FONT, size=18, bold=True,
                    color=BLANC, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        # Ligne de connexion entre pastilles
        if i < n - 1:
            line = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(x + (item_w + pastille_size) / 2),
                Inches(top + pastille_size / 2 - 0.02),
                Inches(item_w + GAP - pastille_size),
                Inches(0.04),
            )
            line.name = f"DSFR-stepper-connecteur-{i+1}-decoratif"
            line.fill.solid()
            line.fill.fore_color.rgb = BLEU_MOYEN
            line.line.fill.background()
            line.shadow.inherit = False
        # Texte etape
        t_box = slide.shapes.add_textbox(
            Inches(x), Inches(top + pastille_size + 0.1),
            Inches(item_w), Inches(height - pastille_size - 0.1),
        )
        t_box.name = f"DSFR-stepper-texte-{i+1}"
        _apply_text(t_box.text_frame, etape, font=FONT, size=14, bold=False,
                    color=NOIR, align=PP_ALIGN.CENTER)
    return slide


def add_tableau(slide, headers, rows, top, left=MARGIN_L, width=CONTENT_W,
                col_widths=None, row_h=0.45):
    """Tableau DSFR : en-tetes bleu fonce + lignes alternees."""
    ncols = len(headers)
    nrows = len(rows) + 1
    if col_widths is None:
        col_widths = [width / ncols] * ncols
    table_shape = slide.shapes.add_table(
        nrows, ncols,
        Inches(left), Inches(top),
        Inches(width), Inches(row_h * nrows),
    )
    tbl = table_shape.table
    tbl.name = "DSFR-tableau"
    # Largeurs colonnes
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = Inches(w)
    # Hauteur lignes
    for r in range(nrows):
        tbl.rows[r].height = Inches(row_h)
    # En-tetes
    for c, h in enumerate(headers):
        cell = tbl.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = BLEU_FRANCE
        cell.margin_left = Inches(0.1)
        cell.margin_right = Inches(0.1)
        cell.margin_top = Inches(0.05)
        cell.margin_bottom = Inches(0.05)
        tf = cell.text_frame
        _apply_text(tf, h, font=FONT, size=14, bold=True, color=BLANC,
                    anchor=MSO_ANCHOR.MIDDLE)
    # Corps
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = tbl.cell(r + 1, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BLANC if r % 2 == 0 else BLEU_CLAIR
            cell.margin_left = Inches(0.1)
            cell.margin_right = Inches(0.1)
            cell.margin_top = Inches(0.05)
            cell.margin_bottom = Inches(0.05)
            tf = cell.text_frame
            _apply_text(tf, val, font=FONT, size=14, color=NOIR,
                        anchor=MSO_ANCHOR.MIDDLE)
    # Marquer la premiere ligne comme header (a11y)
    tblPr = tbl._tbl.find(".//{http://schemas.openxmlformats.org/drawingml/2006/main}tblPr")
    if tblPr is not None:
        tblPr.set("firstRow", "1")
        tblPr.set("bandRow", "1")
    return Emu(table_shape.height).inches


def add_texte_libre(slide, texte, top, left=MARGIN_L, width=CONTENT_W,
                    height=0.6, size=14, bold=False, color=NOIR,
                    align=PP_ALIGN.LEFT):
    """Zone de texte positionnee librement."""
    box = slide.shapes.add_textbox(
        Inches(left), Inches(top),
        Inches(width), Inches(height),
    )
    box.name = "DSFR-texte-libre"
    _apply_text(box.text_frame, texte, font=FONT, size=size, bold=bold,
                color=color, align=align)
    return slide


def add_image(slide, image_path, top, left, width, height=None, alt_text=""):
    """Image positionnee librement avec alt text accessible."""
    from pathlib import Path
    img_path = Path(image_path)
    if not img_path.is_absolute():
        img_path = PROJECT_ROOT / img_path
    kwargs = {"width": Inches(width)}
    if height is not None:
        kwargs["height"] = Inches(height)
    pic = slide.shapes.add_picture(
        str(img_path), Inches(left), Inches(top), **kwargs,
    )
    if alt_text:
        pic._element.find(
            ".//{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr"
        ).set("descr", alt_text)
    else:
        pic.name = "DSFR-image-decoratif"
    return pic


def _set_run_hyperlink(slide, run, url):
    """Ajoute un lien cliquable sur un run de texte."""
    run.font.underline = True
    rId = slide.part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    rPr = run._r.get_or_add_rPr()
    hlinkClick = etree.SubElement(
        rPr,
        f"{{{NSMAP_A}}}hlinkClick",
        {"{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id": rId},
    )
    return hlinkClick


def add_qrcode(slide, image_path, url, top, left, size=1.10,
               label=None, label_width=2.80, label_position="right"):
    """QR code imprime avec alternative visible : CTA + URL lisible."""
    pic = add_image(
        slide,
        image_path,
        top=top,
        left=left,
        width=size,
        height=size,
        alt_text=f"QR code : {url}",
    )
    pic.name = "DSFR-qrcode"

    label = label or url
    gap = 0.14
    if label_position == "left":
        text_left = left - label_width - gap
    else:
        text_left = left + size + gap

    cta_box = slide.shapes.add_textbox(
        Inches(text_left), Inches(top + 0.08),
        Inches(label_width), Inches(0.28),
    )
    cta_box.name = "DSFR-qrcode-cta"
    _apply_text(
        cta_box.text_frame,
        "Scannez-moi !",
        font=FONT,
        size=11,
        bold=True,
        color=BLEU_FRANCE,
    )

    url_box = slide.shapes.add_textbox(
        Inches(text_left), Inches(top + 0.40),
        Inches(label_width), Inches(max(size - 0.30, 0.55)),
    )
    url_box.name = "DSFR-qrcode-url-visible"
    p = _apply_text(
        url_box.text_frame,
        label,
        font=FONT,
        size=8.5,
        bold=False,
        color=BLEU_FRANCE,
    )
    if p.runs:
        _set_run_hyperlink(slide, p.runs[0], url)

    return pic


def add_fleche(slide, top, left, width=0.8):
    """Fleche verte d'evolution (entre 2 KPI)."""
    fleche = slide.shapes.add_shape(
        MSO_SHAPE.RIGHT_ARROW,
        Inches(left), Inches(top),
        Inches(width), Inches(0.35),
    )
    fleche.name = "DSFR-fleche-decoratif"
    fleche.fill.solid()
    fleche.fill.fore_color.rgb = VERT_SUCCES
    fleche.line.fill.background()
    fleche.shadow.inherit = False
    return slide


def add_checklist(slide, items, top, left=MARGIN_L, width=CONTENT_W,
                  height=None, size=14):
    """Liste a cocher DSFR : case Unicode + texte.

    items : liste d'items. Chaque item peut etre :
      - une string (case non cochee par defaut)
      - un tuple (texte, checked: bool) pour controler l'etat
    """
    if height is None:
        height = len(items) * 0.45 + 0.3
    box = slide.shapes.add_textbox(
        Inches(left), Inches(top),
        Inches(width), Inches(height),
    )
    box.name = "DSFR-checklist"
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.15)
    tf.margin_right = Inches(0.15)
    tf.margin_top = Inches(0.1)
    tf.margin_bottom = Inches(0.1)
    tf.paragraphs[0].text = ""
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            text, checked = item[0], item[1]
        else:
            text, checked = item, False
        box_char = "\u2611" if checked else "\u2610"  # case cochee ou vide
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.line_spacing = 1.5
        # Case
        run_box = p.add_run()
        run_box.text = f"{box_char}  "
        run_box.font.name = FONT
        run_box.font.size = Pt(size + 4)
        run_box.font.bold = True
        run_box.font.color.rgb = VERT_SUCCES if checked else BLEU_FRANCE
        # Texte
        run_text = p.add_run()
        run_text.text = text
        run_text.font.name = FONT
        run_text.font.size = Pt(size)
        run_text.font.color.rgb = NOIR
    return slide


def add_avant_apres(slide, avant_titre, avant_bullets, apres_titre, apres_bullets,
                    top=None, height=3.5):
    """Comparaison avant/apres en 2 colonnes : rouge clair (avant) / vert clair (apres)."""
    if top is None:
        top = TOP_CARDS
    add_alert(slide, avant_titre, avant_bullets,
              top=top, left=MARGIN_L, width=COL_W, height=height,
              alert_type="error")
    add_alert(slide, apres_titre, apres_bullets,
              top=top, left=COL_R, width=COL_W, height=height,
              alert_type="success")
    return slide


def add_exemple_contre_exemple(slide, bon_titre, bon_bullets,
                                mauvais_titre, mauvais_bullets,
                                top=None, height=3.5):
    """2 colonnes pedagogiques : bon exemple (vert, check) / contre-exemple (rouge, croix)."""
    if top is None:
        top = TOP_CARDS
    add_alert(slide, f"\u2713  {bon_titre}", bon_bullets,
              top=top, left=MARGIN_L, width=COL_W, height=height,
              alert_type="success")
    add_alert(slide, f"\u2717  {mauvais_titre}", mauvais_bullets,
              top=top, left=COL_R, width=COL_W, height=height,
              alert_type="error")
    return slide


def add_encadre(slide, top, left, width, height, titre="", bullets=None,
                couleur_fond=GRIS_CLAIR, couleur_accent=BLEU_FRANCE):
    """Encadre parametrable (titre + bullets)."""
    _make_box(slide, top, left, width, height,
              fill_color=couleur_fond, accent_color=couleur_accent, accent_w=0.08)
    y = top + 0.15
    if titre:
        if not bullets:
            t_box = slide.shapes.add_textbox(
                Inches(left + 0.25), Inches(top),
                Inches(width - 0.4), Inches(height),
            )
            t_box.name = "DSFR-encadre-titre"
            _apply_text(t_box.text_frame, titre, font=FONT, size=14, bold=True,
                        color=couleur_accent, anchor=MSO_ANCHOR.MIDDLE)
        else:
            t_box = slide.shapes.add_textbox(
                Inches(left + 0.25), Inches(y),
                Inches(width - 0.4), Inches(0.45),
            )
            t_box.name = "DSFR-encadre-titre"
            _apply_text(t_box.text_frame, titre, font=FONT, size=14, bold=True,
                        color=couleur_accent)
        y += 0.5
    if bullets:
        b_box = slide.shapes.add_textbox(
            Inches(left + 0.25), Inches(y),
            Inches(width - 0.4), Inches(height - (y - top) - 0.15),
        )
        b_box.name = "DSFR-encadre-bullets"
        _add_bullets(b_box.text_frame, bullets, font=FONT, size=14, color=NOIR)
    return slide


# ----------------------------------------------------------------------
# Refontes DSFR : Sommaire et Chapitre
# ----------------------------------------------------------------------
def compose_sommaire(slide, titre, parties):
    """Compose un sommaire DSFR avec 3 cards numerotees.

    parties = [(titre_partie, description), ...]  (3 elements maximum)
    """
    # Le titre est deja pose par new_slide
    # On ajoute juste les cards
    n = min(len(parties), 3)
    card_w = (CONTENT_W - GAP * (n - 1)) / n
    card_h = 3.6
    card_top = TOP_CARDS
    for i, (titre_partie, description) in enumerate(parties[:n]):
        x = MARGIN_L + i * (card_w + GAP)
        add_card(slide, titre_partie, description, top=card_top, left=x,
                 width=card_w, height=card_h, numero=i + 1)
    return slide


def compose_chapitre(slide, numero, titre):
    """Compose une slide de section DSFR : composant Highlight centre avec numero + titre.

    Accent Bleu France a gauche + fond gris clair + texte « N. Titre » en 32pt Bleu France.
    Sobre, conforme au composant Highlight DSFR (fr-highlight).
    """
    # Supprimer le placeholder Title natif
    for ph in list(slide.placeholders):
        if _is_title_placeholder(ph):
            sp = ph._element
            sp.getparent().remove(sp)

    # Highlight DSFR centre verticalement dans la zone libre (y=0.9 -> 6.95)
    # Zone : CONTENT_W de large, ~1.8" de haut, centre a y=3.85
    top = 3.0
    height = 1.8
    _make_box(slide, top, MARGIN_L, CONTENT_W, height,
              fill_color=GRIS_CLAIR, accent_color=BLEU_FRANCE, accent_w=0.16)

    # Texte « N. Titre » sur une ligne
    texte = f"{numero}. {titre}"
    t_box = slide.shapes.add_textbox(
        Inches(MARGIN_L + 0.45), Inches(top + 0.15),
        Inches(CONTENT_W - 0.6), Inches(height - 0.3),
    )
    t_box.name = "DSFR-section-titre"
    _apply_text(t_box.text_frame, texte, font=FONT, size=32, bold=True,
                color=BLEU_FRANCE, anchor=MSO_ANCHOR.MIDDLE,
                align=PP_ALIGN.LEFT)
    return slide


# ----------------------------------------------------------------------
# Post-traitement a11y
# ----------------------------------------------------------------------
def _neutralize_auto_numbering(txBody):
    """Ajoute <a:buNone/> sur chaque paragraphe d'un text frame.

    Neutralise la numerotation automatique heritee du layout (buAutoNum),
    qui sinon prefixe les paragraphes par « 1. », « 2. », etc. au rendu.
    Utilise sur le placeholder du fil d'Ariane.
    """
    a_ns = f"{{{NSMAP_A}}}"
    for p in txBody.iter(f"{a_ns}p"):
        pPr = p.find(f"{a_ns}pPr")
        if pPr is None:
            pPr = etree.SubElement(p, f"{a_ns}pPr")
            p.remove(pPr)
            p.insert(0, pPr)
        # Retirer tout buAutoNum existant
        for el in pPr.findall(f"{a_ns}buAutoNum"):
            pPr.remove(el)
        # Retirer les buChar eventuels aussi
        for el in pPr.findall(f"{a_ns}buChar"):
            pPr.remove(el)
        # Ajouter buNone s'il n'est pas deja present
        if pPr.find(f"{a_ns}buNone") is None:
            etree.SubElement(pPr, f"{a_ns}buNone")


def _set_lang_on_runs(element, lang="fr-FR"):
    """Applique lang=fr-FR sur chaque run de texte.

    Couvre trois cas :
    - rPr deja present sur un run : on force l'attribut lang
    - rPr absent (run cree par python-pptx via tf.text=...) : on cree le rPr
      en tete du run avant <a:t>, avec lang
    - defRPr et endParaRPr : on force aussi l'attribut lang
    """
    r_tag = f"{{{NSMAP_A}}}r"
    rPr_tag = f"{{{NSMAP_A}}}rPr"
    for r in element.iter(r_tag):
        rPr = r.find(rPr_tag)
        if rPr is None:
            rPr = etree.SubElement(r, rPr_tag)
            # rPr doit etre le 1er enfant du run (avant <a:t>)
            r.remove(rPr)
            r.insert(0, rPr)
        rPr.set("lang", lang)
    for defRPr in element.iter(f"{{{NSMAP_A}}}defRPr"):
        defRPr.set("lang", lang)
    for endParaRPr in element.iter(f"{{{NSMAP_A}}}endParaRPr"):
        endParaRPr.set("lang", lang)


def _mark_decoratives(slide):
    """Alt text vide pour les shapes portant 'decoratif' dans leur nom."""
    for shape in slide.shapes:
        if shape.name and "decoratif" in shape.name.lower():
            sp = shape._element
            # Trouver ou creer nvSpPr/cNvPr
            cNvPr = sp.find(f".//{{{NSMAP_P}}}cNvPr")
            if cNvPr is None:
                cNvPr = sp.find(f".//{{{NSMAP_A}}}cNvPr")
            if cNvPr is not None:
                cNvPr.set("descr", "")


def _reorder_shapes(slide):
    """Reordonne le spTree : titre -> contenu -> footer -> decoratifs."""
    spTree = slide.shapes._spTree
    shapes_by_category = {"titre": [], "contenu": [], "footer": [], "decoratif": []}
    other = []
    children = list(spTree)
    # Separer les shapes des autres elements (nvGrpSpPr, grpSpPr)
    for child in children:
        tag = etree.QName(child.tag).localname
        if tag == "sp" or tag == "pic" or tag == "graphicFrame" or tag == "cxnSp":
            name = ""
            cNvPr = child.find(f".//{{{NSMAP_P}}}cNvPr")
            if cNvPr is None:
                cNvPr = child.find(f".//{{{NSMAP_A}}}cNvPr")
            if cNvPr is not None:
                name = cNvPr.get("name", "")
            name_low = name.lower()
            if "decoratif" in name_low:
                shapes_by_category["decoratif"].append(child)
            elif name.startswith("Titre") or "chapitre-titre" in name_low:
                shapes_by_category["titre"].append(child)
            elif ("pied de page" in name_low or "numero" in name_low
                  or "date" in name_low or "connecteur" in name_low):
                shapes_by_category["footer"].append(child)
            else:
                shapes_by_category["contenu"].append(child)
        else:
            other.append(child)
    # Vider le spTree et le reconstituer dans l'ordre
    for child in children:
        spTree.remove(child)
    for child in other:
        spTree.append(child)
    for child in shapes_by_category["titre"]:
        spTree.append(child)
    for child in shapes_by_category["contenu"]:
        spTree.append(child)
    for child in shapes_by_category["footer"]:
        spTree.append(child)
    for child in shapes_by_category["decoratif"]:
        spTree.append(child)


def finalize_pptx(prs, output, title="", author="Alex", subject="",
                  lang="fr-FR"):
    """Post-traitement a11y + sauvegarde.

    - Ordre de lecture XML (titre -> contenu -> footer -> decoratifs)
    - lang=fr-FR sur chaque run
    - Alt text vide sur shapes decoratifs
    - Metadonnees core properties
    """
    for slide in prs.slides:
        _mark_decoratives(slide)
        _set_lang_on_runs(slide._element, lang=lang)
        _reorder_shapes(slide)
        # Notes presentateur : meme post-traitement de langue.
        # add_notes() cree un run sans rPr, sans cette passe les notes
        # sont rendues en langue systeme (souvent en-US).
        if slide.has_notes_slide:
            _set_lang_on_runs(slide.notes_slide._element, lang=lang)
    # Core properties
    cp = prs.core_properties
    if title:
        cp.title = title
    if author:
        cp.author = author
    if subject:
        cp.subject = subject
    cp.language = lang
    prs.save(output)
    # macOS : retirer le flag com.apple.quarantine pose par Gatekeeper
    # Sans ce fix, PowerPoint ouvre le PPTX en mode protege et refuse
    # d'enregistrer les modifications manuelles de l'utilisateur.
    try:
        import subprocess
        subprocess.run(
            ["xattr", "-d", "com.apple.quarantine", str(output)],
            capture_output=True, check=False, timeout=5,
        )
    except Exception:
        pass
    return output
