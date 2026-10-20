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
* **OPEN_MATH = true é, por ora, fato sobre os enunciados que o kernel codifica, não certificação
  de fidelidade aos problemas Millennium. F.1 não foi checada** (próximos a conferir: O8,
  O4, O1). **F.1/O8 feito** (`conditional/F1_O8.md`): `ConstructiveYM4D` é **paramétrica**
  (kernel, `ATK.F1YM.parametrica`); o O8 contado, `YMNucleo`, é **sombra** do Clay (sem
  correspondência a Yang–Mills; "não trivial" = não gaussiana) e, por fonte, provavelmente é
  satisfeito pelo quadrado de Wick `:φ²:` do campo livre massivo, o que o tornaria não aberto.
  Ponto (iii), `wick` padrão: confirmado no kernel. Ponto (i), ciclicidade: passa por fonte (o `H`
  é existencial; e os axiomas só usam o campo em `D`, provado no kernel: `troca_fora_de_D`,
  `extensao_de_D`). **Registro aplicado**: `StatusFinal.natureza` marca O1–O7 `aberto` e O8
  `naoFormalizado` (`sete_abertas_uma_nao_formalizada`). `OPEN_MATH = true` = nenhuma obrigação
  provada no kernel; **não** = oito problemas abertos: O8 é sombra com testemunha na literatura
  (por fonte, lacuna de fonte primária em `F1_O8.md` §6).
* **Congelamento** (`atk-kernel/audits/`): **3363 teoremas esperados**
  (`scripts/expected_theorems.txt`), **3363/3363 verificados localmente** (Lean 4.34.1, Mathlib
  `v4.34.1`, `lake build` completo sem erros) e **0 fora do padrão** de axiomas (`propext`,
  `Classical.choice`, `Quot.sound`). Nenhum `sorryAx`, nenhum axioma novo; a distribuição por
  teorema está em `audits/axioms.txt`.
* **Nível da evidência**: local, por compilação (`congelar.py --axiomas`, `lake env lean` em cada
  módulo) **e** por CI (`check_axioms.py` sobre os logs do run, ver abaixo). Localmente o
  `check_axioms.py` dá `NOT_RUN` por desenho: ele lê os logs do CI.
* **Hash das fontes**: o valor atual está em `audits/provenance.json` (`sources_sha256`).
* **CI**: o run **343** de `atk-kernel.yml` (job 118588897763, commit `d6e63b0`) passou: **T1 GREEN,
  3363/3363 teoremas certificados**, T2 GREEN, T6 GREEN (0 fontes sinalizadas), 0 `NOT_CERTIFIED`,
  com `sources_sha256` `24f8dba…`, o mesmo do congelamento local. Atestação em
  `audits/provenance.json`. Commits que só mudam documentação não disparam novo run.

**`CLOSED_MATH` por obrigação** (`StatusFinal.closedMillennium`): um item só conta como fechado
se estiver provado **e** for fiel ao problema Millennium. Fidelidade: `fiel` para O1, O2 e O4 (o
kernel prova que a obrigação é a conjectura real), `sombra` para O8, `naoConferida` para O3, O5, O6
e O7. `closedMillennium_hoje`: nenhum dos oito. `sombra_nunca_millennium`: provar `YMNucleo` não
muda isso.

Para 7 dos 8, *closed* exige resolver um problema Millennium; não há caminho de formalização. Para
O8, *closed* no sentido do kernel é alcançável (reconstrução de Wightman de `:φ²:`; os axiomas do
kernel só usam o campo em `D`, provado em `ATK.F1YM.troca_fora_de_D`), mas isso fecha a sombra
`YMNucleo`, não o Clay. Portanto `CLOSED_MATH = true` agregado seria enganoso mesmo no melhor caso;
o mapa por obrigação, com a semântica "provado e fiel ao Millennium", é o que carrega a verdade.

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

## 6a. O7: uma instância numérica (dado, não teorema)

Para `y² = x³ − x` (condutor 32, posto 0): torsão `[2,2]` (`16 = 4²`), `Δ = 64 > 0` (duas
componentes reais), `Ω = 5.24411510858…` (integral sobre `E(ℝ)` inteiro), `L(E,1) = 0.65551438857…`
(série própria e PARI concordam), Tamagawa `2`, logo `#Ш_an = 1` com resíduo `10⁻²²`.
`conditional/o7_numerico/`. **Não promove nada**: `fidelidade(O7)` continua `naoConferida`, o
status de O7 continua aberto (o alvo é a fórmula para toda curva), e mesmo muitas curvas seriam
dado, não BSD.

## 6b. Limite do kernel

Para sete dos oito, a árvore de redução termina num problema Millennium. O kernel torna a folha
explícita e verificável; não a move. O trabalho futuro é (a) fechar as folhas fecháveis (O1
necessidade, O7 numérico, O8 Wightman, O3 **com interface**: o critério do kernel é o de
enstrofia, não BKM nem PSL), (b) registrar as interfaces (`conditional/MAPA_FOLHAS.md`), e (c)
esperar a matemática. O kernel não transforma conjecturas em soluções: verifica uma prova quando
ela existir, não a produz.

## 7. O que este projeto não é

* Não é a solução de nenhum dos problemas do milênio.
* Não é candidatura ao prêmio do Clay, que exige resolver o problema, publicar e ser aceito.
* Os módulos `AnaliseInversao`, `RefutacaoTri`, `StatusHonesto` e o teorema `B1_para_B4_real`
  **não existem**.

**Valor real**: formalização e auditoria. São milhares de teoremas rastreáveis com axiomas
auditados, enunciados reais dos problemas, lacunas nomeadas, equivalências provadas no kernel e
firewalls que mostram onde um fechamento seria vazio (`ns_toy_model_vacuous`, `mundo_iff`,
`hodge_cl_zero_iff`, `nucleo_sem_g`, `experimentos/StabilizedBrinquedo.lean`).
