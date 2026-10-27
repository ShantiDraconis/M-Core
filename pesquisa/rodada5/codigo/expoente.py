#!/usr/bin/env python3
"""Companheiro numérico da rodada 35: o expoente de convergência dos zeros é 1 (ATK/ZeroClasses/Expoente.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `nao_somavel_ZM`: `Σ_{|γ| ≤ T} 1/|ρ|` cresce como `(log(T/2π))²/(2π)` (diverge), enquanto `Σ 1/|ρ|^{1,2}` se
  estabiliza;
* `xi_lb_par`: `ξ(2n + 2)` contra a cota `(2 − π²/6)·n!/π^{n+1}` e contra `e^{a + K(2n+2)}` (que ele ultrapassa);
* `N_tende_infinito`: `N(T)` em `T = 50, 100, …, 300`.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None):
    g = ca.zeros()
    somas = {}
    for T in (50, 100, 150, 200, 250, 300):
        zs = [x for x in g if x <= T]
        s1 = sum(2 / math.sqrt(0.25 + x * x) for x in zs)
        s12 = sum(2 / (0.25 + x * x) ** 0.6 for x in zs)
        somas[str(T)] = {"N": len(zs), "soma_1": s1, "soma_1.2": s12,
                         "previsto_soma_1": math.log(T / (2 * math.pi)) ** 2 / (2 * math.pi)}
    xi_par = {}
    b = 2 - math.pi ** 2 / 6
    for n in (1, 3, 5, 10, 20, 40):
        s = 2 * n + 2
        val = abs(en.xi(complex(s, 0)))
        cota = b * math.factorial(n) / math.pi ** (n + 1)
        xi_par[str(n)] = {"xi": val, "cota": cota, "ok": val >= cota,
                          "log_xi_sobre_s": math.log(val) / s}
    res = {"somas": somas, "xi_par": xi_par}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "expoente.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
