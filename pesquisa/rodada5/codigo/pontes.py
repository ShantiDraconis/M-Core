#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Pontes (rodada 24): as pontes B1–B23 em fórmulas pequenas.

Só biblioteca padrão. Conta tudo por enumeração (2ⁿ atribuições) — é exatamente o custo exponencial que as
pontes **não** removem.

* N = #SAT; ord₀ ∏(t + R²) (coeficientes inteiros exatos); det diag(R); posto + N = 2ⁿ;
* F(z) = Σ z^R: F(0) = N, 0 ≤ F(z) − N ≤ 2ⁿz; com z = 2^{−(n+2)}, arredondar recupera N (T2);
* Q_φ(x) = R(x)² + Σ(xᵢ(1−xᵢ))²: zero nos pontos booleanos satisfatórios, positivo nos demais;
* B1: R = 0 ⟺ B | R para B > m.
"""
import itertools
import json
import os
import random
import sys
from fractions import Fraction as Fr


def viol(x, C):
    return 0 if any(x[i] == p for (i, p) in C) else 1


def R(phi, x):
    return sum(viol(x, C) for C in phi)


def Rreal(phi, x):
    tot = 0
    for C in phi:
        q = 1
        for (i, p) in C:
            lit = x[i] if p else 1 - x[i]
            q *= 1 - lit
        tot += q
    return tot


def Q(phi, x):
    return Rreal(phi, x) ** 2 + sum((xi * (1 - xi)) ** 2 for xi in x)


def poly_prod(rs):
    """Coeficientes (grau crescente) de ∏ (t + r²)."""
    c = [1]
    for r in rs:
        a = r * r
        nc = [0] * (len(c) + 1)
        for k, v in enumerate(c):
            nc[k] += a * v
            nc[k + 1] += v
        c = nc
    return c


def ordem_zero(c):
    k = 0
    while c[k] == 0:
        k += 1
    return k


def analisa(phi, n):
    xs = list(itertools.product((False, True), repeat=n))
    rs = [R(phi, x) for x in xs]
    N = sum(1 for r in rs if r == 0)
    coef = poly_prod(rs)
    det = 1
    for r in rs:
        det *= r
    posto = sum(1 for r in rs if r != 0)
    z = Fr(1, 2 ** (n + 2))
    F = sum(z ** r for r in rs)
    v = F + Fr(1, 5)  # qualquer v a menos de 1/4 de F
    m = len(phi)
    return {"N": N, "ord0": ordem_zero(coef), "det": det, "posto+N": posto + N, "2^n": 2 ** n,
            "F(0)": sum(1 for r in rs if r == 0), "F(z)-N": float(F - N), "cota 2^n z": float(2 ** n * z),
            "arredonda": round(float(v)) == N or abs(float(v) - N) < 0.5,
            "B1": all((r == 0) == ((r % (m + 1)) == 0) for r in rs),
            "Q_bool_zero_iff_sat": all((Q(phi, [1 if b else 0 for b in x]) == 0) == (R(phi, x) == 0) for x in xs)}


def main(saida=None):
    res = {}
    ex1 = [[(0, True), (1, True)], [(0, False), (1, True)], [(0, True), (1, False)]]
    ex2 = [[(0, True)], [(0, False)]]
    res["exemplo_um"] = analisa(ex1, 2)
    res["exemplo_um_Z"] = poly_prod([R(ex1, x) for x in itertools.product((False, True), repeat=2)])
    res["exemplo_zero"] = analisa(ex2, 1)
    res["exemplo_zero_Z"] = poly_prod([R(ex2, x) for x in itertools.product((False, True), repeat=1)])
    random.seed(24)
    ok = {"formulas": 0, "ord0==N": 0, "det0_iff_sat": 0, "posto": 0, "T2": 0, "B1": 0, "Q": 0}
    for _ in range(300):
        n = random.randint(1, 7)
        m = random.randint(1, 25)
        phi = [[(random.randrange(n), random.random() < 0.5) for _ in range(random.randint(1, 3))] for _ in range(m)]
        a = analisa(phi, n)
        ok["formulas"] += 1
        ok["ord0==N"] += a["ord0"] == a["N"]
        ok["det0_iff_sat"] += (a["det"] == 0) == (a["N"] > 0)
        ok["posto"] += a["posto+N"] == a["2^n"]
        ok["T2"] += 0 <= a["F(z)-N"] <= a["cota 2^n z"] <= 0.25 and a["arredonda"]
        ok["B1"] += a["B1"]
        ok["Q"] += a["Q_bool_zero_iff_sat"]
    res["aleatorias"] = ok
    res["Q_real_em_ponto_nao_booleano"] = Q(ex1, [0.5, 0.5])
    res["aviso"] = "enumeração 2ⁿ: as pontes mudam a linguagem, não o custo; o kernel prova as identidades (Pontes.lean)"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
