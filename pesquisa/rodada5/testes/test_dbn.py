"""Testes do companheiro numérico de ATK/DeBruijnNewman e ATK/LaguerrePolya (rodada 12)."""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import dbn  # noqa: E402
import edrei  # noqa: E402


def test_H0_e_xi():
    # H₀(z) = ξ(1/2 + iz)/2 (`H_zero`) e troca de sinal no primeiro zero γ₁ = 14,1347…
    assert abs(dbn.H(0, 0) - edrei.XI_MEIO / 2) < 1e-12
    assert dbn.H(0, 14.13) > 0 > dbn.H(0, 14.14)


def test_calor_reverso():
    # ∂H/∂t = −∂²H/∂x² (`calor`)
    for t, x in ((0.0, 5.0), (0.2, 10.0), (-0.3, 2.0)):
        dt, mdxx = dbn.residuo_calor(t, x)
        assert abs(dt - mdxx) < 1e-5 * max(1.0, abs(dt)) + 1e-8


def test_laguerre_exato():
    p = dbn.P_TESTE  # (x+1)(x−1/2)²(x−3)
    assert dbn.raizes_reais(p)
    for c in (F(1, 3), F(-2), F(5), F(-1, 7)):
        assert dbn.raizes_reais(dbn.add(p, dbn.esc(c, dbn.der(p))))
    q = p
    for _ in range(10):
        q = dbn.add(q, dbn.esc(F(-1, 10), dbn.der(dbn.der(q))))
        assert dbn.raizes_reais(q)


def test_sentido_direto_falha():
    # X² tem raízes reais; (1 + D²)X² = X² + 2 não (`calor_direto_falha`)
    assert dbn.raizes_reais([F(0), F(0), F(1)])
    assert not dbn.raizes_reais([F(2), F(0), F(1)])
    assert not dbn.raizes_reais(dbn.mul([F(1), F(0), F(1)], dbn.produto([1, 1])))
