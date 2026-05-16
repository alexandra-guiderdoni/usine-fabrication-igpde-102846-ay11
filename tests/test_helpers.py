"""Tests des fonctions pures et helpers (sans PPTX)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from igpde_dsfr_components import (
    _plain_text,
    _estimate_height,
    _safe_top,
    estimate_callout_height,
    estimate_highlight_height,
    estimate_quote_height,
    estimate_card_height,
    Stack,
    CONTENT_W,
    BOTTOM_CONTENT,
)


class TestPlainText:
    def test_string_simple(self):
        assert _plain_text("Bonjour") == "Bonjour"

    def test_list_de_strings(self):
        assert _plain_text(["Bon", "jour"]) == "Bonjour"

    def test_segments_riches(self):
        assert _plain_text([["gras", {}], "normal"]) == "grasnormal"

    def test_tuple(self):
        assert _plain_text(("A", "B")) == "AB"

    def test_none_retourne_string_none(self):
        # _plain_text passe par str() pour les scalaires non-list
        assert _plain_text(None) == "None"


class TestEstimateHeight:
    def test_string_courte(self):
        h = _estimate_height("Court", CONTENT_W)
        assert 0.1 < h < 0.5

    def test_liste_bullets(self):
        h = _estimate_height(["A", "B", "C"], CONTENT_W)
        assert h > _estimate_height("A", CONTENT_W)

    def test_none_retourne_zero(self):
        assert _estimate_height(None, CONTENT_W) == 0.0

    def test_taille_grande_augmente_hauteur(self):
        h_petit = _estimate_height("Texte assez long pour tester", CONTENT_W, size=11)
        h_grand = _estimate_height("Texte assez long pour tester", CONTENT_W, size=24)
        assert h_grand > h_petit

    def test_largeur_etroite_augmente_hauteur(self):
        texte = "Un texte suffisamment long pour etre coupe sur plusieurs lignes"
        h_large = _estimate_height(texte, 12.0)
        h_etroit = _estimate_height(texte, 3.0)
        assert h_etroit > h_large


class TestSafeTop:
    def test_pas_de_debordement(self):
        assert _safe_top(2.5, 2.0) == 2.5

    def test_debordement_remonte(self, capsys):
        result = _safe_top(6.0, 2.0)
        assert result < 6.0
        assert result + 2.0 <= BOTTOM_CONTENT
        captured = capsys.readouterr()
        assert "WARN footer" in captured.err

    def test_minimum_2_3(self, capsys):
        result = _safe_top(6.0, 10.0)
        assert result >= 2.3


class TestEstimators:
    def test_callout_minimum(self):
        h = estimate_callout_height("Titre", ["Un bullet"])
        assert h >= 0.90

    def test_callout_sans_titre(self):
        h = estimate_callout_height("", ["Un bullet"])
        assert h >= 0.90

    def test_highlight_minimum(self):
        h = estimate_highlight_height("Court")
        assert h >= 0.70

    def test_quote_avec_auteur(self):
        h_avec = estimate_quote_height("Citation", auteur="Auteur")
        h_sans = estimate_quote_height("Citation", auteur="")
        assert h_avec > h_sans

    def test_card_avec_numero(self):
        h_avec = estimate_card_height("Titre", ["Contenu"], 3.78, numero="01")
        h_sans = estimate_card_height("Titre", ["Contenu"], 3.78)
        assert h_avec > h_sans


class TestStack:
    def test_push_avance_curseur(self):
        s = Stack(top=2.30, gap=0.30)
        t1 = s.push(1.0)
        assert t1 == pytest.approx(2.30, abs=0.001)
        t2 = s.push(1.5)
        assert t2 == pytest.approx(3.60, abs=0.001)

    def test_gap_zero(self):
        s = Stack(top=1.0, gap=0.0)
        s.push(2.0)
        assert s.cursor == 3.0

    def test_cursor_property(self):
        s = Stack(top=0.0, gap=0.5)
        s.push(1.0)
        assert s.cursor == 1.5
