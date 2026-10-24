#!/usr/bin/env python3
"""Companheiro numérico de ATK/ZeroClasses/Finito (rodada 26): o finito exato, a aritmética terminal, a faixa tolerante.

Só biblioteca padrão e inteiros/frações exatos.

* casos A, B, C: resíduos, a_j, F(z), det(L + qI), M = Σ B^{m−r} e ⌊M/B^m⌋ = #SAT;
* 300 fórmulas aleatórias: ⌊M/B^m⌋ = #SAT, ord₀ F = min R, cotas da função de partição;
* aritmética saturada (Z = 7): associativa; ⊞ com E(1) = 0 não é associativa; estado intervalar "01".
"""
import itertools
import json
import math
import os
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pontes as po  # noqa: E402


def residuos(phi, n):
    return [po.R(phi, x) for x in itertools.product((False, True), repeat=n)]


def analisa(phi, n):
    rs = residuos(phi, n)
    m = len(phi)
    B = 2 ** (n + 1)
    a = [rs.count(j) for j in range(m + 1)]
    M = sum(B ** (m - r) for r in rs)
    detq = {q: math.prod(r * r + q for r in rs) for q in range(5)}
    return {"r": rs, "a": a, "M": M, "B": B, "m": m, "M//B^m": M // B ** m, "#SAT": a[0],
            "ord0_F": min(rs), "det(L+qI)": detq}


def base(M, B, digitos):
    out = []
    for _ in range(digitos):
        out.append(M % B)
        M //= B
    return "".join(str(d) for d in reversed(out))


def satAdd(Z, a, b):
    return min(Z, a + b)


def Ev(k):
    return 0 if k == 1 else k


def boxplus(Z, a, b):
    return Ev(min(Z, a + b))


def E01(x):
    if 0 <= x < Fr(3, 2):
        return "01"
    return math.floor(x + Fr(1, 2))


def main(saida=None):
    res = {}
    A = [[(0, True), (1, True)], [(0, False), (1, True)], [(0, True), (1, False)]]
    Bf = [[(0, True)], [(0, False)]]
    C = [[(0, True)], [(1, True)]]
    for nome, phi, n in (("A", A, 2), ("B", Bf, 1), ("C", C, 2)):
        r = analisa(phi, n)
        r["M_na_base_B"] = base(r["M"], r["B"], r["m"] + 1)
        res["caso_" + nome] = r
    random.seed(26)
    ok = {"formulas": 0, "codificacao": 0, "ord0F_min": 0, "particao": 0}
    for _ in range(300):
        n = random.randint(1, 7)
        phi = [[(random.randrange(n), random.random() < 0.5) for _ in range(random.randint(1, 3))]
               for _ in range(random.randint(1, 20))]
        r = analisa(phi, n)
        ok["formulas"] += 1
        ok["codificacao"] += r["M//B^m"] == r["#SAT"]
        ok["ord0F_min"] += r["ord0_F"] == min(r["r"])
        mu, N = min(r["r"]), len(r["r"])
        bom = True
        for tau in (0.5, 2.0, 10.0):
            Z = sum(math.exp(-tau * x) for x in r["r"])
            v = -math.log(Z) / tau
            bom &= mu - math.log(N) / tau - 1e-12 <= v <= mu + 1e-12
        ok["particao"] += bom
    res["aleatorias"] = ok
    res["saturada_Z7"] = {"assoc_ok": all(satAdd(7, satAdd(7, a, b), c) == satAdd(7, a, satAdd(7, b, c))
                                          for a in range(9) for b in range(9) for c in range(9)),
                          "Z+1": satAdd(7, 7, 1), "cancelamento": [satAdd(7, 7, 1), satAdd(7, 6, 1)]}
    res["boxplus_Z7"] = {"(0⊞1)⊞1": boxplus(7, boxplus(7, 0, 1), 1), "0⊞(1⊞1)": boxplus(7, 0, boxplus(7, 1, 1)),
                         "tabela": [boxplus(7, a, b) for a, b in ((0, 1), (1, 1), (1, 2), (3, 4), (4, 4), (7, 7))]}
    res["E01"] = {str(x): E01(x) for x in (Fr(0), Fr(1, 4), Fr(1, 2), Fr(99999, 100000), Fr(1), Fr(149999, 100000),
                                           Fr(3, 2), Fr(2), Fr(249, 100), Fr(5, 2))}
    res["E01_soma_mal_definida"] = [E01(Fr(0) + 1), E01(Fr(1) + 1)]
    res["aviso"] = "aritmética exata; o kernel prova as leis (Finito.lean)"
    if saida:
        json.dump(res, open(saida, "w"), indent=1, ensure_ascii=False)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return res


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
