#!/usr/bin/env python3
"""Companheiro numérico da rodada 46: o teorema de Littlewood para `Σ μ(n) n^{−w}` (ATK/ZeroClasses/LittlewoodMu.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `cota_PN`/`littlewood`: `|Σ_{n ≤ N} μ(n) n^{−w} − 1/ζ(w)|` para `N = 10, …, 10⁵` em vários `w` com `½ < Re w < 1`,
  e o quociente pela taxa `(N + ½)^{−ε/4}` da prova (`ε = Re w − ½`), que deve ficar limitado;
* `entradaLittlewood`: o erro espectral `|1 − ζ(s) P_N(s + ε)|²/|s|²` em `s = ½ + iτ` contra a dominação
  `(1 + |τ|)^{−5/4}` (só a forma: a constante da prova não é calculada).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def mobius_ate(M):
    mu = [1] * (M + 1)
    mu[0] = 0
    primo = [True] * (M + 1)
    for p in range(2, M + 1):
        if primo[p]:
            for k in range(p, M + 1, p):
                if k > p:
                    primo[k] = False
                mu[k] = -mu[k]
            pp = p * p
            for k in range(pp, M + 1, pp):
                mu[k] = 0
    return mu


def main(saida=None):
    M = 100000
    mu = mobius_ate(M)
    Ns = [10, 100, 1000, 10000, 100000]
    ws = [complex(0.8, 5.0), complex(0.7, 14.0), complex(0.6, 3.0)]
    tabela = {}
    for w in ws:
        alvo = 1 / zc.zeta(w)
        eps = w.real - 0.5
        soma = 0j
        linhas = []
        k = 0
        for n in range(1, M + 1):
            if mu[n]:
                soma += mu[n] * n ** (-w)
            if k < len(Ns) and n == Ns[k]:
                erro = abs(soma - alvo)
                linhas.append({"N": n, "erro": erro, "erro_sobre_taxa": erro / (n + 0.5) ** (-eps / 4)})
                k += 1
        tabela[str(w)] = linhas
    espectral = []
    eps = 0.2
    N = 2000
    for tau in (0.0, 5.0, 20.0, 50.0):
        s = complex(0.5, tau)
        P = sum(mu[n] * n ** (-(s + eps)) for n in range(1, N + 1) if mu[n])
        e = abs(1 - zc.zeta(s) * P) ** 2 / abs(s) ** 2
        espectral.append({"tau": tau, "erro": e, "erro_vezes_peso": e * (1 + tau) ** 1.25})
    res = {"littlewood": tabela, "espectral_eps_0_2_N_2000": espectral}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_mu.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
