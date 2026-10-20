# M-Core: relatório verificável

Cada afirmação abaixo aponta para um teorema que existe em `atk-kernel/ATK/` e compila.
Para verificar, sem precisar acreditar neste texto:

```bash
cd atk-kernel
lake exe cache get        # ou lake build (compila a Mathlib necessária)
lake build                # a biblioteca inteira
python3 scripts/check_axioms.py   # CERTIFIED só com: compila, sem sorry/admit/axiom, axiomas padrão
```

## 1. Estado

* **Nenhum dos sete problemas está resolvido.** `CLOSED_MATH = false`; o portão
  `ATK/ClosedMathGate.lean` (que exigiria `closed_math` **sem hipóteses**) não existe.
* **Congelamento** (`atk-kernel/audits/`): **3277 teoremas esperados**
  (`scripts/expected_theorems.txt`), **3277/3277 verificados localmente** (Lean 4.34.1, Mathlib
  `v4.34.1`, `lake build` completo sem erros) e **0 fora do padrão** de axiomas (`propext`,
  `Classical.choice`, `Quot.sound`). Nenhum `sorryAx`, nenhum axioma novo; a distribuição por
  teorema está em `audits/axioms.txt`.
* **Hash das fontes**: o valor atual está em `audits/provenance.json` (`sources_sha256`).
* **CI**: os runs 314–318 passaram. O run 318 imprimiu o mesmo hash do congelamento anterior
  (`f1cff370…`, 3235 teoremas). A atestação das fontes atuais é registrada depois do run
  correspondente. O passo de certificação só termina com sucesso quando todos os esperados são
  `CERTIFIED`.

**Status calculado pelo kernel** (`ATK/StatusFinal.lean`): `open_math_true`, `closed_math_false`,
`nenhum_item_em_B`, `closedMath_correto`. Roteiro do que falta: `conditional/ROTEIRO_LIMITE.md`.

## 2. Enunciados reais (`ATK/EnunciadosOficiais.lean`)

| Problema | Definição | Fidelidade |
|---|---|---|
| Riemann | `RH := RiemannHypothesis` (zeta da Mathlib) | real |
| Beal | `Beal := BealConjecture` | real |
| Navier–Stokes | `NS := NSReal`, Clay (A) em `ℝ³` (`ATK.LigacaoNS.clayA_iff`) | real |
| P vs NP | `PNP := classeP ≠ classeNP` sobre `Turing.FinTM2` | real |
| BSD | `BSD := ClayBSDCompleto` (posto e fórmula refinada, `WeierstrassCurve.LFunction`) | real |
| Hodge | `HodgeOficial C` (`ATK/HodgeOficial.lean`) | real **relativo a 3 construções ausentes da Mathlib**: analitificação, decomposição de Hodge, classe de ciclo |
| Yang–Mills | `YMClay Corr` (`ATK/YMOficial.lean`) | **núcleo real**; a "correspondência a Yang–Mills" não tem definição formal no texto do Clay e é parâmetro |

## 3. Fechamento condicional

* `ATK.ClosedMath.closedMath_of_obligations : Bridges M → OpenObligations M → SevenStatements M`
* `ATK.ObrigacoesMinimas.closedMath_minimo : PontesParametricas M → Obrigacoes M → SevenStatements M`
  (`PontesParametricas` e `Obrigacoes` são **estruturas** em `ATK/ObrigacoesMinimas.lean`)
* `ATK.ClosedMathReal.closedMath_real : Lacunas H Y → ClosedMathRealAlvo H Y`, sobre os enunciados reais
* `ATK.EnunciadosOficiais.sete_condicional`: os sete, a partir das lacunas

As hipóteses **não têm habitante**. O kernel prova que, para três problemas, a lacuna **é** a
conjectura:

* `ATK.ClosedMathReal.lacuna_rh_iff`, `lacuna_beal_iff`, `lacuna_pnp_iff`, `tres_lacunas_iff`
* `ATK.ObrigacoesMinimas.beal_obrigacao_iff`, `pnp_obrigacao_iff`, `hodge_obrigacao_iff`, `bsd_obrigacao_iff`

