"""Tests du contrat canonique de l'exercice Sami."""

from __future__ import annotations

from copy import deepcopy
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from exercice_sami_matrice import (  # noqa: E402
    SamiMatrixError,
    load_coverage_codes,
    load_sami_matrix,
    validate_editorial_identity,
    validate_occurrence_manifest,
    validate_sami_matrix,
)


EXPECTED_SEQUENCE = [
    ("preambule", 5),
    ("station-1", 17),
    ("station-2", 15),
    ("station-3", 15),
    ("station-4", 15),
    ("station-5", 18),
    ("marge-remise", 5),
]
EXPECTED_CONTROLS = [
    *(f"P-{index:02d}" for index in range(1, 21)),
    "C-01",
    "C-02",
    *(f"S-{index:02d}" for index in range(1, 6)),
]


def test_normalise_l_absence_de_la_matrice_en_erreur_metier(tmp_path):
    missing_path = tmp_path / "matrice-absente.yml"

    with pytest.raises(SamiMatrixError, match="Matrice illisible"):
        load_sami_matrix(missing_path)


def test_normalise_l_absence_de_la_couverture_en_erreur_metier(tmp_path):
    missing_path = tmp_path / "couverture-absente.md"

    with pytest.raises(SamiMatrixError, match="Couverture illisible"):
        load_coverage_codes(missing_path)


def test_refuse_une_cle_yaml_dupliquee(tmp_path):
    matrix_path = tmp_path / "matrice.yml"
    matrix_path.write_text("version: 1\nversion: 2\n", encoding="utf-8")

    with pytest.raises(SamiMatrixError, match="clé YAML dupliquée"):
        load_sami_matrix(matrix_path)


def test_normalise_une_cle_yaml_non_hachable(tmp_path):
    matrix_path = tmp_path / "matrice.yml"
    matrix_path.write_text("? [a, b]\n: valeur\n", encoding="utf-8")

    with pytest.raises(SamiMatrixError, match="clé YAML invalide"):
        load_sami_matrix(matrix_path)


def test_charge_la_sequence_et_tous_les_controles_dans_l_ordre():
    matrix = load_sami_matrix()

    assert [
        (block["id"], block["duree_minutes"]) for block in matrix["sequence"]
    ] == EXPECTED_SEQUENCE
    assert sum(block["duree_minutes"] for block in matrix["sequence"]) == 90
    assert [control["id"] for control in matrix["controles"]] == EXPECTED_CONTROLS
    assert matrix["identite_editoriale"]["versions"] == {
        "inaccessible": "tp-doc-inaccessible.docx",
        "avec_pistes": "tp-doc-aide-correction.docx",
        "corrigee": "tp-doc-accessible.docx",
    }
    covered_codes = {
        code
        for control in matrix["controles"]
        for code in control["references_pedagogiques"]
    }
    assert covered_codes == load_coverage_codes()


def test_les_anciens_contrats_renvoient_a_la_matrice_sans_liste_normative():
    forbidden_patterns = (
        "21 critères",
        "25 min",
        "25 minutes",
        "sans checklist",
        "sans filet",
        "rapport trimestriel",
        "102638",
    )
    for relative_path in (
        "_source/exercice-sami-spec.md",
        "_source/exercice-sami-diff.md",
    ):
        content = (PROJECT_ROOT / relative_path).read_text(encoding="utf-8")
        normalized = content.casefold()
        assert "_source/exercice-sami-matrice.yml" in content
        assert "source normative" in normalized
        for pattern in forbidden_patterns:
            assert pattern.casefold() not in normalized


def test_le_generateur_ne_conserve_plus_les_marqueurs_normatifs_historiques():
    content = (PROJECT_ROOT / "scripts/generate_exercice_sami.py").read_text(
        encoding="utf-8"
    )

    assert "21 erreurs" not in content
    assert "# Erreur " not in content
    assert "rapport trimestriel" not in content.casefold()


