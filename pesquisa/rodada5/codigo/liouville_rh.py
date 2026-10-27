#!/usr/bin/env python3
"""Companheiro numérico da rodada 99: a função de Liouville (ATK/ZeroClasses/LiouvilleRH.lean).

Só biblioteca padrão. **Nada aqui é certificado.** O que se confere:

* `LSeries_lam_mul_zeta` em `s = 2` e `s = 3`: `Σ_{n ≤ n₀} λ(n)n^{−s}` contra `ζ(2s)/ζ(s)` (`π²/15` em `s = 2`; em
  `s = 3`, `ζ(6)/ζ(3)`);
* a conjectura de Pólya no intervalo: `L(N) ≤ 0` para `2 ≤ N ≤ n₀` (o primeiro contraexemplo é `906 150 257`,
  Tanaka 1980) — o teorema `rh_of_polya` diz que, se valesse sempre, valeria RH;
* o viés: a média de `L(N)/√N` fica perto de `1/ζ(½) ≈ −0,6848` — a contribuição `√x/ζ(½)` do polo de
  `ζ(2s)/ζ(s)` em `s = ½`, o mesmo polo de `liouville_nao_O`;
* `max |L(N)|/√N` (sob RH, `L(x) = O(x^{½+ε})`).
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ZETA_MEIO = -1.4603545088095868  # ζ(1/2)
ZETA3 = 1.2020569031595942


def liouville(n):
    spf = list(range(n + 1))
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for q in range(p * p, n + 1, p):
                if spf[q] == q:
                    spf[q] = p
    lam = [0] * (n + 1)
    if n >= 1:
        lam[1] = 1
    for k in range(2, n + 1):
        lam[k] = -lam[k // spf[k]]
    return lam


def main(saida=None, n=1_000_000):
    lam = liouville(n)
    s2 = sum(lam[k] / k ** 2 for k in range(1, n + 1))
    s3 = sum(lam[k] / k ** 3 for k in range(1, n + 1))
    L = 0
    max_L = -10 ** 9
    max_abs = 0.0
    soma_media, cont = 0.0, 0
    for k in range(1, n + 1):
        L += lam[k]
        if k >= 2:
            max_L = max(max_L, L)
        r = L / math.sqrt(k)
        max_abs = max(max_abs, abs(r))
        if k >= n // 10:
            soma_media += r
            cont += 1
    out = {"n": n,
           "serie_s2": s2, "zeta4_sobre_zeta2": math.pi ** 2 / 15,
           "serie_s3": s3, "zeta6_sobre_zeta3": (math.pi ** 6 / 945) / ZETA3,
           "max_L_N_de_2_a_n": max_L, "L_n": L,
           "media_L_sobre_raiz_no_ultimo_decimo": soma_media / cont, "inv_zeta_meio": 1 / ZETA_MEIO,
           "max_abs_L_sobre_raiz": max_abs,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/LiouvilleRH.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "liouville_rh.json")
    with open(saida, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    return out


if __name__ == "__main__":
    for k, v in main().items():
        print(k, v)
