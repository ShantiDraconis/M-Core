"""Testes do companheiro numérico da rodada 77 (ZeroClasses/ExplicitaReal.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import explicita_real  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return explicita_real.main(os.path.join(d, "explicita_real.json"))


def test_abs_log():
    # `abs_log_ge_x`: |log(x/n)| ≥ d/(2x + 2)
    out = _out()
    assert all(r["min_log_vezes_constante"] >= 1 for r in out["abs_log"])


def test_formula_x_real():
    # `formula_explicita_T_x`: o erro de truncamento em T = 600 é menor que em T = 100 e fica abaixo de 0,25
    out = _out()
    for f in out["formula"]:
        e = [abs(r["erro"]) for r in f["erros"]]
        assert e[-1] < e[0] and e[-1] < 0.25
