"""Testes do companheiro numérico da rodada 108 (atk-kernel/ATK/LiTruncado.lean)."""
import math
import os

DADOS = os.path.join(os.path.dirname(__file__), "..", "dados", "lambda_ate_10000.tsv")
EULER_GAMMA = 0.57721566490153286061


def tabela():
    linhas = [l.rstrip("\n").split("\t") for l in open(DADOS)]
    assert linhas[0] == ["n", "lambda_n", "cota_inferior", "raio_relativo"]
    return [(int(n), float(lam), float(cota)) for n, lam, cota, _ in linhas[1:]]


def principal(n):
    return n / 2 * (math.log(n) - 1 + EULER_GAMMA - math.log(2 * math.pi))


def test_todos_positivos_ate_10000():
    t = tabela()
    assert [n for n, _, _ in t] == list(range(1, 10001))
    assert all(cota > 0 for _, _, cota in t)


def test_lambda_um_forma_fechada():
    # λ₁ = 1 + γ/2 − ½ log 4π (ATK.ZeroClasses.LiUm, rodada 69)
    _, lam1, _ = tabela()[0]
    assert abs(lam1 - (1 + EULER_GAMMA / 2 - math.log(4 * math.pi) / 2)) < 1e-15


def test_termo_principal_negativo_no_comeco():
    # Lei 5 (principal_negativo prova 1 ≤ n ≤ 6 no kernel); numericamente vale até n = 9, e λₙ > 0 ali
    t = tabela()
    for n in range(1, 10):
        assert principal(n) < 0 < t[n - 1][1]
    assert principal(10) > 0


def test_desvio_do_termo_principal():
    # λₙ − (n/2)(log n − 1 + γ − log 2π) = O(√n log n) sob RH (Keiper; Bombieri–Lagarias); aqui |·| < √n log n
    for n, lam, _ in tabela()[9:]:
        assert abs(lam - principal(n)) < math.sqrt(n) * math.log(n)


def test_dh_taxa():
    # Lei 6: |w(σ)|² − 1 = (2β − 1)/((1 − β)² + γ²) para o zero de Davenport–Heilbronn β + iγ
    b, g = 0.80851718245663738555, 85.699348485377592172
    x = (2 * b - 1) / ((1 - b) ** 2 + g ** 2)
    assert 84014e-9 < x < 84015e-9
    # taxa de crescimento da parcela: |w|ⁿ = e^{a n}, a ≈ 4,2·10⁻⁵
    assert abs(0.5 * math.log1p(x) - 4.2006e-5) < 1e-8
