#!/usr/bin/env python3
"""Companheiro numérico da rodada 41: `S(T) = O(log T)` (ATK/ZeroClasses/VariacaoArg.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `variacao_log`: `V(T) = Im ∫_{1/2}^{2} ζ′/ζ(σ + iT) dσ = arg ζ(2 + iT) − arg ζ(½ + iT)` (ramo contínuo) para
  `T` entre 20 e 300, contra `log T`;
* `variacao`: `|V(T)| ≤ (k + 1)π`, com `k` o número de trocas de sinal de `Re ζ(σ + iT)` em `[½, 2]`;
* `conta_zeros_re`: `k` contra a cota de Jensen `log((6T + 38)/(2 − π²/6))/log(7/6)`;
* `cota_zeta_quarto`: `|ζ(s)| ≤ ½ + 1/|s − 1| + 6|s|` numa grade de `Re s ≥ ¼`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def V(T, n=1500):
    tot = 0.0
    prev = zc.zeta(complex(2, T))
    for k in range(1, n + 1):
        s = complex(2 - 1.5 * k / n, T)
        cur = zc.zeta(s)
        tot += cmath.phase(cur / prev)
        prev = cur
    return -tot  # ∫_{1/2}^{2} = −(variação de 2 até 1/2)


def trocas(T, n=1500):
    vals = [zc.zeta(complex(0.5 + 1.5 * k / n, T)).real for k in range(n + 1)]
    return sum(1 for a, b in zip(vals, vals[1:]) if a * b < 0)


def main(saida=None):
    pi2 = 2 - math.pi ** 2 / 6
    linhas = {}
    pior = 0.0
    for T in (20.5, 37.3, 60.1, 100.7, 150.2, 200.9, 250.4, 299.7):
        v = V(T)
        k = trocas(T)
        jensen = math.log((6 * T + 38) / pi2) / math.log(7 / 6)
        linhas[str(T)] = {"V": v, "k": k, "cota_variacao": (k + 1) * math.pi, "jensen": jensen,
                          "V_sobre_logT": v / math.log(T)}
        pior = max(pior, abs(v) / math.log(T))
    quarto = 0.0
    for sg in (0.25, 0.5, 1.0, 2.0, 3.5):
        for t in (1.0, 5.0, 20.0, 100.0):
            s = complex(sg, t)
            quarto = max(quarto, abs(zc.zeta(s)) / (0.5 + 1 / abs(s - 1) + 6 * abs(s)))
    res = {"alturas": linhas, "max_V_sobre_logT": pior, "zeta_quarto_razao_max": quarto}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "variacao_arg.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
