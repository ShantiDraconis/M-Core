"""Testes do companheiro numérico de ATK/ZeroClasses/Forcar (rodada 23)."""
import itertools
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "codigo"))
import encontro as en  # noqa: E402
import forcar as fo  # noqa: E402
import zeroclasses as zc  # noqa: E402


def test_quarteto_e_simetrias():
    # `Pq_eq_Q`, `Pq_zero_iff`, `Pq_refl`, `Pq_conj`
    d, T, s = 0.2, 5.0, complex(0.1, 1.3)
    assert abs(fo.Pq(d, T, s) - fo.Q(d, T, s)) < 1e-9 * abs(fo.Q(d, T, s))
    for e in (1, -1):
        for f in (1, -1):
            assert abs(fo.Pq(d, T, complex(0.5 + e * d, f * T))) < 1e-10
    assert abs(fo.Pq(d, T, 1 - s) - fo.Pq(d, T, s)) < 1e-9
    assert abs(fo.Pq(d, T, s.conjugate()) - fo.Pq(d, T, s).conjugate()) < 1e-9


def test_somar_nao_forca():
    # `somar_nao_forca`: Ξ_λ(ρ) = ξ(ρ) no zero de P
    d, T = 0.1, 7.0
    rho = complex(0.5 + d, T)
    for lam in (1.0, -3.0, 1e4):
        assert abs(en.xi(rho) + lam * fo.Pq(d, T, rho) - en.xi(rho)) < 1e-9


def test_exemplos_do_certificado():
    # `exemplo_linear`, `exemplo_quadratico`, `contraexemplo`
    c = complex(0.75, 10)
    assert fo.certificado(lambda z: z - complex(0.8, 10), c, 1 / 8)["passa"]
    assert fo.certificado(lambda z: (z - c) + 0.25 * (z - c) ** 2 + 0.05, c, 1 / 8)["passa"]
    assert not fo.certificado(lambda z: 1 + (z - c), c, 1 / 8)["passa"]
    w = -2 + math.sqrt(95) / 5
    assert abs((c + w - c) + 0.25 * (w) ** 2 + 0.05) < 1e-15 and abs(w) < 1 / 8 and (c + w).real > 0.5


def test_zeta_linha_passa_fora_falha():
    # o certificado reencontra os zeros da linha; fora da linha (sem zeros) ele falha
    for g in en.GAMMAS[:3]:
        r0 = zc.zero_newton(complex(0.5, g))
        assert fo.certificado(zc.zeta, r0 + complex(2e-4, -1e-4), 1e-3)["passa"]
    for sig in (0.65, 0.85):
        for t in (12, 20, 33):
            assert not fo.certificado(zc.zeta, complex(sig, t), 0.05, amostras=12, aneis=2)["passa"]


def test_sat_lacuna():
    # `sat_iff_zero`, `lacuna`, `viol_eq_prod`
    phi = [[(0, True), (1, False)], [(1, True), (2, True)], [(0, False), (2, False)]]
    vals = {x: fo.R(phi, x) for x in itertools.product((False, True), repeat=3)}
    assert all(isinstance(v, int) and v >= 0 for v in vals.values())
    assert any(v == 0 for v in vals.values())
    assert min(fo.R([[(0, True)], [(0, False)]], x) for x in ((False,), (True,))) == 1


def test_divisibilidade_e_assintotico():
    assert 84 - 7 * 12 == 0 and 85 % 7 != 0
    vals = [(math.log(10 ** k)) ** 2 / 10 ** k for k in (2, 4, 8)]
    assert vals[0] > vals[1] > vals[2] > 0
    x = math.exp(5)
    assert math.log(x) * math.log(x) > 3 * math.log(x)  # n^{log n} > n³ em n = e⁵
