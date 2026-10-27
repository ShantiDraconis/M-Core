"""Testes do companheiro numérico da rodada 87 (ZeroClasses/Unilateral.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import unilateral  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = unilateral.main(os.path.join(d, "unilateral.json"), n=2 * 10 ** 5)
    return _C["o"]


def test_integral_escada():
    # `integral_escada`: ∫_1^X x^{−3} M(⌊x⌋) dx → GA M(2)/2 = 3/π², cauda ≤ 1/X
    out = _out()
    assert out["erro_integral"] <= out["cota_cauda"]


def test_oscilacao_dos_dois_lados():
    # `mertens_omega_mais/menos`, `psi_omega_mais/menos`: os dois sinais aparecem na escala √N
    out = _out()
    assert out["M_max_sobre_raiz"]["valor"] > 0.3 and out["M_min_sobre_raiz"]["valor"] < -0.3
    assert out["psi_max_sobre_raiz"]["valor"] > 0.3 and out["psi_min_sobre_raiz"]["valor"] < -0.3
    assert out["trocas_sinal_M"] > 10 and out["trocas_sinal_psi"] > 10
