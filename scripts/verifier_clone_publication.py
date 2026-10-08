"""Refuse une publication si le clone du site n'est pas prêt à recevoir la copie."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

DEPOT_ATTENDU = (
    "git@github.com:alexandra-guiderdoni/tp-fabrication-igpde-102846-ay11.git"
)


def git(dossier: Path, *arguments: str) -> str:
    resultat = subprocess.run(
        ["git", "-C", str(dossier), *arguments],
        capture_output=True,
        text=True,
        check=False,
    )
    if resultat.returncode:
        detail = resultat.stderr.strip() or resultat.stdout.strip()
        raise RuntimeError(f"git {' '.join(arguments)} : {detail}")
    return resultat.stdout.strip()


def verifier_clone(dossier: Path, depot_attendu: str = DEPOT_ATTENDU) -> list[str]:
    """Contrôle l'identité et l'état du clone avant toute copie destructive."""
    erreurs = []
    dossier = dossier.resolve()
    if not (dossier / ".git").exists():
        return [f"Clone du site absent : {dossier}"]

    try:
        racine = Path(git(dossier, "rev-parse", "--show-toplevel")).resolve()
        if racine != dossier:
            erreurs.append(f"Le dossier cible n'est pas la racine du clone : {racine}")
        branche = git(dossier, "branch", "--show-current")
        if branche != "main":
            erreurs.append(
                f"Branche du clone : {branche or 'détachée'} (main attendue)"
            )
        if git(dossier, "status", "--porcelain"):
            erreurs.append("L'arbre du clone contient des changements locaux")
        depot_lecture = git(dossier, "remote", "get-url", "origin")
        depot_ecriture = git(dossier, "remote", "get-url", "--push", "origin")
        if depot_lecture != depot_attendu or depot_ecriture != depot_attendu:
            erreurs.append(
                "Le dépôt distant origin (lecture ou écriture) diffère du dépôt SSH attendu"
            )
        if erreurs:
            return erreurs

        git(dossier, "fetch", "origin", "main")
        if git(dossier, "rev-parse", "HEAD") != git(
            dossier, "rev-parse", "refs/remotes/origin/main"
        ):
            erreurs.append("Le clone n'est pas aligné sur origin/main")
    except RuntimeError as erreur:
        erreurs.append(str(erreur))
    return erreurs


def main() -> int:
    analyseur = argparse.ArgumentParser(description=__doc__)
    analyseur.add_argument("clone", type=Path)
    analyseur.add_argument("--remote", default=DEPOT_ATTENDU)
    arguments = analyseur.parse_args()
    erreurs = verifier_clone(arguments.clone, arguments.remote)
    if erreurs:
        for erreur in erreurs:
            print(f"Publication refusée : {erreur}")
        return 1
    print(
        "Clone de publication vérifié : main propre, origine SSH et commit distant concordants."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
