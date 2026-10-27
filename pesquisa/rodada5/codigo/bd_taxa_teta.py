#!/usr/bin/env python3
"""Companheiro numérico da rodada 85: `Θ` como o início das taxas de potência (ATK/ZeroClasses/BDTaxaTeta.lean).

Só biblioteca padrão. **Nada aqui é certificado.**

* `comTaxa_iff` num modelo: para `Θ ∈ {0,5; 0,6; 0,875}` hipotéticos, a faixa garantida
  `[2(σ − Θ), (2σ + 3)(σ − Θ)/Θ]` (rodadas 76 e 83) numa grade de `σ ∈ (0, 1)`; o ínfimo da grade onde o piso é
  positivo recupera `Θ` (`Teta_eq_sInf`), a menos do passo da grade;
* `rh_iff_comTaxa_perto`: sob `Θ = ½`, há `σ` com taxa garantida em `(½, ½ + ε)` para `ε = 0,1; 0,01; 0,001`.
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def main(saida=None):
    passo = 1e-3
    grade = [k * passo for k in range(1, 1000)]
    modelos = []
    for teta in (0.5, 0.6, 0.875):
        com_taxa = [s for s in grade if 2 * (s - teta) > 0]
        faixa = {f"{s:.2f}": [2 * (s - teta), (2 * s + 3) * (s - teta) / teta] for s in (0.9, 0.95)}
        modelos.append({"Teta": teta, "inf_grade": min(com_taxa), "faixa": faixa})
    perto = []
    for eps in (0.1, 0.01, 0.001):
        s = 0.5 + eps / 2
        perto.append({"eps": eps, "sigma": s, "piso_RH": 2 * (s - 0.5)})
    out = {"passo": passo, "modelos": modelos, "perto_de_meio": perto,
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDTaxaTeta.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_taxa_teta.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
