#!/usr/bin/env python3
"""Companheiro numérico da rodada 98: `Θ` como expoente exato (ATK/ZeroClasses/TetaExpoente.lean).

Só biblioteca padrão. **Nada aqui é certificado.** O teorema diz que, para cada uma das funções
`E = ±(ψ(N) − N)`, `±(θ(N) − N)`, `±(π(N) − Li(N))`, `±M(N)` e seus valores absolutos,
`Θ = inf{θ : E(N) ≤ N^θ para N grande}`. Numericamente só se vê o expoente local: em cada década
`[10^k, 10^{k+1})` contida em `[2, n]`, `e_k = max log E(N)/log N` sobre os `N` com `E(N) > 1`. Sob RH todos tenderiam a `½`
(devagar, por causa dos fatores `log`). O lado de cima de `θ − N` e de `π − Li` fica vazio até `10⁶`: não há `N` com
`θ(N) > N` nem com `π(N) > Li(N)` (a partir de `8`). Mesmo assim o expoente desses lados é `Θ ≥ ½`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import littlewood_pi_incond as lpi  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
NOMES = ["psi_cima", "psi_baixo", "theta_cima", "theta_baixo", "pi_cima", "pi_baixo", "M_cima", "M_baixo"]


def moebius(n):
    mu = [1] * (n + 1)
    mu[0] = 0
    primo = bytearray([1]) * (n + 1)
    for p in range(2, n + 1):
        if primo[p]:
            for q in range(2 * p, n + 1, p):
                primo[q] = 0
            for q in range(p, n + 1, p):
                mu[q] = -mu[q]
            pp = p * p
            for q in range(pp, n + 1, pp):
                mu[q] = 0
    return mu


def main(saida=None, n=1_000_000):
    L, primo = lpi.tabela_lambda(n)
    mu = moebius(n)
    psi = th = Li = 0.0
    pi = 0
    M = 1  # M(1) = μ(1)
    decadas = {}
    positivos = {k: 0 for k in NOMES}
    for N in range(2, n + 1):
        psi += L[N]
        M += mu[N]
        if primo[N]:
            pi += 1
            th += math.log(N)
        if N > 2:
            Li += lpi.li_passo(N - 1)
        vals = {"psi_cima": psi - N, "psi_baixo": N - psi, "theta_cima": th - N, "theta_baixo": N - th,
                "pi_cima": pi - Li, "pi_baixo": Li - pi, "M_cima": M, "M_baixo": -M}
        k = int(math.log10(N) + 1e-12)
        d = decadas.setdefault(k, {nome: None for nome in NOMES})
        lN = math.log(N)
        for nome, v in vals.items():
            if v > 0 and N >= 8:
                positivos[nome] += 1
            if v > 1:
                e = math.log(v) / lN
                if d[nome] is None or e > d[nome]:
                    d[nome] = e
    completas = {k: v for k, v in decadas.items() if 10 ** (k + 1) - 1 <= n}
    out = {"n": n, "expoente_local_por_decada": {str(k): v for k, v in sorted(completas.items())},
           "quantos_N_com_E_positivo_a_partir_de_8": positivos,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/TetaExpoente.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "teta_expoente.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for k, v in o["expoente_local_por_decada"].items():
        print(k, {a: (round(b, 3) if b is not None else None) for a, b in v.items()})
    print(o["quantos_N_com_E_positivo_a_partir_de_8"])
