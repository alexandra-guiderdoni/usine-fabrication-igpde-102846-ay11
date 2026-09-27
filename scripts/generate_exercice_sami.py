"""Generateur des fichiers de l'exercice Sami.

Produit :
- _assets/graphique-inaccessible.png  (barres couleurs seules)
- _assets/graphique-accessible.png    (barres avec motifs + etiquettes)
- _assets/icone-enveloppe.png         (icone e-mail)
- _assets/organigramme.png            (organigramme du service)
- tp-doc-inaccessible.docx           (21 erreurs intentionnelles)
- tp-doc-aide-correction.docx        (version fautive annotee)
- tp-doc-accessible.docx             (version corrigee)
"""

import subprocess
from xml.sax.saxutils import escape
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
from lxml import etree

PROJECT = Path(__file__).resolve().parent.parent
ASSETS = PROJECT / "_assets"
ASSETS.mkdir(exist_ok=True)

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
ADEC_NS = "http://schemas.microsoft.com/office/drawing/2017/decorative"
DECORATIVE_EXT_URI = "{C183D7F6-B498-43B3-948B-1728B52AA6E4}"


# ------------------------------------------------------------------
# 1. Graphiques PNG
# ------------------------------------------------------------------

INDICATEURS = ["Visiteurs\nuniques", "Pages\nvues", "Taux de\nrebond"]
T4_2024 = [45200, 128000, 42]
T1_2025 = [50600, 142000, 38]
EVOL = ["+12 %", "+11 %", "-4 pts"]


def generate_chart_inaccessible():
    """Barres vert/rouge/orange sans motif ni etiquette."""
    fig, ax = plt.subplots(figsize=(5, 3))
    x = np.arange(len(INDICATEURS))
    w = 0.35
    ax.bar(x - w / 2, T4_2024, w, color="#E74C3C")
    ax.bar(x + w / 2, T1_2025, w, color="#27AE60")
    ax.set_xticks(x)
    ax.set_xticklabels(INDICATEURS, fontsize=8)
    ax.set_title("Evolution du trafic web", fontsize=10)
    ax.tick_params(axis="y", labelsize=7)
    fig.tight_layout()
    path = ASSETS / "graphique-inaccessible.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def generate_chart_accessible():
    """Barres avec motifs distincts + etiquettes sur chaque barre."""
    fig, ax = plt.subplots(figsize=(5, 3))
    x = np.arange(len(INDICATEURS))
    w = 0.35
    bars1 = ax.bar(x - w / 2, T4_2024, w, color="#6C6C6C",
                   edgecolor="black", linewidth=0.8, hatch="///",
                   label="T4 2024")
    bars2 = ax.bar(x + w / 2, T1_2025, w, color="#B0B0B0",
                   edgecolor="black", linewidth=0.8, hatch="...",
                   label="T1 2025")

    for bar, val in zip(bars1, T4_2024):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 500,
                f"{val:,}".replace(",", " "), ha="center", va="bottom",
                fontsize=6)
    for bar, val, ev in zip(bars2, T1_2025, EVOL):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 500,
                f"{val:,}".replace(",", " ") + f" ({ev})",
                ha="center", va="bottom", fontsize=6)

    ax.set_xticks(x)
    ax.set_xticklabels(INDICATEURS, fontsize=8)
    ax.set_title("Evolution du trafic web", fontsize=10)
    ax.tick_params(axis="y", labelsize=7)
    ax.legend(fontsize=7, loc="upper left")
    fig.tight_layout()
    path = ASSETS / "graphique-accessible.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


# ------------------------------------------------------------------
# 2. Icone enveloppe + organigramme
# ------------------------------------------------------------------

