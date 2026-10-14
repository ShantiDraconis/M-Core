# Ligações L1–L5 — dos modelos paramétricos aos objetos reais (14/10/2026)

Para o verde universal, cada linha precisa de um portão `theorem terminal : <enunciado>` sem
hipóteses (`UNIVERSAL_GREEN.md`). Nas cinco linhas paramétricas, o `<enunciado>` só significa o
problema do Clay depois da **ligação**: o modelo construído com os objetos reais. Sem ela, um
"verde" seria vazio (`ns_toy_model_vacuous`, `pnp_toy_model_vacuous`).

| Ligação | Estado | Arquivo | O que foi construído | O que falta |
|---|---|---|---|---|
| **L1** Navier–Stokes | `CONSTRUIDA_NO_KERNEL` | `ATK/LigacaoNS.lean` (15) | `modeloNS`: dados = `ν > 0` e `u₀ ∈ 𝓢(ℝ³, ℝ³)` com `div u₀ = 0`; solução global = `p, u ∈ C^∞(ℝ³ × [0, ∞))` com `∂ₜu + (u·∇)u = νΔu − ∇p`, `div u = 0`, `u(·, 0) = u₀`, energia `∫|u|²` limitada | revisão humana das definições → status `CLOSED` |
| **L2** P vs NP | `ENUNCIADO_FIEL_NO_KERNEL` | `ATK/LigacaoPNP.lean` (12) | `classeP`, `classeNP` sobre `Turing.FinTM2` da Mathlib; `PneNP : classeP ≠ classeNP` | instância `ComplexityModel`: composição de `FinTM2` em tempo polinomial (para `P ⊆ NP` e fechamento por reduções) e a linguagem SAT |
| **L3** Hodge | `NAO_EXISTE_NA_MATHLIB` | — | — | cohomologia de de Rham/Betti de variedades projetivas complexas, decomposição de Hodge, classes de ciclos |
| **L4** BSD | `NAO_EXISTE_NA_MATHLIB` | — | — | `L(E, s)` com continuação analítica (modularidade), Ш, regulador, períodos, números de Tamagawa |
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

## L2 — o que está pronto e o que falta

Pronto: `L ∈ P` ⟺ a função característica de `L` é computável por uma `FinTM2` em tempo
polinomial (`TM2ComputableInPolyTime`); `L ∈ NP` ⟺ verificador em P e certificado de tamanho
polinomial, com pares `⟨w, c⟩` sem ambiguidade (`par_injective`). Sanidade com uma máquina
construída e verificada passo a passo (`apagaEscreve`): `∅` e todas as palavras estão em P e em
NP.

Falta, para a instância `ComplexityModel` (e então B4/O4 sobre o objeto real):

1. composição de `FinTM2` com cota polinomial (simulação passo a passo, transferência de pilha
   preservando a ordem, cota do tamanho da saída pelo tempo);
2. com ela: `P ⊆ NP` (o verificador descarta o certificado) e P fechada por reduções de Karp;
3. a linguagem SAT (codificação binária de fórmulas CNF).

## Efeito no auditor e nos portões

* `terminal-templates/NS.lean.tpl`: a peça `LIGACAO_L1` está preenchida com
  `ATK.LigacaoNS.modeloNS`. Faltam no portão de NS só a ponte B3 e o produtor O3.
* `terminal_gates.json`: NS ganhou `linking_term` e `statement_equivalence`
  (`ATK.LigacaoNS.clayA_iff`); P vs NP ganhou a nota do enunciado fiel `ATK.LigacaoPNP.PneNP`.
* O auditor só conta uma ligação como fechada com status `CLOSED`. L1 fica em
  `CONSTRUIDA_NO_KERNEL` até a revisão humana; por isso o contador de ligações continua 5/5.

**Estado calculado: UNIVERSAL_GREEN = false, linhas verdes 0/7, CLOSED_MATH = false.** As
ligações fixam os objetos; não resolvem nenhum problema.
