"""Testes do companheiro numérico da rodada 67 (ZeroClasses/PsiLog2.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import psi_log2  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return psi_log2.main(os.path.join(d, "psi_log2.json"), N=10 ** 5)


def test_psi_e_pi():
    # `psi_RH_log2`, `pi_RH_log` (numérico): as razões ficam pequenas e caem por década
    out = _out()
    d = [r["max_psi_log2"] for r in out["decadas_psi"]]
    assert all(v < 0.05 for v in d) and all(a > b for a, b in zip(d, d[1:]))
    assert all(p["razao_log"] < 0.05 for p in out["pi_Li"])


def test_formula_explicita():
    # `bordo_explicita` em números: x − Σ_{γ ≤ 600} x^ρ/ρ − log 2π reproduz ψ(x) a menos de 1 em x = 100,5 e 1000,5
    e = _out()["formula_explicita"]
    assert abs(e[0]["dif"]) < 1 and abs(e[1]["dif"]) < 1
    assert all(abs(r["soma_zeros"]) <= r["cota_sqrt_soma"] for r in e)
