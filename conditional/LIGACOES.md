# Ligações L1–L5 — dos modelos paramétricos aos objetos reais (14/10/2026)

Para o verde universal, cada linha precisa de um portão `theorem terminal : <enunciado>` sem
hipóteses (`UNIVERSAL_GREEN.md`). Nas cinco linhas paramétricas, o `<enunciado>` só significa o
problema do Clay depois da **ligação**: o modelo construído com os objetos reais. Sem ela, um
"verde" seria vazio (`ns_toy_model_vacuous`, `pnp_toy_model_vacuous`).

| Ligação | Estado | Arquivo | O que foi construído | O que falta |
|---|---|---|---|---|
| **L1** Navier–Stokes | **`CLOSED`** (revisão humana, 14/10/2026) | `ATK/LigacaoNS.lean` (15) | `modeloNS`: dados = `ν > 0` e `u₀ ∈ 𝓢(ℝ³, ℝ³)` com `div u₀ = 0`; solução global = `p, u ∈ C^∞(ℝ³ × [0, ∞))` com `∂ₜu + (u·∇)u = νΔu − ∇p`, `div u = 0`, `u(·, 0) = u₀`, energia `∫|u|²` limitada | — (fechada) |
| **L2** P vs NP | **`CLOSED`** (titular, 14/10/2026) | `ATK/LigacaoPNP.lean` (13), `ATK/ComposicaoTM2.lean` (26), `ATK/ModeloPNP.lean` (22) | `modeloPNP`: linguagens binárias, `classeP`/`classeNP` sobre `Turing.FinTM2`, reduções de Karp; `P ⊆ NP` e P fechada por reduções **provados** (composição de máquinas em tempo polinomial); `SAT` = CNF satisfatíveis em binário; `fiel : PneNP modeloPNP ↔ P ≠ NP` | — (fechada) |
| **L3** Hodge | `NAO_EXISTE_NA_MATHLIB` | — | — | cohomologia de de Rham/Betti de variedades projetivas complexas, decomposição de Hodge, classes de ciclos |
| **L4** BSD | `PARTE_DO_POSTO_NO_KERNEL` | `ATK/LigacaoBSD.lean` (4) | `ClayBSD`: sobre `WeierstrassCurve.LSeries` da Mathlib, para toda `E/ℚ` existe `F` inteira = `L(E, s)` em `Re s > 3/2` com `ord_{s=1} F = rank E(ℚ)` (o enunciado oficial do Clay); `posto_iff`: `BSDRank modeloPosto ⟺ ClayBSD` sob modularidade e Mordell–Weil (hipóteses explícitas) | a fórmula refinada (`Ω_E`, regulador de Néron–Tate, `Ш`, Tamagawa, torção), exigida pelo portão `BSDFull` |
| **L5** Yang–Mills | `NAO_EXISTE_NA_MATHLIB` | — | — | QFT construtiva em ℝ⁴ (axiomas de Wightman/Osterwalder–Schrader), grupo de gauge compacto |

## L1 — por que é o enunciado (A) do Clay

`clayA_iff`: `ClayStatementA modeloNS ⟺ ∀ ν > 0, ∀ u₀ ∈ 𝓢(ℝ³, ℝ³), div u₀ = 0 → ∃ u, p` com
(1), (2), (3), (6), (7) do texto oficial (Fefferman, 2000). Escolhas de tradução:

* condição (4) `|∂^α u°(x)| ≤ C_{αK}(1 + |x|)^{−K}` = classe de Schwartz da Mathlib;
* (6) = `ContDiffOn ℝ ∞` (suave, não analítico) em `ℝ³ × [0, ∞)`;
* (1) imposta para `t > 0`; em `t = 0` segue de (6) por continuidade;
* (7) inclui a integrabilidade de `|u(·, t)|²` (a integral de Bochner de uma função não
  integrável vale 0 e tornaria (7) vazia).

Testes no kernel: o dado nulo é admissível e tem solução global (`zero_global`); `x ↦ x` não é
admissível (`div = 3`, `id_nao_admissivel`); o fluxo `u = t·v`, `p = −⟨v, x⟩` resolve (1)–(2)
em todo ponto mas não tem energia finita (`fluxo_sem_energia`) — a condição (7) exclui o exemplo
clássico de não unicidade; um dado constante `v ≠ 0` não tem solução global
(`global_nao_trivial`, o contrário do modelo de brinquedo). `clay_ns_condicional`: ponte B3 +
obrigação O3 no modelo genuíno ⇒ o enunciado (A) do Clay.

`SmoothOn` e `enstrophy` (usados por B3 e O3) seguem a teoria local clássica: solução suave em
`[0, T)` com energia e enstrofia finitas em cada `[0, T']`; `enstrophy` = supremo de `∫|∇u|²`
sobre as soluções dessa classe, que é única (Leray; Kato).

