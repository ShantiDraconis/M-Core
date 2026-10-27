#!/usr/bin/env python3
"""Companheiro numérico da rodada 96: Littlewood para `π(x) − Li(x)` sem hipóteses
(ATK/ZeroClasses/LittlewoodPiIncond.lean).

Só biblioteca padrão. **Nada aqui é certificado.** O que se confere, em inteiros `N ≤ n`:

* `Pi_sub_pi`: `0 ≤ Π(N) − π(N) ≤ (ψ(N) − θ(N))/log 2`, com `Π(N) = Σ_{k ≤ N} Λ(k)/log k`;
* `lam_sub_Li`: `1/log N ≤ λ(N) − Li(N) ≤ 1/log 2`, com `λ(N) = Σ_{2 ≤ k ≤ N} 1/log k`, `Li(N) = ∫₂ᴺ dt/log t`;
* `aPi_eq`: `a(N) = Σ_{k ≤ N} (Λ(k) − 1)/log k = (π − Li) + (Π − π) − (λ − Li)`;
* o viés: `π(N) − Li(N)` fica negativo (de `N = 8` até `n`), enquanto `a(N) = Π(N) − λ(N)` troca de sinal muitas
  vezes — a diferença `Π − π = ½π(√N) + ⅓π(∛N) + …` é exatamente o viés, e é `O(√N)`, pequena demais
  para a escala `x^θ`, `θ > ½`, do caso `¬RH`.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def tabela_lambda(n):
    """`Λ(k)` para `0 ≤ k ≤ n` e o indicador de primo."""
    crivo = bytearray([1]) * (n + 1)
    crivo[0] = crivo[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if crivo[p]:
            crivo[p * p::p] = bytearray(len(range(p * p, n + 1, p)))
    lam = [0.0] * (n + 1)
    for p in range(2, n + 1):
        if crivo[p]:
            lp = math.log(p)
            q = p
            while q <= n:
                lam[q] = lp
                q *= p
    return lam, crivo


def li_passo(k):
    """`∫ₖᵏ⁺¹ dt/log t` por Simpson com 4 subintervalos."""
    h = 0.25
    f = [1 / math.log(k + i * h) for i in range(5)]
    return h / 3 * (f[0] + 4 * f[1] + 2 * f[2] + 4 * f[3] + f[4])


def main(saida=None, n=1_000_000):
    L, primo = tabela_lambda(n)
    marcos = [v for v in (100, 1000, 10_000, 100_000, 1_000_000) if v <= n]
    psi = th = Pi = lam_s = a = Li = 0.0
    pi = 0
    linhas = []
    sinal_a = sinal_d = None
    trocas_a = trocas_d = 0
    ultimo_d_nao_neg = None
    for k in range(2, n + 1):
        lk = math.log(k)
        psi += L[k]
        Pi += L[k] / lk
        lam_s += 1 / lk
        a += (L[k] - 1) / lk
        if primo[k]:
            pi += 1
            th += lk
        if k > 2:
            Li += li_passo(k - 1)
        d = pi - Li
        if d >= 0:
            ultimo_d_nao_neg = k
        s_a, s_d = a > 0, d > 0
        if sinal_a is not None and s_a != sinal_a:
            trocas_a += 1
        if sinal_d is not None and k > 8 and s_d != sinal_d:
            trocas_d += 1
        sinal_a, sinal_d = s_a, s_d
        if k in marcos:
            r = math.sqrt(k)
            linhas.append({
                "N": k, "pi_menos_Li": d, "Pi_menos_pi": Pi - pi, "psi_menos_theta_sobre_log2": (psi - th) / math.log(2),
                "lam_menos_Li": lam_s - Li, "inv_log_N": 1 / lk, "inv_log_2": 1 / math.log(2),
                "a": a, "decomposicao": d + (Pi - pi) - (lam_s - Li),
                "Pi_menos_pi_sobre_meio_pi_raiz": (Pi - pi) / (0.5 * sum(1 for j in range(2, int(r) + 1) if primo[j])),
                "a_sobre_raiz_log": a / (r / lk), "pi_menos_Li_sobre_raiz_log": d / (r / lk)})
    out = {"marcos": linhas, "trocas_de_sinal_a": trocas_a, "trocas_de_sinal_pi_menos_Li_depois_de_8": trocas_d,
           "ultimo_N_com_pi_maior_ou_igual_Li": ultimo_d_nao_neg, "n": n,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LittlewoodPiIncond.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "littlewood_pi_incond.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    o = main()
    for r in o["marcos"]:
        print(r)
    print("trocas de sinal de a(N):", o["trocas_de_sinal_a"])
    print("trocas de sinal de π − Li depois de 8:", o["trocas_de_sinal_pi_menos_Li_depois_de_8"])
    print("último N com π(N) ≥ Li(N):", o["ultimo_N_com_pi_maior_ou_igual_Li"])
