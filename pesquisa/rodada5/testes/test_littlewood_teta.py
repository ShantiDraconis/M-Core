"""Testes do companheiro numérico da rodada 93 (ZeroClasses/LittlewoodTeta.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import littlewood_teta  # noqa: E402

_C = {}


def _out():
    if "o" not in _C:
        with tempfile.TemporaryDirectory() as d:
            _C["o"] = littlewood_teta.main(os.path.join(d, "littlewood_teta.json"), n=200_000)
    return _C["o"]


def test_psi_menos_theta():
    # `Chebyshev.psi_sub_theta_le_mul_sqrt`: (ψ − θ)/√x fica bem abaixo de C = 3(log 4 + 4)
    o = _out()
    assert o["max_psi_menos_theta_sobre_raiz"] < 1.5 < o["C_mathlib"]


def test_trocas():
    # ψ(x) − x troca de sinal muitas vezes; θ(x) < x em todo o intervalo (a troca de θ está longe)
    o = _out()
    assert o["trocas_psi"] > 100
    assert o["theta_menor_que_x"]
    assert o["max_theta_sobre_raiz"] < 0
