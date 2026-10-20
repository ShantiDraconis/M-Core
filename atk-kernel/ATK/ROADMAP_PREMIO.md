# M-Core: roteiro honesto de `nenhum` → `verdadeiro` para os 7 enunciados

Este documento não é Lean — de propósito. Não há espaço seguro neste repositório para um
"rascunho com `sorry`": `final-proof-miner.yml` roda por `cron` a cada hora, independente de
qualquer push, e sua checagem (`grep -RInE '\b(sorry|admit|sorryAx)\b' --include='*.lean' .`) é
sobre a raiz do repositório inteiro — não só `ATK/`. Qualquer `.lean` com `sorry`, em qualquer
diretório, falha esse workflow dentro de uma hora após o merge. Por isso este roteiro é só prosa:
nomeia os alvos reais e onde eles já estão, sem criar nenhum arquivo Lean novo.

Os sete enunciados-alvo já existem no kernel como `Prop`s honestas — sem prova, sem `sorry`,
compilando hoje precisamente porque não afirmam nada. `ValorBelnap` de cada um: `nenhum`
(`⟨false, false⟩`) — nem prova, nem refutação. Virar `verdadeiro` (`⟨true, false⟩`) exige uma
prova real, do tamanho exato do enunciado, inserida em `ATK/` como um teorema de verdade, do
mesmo jeito que `ATK.ObligationsClosed.B1`/`B4` chegaram lá.

| # | Problema | Alvo real (nome Lean, sem prova) | Onde vive hoje | O que falta |
|---|---|---|---|---|
| O1 | Riemann | `ATK.NecessidadeBD.EntradaLittlewood ε` (`0 < ε ≤ 1/2`) e `EntradasNecessidade` | `ATK/NecessidadeBD.lean` | Littlewood-type bound em `1/ζ` na linha crítica + decaimento de `J(ε)` via produto de Hadamard. Checado nesta sessão: nenhuma das duas peças (contagem de zeros/fórmula explícita, fatoração de Hadamard para funções inteiras) está no Mathlib hoje. `EntradasNecessidade ⇒ RH` já está provado (`rh_of_entradas`); a direção que falta tem, pelo próprio docstring do arquivo, "a força exata de RH". |
| O2 | Beal | `ATK.Conditional.Beal.GCDLowerBoundSmallExponents` | `ATK/Conditional/Beal.lean` | Excluir o caso residual `mdc(x,y,z) ≤ 2`; ~11-17% do domínio já reduzido via FLT/Darmon–Merel (condicional a B2/B8), resto aberto. |
| O3 | Navier–Stokes | `ATK.Conditional.NavierStokes.EnstrophyAPrioriBound` | `ATK/Conditional/NavierStokes.lean` | Cota a priori para a enstrofia independente de já saber que a solução é suave — equivalente em força aos critérios de Beale–Kato–Majda/Prodi–Serrin, não contornável por uma desigualdade mais fraca (ver `ATK.NSExplosao.explosao_comparacao`). |
| O4 | P vs NP | `ATK.Conditional.PvsNP.SATNotInP` | `ATK/Conditional/PvsNP.lean` | Um lower bound super-polinomial real para SAT — é o próprio P ≠ NP, não um passo intermediário. `B4` (Cook–Levin, `SAT ∈ NP`) já provado; não ajuda a fechar esta direção. |
| O5 | Hodge | `ATK.Conditional.Hodge.MiddleCodimension` | `ATK/Conditional/Hodge.lean` | Toda classe de Hodge racional vem de um divisor/ciclo algébrico — falta a parte que depende de cohomologia de variedades (sequência exponencial), fora do que `HodgeFiltracao` já cobre incondicionalmente. |
| O6/O7 | BSD | obrigação de posto (`rank E ≤ analyticRank E` para posto analítico ≥ 2) | `ATK/Conditional/BSD.lean` | Cota superior do posto via Selmer/sistema de Euler — Gross–Zagier–Kolyvagin (`B6`, já certificado) só cobre posto analítico ≤ 1; nenhum método geral conhecido além disso. |
| O8 | Yang–Mills | obrigação de mass gap | `ATK/Conditional/YangMills.lean` | Construção de medida em `ℝ⁴` satisfazendo os axiomas de Osterwalder–Schrader com `mass gap > 0` — a reconstrução (`B7`, já certificada) só existe no modelo de rede de `ATK.YMToy`, não no contínuo. |

## O que o roteiro não é

- Não é uma lista de "quase resolvido" — cada linha é, na força lógica, pelo menos tão difícil
  quanto o problema de Millennium correspondente (literalmente, no caso de O1 e O4).
- Não cria nenhum arquivo `.lean` novo, com ou sem `sorry`.
- Não altera `AuditoriaBelnapReal.lean`: os oito itens continuam `nenhum`, auditados com fonte
  real, sem mudança nesta rodada.

## Quando algo muda de fato

Quando (e só quando) uma prova real e certificada — compila limpo, sem `sorry`/`admit`/`axiom`,
sobre o enunciado exato de uma das linhas acima — entrar em `ATK/`, ela:

1. vira um teorema novo em `scripts/expected_theorems.txt` e um import em `ATK.lean`;
2. muda o `proof_theorem`/`status` do item correspondente em `scripts/obligations.json`;
3. muda esse item, em `ATK/AuditoriaBelnapReal.lean`, de `nenhum` para `verdadeiro` — não por
   decreto, mas porque `Evidencia.valor` o computa a partir do `temAFavor := true` real, com
   `prova := some "<nome do teorema>"`.

Até lá, o estado honesto é o que já está auditado: `nenhum` nos oito, `verdadeiro` só em B1/B4,
`falso` nos dois esquemas paramétricos sem ligação fixada (NS, P vs NP) — uma revisão de PR
corrigiu uma versão anterior que rotulava esses dois como `ambos` por conflação entre
reivindicações; veja a seção 6 de `README_FECHAMENTO_HONESTO.md`.
