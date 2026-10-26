import Mathlib

/-!
# ATK — PonteHodgeRestante (obstáculos documentados, não formalizados)

Este arquivo NÃO formaliza o teorema de Lefschetz (1,1) nem a Conjectura de
Hodge geral, nem como `Prop` nem como `def`. Pesquisa feita antes de escrever
qualquer código (busca direta no código-fonte do Mathlib, não por memória),
e o resultado é negativo das duas vezes: a infraestrutura necessária
simplesmente não existe no Mathlib hoje. Registrar uma `Prop` mesmo assim
produziria ou uma proposição vazia (sempre trivialmente satisfeita por falta
de hipóteses reais) ou exigiria inventar definições ad-hoc que pareceriam
geometria algébrica séria sem ser — exatamente o tipo de inflação que este
projeto se recusa a fazer. Por isso este arquivo é só documentação do
obstáculo, nada mais.

## 1. Teorema de Lefschetz (1,1)

Enunciado informal: toda classe de cohomologia inteira de tipo (1,1) numa
variedade projetiva complexa suave é a classe de um divisor algébrico.

Para formalizar isso como `Prop` não-vazia, precisaríamos de:

* **Decomposição de Hodge** `H^n(X,ℂ) = ⊕_{p+q=n} H^{p,q}(X)` para uma
  variedade complexa (ou ao menos cohomologia de de Rham com estrutura
  complexa). Busca: `HodgeDecomposition`, `HodgeStructure`, `HodgeClass` —
  **zero resultados** no Mathlib.
* **Cohomologia singular ou de de Rham** de uma variedade/esquema, como
  grupo abeliano graduado `H^k(X, ℤ)` ou `H^k(X, ℂ)`. Busca:
  `singularCohomology`, `SingularCohomology`, `deRhamCohomology` —
  **zero resultados**.
* **Variedade de Kähler** (necessária para a decomposição de Hodge clássica
  via teoria de Hodge harmônica). Busca: `KaehlerManifold`, `KahlerManifold`
  — **zero resultados**.

O que o Mathlib TEM, e que é relevante mas insuficiente sozinho:

* `Mathlib.AlgebraicGeometry.AlgebraicCycle.Basic`: define `AlgebraicCycle`
  e `IsWeilDivisor` (ciclos de codimensão 1 via `Order.coheight`). Isso cobre
  o lado "divisor algébrico" da conclusão do teorema, mas não existe nenhuma
  ponte no Mathlib ligando um `AlgebraicCycle`/`IsWeilDivisor` a uma classe
  de cohomologia — porque a própria noção de "classe de cohomologia de um
  ciclo" (o mapa de classe de ciclo, cycle class map) não está formalizada.

Conclusão: falta tanto a premissa (classe de Hodge de tipo (1,1)) quanto a
ponte entre conclusão geométrica e objeto cohomológico. Não há como escrever
`Lefschetz11 : Prop` que não seja vazia ou inventada.

## 2. Conjectura de Hodge geral

Enunciado informal: toda classe em `H^{k,k}(X) ∩ H^{2k}(X,ℚ)` é combinação
racional de classes de ciclos algébricos.

Depende de tudo que falta no item 1, mais:

* Uma noção de "classe racional" dentro da decomposição de Hodge —
  inexistente, pois a própria decomposição não existe.
* Soma/combinação linear de classes de ciclos algébricos de codimensão `k`
  arbitrária (o Mathlib só tem o caso codimensão 1 via `IsWeilDivisor`).

Conclusão: o obstáculo é estritamente maior que para Lefschetz (1,1), pelo
mesmo motivo de base (ausência total de teoria de Hodge no Mathlib), então
nem a versão mais fraca (k=1) nem a geral podem virar `Prop` honesta aqui.

## Resumo

| Peça necessária                          | Existe no Mathlib? |
|-------------------------------------------|:---:|
| Decomposição de Hodge H^{p,q}              | Não |
| Cohomologia singular/de Rham graduada       | Não |
| Variedade de Kähler                         | Não |
| Ciclo algébrico / divisor de Weil           | Sim (codim. 1 só) |
| Mapa de classe de ciclo (cycle class map)    | Não |

Isso não é falha de formalização desta sessão — é um gap real e documentado
da biblioteca Mathlib em geometria algébrica complexa / teoria de Hodge,
consistente com o estado conhecido do projeto (a área de geometria algébrica
do Mathlib é majoritariamente sobre esquemas sobre corpos quaisquer, não
geometria complexa/analítica).
-/
