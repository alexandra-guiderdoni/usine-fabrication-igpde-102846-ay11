"""Tests du contrôle de fraîcheur des ressources hors chaîne de pack."""

from __future__ import annotations

import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from verifier_fraicheur_pack import (  # noqa: E402
    RESSOURCES_GENEREES,
    RessourceGeneree,
    verifier_fraicheur,
)


RESSOURCE = RessourceGeneree(
    nom="ressource de test",
    commande="make test-ressource",
    sources=("sources/entree.txt",),
    sorties=("sorties/resultat.txt", "sorties/copie.txt"),
)


def _ecrire(racine: Path, chemin: str, contenu: str, horodatage: int) -> Path:
    cible = racine / chemin
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(contenu, encoding="utf-8")
    os.utime(cible, ns=(horodatage, horodatage))
    return cible


def test_signale_une_sortie_absente(tmp_path):
    _ecrire(tmp_path, "sources/entree.txt", "source", 1_000_000_000)
    _ecrire(tmp_path, "sorties/resultat.txt", "sortie", 2_000_000_000)

    problemes = verifier_fraicheur(tmp_path, (RESSOURCE,))

    assert problemes == [
        "ressource de test : fichier absent (sorties/copie.txt) ; lancer make test-ressource"
    ]


def test_signale_les_sorties_plus_anciennes_que_la_source(tmp_path):
    _ecrire(tmp_path, "sources/entree.txt", "source", 2_000_000_000)
    _ecrire(tmp_path, "sorties/resultat.txt", "sortie", 1_000_000_000)
    _ecrire(tmp_path, "sorties/copie.txt", "copie", 3_000_000_000)

    problemes = verifier_fraicheur(tmp_path, (RESSOURCE,))

    assert problemes == [
        "ressource de test : plus ancien que sources/entree.txt "
        "(sorties/resultat.txt) ; lancer make test-ressource"
    ]


def test_accepte_des_sorties_aussi_recentes_que_les_sources(tmp_path):
    _ecrire(tmp_path, "sources/entree.txt", "source", 1_000_000_000)
    _ecrire(tmp_path, "sorties/resultat.txt", "sortie", 1_000_000_000)
    _ecrire(tmp_path, "sorties/copie.txt", "copie", 2_000_000_000)

    assert verifier_fraicheur(tmp_path, (RESSOURCE,)) == []


def test_la_matrice_est_une_source_du_controle_de_fraicheur_sami():
    sami = next(
        resource for resource in RESSOURCES_GENEREES if resource.nom == "documents Sami"
    )

    assert "_source/exercice-sami-matrice.yml" in sami.sources
