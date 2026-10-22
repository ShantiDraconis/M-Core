# RH — 1/2 como incógnita: o zero β + iγ com as duas partes livres (22/10/2026)

**Resultado.** Com β e γ livres e o centro κ no lugar de 1/2, o sistema Re ζ(β+iγ) = 0, Im ζ(β+iγ) = 0 tem
três respostas de níveis diferentes:

* **o centro κ sai exatamente 1/2**, provado sem RH;
* **a concentração em torno de 1/2 é assintótica**: provada incondicionalmente na forma de cota; a média
  tende a zero se B10 valer;
* **que cada zero esteja exatamente no centro** é RH, que segue aberta.

Até a altura 300, todas as 138 soluções achadas sem fixar 1/2 têm β = 1/2 a 7·10⁻¹³ (ponto flutuante).

Kernel: `atk-kernel/ATK/ZeroIncognito.lean` (14 teoremas, axiomas padrão). Código: `codigo/zero_incognito.py`.
Dados: `dados/zero_incognito.json` (γ ≤ 100), `dados/ate300/` (γ ≤ 300). Figura: `dados/zero_incognito.png`.

## No kernel

| Teorema | Enunciado | Condição |
| --- | --- | --- |
| `sistema_iff` | ζ(β+iγ) = 0 ⟺ Re ζ = 0 e Im ζ = 0 | — |
| `sistema` | solução não trivial ⇒ 0 < β < 1, γ ≠ 0, e (1−β, γ), (β, −γ), (1−β, −γ) também são soluções | incondicional |
| `soma_desvio` | Σ_{0<γ≤T} (β − κ) = (1/2 − κ)·N(T) para todo κ | incondicional |
| `incognita_resolvida` | Σ (β − κ) = 0 ⟺ κ = 1/2 (havendo zeros até T) | incondicional |
| `centro_exato` | média de β sobre os zeros com 0 < γ ≤ T = 1/2 | incondicional |
| `dispersao_le` | Σ (β − 1/2)² ≤ δ²·N(T) + C_δ·T para todo δ > 0 | incondicional (Bohr–Landau) |
| `dispersao_media_tende_zero` | Σ (β − 1/2)² / N(T) → 0 | B10 (N(T)/T → ∞) |
| `rh_iff_dispersao` | RH ⟺ Σ (β − 1/2)² = 0 para todo T | equivalência; RH aberta |

Igualar o resto a zero, Σ (β − κ) = 0, **resolve** a incógnita κ. O motivo é a simetria ρ ↦ 1 − ρ̄: ela leva
cada β em 1 − β na mesma altura, e por isso os desvios se cancelam em pares, estejam os zeros na reta ou não.

## Numérico: as duas equações resolvidas sem fixar 1/2

Região β ∈ [−1, 2], 1 ≤ γ ≤ 300. Três contagens independentes:

| Método | γ ≤ 100 | γ ≤ 300 | Usa 1/2? |
| --- | --- | --- | --- |
| Princípio do argumento na borda dos retângulos | 29 | 138 | não |
| Newton complexo a partir de 2574 / 7774 sementes espalhadas | 29 soluções | 138 soluções | não |
| Trocas de sinal de Z(t) na reta (Riemann–Siegel θ) | 29 | 138 | sim (controle) |
| max \|β − 1/2\| entre as soluções | 2,2·10⁻¹⁴ | 7,1·10⁻¹³ | — |

* A contagem pelo argumento é exatamente igual às trocas de sinal na reta. Portanto nenhum zero da região
  ficou fora de 1/2 (até a precisão do ponto flutuante).
* Os 138 batem com Riemann–von Mangoldt: (T/2π)log(T/2π) − T/2π + 7/8 ≈ 137,7 em T = 300, a menos de S(T).

## Como ζ se comporta fora de 1/2

Na altura de cada zero, |ζ(1/2 + ε + iγₙ)| ≈ |ε|·|ζ′(ρₙ)| (razão 0,99 a 1,00 para ε = 0,01):

| γₙ | \|ζ′(ρₙ)\| | ε = 0,01 | ε = 0,25 |
| --- | --- | --- | --- |
| 14,134725 | 0,7932 | 0,00790 | 0,1795 |
| 21,022040 | 1,1368 | 0,01130 | 0,2454 |
| 25,010858 | 1,3717 | 0,01362 | 0,2900 |
| 30,424876 | 1,3039 | 0,01294 | 0,2700 |
| 32,935062 | 1,3821 | 0,01371 | 0,2835 |

O perfil m(β) = min_{10≤γ≤300} |ζ(β+iγ)| é um V com vértice exatamente em β = 1/2. Alguns valores: 0,0826 em
β = 0,4; 0 em 0,5; 0,0762 em 0,6; 0,4886 em 0; 0,3260 em 1. O mínimo é dominado pelo primeiro zero, onde |ζ′| é
menor.

Cada zero é simples e transversal: as curvas Re ζ = 0 e Im ζ = 0 se cruzam, não se tocam. Por isso um zero não
pode "escorregar" um pouco para fora de 1/2 sem que ζ mude de forma global. E se um zero saísse da reta, a
simetria obrigaria um par (1/2 + ε, 1/2 − ε) na mesma altura (`ATK.EixoDeslocado`, `ATK.ForaDaLinha`).

## Limites

* Números de ponto flutuante, sem certificação intervalar. Verificações rigorosas e muito maiores já existem:
  todos os zeros até 3·10¹² estão na reta (Platt–Trudgian 2021).
* Nada aqui prova RH. O que é novo no kernel é a forma "κ incógnito ⇒ κ = 1/2" para o centro, e a separação
  entre centro (provado), concentração (provada em cota; média sob B10) e máximo (RH).
