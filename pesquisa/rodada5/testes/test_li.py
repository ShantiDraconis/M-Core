"""Testes do companheiro numérico de ATK/LiCriterio.lean."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import li  # noqa: E402


def test_lambda1_formula_fechada():
    lam = li.lambdas(nmax=3, N=40)
    assert abs(lam[0] - li.lambda1_exato()) < li.D("1e-18")


def test_primeiros_lambdas_positivos_e_crescentes():
    lam = li.lambdas(nmax=12, N=40)
    assert all(x > 0 for x in lam)
    assert all(lam[i] < lam[i + 1] for i in range(len(lam) - 1))


def test_lambda2_conhecido():
    lam = li.lambdas(nmax=2, N=40)
    assert abs(lam[1] - li.D("0.0923457352280466")) < li.D("1e-15")
