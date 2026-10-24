# ATK/Discovery — truncamento, cauda, infinitesimal, melhoria ortogonal e `E₁ = 1 − log 2` (24/10/2026)

Formalização no kernel (Lean 4.34.1 + Mathlib d13f23b) das propostas sobre truncamento e cauda e das
reduções do defeito. São 6 módulos e 68 teoremas, sem `sorry` e sem axiomas além de `propext`,
`Classical.choice` e `Quot.sound`.

| Módulo | O que está provado |
|---|---|
| `Discovery/Truncamento.lean` (15) | `P_N(x) = ⌊10ᴺx⌋/10ᴺ`, `T_N = x − P_N`: reconstrução exata, `0 ≤ T_N < 10⁻ᴺ`; o zero observado esconde um positivo; a projeção não é injetiva; **`a < b ⟺ P_N(a) − P_N(b) < T_N(b) − T_N(a)`**; com `P_N` iguais decide a cauda; contagens naturais têm cauda `0`; `P_N(x)` cresce e converge para `x`; observar zero não basta, e a cauda que some também não; fechamento por duas componentes |
| `Discovery/Habitante.lean` (9) | `Habitante` = valor + precisão + cabeça + cauda + **prova** da reconstrução, em qualquer grupo aditivo linearmente ordenado; o certificado `Comparacao a b` existe **se e só se** `a < b`; nenhum habitante se compara consigo; **o par P01 (`combustível = 1`, `tamanho = 1`) não tem certificado em precisão nenhuma**; objeto estruturado `(R, I, F, T)` com valor `(R+F+T) + Ii`: a observação não é injetiva, observação `0` com valor `≠ 0`; a equivalência observacional não implica igualdade de valor |
| `Discovery/Infinitesimal.lean` (14) | `ε_H = 10⁻ᴴ` nos hiper-reais: `0 < ε_H < 10⁻ⁿ` para todo `n` e `< r` para todo real `r > 0`; `1 − ε_H < 1 < 1 + ε_H`, os três com parte padrão `1`; `0 < ε_H < 2ε_H`, todos com parte padrão `0`; **a cauda não decide a parte padrão** (`ε_H` e `1/4 + ε_H`); em `ℝ` não existe esse dígito; a desigualdade estrita de cada etapa não passa ao limite |
| `Discovery/Contracao.lean` (6) | `D_{n+1} ≤ (1 − αₙ)D_n` com `Σαₙ = ∞` ⟹ `D_n → 0` (via `D_N ≤ D_0 e^{−Σα}`); **a cota condicional `D_N ≤ 5/(2(N+1))`** a partir de `D₂ = 5/6` e do ganho `g_n ≥ D_n/(n+2)`; mesmo valor inicial `5/6` e mesma monotonia com limites `0` e `1/2`; `D_N → 0 ⟺ ∀m ∃N, D_N < 10⁻ᵐ` |
| `Discovery/Hilbert.lean` (9) | `‖r − ce‖² = ‖r‖² − 2c⟨r,e⟩ + c²`, mínimo em `c = ⟨r,e⟩`; `D(K) = inf ‖v − q‖²` decresce com `K`; **identidade exata `D(K ⊕ ℝe) = D(K) − ⟨r, e⟩²`**; **contraexemplo em `ℝ³`**: ganho `0` com `D = 1`, então `⟨r,e⟩² ≥ D/3` falha — a contração não é automática |
| `Discovery/RhoMeio.lean` (15) | Nyman–Beurling em `L²(0,1)`, `ρ_{1/2}(x) = {1/(2x)} − ½{1/x}`: degraus `((n+1) mod 2)/2`, `ρ² = ρ/2`; **`∫₀¹ρ_{1/2} = (log 2)/2`, `∫₀¹ρ_{1/2}² = (log 2)/4`**; **`E(c) = 1 − c log 2 + c²(log 2)/4`**, mínimo **só** em `c = 2`, **`inf_c E(c) = 1 − log 2 > 0`** |

## O que mudou no acervo

* `E₁ = 1 − log 2` era só um intervalo numérico (`ATK.TerceiroTemplo.E1_intervalo`). Agora o valor
  sai do cálculo exato das integrais de Nyman–Beurling (`ATK.Discovery.RhoMeio.iInf_erro`).
* A hipótese de ganho `|⟨r_n, e_{n+1}⟩|² ≥ D_n/(n+2)` foi testada: a geometria sozinha não a dá
  (`ATK.Discovery.Hilbert.contraexemplo_correlacao`). Se ela valesse, daria `D_N ≤ 5/(2(N+1))`
  (`ATK.Discovery.Contracao.cota_cinco_meios`).
* O lema P01 refutado (`decodeCircuitCore_size_lt`) continua refutado: contagens naturais não têm
  cauda (`ATK.Discovery.Truncamento.natural_sem_cauda`, `ATK.Discovery.Cauda.p01_sem_certificado`).

## O que continua aberto

* `D_∞ = 0` para o defeito genuíno, que é RH (`ATK.DInfinito`, `ATK.ATKIBagchi`).
* Uma correlação quantitativa ou uma família explícita de aproximantes com erro tendendo a zero.
* Os outros seis problemas.

`UNIVERSAL_GREEN = false`, `CLOSED_MATH = false`, `OPEN_MATH = true`, `TERMINAL_CERTIFIED 0/7`.
