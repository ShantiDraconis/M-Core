"""Testes do companheiro numérico da rodada 85 (ZeroClasses/BDTaxaTeta.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_taxa_teta  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_taxa_teta.main(os.path.join(d, "bd_taxa_teta.json"))


def test_inf_recupera_teta():
    out = _out()
    for m in out["modelos"]:
        assert 0 < m["inf_grade"] - m["Teta"] <= out["passo"] + 1e-12


def test_perto_de_meio():
    for r in _out()["perto_de_meio"]:
        assert 0.5 < r["sigma"] < 0.5 + r["eps"] and r["piso_RH"] > 0
