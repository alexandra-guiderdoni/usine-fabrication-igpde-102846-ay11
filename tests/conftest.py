"""Fixtures partagees pour les tests igpde_dsfr_components."""

import sys
from pathlib import Path

import pytest

# Ajouter scripts/ au path pour permettre l'import direct
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import (  # noqa: E402
    create_presentation,
    new_slide,
)


@pytest.fixture(scope="session")
def deck():
    """Charge le PPTX final assemble depuis le disque (lecture seule)."""
    from pptx import Presentation as PrsLoad

    pptx_path = Path(__file__).parent.parent / "formation-102638-juin-2026.pptx"
    if not pptx_path.exists():
        pytest.skip(
            f"PPTX final non trouve : {pptx_path}. "
            "Lancer d'abord : python3 scripts/assemble.py"
        )
    return PrsLoad(str(pptx_path))


@pytest.fixture
def prs():
    """Presentation IGPDE chargee depuis le template reel."""
    prs, _layouts = create_presentation()
    return prs


@pytest.fixture
def layouts():
    """Dictionnaire des layouts disponibles."""
    _prs, layouts = create_presentation()
    return layouts


@pytest.fixture
def slide(prs, layouts):
    """Slide vide avec layout titre_contenu, prete pour les composants."""
    return new_slide(prs, layouts, layout_name="titre_contenu",
                     titre="Test", page_num=1)
