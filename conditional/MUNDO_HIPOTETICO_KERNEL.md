# Os fechamentos hipotéticos no kernel: o que acontece

Todos os arquivos de "closed math" hipotético foram submetidos ao kernel do Lean
(Lean 4.34.1, Mathlib `v4.34.1`, compilação local). Este relatório registra o resultado e o que
ele significa.

## Resumo

| Grupo | Arquivos | Resultado no kernel |
|---|---|---|
| Família ClosedMath do M-Core (`ClosedMath`, `FinalRoot`, `TeoremaGlobal`, `BridgeReduction`, `ObligationsClosed`, `ObrigacoesMinimas`, `ModelosSete`, `AlgebraTerminal`, `HypothesisCalculus`) | 9 módulos, 170 teoremas | **todos aceitos**, só `propext`, `Classical.choice` e `Quot.sound` |
| Oráculos `HypotheticalClosureOracle` (Beal, BSD, Hodge, P≠NP) | 4 cadeias, 59 módulos no total | **todos aceitos**, os teoremas-oráculo **sem nenhum axioma** |
| Navier–Stokes: `BackwardHypotheticalClosureOracle`, `GlobalRegularityFromG1`, `StabilizedHypothetical`, `NS_Multistate` | 4 arquivos | os originais **não compilam**; com as correções mínimas de `experimentos/ns_correcoes_minimas.diff`, aceitos |
| Mundo O1 reconstruído (`ATK/MundoHipotetico.lean`) | 28 teoremas | aceitos, padrão |
| Experimento com `axiom` e `sorry` (`experimentos/AxiomaHipotetico.lean`) | 4 teoremas | aceitos pelo kernel, **denunciados** por `#print axioms` |

Logs: `atk-kernel/experimentos/oraculos_externos.out`, `StabilizedBrinquedo.out` e
`AxiomaHipotetico.out`. Para reproduzir, use `atk-kernel/scripts/kernel_externo.py SRC MODULO OUT`.

## O que o kernel mostra

### 1. O fechamento aceito é sempre condicional

O kernel aceita `closedMath_of_obligations`, `teorema_global`, `raiz_de_produtores`,
`closedMath_minimo` etc. porque **cada um recebe as obrigações abertas como hipótese**
(`OpenObligations M`, `ObrigacoesTerminais M`, `Produtores M`, …). Nenhum deles tem um enunciado
sem hipóteses. O portão `ATK/ClosedMathGate.lean`, que exigiria `theorem closed_math` **sem**
hipóteses, continua inexistente.

### 2. O mundo hipotético é exatamente as conjecturas (`mundo_iff`)

`Nonempty (Mundo S) ↔ ∀ i, Pᵢ`. Supor o mundo O1 é supor os oito enunciados; o fechamento
`fechar_tudo` é só aplicar `fᵢ` a `qᵢ` (`fechar_tudo_eq` é `rfl`), e o mundo construído a partir
das provas tem `Qᵢ = Pᵢ` com `fᵢ = id` (`mundo_canonico_circular`).

### 3. Os oráculos dos repositórios são a identidade

`hypothetical_common_prime`, `hypothetical_rank_part`, `hypothetical_pointwise`,
`hypothetical_final` e `hypothetical_global_regularity` passam **sem nenhum axioma**, porque
`HypotheticalClosure := Enunciado`, e o teorema devolve a hipótese (`oraculo_eq_id : oraculo P = id`).
O próprio Hodge declara isso (`specificationOracleOnly = true`).

### 4. Vacuidade e explosão

* Se algum `Pᵢ` é falso, não existe mundo (`mundo_vazio_de_falso`), e "do mundo" segue qualquer
  proposição (`mundo_prova_tudo_se_falso`).
* Com uma especificação contraditória (`RH` num terminal, `¬RH` noutro), o kernel aceita
  `Mundo → RH ∧ ¬RH` (`contraditorio_prova_rh_e_nao_rh`). Aceitar uma implicação não diz nada
  sobre a consistência das hipóteses.

### 5. Brinquedo e fidelidade

* Com `Pᵢ := True` existe mundo (`mundo_brinquedo`): "fechado", sem conteúdo.
* Só uma especificação **fiel** (`Pᵣₕ = RiemannHypothesis`, `P_beal = BealConjecture`) entrega os
  enunciados reais (`fiel_fecha`), e o brinquedo só é fiel se RH e Beal já forem verdadeiros
  (`brinquedo_fiel_iff`).

