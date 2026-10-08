"""Le garde de publication refuse les clones modifiés ou divergents."""

import subprocess

import pytest
from verifier_clone_publication import verifier_clone


def git(*arguments, dossier=None):
    return subprocess.run(
        ["git", *arguments],
        cwd=dossier,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


@pytest.fixture
def depot_site(tmp_path):
    distant = tmp_path / "site.git"
    clone = tmp_path / "site"
    git("init", "--bare", "-b", "main", str(distant))
    git("clone", str(distant), str(clone))
    git("config", "user.name", "Test IGPDE", dossier=clone)
    git("config", "user.email", "test@localhost", dossier=clone)
    (clone / "index.html").write_text("Site initial", encoding="utf-8")
    git("add", "index.html", dossier=clone)
    git("commit", "-m", "Site initial", dossier=clone)
    git("push", "-u", "origin", "main", dossier=clone)
    return distant, clone


def test_clone_propre_aligne_accepte(depot_site):
    distant, clone = depot_site
    assert verifier_clone(clone, str(distant)) == []


def test_branche_et_arbre_non_conformes_refuses(depot_site):
    distant, clone = depot_site
    git("switch", "-c", "autre", dossier=clone)
    (clone / "index.html").write_text("Changement local", encoding="utf-8")
    erreurs = verifier_clone(clone, str(distant))
    assert any("Branche" in erreur for erreur in erreurs)
    assert any("changements locaux" in erreur for erreur in erreurs)


def test_depot_distant_inattendu_refuse(depot_site):
    distant, clone = depot_site
    assert any(
        "dépôt distant" in erreur
        for erreur in verifier_clone(clone, str(distant) + "-autre")
    )


def test_clone_en_retard_refuse_apres_fetch(depot_site, tmp_path):
    distant, clone = depot_site
    second = tmp_path / "second"
    git("clone", str(distant), str(second))
    git("config", "user.name", "Test IGPDE", dossier=second)
    git("config", "user.email", "test@localhost", dossier=second)
    (second / "nouveau.html").write_text("Nouvelle page", encoding="utf-8")
    git("add", "nouveau.html", dossier=second)
    git("commit", "-m", "Nouvelle page", dossier=second)
    git("push", "origin", "main", dossier=second)
    assert any("aligné" in erreur for erreur in verifier_clone(clone, str(distant)))
