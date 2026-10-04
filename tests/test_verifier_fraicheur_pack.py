"""Tests du contrôle de fraîcheur des ressources générées du pack."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from verifier_fraicheur_pack import (
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


def test_le_qr_code_est_une_source_du_deck_wcag():
    wcag = next(
        resource
        for resource in RESSOURCES_GENEREES
        if resource.nom == "deck WCAG condensé"
    )

    assert "_assets/qr-wcag-plain-english.png" in wcag.sources


def test_la_fraicheur_suit_le_fichier_de_configuration_alternatif(tmp_path):
    config_path = tmp_path / "session.yml"
    config_path.write_text(
        """formation:
  code: "999999"
  date: 9 octobre 2026
  footer: Formation alternative
  output: deck-alternatif.pptx
  livrables: pack-alternatif
  site_url: https://example.test/alternative/
""",
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["FORMATION_CONFIG"] = str(config_path)
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import verifier_fraicheur_pack as v; "
            "print(v.LIVRABLES); "
            "print(next(r for r in v.RESSOURCES_GENEREES "
            "if r.nom == 'checklists Sami').sources)",
        ],
        cwd=PROJECT_ROOT / "scripts",
        env=env,
        capture_output=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "pack-alternatif" in result.stdout
    assert str(config_path) in result.stdout


def test_signale_une_source_de_configuration_exterieure_sans_erreur(tmp_path):
    racine = tmp_path / "projet"
    source = _ecrire(tmp_path, "session.yml", "source", 3_000_000_000)
    _ecrire(racine, "sortie.txt", "sortie", 1_000_000_000)
    ressource = RessourceGeneree(
        nom="configuration extérieure",
        commande="make sortie",
        sources=(str(source),),
        sorties=("sortie.txt",),
    )

    problemes = verifier_fraicheur(racine, (ressource,))

    assert problemes == [
        f"configuration extérieure : plus ancien que {source} "
        "(sortie.txt) ; lancer make sortie"
    ]


def test_les_checklists_sont_soumises_au_controle_de_fraicheur():
    checklist = next(
        resource
        for resource in RESSOURCES_GENEREES
        if resource.nom == "checklists Sami"
    )

    assert checklist.commande == "make checklist"
    assert "_source/exercice-sami-matrice.yml" in checklist.sources
    assert checklist.sorties == (
        "_source/checklist-accessibilite-bureautique.md",
        "livrables-IGPDE-2026-102846/Livrables-Stagiaires/tp-word-igpde/"
        "checklist-accessibilite-bureautique.docx",
    )


def _ressource_pdf_checklist():
    return next(
        resource
        for resource in RESSOURCES_GENEREES
        if resource.nom == "checklist PDF Sami"
    )


def test_le_pdf_checklist_est_soumis_au_controle_de_fraicheur():
    checklist_pdf = _ressource_pdf_checklist()

    assert checklist_pdf.commande == "make pdf"
    assert "_source/checklist-accessibilite-bureautique.md" in checklist_pdf.sources
    assert checklist_pdf.sorties == (
        "livrables-IGPDE-2026-102846/Livrables-Stagiaires/tp-word-igpde/"
        "checklist-accessibilite-bureautique.pdf",
    )


def test_signale_un_pdf_checklist_absent(tmp_path):
    checklist_pdf = _ressource_pdf_checklist()
    for source in checklist_pdf.sources:
        _ecrire(tmp_path, source, "source", 1_000_000_000)

    problemes = verifier_fraicheur(tmp_path, (checklist_pdf,))

    assert problemes == [
        "checklist PDF Sami : fichier absent "
        "(livrables-IGPDE-2026-102846/Livrables-Stagiaires/tp-word-igpde/"
        "checklist-accessibilite-bureautique.pdf) ; lancer make pdf"
    ]


def test_signale_un_pdf_checklist_plus_ancien_que_le_markdown(tmp_path):
    checklist_pdf = _ressource_pdf_checklist()
    for source in checklist_pdf.sources:
        horodatage = (
            3_000_000_000
            if source == "_source/checklist-accessibilite-bureautique.md"
            else 1_000_000_000
        )
        _ecrire(tmp_path, source, "source", horodatage)
    _ecrire(
        tmp_path,
        checklist_pdf.sorties[0],
        "pdf",
        2_000_000_000,
    )

    problemes = verifier_fraicheur(tmp_path, (checklist_pdf,))

    assert problemes == [
        "checklist PDF Sami : plus ancien que "
        "_source/checklist-accessibilite-bureautique.md "
        "(livrables-IGPDE-2026-102846/Livrables-Stagiaires/tp-word-igpde/"
        "checklist-accessibilite-bureautique.pdf) ; lancer make pdf"
    ]
