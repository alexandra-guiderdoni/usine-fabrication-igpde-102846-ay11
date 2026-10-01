"""Charge et valide la matrice pédagogique canonique de l'exercice Sami."""

from __future__ import annotations

from pathlib import Path
import re

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MATRIX_PATH = PROJECT_ROOT / "_source" / "exercice-sami-matrice.yml"
DEFAULT_COVERAGE_PATH = (
    PROJECT_ROOT / "_source" / "references" / "martine-sutra-couverture.md"
)

CONTROL_FIELDS = {
    "id",
    "niveau",
    "station",
    "intitule",
    "impact",
    "regle",
    "defaut",
    "action_attendue",
    "occurrences_attendues",
    "ancrage",
    "piste",
    "etat_corrige",
    "procedure_word",
    "procedure_writer",
    "preuve",
    "checklist",
    "guide",
    "slide",
    "note_formateur",
    "surfaces",
    "references_pedagogiques",
    "transformations_editoriales",
}
COMMON_REQUIRED_STRINGS = {
    "intitule",
    "impact",
    "regle",
    "etat_corrige",
    "checklist",
    "slide",
    "note_formateur",
}
PRACTICED_REQUIRED_STRINGS = {
    "station",
    "action_attendue",
    "procedure_word",
    "procedure_writer",
    "guide",
} | COMMON_REQUIRED_STRINGS
SIGNALLED_NULL_FIELDS = {
    "station",
    "defaut",
    "action_attendue",
    "ancrage",
    "piste",
    "procedure_word",
    "procedure_writer",
    "guide",
}
SIGNALLED_SURFACES = {
    "checklist_stagiaire",
    "checklist_formateur",
    "slides_checklist",
    "notes_formateur",
}
EXPECTED_CONTROL_IDS = (
    *(f"P-{index:02d}" for index in range(1, 21)),
    "C-01",
    "C-02",
    *(f"S-{index:02d}" for index in range(1, 6)),
)
EXPECTED_SEQUENCE_IDS = (
    "preambule",
    "station-1",
    "station-2",
    "station-3",
    "station-4",
    "station-5",
    "marge-remise",
)
EXPECTED_VERSION_FILENAMES = {
    "inaccessible": "tp-doc-inaccessible.docx",
    "avec_pistes": "tp-doc-aide-correction.docx",
    "corrigee": "tp-doc-accessible.docx",
}


class SamiMatrixError(ValueError):
    """Signale une matrice absente, illisible ou invalide."""


class _UniqueKeyLoader(yaml.SafeLoader):
    """Charge du YAML sûr en refusant les clés dupliquées."""


def _construct_unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            hash(key)
        except TypeError as error:
            raise yaml.constructor.ConstructorError(
                "construction d'un objet",
                node.start_mark,
                "clé YAML invalide : valeur non hachable",
                key_node.start_mark,
            ) from error
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "construction d'un objet",
                node.start_mark,
                f"clé YAML dupliquée : {key}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _expected_station(control_id: str) -> str | None:
    if control_id.startswith("S-"):
        return None
    if control_id.startswith("C-") or control_id in {"P-19", "P-20"}:
        return "station-5"
    number = int(control_id.removeprefix("P-"))
    if number <= 5:
        return "station-1"
    if number <= 11:
        return "station-2"
    if number <= 14:
        return "station-3"
    return "station-4"


def _validate_string_list(
    control_id: str, field: str, value: object, *, allow_empty: bool = False
) -> None:
    if (
        not isinstance(value, list)
        or (not allow_empty and not value)
        or any(type(item) is not str or not item for item in value)
        or len(value) != len(set(value))
    ):
        raise SamiMatrixError(
            f"{control_id} : {field} doit être une liste de chaînes uniques"
        )


def _validate_nonempty_string(control_id: str, field: str, value: object) -> None:
    if type(value) is not str or not value.strip():
        raise SamiMatrixError(f"{control_id} : {field} doit être une chaîne non vide")


def load_sami_matrix(path: Path = DEFAULT_MATRIX_PATH) -> dict:
    """Retourne la matrice YAML sous forme structurée."""
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise SamiMatrixError(f"Matrice illisible : {path}") from error
    try:
        matrix = yaml.load(source, Loader=_UniqueKeyLoader)
    except yaml.YAMLError as error:
        raise SamiMatrixError(f"YAML invalide : {path} : {error}") from error
    if not isinstance(matrix, dict):
        raise SamiMatrixError("La racine de la matrice doit être un objet")
    return validate_sami_matrix(matrix)


def load_coverage_codes(path: Path = DEFAULT_COVERAGE_PATH) -> frozenset[str]:
    """Retourne les codes pédagogiques définis par la référence locale."""
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise SamiMatrixError(f"Couverture illisible : {path}") from error
    codes = frozenset(re.findall(r"`(MS-\d{2})`", source))
    if not codes:
        raise SamiMatrixError(f"Aucun code pédagogique trouvé : {path}")
    return codes


