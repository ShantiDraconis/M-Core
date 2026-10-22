"""Testes do espelho Python de ATK–Closed Math (unittest; também roda com pytest).

Exatos (Fraction / racionais gaussianos) para as identidades algébricas; numéricos com tolerância
para geometria, contornos e o critério terminal. SymPy é usado quando disponível.
"""
import math, os, sys, unittest, cmath
from fractions import Fraction as Fr
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "codigo"))
import closed_math as cm  # noqa: E402
from closed_math import Q, I, HALF  # noqa: E402

PONTOS = [Q(Fr(a, 7), Fr(b, 5)) for a in range(-4, 5) for b in range(-4, 5)]
PARAMS = [(Fr(0), Fr(1)), (Fr(1, 4), Fr(1)), (Fr(1, 10), Fr(14)), (Fr(-2, 3), Fr(5, 2))]


class Semantica(unittest.TestCase):
    def test_exaustivo_exclusivo(self):
        for zero in (True, False):
            for linha in (True, False):
                estados = [zero and linha, zero and not linha, (not zero) and linha, (not zero) and not linha]
                self.assertEqual(sum(estados), 1)

    def test_verificador(self):
        self.assertEqual(cm.checar(0, 0), "indeterminado")
        self.assertEqual(cm.checar(0.3, 0.1), "naoZero")
        self.assertEqual(cm.checar(0.05, 0.1), "indeterminado")
        self.assertEqual(cm.checarIC(Fr(1, 10), Fr(2, 10), Fr(-1), Fr(1)), "naoZero")
        self.assertEqual(cm.checarIC(Fr(-1, 10), Fr(2, 10), Fr(-1), Fr(1)), "indeterminado")


class Operadores(unittest.TestCase):
    def test_klein_e_troca(self):
        for s in PONTOS:
            self.assertEqual(cm.opJ(cm.opJ(s)), s)
            self.assertEqual(cm.opR(cm.opR(s)), s)
            self.assertEqual(cm.opS(cm.opS(s)), s)
            self.assertEqual(cm.opT(cm.opT(s)), s)
            self.assertEqual(cm.opR(cm.opJ(s)), cm.opS(s))
            self.assertEqual(cm.opR(cm.opS(s)), cm.opJ(s))
            self.assertEqual(cm.opT(cm.opR(cm.opT(s))), s.conj() + I)
            self.assertEqual(cm.opR(s).re() - Fr(1, 2), -(s.re() - Fr(1, 2)))
            self.assertEqual((cm.opT(cm.opR(cm.opT(s))) == s), s.im() == Fr(1, 2))

    def test_par(self):
        for d in (Fr(1, 10), Fr(-3, 7), Fr(0)):
            for t in (Fr(14), Fr(-1, 3)):
                sp, sm = HALF + d + t * I, HALF - d + t * I
                self.assertEqual((sp + sm) / 2, HALF + t * I)
                self.assertEqual((sp - sm).normSq(), 4 * d * d)
                self.assertEqual(sp == sm, d == 0)
                self.assertEqual((cm.opT(sp) + cm.opT(sm)) / 2, Q(t, Fr(1, 2)))


class Modelo(unittest.TestCase):
    def test_identidades(self):
        for d, g in PARAMS:
            for s in PONTOS:
                self.assertEqual(cm.G(d, g, s), cm.G_fat(d, g, s))
                self.assertEqual(cm.G(d, g, cm.opS(s)), cm.G(d, g, s))
                self.assertEqual(cm.G(d, g, s.conj()), cm.G(d, g, s).conj())
            for z in cm.raizes(d, g):
                self.assertEqual(cm.G(d, g, z), 0)

    def test_nao_zeros(self):
        for d, g in PARAMS:
            self.assertEqual(cm.G(d, g, HALF), Q((d * d + g * g) ** 2))
            self.assertNotEqual(cm.G(d, g, Q(2)), 0)

    def test_polinomio_conservacao_multiplicidade(self):
        g = Fr(1)
        for d in (Fr(1, 4), Fr(1, 2), Fr(0)):
            p = cm.prod_lin(cm.raizes(d, g))
            self.assertEqual(p.deg(), 4)                        # conservação da contagem
            for s in PONTOS[:20]:
                self.assertEqual(p.ev(s), cm.G(d, g, s))
        self.assertEqual(cm.mult(cm.prod_lin(cm.raizes(Fr(0), g)), HALF + I), 2)
        self.assertEqual(cm.mult(cm.prod_lin(cm.raizes(Fr(1, 4), g)), Fr(3, 4) + I), 1)
        for m in range(1, 8):
            self.assertEqual(cm.mult(cm.lin(2) ** m, Q(2)), m)

    def test_H_ordem(self):
        g = Fr(1)
        for d, esperado in ((Fr(0), 3), (Fr(1, 4), 1)):
            hn = cm.prod_lin([HALF + g * I, HALF - g * I] + cm.raizes(d, g))
            self.assertEqual(cm.mult(hn, HALF + I), esperado)


