"""Testes do companheiro numérico da rodada 57 (ZeroClasses/QuasiRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import quasi_rh  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return quasi_rh.main(os.path.join(d, "quasi_rh.json"))


def test_cotas_psi_e_M():
    # `psi_of_semZeros`, `mertens_of_semZeros` (lado "cota", dado finito): razões limitadas e decrescentes em θ
    out = _out()
    assert out["M_1e6"] == 212
    c = out["cotas"]
    assert all(r["max_psi"] < 1 and r["max_M"] < 1 for r in c)
    assert all(a["max_psi"] >= b["max_psi"] and a["max_M"] >= b["max_M"] for a, b in zip(c, c[1:]))


def test_deslocamento_mu():
    # `somas_limitadas_gen` com a = μ: Σ μ(n) n^{−0,8} → 1/ζ(0,8); `norm_F_le`: |1/ζ| moderado em σ ≥ 0,6
    out = _out()
    p = out["parciais_mu"]
    assert p[-1]["dif"] < 0.01 < p[0]["dif"]
    assert all(r["abs_inv_zeta"] < 2 for r in out["inv_zeta"])