def validate_sami_matrix(
    matrix: dict, coverage_path: Path = DEFAULT_COVERAGE_PATH
) -> dict:
    """Valide les invariants structurels de la matrice et la retourne."""
    if not isinstance(matrix, dict):
        raise SamiMatrixError("La racine de la matrice doit être un objet")
    if type(matrix.get("version")) is not int or matrix["version"] != 1:
        raise SamiMatrixError("La matrice doit déclarer la version 1")

    sequence = matrix.get("sequence")
    if not isinstance(sequence, list):
        raise SamiMatrixError("La séquence doit être une liste")
    try:
        sequence_ids = tuple(block["id"] for block in sequence)
    except (KeyError, TypeError) as error:
        raise SamiMatrixError(
            "Chaque bloc de la séquence doit avoir un identifiant"
        ) from error
    if sequence_ids != EXPECTED_SEQUENCE_IDS:
        raise SamiMatrixError("La séquence doit contenir les sept blocs canoniques")

    durations = []
    for block in sequence:
        _validate_nonempty_string(block["id"], "titre", block.get("titre"))
        try:
            duration = block["duree_minutes"]
        except (KeyError, TypeError) as error:
            raise SamiMatrixError(
                "Chaque bloc de la séquence doit définir une durée en minutes"
            ) from error
        if type(duration) is not int or duration <= 0:
            raise SamiMatrixError(
                "Chaque durée doit être un entier strictement positif"
            )
        durations.append(duration)

    total_minutes = sum(durations)

    if total_minutes != 90:
        raise SamiMatrixError("La séquence doit totaliser 90 minutes")

    controls = matrix.get("controles")
    if not isinstance(controls, list):
        raise SamiMatrixError("Les contrôles doivent être une liste")

    coverage_codes = load_coverage_codes(coverage_path)
    seen_ids: set[str] = set()
    for control in controls:
        control_id = control.get("id") if isinstance(control, dict) else None
        if not control_id:
            raise SamiMatrixError("Chaque contrôle doit posséder un identifiant")
        if control_id not in EXPECTED_CONTROL_IDS:
            raise SamiMatrixError(f"identifiant inconnu : {control_id}")
        if control_id in seen_ids:
            raise SamiMatrixError(f"Identifiant dupliqué : {control_id}")
        seen_ids.add(control_id)

        expected_station = _expected_station(control_id)
        if expected_station is not None and control.get("station") != expected_station:
            raise SamiMatrixError(
                f"{control_id} doit être rattaché à {expected_station}"
            )

        expected_level = control_id[0]
        if control.get("niveau") != expected_level:
            raise SamiMatrixError(
                f"{control_id} doit porter le niveau {expected_level}"
            )

        missing_fields = CONTROL_FIELDS - control.keys()
        if missing_fields:
            missing = ", ".join(sorted(missing_fields))
            raise SamiMatrixError(
                f"{control_id} : champ obligatoire absent : {missing}"
            )

        _validate_string_list(control_id, "surfaces", control["surfaces"])
        _validate_string_list(
            control_id,
            "references_pedagogiques",
            control["references_pedagogiques"],
            allow_empty=True,
        )
        _validate_string_list(
            control_id,
            "transformations_editoriales",
            control["transformations_editoriales"],
            allow_empty=True,
        )

        proof = control["preuve"]
        if not isinstance(proof, dict):
            raise SamiMatrixError(
                f"{control_id} : preuve doit définir un mode et un attendu"
            )
        for proof_field in ("mode", "attendu"):
            _validate_nonempty_string(
                control_id, f"preuve.{proof_field}", proof.get(proof_field)
            )

        if control["niveau"] in {"P", "C"}:
            for field in PRACTICED_REQUIRED_STRINGS:
                _validate_nonempty_string(control_id, field, control[field])
        elif control["niveau"] == "S":
            valid_surfaces = set(control["surfaces"]) == SIGNALLED_SURFACES
            if any(control[field] is not None for field in SIGNALLED_NULL_FIELDS):
                valid_surfaces = False
            if not valid_surfaces:
                raise SamiMatrixError(
                    f"{control_id} : surfaces réservées aux contrôles signalés"
                )
            for field in COMMON_REQUIRED_STRINGS:
                _validate_nonempty_string(control_id, field, control[field])
        else:
            raise SamiMatrixError(f"{control_id} : niveau inconnu")

        occurrences = control["occurrences_attendues"]
        if type(occurrences) is not int or occurrences < 0:
            raise SamiMatrixError(
                f"{control_id} : occurrences_attendues doit être un entier positif ou nul"
            )
        occurrence_fields = ("defaut", "ancrage", "piste")
        if occurrences == 0 and any(
            control[field] is not None for field in occurrence_fields
        ):
            raise SamiMatrixError(
                f"{control_id} : une occurrence à zéro interdit défaut, ancrage et piste"
            )
        if occurrences > 0:
            for field in occurrence_fields:
                _validate_nonempty_string(control_id, field, control[field])

        unknown_references = set(control["references_pedagogiques"]) - coverage_codes
        if unknown_references:
            unknown = ", ".join(sorted(unknown_references))
            raise SamiMatrixError(f"{unknown} : référence pédagogique inconnue")

    control_ids = tuple(control["id"] for control in controls)
    if control_ids != EXPECTED_CONTROL_IDS:
        raise SamiMatrixError(
            "Les contrôles sont absents, en trop ou hors ordre canonique"
        )

    identity = matrix.get("identite_editoriale")
    if not isinstance(identity, dict):
        raise SamiMatrixError("Le contrat d'identité éditoriale est obligatoire")
    if identity.get("versions") != EXPECTED_VERSION_FILENAMES:
        raise SamiMatrixError(
            "Le contrat doit préserver les trois noms de fichiers DOCX"
        )
    transformation_controls = {
        control["id"] for control in controls if control["transformations_editoriales"]
    }
    transformations = identity.get("transformations_autorisees")
    _validate_string_list(
        "identite_editoriale", "transformations_autorisees", transformations
    )
    if set(transformations) != transformation_controls:
        raise SamiMatrixError(
            "Les transformations éditoriales globales et locales divergent"
        )

    return matrix


