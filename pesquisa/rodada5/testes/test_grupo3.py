"""Testes do companheiro numérico do Grupo 3 (rodada 13): ATK/XiMomentos, ATK/ProdutoresTN, ATK/JensenPolya."""
import math
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import dbn  # noqa: E402
import edrei  # noqa: E402
import grupo3  # noqa: E402

A = grupo3.coef_xi()
GAM = [math.factorial(k) * A[k] for k in range(len(A))]


def test_M1_momentos_positivos():
    # aₙ = 2∫Φu²ⁿ/(2n)! > 0 (`aXi_pos`); a₀ = ξ(1/2)
    assert all(x > 0 for x in A)
    assert abs(A[0] - edrei.XI_MEIO) < 1e-12


def test_M2_sanduiche():
    # Cauchy–Schwarz (cota superior, incondicional) e Turán (cota inferior)
    for n in range(len(A) - 2):
        cs = A[n + 1] ** 2 * math.factorial(2 * n + 2) ** 2
        assert cs <= A[n] * math.factorial(2 * n) * A[n + 2] * math.factorial(2 * n + 4) * (1 + 1e-12)
        assert GAM[n] * GAM[n + 2] <= GAM[n + 1] ** 2


def test_M3_menores_contiguos_estaveis():
    for r in (2, 3, 4, 6):
        assert all(grupo3.sinal_estavel(A, r, k, eps=1e-12) == 1 for k in range(len(A) - r))


def test_G37_jensen_hiperbolicos():
    for d in (2, 3, 4, 5, 6):
        for n in range(len(A) - d):
            assert dbn.raizes_reais(grupo3.jensen(GAM, d, n))


def test_hankel_nao_toeplitz():
    # μ = (3/2)δ₀ + ½δ₁: Hankel [m_{i+j}] semidefinida (menores principais ≥ 0), Toeplitz com menor −7/2880
    m = [F(3, 2) * (1 if n == 0 else 0) + F(1, 2) for n in range(8)]
    for r in (1, 2, 3):
        assert grupo3.det([[m[i + j] for j in range(r)] for i in range(r)]) >= 0
    b = [m[n] / math.factorial(2 * n) for n in range(6)]
    assert grupo3.det([[grupo3.toep(b, i, j) for j in (0, 1, 2)] for i in (1, 2, 3)]) == F(-7, 2880)
