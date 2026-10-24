"""Testes do companheiro numérico de ATK/TuranDispersao (rodada 15)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import turan  # noqa: E402


def test_phid_formula():
    # ∂ᵤphiT = (−8w³ + 30w² − 15w)e^{u/2−w} (`hasDerivAt_phiT`)
    for u in (0.1, 0.3, 0.8):
        e = 1e-6
        fd = (turan.phi_e_phid(u + e)[0] - turan.phi_e_phid(u - e)[0]) / (2 * e)
        d = turan.phi_e_phid(u)[1]
        assert abs(fd - d) < 1e-7 * max(1.0, abs(d))


def test_psi_crescente():
    # o lema de Csordas (BUILD_PENDING no kernel), numa malha de (0, 2]
    ps = [turan.psi(k * 0.001) for k in range(1, 2001)]
    assert all(ps[i + 1] > ps[i] for i in range(len(ps) - 1))


def test_identidade_dispersao():
    # (2m+3)γ_{m+1}² − (2m+1)γ_mγ_{m+2} = ½∬KK(ts)^{2m+2}(t²−s²)(ψ(t)−ψ(s)) (`turan_disp`)
    g = [turan.gam(k) for k in range(5)]
    for m in (0, 1):
        lhs = (2 * m + 3) * g[m + 1] ** 2 - (2 * m + 1) * g[m] * g[m + 2]
        rhs = turan.dispersao(m)
        assert lhs > 0 and abs(lhs - rhs) < 1e-6 * lhs