def validate_occurrence_manifest(matrix: dict, manifest: dict[str, int]) -> None:
    """Vérifie que les défauts produits correspondent exactement à la matrice."""
    if not isinstance(manifest, dict):
        raise SamiMatrixError("Le manifeste des occurrences doit être un objet")

    expected = {
        control["id"]: control["occurrences_attendues"]
        for control in matrix["controles"]
    }
    unknown_ids = set(manifest) - set(expected)
    if unknown_ids:
        unknown = ", ".join(sorted(unknown_ids))
        raise SamiMatrixError(f"{unknown} : défaut déclaré hors matrice")

    for control_id, expected_count in expected.items():
        actual_count = manifest.get(control_id, 0)
        if type(actual_count) is not int or actual_count < 0:
            raise SamiMatrixError(
                f"{control_id} : le compte doit être un entier positif ou nul"
            )
        if actual_count != expected_count:
            raise SamiMatrixError(
                f"{control_id} : {actual_count} occurrence(s), "
                f"{expected_count} attendue(s)"
            )


def _validate_editorial_blocks(version_name: str, blocks: object) -> None:
    if not isinstance(blocks, list):
        raise SamiMatrixError(f"{version_name} : les blocs doivent être une liste")
    for index, block in enumerate(blocks, start=1):
        if not isinstance(block, dict):
            raise SamiMatrixError(
                f"{version_name} : le bloc {index} doit être un objet"
            )
        _validate_nonempty_string(version_name, f"bloc {index}.id", block.get("id"))
        _validate_nonempty_string(
            version_name, f"bloc {index}.texte", block.get("texte")
        )


def validate_editorial_identity(matrix: dict, versions: dict[str, list[dict]]) -> None:
    """Vérifie l'identité du corps et les transformations déclarées."""
    expected_versions = matrix["identite_editoriale"]["versions"]
    if not isinstance(versions, dict) or set(versions) != set(expected_versions):
        raise SamiMatrixError("Les trois versions éditoriales sont requises")

    for version_name, blocks in versions.items():
        _validate_editorial_blocks(version_name, blocks)

    inaccessible = versions["inaccessible"]
    with_hints = versions["avec_pistes"]
    corrected = versions["corrigee"]
    expected_order = [block["id"] for block in inaccessible]
    for version_name, blocks in versions.items():
        if [block["id"] for block in blocks] != expected_order:
            raise SamiMatrixError(
                f"{version_name} : ordre éditorial différent de l'inaccessible"
            )

    if [block["texte"] for block in with_hints] != [
        block["texte"] for block in inaccessible
    ]:
        raise SamiMatrixError("La version avec pistes modifie le corps éditorial")

    allowed_controls = set(matrix["identite_editoriale"]["transformations_autorisees"])
    controls = {control["id"]: control for control in matrix["controles"]}
    for source_block, corrected_block in zip(inaccessible, corrected, strict=True):
        if source_block["texte"] == corrected_block["texte"]:
            continue
        transformation = corrected_block.get("transformation", {})
        control_id = transformation.get("controle")
        transformation_type = transformation.get("type")
        declared_types = controls.get(control_id, {}).get(
            "transformations_editoriales", []
        )
        if (
            control_id not in allowed_controls
            or transformation_type not in declared_types
        ):
            raise SamiMatrixError(
                f"{corrected_block['id']} : différence éditoriale non déclarée"
            )
        if transformation_type == "developpement_acronyme_premiere_occurrence":
            source_acronyms = re.findall(r"\b[A-ZÀ-ÖØ-Þ]{2,}\b", source_block["texte"])
            corrected_text = corrected_block["texte"]
            if not source_acronyms or any(
                f"({acronym})" not in corrected_text for acronym in source_acronyms
            ):
                raise SamiMatrixError(
                    f"{corrected_block['id']} : l'acronyme source doit être conservé"
                )
