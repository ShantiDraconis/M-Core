"""Testes do companheiro numérico da rodada 48 (ZeroClasses/HardyFourier.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import hardy_fourier as hf  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return hf.main(os.path.join(d, "hardy_fourier.json"))


def test_Hr_par_e_cota():
    # `Hr_neg` e `abs_Hr_le`: Hr(−u) = Hr(u) e |Hr(u)| ≤ 5e^{−|u|/2}
    out = _out()
    for p in out["Hr_par"]:
        assert abs(p["Hr"] - p["Hr_neg"]) < 1e-12
    for c in out["Hr_cota"]:
        assert c["abs_Hr"] <= c["cota"]
    for e in out["exp_cos"]:
        assert abs(e["simpson"] - e["exato"]) < 1e-9


def test_Fx_eq_e_decaimento():
    # `Fx_eq`: (1/4)∫₀^∞ Hr = ξ(1/2); troca de sinal em t₁; `abs_Xi_le`
    out = _out()
    assert abs(out["Xi_meio"]["integral"] - out["Xi_meio"]["conhecido"]) < 1e-10
    a, b = out["troca_t1"]
    assert a["Xi"] > 0 > b["Xi"]
    for d in out["decaimento"]:
        assert abs(d["Xi"]) <= d["cota"]
