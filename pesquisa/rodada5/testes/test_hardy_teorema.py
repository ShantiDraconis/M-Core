"""Testes do companheiro numérico da rodada 50 (ZeroClasses/HardyTeorema.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import hardy_teorema as ht  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return ht.main(os.path.join(d, "hardy_teorema.json"))


def test_trocas_de_sinal():
    # `trocasInfinitas` (numérico): Ξ troca de sinal 10 vezes em (0, 50] e 29 em (0, 100]
    out = _out()
    assert out["contagem"] == {"50": 10, "100": 29}
    assert all(d < 0.01 for d in out["dif_gammas"])


def test_rvm():
    # a contagem em T = 100 bate com o termo principal de Riemann–von Mangoldt
    out = _out()
    assert abs(out["contagem"]["100"] - out["rvm_principal"]["100"]) < 1
