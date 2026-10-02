"""Contrats structurels de la partie II pilotée par la matrice Sami."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from exercice_sami_matrice import load_sami_matrix
from igpde_dsfr_components import create_presentation
from slides import SlideContext, discover_slides, load_slide_module


ROOT = Path(__file__).parent.parent
SLIDES_DIR = ROOT / "scripts" / "slides"
STATION_MODULES = {
    "station-1": (
        "08_pilier1-styles-titre.py",
        "09_pilier1-listes.py",
        "10_pilier1-tableaux-flottants.py",
    ),
    "station-2": (
        "11_pilier2-contraste.py",
        "12_pilier2-couleur-seule.py",
        "13_pilier3-alt-text.py",
        "14_pilier3-liens-infos.py",
    ),
    "station-3": (
        "15_exercice-sami.py",
        "16_pilier4-langue-lisibilite.py",
        "17_pilier4-espaces-clignotants.py",
        "18_pilier5-avant-publier.py",
    ),
    "station-4": (
        "19_pilier5-verificateur.py",
        "20_export-pdf-accessible.py",
        "21_etude-cas-sophie.py",
    ),
    "station-5": (
        "22_par-ou-commencer.py",
        "26_checklist-21-criteres.py",
        "26a_checklist-exercice-2.py",
    ),
}
CHECKLIST_MODULES = (
    "26b_checklist-autres.py",
    "26c_checklist-autres-2.py",
    "26d_checklist-station-5-signales.py",
)
SYNTHESIS_MODULE = "26e_synthese-matinee.py"
DETAIL_MODULES = tuple(
    filename for modules in STATION_MODULES.values() for filename in modules[1:]
)


def _slide_text(filename: str) -> str:
    slide = _build_slide(filename)
    texts = []
    for shape in slide.shapes:
        if getattr(shape, "has_text_frame", False) and shape.text.strip():
            texts.append(shape.text)
        if getattr(shape, "has_table", False):
            texts.extend(
                cell.text
                for row in shape.table.rows
                for cell in row.cells
                if cell.text.strip()
            )
    return "\n".join(texts)


def _build_slide(filename: str):
    prs, layouts = create_presentation()
    ctx = SlideContext(
        page_num=1,
        date="9 octobre 2026",
        footer_base="Formation 102846",
        formation_code="102846",
    )
    return load_slide_module(SLIDES_DIR / filename).build(prs, layouts, ctx)


def test_les_modules_de_station_ne_recopient_pas_les_identifiants_normatifs():
    matrix = load_sami_matrix()
    normative_labels = [control["intitule"] for control in matrix["controles"]]
    for filename in (*sum(STATION_MODULES.values(), ()), *CHECKLIST_MODULES):
        source = (SLIDES_DIR / filename).read_text(encoding="utf-8")
        assert "sami_slide_data" in source, filename
        assert not re.search(r"\b[PCS]-\d{2}\b", source), filename
        assert all(label not in source for label in normative_labels), filename


def test_chaque_station_rend_les_controles_de_la_matrice_dans_le_bon_ordre():
    matrix = load_sami_matrix()
    for station_id, modules in STATION_MODULES.items():
        text = "\n".join(_slide_text(filename) for filename in modules)
        controls = [
            control
            for control in matrix["controles"]
            if control["station"] == station_id
        ]
        positions = []
        for control in controls:
            assert control["intitule"] in text
            positions.append(text.index(control["id"]))
        assert positions == sorted(positions)


def test_les_stations_suivent_le_preambule_et_precedent_la_partie_web():
    filenames = [path.name for path in discover_slides()]
    ordered_modules = sum(STATION_MODULES.values(), ()) + CHECKLIST_MODULES
    positions = [filenames.index(filename) for filename in ordered_modules]
    assert filenames.index("05_quiz-flash-a-vs-b.py") < positions[0]
    assert positions == sorted(positions)
    assert positions[-1] < filenames.index("28_chapitre-easy-checks.py")


def test_les_checklists_affichent_toutes_les_lignes_canoniques():
    matrix = load_sami_matrix()
    text = "\n".join(_slide_text(filename) for filename in CHECKLIST_MODULES)
    for control in matrix["controles"]:
        assert control["checklist"] in text


def test_la_synthese_separe_la_partie_2_de_la_partie_web_sans_identifiant():
    filenames = [path.name for path in discover_slides()]
    assert filenames.index(CHECKLIST_MODULES[-1]) < filenames.index(SYNTHESIS_MODULE)
    assert filenames.index(SYNTHESIS_MODULE) < filenames.index(
        "28_chapitre-easy-checks.py"
    )
    text = _slide_text(SYNTHESIS_MODULE)
    assert not re.search(r"\b[PCS]-\d{2}\b", text)


def test_les_details_presentent_word_avant_writer():
    for filename in DETAIL_MODULES:
        text = _slide_text(filename)
        assert "Dans Word" in text, filename
        assert "Dans Writer" in text, filename
        assert text.index("Dans Word") < text.index("Dans Writer"), filename


def test_les_notes_de_station_portent_minutage_variantes_et_preuves():
    matrix = load_sami_matrix()
    durations = {block["id"]: block["duree_minutes"] for block in matrix["sequence"]}
    for station_id, modules in STATION_MODULES.items():
        for filename in modules:
            notes = _build_slide(filename).notes_slide.notes_text_frame.text
            assert f"{durations[station_id]} minutes" in notes, filename
            assert "Parcours guidé" in notes, filename
            assert "Variante autonome" in notes, filename
            assert "Preuves attendues" in notes, filename


def test_le_quiz_final_reste_absent():
    filenames = {path.name for path in discover_slides()}
    assert "23_quiz-final.py" not in filenames
    assert "23b_quiz-final-reponses.py" not in filenames
