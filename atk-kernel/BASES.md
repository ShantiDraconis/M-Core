# ATK — Mapa das bases que faltam na Mathlib

Este arquivo organiza, problema por problema, a infraestrutura matemática que precisa existir em
Lean/Mathlib para que cada lacuna do M-Core possa ser atacada formalmente. Ele separa três coisas
que não devem ser confundidas:

* **Base**: um teorema ou uma definição conhecidos na literatura, ausentes da Mathlib, que podem
  ser formalizados sem resolver nenhum problema aberto.
* **Ponte**: um teorema publicado e profundo (Wiles, Báez-Duarte, Gross–Zagier, …) que hoje entra
  no kernel como hipótese explícita, nunca como `axiom`.
* **Núcleo aberto**: o enunciado que ninguém sabe provar. Nenhuma base o fecha; as bases só tornam
  possível escrevê-lo e testá-lo com fidelidade.

Regras do kernel valem para todas as bases: sem `sorry`, sem `admit`, sem `axiom` novo, auditoria
por `#print axioms` no CI, e as flags (`OPEN_MATH`, `CLOSED_MATH`, `UNIVERSAL_GREEN`) nunca são
editadas à mão. Os arquivos ficam em `ATK/Base*.lean` (a auditoria do CI só percorre `ATK/*.lean`),
escritos no estilo da Mathlib para poderem ser propostos a ela.

Legenda de estado: ✅ certificado no CI · 🟡 em andamento · ⬜ não iniciado · ⛔ fora do alcance da
Mathlib atual (exige teoria grande que ainda não existe).

---

## Navier–Stokes (enunciado A do Clay: ℝ³ ou T³, sem força)

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| N1 | Galerkin em Fourier no toro | termo convectivo truncado; `Σ N(u)_k · conj û_k = 0`; Leray; identidade de energia | ✅ | `BaseGalerkinNS` |
| N2 | Existência global dissipativa | `F` localmente Lipschitz, `⟪F v, v⟫ ≤ 0` ⇒ solução em `[0,T]` para todo `T`, com `‖u(t)‖ ≤ ‖u(0)‖`; unicidade | ✅ | `BaseEDODissipativa` |
| N2b | Instância Galerkin | o subespaço admissível (div. nula, realidade) é invariante pelo campo de Galerkin; o campo é localmente Lipschitz e dissipativo ⇒ soluções globais de Galerkin | 🟡 | — |
| N3 | Espaços de energia | `L²_σ(T³)`, `H¹`, desigualdade de Poincaré em média nula (a Mathlib tem `mFourierBasis` e `BesselPotentialSpace`) | ⬜ | — |
| N4 | Compacidade | Aubin–Lions (ou Arzelà–Ascoli + estimativa de `∂ₜu_N` em `H⁻¹`) | ⬜ | — |
| N5 | Soluções fracas de Leray | passagem ao limite `N → ∞`; desigualdade de energia | ⬜ | — |
| N6 | Regularidade 2D / dados pequenos | Ladyzhenskaya 2D; Fujita–Kato | ⬜ | — |
| — | **Núcleo aberto** | regularidade global 3D sem força | aberto | — |

Contexto 2026: a explosão com força externa (enunciados C/D) foi anunciada e está em verificação;
não afeta o enunciado A acima.

## Hipótese de Riemann

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| R1 | Função ξ e Ξ | ξ inteira; `ξ(1−s)=ξ(s)`; `ξ(s̄)=conj ξ(s)`; Ξ real e par; zeros; troca de sinal; RH ⟺ zeros de Ξ reais | ✅ | `BaseRiemannXi` |
| R1' | Família de Báez-Duarte | `D_N = 1 − bᵀG⁻¹b`; `b_k = (log k + 1 − γ)/k`; `D_N > 0` | ✅ | `GramBaezDuarte`, `BaezDuarteVetorB`, `RelacionalDN` |
| R2 | Sinal de Ξ(0) | `Ξ(0) = ξ(1/2) > 0` (de `ζ(1/2) < 0`, já no kernel) | ⬜ | — |
| R3 | Representação integral | `Ξ(t) = ∫₀^∞ Φ(u) cos(ut) du` a partir da teta de Jacobi (a Mathlib tem `jacobiTheta₂` e a equação funcional) | ⬜ | — |
| R4 | Teorema de Hardy | infinitos zeros na reta crítica | ⬜ | — |
| R5 | Certificação numérica de zeros | aritmética intervalar para ζ (Euler–Maclaurin) + troca de sinal de Ξ | ⬜ | — |
| R6 | Necessidade de Báez-Duarte | RH ⇒ `D_N → 0` (hoje com entradas isoladas em `NecessidadeBD`) | 🟡 | `NecessidadeBD` |
| — | **Núcleo aberto** | `D_∞ = 0` (O1) | aberto | — |

