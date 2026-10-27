"""Testes do companheiro numérico da rodada 90 (ZeroClasses/LittlewoodBase.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_base  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_base.main(os.path.join(d, "littlewood_base.json"))
    return _C["o"]


def test_mgf_e_lado_psi():
    # `integral_kg_exp` e `A_sub_eq`: A_τ(u) − e^{u/2+τ/4} = ∫ k_τ(v) F(u − v) dv
    out = _out()
    for r in out["mgf"]:
        assert abs(r["quad"] - r["exp"]) < 1e-9
    for r in out["lado_psi"]:
        assert abs(r["A_menos_W1"] - r["integral"]) < 1e-4


def test_re_pw_RH():
    # `re_pw_RH`: Re(W(ρ)/ρ) = e^{−τγ²}(cos(γu)/2 + γ sen(γu))/|ρ|² em Re ρ = ½
    for r in _out()["re_pw_RH"]:
        assert abs(r["re"] - r["formula"]) <= 1e-12 * max(1.0, abs(r["formula"]))
    assert _out()["max_F_sobre_1_y2"] < 2
