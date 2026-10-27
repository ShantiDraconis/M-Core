"""Testes do companheiro numérico da rodada 83 (ZeroClasses/BDTaxaPiso.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_taxa_piso  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_taxa_piso.main(os.path.join(d, "bd_taxa_piso.json"))


def test_wsigma_zero():
    for r in _out()["Wsigma_zero"]:
        assert abs(r["quad"] - r["formula"]) < 1e-4


def test_faixa_r75():
    # as inclinações locais da rodada 75 (σ = 0,75) caem na faixa [2σ − 1, (2σ + 3)(2σ − 1)] sob RH
    out = _out()
    f = {r["sigma"]: r for r in out["faixa_RH"]}[out["sigma_r75"]]
    assert all(f["piso_RH"] <= x <= f["teto_RH"] for x in out["inclinacoes_r75"])
    assert all(2 < r["fator"] < 5 for r in out["faixa_RH"])
