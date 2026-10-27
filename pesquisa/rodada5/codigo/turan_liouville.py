#!/usr/bin/env python3
"""Companheiro numérico da rodada 100: a conjectura de Turán implica RH (ATK/ZeroClasses/TuranLiouville.lean).

Só biblioteca padrão. **Nada aqui é certificado.** (Não confundir com `turan.py`, da rodada 15, sobre as
desigualdades de Turán dos coeficientes de Ξ.) O teorema `rh_of_turan` diz: se `T(N) = Σ_{n ≤ N} λ(n)/n ≥ 0` para
todo `N`, vale RH. Aqui se confere, até `n₀`:

* `T(N) > 0` em todo `1 ≤ N ≤ n₀` (o menor contraexemplo é `72 185 376 951 205`, Borwein–Ferguson–Mossinghoff 2008);
* `T(N) → 0` (a série `Σ λ(n)/n` converge para `0`, pelo PNT), e o tamanho de `√N·T(N)`;
* a identidade `Σ λ(n)n^{−1−s} = ζ(2s + 2)/ζ(s + 1)` em `s = 1` (`π²/15`, a de `GA_T_eq`).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import liouville_rh as lv  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None, n=1_000_000):
    lam = lv.liouville(n)
    T = 0.0
    min_T, arg_min = float("inf"), None
    min_r, max_r = float("inf"), -float("inf")
    for k in range(1, n + 1):
        T += lam[k] / k
        if T < min_T:
            min_T, arg_min = T, k
        if k >= 100:
            r = math.sqrt(k) * T
            min_r, max_r = min(min_r, r), max(max_r, r)
    s1 = sum(lam[k] / k ** 2 for k in range(1, n + 1))
    out = {"n": n, "T_n": T, "min_T": min_T, "N_do_min": arg_min,
           "min_raiz_N_T_a_partir_de_100": min_r, "max_raiz_N_T_a_partir_de_100": max_r,
           "serie_s1": s1, "pi2_sobre_15": math.pi ** 2 / 15,
           "aviso": "numérico; nada aqui é certificado — o teorema está em ATK/ZeroClasses/TuranLiouville.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "turan_liouville.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    for k, v in main().items():
        print(k, v)
