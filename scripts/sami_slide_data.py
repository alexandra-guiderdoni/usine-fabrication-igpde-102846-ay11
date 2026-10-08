"""Expose aux slides les données canoniques du TP Sami."""

from __future__ import annotations

from functools import lru_cache

from exercice_sami_matrice import load_sami_matrix


@lru_cache(maxsize=1)
def sami_matrix() -> dict:
    """Charge une fois la matrice validée pendant une génération."""
    return load_sami_matrix()


def sequence_block(block_id: str) -> dict:
    """Retourne un bloc de séquence par son identifiant stable."""
    return next(block for block in sami_matrix()["sequence"] if block["id"] == block_id)


def station_blocks() -> tuple[dict, ...]:
    """Retourne les cinq étapes dans l'ordre canonique."""
    return tuple(
        block
        for block in sami_matrix()["sequence"]
        if block["id"].startswith("station-")
    )


def tp_duration() -> int:
    """Retourne la durée totale du TP, marge et remise comprises."""
    return sum(block["duree_minutes"] for block in sami_matrix()["sequence"])


def version_filename(version_name: str) -> str:
    """Retourne le nom canonique d'une version du document Sami."""
    return sami_matrix()["identite_editoriale"]["versions"][version_name]


def station_controls(station_id: str) -> tuple[dict, ...]:
    """Retourne les contrôles d'une étape dans l'ordre canonique."""
    return tuple(
        control
        for control in sami_matrix()["controles"]
        if control["station"] == station_id
    )


def signalled_controls() -> tuple[dict, ...]:
    """Retourne les contrôles signalés, sans manipulation obligatoire."""
    return tuple(
        control for control in sami_matrix()["controles"] if control["niveau"] == "S"
    )


def control_heading(control: dict) -> str:
    """Formate l'identifiant, le niveau et le libellé canonique."""
    return f"{control['id']} [{control['niveau']}] - {control['intitule']}"


def checklist_item(control: dict) -> str:
    """Formate une ligne de checklist directement depuis la matrice."""
    return f"{control['id']} [{control['niveau']}] - {control['checklist']}"


def station_notes(
    station_id: str,
    *,
    controls: tuple[dict, ...] | None = None,
    question: str,
    help_text: str,
) -> str:
    """Construit les notes formateur communes à une slide d'étape."""
    block = sequence_block(station_id)
    selected = controls or station_controls(station_id)
    proofs = " ; ".join(
        f"{control['id']} : {control['preuve']['attendu']}" for control in selected
    )
    ids = ", ".join(control["id"] for control in selected)
    return (
        f"Minutage de l'étape : {block['duree_minutes']} minutes, synthèse comprise. "
        f"Contrôles travaillés sur cette slide : {ids}.\n\n"
        "Parcours guidé : partir du DOCX avec pistes, reformuler le problème et "
        "laisser le binôme réaliser la correction. Variante autonome : partir du "
        "DOCX inaccessible et n'ouvrir les pistes qu'en cas de blocage.\n\n"
        f"Points d'aide possibles : {help_text}\n\n"
        f"Question de synthèse : {question}\n\n"
        f"Preuves attendues : {proofs}"
    )


def preamble_notes() -> str:
    """Construit les notes du préambule depuis son minutage canonique."""
    block = sequence_block("preambule")
    return (
        f"Préambule limité à {block['duree_minutes']} minutes, quiz compris. "
        "Distribuer la checklist et les cartes WCAG, puis proposer le DOCX avec "
        "pistes comme point de départ conseillé. Le DOCX inaccessible constitue "
        "la variante autonome. Ne pas révéler le corrigé avant la remise finale."
    )
