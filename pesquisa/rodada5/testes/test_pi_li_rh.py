"""Testes do companheiro numérico da rodada 65 (ZeroClasses/PiLiRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import pi_li_rh  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return pi_li_rh.main(os.path.join(d, "pi_li_rh.json"), N=10 ** 6)


def test_theta_e_pi():
    # `theta_RH`, `pi_RH` (numérico): as razões caem com x; para x ≥ 10⁴, dentro de Schoenfeld (válido em x ≥ 2657)
    out = _out()
    d = [r["max_theta_log3"] for r in out["decadas_theta"]]
    assert all(a > b for a, b in zip(d, d[1:]))
    assert all(p["razao_log2"] < 0.02 for p in out["pi_Li"])
    assert all(p["razao_schoenfeld"] < 1 for p in out["pi_Li"] if p["x"] >= 10 ** 4)


def test_formula_de_partes():
    # `pi_sub_Li`: π(10⁴) − Li(10⁴) = (θ − x)/log x + ∫ (θ(t) − t)/(t log² t) + 2/log 2
    p = _out()["partes_10^4"]
    assert abs(p["pi-Li"] - p["formula"]) < 1e-3
