#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Fronteira (rodada 27): a fronteira entre estados antes do colapso.

Aritmética exata (frações) para tudo, exceto os valores de ζ (ponto flutuante, `zeroclasses.zeta`):

* Q(x) = ⌊x + ½⌋, P(x) = {k : |x − k| ≤ ½}: em 4001 racionais de [−5, 5], P = argmin, |P| ≤ 2,
  |P| = 2 exatamente nas fronteiras k + ½, Q ∈ P;
* erro do colapso numa soma, Q(x + y) − Q x − Q y ∈ {−1, 0, 1} em 160 801 pares, com a distribuição;
* adjacência ⟺ |a − b| = 1; fecho de equivalência em {−6..6} é uma única classe;
* Δ_ab(x) = (b − a)(2x − a − b) e Δ_ab = 0 ⟺ x = (a + b)/2 em 2000 triplas aleatórias;
* intervalos: soma de Minkowski por amostragem, larguras, I − I, estados(I) por força bruta vs fórmula;
* |ζ| em 9/20 + 10i, 11/20 + 10i (não nulos) e a reflexão β + iγ ↦ (1 − β) + iγ no primeiro zero.
"""
import json
import math
import os
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

MEIO = Fr(1, 2)


def Q(x):
    return math.floor(x + MEIO)


def P(x):
    k0 = math.floor(x)
    return {k for k in range(k0 - 2, k0 + 3) if abs(x - k) <= MEIO}


def argmin(x):
    k0 = math.floor(x)
    cand = range(k0 - 3, k0 + 4)
    d = min(abs(x - k) for k in cand)
    return {k for k in cand if abs(x - k) == d}


def Dif(a, b, x):
    return (x - a) ** 2 - (x - b) ** 2


def adj(a, b):
    if a == b:
        return False
    x = Fr(a + b, 2)
    return a in P(x) and b in P(x)


def classes(adjr, U):
    pai = {u: u for u in U}

    def acha(u):
        while pai[u] != u:
            u = pai[u]
        return u
    for a in U:
        for b in U:
            if adjr(a, b):
                pai[acha(a)] = acha(b)
    return len({acha(u) for u in U})


def soma(I, J):
    return (I[0] + J[0], I[1] + J[1])


def neg(I):
    return (-I[1], -I[0])


def estados_bruto(I, passos=600):
    lo, hi = I
    out = set()
    for i in range(passos + 1):
        out |= P(lo + (hi - lo) * Fr(i, passos))
    return out


def estados_formula(I):
    lo, hi = I
    return {k for k in range(math.floor(lo) - 2, math.ceil(hi) + 3) if lo <= k + MEIO and k - MEIO <= hi}


def main(saida=None):
    res = {}
    grade = [Fr(i, 400) for i in range(-2000, 2001)]
    ok = {"pontos": 0, "P_eq_argmin": 0, "card_le_2": 0, "dois_iff_fronteira": 0, "Q_em_P": 0}
    for x in grade:
        p = P(x)
        ok["pontos"] += 1
        ok["P_eq_argmin"] += p == argmin(x)
        ok["card_le_2"] += len(p) <= 2
        ok["dois_iff_fronteira"] += (len(p) == 2) == ((x - MEIO).denominator == 1)
        ok["Q_em_P"] += Q(x) in p
    res["produtor"] = ok
    res["P(1/2)"], res["P(3/2)"] = sorted(P(MEIO)), sorted(P(Fr(3, 2)))
    res["Q(1/2)"], res["Q(3/2)"] = Q(MEIO), Q(Fr(3, 2))
    grade2 = [Fr(i, 40) for i in range(-200, 201)]
    dist = {-1: 0, 0: 0, 1: 0}
    for x in grade2:
        for y in grade2:
            dist[Q(x + y) - Q(x) - Q(y)] += 1
    res["erro_colapso_soma"] = {str(k): v for k, v in dist.items()}
    res["Q(1/2+1/2)-2Q(1/2)"], res["Q(2/5+2/5)-2Q(2/5)"] = Q(Fr(1)) - 2 * Q(MEIO), Q(Fr(4, 5)) - 2 * Q(Fr(2, 5))
    U = range(-6, 7)
    res["adjacencia"] = {"adj_iff_dist1": all(adj(a, b) == (abs(a - b) == 1) for a in U for b in U),
                         "0~1": adj(0, 1), "1~2": adj(1, 2), "0~2": adj(0, 2),
                         "classes_do_fecho_em_-6..6": classes(adj, list(U))}
    random.seed(27)
    okd = {"triplas": 0, "fatora": 0, "zero_iff_meio": 0, "reflexao": 0}
    for _ in range(2000):
        a, b = Fr(random.randint(-50, 50), random.randint(1, 9)), Fr(random.randint(-50, 50), random.randint(1, 9))
        if a == b:
            continue
        x = Fr(random.randint(-500, 500), random.randint(1, 20))
        okd["triplas"] += 1
        okd["fatora"] += Dif(a, b, x) == (b - a) * (2 * x - a - b)
        okd["zero_iff_meio"] += (Dif(a, b, x) == 0) == (x == (a + b) / 2) and Dif(a, b, (a + b) / 2) == 0
        okd["reflexao"] += Dif(a, b, a + b - x) == -Dif(a, b, x)
    res["competicao"] = okd
    res["Delta01(1/2)"], res["Delta12(3/2)"] = str(Dif(0, 1, MEIO)), str(Dif(1, 2, Fr(3, 2)))
    oki = {"pares": 0, "minkowski": 0, "larguras": 0, "I-I_simetrico": 0, "estados": 0}
    for _ in range(300):
        a, c = Fr(random.randint(-40, 40), 8), Fr(random.randint(-40, 40), 8)
        I, J = (a, a + Fr(random.randint(0, 24), 8)), (c, c + Fr(random.randint(0, 24), 8))
        S = soma(I, J)
        oki["pares"] += 1
        amostra = [Fr(i, 50) for i in range(51)]
        mk = all(S[0] <= I[0] + (I[1] - I[0]) * s + J[0] + (J[1] - J[0]) * t <= S[1]
                 for s in amostra[::10] for t in amostra[::10])
        z = S[0] + (S[1] - S[0]) * Fr(random.randint(0, 100), 100)
        x = max(I[0], z - J[1])
        mk &= I[0] <= x <= I[1] and J[0] <= z - x <= J[1]
        oki["minkowski"] += mk
        oki["larguras"] += (S[1] - S[0]) == (I[1] - I[0]) + (J[1] - J[0])
        D = soma(I, neg(I))
        oki["I-I_simetrico"] += D == (-(I[1] - I[0]), I[1] - I[0]) and (D == (0, 0)) == (I[0] == I[1])
        oki["estados"] += estados_bruto(I) == estados_formula(I)
    res["intervalos"] = oki
    res["estados[2/5,3/5]"] = sorted(estados_formula((Fr(2, 5), Fr(3, 5))))
    res["estados[0,1]"] = sorted(estados_formula((Fr(0), Fr(1))))
    res["estados[0,3/2]"] = sorted(estados_formula((Fr(0), Fr(3, 2))))
    z1, z2 = zc.zeta(complex(0.45, 10)), zc.zeta(complex(0.55, 10))
    rho = zc.zero_newton(complex(0.5, 14.13))
    res["zeta"] = {"|ζ(9/20+10i)|": abs(z1), "|ζ(11/20+10i)|": abs(z2),
                   "rho1": [rho.real, rho.imag], "|ζ(1-β+iγ)|": abs(zc.zeta(complex(1 - rho.real, rho.imag))),
                   "d(rho1)": abs(rho.real - 0.5)}
    res["aviso"] = "aritmética exata exceto ζ; o kernel prova as leis (Fronteira.lean)"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
