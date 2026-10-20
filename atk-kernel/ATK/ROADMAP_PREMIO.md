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

**Categorias de produtor** (nenhuma delas é "fechamento" — todas as 8 linhas abaixo têm
`status = open`):

- `route-eliminated` — uma rota proposta para o alvo foi fechada por incompatibilidade real
  (não é produção, é eliminação de um caminho).
- `conditional-reduction` — reduz o alvo a um caso residual menor, condicional a um resultado
  externo (bridge).
- `context-machinery` — resultado padrão necessário para enquadrar o problema; não avança sobre
  ele.
- `clarifying-prerequisite` — conteúdo real e não-trivial, mas ortogonal ao alvo: esclarece a
  definição correta do problema sem aproximar a prova (ver O5 abaixo — checado nesta sessão,
  `IsHodgeClass` é definida independentemente de `filtracao`, e identificá-las exige o argumento
  de conjugação; não é `Iff.rfl` disfarçado, mas também não toca algebricidade).
- `genuine-partial-producer` — matemática nova real na direção do alvo (casos concretos,
  identidades reduzidas).

**Funil** = existe um teorema conhecido e nomeável tal que formalizá-lo isola o conteúdo aberto
num único enunciado (sem resolvê-lo). "Não formalizado" significa que o caminho existe na
literatura mas não foi andado neste kernel. Distinção que importa: funil isola a **obrigação
inteira** num único enunciado aberto nomeado (O1 ≡ RH; O3 ≡ "nenhuma solução satisfaz BKM/PSL";
O8 ≡ "construir medida contínua não-abeliana"). `genuine-partial-producer` cobre só uma **fatia**
— é por isso que O7 (Gross–Zagier–Kolyvagin cobre posto analítico ≤ 1; o alvo é posto ≥ 2, sem
produtor) é produtor parcial, não funil, mesma forma de O2 (FLT cobre `gcd>2`; `gcd≤2` não tem
produtor).

| O | Alvo (nome Lean) | Categoria | Funil disponível | Status | Razão |
|---|---|---|---|---|---|
| O1 | `ATK.NecessidadeBD.EntradaLittlewood`/`EntradasNecessidade` | `route-eliminated` | `NecessidadeRH` (RH ⇒ D_N→0, Báez-Duarte) — não formalizado | open | Rota de contração `D_{2N}≤q·D_N` eliminada por `sem_contracao_de_piso_log` (incompatível com o piso log BBLS/Burnol). Littlewood-bound + decaimento de Hadamard não estão no Mathlib. |
| O2 | `ATK.Conditional.Beal.GCDLowerBoundSmallExponents` | `conditional-reduction` | nenhum conhecido (ABC implica Beal, mas é mais forte e aberto — funil para cima, não para baixo) | open | FLT (formalizado externamente, não integrado) fecha o caso `gcd(x,y,z)>2` via `exponent_gcd_le_two`; o caso `gcd≤2` é O2 em si. Sem medida natural no espaço de expoentes — nenhuma fração de "cobertura do domínio" é citada aqui. |
| O3 | `ATK.Conditional.NavierStokes.EnstrophyAPrioriBound` | `route-eliminated` | BKM + Prodi–Serrin–Ladyzhenskaya — não formalizado | open | A rota de dados pequenos (`y'≤-ay+by³`, `bM²<a`) nunca pretendeu cobrir o caso geral — não se estende a ele, porque a mesma desigualdade explode quando `by₀²>a` (`NSExplosao.explosao_comparacao`). Não é uma rota geral que "caiu"; é uma desigualdade escalar que nunca bastava sozinha. |
| O4 | `ATK.Conditional.PvsNP.SATNotInP` | `context-machinery` | nenhum conhecido (barreiras — Razborov–Rudich, GCT — são o próprio conteúdo) | open | Shannon (não-construtivo) e a cota linear explícita (`n≤2s+1`) enquadram o problema; nenhum dos dois é um produtor sobre SAT especificamente. Zero produtores reais sobre a obrigação em si. |
| O5 | `ATK.Conditional.Hodge.MiddleCodimension` | `clarifying-prerequisite` | nenhum conhecido (algebricidade não reduz; versão integral é falsa por Atiyah–Hirzebruch, só a racional é o alvo) | open | `HodgeFiltracao` identifica `IsHodgeClass` com a filtração — conteúdo real, mas nunca toca se a classe vem de um ciclo algébrico. |
| O6 | `ATK.Conditional.BSD.RankOpen` (posto analítico ≥ 2) | `genuine-partial-producer` | nenhum conhecido (Iwasawa main conjecture reduz a outro problema aberto) | open | Posto algébrico certificado em curvas concretas (`posto_R30`, `posto_R6`), uma por vez; Gross–Zagier–Kolyvagin só cobre posto analítico ≤ 1. |
| O7 | `ATK.Conditional.BSD.RefinedOpen` | `genuine-partial-producer` | nenhum conhecido | open | Reduz a uma identidade numérica concreta em `y²=x³-x` (`L(E,1)=Ω·∏c_p·#Ш/16`); `#Ш` finitude continua aberta. |
| O8 | `ATK.Conditional.YangMills.ConstructiveYM4D` | `genuine-partial-producer` | OS reconstruction (Osterwalder–Schrader 1973/75) — não formalizado | open | Modelo de rede (`YMToy`) satisfaz a versão lattice de toda condição (positividade de reflexão, clustering com `m(β)>0`); o limite contínuo 4D não-abeliano é o aberto, nomeado. |

