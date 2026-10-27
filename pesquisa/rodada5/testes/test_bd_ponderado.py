"""Testes do companheiro numérico da rodada 59 (ZeroClasses/BDPonderado.lean)."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import bd_ponderado  # noqa: E402


def _out():
    with tempfile.TemporaryDirectory() as d:
        return bd_ponderado.main(os.path.join(d, "bd_ponderado.json"))


def test_meio_reproduz_DN():
    # `DNσ_meio`: D_N(½) = D_N — D₁ = 0,858212051…, D₂ = 0,289964574… (gram2.json); G₁₁ = log 2π − γ
    out = _out()
    d = out["D"]["0.5"]
    assert abs(d[0] - 0.85821205139551088) < 1e-7
    assert abs(d[1] - 0.28996457374220273) < 1e-7
    assert abs(out["G11_meio"] - out["log2pi_menos_gamma"]) < 1e-7


def test_monotonia():
    # D_N(σ) não cresce com N (mais funções na base) e cai com σ para N fixo, nos dados
    out = _out()
    D = out["D"]
    for s, v in D.items():
        assert all(a >= b - 1e-12 for a, b in zip(v, v[1:]))
    sig = sorted(D, key=float)
    for N in range(len(D[sig[0]])):
        assert all(D[a][N] > D[b][N] for a, b in zip(sig, sig[1:]))
