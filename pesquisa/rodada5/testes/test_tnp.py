"""Testes do companheiro numérico da rodada 54 (ZeroClasses/TNP.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import tnp  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return tnp.main(os.path.join(d, "tnp.json"))


def test_psi_theta_pi():
    # `psi_tnp`, `tendsto_theta_div`, `tendsto_primeCounting` (numérico): valores conhecidos e tendências
    out = _out()
    t = out["tabela"]
    assert [r["pi"] for r in t] == [168, 1229, 9592, 78498]
    assert all(r["erro_rel"] < 4e-3 for r in t)
    assert all(a["theta_x"] < b["theta_x"] for a, b in zip(t, t[1:]))
    assert all(a["pi_log_x"] > b["pi_log_x"] > 1 for a, b in zip(t, t[1:]))


def test_incremento():
    # `incremento`: h ψ(y) ≤ ψ₁(y + h) − ψ₁(y) ≤ h ψ(y + h)
    out = _out()
    for r in out["incremento"]:
        assert r["baixo"] <= r["meio"] <= r["alto"]
