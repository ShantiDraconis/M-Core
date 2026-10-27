#!/usr/bin/env python3
"""Companheiro numérico da rodada 83: o teto da taxa para `c` arbitrário (ATK/ZeroClasses/BDTaxaPiso.lean).

Só biblioteca padrão. Lê `dados/bd_taxa.json` (rodada 75). **Nada aqui é certificado.**

* `Wσ_zero`: `∫_0^1 t^{2σ−1} dt = 1/(2σ)` por quadratura;
* `sanduiche_DN` sob RH: a faixa `[2σ − 1, (2σ + 3)(2σ − 1)]` em `σ = 0,6; 0,75; 0,9`, e o fator
  `(2σ + 3)/(2Θ)` entre teto e piso;
* as inclinações locais `1,53–1,76` da rodada 75 em `σ = 0,75` caem dentro da faixa `[0,5; 2,25]`, como deveriam se
  RH vale. Isso não mede `κ` (barreira B2);
* `rh_of_taxaDN`: o limiar `(2σ₀ + 3)(2σ₀ − 1)` de uma taxa que, num único `σ₀`, implicaria RH.
"""
import json
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def quad(f, a, b, n=200000):
    h = (b - a) / n
    return h * sum(f(a + (j + 0.5) * h) for j in range(n))


def main(saida=None):
    w0 = [{"sigma": s, "quad": quad(lambda t: t ** (2 * s - 1), 0, 1), "formula": 1 / (2 * s)}
          for s in (0.6, 0.75, 0.9)]
    faixa = []
    for s in (0.6, 0.75, 0.9):
        faixa.append({"sigma": s, "piso_RH": 2 * s - 1, "teto_RH": (2 * s + 3) * (2 * s - 1),
                      "fator": (2 * s + 3) / (2 * 0.5), "limiar_rh_of_taxaDN": (2 * s + 3) * (2 * s - 1)})
    with open(os.path.join(AQUI, "..", "dados", "bd_taxa.json"), encoding="utf-8") as fh:
        taxa = json.load(fh)
    out = {"Wsigma_zero": w0, "faixa_RH": faixa, "inclinacoes_r75": taxa["expoentes_locais"],
           "sigma_r75": taxa["sigma"],
           "aviso": "numérico; nada aqui é certificado — os teoremas estão em ATK/ZeroClasses/BDTaxaPiso.lean"}
    if saida is None:
        saida = os.path.join(AQUI, "..", "dados", "bd_taxa_piso.json")
    with open(saida, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    return out


if __name__ == "__main__":
    print(main())
