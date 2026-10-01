"""Tests d'intégration XML des trois DOCX de l'exercice Sami."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import re
from zipfile import ZipFile

from docx import Document

from exercice_sami_matrice import load_sami_matrix
from generate_exercice_sami import build_accessible, build_inaccessible


PROJECT_ROOT = Path(__file__).parent.parent


def _archive_text(path: Path, member: str) -> str:
    with ZipFile(path) as archive:
        return archive.read(member).decode("utf-8")


def _archive_members(path: Path) -> set[str]:
    with ZipFile(path) as archive:
        return set(archive.namelist())


def _paragraph_region(path: Path, start: str, end: str):
    paragraphs = Document(path).paragraphs
    start_index = next(
        index for index, paragraph in enumerate(paragraphs) if paragraph.text == start
    )
    end_index = next(
        index
        for index, paragraph in enumerate(paragraphs[start_index:], start_index)
        if paragraph.text == end
    )
    return paragraphs[start_index : end_index + 1]


def test_le_docx_guide_consomme_directement_le_libelle_de_la_matrice(tmp_path):
    matrix = deepcopy(load_sami_matrix())
    control = next(item for item in matrix["controles"] if item["id"] == "P-01")
    control["intitule"] = "Libellé injecté depuis la matrice"

    output = build_inaccessible(
        PROJECT_ROOT / "_assets" / "graphique-inaccessible.png",
        with_guidance=True,
        output_name="guide.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )

    comments = _archive_text(output, "word/comments.xml")
    assert "Libellé injecté depuis la matrice" in comments


def test_le_corrige_porte_un_titre_principal_et_le_controle_p01(tmp_path):
    matrix = deepcopy(load_sami_matrix())
    control = next(item for item in matrix["controles"] if item["id"] == "P-01")
    control["intitule"] = "Titre principal piloté par la matrice"

    output = build_accessible(
        PROJECT_ROOT / "_assets" / "graphique-accessible.png",
        matrix=matrix,
        output_dir=tmp_path,
    )

    document = Document(output)
    title = next(
        paragraph
        for paragraph in document.paragraphs
        if paragraph.text == "Rendre un document Word accessible"
    )
    assert title.style.name == "Title"
    assert "Titre principal piloté par la matrice" in "\n".join(
        paragraph.text for paragraph in document.paragraphs
    )


def test_la_hierarchie_p02_est_fautive_au_depart_et_corrigee(tmp_path):
    matrix = load_sami_matrix()
    control = next(item for item in matrix["controles"] if item["id"] == "P-02")
    heading_text = f"{control['id']} - {control['intitule']}"
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    chart_good = PROJECT_ROOT / "_assets" / "graphique-accessible.png"

    inaccessible = build_inaccessible(
        chart_bad,
        output_name="inaccessible.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    corrected = build_accessible(chart_good, matrix=matrix, output_dir=tmp_path)

    bad_doc = Document(inaccessible)
    good_doc = Document(corrected)

    def style_for(document, text):
        return next(
            paragraph.style.name
            for paragraph in document.paragraphs
            if paragraph.text == text
        )

    station_title = next(
        block["titre"] for block in matrix["sequence"] if block["id"] == "station-1"
    )
    assert style_for(bad_doc, "Rendre un document Word accessible") == "Normal"
    assert style_for(bad_doc, station_title) == "Heading 1"
    assert style_for(bad_doc, heading_text) == "Heading 4"
    assert style_for(good_doc, heading_text) == "Heading 2"

    bad_heading = next(
        paragraph for paragraph in bad_doc.paragraphs if paragraph.text == heading_text
    )
    good_heading = next(
        paragraph for paragraph in good_doc.paragraphs if paragraph.text == heading_text
    )
    bad_numbering = bad_heading._p.pPr.numPr
    good_numbering = good_heading._p.pPr.numPr
    assert bad_numbering is not None
    assert good_numbering is not None
    assert bad_numbering.ilvl.val == 3
    assert good_numbering.ilvl.val == 1
    for sibling in ("P-01", "P-03", "P-04", "P-05"):
        sibling_control = next(
            item for item in matrix["controles"] if item["id"] == sibling
        )
        sibling_text = f"{sibling} - {sibling_control['intitule']}"
        assert style_for(bad_doc, sibling_text) == "Heading 2"
        assert style_for(good_doc, sibling_text) == "Heading 2"


def test_les_titres_hors_station_un_restant_ne_creent_pas_d_occurrence_cachee(
    tmp_path,
):
    matrix = load_sami_matrix()
    output = build_inaccessible(
        PROJECT_ROOT / "_assets" / "graphique-inaccessible.png",
        icon_path=PROJECT_ROOT / "_assets" / "icone-enveloppe.png",
        organigramme_path=PROJECT_ROOT / "_assets" / "organigramme.png",
        output_name="inaccessible.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    document = Document(output)
    expected_styles = {
        "Introduction": "Heading 1",
        "Résultats du trimestre": "Heading 2",
        "Détail par canal": "Heading 3",
        "Organisation du service": "Heading 2",
        "Contact": "Heading 2",
        "Répartition par service": "Heading 3",
        "ANNEXES": "Heading 2",
    }

    for text, style_name in expected_styles.items():
        paragraph = next(item for item in document.paragraphs if item.text == text)
        assert paragraph.style.name == style_name


def test_la_partie_non_migree_annexes_conserve_son_defaut_de_casse(tmp_path):
    matrix = load_sami_matrix()
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    chart_good = PROJECT_ROOT / "_assets" / "graphique-accessible.png"
    inaccessible = build_inaccessible(
        chart_bad,
        output_name="inaccessible.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    corrected = build_accessible(chart_good, matrix=matrix, output_dir=tmp_path)

    inaccessible_annexes = next(
        item for item in Document(inaccessible).paragraphs if item.text == "ANNEXES"
    )
    corrected_annexes = next(
        item for item in Document(corrected).paragraphs if item.text == "Annexes"
    )

    assert "w:caps" not in inaccessible_annexes._p.xml
    assert "w:caps" in corrected_annexes._p.xml


def test_p03_guide_le_sommaire_manuel_et_le_corrige_le_rend_actualisable(
    tmp_path,
):
    matrix = load_sami_matrix()
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    chart_good = PROJECT_ROOT / "_assets" / "graphique-accessible.png"
    inaccessible = build_inaccessible(
        chart_bad,
        output_name="inaccessible.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    guided = build_inaccessible(
        chart_bad,
        with_guidance=True,
        output_name="guide.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    corrected = build_accessible(chart_good, matrix=matrix, output_dir=tmp_path)

    inaccessible_xml = _archive_text(inaccessible, "word/document.xml")
    guided_xml = _archive_text(guided, "word/document.xml")
    corrected_xml = _archive_text(corrected, "word/document.xml")
    comments = _archive_text(guided, "word/comments.xml")

    assert "TOC \\o" not in inaccessible_xml
    assert "TOC \\o" not in guided_xml
    assert "TOC \\o" in corrected_xml
    assert comments.count("Document — P-03") == 1


def test_p04_remplace_les_marqueurs_saisis_par_des_listes_natives(tmp_path):
    matrix = load_sami_matrix()
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    chart_good = PROJECT_ROOT / "_assets" / "graphique-accessible.png"
    guided = build_inaccessible(
        chart_bad,
        with_guidance=True,
        output_name="guide.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    corrected = build_accessible(chart_good, matrix=matrix, output_dir=tmp_path)

    guided_doc = Document(guided)
    corrected_doc = Document(corrected)
    bad_bullet = next(
        paragraph
        for paragraph in guided_doc.paragraphs
        if "Augmenter le trafic de 10 %" in paragraph.text
    )
    good_bullet = next(
        paragraph
        for paragraph in corrected_doc.paragraphs
        if paragraph.text == "Augmenter le trafic de 10 %"
    )
    bad_number = next(
        paragraph
        for paragraph in guided_doc.paragraphs
        if "Refonte de la page d'accueil" in paragraph.text
    )
    good_number = next(
        paragraph
        for paragraph in corrected_doc.paragraphs
        if paragraph.text == "Refonte de la page d'accueil"
    )
    comments = _archive_text(guided, "word/comments.xml")

    assert bad_bullet.style.name == "Normal"
    assert bad_number.style.name == "Normal"
    assert good_bullet.style.name == "List Bullet"
    assert good_number.style.name == "List Number"
    assert comments.count("P-04 -") == 1


def test_p05_remplace_les_artifices_par_des_fonctions_de_mise_en_page(tmp_path):
    matrix = load_sami_matrix()
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    chart_good = PROJECT_ROOT / "_assets" / "graphique-accessible.png"
    guided = build_inaccessible(
        chart_bad,
        with_guidance=True,
        output_name="guide.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    corrected = build_accessible(chart_good, matrix=matrix, output_dir=tmp_path)

    start = "Mise en page robuste"
    end = "Fin de la zone Mise en page robuste."
    bad_region = _paragraph_region(guided, start, end)
    good_region = _paragraph_region(corrected, start, end)
    bad_xml = "".join(paragraph._p.xml for paragraph in bad_region)
    good_xml = "".join(paragraph._p.xml for paragraph in good_region)
    corrected_xml = _archive_text(corrected, "word/document.xml")
    comments = _archive_text(guided, "word/comments.xml")

    assert sum(not paragraph.text for paragraph in bad_region) >= 4
    assert any("  " in paragraph.text for paragraph in bad_region)
    assert "<w:tab" in bad_xml
    assert "<w:br" in bad_xml
    assert "w:pageBreakBefore" not in bad_xml
    assert 'w:num="2"' not in _archive_text(guided, "word/document.xml")

    assert not any("  " in paragraph.text for paragraph in good_region)
    assert "<w:tab" not in good_xml
    assert "<w:br" not in good_xml
    assert "w:pageBreakBefore" in good_xml
    assert "<w:spacing" in good_xml
    assert "<w:ind" in good_xml
    assert 'w:num="2"' in corrected_xml
    assert comments.count("P-05 -") == 1

    bad_text = re.sub(r"\s+", " ", " ".join(p.text for p in bad_region)).strip()
    good_text = re.sub(r"\s+", " ", " ".join(p.text for p in good_region)).strip()
    assert bad_text == good_text


def test_le_titre_de_station_est_lu_dans_la_matrice(tmp_path):
    matrix = deepcopy(load_sami_matrix())
    station = next(item for item in matrix["sequence"] if item["id"] == "station-1")
    station["titre"] = "Titre de station injecté depuis la matrice"

    output = build_accessible(
        PROJECT_ROOT / "_assets" / "graphique-accessible.png",
        matrix=matrix,
        output_dir=tmp_path,
    )

    heading = next(
        paragraph
        for paragraph in Document(output).paragraphs
        if paragraph.text == "Titre de station injecté depuis la matrice"
    )
    assert heading.style.name == "Heading 1"


def test_les_builders_lisent_les_noms_des_trois_versions_dans_la_matrice(tmp_path):
    matrix = deepcopy(load_sami_matrix())
    matrix["identite_editoriale"]["versions"] = {
        "inaccessible": "depart.docx",
        "avec_pistes": "guide.docx",
        "corrigee": "corrige.docx",
    }
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    chart_good = PROJECT_ROOT / "_assets" / "graphique-accessible.png"

    inaccessible = build_inaccessible(chart_bad, matrix=matrix, output_dir=tmp_path)
    guided = build_inaccessible(
        chart_bad, with_guidance=True, matrix=matrix, output_dir=tmp_path
    )
    corrected = build_accessible(chart_good, matrix=matrix, output_dir=tmp_path)

    assert [inaccessible.name, guided.name, corrected.name] == [
        "depart.docx",
        "guide.docx",
        "corrige.docx",
    ]


def test_le_guide_contient_une_piste_par_occurrence_de_la_station_un(tmp_path):
    matrix = load_sami_matrix()
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    inaccessible = build_inaccessible(
        chart_bad,
        output_name="inaccessible.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    guided = build_inaccessible(
        chart_bad,
        with_guidance=True,
        output_name="guide.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )
    corrected = build_accessible(
        PROJECT_ROOT / "_assets" / "graphique-accessible.png",
        matrix=matrix,
        output_dir=tmp_path,
    )
    comments = _archive_text(guided, "word/comments.xml")
    controls = [
        control for control in matrix["controles"] if control["station"] == "station-1"
    ]

    for control in controls:
        assert comments.count(f"{control['id']} -") == control["occurrences_attendues"]
        assert control["regle"] in comments
        assert control["action_attendue"] in comments
    assert sum(comments.count(f"{control['id']} -") for control in controls) == 5
    assert "word/comments.xml" not in _archive_members(inaccessible)
    assert "word/comments.xml" not in _archive_members(corrected)


def test_les_trois_versions_partagent_le_contenu_pedagogique_de_la_station_un(
    tmp_path,
):
    matrix = load_sami_matrix()
    chart_bad = PROJECT_ROOT / "_assets" / "graphique-inaccessible.png"
    paths = [
        build_inaccessible(
            chart_bad,
            output_name="inaccessible.docx",
            matrix=matrix,
            output_dir=tmp_path,
        ),
        build_inaccessible(
            chart_bad,
            with_guidance=True,
            output_name="guide.docx",
            matrix=matrix,
            output_dir=tmp_path,
        ),
        build_accessible(
            PROJECT_ROOT / "_assets" / "graphique-accessible.png",
            matrix=matrix,
            output_dir=tmp_path,
        ),
    ]
    documents = [Document(path) for path in paths]
    controls = [
        control for control in matrix["controles"] if control["station"] == "station-1"
    ]
    expected_paragraphs = {"Rendre un document Word accessible"}
    for control in controls:
        expected_paragraphs.update(
            {
                f"{control['id']} - {control['intitule']}",
                f"Problème : {control['defaut']}",
                f"Pourquoi : {control['impact']}",
                f"Règle : {control['regle']}",
                f"Dans Word : {control['procedure_word']}",
                f"Dans LibreOffice Writer : {control['procedure_writer']}",
                f"À faire : {control['action_attendue']}",
                f"Preuve : {control['preuve']['attendu']}",
            }
        )

    for document in documents:
        paragraphs = {paragraph.text for paragraph in document.paragraphs}
        assert expected_paragraphs <= paragraphs
        normalized = re.sub(
            r"\s+",
            " ",
            " ".join(paragraph.text for paragraph in document.paragraphs),
        )
        for content in (
            "Augmenter le trafic de 10 %",
            "Refonte de la page d'accueil",
            "Retrait du paragraphe aligné avec",
            "Ligne principale Suite sur un paragraphe distinct",
            "Début de la page suivante",
            "Colonne gauche : structure Colonne droite : navigation",
        ):
            assert content in normalized


def test_les_pistes_documentaires_sont_ancrees_dans_le_corps(tmp_path):
    matrix = load_sami_matrix()
    output = build_inaccessible(
        PROJECT_ROOT / "_assets" / "graphique-inaccessible.png",
        with_guidance=True,
        output_name="guide.docx",
        matrix=matrix,
        output_dir=tmp_path,
    )

    members = _archive_members(output)
    for member in members:
        if member.startswith("word/header") or member.startswith("word/footer"):
            xml = _archive_text(output, member)
            assert "commentRangeStart" not in xml
            assert "commentReference" not in xml

    comments = _archive_text(output, "word/comments.xml")
    assert "Document — P-03" in comments
    assert "Document — Critère 18" in comments
