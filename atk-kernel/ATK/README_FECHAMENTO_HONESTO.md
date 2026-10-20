# M-Core: Fechamento Honesto do Meio — Por que `true/false` não é um termo de prova

## 1. Resumo

Este documento explica, apontando para teoremas verificados pelo kernel (não apenas texto que
alguém pode pular), por que a proposta `Tri.tf : P → ¬P → Tri P` para marcar `OPEN_MATH` /
`BRIDGE` / `CLOSED_MATH` como "verdadeiro e falso ao mesmo tempo" é logicamente inválida, e qual
é a forma segura de rastrear discordância real entre frentes de ataque: a lógica de quatro
valores de Belnap–Dunn, implementada como metadado de auditoria **fora** do sistema de provas
(`ATK.StatusHonesto`, `ATK.RefutacaoTri`, `ATK.AnaliseInversao`).

Nenhum destes três arquivos fecha, formaliza ou fabrica uma prova de qualquer um dos Millennium
Problems ou da conjectura de Beal. Eles documentam, com teoremas reais sobre os tipos reais do
kernel (`ATK.ClosedMath.Models`, `ATK.ClosedMath.SevenStatements`), por que uma certa tentação de
representação não funciona — e como representar honestamente o estado de evidência atual sem
cair nela.

## 2. O problema com `Tri.tf`

A proposta era:

```lean
inductive Tri (P : Prop) where
  | t  : P → Tri P
  | f  : ¬P → Tri P
  | tf : P → ¬P → Tri P
```

Em Lean, `¬P` é `P → False`. Para construir `Tri.tf h1 h2` é preciso ter, ao mesmo tempo,
`h1 : P` e `h2 : ¬P`. Mas `h2 h1 : False` já é um termo de `False` — e de `False`, `False.elim`
prova qualquer coisa (principio da explosão). `Tri.tf` não é um terceiro estado estável: é um
detector de inconsistência. Se `P := ATK.ClosedMath.SevenStatements M` e alguém de fato
construísse `Tri.tf h1 h2`, a notícia seria que a teoria de base (Mathlib, ou a lógica que o Lean
está checando) é inconsistente — não que `SevenStatements M` tem um terceiro valor de verdade
interessante.

Por que isso passaria pelos checadores de axioma do projeto (`check_axioms.py`,
`axiom-gate-G6b.sh`)? Porque esses scripts checam `sorry`/`admit`/`axiom` e o fecho de axiomas de
um teorema já construído — não checam se as premissas que alguém *forneceria* para construir
`Tri.tf` são, elas próprias, consistentes entre si. É exatamente o tipo de buraco que o projeto
já fechou quando removeu `ForcagemManual`.

## 3. A refutação formalizada (`ATK/RefutacaoTri.lean`)

```lean
theorem tf_requires_false {P : Prop} (h1 : P) (h2 : ¬P) : False := h2 h1
theorem tf_explodes {P Q : Prop} (h1 : P) (h2 : ¬P) : Q := (tf_requires_false h1 h2).elim
```

Consequência concreta para este projeto: `ATK.ClosedMath.SevenStatements M` e sua negação nunca
podem estar ambas habitadas — se estivessem, não seria `true/false`, seria `False`
(`sevenStatements_tf_would_explode`).

## 4. A forma correta: lógica de Belnap como metadado, fora do kernel de provas

Não é possível (nem desejável) ter `P ∧ ¬P` dentro do mesmo sistema lógico. É possível ter dois
`Bool` independentes, fora dele, registrando o que cada frente *relatou* — nunca uma prova
literal de `P` e uma prova literal de `¬P` (`ATK/StatusHonesto.lean`):

```lean
inductive ValorBelnap where
  | verdadeiro | falso | ambos | nenhum
  deriving DecidableEq, Repr

structure Evidencia where
  camada : String
  claim : String
  temAFavor : Bool
  temContra : Bool
  fonte : String
  prova : Option String := none
```