def generate_icon_enveloppe():
    """Petite icone d'enveloppe pour le paragraphe contact."""
    fig, ax = plt.subplots(figsize=(0.5, 0.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect("equal")
    ax.axis("off")
    # Corps de l'enveloppe
    rect = mpatches.FancyBboxPatch((1, 2), 8, 5, boxstyle="round,pad=0.3",
                                    facecolor="#000091", edgecolor="#000091")
    ax.add_patch(rect)
    # Rabat triangulaire
    ax.plot([1, 5, 9], [7, 3.5, 7], color="white", linewidth=1.5)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    path = ASSETS / "icone-enveloppe.png"
    fig.savefig(path, dpi=100, transparent=True, bbox_inches="tight",
                pad_inches=0.02)
    plt.close(fig)
    return path


def generate_organigramme():
    """Organigramme simple de la Direction des affaires juridiques."""
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis("off")

    box_style = dict(boxstyle="round,pad=0.4", facecolor="#000091",
                     edgecolor="#000091")
    text_kw = dict(ha="center", va="center", fontsize=8, color="white",
                   fontweight="bold", bbox=box_style)

    ax.text(6, 6, "Direction des\naffaires juridiques", **text_kw)

    equipes = [
        (1.5, 2.5, "Bureau du\ndroit public"),
        (4.5, 2.5, "Bureau du\ndroit social"),
        (7.5, 2.5, "Bureau de la\ncommunication"),
        (10.5, 2.5, "Bureau des\naffaires internationales"),
    ]
    for x, y, label in equipes:
        ax.text(x, y, label, **text_kw)
        ax.plot([x, x], [y + 0.8, 5.2], color="#000091", linewidth=1.5)

    ax.plot([1.5, 10.5], [5.2, 5.2], color="#000091", linewidth=1.5)
    ax.plot([6, 6], [5.2, 5.5], color="#000091", linewidth=1.5)

    fig.tight_layout()
    path = ASSETS / "organigramme.png"
    fig.savefig(path, dpi=150, facecolor="white", bbox_inches="tight")
    plt.close(fig)
    return path


def generate_texte_image():
    """Genere une image contenant du texte (avis important) pour l'erreur texte-image."""
    fig, ax = plt.subplots(figsize=(5, 1.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3)
    ax.axis("off")
    rect = mpatches.FancyBboxPatch((0.2, 0.2), 9.6, 2.6, boxstyle="round,pad=0.3",
                                    facecolor="#FFF3CD", edgecolor="#856404",
                                    linewidth=1.5)
    ax.add_patch(rect)
    ax.text(5, 1.5,
            "Avis important : les indicateurs du T2 2025\n"
            "seront transmis avant le 15 septembre 2025.",
            ha="center", va="center", fontsize=11,
            fontweight="bold", color="#856404")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    path = ASSETS / "texte-image.png"
    fig.savefig(path, dpi=150, facecolor="white", bbox_inches="tight",
                pad_inches=0.05)
    plt.close(fig)
    return path


# ------------------------------------------------------------------
# 3. Document inaccessible
# ------------------------------------------------------------------

def _add_watermark(doc, text):
    """Ajoute un filigrane texte diagonal au document via VML dans le header."""
    from lxml import etree
    section = doc.sections[0]
    header = section.header
    header.is_linked_to_previous = False
    p = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
    ns = {
        "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
        "v": "urn:schemas-microsoft-com:vml",
        "o": "urn:schemas-microsoft-com:office:office",
    }
    pict_xml = (
        f'<w:r xmlns:w="{ns["w"]}" xmlns:v="{ns["v"]}" xmlns:o="{ns["o"]}">'
        f'<w:rPr><w:noProof/></w:rPr>'
        f'<w:pict>'
        f'<v:shapetype id="_x0000_t136" coordsize="21600,21600" o:spt="136" '
        f'path="m@7,l@8,m@5,21600l@6,21600e">'
        f'<v:formulas><v:f eqn="sum #0 0 10800"/></v:formulas>'
        f'<v:path textpathok="t"/>'
        f'<v:textpath on="t" fitshape="t"/>'
        f'<o:lock v:ext="edit" text="t" shapetype="t"/>'
        f'</v:shapetype>'
        f'<v:shape id="WaterMark" o:spid="_x0000_s2049" type="#_x0000_t136" '
        f'style="position:absolute;margin-left:0;margin-top:0;width:500pt;'
        f'height:100pt;rotation:315;z-index:-251658752;'
        f'mso-position-horizontal:center;mso-position-horizontal-relative:margin;'
        f'mso-position-vertical:center;mso-position-vertical-relative:margin" '
        f'o:allowincell="f" fillcolor="silver" stroked="f">'
        f'<v:fill opacity=".5"/>'
        f'<v:textpath style="font-family:&quot;Arial&quot;;font-size:1pt" '
        f'string="{text}"/>'
        f'</v:shape>'
        f'</w:pict>'
        f'</w:r>'
    )
    r_element = etree.fromstring(pict_xml)
    p._p.append(r_element)


def _set_image_alt(doc, alt_text="", title=""):
    """Pose alt text et titre sur la derniere image inseree."""
    inline_shape = doc.inline_shapes[-1]
    pic = inline_shape._inline
    docPr = pic.find(qn("wp:docPr"))
    if docPr is not None:
        docPr.set("descr", alt_text)
        if title:
            docPr.set("title", title)


def _mark_image_decorative(doc):
    """Marque la derniere image comme decorative via l'extension Office."""
    _set_image_alt(doc, alt_text="", title="")
    inline_shape = doc.inline_shapes[-1]
    docPr = inline_shape._inline.find(qn("wp:docPr"))
    if docPr is None:
        return

    extLst = docPr.find(f"{{{A_NS}}}extLst")
    if extLst is None:
        extLst = etree.SubElement(docPr, f"{{{A_NS}}}extLst")
    for ext in list(extLst.findall(f"{{{A_NS}}}ext")):
        if ext.get("uri") == DECORATIVE_EXT_URI:
            extLst.remove(ext)
    ext = parse_xml(
        f'<a:ext xmlns:a="{A_NS}" uri="{DECORATIVE_EXT_URI}">'
        f'<adec:decorative xmlns:adec="{ADEC_NS}" val="1"/>'
        f'</a:ext>'
    )
    extLst.append(ext)


def _set_style_language(style, lang):
    """Pose la langue sur un style Word."""
    rPr = style.element.get_or_add_rPr()
    lang_el = rPr.find(qn("w:lang"))
    if lang_el is None:
        lang_el = parse_xml(
            f'<w:lang {nsdecls("w")} w:val="{lang}" '
            f'w:eastAsia="{lang}" w:bidi="{lang}"/>'
        )
        rPr.append(lang_el)
    else:
        lang_el.set(qn("w:val"), lang)
        lang_el.set(qn("w:eastAsia"), lang)
        lang_el.set(qn("w:bidi"), lang)


def _set_doc_defaults_language(doc, lang):
    """Pose la langue par defaut du document dans styles.xml."""
    styles = doc.styles.element
    doc_defaults = styles.find(qn("w:docDefaults"))
    if doc_defaults is None:
        doc_defaults = parse_xml(f'<w:docDefaults {nsdecls("w")}/>')
        styles.insert(0, doc_defaults)

    rPr_default = doc_defaults.find(qn("w:rPrDefault"))
    if rPr_default is None:
        rPr_default = parse_xml(f'<w:rPrDefault {nsdecls("w")}/>')
        doc_defaults.insert(0, rPr_default)

    rPr = rPr_default.find(qn("w:rPr"))
    if rPr is None:
        rPr = parse_xml(f'<w:rPr {nsdecls("w")}/>')
        rPr_default.append(rPr)

    lang_el = rPr.find(qn("w:lang"))
    if lang_el is None:
        lang_el = parse_xml(
            f'<w:lang {nsdecls("w")} w:val="{lang}" '
            f'w:eastAsia="{lang}" w:bidi="{lang}"/>'
        )
        rPr.append(lang_el)
    else:
        lang_el.set(qn("w:val"), lang)
        lang_el.set(qn("w:eastAsia"), lang)
        lang_el.set(qn("w:bidi"), lang)


def _add_hyperlink(paragraph, text, url):
    """Ajoute un vrai lien hypertexte Word avec style visuel standard."""
    r_id = paragraph.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = parse_xml(
        f'<w:hyperlink {nsdecls("w", "r")} r:id="{r_id}">'
        f'<w:r>'
        f'<w:rPr><w:color w:val="0000FF"/><w:u w:val="single"/></w:rPr>'
        f'<w:t>{escape(text)}</w:t>'
        f'</w:r>'
        f'</w:hyperlink>'
    )
    paragraph._p.append(hyperlink)


def _add_toc(doc):
    """Insere un champ Table des matieres automatique."""
    from lxml import etree
    p = doc.add_paragraph()
    run = p.add_run()
    fldChar_begin = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    run._r.append(fldChar_begin)
    run2 = p.add_run()
    instrText = parse_xml(
        f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText>'
    )
    run2._r.append(instrText)
    run3 = p.add_run()
    fldChar_separate = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    run3._r.append(fldChar_separate)
    run4 = p.add_run("(Table des matières - mettre à jour avec F9)")
    run4.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    run4.font.size = Pt(10)
    run5 = p.add_run()
    fldChar_end = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run5._r.append(fldChar_end)


def _add_simple_field(paragraph, instr):
    """Ajoute un champ Word simple dans un paragraphe."""
    run_begin = paragraph.add_run()
    run_begin._r.append(
        parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    )
    run_instr = paragraph.add_run()
    run_instr._r.append(
        parse_xml(
            f'<w:instrText {nsdecls("w")} xml:space="preserve"> {instr} </w:instrText>'
        )
    )
    run_sep = paragraph.add_run()
    run_sep._r.append(
        parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    )
    run_result = paragraph.add_run("1")
    run_end = paragraph.add_run()
    run_end._r.append(
        parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    )
    return run_result


DOCUMENT_TITLE = "Rapport trimestriel - Bilan T1 2025"
HEADER_TEXT = "Direction des affaires juridiques - Rapport trimestriel T1 2025"


def _format_header_footer_run(run):
    """Applique le style explicite aux textes d'en-tete et pied de page."""
    run.font.name = "Arial"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)


def _format_header_paragraph(paragraph):
    for run in paragraph.runs:
        _format_header_footer_run(run)


def _add_page_footer(doc, document_name=DOCUMENT_TITLE):
    """Ajoute un pied de page Page X / Y avec champs Word natifs."""
    footer = doc.sections[0].footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.clear()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if document_name:
        p.add_run(document_name)
        p.add_run(" - ")
    p.add_run("Page ")
    _add_simple_field(p, "PAGE")
    p.add_run(" / ")
    _add_simple_field(p, "NUMPAGES")
    for run in p.runs:
        _format_header_footer_run(run)


def _add_fake_list_item(doc, marker, text):
    """Ajoute un item tape manuellement mais aligne comme une vraie liste."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.first_line_indent = Inches(-0.18)
    run = p.add_run(f"{marker}\t{text}")
    run.font.name = "Arial"
    run.font.size = Pt(11)
    return p


def _add_guidance_comment(doc, runs, text):
    """Ajoute un commentaire Word de correction sur un ou plusieurs runs."""
    if not runs:
        return
    if not isinstance(runs, (list, tuple)):
        runs = [runs]
    runs = [run for run in runs if run is not None]
    if runs:
        doc.add_comment(
            runs,
            text=text,
            author="Formation IGPDE",
            initials="IGPDE",
        )


def build_inaccessible(chart_path: Path, icon_path: Path = None,
                       organigramme_path: Path = None,
                       texte_image_path: Path = None,
                       with_guidance: bool = False,
                       output_name: str = "tp-doc-inaccessible.docx"):
    doc = Document()
    doc.core_properties.title = ""
    doc.core_properties.author = ""
    doc.core_properties.subject = ""

    style_normal = doc.styles["Normal"]
    style_normal.font.name = "Arial"
    style_normal.font.size = Pt(11)
    # Erreur 15 : texte justifie (cree des espaces inegaux, difficile pour dyslexiques)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # En-tete fictif
    header = doc.sections[0].header
    hp = header.paragraphs[0]
    hp.text = HEADER_TEXT
    hp.style.font.name = "Arial"
    hp.style.font.size = Pt(9)
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _format_header_paragraph(hp)
    _add_page_footer(doc)

    # Erreur 18 : filigrane invisible au lecteur d'ecran
    _add_watermark(doc, "CONFIDENTIEL")

    # Erreur 1 : faux Titre 1 (gras Arial 16, couleur bleu pour simuler un vrai titre)
    p = doc.add_paragraph()
    run = p.add_run("Introduction")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 1 - Problème : ce titre est seulement mis en forme en "
            "gras/couleur, il n'est pas reconnu comme titre par Word. Impact : "
            "la navigation au lecteur d'écran reste plate. Méthode : appliquer "
            "Accueil > Styles > Titre 1.",
        )
        _add_guidance_comment(
            doc,
            run,
            "Critère 14 - Problème : les propriétés du document sont vides. "
            "Impact : le fichier est moins identifiable pour les aides "
            "techniques et la recherche documentaire. Méthode : Fichier > "
            "Informations > Propriétés. Titre attendu : Rapport trimestriel - "
            "Bilan T1 2025 ; auteur : Sami Dupont.",
        )

    intro_paragraph = doc.add_paragraph(
        "Ce rapport trimestriel présente les résultats de communication "
        "numérique de la Direction des affaires juridiques pour le premier "
        "trimestre 2025. Il couvre les principaux indicateurs de performance "
        "de nos canaux digitaux."
    )
    if with_guidance:
        _add_guidance_comment(
            doc,
            intro_paragraph.runs,
            "Critère 15 - Problème : le texte courant est justifié. Impact : "
            "les espaces irréguliers entre les mots peuvent gêner la lecture, "
            "notamment pour des personnes dyslexiques ou malvoyantes. Méthode : "
            "sélectionner le texte ou le style Normal, puis choisir "
            "Accueil > Aligner à gauche.",
        )

    # Erreur 19 : faux sommaire tape a la main (points de suite manuels)
    p = doc.add_paragraph()
    run = p.add_run("Sommaire")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 19 - Problème : ce sommaire est tapé à la main. Impact : "
            "il n'est ni navigable ni mis à jour automatiquement. Méthode : "
            "appliquer les styles de titres, puis Références > Table des "
            "matières.",
        )
    for titre_som, page in [
        ("Résultats du trimestre", "2"),
        ("Détail par canal", "3"),
        ("Organisation du service", "4"),
        ("Contact", "5"),
        ("Annexes", "5"),
    ]:
        doc.add_paragraph(f"{titre_som} .............. {page}")

    doc.add_paragraph()

    # Erreur 5 : couleur seule (rouge #FF0000 sans gras, meme texte que l'accessible)
    p = doc.add_paragraph()
    run = p.add_run("Urgent - Retour attendu avant le 30 juin 2025")
    run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)
    run.font.name = "Arial"
    run.font.size = Pt(11)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 5 - Problème : l'urgence repose surtout sur le rouge. "
            "Impact : l'information peut être perdue sans perception de la "
            "couleur. Méthode : ajouter une emphase non colorée, par exemple "
            "le gras, et conserver un libellé explicite.",
        )

    doc.add_paragraph(
        "La direction demande un retour rapide sur les indicateurs."
    )

    # Erreur 2 : faux Titre 2 (gras Arial 14, couleur bleu pour simuler un vrai titre)
    p = doc.add_paragraph()
    run = p.add_run("Résultats du trimestre")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 2 - Problème : ce sous-titre est seulement visuel. "
            "Impact : il ne structure pas le document pour la navigation. "
            "Méthode : appliquer Accueil > Styles > Titre 2.",
        )

    # Erreur 4 : tableau sans en-tete balisee
    table = doc.add_table(rows=4, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    data = [
        ["Indicateur", "T4 2024", "T1 2025", "Évolution"],
        ["Visiteurs uniques", "45 200", "50 600", "+12 %"],
        ["Pages vues", "128 000", "142 000", "+11 %"],
        ["Taux de rebond", "42 %", "38 %", "-4 pts"],
    ]
    for i, row_data in enumerate(data):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                paragraph.style.font.name = "Arial"
                paragraph.style.font.size = Pt(10)
    # Pas de ligne d'en-tete balisee (pas de tblHeader)
    if with_guidance:
        _add_guidance_comment(
            doc,
            table.cell(0, 0).paragraphs[0].runs,
            "Critère 4 - Problème : la première ligne du tableau n'est pas "
            "déclarée comme en-tête. Impact : les cellules ne sont pas "
            "associées à leurs colonnes. Méthode : sélectionner le tableau > "
            "Création de tableau > Options de style de tableau > Ligne "
            "d'en-tête.",
        )

    # Erreur 16 : paragraphes vides pour simuler un espacement
    empty_paragraphs = []
    for _ in range(4):
        empty_paragraphs.append(doc.add_paragraph())
    if with_guidance:
        _add_guidance_comment(
            doc,
            table.cell(0, 1).paragraphs[0].runs,
            "Critère 16 - Problème : l'espacement est créé avec des "
            "paragraphes vides. Impact : un lecteur d'écran peut annoncer des "
            "vides inutiles. Méthode : supprimer ces paragraphes et régler "
            "l'espacement avec Mise en page > Paragraphe > Espacement "
            "avant/après ou via les styles.",
        )

    # Erreur 11 : fausse liste a puces (puces tapees et indentees manuellement)
    doc.add_paragraph("Objectifs du trimestre :")
    first_fake_bullet = None
    for item in [
        "Augmenter le trafic de 10 %",
        "Publier 3 articles par semaine",
        "Réduire le taux de rebond sous 40 %",
    ]:
        p = _add_fake_list_item(doc, "\u2022", item)
        first_fake_bullet = first_fake_bullet or p
    if with_guidance and first_fake_bullet:
        _add_guidance_comment(
            doc,
            first_fake_bullet.runs,
            "Critère 11 - Problème : les puces sont tapées au clavier. "
            "Impact : Word ne les expose pas comme une liste structurée. "
            "Méthode : sélectionner les éléments de liste > Accueil > Puces.",
        )

    # Erreur 12 : fausse liste numerotee (numeros tapes et indentes manuellement)
    doc.add_paragraph("Priorités pour le prochain trimestre :")
    first_fake_number = None
    for numero, item in enumerate([
        "Refonte de la page d'accueil",
        "Mise en conformité accessibilité",
        "Déploiement de la newsletter",
    ], start=1):
        p = _add_fake_list_item(doc, f"{numero}.", item)
        first_fake_number = first_fake_number or p
    if with_guidance and first_fake_number:
        _add_guidance_comment(
            doc,
            first_fake_number.runs,
            "Critère 12 - Problème : les numéros sont tapés à la main. "
            "Impact : la numérotation n'est pas reconnue comme liste. "
            "Méthode : sélectionner les éléments de liste > Accueil > "
            "Numérotation.",
        )

    doc.add_paragraph()

    # Erreur 3 : faux Titre 3 (gras Arial 12 souligne, couleur bleu pour simuler un vrai titre)
    p = doc.add_paragraph()
    run = p.add_run("Détail par canal")
    run.bold = True
    run.underline = True
    run.font.name = "Arial"
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 3 - Problème : le soulignement et le gras créent "
            "seulement une apparence de titre. Impact : le niveau de titre est "
            "absent de la structure. Méthode : Accueil > Styles > Titre 3.",
        )

    # Erreur 7 : image sans alt + couleurs seules
    doc.add_picture(str(chart_path), width=Inches(4.5))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if with_guidance:
        _add_guidance_comment(
            doc,
            last_paragraph.runs,
            "Critère 7 - Problème : le graphique n'a pas d'alternative et "
            "s'appuie sur la couleur seule. Impact : il est inaccessible au "
            "lecteur d'écran et difficile pour certains daltonismes. Méthode : "
            "ajouter un texte alternatif descriptif, puis utiliser motifs, "
            "étiquettes et légende textuelle.",
        )

    doc.add_paragraph()

    # Erreur 9 : organigramme avec alt "image.png" (nom de fichier par defaut)
    if organigramme_path:
        p = doc.add_paragraph()
        run = p.add_run("Organisation du service")
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
        if with_guidance:
            _add_guidance_comment(
                doc,
                run,
                "Titre visuel supplémentaire - Problème : ce titre est "
                "formaté directement. Impact : il n'apparaît pas dans la "
                "navigation. Méthode : appliquer le style Titre 2.",
            )

        doc.add_picture(str(organigramme_path), width=Inches(5.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        _set_image_alt(doc, alt_text="image.png")
        if with_guidance:
            _add_guidance_comment(
                doc,
                doc.paragraphs[-1].runs,
                "Critère 9 - Problème : l'alternative 'image.png' ne décrit "
                "pas l'organigramme. Impact : l'information est perdue. "
                "Méthode : mettre une alternative courte qui renvoie vers une "
                "description détaillée dans le corps.",
            )

        doc.add_paragraph()

    # Erreur 10 : icone redondante avec alt "E-mail" au lieu de decoratif
    if icon_path:
        p = doc.add_paragraph()
        run = p.add_run("Contact")
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
        if with_guidance:
            _add_guidance_comment(
                doc,
                run,
                "Titre visuel supplémentaire - Problème : ce titre est "
                "seulement visuel. Impact : rupture de navigation. Méthode : "
                "appliquer le style Titre 2.",
            )

        p = doc.add_paragraph()
        p.add_run("Pour toute question, contactez-nous par ")
        r = p.add_run()
        r.add_picture(str(icon_path), width=Inches(0.18))
        _set_image_alt(doc, alt_text="E-mail")
        p.add_run(" e-mail pour plus d'informations.")
        if with_guidance:
            _add_guidance_comment(
                doc,
                r,
                "Critère 10 - Problème : l'icône répète le mot e-mail déjà "
                "présent dans le texte. Impact : redondance à la lecture "
                "vocale. Méthode : clic droit sur l'image > Afficher le texte "
                "de remplacement > Marquer comme décoratif.",
            )

    # Erreur 13 : passage anglais sans balisage de langue
    p = doc.add_paragraph(
        "The quarterly report is available upon request. "
        "Please contact the communication department for further details."
    )
    if with_guidance:
        _add_guidance_comment(
            doc,
            p.runs,
            "Critère 13 - Problème : ce passage anglais n'est pas balisé dans "
            "sa langue. Impact : il peut être prononcé avec une voix française. "
            "Méthode : sélectionner le texte > Révision > Langue > Définir la "
            "langue de vérification > Anglais.",
        )

    # Erreur 20 : texte sous forme d'image
    if texte_image_path:
        doc.add_paragraph()
        doc.add_picture(str(texte_image_path), width=Inches(4.5))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        if with_guidance:
            _add_guidance_comment(
                doc,
                doc.paragraphs[-1].runs,
                "Critère 20 - Problème : ce texte est une image. Impact : il "
                "n'est ni sélectionnable, ni recherchable, ni fiable en "
                "synthèse vocale. Méthode : le ressaisir en vrai texte Word.",
            )

    # Erreur 21 : tableau avec cellules fusionnees et en-tetes seulement visuels
    doc.add_paragraph()
    p = doc.add_paragraph()
    run = p.add_run("Répartition par service")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 21 - Problème : la première ligne fusionnée complexifie "
            "la structure du tableau. Impact : les associations cellules/"
            "en-têtes deviennent fragiles. Méthode : refaire un tableau simple "
            "sans fusion et cocher Ligne d'en-tête.",
        )
    table = doc.add_table(rows=4, cols=3, style="Table Grid")
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Fusionner la premiere ligne sur 3 colonnes
    table.cell(0, 0).merge(table.cell(0, 2))
    data = [
        ["Direction des affaires juridiques", "", ""],
        ["Service", "Effectif", "Budget"],
        ["Communication", "12", "45 000"],
        ["Juridique", "28", "120 000"],
    ]
    for i, row_data in enumerate(data):
        for j, cell_text in enumerate(row_data):
            if i == 0 and j > 0:
                continue
            cell = table.cell(i, j)
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for cell_run in paragraph.runs:
                    cell_run.font.name = "Arial"
                    cell_run.font.size = Pt(10)
                    if i in (0, 1):
                        cell_run.bold = True
    # Pas de tblHeader : les libelles sont visuels, pas declares comme en-tetes Word.
    if with_guidance:
        _add_guidance_comment(
            doc,
            table.cell(1, 0).paragraphs[0].runs,
            "Critère 21 - Problème : les libellés en gras sont seulement "
            "visuels. Impact : ils ne sont pas annoncés comme en-têtes. "
            "Méthode : déclarer la ligne d'en-tête avec l'option Word et "
            "supprimer la ligne fusionnée.",
        )

    doc.add_paragraph()

    # Section Annexes (faux titre + Erreur 17 : majuscules tapees au clavier)
    p = doc.add_paragraph()
    run = p.add_run("ANNEXES")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 17 - Problème : le mot est tapé entièrement en capitales. "
            "Impact : certaines aides peuvent l'épeler ou le prononcer moins "
            "naturellement. Méthode : saisir 'Annexes' en minuscules puis "
            "appliquer Police > Tout en majuscules si l'effet visuel est voulu.",
        )

    # Erreur 8 : lien non descriptif
    p = doc.add_paragraph("Pour accéder aux annexes, ")
    _add_hyperlink(
        p,
        "cliquez ici",
        "https://example.org/annexes-rapport-t1-2025.pdf",
    )
    p.add_run(".")
    if with_guidance:
        _add_guidance_comment(
            doc,
            p.runs,
            "Critère 8 - Problème : 'cliquez ici' n'est pas descriptif. "
            "Impact : hors contexte, le lien ne dit pas où il mène. Méthode : "
            "remplacer par 'Consulter les annexes du rapport T1 2025 (PDF, "
            "1,2 Mo)'.",
        )

    # Erreur 6 : contraste ambigu (gris #767676)
    p = doc.add_paragraph()
    run = p.add_run("Note : les données sont provisoires et susceptibles "
                     "d’ajustements lors de la consolidation finale.")
    run.font.color.rgb = RGBColor(0x76, 0x76, 0x76)
    run.font.size = Pt(9)
    run.font.name = "Arial"
    if with_guidance:
        _add_guidance_comment(
            doc,
            run,
            "Critère 6 - Problème : le gris #767676 sur blanc est trop juste "
            "pour du petit texte. Impact : la note peut être difficile à lire. "
            "Méthode : mesurer le contraste, puis utiliser #595959 ou du noir.",
        )

    # Erreur 14 : pas de proprietes document
    if with_guidance:
        _add_guidance_comment(
            doc,
            hp.runs,
            "Critère 18 - Problème : le filigrane CONFIDENTIEL est un objet "
            "graphique dans l'en-tête. Impact : il peut être invisible pour les "
            "lecteurs d'écran. Méthode : ajouter 'Document confidentiel' en "
            "vrai texte dans le corps du document.",
        )

    output = PROJECT / "_source" / output_name
    doc.save(str(output))
    _remove_quarantine(output)
    print(f"  -> {output.name}")
    return output


# ------------------------------------------------------------------
# 3. Document accessible
# ------------------------------------------------------------------

def build_accessible(chart_path: Path, icon_path: Path = None,
                     organigramme_path: Path = None,
                     texte_image_path: Path = None):
    doc = Document()

    style_normal = doc.styles["Normal"]
    style_normal.font.name = "Arial"
    style_normal.font.size = Pt(11)
    # Alignement a gauche (pas de justification)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

    # Langue du document : fr-FR par defaut, passage anglais balise plus bas.
    _set_doc_defaults_language(doc, "fr-FR")
    _set_style_language(style_normal, "fr-FR")

    # Configurer les styles de titre
    for level, size in [(1, 16), (2, 14), (3, 12)]:
        style = doc.styles[f"Heading {level}"]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

    # En-tete
    header = doc.sections[0].header
    hp = header.paragraphs[0]
    hp.text = HEADER_TEXT
    hp.style.font.name = "Arial"
    hp.style.font.size = Pt(9)
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    _format_header_paragraph(hp)
    _add_page_footer(doc)

    # Mention confidentiel dans le corps (pas en filigrane)
    p = doc.add_paragraph()
    run = p.add_run("Document confidentiel")
    run.font.name = "Arial"
    run.font.size = Pt(11)

    # Titre 1
    doc.add_heading("Introduction", level=1)

    doc.add_paragraph(
        "Ce rapport trimestriel présente les résultats de communication "
        "numérique de la Direction des affaires juridiques pour le premier "
        "trimestre 2025. Il couvre les principaux indicateurs de performance "
        "de nos canaux digitaux."
    )

    # Sommaire automatique (table des matieres generee depuis les styles)
    doc.add_heading("Sommaire", level=2)
    _add_toc(doc)

    # Mention urgente accessible (#C00000 ratio 6.5:1 sur blanc)
    p = doc.add_paragraph()
    run = p.add_run("Urgent - Retour attendu avant le 30 juin 2025")
    run.bold = True
    run.font.color.rgb = RGBColor(0xC0, 0x00, 0x00)
    run.font.name = "Arial"
    run.font.size = Pt(11)

    doc.add_paragraph(
        "La direction demande un retour rapide sur les indicateurs."
    )

    # Titre 2
    doc.add_heading("Résultats du trimestre", level=2)

    # Tableau avec en-tete balisee
    table = doc.add_table(rows=4, cols=4, style="Table Grid")
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    data = [
        ["Indicateur", "T4 2024", "T1 2025", "Évolution"],
        ["Visiteurs uniques", "45 200", "50 600", "+12 %"],
        ["Pages vues", "128 000", "142 000", "+11 %"],
        ["Taux de rebond", "42 %", "38 %", "-4 pts"],
    ]
    for i, row_data in enumerate(data):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
            if i == 0:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True

    # Baliser la premiere ligne comme en-tete
    tbl = table._tbl
    first_row = tbl.tr_lst[0]
    trPr = first_row.get_or_add_trPr()
    tblHeader = parse_xml(f'<w:tblHeader {nsdecls("w")} val="true"/>')
    trPr.append(tblHeader)

    # Vraie liste a puces native
    doc.add_paragraph("Objectifs du trimestre :")
    for item in [
        "Augmenter le trafic de 10 %",
        "Publier 3 articles par semaine",
        "Réduire le taux de rebond sous 40 %",
    ]:
        doc.add_paragraph(item, style="List Bullet")

    # Vraie liste numerotee native
    doc.add_paragraph("Priorités pour le prochain trimestre :")
    for item in [
        "Refonte de la page d'accueil",
        "Mise en conformité accessibilité",
        "Déploiement de la newsletter",
    ]:
        doc.add_paragraph(item, style="List Number")

    # Titre 3
    doc.add_heading("Détail par canal", level=3)

    # Image avec alt text
    doc.add_picture(str(chart_path), width=Inches(4.5))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Ajouter alt text a l'image
    inline_shape = doc.inline_shapes[-1]
    pic = inline_shape._inline
    nvPicPr = pic.find(qn("wp:docPr"))
    if nvPicPr is not None:
        nvPicPr.set("descr",
            "Graphique d'évolution du trafic web T1 2025 : "
            "visiteurs uniques en hausse de 12 %, pages vues +11 %, "
            "taux de rebond en baisse de 4 points.")
        nvPicPr.set("title", "Trafic web T1 2025")

    # Organigramme avec alt court + description detaillee
    if organigramme_path:
        doc.add_heading("Organisation du service", level=2)

        doc.add_picture(str(organigramme_path), width=Inches(5.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        _set_image_alt(
            doc,
            alt_text="Organigramme de la Direction des affaires juridiques "
                     "(description ci-dessous).",
            title="Organigramme du service",
        )

        p = doc.add_paragraph()
        run = p.add_run(
            "La Direction des affaires juridiques comprend 4 bureaux : "
            "le Bureau du droit public, le Bureau du droit social, "
            "le Bureau de la communication et le Bureau des affaires "
            "internationales. Chaque bureau est rattaché directement "
            "à la direction.")
        run.font.name = "Arial"
        run.font.size = Pt(10)

    # Icone decorative + paragraphe contact
    if icon_path:
        doc.add_heading("Contact", level=2)

        p = doc.add_paragraph()
        p.add_run("Pour toute question, contactez-nous par ")
        r = p.add_run()
        r.add_picture(str(icon_path), width=Inches(0.18))
        _mark_image_decorative(doc)
        p.add_run(" e-mail pour plus d'informations.")

    # Passage anglais avec balisage de langue
    p = doc.add_paragraph()
    run = p.add_run(
        "The quarterly report is available upon request. "
        "Please contact the communication department for further details.")
    run.font.name = "Arial"
    run.font.size = Pt(11)
    rPr = run._r.get_or_add_rPr()
    lang_en = parse_xml(f'<w:lang {nsdecls("w")} w:val="en-US"/>')
    rPr.append(lang_en)

    # Texte en clair (pas sous forme d'image)
    p = doc.add_paragraph()
    run = p.add_run(
        "Avis important : les indicateurs du T2 2025 "
        "seront transmis avant le 15 septembre 2025.")
    run.font.name = "Arial"
    run.font.size = Pt(11)

    # Tableau simple sans cellules fusionnees
    doc.add_heading("Répartition par service", level=3)
    table = doc.add_table(rows=3, cols=3, style="Table Grid")
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    data = [
        ["Service", "Effectif", "Budget"],
        ["Communication", "12", "45 000"],
        ["Juridique", "28", "120 000"],
    ]
    for i, row_data in enumerate(data):
        for j, cell_text in enumerate(row_data):
            cell = table.cell(i, j)
            cell.text = cell_text
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = "Arial"
                    run.font.size = Pt(10)
            if i == 0:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True
    tbl = table._tbl
    first_row = tbl.tr_lst[0]
    trPr = first_row.get_or_add_trPr()
    tblHeader = parse_xml(f'<w:tblHeader {nsdecls("w")} val="true"/>')
    trPr.append(tblHeader)

    # Annexes (Titre 2, majuscules via all_caps, pas tapees au clavier)
    h = doc.add_heading("Annexes", level=2)
    for run in h.runs:
        run.font.all_caps = True

    # Lien descriptif
    p = doc.add_paragraph()
    _add_hyperlink(
        p,
        "Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo)",
        "https://example.org/annexes-rapport-t1-2025.pdf",
    )

    # Note avec contraste suffisant (#595959 -> ratio 7:1)
    p = doc.add_paragraph()
    run = p.add_run(
        "Note : les données sont provisoires et susceptibles "
        "d'ajustements lors de la consolidation finale.")
    run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
    run.font.size = Pt(9)
    run.font.name = "Arial"

    # Proprietes du document
    doc.core_properties.title = DOCUMENT_TITLE
    doc.core_properties.author = "Sami Dupont"
    doc.core_properties.language = "fr-FR"
    doc.core_properties.subject = "Bilan communication numérique T1 2025"
    doc.core_properties.keywords = (
        "accessibilité, document bureautique, Word, rapport trimestriel, "
        "communication numérique"
    )

    output = PROJECT / "_source" / "tp-doc-accessible.docx"
    doc.save(str(output))
    _remove_quarantine(output)
    print(f"  -> {output.name}")
    return output


def _remove_quarantine(path: Path):
    """Retire le flag com.apple.quarantine sur macOS."""
    try:
        subprocess.run(
            ["xattr", "-d", "com.apple.quarantine", str(path)],
            capture_output=True,
        )
    except FileNotFoundError:
        pass


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

if __name__ == "__main__":
    print("Generation des graphiques...")
    chart_bad = generate_chart_inaccessible()
    print(f"  -> {chart_bad.name}")
    chart_good = generate_chart_accessible()
    print(f"  -> {chart_good.name}")

    print("\nGeneration des images supplementaires...")
    icon = generate_icon_enveloppe()
    print(f"  -> {icon.name}")
    orga = generate_organigramme()
    print(f"  -> {orga.name}")
    txt_img = generate_texte_image()
    print(f"  -> {txt_img.name}")

    print("\nGeneration des documents Word...")
    build_inaccessible(chart_bad, icon_path=icon, organigramme_path=orga,
                       texte_image_path=txt_img)
    build_inaccessible(chart_bad, icon_path=icon, organigramme_path=orga,
                       texte_image_path=txt_img, with_guidance=True,
                       output_name="tp-doc-aide-correction.docx")
    build_accessible(chart_good, icon_path=icon, organigramme_path=orga,
                     texte_image_path=txt_img)

    print("\nTermine.")
