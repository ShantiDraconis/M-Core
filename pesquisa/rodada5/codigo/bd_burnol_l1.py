#!/usr/bin/env python3
"""Companheiro numérico da rodada 80: Burnol restrito (ATK/ZeroClasses/BDBurnolL1.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `J_reta`: `∫_ε^1 dt/t = −log ε` por quadratura;
* `piso_reta` e `burnol_L1` com `ρ₁ = ½ + 14,1347i`, `σ = ½`, `A = 1`: as constantes explícitas da prova
  (`C = C₀σ`, `B = σ − log m₀`) e o piso `C/(log N + log 2 + B)` para `N = 10², 10⁴, 10⁶, 10¹²`;
* comparação com a constante de Burnol `Σ_ρ m_ρ²/|ρ|² = 2 + γ − log 4π ≈ 0,0462` (zeros simples; citada, não
  formalizada para `c` arbitrário): o piso restrito tem a mesma forma `1/log N`, com constante ≈ 2000 vezes menor.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
GAMMA1 = 14.134725141734693
EULER = 0.5772156649015329


def constantes(sigma=0.5, gamma=GAMMA1):
    r = 1 / (2 * math.hypot(sigma, gamma))
    m0 = min(1.0, r * sigma)
    c0 = min(3 * r * r / 8, (3 * r * (1 - sigma) / 8) ** 2 / (2 - 2 * sigma))
    return {"r": r, "m0": m0, "C0": c0, "C": c0 * sigma, "B": sigma - math.log(m0)}


def quad(f, a, b, n=200000):
    h = (b - a) / n
    return h * sum(f(a + (j + 0.5) * h) for j in range(n))


def main(saida=None):
    jr = [{"eps": e, "quad": quad(lambda t: 1 / t, e, 1), "formula": -math.log(e)} for e in (0.5, 0.1, 0.01)]
    k = constantes()
    burnol = 2 + EULER - math.log(4 * math.pi)
    pisos = []
    for N in (10 ** 2, 10 ** 4, 10 ** 6, 10 ** 12):
        den = math.log(N) + math.log(2) + k["B"]
        pisos.append({"N": N, "piso": k["C"] / den, "piso_vezes_log": k["C"] / den * math.log(N),
                      "burnol_assintotico": burnol / math.log(N)})
    out = {"J_reta": jr, "constantes": k, "constante_burnol": burnol, "razao": burnol / k["C"], "pisos": pisos,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDBurnolL1.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_burnol_l1.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
