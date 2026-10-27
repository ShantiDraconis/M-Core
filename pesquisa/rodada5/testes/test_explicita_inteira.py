"""Testes do companheiro numérico da rodada 78 (ZeroClasses/ExplicitaInteira.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_inteira  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return explicita_inteira.main(os.path.join(d, "explicita_inteira.json"))


def test_integral_e_perron_zero():
    # `integral_um_div` e `perron_zero`
    for r in _out()["integrais"]:
        assert abs(r["quadratura"] - r["formula"]) < 1e-6
        assert r["perron_zero"] <= r["cota"]


def test_psi0_no_primo():
    # `formula_explicita_T_N`: em N = 11 (primo) o valor certo é ψ₀(N), não ψ(N)
    f = {r["N"]: r for r in _out()["formula"]}
    assert abs(f[11]["erro_psi0"]) < 0.3 < abs(f[11]["erro_psi"])
