#!/usr/bin/env python3
"""Companheiro numérico da rodada 84: sem lei de potência para `D_N` (ATK/ZeroClasses/BDSemPotencia.lean).

Só biblioteca padrão. Lê `rodada2/dados/RH_Gram_DN.tsv` (`D_N` em double-double para `N ≤ 7999`, rodada 2).
**Nada aqui é certificado.**

* `contracao_impossivel_incond` contra os dados: `max_{100 ≤ N < 4000} D_{2N}/D_N = 0,946 < 1`. Os dados finitos são
  compatíveis com uma contração `q = 0,946`, que o teorema exclui para sempre (barreira B2: `amostra_finita_nao_decide`);
* `DN_sem_potencia`: o expoente local médio `log(D_N/D_{2N})/log 2` cai de `0,38` (`[16, 32)`) para `0,12`
  (`[2048, 4096)`), não monotonicamente, como deve sem lei de potência; `D_N log N / C₀`, `C₀ = 2 + γ − log 4π`, fica
  em `[0,957; 1,010]` para `256 ≤ N < 8000`.
"""
import json
import math
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(AQUI, "..", "..", "rodada2", "dados", "RH_Gram_DN.tsv")
C0 = 2 + 0.5772156649015329 - math.log(4 * math.pi)


def ler():
    d = {}
    with open(TSV, encoding="utf-8") as fh:
        next(fh)
        for linha in fh:
            p = linha.split("\t")
            d[int(p[0])] = float(p[1])
    return d


def main(saida=None):
    d = ler()
    razoes = [d[2 * n] / d[n] for n in range(100, 4000)]
    blocos = []
    n = 16
    while 2 * n <= 4096:
        expo = [math.log(d[m] / d[2 * m]) / math.log(2) for m in range(n, 2 * n) if 2 * m in d]
        blocos.append({"bloco": [n, 2 * n], "expoente_medio": sum(expo) / len(expo)})
        n *= 2
    burnol = [d[n] * math.log(n) / C0 for n in range(256, 8000)]
    out = {"max_razao_diadica_100_4000": max(razoes), "expoentes_por_bloco": blocos,
           "DN_logN_sobre_C0": [min(burnol), max(burnol)],
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDSemPotencia.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_sem_potencia.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
