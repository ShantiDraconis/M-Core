"""Testes do companheiro numérico da rodada 56 (ZeroClasses/VonKochRH.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import von_koch_rh  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return von_koch_rh.main(os.path.join(d, "von_koch_rh.json"))


def test_somas_e_crescimento():
    # `somas_limitadas`/`cota_gen` (numérico): S_N(0,8) → H(0,8); `norm_H_le`: |H(σ + it)| ≪ (1 + t)^{0,1}
    out = _out()
    p = out["parciais"]
    assert p[-1]["dif"] < 0.02 < p[0]["dif"]
    assert all(r["razao"] < 2 for r in out["crescimento"])


def test_coeficientes_e_von_koch():
    # `norm_fco_le`: |Λ(n) − 1| ≤ (1/δ + 1) n^δ; `psi_of_RH` nos dados: |ψ(N) − N| ≤ (N + 1)^{1/2+ε} até 10⁶
    out = _out()
    assert all(r["max_razao"] <= 1 for r in out["coeficientes"])
    assert all(r["max_razao"] < 1 for r in out["von_koch"])
