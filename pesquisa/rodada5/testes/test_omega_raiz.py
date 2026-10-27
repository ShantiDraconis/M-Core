"""Testes do companheiro numérico da rodada 88 (ZeroClasses/OmegaRaiz.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import omega_raiz  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = omega_raiz.main(os.path.join(d, "omega_raiz.json"), n=2 * 10 ** 5)
    return _C["o"]


def test_omega_raiz_dos_dois_lados():
    # `psi_omega_mais_raiz`/`_menos_raiz` com c = 1/(8|ρ₀|); `mertens_omega_*_raiz` com 0,1
    out = _out()
    assert 0.008 < out["c_psi"] < 0.009
    assert out["psi_acima"] > 100 and out["psi_abaixo"] > 100
    assert out["M_acima_0_1"] > 100 and out["M_abaixo_0_1"] > 100


def test_zeros_simples():
    # sanidade de `simples_of_mertens_le`: ζ(ρ) ≈ 0 e ζ′(ρ) ≠ 0 nos 3 primeiros zeros
    for z in _out()["zeros"]:
        assert z["abs_zeta"] < 1e-6
        assert z["abs_deriv"] > 0.5