Por isso um arquivo sem `sorry`/`axiom`/hipótese que construa `SATNotInP` seria uma prova de
P ≠ NP. Não existe atalho por "alinhamento de tipos".

## 4. Pontes já provadas no kernel

* **B1**, Báez-Duarte (suficiência): `ATK.ObligationsClosed.B1 : BaezDuarteCriterion`, com
  `ATK.ObrigacoesMinimas.rh_obrigacao_suficiente : Tendsto DN atTop (𝓝 0) → RiemannHypothesis`
* **B4**, Cook–Levin: `ATK.ObligationsClosed.B4`, `ATK.CookLevinNP.cookLevin : CookLevin modeloPNP SAT`

## 5. O que falta para o iff de RH

A direção de necessidade (RH ⇒ `D_N → 0`) tem esqueleto em `ATK/NecessidadeBD.lean`:
`necessidade_de_entradas`, `rh_iff_DN_of_entradas` e a entrada de Littlewood para `ε > 1/2`
(`entradaLittlewood_of_gt_half`, incondicional). Falta `RiemannHypothesis → EntradasNecessidade`:

* convergência de `Σ μ(n) n^{−ε−s}` para `1/ζ` na linha crítica, com `0 < ε ≤ 1/2` (Littlewood;
  cotas de Lindelöf/Titchmarsh);
* `J(ε) → 0` quando `ε → 0⁺` (produto de Hadamard).

É formalização de resultados publicados, e é pesada. Fechá-la daria o **iff** de RH, não RH.

`ATK/FechamentoO1.lean` dá a estrutura completa: `N(T)` bem definido (zeros finitos, provado),
os três teoremas ausentes da Mathlib com tipo exato (`RiemannVonMangoldt`, `HadamardXi`,
`LittlewoodSobRH`), `NecessidadeRH → (RH ⟺ D_N → 0)` e `rotaO1_iff_rh` (todo produtor de O1 tem a
força exata de RH). Ver `conditional/FECHAMENTO_O1.md`.

## 6. Lógica de 4 valores: a "inversão" open/closed

Em `ATK/Indeterminacy.lean`, seção 4 (Belnap–Dunn), `Quatro` é o par (evidência positiva,
evidência negativa), `B = ⟨true, true⟩` e `nao` troca as componentes:

* `ATK.Indeterminacy.Quatro.nao_B : nao B = B := rfl`: **`B` é o ponto fixo da negação**. A
  equação "open = nao closed" só é satisfeita com os dois lados iguais quando ambos estão em `B`.
* `ATK.Indeterminacy.Quatro.nao_explode`: `P` e `¬P` designados não tornam `Q` designado.
* `ATK.Indeterminacy.closed_e_refutado_impossivel : ¬ (ClosedMath P ∧ ClosedMath (¬ P))`
* `ATK.Indeterminacy.flag_nao_e_prova`: a flag `CLOSED_MATH = true` não é prova.

**Limite**: são identidades da lógica de 4 valores. **Não** dizem nada sobre o estado de RH,
P ≠ NP ou dos outros. Um terceiro estado "verdadeiro e falso" **no nível de prova** é impossível
(`closed_e_refutado_impossivel`): habitar `P` e `¬P` dá `False`.

## 7. O que este projeto não é

* Não é a solução de nenhum dos problemas do milênio.
* Não é candidatura ao prêmio do Clay, que exige resolver o problema, publicar e ser aceito.
* Os módulos `AnaliseInversao`, `RefutacaoTri`, `StatusHonesto` e o teorema `B1_para_B4_real`
  **não existem**.

**Valor real**: formalização e auditoria. São milhares de teoremas rastreáveis com axiomas
auditados, enunciados reais dos problemas, lacunas nomeadas, equivalências provadas no kernel e
firewalls que mostram onde um fechamento seria vazio (`ns_toy_model_vacuous`, `mundo_iff`,
`hodge_cl_zero_iff`, `nucleo_sem_g`, `experimentos/StabilizedBrinquedo.lean`).
