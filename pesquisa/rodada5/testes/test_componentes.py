"""Testes do companheiro numérico de ATK/ZeroClasses/Componentes (rodada 22)."""
import cmath
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import componentes as co  # noqa: E402
import zeroclasses as zc  # noqa: E402


def test_cauchy_riemann_e_perpendicular():
    # `cauchy_riemann`, `cruzamento_perpendicular`
    rho = zc.zero_newton(complex(0.5, 14.13))
    w = co.dz(rho)
    us, ut, vs, vt = co.cauchy_riemann(rho)
    assert abs(us - vt) < 1e-7 and abs(ut + vs) < 1e-7
    assert abs(us - w.real) < 1e-7 and abs(ut + w.imag) < 1e-7
    assert abs(us * vs + ut * vt) < 1e-7  # ∇u ⟂ ∇v
    assert abs((us - vs) * (us + vs) + (ut - vt) * (ut + vt)) < 1e-7  # ∇(u−v) ⟂ ∇(u+v)


def test_curvas_C():
    # `cruzam_so_no_zero`: u = v e u = −v só no zero; `igual_nao_e_zero`
    rho = zc.zero_newton(complex(0.5, 21.02))
    z = zc.zeta(rho)
    assert abs(z.real) < 1e-10 and abs(z.imag) < 1e-10
    w = 1 + 1j
    assert w.real == w.imag and w != 0


def test_minimos_sao_zeros():
    # `minimo_local_e_zero`: os mínimos locais da malha caem sobre zeros (todos na linha)
    sig, tt, A = co.malha(0.05, 0.95, 10.0, 40.0, 0.05, 0.02)
    mins = co.minimos_locais(sig, tt, A)
    assert len(mins) == 6  # zeros com 10 < γ < 40: 14,13; 21,02; 25,01; 30,42; 32,94; 37,59
    for s, t, _ in mins:
        r = zc.zero_newton(complex(s, t))
        assert abs(zc.zeta(r)) < 1e-10 and abs(r.real - 0.5) < 1e-9


def test_minimo_na_fronteira():
    # `minimo_na_fronteira`: região sem zeros ⇒ sem mínimo interior; mínimo na borda
    sig, tt, A = co.malha(0.55, 0.95, 10.0, 30.0, 0.01, 0.02)
    assert co.minimos_locais(sig, tt, A) == []
    i, k = min(((i, k) for i in range(len(sig)) for k in range(len(tt))), key=lambda p: A[p[0]][p[1]])
    assert i == 0  # na borda σ = 0,55


def test_residuo():
    # `residuo_primeiro_zero`: (s − ρ₁)ζ′/ζ → 1
    rho = zc.zero_newton(complex(0.5, 14.13))
    for d in (1e-3, 1e-4):
        q = d * co.dz(rho + d) / zc.zeta(rho + d)
        assert abs(q - 1) < 10 * d


def test_riemann_von_mangoldt():
    assert abs(co.N_principal(1e3) - 649) < 1  # N(1000) = 649
    assert abs(co.N_principal(3000175332800.0) / 1.2363e13 - 1) < 1e-3  # Platt–Trudgian: ≈ 1,2363·10¹³ zeros
    assert 101.5 < co.N_principal_log(100) < 101.6  # N(10¹⁰⁰) ≈ 3,62·10¹⁰¹, não 10¹⁰²


def test_cosh_modelo():
    # `simetria_sem_fora`: zeros ½ + i(2k+1)π/2, todos na linha; F(1 − s) = F(s); F(s̄) = conj F(s)
    for k in range(-4, 4):
        z = 0.5 + 1j * (2 * k + 1) * math.pi / 2
        assert abs(cmath.cosh(z - 0.5)) < 1e-14
    s = complex(0.3, 2.0)
    assert abs(cmath.cosh(1 - s - 0.5) - cmath.cosh(s - 0.5)) < 1e-14
    assert abs(cmath.cosh(s.conjugate() - 0.5) - cmath.cosh(s - 0.5).conjugate()) < 1e-14
