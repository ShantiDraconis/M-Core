#!/usr/bin/env python3
"""Companheiro numérico da rodada 30: `N(T) = O(T log T)` pela fórmula de Jensen (ATK/ZeroClasses/Jensen.lean).

Só biblioteca padrão. **Nada aqui é certificado**: são conferências em ponto flutuante das cotas que o kernel prova.

* ξ(½) = 0,49712… (o denominador de Jensen; `xi_metade_ne_zero`);
* `cota_zeta`: ‖(s − 1)ζ(s)‖ ≤ 1 + ‖s − 1‖(½ + 3‖s‖) amostrada em ½ ≤ σ ≤ 3, |t| ≤ 60;
* `Gamma_le`: max Γ em [¼, n + 1] ≤ 4 + n! para 1 ≤ n ≤ 12;
* `cota_xi`: max |ξ| na circunferência ‖s − ½‖ = R contra Bx(R, n), R = 2T + 2, n = ⌈T⌉ + 1;
* `N_cota` e `N_O_TlogT`: a cota log(Bx/ξ(½))/log 2 e C·T·log T contra o termo principal de Riemann–von Mangoldt
  e os valores tabelados N(100) = 29, N(1000) = 649 — a cota vale e é grosseira (fator ~ 2π/log 2 ≈ 9 no termo T log T).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import encontro as en  # noqa: E402
import zeroclasses as zc  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
TABELA = {100: 29, 1000: 649}  # contagem clássica de zeros 0 < γ ≤ T (Odlyzko)


def Bx(R, n):
    return (R + 1) / 2 * (4 + math.factorial(n)) * (1 + (R + 1) * (0.5 + 3 * (R + 1)))


def log_Bx(R, n):
    return (math.log((R + 1) / 2) + math.log(4 + math.factorial(n))
            + math.log(1 + (R + 1) * (0.5 + 3 * (R + 1))))


def rvm(T):
    x = T / (2 * math.pi)
    return x * math.log(x) - x + 7 / 8


def cota_zeta():
    pior = 0.0
    n = 0
    for i in range(11):
        sig = 0.5 + 0.25 * i
        for j in range(-60, 61):
            s = complex(sig, j + 0.37)
            esq = abs((s - 1) * zc.zeta(s))
            dir_ = 1 + abs(s - 1) * (0.5 + 3 * abs(s))
            pior = max(pior, esq / dir_)
            n += 1
    return {"pontos": n, "max_razao": pior}


def gamma_le():
    out = {}
    for n in range(1, 13):
        xs = [0.25 + k * (n + 0.75) / 4000 for k in range(4001)]
        m = max(math.gamma(x) for x in xs)
        out[n] = {"max_Gamma": m, "cota": 4 + math.factorial(n), "ok": m <= 4 + math.factorial(n)}
    return out


def cota_xi(T, K=720):
    R, n = 2 * T + 2, math.ceil(T) + 1
    m = 0.0
    for k in range(K):
        s = 0.5 + R * complex(math.cos(2 * math.pi * k / K), math.sin(2 * math.pi * k / K))
        if abs(s - 1) < 1e-9:
            continue
        m = max(m, abs(en.xi(s)))
    return {"T": T, "R": R, "n": n, "max_xi_circ": m, "Bx": Bx(R, n), "ok": m <= Bx(R, n)}


def main(saida=None):
    a = abs(en.xi(0.5))
    A = abs(math.log(a))
    l2 = math.log(2)
    C = ((13 + A / l2) / 2 + 4) / l2
    linhas = []
    for T in (2, 5, 10, 14.134725, 50, 100, 1000, 10 ** 4, 10 ** 5):
        n = math.ceil(T) + 1
        cota = (log_Bx(2 * T + 2, n) - math.log(a)) / l2
        lin = {"T": T, "cota_jensen": cota, "C_T_logT": C * T * math.log(T), "rvm": rvm(T)}
        if T in TABELA:
            lin["N_tabelado"] = TABELA[T]
        lin["ok"] = cota <= lin["C_T_logT"] + 1e-9 and cota >= max(lin["rvm"], lin.get("N_tabelado", 0))
        lin["razao_cota_sobre_TlogT"] = cota / (T * math.log(T))
        linhas.append(lin)
    res = {
        "xi_meio": a,
        "A=|log xi(1/2)|": A,
        "C": C,
        "constante_rvm_TlogT": 1 / (2 * math.pi),
        "constante_assintotica_cota": 1 / l2,
        "contagem": linhas,
        "cota_zeta": cota_zeta(),
        "Gamma_le": gamma_le(),
        "cota_xi": [cota_xi(T) for T in (2, 3, 5)],
    }
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "contagem.json")
    with open(saida, "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    return res


if __name__ == "__main__":
    print(json.dumps(main(), indent=1, ensure_ascii=False)[:3000])
