"""Testes do companheiro numérico da rodada 70 (ZeroClasses/ExplicitaResiduos.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_residuos  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return explicita_residuos.main(os.path.join(d, "explicita_residuos.json"))


def test_constantes():
    # `logDeriv_zeta1_zero`: ζ₁′/ζ₁(0) = log 2π − 1; `deriv_trivial`: ζ′(−2k) = forma fechada ≠ 0
    out = _out()
    assert abs(out["logDeriv_zeta1_zero"] - out["log2pi_menos_1"]) < 1e-8
    for t in out["zeros_triviais"]:
        assert abs(t["dif_finita"] - t["forma_fechada"]) < 1e-6 * max(1.0, abs(t["forma_fechada"]))
        assert abs(t["forma_fechada"]) > 1e-3
    assert abs(out["cauda_trivial_K50"] - out["menos_meio_log"]) < 1e-12


def test_bordo_largo():
    # `bordo_largo`: (1/2πi)∮ x^s(−ζ′/ζ)/s = x − Σ x^ρ/ρ + Σ_{n<K} x^{−2(n+1)}/(2(n+1)) − log 2π
    out = _out()
    for r in out["retangulo_largo"]:
        assert abs(r["integral_re"] - r["residuos"]) < 1e-6
        assert abs(r["integral_im"]) < 1e-6
