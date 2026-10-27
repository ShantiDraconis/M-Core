"""Testes do companheiro numérico da rodada 55 (ZeroClasses/VonKoch.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import von_koch  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return von_koch.main(os.path.join(d, "von_koch.json"))


def test_serie_e_identidade():
    # `GA_eq_LSeries`, `LSeries_cL`: G(s) = −ζ′/ζ(s) − ζ(s) em s > 1; a identidade de `zeroFree_of_psi`
    out = _out()
    for r in out["serie"]:
        assert r["dif"] < 1e-6
        assert r["residuo_identidade"] < 1e-6
    assert abs(out["serie"][1]["menos_logderiv_menos_zeta"] - (0.5699609930944 - 1.6449340668482)) < 1e-8


def test_von_koch_nos_dados():
    # o lado de RH (dado finito): |ψ(N) − N| ≤ √N log²N/(8π) até 10⁶ (Schoenfeld, sob RH, x ≥ 73,2)
    out = _out()
    assert all(r["max_E_sqrt_log2"] < 1 / (8 * 3.141592653589793) for r in out["faixas"])
    assert all(r["max_E_sqrt"] < 1 for r in out["faixas"])
