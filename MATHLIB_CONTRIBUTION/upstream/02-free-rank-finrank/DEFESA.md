# Candidato 02 — material de estudo para defender o PR na revisão da Mathlib

Este arquivo é para o titular **estudar**, não para copiar. A política da Mathlib
([página "contribute" do site da comunidade](https://github.com/leanprover-community/leanprover-community.github.io/blob/lean4/templates/contribute/index.md))
diz:

- "Using an LLM when writing comments on GitHub or Zulip is not allowed: use your own words."
- "It is essential that you understand all the content written by an AI", e a pessoa deve ser
  capaz de "justify each decision to reviewers without the use of an AI".
- O uso de IA tem de ser explicado na descrição do PR ("Explain which tool(s) you used and how
  you used it"). Um PR com bastante código gerado leva o rótulo `LLM-generated`, que se põe
  comentando `LLM-generated`.

Por isso as respostas aos revisores têm de ser suas, escritas sem IA. O que segue explica a
matemática e cada escolha, para você poder responder com segurança.

## 1. O que o PR acrescenta

Dois arquivos, +32 linhas:

| Declaração | Arquivo | O que diz |
|---|---|---|
| `QuotientGroup.instHasUniqueRoots` e a versão aditiva `QuotientAddGroup.instHasUniqueDiv` | `Mathlib/GroupTheory/Torsion.lean` | `G ⧸ torsion G` tem raízes únicas: `aⁿ = bⁿ`, `n ≠ 0` ⟹ `a = b` |
| `AddGroup.rank_eq_finrank_int` | `Mathlib/GroupTheory/FiniteAbelian/Basic.lean` | `G` f.g. com divisão única: número mínimo de geradores = `finrank ℤ G` |
| `AddCommGroup.freeRank_eq_finrank` | idem | `G` f.g.: `freeRank G = finrank ℤ G` |

E um `import` privado novo, `Mathlib.LinearAlgebra.Dimension.Torsion.Basic`.

## 2. A matemática, em palavras

**Definições da Mathlib.** `AddGroup.rank G` é o menor tamanho de um conjunto que gera `G` como
grupo. `AddCommGroup.freeRank G` é `AddGroup.rank (G ⧸ torsion G)`, o número mínimo de
geradores da parte livre. `Module.finrank ℤ G` é a dimensão de `G` como `ℤ`-módulo (o tamanho
máximo de uma família linearmente independente).

**Lema `rank_eq_finrank_int`.** Seja `G` abeliano, finitamente gerado e sem torção.

1. Pelo teorema de estrutura sobre um domínio de ideais principais, `G` é um `ℤ`-módulo
   **livre**: tem uma base com `r = finrank ℤ G` elementos (`Module.finBasis`).
2. `rank ≤ r`: os `r` elementos da base geram `G` como `ℤ`-módulo. Sobre `ℤ`, o `span` de um
   conjunto é o subgrupo que ele gera (`Submodule.span_int_eq_addSubgroupClosure`). Logo eles
   geram `G` como grupo, e `AddGroup.rank_le` dá `rank G ≤ r`.
3. `r ≤ rank`: tome um conjunto gerador `S` com `rank G` elementos (`AddGroup.rank_spec`). Ele
   gera `G` como grupo, logo como `ℤ`-módulo, e um conjunto que gera um módulo tem pelo menos
   `finrank` elementos (`finrank_le_of_span_eq_top`).

O passo 1 é onde "sem torção" é usado. Contraexemplo: `ZMod 2` é gerado por um elemento
(`rank = 1`), mas `finrank ℤ (ZMod 2) = 0`.

**Lema `freeRank_eq_finrank`.** `freeRank G = rank (G ⧸ T)`, com `T` a torção. `G ⧸ T` é sem
torção (a instância nova), então o lema anterior dá `rank (G ⧸ T) = finrank ℤ (G ⧸ T)`. E
quocientar pela torção não muda o posto. Esse resultado já está na Mathlib
(`finrank_quotient_torsion_eq`, em `LinearAlgebra/Dimension/Torsion/Basic.lean`). A razão é que
uma família independente em `G ⧸ T` se levanta a uma família independente em `G`.

**Instância.** Em `G ⧸ T` (comutativo), se `aⁿ = bⁿ` com `n ≠ 0`, então `(a b⁻¹)ⁿ = 1`, e a
ausência de torção dá `a = b`. Na Mathlib: `(Commute.all a b).eq_of_pow_eq_pow hn hab`, usando a
instância `IsMulTorsionFree` que já existia para o quociente.

## 3. Cada escolha e as perguntas prováveis dos revisores

**"Por que `[HasUniqueDiv G]` e não `[IsAddTorsionFree G]`?"** Em 29/09/2026 a Mathlib separou os
dois conceitos. A docstring de `IsAddTorsionFree` em `Mathlib/Algebra/Group/Monoid.lean` pede
para usar `HasUniqueDiv` em monoides comutativos. Assim a busca de instâncias deriva as duas
coisas sem um laço caro. `HasUniqueDiv` implica `IsAddTorsionFree` por instância, e para grupos
comutativos os dois são equivalentes.

**"Por que uma instância nova em `Torsion.lean`?"** Antes dela, `G ⧸ torsion G` só tinha
`IsMulTorsionFree`, e o lema acima não se aplicava ao quociente sem uma prova local. A primeira
versão do patch tinha essa prova como um `have` dentro de `freeRank_eq_finrank`. Uma instância
é o lugar certo, porque serve para qualquer lema futuro que peça `HasUniqueDiv`.

- O nome aditivo é dado à mão (`to_additive _root_.QuotientAddGroup.instHasUniqueDiv`): sem
  isso o `to_additive` gerava `QuotientAddGroup.insthasUniqueDiv`, com `h` minúsculo.
- Objeção possível: "agora há dois caminhos para `IsMulTorsionFree` no quociente." São
  proposições, então não há problema de diamante.
- Alternativa, se pedirem: trocar a instância antiga pela nova, já que `HasUniqueRoots` implica
  `IsMulTorsionFree`. Não fiz isso para não mudar uma declaração existente. É fácil fazer.

**"Por que em `FiniteAbelian/Basic.lean`?"** O lema precisa do teorema de estrutura sobre um
PID (`Module.Free` para módulos f.g. sem torção), que vem de `Mathlib.Algebra.Module.PID`. Esse
arquivo já é importado ali. `Torsion.lean`, onde `freeRank` é definido, fica muito abaixo na
hierarquia e não pode importar isso. A docstring de `FiniteAbelian/Basic.lean` trata da
estrutura dos grupos abelianos f.g., que é o assunto.

**"O import novo é necessário?"** Ele traz `finrank_quotient_torsion_eq`. Medido no `master`: o
fecho de imports do arquivo já tinha 2198 módulos e o import novo acrescenta **só** o próprio
`Dimension/Torsion/Basic.lean`. Foi posto como `import` privado, não como `public import`.

**"A prova `exact finrank_quotient_torsion_eq` depende de igualdade definicional?"** Sim.
`finrank_quotient_torsion_eq` fala de `G ⧸ (torsion G).toIntSubmodule` (quociente por
submódulo), e o objetivo fala de `G ⧸ torsion G` (quociente por subgrupo). Os dois tipos e as
duas estruturas de `ℤ`-módulo são iguais por definição, e o Lean aceita. Se um revisor preferir
não depender disso, há uma prova alternativa sem esse passo. Ela estava na primeira versão do
patch e está no commit `e403f3b`:

- `f : G →ₗ[ℤ] G ⧸ T` é sobrejetora, e o núcleo `T` tem posto 0, porque todo elemento é de
  torção (`rank_eq_zero_iff`);
- pelo teorema do posto e da nulidade (`LinearMap.rank_eq_of_surjective`),
  `rank G = rank (G ⧸ T) + 0`.

**"Por que o nome `AddGroup.rank_eq_finrank_int`?"** `AddGroup.rank` porque é sobre esse
conceito. O sufixo `_int` diz que o `finrank` é sobre `ℤ`, como em `Submodule.torsion_int` e
`isAddTorsion_iff_isTorsion_int`. Alternativas razoáveis, se pedirem:
`AddGroup.rank_eq_finrank`, `Module.finrank_int_eq_addGroup_rank`.

**"E a versão multiplicativa?"** Não está incluída. Ela seria
`CommGroup.freeRank G = Module.finrank ℤ (Additive G)`. O `to_additive` não a gera, porque o
enunciado só faz sentido do lado aditivo. Pode ser acrescentada se pedirem.

**"E uma versão com `Module.rank` (cardinal)?"** Sai em uma linha de `Module.finrank_eq_rank`
(para `G` f.g.). Também pode ser acrescentada.

**"Para que serve?"** A Mathlib define `freeRank` e não tem nenhum lema que o ligue à álgebra
linear. O posto de Mordell–Weil de uma curva elíptica aparece de duas formas:
`AddCommGroup.freeRank E(K)` (por exemplo no formal-conjectures, enunciado de BSD) e
`Module.finrank ℤ E(K)` (o mais comum). Este lema é exatamente a ponte entre as duas. No ATK ele
foi necessário para comparar os dois enunciados de BSD (`ATK.IntegracaoFCBSD.postoMW_eq_freeRank`).

## 4. Perguntas para testar a si mesmo (responda sem consultar)

1. Por que `rank_eq_finrank_int` é falso para `ZMod 2`? Qual hipótese falha?
2. Qual dos dois sentidos da desigualdade usa que `G` é livre? E o outro, usa o quê?
3. Por que, sobre `ℤ`, "gera como grupo" e "gera como módulo" são a mesma coisa?
4. O que diz `finrank_quotient_torsion_eq`, e por que quocientar pela torção não muda o posto?
5. Por que `HasUniqueDiv` e não `IsAddTorsionFree`?
6. O que muda para quem importa `FiniteAbelian/Basic.lean` com o import novo?

## 5. Checagens feitas no `master` `8678dc2` (Lean v4.35.0)

Ver `STATUS.md`: build dos dois arquivos e dos módulos que importam `Torsion.lean` diretamente;
`#print axioms` só com `propext`, `Classical.choice`, `Quot.sound`; `#lint` sem erros nos dois
arquivos; `lake exe lint-style` limpo.
