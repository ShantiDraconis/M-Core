"""Testes do companheiro numérico da rodada 62 (ZeroClasses/Abscissa.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import abscissa  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return abscissa.main(os.path.join(d, "abscissa.json"))


def test_convergencia_a_direita():
    # `tendsto_mu`, `tendsto_cL` (numérico): em Re s = 0,75 o erro em N = 10⁶ é < 0,02; em 1,2 + 3i, < 10⁻⁴
    out = _out()
    for k in ("mu", "cL"):
        ult = {r["s"]: r["dif"] for r in out[k] if r["N"] == 10 ** 6}
        assert ult["(0.75+0j)"] < 0.02 and ult["(0.75+10j)"] < 0.02
        assert ult["(1.2+3j)"] < 1e-4


def test_oscilacao_a_esquerda():
    # em s = 0,4 < ½ o máximo das somas parciais de Σ μ(n)n^{−0,4} cresce (dado finito)
    out = _out()
    m = [r["max_abs"] for r in out["mu_0_4"]]
    assert all(a < b for a, b in zip(m, m[1:]))
