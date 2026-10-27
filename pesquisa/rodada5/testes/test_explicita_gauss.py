"""Testes do companheiro numérico da rodada 89 (ZeroClasses/ExplicitaGauss.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_gauss  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = explicita_gauss.main(os.path.join(d, "explicita_gauss.json"))
    return _C["o"]


def test_integral_linha():
    # `integral_linha`: ∫ exp((a + iy)Y + τ(a + iy)²) dy = 2π k_τ(Y)
    for r in _out()["linha"]:
        assert abs(r["quad"] - r["2pi_k"]) < 1e-8 * r["2pi_k"]


def test_formula_gauss():
    # `formula_gauss`: A_τ(u) = W(1) + W(−2)/2 − W(0) log 2π − Σ_ρ W(ρ)/ρ + (1/2π)∫ F_W(−5/2 + iy) dy
    for r in _out()["formula"]:
        assert r["erro"] < 1e-3