## L2 — construída e fechada (14/10/2026)

Parte 1 (`ATK/LigacaoPNP.lean`): `L ∈ P` ⟺ a função característica de `L` é computável por uma
`FinTM2` em tempo polinomial (`TM2ComputableInPolyTime`); `L ∈ NP` ⟺ verificador em P e
certificado de tamanho polinomial, com pares `⟨w, c⟩` sem ambiguidade (`par_injective`).

Parte 2, o que faltava e agora está no kernel:

1. **Composição de máquinas em tempo polinomial** (`ATK/ComposicaoTM2.lean`, 26 teoremas), que a
   Mathlib não tem: `comp : TM2ComputableInPolyTime ea eb f → TM2ComputableInPolyTime eb ec g →
   TM2ComputableInPolyTime ea ec (g ∘ f)`. A máquina composta roda `M₁`, transfere a saída para a
   entrada de `M₂` por uma pilha auxiliar (duas inversões preservam a ordem) e roda `M₂`;
   `run_comp` dá a execução exata em `n₂ + 2(|y| + 1) + n₁` passos, e `saida_le` limita a saída
   por `|x| + n · pushMax`, o que mantém o tempo total polinomial (`eval_mono`).
2. **`P ⊆ NP`** (`P_sub_NP`): uma máquina construída e verificada passo a passo (`decTM`) decodifica
   o primeiro componente de `⟨w, c⟩` em tempo `2|x| + 2` (`decComputavel`, `dec_par`); o
   verificador é "decodifica e roda o decisor", com certificado vazio.
3. **Reduções de Karp** (`Red`: função computável em tempo polinomial por `FinTM2`), reflexivas e
   transitivas, e **P fechada por elas** (`P_fechada_red`).
4. **SAT**: fórmulas CNF (`List (List (ℕ × Bool))`) codificadas em binário com quatro símbolos de
   dois bits; `SAT` = codificações de fórmulas satisfatíveis. Sanidade: a fórmula vazia está em SAT,
   a cláusula vazia não é satisfatível.
5. **`modeloPNP`** com `fiel : PneNP modeloPNP ↔ ATK.LigacaoPNP.PneNP` (por definição) e `fielL2`.

O modelo de portão `PNPModelo` está preenchido com `ATK.ModeloPNP.modeloPNP` e `ATK.ModeloPNP.SAT`
e compila sem nenhum axioma extra. No portão de P vs NP faltam agora só a ponte B4 (Cook–Levin
**neste** modelo) e o produtor O4 (SAT ∉ P). Fechada pelo titular em 14/10/2026.

## L4 — a parte do posto (14/10/2026)

A Mathlib v4.34.1 já define a função L de uma curva de Weierstrass sobre um corpo de números
(`WeierstrassCurve.LFunction`/`LSeries`), com o fator local certo em cada primo a partir do modelo
minimal e do tipo de redução. Com ela, o **enunciado oficial do Clay** — a expansão de `L(E, s)` em
`s = 1` é `c (s − 1)^r + …` com `c ≠ 0` e `r = rank E(ℚ)` — fica escrito sem objeto novo
(`ATK.LigacaoBSD.ClayBSD`). Provado: a continuação é única (`continuacao_unica`), a ordem não
depende da escolha, e `L(E, 1) = 0 ⟺ posto > 0` (`zero_iff_posto_pos`).

O modelo paramétrico usa postos em `ℕ`; a ponte entre os dois (`posto_iff`) usa a modularidade
(existência da continuação, com ordem finita) e o teorema de Mordell–Weil (posto finito). São
teoremas publicados que não estão na Mathlib e entram como hipóteses explícitas.

O que falta para a L4 inteira é a **fórmula refinada**, que o nosso portão (`BSDFull`) exige junto
com o posto: período real, regulador de Néron–Tate, `Ш` (cohomologia de Galois), números de
Tamagawa e torção. Observação de fidelidade: a descrição oficial do Clay enuncia como problema a
parte do posto; a fórmula refinada aparece como observação. Alinhar o portão de BSD ao enunciado do
Clay (só o posto) é uma decisão do titular.

**Critério de fidelidade certificado (14/10/2026).** `ATK.Termos.PNP.FielL2 M` diz que as classes
do modelo são, a menos de uma bijeção das linguagens, `classeP` e `classeNP`;
`ATK.Termos.PNP.pneNP_de_fiel` prova `FielL2 M → (PneNP M ↔ ATK.LigacaoPNP.PneNP)`. Então quem
construir o modelo da L2 tem um alvo verificável por máquina: provar `FielL2`. Nenhum modelo com
finitas linguagens é fiel (`ATK.Termos.PNP.finito_nao_fiel`), em particular o de brinquedo de
`ATK.FinalRoot.pnp_depende_do_modelo` (`Lang := Bool`). A relação de
redução `Red` não entra no critério: ela só importa para a ponte B4 (Cook–Levin), não para o
enunciado. Ver [`TERMOS.md`](TERMOS.md), termos T21 e T22.

