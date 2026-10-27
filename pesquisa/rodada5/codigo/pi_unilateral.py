#!/usr/bin/env python3
"""Companheiro numérico da rodada 97: `Θ` por cotas de um lado de `θ(x) − x` e `π(x) − Li(x)`
(ATK/ZeroClasses/PiUnilateral.lean).

Só biblioteca padrão. **Nada aqui é certificado.** Os teoremas dizem que **um lado só** decide RH: por exemplo,
RH ⟺ `π(x) ≤ Li(x) + O(x^{½+ε})`. Numericamente o lado de cima parece "de graça" — em `8 ≤ x ≤ n` vale
`π(x) < Li(x)` e `θ(x) < x` —, e mesmo assim ele equivale a RH: por Littlewood (rodada 96) os dois lados são
violados em escala `√x log log log x/log x`, só que muito além de `n`. Aqui se registram, em inteiros `2 ≤ N ≤ n`:

* os extremos de `(θ(N) − N)/√N` e de `(π(N) − Li(N))/(√N/log N)` (os dois lados);
* o último `N` com `θ(N) ≥ N` e com `π(N) ≥ Li(N)`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import littlewood_pi_incond as lpi  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None, n=1_000_000):
    _, primo = lpi.tabela_lambda(n)
    th = Li = 0.0
    pi = 0
    ext = {"theta_max": -1e9, "theta_min": 1e9, "pi_max": -1e9, "pi_min": 1e9}
    arg = {}
    ult_th = ult_pi = None
    for N in range(2, n + 1):
        if primo[N]:
            pi += 1
            th += math.log(N)
        if N > 2:
            Li += lpi.li_passo(N - 1)
        r = math.sqrt(N)
        t = (th - N) / r
        p = (pi - Li) / (r / math.log(N))
        if th >= N:
            ult_th = N
        if pi >= Li:
            ult_pi = N
        for k, v, cmp in (("theta_max", t, max), ("theta_min", t, min), ("pi_max", p, max), ("pi_min", p, min)):
            if N >= 100 and cmp(v, ext[k]) == v and v != ext[k]:
                ext[k], arg[k] = v, N
    out = {"n": n, "extremos_a_partir_de_100": {k: {"valor": ext[k], "N": arg[k]} for k in ext},
           "ultimo_N_com_theta_maior_ou_igual_N": ult_th, "ultimo_N_com_pi_maior_ou_igual_Li": ult_pi,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/PiUnilateral.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "pi_unilateral.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for k, v in o["extremos_a_partir_de_100"].items():
        print(k, v)
    print("último N com θ(N) ≥ N:", o["ultimo_N_com_theta_maior_ou_igual_N"])
    print("último N com π(N) ≥ Li(N):", o["ultimo_N_com_pi_maior_ou_igual_Li"])
