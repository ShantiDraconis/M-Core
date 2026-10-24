"""Testes do companheiro numérico de ATK/EdreiInteira e ATK/XiTP (rodada 10)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import edrei  # noqa: E402
import fechamento  # noqa: E402


def test_I0_razao_limite():
    b, rz = edrei.razoes_inversa_I0(60)
    assert all(x > 0 for x in b)
    assert all(rz[k + 1] <= rz[k] + 1e-15 for k in range(len(rz) - 1))
    assert abs(rz[-1] - 4 / edrei.J01 ** 2) < 1e-9  # raiz −1/L = −j₀,₁²/4


def test_I0_toeplitz_tn():
    assert fechamento.menor_minimo(edrei.coef_I0(8)) >= 0


def test_a_xi_zero():
    assert abs(edrei.a_xi(0) - edrei.XI_MEIO) < 1e-9


def test_a_xi_positivos_turan():
    a = [edrei.a_xi(n) for n in range(8)]
    assert all(x > 0 for x in a)
    assert all(a[n] ** 2 >= a[n - 1] * a[n + 1] for n in range(1, 7))
