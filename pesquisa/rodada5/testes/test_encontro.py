"""Testes do companheiro numérico de ATK/ZeroClasses/Encontro (rodada 21)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import encontro as en  # noqa: E402
import zeroclasses as zc  # noqa: E402


def test_gamma_lanczos():
    assert abs(en.gamma(5) - 24) < 1e-10
    assert abs(en.gamma(0.5) - math.sqrt(math.pi)) < 1e-12
    assert abs(en.gamma(complex(-0.5, 0)) - (-2 * math.sqrt(math.pi))) < 1e-10


def test_det_A_e_matA():
    # `det_matA`, `det_zeta`: det A(w) = |w|²; `matA_mul` (multiplicação = produto de matrizes)
    w, v = complex(0.3, -1.2), complex(-2.0, 0.7)
    assert abs(en.det_A(w) - abs(w) ** 2) < 1e-15
    assert abs(en.det_A(w * v) - en.det_A(w) * en.det_A(v)) < 1e-12


def test_numeros_enviados():
    # os 15 módulos e o peso w conferem com os enviados (6 casas)
    assert format(abs(zc.zeta(complex(0.2, en.GAMMAS[0]))), ".6f") == "0.269427"
    assert format(abs(zc.zeta(complex(0.985, en.GAMMAS[2]))), ".6f") == "0.485033"
    z1, z2 = zc.zeta(complex(0.2, 14.134725)), zc.zeta(complex(0.8, 14.134725))
    w = -z1 / z2
    assert abs(w - complex(1.273752395525554, 0.062956684041557)) < 1e-9
    assert abs(z1 + w * z2) < 1e-15  # `dois_pontos`: exato por construção


def test_zeta_menos_meio():
    # `zeta_menos_meio`: ζ(−½) ≠ 0; valor = −ζ(3/2)/(4π)
    v = zc.zeta(-0.5).real
    assert abs(v - (-zc.zeta(1.5).real / (4 * math.pi))) < 1e-12
    assert v < -1 / (4 * math.pi)


def test_cruzamento_SD():
    # `cruzamento`: (|S|² + |D|²)/4 = |ξ(s₊)|² = det A = ξ(s₊)ξ(s₋), s₋ = 1 − s̄₊
    for s in (complex(0.6, 14.0), complex(0.3, 21.0), complex(0.51, 30.0)):
        a, b, S, D = en.SD(s)
        q = abs(a) ** 2
        assert abs(b - a.conjugate()) < 1e-12 * max(1e-30, abs(a)) + 1e-25  # `xi_espelho`
        assert abs((abs(S) ** 2 + abs(D) ** 2) / 4 - q) < 1e-9 * q
        assert abs(a * b - q) < 1e-9 * q


def test_estabilizacao():
    # `estabilizacao_primeiro_zero`: D(u)/u² → |ξ′(ρ₁)|² ≈ 1,9119·10⁻⁶; |ξ(ρ₁ − u)| = |ξ(ρ₁ + u)|
    rho = zc.zero_newton(complex(0.5, 14.13))
    d2 = abs(en.deriv(en.xi, rho)) ** 2
    assert abs(d2 - 1.911912079683e-6) < 1e-14
    erros = [abs(abs(en.xi(rho + u)) ** 2 / u ** 2 - d2) / d2 for u in (1e-1, 1e-2, 1e-3)]
    assert erros[0] > 50 * erros[1] > 2500 * erros[2]  # convergência quadrática
    assert abs(abs(en.xi(rho - 0.01)) - abs(en.xi(rho + 0.01))) < 1e-15


def test_colisao():
    # `Fcol_zero_iff`, `logderiv_Fcol`, `logderiv_limite`
    c, s = complex(0.5, 14.0), complex(0.3, 13.0)
    for n in (1, 10, 100):
        d = 1 / (2 * n + 1)
        assert abs(en.Fcol(d, c, c + d)) < 1e-15 and abs(en.Fcol(d, c, c - d)) < 1e-15
        lhs = 2 * (s - c) / en.Fcol(d, c, s)
        assert abs(lhs - (1 / (s - (c + d)) + 1 / (s - (c - d)))) < 1e-12
    assert abs(1 / (s - (c + 1e-6)) + 1 / (s - (c - 1e-6)) - 2 / (s - c)) < 1e-10


def test_varredura_curta():
    # mínimo positivo fora da linha num pedaço da malha (heurístico, não certificado)
    mn, arg, margem = en.bloco(0.55, 0.95, 14, 0.01, 0.02)
    assert 0.03 < mn < 0.05 and abs(arg[0] - 0.55) < 1e-12 and margem > 0


def test_escala_gigante():
    T, N = 10 ** 100, 10 ** 1000
    assert T * 10 ** 901 < 5 * (2 * N + 1)  # T·δ < 5·10⁻⁹⁰¹
    assert abs(math.log10(math.sqrt(T / (2 * math.pi))) - 49.60091006582094) < 1e-9
    borda = 1 / (4.896 * 100 * math.log(10))
    assert borda < 0.5 < 1 - borda  # `candidato_gigante`: dentro da janela
