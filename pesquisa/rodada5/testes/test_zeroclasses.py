"""Testes do companheiro numérico de ATK/ZeroClasses (rodadas 16–19) e ATK/TruncamentoToeplitz."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import zeroclasses as zc  # noqa: E402


def test_zeta_controles():
    assert abs(zc.zeta(2) - math.pi ** 2 / 6) < 1e-12
    assert abs(zc.zeta(-2)) < 1e-10  # zero trivial (`trivial_zero`)
    assert abs(zc.zeta(complex(0.5, zc.GAMMA1))) < 1e-10


def test_orbita_primeiro_zero():
    # na reta: órbita {ρ, ρ̄} de cardinal 2 (`quarteto_ou_par`), todos zeros (`orbita_nao_trivial`)
    rho = zc.zero_newton(complex(0.5, 14.13))
    assert abs(rho.real - 0.5) < 1e-10
    assert all(abs(zc.zeta(w)) < 1e-10 for w in zc.orbita(rho))
    assert zc.card_orbita(rho) == 2
    # fora da reta e fora do eixo: 4 (`card_quatro`); no ponto c: 1 (`card_um`)
    assert zc.card_orbita(complex(0.3, 2.0)) == 4
    assert zc.card_orbita(complex(0.5, 0.0)) == 1
    assert zc.card_orbita(complex(0.3, 0.0)) == 2


def test_K3_vazio_e_encaixe():
    assert not zc.malha_K(3)  # `K_tres`
    for n in range(4, 12):
        assert set(zc.malha_K(n)) <= set(zc.malha_K(n + 1))  # `K_mono`


def test_minimos_decrescem_e_positivos():
    ms = [zc.m_malha(n)[0] for n in range(4, 15)]
    assert all(ms[i + 1] <= ms[i] for i in range(len(ms) - 1))  # `m_antitone`
    assert all(m > 0.1 for m in ms)  # verificação finita (não certificada)


def test_truncamento_P():
    a = zc.coef(10)
    for N in range(0, 5):
        pos, zer, ind, neg = zc.sinais_P(a, N)
        assert neg == 0 and ind == 0
        # contagem: todos os pares (I, J) de mesmo tamanho r ≥ 1 em {0..N}
        assert pos + zer == math.comb(2 * N + 2, N + 1) - 1


def test_menor3_e_defeito():
    a = zc.coef(6)
    m3 = a[1] ** 3 - 2 * a[0] * a[1] * a[2] + a[0] ** 2 * a[3]
    from fractions import Fraction as Fr
    af = [Fr(x) for x in a]
    assert abs(float(zc.menor(af, (1, 2, 3), (0, 1, 2))) - m3) < 1e-12 * abs(m3)  # `menor3`
    assert m3 > 0
    assert all(zc.D2(a, n) > 0 for n in range(3))


def test_fluxo():
    a = zc.coef(8)
    for n in range(4):
        vals = [zc.D2(zc.fluxo(a, t), n) / math.exp(-2 * t * (n + 1) * n) for t in (0.0, 0.1, 0.5, 1.0)]
        # `D2_fluxo`: normalizado = a_{n+1}² − e^{−2τ}aₙa_{n+2}, crescente em τ (`defeito_monotono`)
        for t, v in zip((0.0, 0.1, 0.5, 1.0), vals):
            assert abs(v - (a[n + 1] ** 2 - math.exp(-2 * t) * a[n] * a[n + 2])) < 1e-12 * a[n + 1] ** 2
        assert all(vals[i] <= vals[i + 1] for i in range(3))
    ex = [1.0, 1.0, 2.0, 1.0]
    assert zc.D2(ex, 0) < 0 < zc.D2(zc.fluxo(ex, 1.0), 0)  # `volta_ingenua_invalida`


def test_z2_mais_1():
    assert abs(1j ** 2 + 1) == 0  # zero imaginário puro
    assert all(abs(x * x + 1) >= 1 for x in [k / 10 for k in range(-100, 101)])  # nenhum real


def test_mundo_fora_modelo():
    # modelo (não é ζ): um quarteto hipotético fora da linha, com a órbita do kernel (`ponto_medio`,
    # `equilibrio`): o ponto médio de ρ e 1 − ρ̄ está na linha e os desvios β − 1/2 somam zero.
    for rho in (complex(0.6, 20.0), complex(0.51, 1e6), complex(0.9, 3.0)):
        q = zc.orbita(rho)
        assert zc.card_orbita(rho) == 4
        meio = (rho + (1 - rho.conjugate())) / 2
        assert abs(meio.real - 0.5) < 1e-12 and abs(meio.imag - rho.imag) < 1e-9
        acima = [w for w in q if w.imag > 0]
        assert abs(sum(w.real - 0.5 for w in acima)) < 1e-12


def FM(d, t, z):
    w = z - 0.5
    return (w * w + t * t) * ((w - d) ** 2 + t * t) * ((w + d) ** 2 + t * t)


def test_familia_dois_casos():
    # `ATK.ZeroClasses.Complementar`: F_{d,t}(1 − z) = F_{d,t}(z); zeros 1/2 ± it, 1/2 ± d ± it;
    # todos na reta ⟺ d = 0; ponto médio dos externos = zero central.
    t = 1.0
    for d in (0.0, 0.25, 0.1):
        for z in (complex(0.3, 0.7), complex(-1.0, 2.0), complex(0.5, 5.0)):
            assert abs(FM(d, t, 1 - z) - FM(d, t, z)) < 1e-9 * max(1.0, abs(FM(d, t, z)))
        zeros = [complex(0.5 + e * d, s * t) for e in (0, 1, -1) for s in (1, -1)]
        assert all(abs(FM(d, t, z)) < 1e-12 for z in zeros)
        fora = [z for z in zeros if abs(z.real - 0.5) > 1e-15]
        assert (len(fora) == 0) == (d == 0.0)
        assert abs((complex(0.5 - d, t) + complex(0.5 + d, t)) / 2 - complex(0.5, t)) < 1e-15


def test_triviais_rigidez():
    z = [-2 * (n + 1) for n in range(10)]
    assert all(z[n + 2] - 2 * z[n + 1] + z[n] == 0 for n in range(8))  # `triv_segunda_diferenca`
    # zeros triviais de ζ (Euler–Maclaurin em ponto flutuante perde precisão por cancelamento além de −4)
    assert all(abs(zc.zeta(x)) < 1e-9 for x in z[:2])


def test_derivada_triviais():
    # `deriv_trivial_fechada`: ζ′(−2k) = (−1)ᵏ(2k)! ζ(2k+1) / (2(2π)^{2k}), por diferenças centrais
    for k in (1, 2):
        h = 1e-3  # passo maior: o Euler–Maclaurin em ponto flutuante tem ruído ~1e-11 perto de −4
        fd = (zc.zeta(-2 * k + h) - zc.zeta(-2 * k - h)) / (2 * h)
        formula = (-1) ** k * math.factorial(2 * k) * zc.zeta(2 * k + 1).real / (2 * (2 * math.pi) ** (2 * k))
        assert abs(fd - formula) < 1e-4 * abs(formula)
    assert abs(-math.factorial(2) * zc.zeta(3).real / (2 * (2 * math.pi) ** 2) + 0.0304484571) < 1e-9


def test_construcao_ZATK():
    # `Construcao`: Z_ATK = ζ·P_N preserva os zeros de ζ e acrescenta os quartetos ½ ± δₙ ± itₙ, δₙ = 1/(2n+3)
    def Q(d, t, s):
        return ((s - 0.5 - d) ** 2 + t * t) * ((s - 0.5 + d) ** 2 + t * t)

    t = [3.0, 5.0, 7.0]
    def PN(s):
        out = 1.0
        for n, tn in enumerate(t):
            out *= Q(1 / (2 * n + 3), tn, s)
        return out
    for n, tn in enumerate(t):
        d = 1 / (2 * n + 3)
        for z in (complex(0.5 + d, tn), complex(0.5 + d, -tn), complex(0.5 - d, tn), complex(0.5 - d, -tn)):
            assert abs(PN(z)) < 1e-6
        z0 = complex(0.3, 0.2)
        assert abs(PN(1 - z0) - PN(z0)) < 1e-12 * abs(PN(z0))  # P_N(1 − s) = P_N(s)
    rho = zc.zero_newton(complex(0.5, 14.13))
    assert abs(zc.zeta(rho) * PN(rho)) < 1e-10 * abs(PN(rho))  # zeros de ζ preservados
    assert all(abs(PN(complex(-2 * k, 0))) > 1 for k in (1, 2, 3))  # triviais continuam simples
