"""Testes do companheiro numérico de ATK/ZeroClasses e ATK/TruncamentoToeplitz (rodada 16)."""
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
