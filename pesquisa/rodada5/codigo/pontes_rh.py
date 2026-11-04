#!/usr/bin/env python3
"""Companheiro numérico da rodada 102: as seis "pontes" para RH (ATK/ZeroClasses/PontesRH.lean).

Só biblioteca padrão (``fractions``, ``decimal``, ``math``). **Nada aqui é certificado.** Os teoremas estão em
``ATK/ZeroClasses/PontesRH.lean`` e ``ATK/ZeroClasses/PontesRHAbscissa.lean``; aqui só se auditam os números
da afirmação "RH até C₀":

* o par mais próximo da janela nova (centros com 30 dígitos, raios 285·10⁻²⁰ e 449·10⁻²⁰): o gap exato em ℚ,
  o erro do gap, e a comparação com ``9585/5777953`` (que é ``(71/10000)·ḡ``, um valor derivado, não medido);
* o gap normalizado ``s = gap / (2π / log(T/2π))``;
* ``S(T) = N(T) − θ(T)/π − 1`` em ``C₀ = 6 000 362 444 943/2`` com o ``N(C₀)`` declarado;
* a contagem esperada ``(θ(b) − θ(a))/π`` na janela declarada (23 111 813 zeros);
* a média tautológica: ``⟨½ + (gᵢ/ḡ − 1)·b⟩ = ½`` para quaisquer ``gᵢ`` (``media_tautologica``);
* a conjugação de Möbius ``M(1 − s) = J(M(s))`` em pontos racionais (``M_tensao``);
* a estatística GUE de vizinhos (núcleo seno, determinante de Fredholm por Gauss–Legendre):
  ``P(s < 0,01)`` e ``P(s > 3)``, com as contagens esperadas para ``N`` gaps.
"""
import json
import math
import os
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from math import gcd

AQUI = os.path.dirname(os.path.abspath(__file__))

G1 = F(300018051927946511944262498325, 10 ** 17)
G2 = F(300018051927946678691400506282, 10 ** 17)
R1 = F(285, 10 ** 20)
R2 = F(449, 10 ** 20)
C0 = F(6000362444943, 2)
N_C0 = 12363178644727
JANELA = (D("3000175822471.5"), D("3000181222471.5"))
N_JANELA = 23111813


def _pi():
    getcontext().prec += 10

    def arctan_inv(x):
        x = D(x)
        s, t, n, sinal, x2 = D(0), 1 / x, 1, 1, x * x
        while True:
            termo = t / n
            if termo == 0 or abs(termo) < D(10) ** (-getcontext().prec):
                break
            s += sinal * termo
            t /= x2
            n += 2
            sinal = -sinal
        return s

    p = 4 * (4 * arctan_inv(5) - arctan_inv(239))
    getcontext().prec -= 10
    return +p


def theta_rs(t, pi):
    """Fase de Riemann–Siegel (expansão assintótica, erro ≪ t⁻⁵)."""
    t = D(t)
    return t / 2 * (t / (2 * pi)).ln() - t / 2 - pi / 8 + 1 / (48 * t) + D(7) / (5760 * t ** 3)


