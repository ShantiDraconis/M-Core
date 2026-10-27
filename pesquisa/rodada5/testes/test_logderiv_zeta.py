"""Testes do companheiro numérico da rodada 52 (ZeroClasses/LogDerivZeta.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import logderiv_zeta as lz  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return lz.main(os.path.join(d, "logderiv_zeta.json"))


def test_regiao():
    # `logDeriv_zeta_le` (numérico): |ζ′/ζ| ≤ 0,05 log²t na faixa testada
    out = _out()
    assert all(r["razao_log2"] < 0.05 for r in out["regiao"])


def test_serie():
    # `norm_logDeriv_le`: |ζ′/ζ(σ + it)| ≤ −ζ′/ζ(σ); −ζ′/ζ(2) = 0,5699609…
    out = _out()
    for r in out["serie"]:
        assert r["abs"] <= r["menos_logderiv_real"]
    assert abs(out["serie"][-1]["menos_logderiv_real"] - 0.5699609931) < 1e-6