class Taxonomia(unittest.TestCase):
    def test_truncamentos(self):
        for n in range(80):
            self.assertNotEqual(Fr((10 ** n) // 3, 10 ** n), Fr(1, 3))
        self.assertEqual(Fr(33, 100) - Fr(1, 3), Fr(-1, 300))

    def test_limite(self):
        for h in (1e-2, 1e-4, -1e-4):
            x = 1 + h
            self.assertAlmostEqual((x * x - 1) / (x - 1), 2, delta=2 * abs(h) + 1e-9)

    def test_sin_pi(self):
        for k in range(-30, 31):
            self.assertLess(abs(cmath.sin(math.pi * k)), 1e-12)
        self.assertGreater(abs(cmath.sin(math.pi * (0.5 + 0.1j))), 0.5)

    def test_contornos(self):
        L = lambda z: 3 / (z - 1) + 2 / (z + 2) - 2 / z - 1 / (z - 4)
        self.assertAlmostEqual(cm.contorno(L, 0, 3).real, 3, places=8)
        for d in (0.25, 0.0):
            A = [0.5 + 1j, 0.5 - 1j, 0.5 + d + 1j, 0.5 + d - 1j, 0.5 - d + 1j, 0.5 - d - 1j]
            self.assertAlmostEqual(cm.contorno(lambda z: sum(1 / (z - a) for a in A), 0.5, 2).real, 6, places=8)


class Geometria(unittest.TestCase):
    def test_esfera(self):
        for s in (0.6 + 14j, 0.4 + 14j, 3 - 2j, 0j):
            self.assertAlmostEqual(np.linalg.norm(cm.P(s)), 1, places=12)
        sp, sm = 0.6 + 14j, 0.4 + 14j
        corda = np.linalg.norm(cm.P(sp) - cm.P(sm))
        self.assertAlmostEqual(corda, 2 * abs(sp - sm) / math.sqrt((1 + abs(sp) ** 2) * (1 + abs(sm) ** 2)), places=14)
        self.assertAlmostEqual(2 * math.asin(corda / 2), 0.002028, places=6)

    def test_cilindro_cone(self):
        self.assertAlmostEqual(np.linalg.norm(cm.Cil(0.6 + 14j)[:2] - cm.Cil(0.4 + 14j)[:2]), 1.175571, places=6)
        k = cm.Kc(0.1, math.pi)
        self.assertAlmostEqual(k[0] ** 2 + k[1] ** 2, k[2] ** 2, places=14)
        self.assertTrue(np.allclose(cm.Kc(0, 1.0), cm.Kc(0, 2.0)))       # cone perde a ordenada
        self.assertFalse(np.allclose(cm.Kt(28, 0, 1.0), cm.Kt(28, 0, 2.0)))  # cone elevado não

    def test_toro(self):
        R, r, T = 3.0, 1.0, 28.0
        for s in (0.3 + 2j, 0.5 + 14j, 0.9 - 7j):
            x, y, z = cm.tor(R, r, T, s)
            self.assertAlmostEqual((math.hypot(x, y) - R) ** 2 + z ** 2, r * r, places=12)
            xR = cm.tor(R, r, T, complex(1 - s.real, s.imag))
            self.assertTrue(np.allclose(xR, [x, y, -z]))                 # R = espelho z ↦ −z
            xS = cm.tor(R, r, T, 1 - s)
            self.assertTrue(np.allclose(xS, [x, -y, -z]))                # S = rotação de π
        self.assertAlmostEqual(math.hypot(*cm.tor(R, r, T, 0.5 + 5j)[:2]), R - r, places=12)
        self.assertAlmostEqual(cm.Kg(R, r, math.pi), -1 / (r * (R - r)), places=14)
        th = np.linspace(0, 2 * np.pi, 20001)
        self.assertAlmostEqual(2 * np.pi * np.trapezoid(r * (R + r * np.cos(th)), th), 4 * math.pi ** 2 * R * r, places=6)
        gb = 2 * np.pi * np.trapezoid(np.array([cm.Kg(R, r, x) for x in th]) * r * (R + r * np.cos(th)), th)
        self.assertAlmostEqual(gb, 0, places=8)                         # Gauss–Bonnet
        self.assertLess(np.linalg.norm(cm.tor(R, r, T, 1 + 1j) - cm.tor(R, r, T, 0 + 1j)), 1e-12)  # reencontro
        for sig in [x for x in np.linspace(0.01, 0.99, 50) if min(abs(x - 0.25), abs(x - 0.75)) > 1e-6]:
            self.assertEqual(cm.Kg(R, r, 2 * math.pi * sig) < 0, 0.25 < sig < 0.75)


class Superficies(unittest.TestCase):
    """Helicoide, cilindro parabólico, sela e hiperboloide recuperam s (injetivas); o toro não."""
    def test_recuperacao(self):
        rng = np.random.default_rng(7)
        for _ in range(200):
            s = complex(rng.uniform(0.01, 0.99), rng.uniform(-40, 40))
            x, y, z = s.real * math.cos(s.imag), s.real * math.sin(s.imag), s.imag      # helicoide
            self.assertAlmostEqual(complex(math.hypot(x, y), z), s, places=9)
            X, Y, Z = math.cosh(s.imag) * math.cos(s.real), math.cosh(s.imag) * math.sin(s.real), math.sinh(s.imag)
            self.assertAlmostEqual(complex(math.atan2(Y, X), math.asinh(Z)), s, places=6)  # hiperboloide
        R, r, T = 3.0, 1.0, 1.0
        a, b = 0.5 + 1j, 0.5 + 2j
        self.assertLess(np.linalg.norm(cm.tor(R, r, T, a) - cm.tor(R, r, T, b)), 1e-12)   # mesma imagem
        self.assertEqual(cm.G(0, 1, Q(Fr(1, 2), 1)), 0)
        self.assertNotEqual(cm.G(0, 1, Q(Fr(1, 2), 2)), 0)                                 # estados diferentes

    def test_margem_invariante(self):
        from zeta_em import zeta
        zs = cm.Kn_grade(8, ns=6, nt=40)
        m_plano = min(abs(zeta(z)) for z in zs)
        m_sela = min(abs(zeta(complex(p[0], p[1]))) for p in [(z.real, z.imag, z.real**2 - z.imag**2) for z in zs])
        self.assertEqual(m_plano, m_sela)

    def test_mu_real(self):
        for rho in (0.5 + 14.1347j, 0.6 + 14j, 0.4 - 3j):
            mu = (rho - 0.5) / 1j
            self.assertEqual(abs(mu.imag) < 1e-15, abs(rho.real - 0.5) < 1e-15)


class Terminal(unittest.TestCase):
    def test_bernoulli(self):
        B = cm.BN
        self.assertEqual(B[1], Fr(-1, 2)); self.assertEqual(B[2], Fr(1, 6)); self.assertEqual(B[4], Fr(-1, 30))
        self.assertEqual(B[10], Fr(5, 66)); self.assertEqual(B[3], 0)

    def test_EM_aproxima_zeta(self):
        from zeta_em import zeta
        for s in (0.75 + 3j, 0.6 + 14j, 0.9 - 20j):
            self.assertLess(abs(cm.EM(40, 10, s) - zeta(s)), 1e-9)

    def test_cota_E_valida(self):
        """A cota provada no kernel majora o erro observado em pontos de K_n."""
        from zeta_em import zeta
        for n in (5, 10, 20):
            for z in cm.Kn_grade(n, ns=5, nt=7):
                self.assertLessEqual(abs(cm.EM(10, 4, z) - zeta(z)), cm.Eb(n, 10, 4) * (1 + 1e-9) + 1e-12)

    def test_E_tende_zero(self):
        vals = [cm.Eb(10, N, 6) for N in (10, 100, 1000, 10000)]
        self.assertTrue(all(a > b for a, b in zip(vals, vals[1:])))
        self.assertLess(vals[-1], 1e-15)


try:
    import sympy as sp
except ImportError:
    sp = None


@unittest.skipIf(sp is None, "sympy ausente")
class Simbolico(unittest.TestCase):
    def test_G_sympy(self):
        s, d, g = sp.symbols("s d g")
        Gk = ((s - sp.Rational(1, 2)) ** 2 - d ** 2 + g ** 2) ** 2 + 4 * g ** 2 * d ** 2
        Gf = ((s - sp.Rational(1, 2) - d) ** 2 + g ** 2) * ((s - sp.Rational(1, 2) + d) ** 2 + g ** 2)
        self.assertEqual(sp.expand(Gk - Gf), 0)
        self.assertEqual(sp.expand(Gk.subs(s, 1 - s) - Gk), 0)
        raizes = sp.solve(Gf.subs({d: sp.Rational(1, 4), g: 1}), s)
        self.assertEqual(len(raizes), 4)

    def test_multiplicidade_sympy(self):
        s = sp.symbols("s")
        p = sp.Poly(((s - sp.Rational(1, 2)) ** 2 + 1) ** 3, s)
        self.assertEqual(sp.roots(p)[sp.Rational(1, 2) + sp.I], 3)

    def test_curvatura_sympy(self):
        th, R, r = sp.symbols("theta R r", positive=True)
        sqrtG = R + r * sp.cos(th)
        K = -(1 / (r * sqrtG)) * sp.diff(sp.diff(sqrtG, th) / r, th)
        self.assertEqual(sp.simplify(K - sp.cos(th) / (r * (R + r * sp.cos(th)))), 0)
        self.assertEqual(sp.integrate(sp.cos(th), (th, 0, 2 * sp.pi)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
