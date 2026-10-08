"""Garde-fou PDF/UA-1 de make pdf : un PDF de repli ne remplace jamais un livrable.

Quand WeasyPrint refuse le mode PDF/UA-1, le générateur embarqué bascule sans
échouer sur un PDF sans structure d'accessibilité. Les PDF de test sont produits
par les deux mêmes appels WeasyPrint que ce générateur.
"""

import subprocess

import fabriquer_pack
import pack_supports
import pytest
import weasyprint

HTML = "<html lang='fr'><head><title>Essai</title></head><body><h1>Essai</h1><p>Texte.</p></body></html>"


@pytest.fixture
def pdfs(tmp_path):
    ua, repli = tmp_path / "ua.pdf", tmp_path / "repli.pdf"
    weasyprint.HTML(string=HTML).write_pdf(ua, pdf_variant="pdf/ua-1")
    weasyprint.HTML(string=HTML).write_pdf(repli)
    return ua, repli


@pytest.fixture
def usine(tmp_path, monkeypatch):
    livrable = tmp_path / "pack" / "fiche.pdf"
    livrable.parent.mkdir()
    livrable.write_bytes(b"livrable precedent")
    monkeypatch.setattr(fabriquer_pack, "RACINE", tmp_path)
    monkeypatch.setattr(
        fabriquer_pack, "PDFS", [("fiche.md", "pack/fiche.pdf", None, [], None)]
    )
    return livrable


def _generateur(produit):
    # Le message annonce toujours PDF/UA-1 : le contrôle doit porter sur le fichier.
    def generer(md2pdf, source, sortie, bandeau, alt, options):
        sortie.write_bytes(produit.read_bytes())
        return subprocess.CompletedProcess(
            [], 0, stdout="  Standard : PDF/UA-1\n", stderr=""
        )

    return generer


def test_pdf_ua_reconnu(pdfs):
    ua, _ = pdfs
    assert fabriquer_pack.est_pdf_ua(ua) is True


def test_pdf_de_repli_refuse(pdfs):
    _, repli = pdfs
    assert fabriquer_pack.est_pdf_ua(repli) is False


def test_make_pdf_ne_regenere_pas_la_fiche_formateur():
    assert all(
        "fiche-formateur-principes-wcag" not in str(source)
        and "fiche-formateur-principes-wcag" not in str(sortie)
        for source, sortie, _, _, _ in fabriquer_pack.PDFS
    )


def test_les_memos_affichent_la_page_et_le_total_des_la_couverture():
    memos = [
        options
        for source, _, _, options, _ in fabriquer_pack.PDFS
        if source.startswith("fiche-pratique/memo-")
    ]
    assert len(memos) == 2
    assert all("--page-total-footer" in options for options in memos)


def test_les_memos_structurent_les_cinq_etapes_en_liste():
    memos = [
        options
        for source, _, _, options, _ in fabriquer_pack.PDFS
        if source.startswith("fiche-pratique/memo-")
    ]
    assert len(memos) == 2
    assert all(options.count("--subtitle-list-item") == 5 for options in memos)


def test_make_pdf_refuse_un_repli_et_garde_le_livrable(pdfs, usine, monkeypatch):
    _, repli = pdfs
    monkeypatch.setattr(pack_supports, "generer_pdf", _generateur(repli))

    with pytest.raises(SystemExit):
        fabriquer_pack.pdf()

    assert usine.read_bytes() == b"livrable precedent"
    assert [p.name for p in usine.parent.iterdir()] == ["fiche.pdf"]


def test_make_pdf_remplace_le_livrable_par_un_pdf_ua(pdfs, usine, monkeypatch):
    ua, _ = pdfs
    monkeypatch.setattr(pack_supports, "generer_pdf", _generateur(ua))

    fabriquer_pack.pdf()

    assert usine.read_bytes() == ua.read_bytes()
    assert [p.name for p in usine.parent.iterdir()] == ["fiche.pdf"]


LIVRES = [
    fabriquer_pack.RACINE / sortie for _, sortie, _, _, _ in fabriquer_pack.PDFS
] + [
    copie / sortie.split("/")[-1]
    for _, sortie, _, _, copie in fabriquer_pack.PDFS
    if copie is not None
]


@pytest.mark.parametrize("chemin", LIVRES, ids=lambda c: c.name)
def test_pdf_livres_en_pdf_ua(chemin):
    assert fabriquer_pack.est_pdf_ua(chemin) is True
