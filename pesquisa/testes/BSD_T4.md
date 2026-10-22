# BSD T4(a): fator 2 em `ATK.BSDRefinada.formula_E32_iff` (y² = x³ − x)

**Hipótese testada.** No ramo `ccr-46709b88-u9mbgb`, `FormulaRefinada E32 ↔ Ш finito ∧ L(E,1) = periodo·tamagawa·#Ш/16`.
Com #Ш = 1, isso é numericamente verdadeiro, erra por um fator, ou depende de convenção?

**Normalizações lidas no código Lean (não supostas).**
- `periodo` = ∫_{g>0} 2/√g dx no modelo minimal global, com g = 4x³+b₂x²+2b₄x+b₆; para E32, g = 4x³ − 4x (`gR_E32`).
  O conjunto {g>0} = (−1,0) ∪ (1,∞) cobre **as duas componentes reais**, então `periodo` = ∫_{E(ℝ)}|ω|, já com c_∞ = 2.
  Trocar de modelo minimal (u = ±1) não muda o valor.
- `tamagawa` = ∏ᶠ sobre os primos finitos de [E(ℚ_p):E⁰(ℚ_p)], sem fator em ∞.
- `ordemTorsao_E32 = 4` e `regulador_E32 = 1` são teoremas do kernel.
- L é `WeierstrassCurve.LSeries` da Mathlib: Euler local 1 − a_pT + pT² nos primos bons, 1 nos aditivos, centro em s = 1.

**Método e controles (todos passaram).**
1. a_p calculado de dois jeitos independentes (soma de Legendre e #E(F_p) por força bruta, p < 400). Hasse vale e a_p = 0 para p ≡ 3 (4).
2. O condutor e o sinal saem da equação funcional:
   - L(1) = Σ aₙ/n [e^{−2πnA/√N} + ε e^{−2πn/(A√N)}] tem de ser o mesmo para A ∈ {1; 0,7; 1,3; 2};
   - só N = 32, ε = +1 passa (dispersão 5·10⁻⁴¹); N = 16, 64 e ε = −1 falham (dispersão ≥ 0,07).
3. Ω por quadratura mpmath (40 dígitos, substituições que removem as singularidades), conferido por AGM e por ϖ = Γ(1/4)²/(2√(2π)).
4. c₂ pelo algoritmo de Tate:
   - Δ = 64, v₂ = 6 < 12, logo minimal; ponto singular (1,0) mod 2; após x → x+1, 2 | b₂ e 4 | a₆; v₂(b₈) = 2 < 3, logo **tipo III, c₂ = 2**, f₂ = 5;
   - Ogg com f = 5 vindo do teste 2 dá m = 2;
   - (±1,0) reduzem ao ponto singular, então c₂ ≥ 2.

**Resultados.**

| grandeza | valor |
|---|---|
| L(E,1) (FE, 600 termos) = ϖ/4 | 0,65551438857302995261620989747277985 |
| ∫_{−1}^{0} 2/√g = ∫_{1}^{∞} 2/√g = ω₁ = ϖ | 2,62205755429211981046483958989 |
| Ω_ATK = `periodo E32` = 2ϖ | 5,24411510858423962092967917978 |
| L(E,1)/Ω_ATK | 0,125 = 1/8 = c₂/16 |
| #Ш_an = 16·L/(Ω_ATK·c₂) | 1,000… (35 dígitos) |

| convenção (Ω, c) | #Ш_an implicado |
|---|---|
| kernel: Ω = ∫_{E(ℝ)}\|ω\| = 2ϖ, c₂ = 2 | **1** |
| Ω = ω₁ = 2,622057 (o "real period" do controle da tarefa), c₂ = 2 | 2: impossível, #Ш é quadrado |
| Ω_ATK sem c₂ | 2: impossível |
| Ω = ω₁ com c₂·c_∞ = 4 | 1 |

**Interpretação.**
- **O enunciado do kernel, como está, é numericamente verdadeiro.** Com as definições do kernel ele equivale a
  "Ш finito e #Ш = 1", e L = Ω_ATK·2/16 confere em 35 dígitos (L/Ω_ATK = 1/8, exatamente racional).
- **Não há fator 2 errado** em `FormulaRefinada` nem em `formula_E32_iff`: c_∞ = 2 já está dentro de `periodo`.
- O fator 2 só aparece se Ω for o menor período real ω₁ ≈ 2,622057, exatamente o valor dado no controle da tarefa;
  com ele a fórmula daria 0,3278 = L/2. Esse "2,622057" é ω₁ (Ω sem c_∞), não o Ω de BSD.
- O controle da tarefa tem ainda um erro de dígitos: L(E,1) = 0,65551438857…, não 0,6555143795…. A forma fechada ϖ/4 e a FE confirmam.
- Não consegui abrir a LMFDB (https://www.lmfdb.org/EllipticCurve/Q/32/a/3, bloqueada). Até onde sei, ela usa Ω = ∫_{E(ℝ)}|ω| = 5,2441…; **não verificado.**
- #Ш(E32) = 1 é teorema (CM de posto 0: Rubin; BSD completo para N < 5000 e r_an ≤ 1, Creutz–Miller). O teste não prova isso:
  mostra que o lado numérico é coerente com #Ш = 1.

**Mostra × sugere.** *Mostra* que as normalizações de Ω, c_p, L e torção no kernel são coerentes entre si e com BSD para E32.
*Sugere*, sem provar, que `FormulaRefinada` está bem calibrada em geral; faltam Δ < 0 (11a1), c_p > 1 multiplicativo (14a1) e posto 1 (37a1).
**Limites.** c₂ vem de Tate e Ogg: assumi que o índice do kernel é o c_v usual, e ninguém calculou `tamagawa E32` no Lean.
Também não conferi `MinimalGlobal E32`; se ele falhasse, `periodo` valeria 0.
**Próximos passos.** (i) Repetir em 11a1, 14a1 e 37a1 (`coefLider` com r = 1, Ω de uma componente).
(ii) Provar no Lean `periodo E32 = 2ϖ` (integrais Beta) e `tamagawa E32 = 2`. (iii) T4(b,c) (E₆, E₃₄, Tunnell n = 34) não foram rodados.

Código: `tests/code/BSD_T4.py`; saída: `tests/work/BSD_T4.out`; tempo < 2 s.
