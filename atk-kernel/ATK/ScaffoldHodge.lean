import Mathlib

/-!
# ATK — ScaffoldHodge (andaime mínimo, NÃO teoria canônica)

Isto é andaime (scaffolding) deste projeto — definições simplificadas/
axiomatizadas para permitir enunciar os conceitos de variedade de Kähler e
decomposição de Hodge, NÃO a construção canônica que uma contribuição real
ao Mathlib exigiria (que derivaria tudo de cohomologia de feixes/de Rham
construída do zero, com fibrado tangente holomorfo, derivada exterior geral
de formas sobre uma variedade, etc. — projeto de anos, não deste arquivo).

Pesquisa feita no código-fonte real do Mathlib antes de escrever (busca
direta, não por memória):

* Mathlib TEM variedades modeladas sobre um corpo qualquer via
  `ModelWithCorners 𝕜 E H` + `IsManifold`, incluindo `𝕜 = ℂ`
  (`Mathlib/Geometry/Manifold/IsManifold/Basic.lean`,
  `Mathlib/Geometry/Manifold/Complex.lean`) — "variedade complexa" é
  genuinamente expressável em geral, mas NÃO é usada diretamente abaixo
  (ver a escolha de escopo na próxima observação).
* Mathlib TEM `ContinuousAlternatingMap` como fibrado sobre uma variedade
  (`Mathlib/Geometry/Manifold/VectorBundle/ContinuousAlternatingMap.lean`) —
  a maquinaria de formas diferenciais contínuas existe, mesmo sem o nome
  "DifferentialForm", mas sem derivada exterior geral associada.
* Mathlib TEM `EuclideanSpace 𝕜 (Fin n)` com `[RCLike 𝕜]`
  (`Mathlib/Analysis/InnerProductSpace/PiL2.lean`), dando uma instância
  GENUÍNA de `InnerProductSpace ℂ` quando `𝕜 = ℂ` (via
  `PiLp.innerProductSpace` + `InnerProductSpace ℂ ℂ`, ambas reais).
* Mathlib TEM `DirectSum.IsInternal` (`Mathlib/Algebra/DirectSum/Basic.lean`),
  a noção certa e não-trivial de "soma direta interna de submódulos":
  `Function.Bijective (DirectSum.coeAddMonoidHom A)`.
* Mathlib NÃO TEM: métrica Hermitiana/Riemanniana geral sobre o fibrado
  tangente de uma variedade abstrata, derivada exterior geral de formas
  numa variedade, cohomologia de de Rham ou singular, decomposição de Hodge,
  variedade de Kähler. Busca com zero resultados para cada um desses nomes
  (`KahlerManifold`, `HodgeDecomposition`, `HodgeStructure`, `HodgeClass`,
  `singularCohomology`, `deRhamCohomology` — nenhum existe).

Escolha de escopo feita aqui: em vez de tentar bundlar um tipo de variedade
abstrata arbitrária com uma métrica de fibrado tangente geral (o que exigiria
construir, do zero, exatamente a parte que falta — fibrado tangente +
métrica + derivada exterior), `KahlerManifoldData` trabalha com o MODELO
LOCAL EUCLIDIANO `EuclideanSpace ℂ (Fin n)`, que já carrega a métrica
hermitiana padrão genuína do Mathlib, restrito a um subconjunto aberto. A
condição de fechamento da forma associada (`dω = 0`) é tomada como CAMPO
HIPOTÉTICO — não há como derivá-la aqui, pois a derivada exterior geral não
existe no Mathlib. Isto é o caso local simplificado, honestamente rotulado
como tal — NÃO a definição geral de variedade de Kähler (que permitiria
cartas e colagem arbitrárias sobre uma variedade complexa abstrata).
-/

/-- Andaime (não a construção canônica): um "dado de Kähler" local, sobre um
aberto não-vazio de `EuclideanSpace ℂ (Fin n)`. A métrica hermitiana usada é
a padrão do Mathlib (genuína, não inventada). A condição de fechamento é um
campo hipotético, postulado, não derivado — ver nota acima sobre por que
isso não pode ser feito de primeiros princípios aqui. -/
structure KahlerManifoldData (n : ℕ) where
  domain : Set (EuclideanSpace ℂ (Fin n))
  domain_open : IsOpen domain
  domain_nonempty : domain.Nonempty
  /-- Representa a condição `dω = 0` para a forma de Kähler associada à
      métrica hermitiana padrão em `domain` — postulada, não derivada de uma
      derivada exterior real (que o Mathlib não tem). -/
  isClosed : Prop

/-- Andaime mínimo para decomposição de Hodge: dado um espaço vetorial
complexo `V` (que representaria `H^k(X,ℂ)` para alguma variedade `X`, mas
aqui é um PARÂMETRO ABSTRATO — não derivado de uma construção real de
cohomologia, que o Mathlib não tem), uma "decomposição de Hodge" é uma
família de submódulos `H p` (indexada por `p : Fin (k+1)`, representando
`H^{p, k-p}`) cuja soma direta interna é todo o `V` — usando
`DirectSum.IsInternal`, a noção real e não-trivial do Mathlib para isso
(não uma condição vazia: exige independência das componentes E que a soma
cubra `V` inteiro). -/
structure HodgeDecompositionData (k : ℕ) (V : Type*) [AddCommGroup V] [Module ℂ V] where
  H : Fin (k + 1) → Submodule ℂ V
  isInternal : DirectSum.IsInternal H
