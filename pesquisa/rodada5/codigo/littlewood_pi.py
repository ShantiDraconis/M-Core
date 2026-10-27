#!/usr/bin/env python3
"""Companheiro numérico da rodada 95: Littlewood para `π(x) − Li(x)` sob RH
(ATK/ZeroClasses/LittlewoodPi.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `Li_eq`: `Li(x) = ∫₂ˣ dt/log t = x/log x − 2/log 2 + ∫₂ˣ dt/log² t` por quadratura;
* `pi_sub_Li`: `π(x) − Li(x) = (θ(x) − x)/log x + 2/log 2 + E(x)`, `E(x) = ∫₂ˣ (θ(t) − t) dt/(t log² t)`;
* o tamanho de `2/log 2 + E(x)` contra `√x/log x` (o teorema precisa que seja `o(√x log log log x/log x)`);
* `π(x) < Li(x)` para `x` entre o último ponto pequeno com `π ≥ Li` e `10⁶` (Büthe 2018: `π(x) < li(x)` até `10¹⁹`),
  embora o teorema garanta infinitas trocas de sinal sob RH.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def tabelas(n):
    crivo = bytearray([1]) * (n + 1)
    crivo[0] = crivo[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if crivo[p]:
            crivo[p * p::p] = bytearray(len(range(p * p, n + 1, p)))
    pi = [0] * (n + 1)
    th = [0.0] * (n + 1)
    a, b = 0, 0.0
    for k in range(n + 1):
        if crivo[k]:
            a += 1
            b += math.log(k)
        pi[k], th[k] = a, b
    return pi, th


def integral(f, a, b, m):
    h = (b - a) / m
    return sum(f(a + (i + 0.5) * h) for i in range(m)) * h


def main(saida=None, n=1_000_000):
    pi, th = tabelas(n)
    li = []
    for x in (10.0, 100.0, 1000.0):
        m = 20000
        L1 = integral(lambda t: 1 / math.log(t), 2, x, m)
        L2 = x / math.log(x) - 2 / math.log(2) + integral(lambda t: 1 / math.log(t) ** 2, 2, x, m)
        li.append({"x": x, "Li": L1, "por_partes": L2})
    ident = []
    for x in [v for v in (1000.0, 10000.0, 100000.0, 1000000.0) if v <= n]:
        # integrais exatas por trechos em [k, k+1): θ constante
        Lx = 0.0
        E = 0.0
        k = 2
        while k < x:
            k1 = min(k + 1, x)
            m = 8
            h = (k1 - k) / m
            for i in range(m):
                t = k + (i + 0.5) * h
                Lx += h / math.log(t)
                E += h * (th[k] - t) / (t * math.log(t) ** 2)
            k += 1
        lhs = pi[int(x)] - Lx
        rhs = (th[int(x)] - x) / math.log(x) + 2 / math.log(2) + E
        R = 2 / math.log(2) + E
        ident.append({"x": x, "pi_menos_Li": lhs, "formula": rhs, "resto": R,
                      "resto_sobre_raiz_log": R / (math.sqrt(x) / math.log(x))})
    # π − Li é decrescente em cada [k, k+1) (π constante, Li crescente): basta olhar os inteiros k
    Lacc = 0.0
    ultimos = []
    for k in range(2, n):
        if pi[k] >= Lacc:
            ultimos.append(k)
        Lacc += sum(1 / math.log(k + (i + 0.5) / 16) for i in range(16)) / 16
    ultimo_pi_maior = max(ultimos) if ultimos else None
    out = {"Li_por_partes": li, "pi_menos_Li": ident, "ultimo_k_com_pi_maior_ou_igual_Li": ultimo_pi_maior,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodPi.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_pi.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for r in o["Li_por_partes"]:
        print(r)
    for r in o["pi_menos_Li"]:
        print(r)
    print("ultimo k com pi(k) >= Li(k):", o["ultimo_k_com_pi_maior_ou_igual_Li"])
