"""Generateur des fichiers de l'exercice Sami.

Produit :
- _assets/graphique-inaccessible.png  (barres couleurs seules)
- _assets/graphique-accessible.png    (barres avec motifs + etiquettes)
- _assets/icone-enveloppe.png         (icone e-mail)
- _assets/organigramme.png            (organigramme du service)
- sami-doc-inaccessible.docx         (10 erreurs intentionnelles)
- sami-doc-accessible.docx           (version corrigee)
"""

import os
import subprocess
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

PROJECT = Path(__file__).resolve().parent.parent
ASSETS = PROJECT / "_assets"
ASSETS.mkdir(exist_ok=True)


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


# ------------------------------------------------------------------
# 3. Document inaccessible
# ------------------------------------------------------------------

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
    """Marque la derniere image comme decorative (alt vide)."""
    _set_image_alt(doc, alt_text="", title="")


def build_inaccessible(chart_path: Path, icon_path: Path = None,
                       organigramme_path: Path = None):
    doc = Document()

    style_normal = doc.styles["Normal"]
    style_normal.font.name = "Arial"
    style_normal.font.size = Pt(11)

    # En-tete fictif
    header = doc.sections[0].header
    hp = header.paragraphs[0]
    hp.text = "Direction des affaires juridiques"
    hp.style.font.name = "Arial"
    hp.style.font.size = Pt(9)
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Erreur 1 : faux Titre 1 (gras Arial 16, couleur bleu pour simuler un vrai titre)
    p = doc.add_paragraph()
    run = p.add_run("Introduction")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

    doc.add_paragraph(
        "Ce rapport trimestriel présente les résultats de communication "
        "numérique de la Direction des affaires juridiques pour le premier "
        "trimestre 2025. Il couvre les principaux indicateurs de performance "
        "de nos canaux digitaux."
    )

    # Erreur 5 : couleur seule (rouge #FF0000 sans gras, meme texte que l'accessible)
    p = doc.add_paragraph()
    run = p.add_run("Urgent - Retour attendu avant le 30 juin 2025")
    run.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)
    run.font.name = "Arial"
    run.font.size = Pt(11)

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

    doc.add_paragraph()

    # Erreur 3 : faux Titre 3 (gras Arial 12 souligne, couleur bleu pour simuler un vrai titre)
    p = doc.add_paragraph()
    run = p.add_run("Détail par canal")
    run.bold = True
    run.underline = True
    run.font.name = "Arial"
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

    # Erreur 7 : image sans alt + couleurs seules
    doc.add_picture(str(chart_path), width=Inches(4.5))
    last_paragraph = doc.paragraphs[-1]
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()

    # Erreur 9 : organigramme avec alt "image.png" (nom de fichier par defaut)
    if organigramme_path:
        p = doc.add_paragraph()
        run = p.add_run("Organisation du service")
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

        doc.add_picture(str(organigramme_path), width=Inches(5.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        _set_image_alt(doc, alt_text="image.png")

        doc.add_paragraph()

    # Erreur 10 : icone redondante avec alt "E-mail" au lieu de decoratif
    if icon_path:
        p = doc.add_paragraph()
        run = p.add_run("Contact")
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

        p = doc.add_paragraph()
        p.add_run("Pour toute question, contactez-nous par ")
        r = p.add_run()
        r.add_picture(str(icon_path), width=Inches(0.18))
        _set_image_alt(doc, alt_text="E-mail")
        p.add_run(" e-mail pour plus d'informations.")

    doc.add_paragraph()

    # Section Annexes (faux titre aussi, meme apparence)
    p = doc.add_paragraph()
    run = p.add_run("Annexes")
    run.bold = True
    run.font.name = "Arial"
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

    # Erreur 8 : lien non descriptif
    p = doc.add_paragraph("Pour accéder aux annexes, ")
    run = p.add_run("cliquez ici")
    run.font.color.rgb = RGBColor(0x00, 0x00, 0xFF)
    run.underline = True
    p.add_run(".")

    # Erreur 6 : contraste ambigu (gris #767676)
    p = doc.add_paragraph()
    run = p.add_run("Note : les données sont provisoires et susceptibles "
                     "d’ajustements lors de la consolidation finale.")
    run.font.color.rgb = RGBColor(0x76, 0x76, 0x76)
    run.font.size = Pt(9)
    run.font.name = "Arial"

    # Pas de proprietes document (erreur bonus)
    output = PROJECT / "_source" / "sami-doc-inaccessible.docx"
    doc.save(str(output))
    _remove_quarantine(output)
    print(f"  -> {output.name}")
    return output


# ------------------------------------------------------------------
# 3. Document accessible
# ------------------------------------------------------------------

def build_accessible(chart_path: Path, icon_path: Path = None,
                     organigramme_path: Path = None):
    doc = Document()

    # Police par defaut : Calibri (fallback Marianne)
    style_normal = doc.styles["Normal"]
    style_normal.font.name = "Arial"
    style_normal.font.size = Pt(11)

    # Langue du document : fr-FR sur le style Normal (propage a tout le texte)
    rPr = style_normal.element.get_or_add_rPr()
    lang_el = rPr.find(qn("w:lang"))
    if lang_el is None:
        lang_el = parse_xml(f'<w:lang {nsdecls("w")} w:val="fr-FR" w:eastAsia="fr-FR" w:bidi="fr-FR"/>')
        rPr.append(lang_el)
    else:
        lang_el.set(qn("w:val"), "fr-FR")

    # Configurer les styles de titre
    for level, size in [(1, 16), (2, 14), (3, 12)]:
        style = doc.styles[f"Heading {level}"]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0x00, 0x00, 0x91)

    # En-tete
    header = doc.sections[0].header
    hp = header.paragraphs[0]
    hp.text = "Direction des affaires juridiques"
    hp.style.font.name = "Arial"
    hp.style.font.size = Pt(9)
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # Titre 1
    doc.add_heading("Introduction", level=1)

    doc.add_paragraph(
        "Ce rapport trimestriel présente les résultats de communication "
        "numérique de la Direction des affaires juridiques pour le premier "
        "trimestre 2025. Il couvre les principaux indicateurs de performance "
        "de nos canaux digitaux."
    )

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

    doc.add_paragraph()

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

    doc.add_paragraph()

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
            "internationales. Chaque bureau est rattache directement "
            "a la direction.")
        run.font.name = "Arial"
        run.font.size = Pt(10)

        doc.add_paragraph()

    # Icone decorative + paragraphe contact
    if icon_path:
        doc.add_heading("Contact", level=2)

        p = doc.add_paragraph()
        p.add_run("Pour toute question, contactez-nous par ")
        r = p.add_run()
        r.add_picture(str(icon_path), width=Inches(0.18))
        _mark_image_decorative(doc)
        p.add_run(" e-mail pour plus d'informations.")

    doc.add_paragraph()

    # Annexes (Titre 2)
    doc.add_heading("Annexes", level=2)

    # Lien descriptif
    p = doc.add_paragraph()
    run = p.add_run(
        "Consulter les annexes du rapport T1 2025 (PDF, 1,2 Mo)")
    run.font.color.rgb = RGBColor(0x00, 0x00, 0xFF)
    run.underline = True

    # Note avec contraste suffisant (#595959 -> ratio 7:1)
    p = doc.add_paragraph()
    run = p.add_run(
        "Note : les données sont provisoires et susceptibles "
        "d'ajustements lors de la consolidation finale.")
    run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
    run.font.size = Pt(9)
    run.font.name = "Arial"

    # Proprietes du document
    doc.core_properties.title = "Rapport trimestriel – Bilan T1 2025"
    doc.core_properties.author = "Sami Dupont"
    doc.core_properties.language = "fr-FR"
    doc.core_properties.subject = "Bilan communication numérique T1 2025"

    output = PROJECT / "_source" / "sami-doc-accessible.docx"
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

    print("\nGeneration des documents Word...")
    build_inaccessible(chart_bad, icon_path=icon, organigramme_path=orga)
    build_accessible(chart_good, icon_path=icon, organigramme_path=orga)

    print("\nTermine.")