def gauss_legendre(m):
    xs, ws = [], []
    for i in range(1, m + 1):
        x = math.cos(math.pi * (i - 0.25) / (m + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, m + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = m * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-16:
                break
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


def _det(a):
    n = len(a)
    a = [linha[:] for linha in a]
    d = 1.0
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(a[r][c]))
        if a[p][c] == 0:
            return 0.0
        if p != c:
            a[c], a[p] = a[p], a[c]
            d = -d
        d *= a[c][c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            for k in range(c, n):
                a[r][k] -= f * a[c][k]
    return d


def lacuna_vazia(s, m=40):
    """``E(0; s) = det(I − K_seno)`` em ``L²[0, s]``: probabilidade GUE de nenhum zero num intervalo de
    comprimento ``s`` (densidade 1)."""
    xs, ws = gauss_legendre(m)
    x = [s * (t + 1) / 2 for t in xs]
    w = [s * v / 2 for v in ws]

    def k(a, b):
        d = a - b
        return 1.0 if d == 0 else math.sin(math.pi * d) / (math.pi * d)

    n = len(x)
    a = [[(1.0 if i == j else 0.0) - math.sqrt(w[i]) * k(x[i], x[j]) * math.sqrt(w[j]) for j in range(n)]
         for i in range(n)]
    return _det(a)


def cauda_gue(x, h=1e-3, m=40):
    """``P(S > x) = −∂ₓ E(0; x)`` para o espaçamento ``S`` de vizinhos (densidade 1)."""
    return -(lacuna_vazia(x + h, m) - lacuna_vazia(x - h, m)) / (2 * h)


def main(saida=None, m=40):
    getcontext().prec = 60
    pi = _pi()
    gap = G2 - G1
    erro = R1 + R2
    u = F(9585, 5777953)
    t = D(G1.numerator) / D(G1.denominator)
    gap_medio = 2 * pi / (t / (2 * pi)).ln()
    s = D(gap.numerator) / D(gap.denominator) / gap_medio
    tc0 = D(C0.numerator) / D(C0.denominator)
    s_c0 = D(N_C0) - (theta_rs(tc0, pi) / pi + 1)
    esperado = (theta_rs(JANELA[1], pi) - theta_rs(JANELA[0], pi)) / pi

    # média tautológica com gaps arbitrários
    gs = [F(3, 7), F(11, 5), F(1, 9), F(5, 2), F(2, 3)]
    gbar = sum(gs) / len(gs)
    b = F(3, 5000)
    media = sum(F(1, 2) + (g / gbar - 1) * b for g in gs) / len(gs)

    # Möbius: M(1 − s) = J(M(s)) em pontos racionais
    def mob(z):
        return (z - 1) / (z + 1)

    def jj(w):
        return -(w + 1) / (1 - 3 * w)

    pontos = [F(1, 3), F(7, 4), F(-5, 2), F(71, 10000), F(1, 2)]
    tensao_ok = all(mob(1 - z) == jj(mob(z)) for z in pontos)

    p_pequeno = math.pi ** 2 / 9 * 0.01 ** 3 - 2 * math.pi ** 4 / 225 * 0.01 ** 5
    p_maior3 = cauda_gue(3.0, m=m)
    contagens = {}
    for n_gaps in (14380682, 23111812):
        lo, hi = n_gaps * p_pequeno, n_gaps * p_maior3
        contagens[str(n_gaps)] = {"esperado_s_lt_0_01": lo, "sigma_s_lt_0_01": math.sqrt(lo),
                                  "esperado_s_gt_3": hi, "sigma_s_gt_3": math.sqrt(hi)}

    out = {
        "gap_centros": [gap.numerator, gap.denominator],
        "gap_centros_float": float(gap),
        "erro_gap": [erro.numerator, erro.denominator],
        "erro_sobre_gap": float(erro / gap),
        "um_e_menos_17_sobre_gap": float(F(1, 10 ** 17) / gap),
        "u_9585_5777953": float(u),
        "mdc_9585_5777953": gcd(9585, 5777953),
        "u_igual_71e4_vezes_gbar": u == F(71, 10000) * F(1350000, 5777953),
        "gap_menos_u": float(gap - u),
        "gap_medio_local": float(gap_medio),
        "s_normalizado": float(s),
        "S_de_C0": float(s_c0),
        "zeros_esperados_janela": float(esperado),
        "zeros_declarados_janela": N_JANELA,
        "media_tautologica": [media.numerator, media.denominator],
        "re_abs": [(F(1, 2) + (F(71, 10000) - 1) * b).numerator, (F(1, 2) + (F(71, 10000) - 1) * b).denominator],
        "mobius_tensao_ok": tensao_ok,
        "M_meio": [mob(F(1, 2)).numerator, mob(F(1, 2)).denominator],
        "theta_graus_71e4": [(360 * (F(71, 10000) - 1) / (F(71, 10000) + 1)).numerator,
                             (360 * (F(71, 10000) - 1) / (F(71, 10000) + 1)).denominator],
        "gue_P_s_lt_0_01": p_pequeno,
        "gue_P_s_gt_3": p_maior3,
        "gue_normalizacao": cauda_gue(0.002, h=1e-3, m=m),
        "gue_contagens": contagens,
        "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/PontesRH.lean",
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "pontes_rh.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for k, v in o.items():
        print(k, v)
