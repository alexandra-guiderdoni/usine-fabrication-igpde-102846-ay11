"""Copie des documents Word de l'exercice dans le pack : trois noms attendus, aucun manquant."""

import pack_supports
import pytest

NOMS = [
    "tp-doc-accessible.docx",
    "tp-doc-aide-correction.docx",
    "tp-doc-inaccessible.docx",
]


@pytest.fixture
def usine(tmp_path):
    (tmp_path / "_source").mkdir()
    stagiaires = tmp_path / "Livrables-Stagiaires"
    (stagiaires / "tp-word-igpde").mkdir(parents=True)
    return tmp_path, stagiaires


def test_trois_documents_copies_sous_leur_nom(usine):
    racine, stagiaires = usine
    for nom in NOMS:
        (racine / "_source" / nom).write_bytes(nom.encode())

    pack_supports.docx_sami(racine, stagiaires)

    cible = stagiaires / "tp-word-igpde"
    assert sorted(p.name for p in cible.iterdir()) == NOMS
    for nom in NOMS:
        assert (cible / nom).read_bytes() == nom.encode()


def test_document_manquant_signale(usine):
    racine, stagiaires = usine
    for nom in NOMS[1:]:
        (racine / "_source" / nom).write_bytes(b"docx")

    with pytest.raises(FileNotFoundError):
        pack_supports.docx_sami(racine, stagiaires)
