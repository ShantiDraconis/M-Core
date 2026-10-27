"""Testes do companheiro numérico da rodada 37 (ZeroClasses/RegiaoLivre.lean)."""
import math
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import regiao_livre as rl  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return rl.main(os.path.join(d, "regiao_livre.json"))


def test_cotas():
    # `cota_zeta_faixa`, `cota_zeta_real`, `prod341`, `re_logDeriv_local`
    out = _out()
    assert out["faixa_pior_razao"] <= 1
    assert all(v <= 8 for v in out["real_(s-1)zeta"].values())
    assert out["prod341_min"] >= 1
    assert out["local_pior_razao"] <= 1


def test_341_e_polo():
    # `tres_quatro_um` na grade; `polo`: −ζ′/ζ(σ) − 1/(σ − 1) → −γ_E
    out = _out()
    assert out["comb341_min"] >= 0
    assert abs(out["polo"]["1.001"] + 0.5772156649) < 1e-2
    assert max(abs(v) for v in out["polo"].values()) < 1


def test_montagem():
    # a aritmética de `regiao_livre_grande`: 2886 + 481 = 3367, c = δ/7 = 1/6734
    out = _out()
    a = out["aritmetica"]
    assert a["soma"] == 3367 and abs(a["c"] - a["1/6734"]) < 1e-15
    assert all(0.5 < v < 1 for v in out["fronteira"].values())
    assert math.isclose(out["fronteira"]["2"], 1 - 1 / (6734 * math.log(2)))
