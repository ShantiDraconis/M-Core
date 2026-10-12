# ATK — agenda de pesquisa formalizada

Estado verificado no kernel do Lean 4.34.1 / Mathlib v4.34.1 (branch `atk-kernel-check`, certificado
`atk-kernel/CERTIFICATE_v2.md`). Nenhuma das sete conjecturas está provada: `OPEN_MATH = true`.

## 1. Auditoria da lógica antiga (`ATK/LogicAudit.lean`, 12/12 no kernel)

Os produtores `Material/Closure.lean` dos repositórios m-core-* são satisfeitos por escolhas triviais:
`MaterialPNPProducer`, `MaterialYMProducer`, `ConcreteAlgebraicityPayload` e `MaterialBSDProducer` aceitam
`True` nos campos que deveriam conter a matemática. `ConcreteUniformLogDNBound` vale para DN = 0. A descida de
Beal não exige boa fundação e admite descida infinita em ℤ. Os alvos de BSD (K8/K12), Hodge (K13) e
P ≠ NP são esquemas sobre dados abstratos: há instâncias verdadeiras e falsas. Provar esses produtores
não diz nada sobre as conjecturas. Eles foram substituídos pelos alvos abaixo.

## 2. Por conjectura

| Problema | Alvo preso à matemática real | Pontes provadas no kernel | O que resta (equivale à conjectura ou é mais forte) | O que falta na Mathlib |
|---|---|---|---|---|
| RH | `RiemannHypothesis` (Mathlib) e `bdDistSq` (distância de Báez-Duarte) | cota ⇒ D_N → 0 ⇒ RH; D_N decresce e converge (D_∞ existe); RH ⇔ D_∞ = 0 | D_∞ = 0 (ou K\* finito, mais forte) | o critério de Báez-Duarte (teorema conhecido, formalizável) |
| Beal | `BealStatement` (gcd em ℕ) | gcd(x,y,z) ≤ 2 dado Fermat; descida bem fundada ⇔ Beal; **Beal ⇒ Fermat** (`ATK.Exact.flt_of_beal`) | a própria conjectura | Fermat completo (projeto em andamento) |
| Navier–Stokes | **`ATK.Exact.NavierStokes` = (A) ∨ (B) ∨ (C) ∨ (D) de Fefferman** (ℝ³, C^∞ em ℝ³×[0,∞), decaimento, energia por integral de Lebesgue) | campo nulo é solução; campo identidade não é (div = 3); absorção, Riccati, absorção sem resto ⇒ enstrofia decrescente, controle de energia ponderado | regularidade global 3D | espaços de Sobolev e soluções de Leray–Hopf 3D |
| BSD | parcial: pontos de E(ℚ), torção ≥ 1 | det/regulador, torção ≥ 1, recuperação de #Ш dada a fórmula | posto analítico = posto, fórmula refinada | continuação analítica de L(E,s) até s = 1 (modularidade) |
| Yang–Mills | — | Cauchy–Schwarz ⇒ massa efetiva não cresce | construção 4D e gap | teoria quântica de campos construtiva (axiomas de Osterwalder–Schrader) |
| Hodge | — | realização linear única quando M é invertível | existência dos ciclos | decomposição de Hodge e mapa de classe de ciclos |
| P ≠ NP | **`ATK.Exact.P_ne_NP`** (máquinas `TM2` da Mathlib, tempo polinomial; NP por verificadores) | P ≠ NP ⇔ ¬(P = NP); P contém um problema concreto | existência de L ∈ NP fora de P | Cook–Levin (para falar de SAT); equivalência TM2 ↔ fita única |

## 3. Alvos exatos (`atk-kernel/ATK/Exact.lean`, 16/16 no kernel)

Os portões das sessões anteriores (`Lane`, `TerminalGate`, `ProofCertificate`, `Producer`) aceitavam qualquer
`Target : Prop`; provou-se no kernel que cada um é habitado **se e somente se** o alvo vale. Agora os alvos
estão fixados nos enunciados oficiais para RH, Navier–Stokes, Beal e P ≠ NP (`ATK.Exact.ExactCertificate`).
Não existe mais "fechamento" com `True`: um certificado terminal tem de conter provas desses enunciados.

**BSD, Yang–Mills e Hodge não são enunciáveis exatamente na Mathlib v4.34.1.** Falta, respectivamente:
a função L de uma curva elíptica sobre ℚ com continuação analítica até s = 1 (modularidade) e o teorema de
Mordell–Weil; a teoria quântica de campos de Yang–Mills em ℝ⁴ com axiomas de Wightman/Osterwalder–Schrader;
a cohomologia de variedades projetivas complexas com decomposição de Hodge, ciclos algébricos e mapa de classe.
Escrever definições improvisadas no lugar seria pior que deixar a lacuna explícita.

**Por que não criar axiomas que "resolvem".** Um `axiom` com o enunciado de uma conjectura é aceito pelo Lean,
mas é a suposição da resposta: aparece em `#print axioms` e reprova o critério 2 de `OBRIGACOES.md`. Os três
axiomas padrão (`propext`, `Classical.choice`, `Quot.sound`) correspondem à matemática usual (ZFC + escolha);
é isso que faz um termo verificado ser uma prova.

## 4. Projetos que avançam de verdade (matemática conhecida, ainda não formalizada)

1. **Critério de Báez-Duarte em Lean.** Transformaria `rh_of_bd_bound` num teorema sem hipótese extra:
   RH ⇔ D_N → 0 sobre o objeto concreto.
2. **P, NP e Cook–Levin sobre as máquinas de Turing da Mathlib.** Prenderia `SAT ∉ P` a um enunciado real.
3. **Contribuir para o projeto de Fermat.** Removeria a hipótese `hFLT` do lema de Beal.
4. **Navier–Stokes:** formular uma divisão bulk/tail **com resto** sobre soluções reais. A versão sem resto
   é falsa (`absorption_without_remainder_forces_decay` mais os dados de Taylor–Green).

Estes são trabalhos de formalização de resultados conhecidos. Nenhum deles prova uma conjectura do milênio.