def test_refuse_une_sequence_dont_le_total_n_est_pas_90_minutes():
    matrix = deepcopy(load_sami_matrix())
    matrix["sequence"][0]["duree_minutes"] = 4

    with pytest.raises(SamiMatrixError, match="90 minutes"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize("invalid_version", [None, 2, "1", True])
def test_refuse_une_version_de_matrice_non_canonique(invalid_version):
    matrix = deepcopy(load_sami_matrix())
    matrix["version"] = invalid_version

    with pytest.raises(SamiMatrixError, match="version 1"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize("invalid_title", [None, "", 42])
def test_refuse_un_titre_de_sequence_absent_ou_mal_type(invalid_title):
    matrix = deepcopy(load_sami_matrix())
    matrix["sequence"][0]["titre"] = invalid_title

    with pytest.raises(SamiMatrixError, match="preambule.*titre.*chaîne"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize("invalid_duration", [0, -1, True, 1.5])
def test_refuse_une_duree_qui_n_est_pas_un_entier_strictement_positif(
    invalid_duration,
):
    matrix = deepcopy(load_sami_matrix())
    matrix["sequence"][0]["duree_minutes"] = invalid_duration
    matrix["sequence"][1]["duree_minutes"] += 5 - invalid_duration

    with pytest.raises(SamiMatrixError, match="entier strictement positif"):
        validate_sami_matrix(matrix)


def test_refuse_une_sequence_de_90_minutes_avec_un_huitieme_bloc():
    matrix = deepcopy(load_sami_matrix())
    matrix["sequence"][5]["duree_minutes"] -= 1
    matrix["sequence"].append(
        {"id": "bloc-imprevu", "titre": "Bloc imprévu", "duree_minutes": 1}
    )

    with pytest.raises(SamiMatrixError, match="sept blocs"):
        validate_sami_matrix(matrix)


def test_refuse_un_identifiant_de_controle_duplique():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"].append(deepcopy(matrix["controles"][0]))

    with pytest.raises(SamiMatrixError, match="dupliqué.*P-01"):
        validate_sami_matrix(matrix)


def test_refuse_un_identifiant_de_controle_mal_forme():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0]["id"] = "X"

    with pytest.raises(SamiMatrixError, match="identifiant inconnu : X"):
        validate_sami_matrix(matrix)


def test_refuse_un_champ_obligatoire_absent_sur_un_controle_pratique():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0].pop("action_attendue", None)

    with pytest.raises(SamiMatrixError, match="P-01.*action_attendue"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("surfaces", None),
        ("references_pedagogiques", None),
        ("transformations_editoriales", "type-de-transformation"),
    ],
)
def test_refuse_une_collection_de_controle_mal_typee(field, value):
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0][field] = value

    with pytest.raises(SamiMatrixError, match=rf"P-01.*{field}.*liste"):
        validate_sami_matrix(matrix)


def test_refuse_une_preuve_sans_mode():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0]["preuve"].pop("mode")

    with pytest.raises(SamiMatrixError, match="P-01.*preuve"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("intitule", 42),
        ("impact", ["impact"]),
        ("action_attendue", True),
    ],
)
def test_refuse_un_champ_textuel_mal_type_sur_un_controle_pratique(field, value):
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0][field] = value

    with pytest.raises(SamiMatrixError, match=rf"P-01.*{field}.*chaîne"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize(("field", "value"), [("mode", []), ("attendu", 42)])
def test_refuse_un_champ_de_preuve_qui_n_est_pas_une_chaine(field, value):
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0]["preuve"][field] = value

    with pytest.raises(SamiMatrixError, match=rf"P-01.*preuve.{field}.*chaîne"):
        validate_sami_matrix(matrix)


def test_refuse_un_defaut_sur_un_controle_sans_occurrence():
    matrix = deepcopy(load_sami_matrix())
    control = next(item for item in matrix["controles"] if item["id"] == "P-20")
    control["defaut"] = "Défaut ajouté hors du contrat"

    with pytest.raises(SamiMatrixError, match="P-20.*occurrence à zéro"):
        validate_sami_matrix(matrix)


def test_refuse_un_nombre_d_occurrences_booleen_dans_la_matrice():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0]["occurrences_attendues"] = True

    with pytest.raises(SamiMatrixError, match="P-01.*entier positif ou nul"):
        validate_sami_matrix(matrix)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("station", "station-1"),
        ("guide", "station-1/hors-perimetre"),
        (
            "surfaces",
            [
                "checklist_stagiaire",
                "checklist_formateur",
                "slides_checklist",
                "notes_formateur",
                "guide",
            ],
        ),
    ],
)
def test_refuse_une_surface_interdite_pour_un_controle_signale(field, value):
    matrix = deepcopy(load_sami_matrix())
    control = next(item for item in matrix["controles"] if item["id"] == "S-01")
    control[field] = value

    with pytest.raises(SamiMatrixError, match="S-01.*surfaces réservées"):
        validate_sami_matrix(matrix)


def test_refuse_un_champ_non_applicable_non_nul_sur_un_controle_signale():
    matrix = deepcopy(load_sami_matrix())
    control = next(item for item in matrix["controles"] if item["id"] == "S-01")
    control["action_attendue"] = []

    with pytest.raises(SamiMatrixError, match="S-01.*surfaces réservées"):
        validate_sami_matrix(matrix)


def test_refuse_un_controle_rattache_a_la_mauvaise_station():
    matrix = deepcopy(load_sami_matrix())
    control = next(item for item in matrix["controles"] if item["id"] == "P-06")
    control["station"] = "station-1"

    with pytest.raises(SamiMatrixError, match="P-06.*station-2"):
        validate_sami_matrix(matrix)


def test_refuse_un_niveau_incoherent_avec_l_identifiant():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0]["niveau"] = "C"

    with pytest.raises(SamiMatrixError, match="P-01.*niveau P"):
        validate_sami_matrix(matrix)


