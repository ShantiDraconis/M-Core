"""Testes do companheiro numérico da rodada 66 (ZeroClasses/ExplicitaPecas.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_pecas  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return explicita_pecas.main(os.path.join(d, "explicita_pecas.json"))


def test_soma_e_alturas():
    # `soma_ordem_norm`: Σ 1/|ρ| ≤ (1 + log T)²/10; `separa`: a separação obtida é ≥ δ; `altura_boa`: razão < 1
    out = _out()
    assert all(r["razao"] < 0.1 for r in out["soma_ordem_norm"])
    for a in out["alturas"]:
        assert a["T0"] <= a["T"] <= a["T0"] + 1 and a["separacao"] >= a["delta"]
        assert all(v < 1 for v in a["razoes"].values())


def test_quarto():
    # `logDeriv_quarto_RH`: |ζ′/ζ(¼ + it)| ≤ C log(2 + |t|) com C pequeno em [0, 300]
    assert _out()["quarto_max"] < 5
