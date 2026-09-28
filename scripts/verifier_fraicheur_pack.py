"""Vérifie les ressources générées que ``make pack`` ne régénère pas.

Le pack reconstruit le deck, les PDF et les supports. Les documents Sami, la
grille XLSX et le deck WCAG sont produits par des commandes distinctes : ce
contrôle empêche de livrer une version plus ancienne que leurs sources.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class RessourceGeneree:
    """Contrat de fraîcheur d'une ressource produite hors de ``make pack``."""

    nom: str
    commande: str
    sources: tuple[str, ...]
    sorties: tuple[str, ...]


RESSOURCES_GENEREES = (
    RessourceGeneree(
        nom="documents Sami",
        commande="make sami",
        sources=("scripts/generate_exercice_sami.py",),
        sorties=(
            "_source/tp-doc-inaccessible.docx",
            "_source/tp-doc-aide-correction.docx",
            "_source/tp-doc-accessible.docx",
        ),
    ),
    RessourceGeneree(
        nom="grille d'audit XLSX",
        commande="make grille",
        sources=(
            "scripts/generate_grille_audit.py",
            "scripts/config.py",
            "config.yml",
        ),
        sorties=(
            "03-easy-checks/grille-audit-easy-checks.xlsx",
            "docs/assets/downloads/grille-audit-easy-checks.xlsx",
        ),
    ),
    RessourceGeneree(
        nom="deck WCAG condensé",
        commande="make wcag",
        sources=(
            "scripts/generate_wcag_langage_clair.py",
            "scripts/igpde_dsfr_components.py",
            "scripts/config.py",
            "config.yml",
            "_source/presentations-source/PPT-IGPDE-DSFR-base-intervenant.pptx",
        ),
        sorties=("wcag/WCAG en langage clair - condensé.pptx",),
    ),
)


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
            noms = ", ".join(str(chemin.relative_to(racine)) for chemin in manquantes)
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
                str(chemin.relative_to(racine)) for chemin in sorties_obsoletes
            )
            problemes.append(
                f"{ressource.nom} : plus ancien que {source_recente.relative_to(racine)} "
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