## Efeito no auditor e nos portões

* `terminal-templates/NS.lean.tpl`: a peça `LIGACAO_L1` está preenchida com
  `ATK.LigacaoNS.modeloNS`. Faltam no portão de NS só a ponte B3 e o produtor O3.
* `terminal_gates.json`: NS ganhou `linking_term` e `statement_equivalence`
  (`ATK.LigacaoNS.clayA_iff`); P vs NP ganhou a nota do enunciado fiel `ATK.LigacaoPNP.PneNP`.
* `terminal-templates/PNPModelo.lean.tpl`: as peças `LIGACAO_L2` e `LIGACAO_L2_SAT` estão
  preenchidas com `ATK.ModeloPNP.modeloPNP` e `ATK.ModeloPNP.SAT`; `terminal_gates.json` ganhou
  `linking_term` e `statement_equivalence` (`ATK.ModeloPNP.fiel`) para P vs NP.
* **Fechamento de uma ligação**: é decisão do titular sobre a fidelidade do modelo. O estado que ele
  registra em `obligations.json` vale como escrito; o registro (`revisao_humana`: quem, quando, com
  que base) fica junto, para consulta. O verde de cada linha continua exigindo o portão terminal
  compilado e certificado pelo kernel.
* **L1 e L2 fechadas em 14/10/2026** por aprovação do titular. Contador de ligações abertas:
  **3/5** (L3–L5, sem base na Mathlib).

**Estado calculado: UNIVERSAL_GREEN = false, linhas verdes 0/7, CLOSED_MATH = false.** As
ligações fixam os objetos; não resolvem nenhum problema.

## Revisão técnica da L1 contra o texto oficial (14/10/2026)

Conferência de `ATK/LigacaoNS.lean` com Fefferman, *Existence and smoothness of the Navier–Stokes
equation* (Clay, 2000), caso (A):

| texto oficial | no kernel | parecer |
|---|---|---|
| `ν > 0`, `n = 3`, `f ≡ 0` | `Admissivel`: `0 < ν`; `E3 = EuclideanSpace ℝ (Fin 3)`; força ausente | fiel |
| (4) `\|∂^α u°(x)\| ≤ C_{αK}(1+\|x\|)^{−K}` para todo `α, K` | `u°` é uma `SchwartzMap E3 E3` | fiel (é a definição da classe de Schwartz; implica `u°` suave) |
| `div u° = 0` | `∀ x, div u₀ x = 0` com `div` por `fderiv` | fiel |
| (1) `∂ₜu + (u·∇)u = νΔu − ∇p` para `t ≥ 0` | `NSEq` para `t > 0`; `conv`, `lap`, `grad` coordenada a coordenada | fiel: em `t = 0` a derivada bilateral não existe para funções só definidas em `t ≥ 0`; a forma unilateral segue por continuidade de (6) |
| (2) `div u = 0` para `t ≥ 0` | `∀ x, ∀ t ≥ 0, div (fatia U t) x = 0` | fiel |
| (3) `u(x, 0) = u°(x)` | `∀ x, U (x, 0) = u₀ x` | fiel |
| (6) `p, u ∈ C^∞(ℝ³ × [0, ∞))` | `ContDiffOn ℝ ∞` em `univ ×ˢ Ici 0` | fiel (suavidade até a fronteira `t = 0`) |
| (7) `∫\|u(x,t)\|² dx < C` para todo `t ≥ 0` | `∃ C, ∀ t ≥ 0, Integrable ∧ ∫ ≤ C` | fiel (`< C` e `≤ C` são equivalentes trocando `C`; a integrabilidade é implícita no texto) |
| quantificadores de (A) | `clayA_iff`: `∀ ν > 0, ∀ u° ∈ 𝓢, div u° = 0 → ∃ U P, SolucaoGlobal` | fiel |

Observações: (i) `SmoothOn` e `enstrophy` não fazem parte do enunciado (A); servem à ponte B3 e
à obrigação O3, e quem formalizar B3 terá de prová-la sobre estas definições; (ii) o Clay também
aceita como solução a refutação: `¬ ClayStatementA modeloNS` implica o enunciado (C) (colapso,
tomando `f = 0`), e por isso existe o portão `NSRefutacao`. **Parecer: a L1 é fiel ao caso (A).**
A mudança de `CONSTRUIDA_NO_KERNEL` para `CLOSED` fica para a revisão humana do titular.