## P vs NP

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| P1 | Modelo genuíno | P e NP sobre `Turing.FinTM2`, SAT ∈ NP | ✅ | `LigacaoPNP`, `SATemNP` |
| P2 | Tableau de Cook–Levin | fórmula do tableau ⟺ execução aceita | ✅ | `CookLevinTableau`, `CookLevinReducao` |
| P3 | M2d | a redução é computável por `FinTM2` em tempo polinomial ⇒ SAT é NP-completo | ⬜ | — |
| P4 | Hierarquia de tempo | `P ≠ EXP` | ⬜ | — |
| P5 | Barreiras | relativização (Baker–Gill–Solovay) | ⬜ | — |
| — | **Núcleo aberto** | SAT ∉ P | aberto | — |

## Yang–Mills (grupo compacto simples, ℝ⁴)

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| Y1 | Calibre na rede | elos, ação de calibre, plaquetas, ação de Wilson invariante | ✅ | `BaseRedeCalibre` |
| Y2 | Medida de Wilson | medida produto preservada por calibre; esperanças de Wilson invariantes | ✅ | `BaseWilsonMedida` |
| Y2' | Variante abeliana | campo livre sem massa não tem gap; com massa, gap ≥ m² | ✅ | `YMSemGap` |
| Y3 | Positividade por reflexão | Osterwalder–Seiler para a ação de Wilson | ⬜ | — |
| Y4 | Gap em acoplamento forte | expansão em cluster para β pequeno | ⬜ | — |
| Y5 | Limite contínuo | axiomas de Wightman/Osterwalder–Schrader em 4D | ⛔ | — |
| — | **Núcleo aberto** | existência em 4D e gap > 0 | aberto | — |

## Birch e Swinnerton-Dyer

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| B0 | Enunciado do Clay | L-função e pontos sobre os objetos da Mathlib | ✅ | `LigacaoBSD`, `CongruentCurve` |
| B1a | 2-torsão | `P + P = 0` ⟺ `y = 0` ⟺ `x` raiz da cúbica | ✅ | `BaseCurvasTorsao` |
| B1b | Nagell–Lutz | pontos de torsão sobre ℚ têm coordenadas inteiras e `y² ∣ Δ` | ⬜ | — |
| B2 | Redução mod p | `E(ℚ)_tors ↪ E(𝔽_p)` para p de boa redução, p ≠ 2 | ⬜ | — |
| B3 | 2-descida | `E(ℚ)/2E(ℚ)` finito para curvas com 2-torsão completa | ⬜ | — |
| B4 | Mordell–Weil | alturas e descida | ⛔ | — |
| B5 | Gross–Zagier–Kolyvagin | posto analítico ≤ 1 | ⛔ | — |
| — | **Núcleo aberto** | posto ≥ 2 e finitude de Ш em geral | aberto | — |

## Hodge

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| H1 | Álgebra linear de Hodge | decomposição de Hodge para toros complexos (álgebra linear) | ⬜ | — |
| H2 | Teorema (1,1) de Lefschetz | classes de divisores | ⛔ | — |
| H3 | Teoria de Hodge em Kähler | harmônicas, decomposição `H^k = ⊕ H^{p,q}` | ⛔ | — |
| — | **Núcleo aberto** | classes de Hodge racionais são algébricas | aberto | — |

## Beal

| Camada | Base | Enunciado-alvo | Estado | Arquivo |
|---|---|---|---|---|
| Be1 | Variantes refutadas | Fermat–Catalan, fator comum necessário, Euler | ✅ | `RefutacoesBeal` |
| Be2 | Beal polinomial | via Mason–Stothers | ✅ | `BealPolinomial` |
| Be3 | Curva de Frey | discriminante e semiestabilidade | 🟡 | `FreyBeal`, `FreyBealResidual` |
| Be4 | Modularidade / Darmon–Granville | finitude por assinatura | ⛔ | — |
| — | **Núcleo aberto** | Beal para inteiros | aberto | — |

---

## Ordem de ataque

1. **N2b** (instância Galerkin): fecha "soluções de Galerkin globais" e abre N3–N5.
2. **R2 → R3 → R4** (Hardy): primeira parte provada de RH sobre a reta.
3. **P3** (M2d): fecha "SAT é NP-completo" no modelo genuíno.
4. **B1b → B2** (torsão): primeira estrutura de `E(ℚ)`.
5. **Y3** (positividade por reflexão).

Nenhuma camada desta lista altera os núcleos abertos. `OPEN_MATH = true`, `CLOSED_MATH = false`.
