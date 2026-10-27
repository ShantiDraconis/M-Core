"""Testes do companheiro numérico da rodada 47 (ZeroClasses/HardyCuspide.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import hardy_cuspide as hc  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return hc.main(os.path.join(d, "hardy_cuspide.json"))


def test_norm_th_cusp():
    # `norm_th_cusp`: |θ(i + η)| ≤ K₀ |η|^{−1/2} e^{−(π/4) Re(1/η)} quando Re(1/η) ≥ 1
    out = _out()
    assert out["cuspide"]
    for c in out["cuspide"]:
        assert c["Re_inv"] >= 1 and c["theta"] <= c["cota"]


def test_Th_cai_na_cuspide():
    # `iteratedDeriv_Th_tendsto` (tendência): |Θ(iα)| e |Θ′(iα)| caem quando α → π/4
    out = _out()
    v = [x["Th"] for x in out["Th_iα"]]
    d = [x["dTh"] for x in out["Th_iα"]]
    assert all(a > b for a, b in zip(v, v[1:]))
    assert d[-1] < d[0]
    cotas = [out["cota_r_le_1_250"][k] for k in ("0.004", "0.002", "0.001", "0.0005")]
    assert all(a > b for a, b in zip(cotas, cotas[1:]))