### 6. Navier–Stokes: o fechamento "22 → 25 → 3 → 1" prova `1 + 1 = 2`

`experimentos/StabilizedBrinquedo.lean` constrói um `CompleteConditionalClosure` com todas as
funções iguais a 0 e todas as proposições iguais a `True`. Para **qualquer** proposição `P`
provada, existe um fechamento cuja conclusão `NoFiniteSingularTime` é exatamente `P`
(`conclusao_arbitraria`), e `Perelman_like_22_25_3_1` aplicado a ele prova `1 + 1 = 2`
(`perelman_prova_aritmetica`). A razão é que o campo `ESSEndpoint.NoFiniteSingularTime` é uma
`Prop` livre, sem ligação com as equações. O teorema não fala de Navier–Stokes.

### 7. `axiom` e `sorry`: o kernel aceita e denuncia

| Teorema | `#print axioms` |
|---|---|
| `rh_e_beal_postulados` (mundo fiel postulado) | `propext, Classical.choice, Quot.sound, ATK.Experimento.S, ATK.Experimento.W, ATK.Experimento.hS` |
| `rh_e_nao_rh` (mundo contraditório postulado) | `…, ATK.Experimento.Wc` |
| `falso : False` | `…, ATK.Experimento.Wc` |
| `rh_por_sorry` | `propext, sorryAx, Classical.choice, Quot.sound` |

O kernel aceita até `False` quando ele vem de um axioma postulado: a responsabilidade é de quem
postula. O `scripts/check_axioms.py` reprova os quatro (fonte com `axiom`/`sorry`, axiomas fora
do padrão). Esse arquivo fica fora de `ATK/` e não entra na certificação.

Durante este trabalho, uma prova com um nome de lema errado (`brinquedo_fiel_iff`, primeira
versão) foi registrada pelo kernel com `sorryAx`, que é o mesmo mecanismo que reprova
automaticamente um teorema quebrado no CI.

## Defeitos encontrados nos arquivos de Navier–Stokes

Os originais em `navier-stokes-critical-barrier-audit` **não compilam em nenhuma versão do Lean 4**
pelos três primeiros motivos abaixo; os demais são de versão ou de prova. As correções foram
aplicadas **só nas cópias de teste** (`experimentos/ns_correcoes_minimas.diff`). Os repositórios
originais não foram alterados.

| Arquivo | Defeito | Efeito |
|---|---|---|
| `MillenniumAudit/StabilizedHypothetical.lean` | `/-! … -/` antes de `import Mathlib` | erro: `import` precisa vir no início do arquivo |
| `StabilizedHypothetical.lean` | campos `y z : ℝ`, `γ1 γ2 θTail … : ℝ` etc. sem parênteses | em Lean 4 isso declara **um** campo `y : z → ℝ`, não dois reais; 9 estruturas ficam com tipos errados |
| `formal/lean/CriticalBarrier/GlobalRegularityFromG1.lean` | `Integrable` sem `open MeasureTheory` | nome desconhecido; vira variável implícita e quebra `G1Bridge` |
| `GlobalRegularityFromG1.lean` | `/-- … -/` antes de `variable` | erro na versão 4.34 (docstring não pode anotar `variable`) |
| `StabilizedHypothetical.lean`, `G1b_total_strict` | `positivity` não usa as hipóteses `h.hγ1 … ≥ 0` | a prova falha; com `linarith [h.hγ1, …]` passa |
| `StabilizedHypothetical.lean`, `K0a_totality` | `rw [← Real.sqrt_sq …]` reescreve todo `ε` | a prova falha; com `calc` passa |
| `NS_Multistate.lean` | `import Mathlib` sem uso | só removido no teste (a Mathlib inteira não está compilada aqui) |

Mesmo corrigidos, esses arquivos continuam condicionais: `G1Bridge` e `ActualNSToTwentyFive` não
têm construtor a partir das equações de Navier–Stokes, como os próprios arquivos dizem.

## Estado

`OPEN_MATH = true` e `CLOSED_MATH = false`, inalterados. O kernel confirma a lógica dos
fechamentos; o conteúdo matemático está inteiro nas hipóteses que nenhum arquivo produz.
