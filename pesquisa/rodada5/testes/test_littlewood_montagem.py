"""Testes do companheiro numérico da rodada 92 (ZeroClasses/LittlewoodMontagem.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_montagem  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_montagem.main(os.path.join(d, "littlewood_montagem.json"))
    return _C["o"]


def test_gauss_e_crescimento():
    # `integral_abs_gauss` e `log_N_le` (com `log u ≤ T²`)
    o = _out()
    for r in o["integral_abs_gauss"]:
        assert abs(r["quad"] - r["inv"]) < 1e-6 * r["inv"]
    for r in o["crescimento"]:
        assert r["log_N"] <= r["cota"]
        assert r["log_N"] <= r["T2"]


def test_oscilacao():
    # `F` troca de sinal muitas vezes em `y ≤ 15` (ilustrativo; o teorema é assintótico)
    o = _out()["oscilacao"]
    assert o["F_max"] > 0 > o["F_min"]
    assert o["trocas_de_sinal"] >= 100
