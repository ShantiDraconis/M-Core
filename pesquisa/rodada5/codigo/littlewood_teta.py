#!/usr/bin/env python3
"""Companheiro numérico da rodada 93: Littlewood para `θ` e as trocas de sinal
(ATK/ZeroClasses/LittlewoodTeta.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `psi_sub_theta_le_mul_sqrt` (Mathlib): `ψ(x) − θ(x) ≤ C√x` com `C = 3(log 4 + 4)`; aqui o máximo de
  `(ψ(x) − θ(x))/√x` em `x ≤ 2·10⁶`;
* `psi_troca_sinal`: `ψ(x) − x` troca de sinal muitas vezes já em `x ≤ 2·10⁶`;
* `theta_troca_sinal`: o teorema garante infinitas trocas para `θ(x) − x`, mas numericamente `θ(x) < x` em todo
  `2 ≤ x ≤ 2·10⁶` (Büthe 2018: vale para `x < 10¹⁹`): a primeira troca está muito além do alcance numérico.
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
    lam = [0.0] * (n + 1)
    th = [0.0] * (n + 1)
    for p in range(2, n + 1):
        if crivo[p]:
            lp = math.log(p)
            th[p] = lp
            pk = p
            while pk <= n:
                lam[pk] = lp
                pk *= p
    psi, theta = [0.0] * (n + 1), [0.0] * (n + 1)
    a = b = 0.0
    for k in range(n + 1):
        a += lam[k]
        b += th[k]
        psi[k], theta[k] = a, b
    return psi, theta


def main(saida=None, n=2_000_000):
    psi, theta = tabelas(n)
    C = 3 * (math.log(4) + 4)
    razao = max((psi[k] - theta[k]) / math.sqrt(k) for k in range(2, n + 1))
    # trocas de sinal de ψ(x) − x: nos inteiros k, ψ(k) − x muda dentro de [k, k+1); basta olhar
    # ψ(k) − k (valor à esquerda) e ψ(k) − (k + 1) (valor à direita do intervalo)
    trocas_psi = 0
    sinal = None
    for k in range(2, n):
        for v in (psi[k] - k, psi[k] - (k + 1)):
            s = v > 0
            if v != 0 and s != sinal:
                if sinal is not None:
                    trocas_psi += 1
                sinal = s
    theta_menor = all(theta[k] < k for k in range(2, n + 1))
    min_theta = min((theta[k] - k) / math.sqrt(k) for k in range(2, n + 1))
    max_theta = max((theta[k] - k) / math.sqrt(k) for k in range(2, n + 1))
    out = {"n": n, "C_mathlib": C, "max_psi_menos_theta_sobre_raiz": razao,
           "trocas_psi": trocas_psi, "theta_menor_que_x": theta_menor,
           "min_theta_sobre_raiz": min_theta, "max_theta_sobre_raiz": max_theta,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodTeta.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_teta.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    print(main())
