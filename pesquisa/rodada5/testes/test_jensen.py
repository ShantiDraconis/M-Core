"""Testes do companheiro numérico de ATK/JensenTuran.lean e ATK/ZeroCritico.lean."""
import os
import sys
from fractions import Fraction

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import jensen  # noqa: E402

D = jensen.D


@pytest.fixture(scope="module")
def coef():
    return jensen.coeficientes(40, D(1) / 64)


def test_a0_e_xi_meio(coef):
    _, a, _ = coef
    assert abs(a[0] - D("0.49712077818831410991")) < D("1e-19")


def test_a1_conhecido(coef):
    _, a, _ = coef
    assert abs(a[1] - D("0.01148597215757271876")) < D("1e-19")


def test_troca_de_sinal_no_primeiro_zero(coef):
    _, a, _ = coef
    assert jensen.Theta(a, -(D("14.13") ** 2)) > 0 > jensen.Theta(a, -(D("14.14") ** 2))


def test_primeiro_zero_dentro_do_disco_certificado(coef):
    _, a, _ = coef
    t1 = jensen.primeiro_zero(a, tol=D("1e-20"))
    assert abs(t1 - D("14.1347251417")) < D("1e-6")
    assert abs(t1 - D("14.134725141734693790")) < D("1e-17")


def test_turan_normalizado(coef):
    _, _, g = coef
    assert all(g[k + 1] ** 2 > g[k] * g[k + 2] for k in range(len(g) - 2))


def test_turan_ordem_3(coef):
    _, _, g = coef
    for k in range(len(g) - 3):
        x0, x1, x2, x3 = g[k:k + 4]
        assert 4 * (x1 ** 2 - x0 * x2) * (x2 ** 2 - x1 * x3) >= (x1 * x2 - x0 * x3) ** 2


def test_sanduiche_momentos(coef):
    M, _, _ = coef
    for n in range(len(M) - 2):
        assert M[n + 1] ** 2 <= M[n] * M[n + 2]                         # Cauchy–Schwarz
        assert (2 * n + 1) * M[n] * M[n + 2] <= (2 * n + 3) * M[n + 1] ** 2   # Turán


def test_toeplitz_gamma_falha_e_a_nao(coef):
    _, a, g = coef
    gF = [Fraction(x) for x in g]
    aF = [Fraction(x) for x in a]
    assert jensen.toeplitz(gF, 3, 1) < 0          # TP∞(γ) é falsa
    for r in range(1, 6):
        for k in range(0, 13):
            assert jensen.toeplitz(aF, r, k) >= 0  # coerente com TP∞(a)


def test_contraexemplo_binomial():
    a = [Fraction(1), Fraction(3), Fraction(3), Fraction(1)]
    g = [Fraction(1), Fraction(3), Fraction(6), Fraction(6)]
    assert jensen.toeplitz(a, 3, 1) == 10
    assert jensen.toeplitz(g, 3, 1) == -3


def test_jensen_hiperbolico_graus_baixos(coef):
    _, _, g = coef
    import math
    gF = [Fraction(x) for x in g]
    for d in range(1, 6):
        for n in range(0, 12):
            c = [Fraction(math.comb(d, j)) * gF[n + j] for j in range(d + 1)]
            assert jensen.sturm_reais(c) == d


def test_sturm_detecta_nao_hiperbolico():
    # X² + 1: nenhuma raiz real
    assert jensen.sturm_reais([Fraction(1), Fraction(0), Fraction(1)]) == 0
    # (X − 1)(X − 2)(X + 3)
    assert jensen.sturm_reais([Fraction(6), Fraction(-7), Fraction(0), Fraction(1)]) == 3
