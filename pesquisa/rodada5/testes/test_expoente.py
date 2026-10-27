"""Testes do companheiro numérico da rodada 35 (ZeroClasses/Expoente.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import expoente as ex  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return ex.main(os.path.join(d, "expoente.json"))


def test_somas():
    # `nao_somavel_ZM`, `expoente_exato`: Σ 1/|ρ| acompanha (log(T/2π))²/(2π); `N_tende_infinito`
    out = _out()
    s = out["somas"]
    for v in s.values():
        assert abs(v["soma_1"] - v["previsto_soma_1"]) < 0.06
    assert s["300"]["N"] == 138 and s["300"]["soma_1"] > 2 * s["50"]["soma_1"]


def test_xi_par():
    # `xi_lb_par`: |ξ(2n+2)| ≥ (2 − π²/6) n!/π^{n+1}; log ξ(s)/s cresce (não é O(s))
    out = _out()
    xp = out["xi_par"]
    assert all(v["ok"] for v in xp.values())
    vals = [xp[k]["log_xi_sobre_s"] for k in ("1", "3", "5", "10", "20", "40")]
    assert all(b > a for a, b in zip(vals, vals[1:]))
