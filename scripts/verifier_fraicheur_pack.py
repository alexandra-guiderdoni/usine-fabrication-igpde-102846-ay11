"""Vérifie la fraîcheur des ressources générées du pack.

Certaines ressources sont reconstruites par ``make pack`` avant ce contrôle,
d'autres par des commandes distinctes. Ce contrôle empêche de livrer une
version plus ancienne que ses sources, quelle que soit sa chaîne de génération.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

from config import DEFAULT_CONFIG_PATH, load_formation_config

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LIVRABLES = load_formation_config()["livrables"]
try:
    CONFIG_SOURCE = str(DEFAULT_CONFIG_PATH.resolve().relative_to(PROJECT_ROOT))
except ValueError:
    CONFIG_SOURCE = str(DEFAULT_CONFIG_PATH.resolve())


@dataclass(frozen=True)
class RessourceGeneree:
    """Contrat de fraîcheur d'une ressource générée du pack."""

    nom: str
    commande: str
    sources: tuple[str, ...]
    sorties: tuple[str, ...]


RESSOURCES_GENEREES = (
    RessourceGeneree(
        nom="documents Sami",
        commande="make sami",
        sources=(
            "scripts/generate_exercice_sami.py",
            "scripts/exercice_sami_matrice.py",
            "_source/exercice-sami-matrice.yml",
        ),
        sorties=(
            "_source/tp-doc-inaccessible.docx",
            "_source/tp-doc-aide-correction.docx",
            "_source/tp-doc-accessible.docx",
        ),
    ),
    RessourceGeneree(
        nom="checklists Sami",
        commande="make checklist",
        sources=(
            "scripts/generate_exercice_sami.py",
            "scripts/exercice_sami_matrice.py",
            "scripts/config.py",
            CONFIG_SOURCE,
            "_source/exercice-sami-matrice.yml",
        ),
        sorties=(
            "_source/checklist-accessibilite-bureautique.md",
            f"{LIVRABLES}/Livrables-Stagiaires/tp-word-igpde/"
            "checklist-accessibilite-bureautique.docx",
        ),
    ),
    RessourceGeneree(
        nom="checklist PDF Sami",
        commande="make pdf",
        sources=(
            "_source/checklist-accessibilite-bureautique.md",
            "scripts/fabriquer_pack.py",
            "scripts/pack_supports.py",
            "scripts/config.py",
            CONFIG_SOURCE,
            "vendor/accessible-pdf/scripts/md2pdf.py",
            "vendor/accessible-pdf/templates/formation.css",
            "fiche-pratique/bandeau-igpde-logos.jpg",
        ),
        sorties=(
            f"{LIVRABLES}/Livrables-Stagiaires/tp-word-igpde/"
            "checklist-accessibilite-bureautique.pdf",
        ),
    ),
    RessourceGeneree(
        nom="grille d'audit XLSX",
        commande="make grille",
        sources=(
            "scripts/generate_grille_audit.py",
            "scripts/config.py",
            CONFIG_SOURCE,
        ),
        sorties=(
            "03-easy-checks/grille-audit-easy-checks.xlsx",
            "docs/assets/downloads/grille-audit-easy-checks.xlsx",
            "docs/grille-audit-easy-checks.xlsx",
        ),
    ),
    RessourceGeneree(
        nom="deck WCAG condensé",
        commande="make wcag",
        sources=(
            "scripts/generate_wcag_langage_clair.py",
            "scripts/igpde_dsfr_components.py",
            "scripts/config.py",
            CONFIG_SOURCE,
            "_assets/qr-wcag-plain-english.png",
            "_source/presentations-source/PPT-IGPDE-DSFR-base-intervenant.pptx",
        ),
        sorties=("wcag/WCAG en langage clair - condensé.pptx",),
    ),
)


def _chemin_affichable(racine: Path, chemin: Path) -> str:
    """Affiche un chemin relatif à l'usine, ou absolu s'il est extérieur."""
    try:
        return str(chemin.relative_to(racine))
    except ValueError:
        return str(chemin)


def verifier_fraicheur(
    racine: Path,
    ressources: Iterable[RessourceGeneree] = RESSOURCES_GENEREES,
) -> list[str]:
    """Retourne les ressources absentes ou plus anciennes que leurs sources."""
    problemes = []
    for ressource in ressources:
        sources = [racine / chemin for chemin in ressource.sources]
        sorties = [racine / chemin for chemin in ressource.sorties]
        manquantes = [chemin for chemin in sources + sorties if not chemin.is_file()]
        if manquantes:
            noms = ", ".join(
                _chemin_affichable(racine, chemin) for chemin in manquantes
            )
            problemes.append(
                f"{ressource.nom} : fichier absent ({noms}) ; lancer {ressource.commande}"
            )
            continue

        source_recente = max(sources, key=lambda chemin: chemin.stat().st_mtime_ns)
        sorties_obsoletes = [
            sortie
            for sortie in sorties
            if sortie.stat().st_mtime_ns < source_recente.stat().st_mtime_ns
        ]
        if sorties_obsoletes:
            noms = ", ".join(
                _chemin_affichable(racine, chemin) for chemin in sorties_obsoletes
            )
            problemes.append(
                f"{ressource.nom} : plus ancien que "
                f"{_chemin_affichable(racine, source_recente)} "
                f"({noms}) ; lancer {ressource.commande}"
            )
    return problemes


def main() -> int:
    problemes = verifier_fraicheur(PROJECT_ROOT)
    if problemes:
        print("Ressources générées à régénérer avant make pack :")
        for probleme in problemes:
            print(f"- {probleme}")
        return 1
    print("Fraîcheur du pack : ressources générées à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