def test_refuse_une_reference_pedagogique_locale_inconnue():
    matrix = deepcopy(load_sami_matrix())
    matrix["controles"][0]["references_pedagogiques"] = ["MS-99"]

    with pytest.raises(SamiMatrixError, match="MS-99.*inconnue"):
        validate_sami_matrix(matrix)


def test_refuse_un_defaut_declare_hors_de_la_matrice():
    matrix = load_sami_matrix()
    manifest = {
        control["id"]: control["occurrences_attendues"]
        for control in matrix["controles"]
        if control["occurrences_attendues"] > 0
    }
    manifest["P-99"] = 1

    with pytest.raises(SamiMatrixError, match="P-99.*hors matrice"):
        validate_occurrence_manifest(matrix, manifest)


def test_normalise_une_matrice_mal_typee_en_erreur_metier():
    with pytest.raises(SamiMatrixError, match="racine.*objet"):
        validate_sami_matrix([])


def test_normalise_un_manifeste_mal_type_en_erreur_metier():
    matrix = load_sami_matrix()

    with pytest.raises(SamiMatrixError, match="manifeste.*objet"):
        validate_occurrence_manifest(matrix, [])


@pytest.mark.parametrize("invalid_count", [True, 1.0, -1])
def test_refuse_un_compte_d_occurrences_mal_type_ou_negatif(invalid_count):
    matrix = load_sami_matrix()
    manifest = {
        control["id"]: control["occurrences_attendues"]
        for control in matrix["controles"]
    }
    manifest["P-01"] = invalid_count

    with pytest.raises(SamiMatrixError, match="P-01.*entier positif ou nul"):
        validate_occurrence_manifest(matrix, manifest)


def test_refuse_une_difference_editoriale_non_declaree():
    matrix = load_sami_matrix()
    unchanged = [{"id": "bloc-1", "texte": "IGPDE"}]
    corrected = [
        {
            "id": "bloc-1",
            "texte": "Institut de la gestion publique et du développement "
            "économique (IGPDE)",
            "transformation": {
                "controle": "P-18",
                "type": "developpement_acronyme_premiere_occurrence",
            },
        }
    ]
    versions = {
        "inaccessible": deepcopy(unchanged),
        "avec_pistes": deepcopy(unchanged),
        "corrigee": corrected,
    }
    validate_editorial_identity(matrix, versions)
    versions["corrigee"][0].pop("transformation")

    with pytest.raises(SamiMatrixError, match="différence éditoriale non déclarée"):
        validate_editorial_identity(matrix, versions)


def test_normalise_un_bloc_editorial_incomplet_en_erreur_metier():
    matrix = load_sami_matrix()
    versions = {
        "inaccessible": [{"id": "bloc-1", "texte": "Texte"}],
        "avec_pistes": [{"id": "bloc-1"}],
        "corrigee": [{"id": "bloc-1", "texte": "Texte"}],
    }

    with pytest.raises(SamiMatrixError, match="avec_pistes.*texte.*chaîne"):
        validate_editorial_identity(matrix, versions)


def test_refuse_un_faux_developpement_d_acronyme():
    matrix = load_sami_matrix()
    versions = {
        "inaccessible": [{"id": "bloc-1", "texte": "IGPDE"}],
        "avec_pistes": [{"id": "bloc-1", "texte": "IGPDE"}],
        "corrigee": [
            {
                "id": "bloc-1",
                "texte": "Contenu sans rapport",
                "transformation": {
                    "controle": "P-18",
                    "type": "developpement_acronyme_premiere_occurrence",
                },
            }
        ],
    }

    with pytest.raises(SamiMatrixError, match="acronyme source"):
        validate_editorial_identity(matrix, versions)


def test_refuse_une_transformation_absente_du_contrat_editorial():
    matrix = deepcopy(load_sami_matrix())
    matrix["identite_editoriale"]["transformations_autorisees"].remove("P-18")

    with pytest.raises(SamiMatrixError, match="transformations éditoriales"):
        validate_sami_matrix(matrix)


def test_refuse_des_transformations_globales_qui_ne_sont_pas_une_liste():
    matrix = deepcopy(load_sami_matrix())
    controls = matrix["identite_editoriale"]["transformations_autorisees"]
    matrix["identite_editoriale"]["transformations_autorisees"] = {
        control: None for control in controls
    }

    with pytest.raises(SamiMatrixError, match="transformations_autorisees.*liste"):
        validate_sami_matrix(matrix)


def test_refuse_le_renommage_d_une_version_editoriale():
    matrix = deepcopy(load_sami_matrix())
    matrix["identite_editoriale"]["versions"]["inaccessible"] = "renomme.docx"

    with pytest.raises(SamiMatrixError, match="trois noms de fichiers"):
        validate_sami_matrix(matrix)