`{temAFavor := true, temContra := true}` não é uma prova de `P ∧ ¬P`. São dois booleanos
registrando dois relatos. Não implica `False`. Não explode. O `lake build` continua verde.

**Ressalva central:** `ambos` significa que duas fontes *relataram* evidência conflitante — não
que a reivindicação tenha um terceiro valor de verdade. Uma reivindicação sem prova em nenhuma
direção é `nenhum`, não `ambos`. Faltar uma etapa de prova não é evidência *contra* o enunciado;
é apenas ausência de evidência. Confundir "incompleto" com "contestado" é exatamente o erro que
este arquivo existe para evitar.

## 5. A equação de inversão `aberto = neg fechado` (`ATK/AnaliseInversao.lean`)

A pergunta "o que faria `OPEN_MATH` e `CLOSED_MATH` fecharem como `true/false` invertido um do
outro, sem nunca construir `Tri.tf`?" tem uma resposta mecânica. Com a negação de Belnap sobre
`ValorBelnap` (fixa `ambos` e `nenhum`, inverte `verdadeiro`/`falso`):

```lean
def neg : ValorBelnap → ValorBelnap
  | .verdadeiro => .falso
  | .falso => .verdadeiro
  | .ambos => .ambos
  | .nenhum => .nenhum

def equacaoInversao (aberto fechado : ValorBelnap) : Prop := aberto = neg fechado
```

o teorema `fixo_e_ambos_ou_nenhum` mostra que os únicos valores que satisfazem `neg v = v` são
`ambos` e `nenhum`. Ou seja: se `OPEN_MATH` e `CLOSED_MATH` forem relatados com o **mesmo** valor
de Belnap e essa equação precisar valer, esse valor só pode ser `ambos` ou `nenhum` — nunca
`verdadeiro` ou `falso` isolados. Isso não é uma falha do kernel; é a lógica de Belnap
confirmando que, além dessas duas, não há uma terceira opção escondida.

## 6. Aplicação honesta ao estado atual — dois exemplos reais, um deles uma correção

* **`ATK.ClosedMath.ns_toy_model_vacuous` / `pnp_toy_model_vacuous`**
  (`ATK/ClosedMath.lean:94,103`): existe um modelo (`temAFavor`) *e* uma prova própria,
  certificada, de que esse modelo específico é vazio/trivial (`temContra`) — evidência real e
  conflitante de duas fontes diferentes dentro do mesmo kernel. Este é um caso legítimo de
  `ambos`.

* **A obrigação aberta de Riemann, `ATK.Conditional.Riemann.UniformLogBound`**
  (`ATK/Conditional/Riemann.lean`): a ponte `BaezDuarteCriterion` (B1) está certificada
  (`ATK.ObligationsClosed.B1`), e o kernel prova
  `riemann_conditional : BaezDuarteCriterion → UniformLogBound → RiemannHypothesis`. Mas
  `UniformLogBound` em si **não tem prova nem refutação no kernel** — é a obrigação O1, marcada
  ABERTA. Isso é `nenhum`, não `ambos`: não existe nenhum teorema no kernel apontando contra
  `UniformLogBound`, só a ausência de uma prova a favor. Um rascunho anterior desta análise
  rotulava essa linha como `ambos` citando "falta uma etapa de prova (Hadamard/convergência)"
  como se fosse evidência contrária — essa é exatamente a confusão que a ressalva da seção 4
  existe para prevenir, e esta versão corrige o rótulo para `nenhum`.

## 7. Por que isso é relevante

Um laudo de auditoria que roda dentro do kernel (`#eval`, `#print axioms`) e diferencia, com
rigor mecânico, "sem prova" de "prova de que é falso" é uma contribuição de metodologia de
honestidade formal — não uma alegação de ter resolvido qualquer um dos Millennium Problems. É
isso, e apenas isso, que este conjunto de três arquivos registra.