## Nota: FLT formalizado externamente (B2)

`anthropics/fermats-last-theorem`, commit `db584cd6d46c92f209a44c0f1c829460d327499d`, pinado em
Lean `v4.33.1` / Mathlib no mesmo commit. Fonte inspecionada diretamente (clone raso, leitura de
`lakefile.lean`, `FinalCheck.lean`, `lean-toolchain`): `FinalCheck.lean` deriva
`flt_mathlib : FermatLastTheorem` (a definição real da Mathlib, `import
Mathlib.NumberTheory.FLT.Basic`) a partir de `fermat_last_theorem`, com `#guard_msgs` gateando
`#print axioms fermat_last_theorem` para `[propext, Classical.choice, Quot.sound]`. Build verde é
alegado pelo README do repositório; **não compilado independentemente nesta auditoria**.

Esse `FermatLastTheorem` é exatamente a hipótese `hFLT` de
`ATK.Conditional.Beal.exponent_gcd_le_two`, já provado e committed neste kernel: dado `hFLT`, toda
solução da equação de Beal tem `gcd(x,y,z) ≤ 2` (a substituição `x=rd,y=sd,z=td` reduz o caso
`gcd>2` a uma instância literal de Fermat). Importar o repo externo não fecharia B2 nem Beal —
só removeria o parâmetro `hFLT` de um teorema já provado. **Beal reduz a O2** (o caso
`gcd(x,y,z)≤2`), que continua `open`. Este kernel não foi alterado para depender do repo externo.

## O que o roteiro não é

- Não é uma lista de "quase resolvido" — cada linha é, na força lógica, pelo menos tão difícil
  quanto o problema de Millennium correspondente (literalmente, no caso de O1 e O4).
- Não cria nenhum arquivo `.lean` novo, com ou sem `sorry`.
- Não altera `AuditoriaBelnapReal.lean`: os oito itens continuam `nenhum`, auditados com fonte
  real, sem mudança nesta rodada.

**Changelog (`bb86b4b`):** `clarifying-prerequisite` é um rótulo deste documento apenas. O enum
de status planejado para `scripts/obligations.json` (Fase 0.2 — `open`, `route-refuted`,
`partial-producer`, `definitional`, `no-funnel-known`) ainda não tem esse quinto valor, e esta
PR não toca `obligations.json`. Quem ler só o JSON hoje ainda vê O5 sob o rótulo antigo
(`definitional`-adjacente); é a mesma misclassificação que esta auditoria corrigiu aqui, só que
ainda não propagada. O enum do schema precisa ganhar `clarifying-prerequisite` (ou nome
equivalente) quando a Fase 0.2 for feita — até lá, este markdown é a fonte certa para O5, não o
JSON.

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
