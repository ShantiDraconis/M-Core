#!/usr/bin/env python3
"""Companheiro numérico da rodada 33: o teorema de Hadamard para ξ (ATK/ZeroClasses/Hadamard.lean).

Só biblioteca padrão. **Nada aqui é certificado**: o kernel prova que existem `A, B` com `ξ = e^{A+Bs}·P`; aqui
se conferem os valores clássicos e a identidade com 138 zeros.

* `A = log ξ(0) = −log 2` e `B = ξ′(0)/ξ(0)` (diferença finita) contra `−γ/2 − 1 + ½ log 4π = −0,0230957…`;
* `B = −Σ_ρ Re(1/ρ)` (pares conjugados), soma até 300 mais a cauda;
* a identidade `ξ(s) = e^{A+Bs}·P_{300}(s)·cauda(s)`, `cauda(s) ≈ exp(−s²/2 · Σ_{|γ|>300} 1/ρ²)`, em pontos dentro e
  fora da faixa crítica, com zeros refinados pela secante em `Ξ(t) = ξ(½ + it)`;
* o passo central da prova (Poisson + Borel–Carathéodory + Cauchy): `log⁺|ξ/P|` em `|s| = R` fica bem abaixo de `R²`
  (da ordem de `R log R`), e `g = log(ξ/P)` tem `g″ ≈ 0`.
"""
import cmath
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canonico as ca  # noqa: E402
import encontro as en  # noqa: E402
import inteira as it  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
T = 300.0


def main(saida=None):
    g = [it.refina(t) for t in ca.zeros()]
    h = 1e-4
    # ξ(0) = ½ (polo de Γ vezes o zero de s); derivada em 0 por diferença central na direção imaginária
    xi0 = abs(en.xi(complex(0, 1e-7)))
    B_fd = ((en.xi(complex(0, h)) - en.xi(complex(0, -h))) / (2j * h) / 0.5).real
    A = math.log(xi0)
    B_soma = -sum(2 * (0.5 / (0.25 + x * x)) for x in g)
    cauda_B = -(math.log(T / (2 * math.pi)) + 1) / (2 * math.pi * T)
    sig2 = -(math.log(T / (2 * math.pi)) + 1) / (math.pi * T)
    pontos = {}
    for nome, s in (("2", 2 + 0j), ("1/2+2i", complex(0.5, 2)), ("3+5i", complex(3, 5)),
                    ("-1+3i", complex(-1, 3)), ("1/2+10i", complex(0.5, 10))):
        aprox = cmath.exp(A + ca.BC * s) * it.P(s, g) * cmath.exp(-s * s / 2 * sig2)
        ex = en.xi(s)
        pontos[nome] = {"xi": [ex.real, ex.imag], "eAB_P_cauda": [aprox.real, aprox.imag],
                        "erro_rel": abs(aprox - ex) / abs(ex)}
    # g = log(ξ/P_300) e a segunda derivada numérica em alguns pontos
    def gfun(s):
        return cmath.log(en.xi(s) / (it.P(s, g) * cmath.exp(-s * s / 2 * sig2)))

    g2 = {}
    for nome, s in (("0.3", 0.3 + 0j), ("2+1i", complex(2, 1)), ("-1+2i", complex(-1, 2))):
        d = 1e-3
        val = (gfun(s + d) - 2 * gfun(s) + gfun(s - d)) / d ** 2
        g2[nome] = abs(val)
    # log⁺|ξ/P| em círculos
    circ = {}
    for R in (5, 10, 20):
        m = max(math.log(max(1.0, abs(en.xi(R * cmath.exp(2j * math.pi * k / 64)) /
                                      it.P(R * cmath.exp(2j * math.pi * k / 64), g))))
                for k in range(64))
        circ[str(R)] = {"max_posLog_xi_sobre_P": m, "R_logR": R * math.log(R), "R2": R * R}
    res = {
        "A": A, "A_esperado": -math.log(2),
        "B_diferenca_finita": B_fd, "B_formula": ca.BC,
        "B_soma_300_mais_cauda": B_soma + cauda_B,
        "identidade": pontos,
        "g_segunda_derivada": g2,
        "circulos": circ,
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "hadamard_xi.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1] if len(sys.argv) > 1 else None), indent=1, ensure_ascii=False))
