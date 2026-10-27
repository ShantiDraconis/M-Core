"""Testes do companheiro numérico da rodada 34 (ZeroClasses/LagariasHadamard.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import lagarias_rec as lr  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return lr.main(os.path.join(d, "lagarias_rec.json"))


def test_serie_e_L():
    # `logDeriv_xi_eq`: ξ′/ξ = B + Σ (1/(s−ρ) + 1/ρ); `Lg_sob_RH`: L = Σ (σ−½)/|s−ρ|² > 0; `Lg_linha`: L(½) = 0
    out = _out()
    for p in out["pontos"].values():
        assert p["erro_serie"] < 1e-3 and p["erro_L"] < 1e-3
        assert p["L_direto"] > 0
    assert abs(out["L(1/2)"]) < 1e-8


def test_monotonia():
    # `rec_monotonia`: |ξ(σ + it)| estritamente crescente em ½ < σ ≤ 3
    out = _out()
    assert all(v["crescente"] for v in out["monotonia"].values())
