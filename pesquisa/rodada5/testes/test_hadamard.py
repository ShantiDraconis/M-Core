"""Testes do companheiro numérico de ATK/HadamardGenero0 e ATK/XiCrescimento (rodada 11)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import edrei  # noqa: E402
import hadamard  # noqa: E402


def test_I0_produto_genero0():
    # B(w) = Σ wⁿ/(n!)² = ∏(1 + 4w/j₀,ₖ²): as funções simétricas dos αₖ são os coeficientes (`coef_eq_lim`)
    zs, p = hadamard.potencias_alpha_I0()
    assert abs(zs[0] - edrei.J01) < 1e-13
    assert abs(p[0] - 1) < 1e-10 and abs(p[1] - 0.5) < 1e-12
    e = hadamard.elementares(p)
    for n in range(1, 6):
        assert abs(e[n] * math.factorial(n) ** 2 - 1) < 1e-10


def test_prodCoef_monotono_e_limitado():
    # `prodCoef_mono`, `prodCoef_le`: os coeficientes parciais crescem com N e ficam ≤ a₀(Σα)ⁿ e ≤ o limite
    zs = hadamard.zeros_j0(30)
    al = [4 / z ** 2 for z in zs]
    cs = [hadamard.prod_coef(1.0, al[:N], 4) for N in range(31)]
    for n in range(5):
        col = [c[n] for c in cs]
        assert all(col[i] <= col[i + 1] + 1e-15 for i in range(30))
        assert col[-1] <= 1 / math.factorial(n) ** 2 + 1e-15
        assert col[-1] <= sum(al) ** n + 1e-15


def test_xi_soma_inversos_quadrados():
    # a₁/a₀ = Σ1/γₖ² (coeficiente n = 1 do produto de gênero 0 de B, sob zeros na linha)
    a0, a1 = edrei.a_xi(0), edrei.a_xi(1)
    p1, _ = hadamard.p_xi()
    parcial = math.fsum(1 / g ** 2 for g in hadamard.GAMMAS)
    assert p1 - parcial > 0.007  # a cauda (zeros > 20) pesa ~30 %
    assert abs(a1 / a0 - p1) < 2e-6


def test_xi_e2():
    a0, a2 = edrei.a_xi(0), edrei.a_xi(2)
    p1, p2 = hadamard.p_xi()
    assert abs(a2 / a0 - (p1 ** 2 - p2) / 2) < 1e-7
