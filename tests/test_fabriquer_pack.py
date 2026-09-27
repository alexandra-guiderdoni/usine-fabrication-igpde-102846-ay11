"""Copie du deck dans le pack : seul un deck complet peut remplacer le livrable."""

import zipfile

import fabriquer_pack
import pytest


def _faux_deck(chemin, nombre_slides, contenu="<p:sld/>", date=(2026, 9, 27, 12, 0, 0)):
    parties = {"[Content_Types].xml": "<Types/>"}
    for i in range(1, nombre_slides + 1):
        parties[f"ppt/slides/slide{i}.xml"] = contenu
        parties[f"ppt/slides/_rels/slide{i}.xml.rels"] = "<Relationships/>"
    with zipfile.ZipFile(chemin, "w") as archive:
        for nom, texte in parties.items():
            archive.writestr(zipfile.ZipInfo(nom, date_time=date), texte)


@pytest.fixture
def usine(tmp_path, monkeypatch):
    formateur = tmp_path / "pack" / "Formateur"
    formateur.mkdir(parents=True)
    monkeypatch.setattr(fabriquer_pack, "RACINE", tmp_path)
    monkeypatch.setattr(fabriquer_pack, "FORMATEUR", formateur)
    monkeypatch.setattr(fabriquer_pack, "CONFIG", {"output": "deck.pptx"})
    monkeypatch.setattr(fabriquer_pack, "nombre_modules", lambda: 3, raising=False)
    return tmp_path, formateur


def test_deck_partiel_refuse_et_livrable_intact(usine):
    racine, formateur = usine
    _faux_deck(racine / "deck.pptx", 1)
    (formateur / "deck.pptx").write_bytes(b"livrable precedent")

    with pytest.raises(SystemExit):
        fabriquer_pack.deck()

    assert (formateur / "deck.pptx").read_bytes() == b"livrable precedent"


def test_deck_complet_copie_dans_le_pack(usine):
    racine, formateur = usine
    _faux_deck(racine / "deck.pptx", 3)

    fabriquer_pack.deck()

    assert (formateur / "deck.pptx").read_bytes() == (racine / "deck.pptx").read_bytes()


def test_deck_regenere_a_l_identique_non_recopie(usine):
    racine, formateur = usine
    _faux_deck(racine / "deck.pptx", 3, date=(2026, 9, 27, 15, 0, 0))
    _faux_deck(formateur / "deck.pptx", 3, date=(2026, 9, 27, 14, 0, 0))
    avant = (formateur / "deck.pptx").read_bytes()
    assert avant != (racine / "deck.pptx").read_bytes()

    fabriquer_pack.deck()

    assert (formateur / "deck.pptx").read_bytes() == avant


def test_deck_au_contenu_modifie_recopie(usine):
    racine, formateur = usine
    _faux_deck(racine / "deck.pptx", 3, contenu="<p:sld>nouveau</p:sld>")
    _faux_deck(formateur / "deck.pptx", 3, contenu="<p:sld>ancien</p:sld>")

    fabriquer_pack.deck()

    assert (formateur / "deck.pptx").read_bytes() == (racine / "deck.pptx").read_bytes()


def test_deck_absent_refuse(usine):
    with pytest.raises(SystemExit):
        fabriquer_pack.deck()
