"""Testes do companheiro numérico da rodada 75 (ZeroClasses/BDTaxa.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_taxa  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_taxa.main(os.path.join(d, "bd_taxa.json"))


def test_taxa():
    # `DNσ_taxa_RH`: a cota espectral cai como potência de N, com expoente local acima de 2(σ − ½) = 0,5
    out = _out()
    cotas = [c["cota"] for c in out["cotas"]]
    assert all(a > b for a, b in zip(cotas, cotas[1:]))
    assert min(out["expoentes_locais"]) > out["expoente_garantido_sob_RH"]


def test_cauda_pequena():
    # a cauda |τ| > 1000 é ordem de grandeza menor que a menor cota calculada
    out = _out()
    assert out["cauda_estimada"] < out["cotas"][-1]["cota"]
