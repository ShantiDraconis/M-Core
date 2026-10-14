# Verde universal e raiz final — a estrutura completa do que falta

Esta é a árvore inteira do fechamento, montada no kernel e no auditor. Ela não prova nenhuma
conjectura. O que ela faz é tornar **exato** e **verificável por máquina** o que falta, e garantir
que `UNIVERSAL_GREEN` e `FINAL_ROOT` só mudem quando a matemática existir.

Estado calculado hoje: `UNIVERSAL_GREEN = false` · `FINAL_ROOT = null` · linhas verdes **0/7** ·
pontes no kernel **1/8** · produtores abertos **8/8** · ligações **L1 e L2 construídas** (revisão humana
pendente; contador de ligações fechadas 0/5) · fiação **21/21** · lacunas: **23 abertas e 2 preenchidas**,
tipos conferidos pelo kernel **25/25** · rota da prova: faltam **16** termos · rota da refutação:
**10** · ensaio do portão **12/12** · resolvidas **0/7** · lacunas fechadas **0/25**.

## As duas metas e o plano T1–T9 — `scripts/plano.py`

O verde universal tem duas metas diferentes, e o auditor agora calcula as duas separadamente a cada
push:

* **verde da biblioteca** (T1–T6 e T9): tudo compila, cada teorema usa só os axiomas padrão, as
  fontes estão congeladas, o projeto é isolado e o portão é fail-closed;
* **verde universal das conjecturas** (T7 e T8): os enunciados reais ligados e os produtores
  terminais provados.

| etapa | critério verificável | estado |
|---|---|---|
| T1 | todos os teoremas esperados certificados; SHA das fontes registrado | ✅ calculado pelo CI a cada push (1097 esperados) |
| T2 | `audits/provenance.json` tem o mesmo SHA das fontes atuais | ✅ congelado (`scripts/congelar.py`) |
| T3 | projeto Lake independente (`atk-kernel/`, lakefile e toolchain próprios) | ✅ |
| T4 | compatibilidade Lean 4.19.0 (raiz `lean/MCore`) ↔ 4.34.1 (`atk-kernel`) | ✅ resolvida por isolamento |
| T5 | `lake build`: todo arquivo auditado compila | ✅ |
| T6 | `#print axioms` (fecho transitivo) só com axiomas padrão; nenhuma fonte com `sorry`/`admit`/`axiom` | ✅ |
| T7 | enunciados reais ligados | 🟡 4/7 (RH e Beal oficiais; L1 e L2 construídas, revisão humana pendente; L3–L5 sem base na Mathlib) |
| T8 | produtores terminais incondicionais (os 7 portões) | ⬜ 0/7; faltam 16 termos (prova) / 10 (refutação) |
| T9 | só o verde é certificado: ensaio do portão completo, fiação tipada, nenhum terminal promovido | ✅ ensaio 12/12 · tipos 25/25 · sensibilidade ok |

Resultado: **biblioteca VERDE · conjecturas ABERTAS**. O CI publica isso numa anotação
`PLANO T1–T9`.

### Sobre a análise colada

* "M-Core/main usa Lean 4.19.0, a biblioteca usa 4.34.1": verdade para a raiz (`lean/MCore`), mas o
  `atk-kernel/` **já é** o projeto Lake independente que a análise recomenda (lakefile, toolchain e
  workflow próprios). Não há o que integrar no núcleo para certificar; T3 e T4 estão fechadas.
* "Falta o ZIP final de 30 módulos ATK-T1": esse pacote não está em nenhum dos repositórios
  acessíveis nem nos ramos do M-Core (busca nos clones locais dos 89 repositórios e em 227 ramos). O
  conteúdo descrito (intervalos certificados, estados de evidência, consistência relativa) já está
  formalizado e certificado em `ATK/AlgebraTerminal.lean` (63 teoremas). Para integrar o pacote quando
  ele for anexado, há `scripts/integrar_biblioteca.py PACOTE.zip T1 --aplicar`: recusa `sorry`,
  `admit`, `axiom`, outra versão do Lean ou nomes com apóstrofo; reescreve os `import` para `ATK.T1.…`,
  acrescenta `#print axioms` e registra tudo no auditor (testado com um pacote sintético).
* "T6: auditar `#print axioms` e dependências transitivas": `#print axioms` já devolve o fecho
  transitivo; `audits/axioms.txt` congela o resultado por teorema (832/839 verificados também neste
  ambiente; os 7 restantes dependem da Mathlib inteira e são certificados pelo CI).

### Trabalho da sessão paralela — integrado em 14/10/2026

Os seis ramos certificados da sessão paralela foram fundidos em `conditional` (só uniões de listas e
fusão campo a campo do JSON, sem conflito de conteúdo): `CongruentBijection`, `BridgeReduction`,
`TeoremaGlobal`, `FatoresQuarticos`, `FreyBealResidual`, `Roda`, `FronteiraUm`, `LimitesUm`,
`OscilacaoHiperreal`, `HypothesisCalculus`, `MellinPlancherel`, `PlancherelL1L2`, `EspectralDN`,
`NecessidadeBD`, `BDDistSqPort`, `BorderPrimes`, `ObrigacoesMinimas`, **`LigacaoNS`** e
**`LigacaoPNP`** (+204 teoremas; ver `FECHAMENTO.md` e `LIGACOES.md`). Efeito no verde universal:

* **L1 construída** (`ATK.LigacaoNS.modeloNS`, `clayA_iff`: o enunciado paramétrico ⟺ enunciado (A)
  do Clay). A peça `LIGACAO_L1` do portão de NS está preenchida — os termos que faltam passam de
  **19 para 18**. O status fica `CONSTRUIDA_NO_KERNEL` até a **revisão humana** das definições; só
  então vira `CLOSED` e o contador de ligações cai para 4/5.
* **L2 parte 1** (`ATK.LigacaoPNP`): P e NP sobre `Turing.FinTM2` da Mathlib, enunciado fiel
  `classeP ≠ classeNP`. Falta a composição de máquinas em tempo polinomial e a linguagem SAT.
* `ObrigacoesMinimas.closedMath_minimo` dispensa a ponte B2 (Beal entra pela forma residual de
  descida), o mesmo que `FinalRoot.verde_fiel_iff` mostra para a parte fiel.
* `NecessidadeBD`: a direção RH ⇒ `D_N → 0` reduzida a duas entradas analíticas nomeadas.

## Resolução: prova **ou** refutação

O Clay aceita como solução tanto a prova quanto a refutação (para Navier–Stokes, `¬(A)` implica o
enunciado (C), colapso com `f = 0`); o mesmo vale para RH, P vs NP, Hodge, BSD e para Beal. O
auditor agora reconhece as duas rotas:

* cada linha tem um portão de **refutação** `ATK/Terminal/<Linha>Refutacao.lean ::
  theorem refutacao : ¬ <enunciado>`, com as mesmas exigências (sem hipóteses, axiomas padrão,
  tipo elaborado = negação do enunciado oficial);
* estado por linha: **PROVADA**, **REFUTADA**, **ABERTA** ou **INCONSISTENTE** (prova e refutação
  certificadas ao mesmo tempo — só possível com base inconsistente; zera o verde e a raiz);
* `UNIVERSAL_GREEN` continua sendo as 7 linhas PROVADAS; o novo contador **RESOLVIDAS** soma
  provadas e refutadas.

As ligações viraram módulos próprios (`terminal-templates/<Linha>Modelo.lean.tpl`), usados pelos dois
portões, de modo que prova e refutação falam do mesmo objeto. Fiação: **21/21 modelos de portão
compilam**; rota da prova: faltam **18** termos; rota da refutação: **12** (7 refutações + 5 termos de
ligação). Ensaio do portão: **12/12** (inclui "linha refutada conta como resolvida, não como verde" e
"refutação por axioma próprio é rejeitada").

## A árvore

```
FINAL_ROOT  (ATK/ClosedMathGate.lean :: closed_math, sem hipóteses)
└── UNIVERSAL_GREEN  (7 portões terminais, scripts/terminal_gates.json)
    ├── VERDE FIEL = RH ∧ Beal  (enunciados oficiais, sem modelo)
    │   ├── RH    portão ATK/Terminal/RH.lean    :: terminal : RiemannHypothesis
    │   │         ponte B1 ✅ (provada no kernel)
    │   │         produtor: IsEmpty ZeroFora  (⟺ RH, riemann_iff_vazio)
    │   └── Beal  portão ATK/Terminal/Beal.lean  :: terminal : BealConjecture
    │             pontes B2 (Fermat, Wiles) e B8 (Darmon–Merel): publicadas, não formalizadas
    │             produtor: ExclusaoResidualFinal  (83,21 % dos expoentes 3..200)
    └── PARAMÉTRICAS (exigem também a ligação ao objeto real)
        ├── NS     ponte B3 · produtor O3 EnstrophyAPrioriBound · ligação L1
        ├── P≠NP   ponte B4 · produtor O4 SATNotInP          · ligação L2
        ├── Hodge  ponte B5 · produtor O5 MiddleCodimension  · ligação L3
        ├── BSD    ponte B6 · produtores O6 RankOpen, O7 RefinedOpen · ligação L4
        └── YM     ponte B7 · produtor O8 ConstructiveYM4D   · ligação L5
```

## O que o kernel certifica — `ATK/FinalRoot.lean` (12 teoremas)

| teorema | conteúdo |
|---|---|
| `pontes_de_restantes` | B1 provada: as 7 pontes restantes reconstroem todas as pontes antigas |
| **`raiz_de_produtores`** | pontes restantes + produtores ⇒ `Raiz M` (os sete enunciados) |
| `raiz_implica_fiel` | a raiz contém o verde fiel |
| **`produtores_fieis_de_raiz`** | a raiz implica `IsEmpty ZeroFora ∧ ExclusaoResidualFinal` **sem pontes** — não há atalho |
| **`verde_fiel_iff`** | `RH ∧ Beal ⟺ IsEmpty ZeroFora ∧ ExclusaoResidualDescida`, **sem nenhuma hipótese** |
| `verde_fiel_iff_final` | sob B2 + B8: `RH ∧ Beal ⟺ IsEmpty ZeroFora ∧ ExclusaoResidualFinal` |
| `verde_fiel_de_produtores` | B2 + B8 + os dois produtores ⇒ verde fiel |
| `produtores_de_obrigacoes` | os produtores novos são mais fracos que as obrigações antigas (o alvo encolheu) |
| `rotas_RH` | `D_∞ = 0`, `UniformLogBound`, contração ⇒ RH; e `RH ⟺ IsEmpty ZeroFora` |
| `rota_contracao_morta` | o piso logarítmico exclui a rota de contração |
| **`ns_depende_do_modelo`**, **`pnp_depende_do_modelo`** | o enunciado paramétrico é verdadeiro num modelo e falso noutro: sem as ligações L1–L5, verde nas paramétricas não significaria nada |

## O auditor — `scripts/universal_green.py` + `scripts/terminal_gates.json`

Chamado pelo `check_axioms.py` em todo push. Para cada linha, o portão só acende se **todas** as
condições valem:

1. o arquivo do portão existe e compilou;
2. a fonte declara literalmente `theorem terminal : <enunciado> :=` — **sem hipóteses**;
3. `#print axioms` ⊆ `{propext, Classical.choice, Quot.sound}`;
4. nenhum `sorry`/`admit`/`axiom` na fonte;
5. nas linhas paramétricas, a ligação (L1–L5) está `CLOSED` no relatório.

`FINAL_ROOT` = SHA-256 do certificado terminal (fontes, portões, axiomas, commit) **só** quando as 7
linhas estão verdes **e** o portão de `CLOSED_MATH` passa; senão `null`. O resultado aparece no
relatório do CI e numa anotação `UNIVERSAL_GREEN false 0/7 · FINAL_ROOT null`.

Testado contra fraude: um portão `theorem terminal : RiemannHypothesis := by sorry` fica vermelho
(axioma `sorryAx`); um portão com hipótese (`theorem terminal (h : …) : BealConjecture`) fica
vermelho (não é o enunciado literal sem hipóteses).

## O que falta, por camada

| camada | itens | o que exige |
|---|---|---|
| pontes (literatura) | B2 Fermat, B3 Leray/BKM, B4 Cook–Levin, B5 Lefschetz (1,1), B6 Gross–Zagier–Kolyvagin, B7 Osterwalder–Schrader, B8 Darmon–Merel | formalizar teoremas **publicados**; B2 está em andamento no projeto de Buzzard (FLT em Lean); B8 depende de modularidade |
| ligações (fundações) | L1 NS 3D, L2 máquinas e classes P/NP, L3 ciclos e cohomologia de Hodge, L4 L-funções de curvas elípticas, L5 QFT 4D | construir os objetos reais na Mathlib; sem isso os enunciados paramétricos não são os do Clay |
| produtores (matemática nova) | `IsEmpty ZeroFora`, `ExclusaoResidualFinal`, O3–O8 | resolver os problemas; nenhuma formalização substitui isto |

Ordem possível, do mais próximo ao mais distante: formalizar pontes publicadas → construir as
fundações das ligações → atacar os produtores. Cada avanço muda os contadores automaticamente.

## A última milha — `atk-kernel/terminal-templates/`, `scripts/verificar_fiacao.py` e os 25 termos tipados

21 modelos de portão: as 7 linhas, as 7 refutações, os 5 módulos de ligação (`<Linha>Modelo`),
`VerdeFiel` e `ClosedMathGate`. Cada um tem a composição completa até o enunciado oficial e
**marcadores** no lugar do que falta (`PROVA_*`, `LIGACAO_*`).

**Os termos agora têm nome e tipo no kernel.** `ATK/Termos.lean` dá um nome Lean a cada
uma das **25 lacunas distintas**, com o tipo exato que o portão exige, e prova sem hipóteses o que já
se pode provar sobre cada uma (39 teoremas): `fecha` (lacunas → enunciado oficial), `exato` /
`decomposicao` (onde a lacuna é *equivalente* ao enunciado), `refutacao_iff` (a forma-testemunha do
contraexemplo) e o que uma refutação acarreta. O catálogo `scripts/termos.json` liga cada lacuna ao
seu nome; `verificar_fiacao.py` troca cada marcador por `(sorry : <tipo do catálogo>)` e compila os
21 modelos: **25/25 tipos conferidos** (23 lacunas abertas com `sorry` tipado, 2 preenchidas com o termo real). O teste de sensibilidade troca o tipo da ponte B3 pelo do
produtor O3 e a compilação falha, como deve. A ficha completa (24 componentes por termo) está em
[`TERMOS.md`](TERMOS.md), gerada por `scripts/termos.py --md`.

| | ocorrências abertas | lacunas |
|---|---|---|
| rota da prova | 16 | 13 provas (2 produtores RH/Beal, 5 pontes B3–B7, 6 produtores O3–O8) + 3 ligações (L3–L5) |
| rota da refutação | 10 | 7 refutações + as mesmas 3 ligações |
| abertas | **23** | 16 + 10 − 3 compartilhadas |
| preenchidas | **2** | `LIGACAO_L2`, `LIGACAO_L2_SAT` (ligação L2 construída) |

Antes da L2 eram 18 + 12 − 5 = 25: as contagens "18 + 12" do CI e "25" do inventário de lacunas
estavam certas e mediam coisas diferentes.

O que os teoremas novos dizem sobre as lacunas:

* **exatas** (a lacuna não pede mais do que a conjectura): RH (`IsEmpty ZeroFora` ⟺ RH), Beal
  (`ExclusaoResidualDescida` ⟺ Beal), Hodge (`HodgeConjecture M` ⟺ B5 ∧ O5), BSD
  (`BSDFull M` ⟺ B6 ∧ O6 ∧ O7) e P vs NP dada a ponte (O4 ⟺ P ≠ NP). `ATK.Termos.raiz_iff` junta
  tudo;
* **formas-testemunha da refutação**: um zero `s` de ζ não trivial, `s ≠ 1`, `Re s ≠ 1/2`; uma
  solução primitiva de Beal, e basta procurá-la no residual da descida com `a`, `b` coprimos
  (`Beal.refutacao_iff_residual`); um dado de Schwartz sem solução global, que com B3 dá a explosão
  da enstrofia, o enunciado (C) do Clay (`NS.colapso_de_refutacao`); SAT ∈ P dada a ponte; uma classe
  de Hodge não algébrica, que com B5 está forçosamente em codimensão do meio e dim X ≥ 4
  (`Hodge.refutacao_meio`); uma curva com postos diferentes, que com B6 tem posto analítico ≥ 2;
* **critério de fidelidade da L2**: `PNP.FielL2 M` (as classes do modelo são P e NP sobre
  `Turing.FinTM2`, a menos de bijeção) implica `PneNP M ⟺ ATK.LigacaoPNP.PneNP`
  (`PNP.pneNP_de_fiel`). Quem construir o modelo da L2 só precisa provar `FielL2`; nenhum modelo com
  finitas linguagens passa (`PNP.finito_nao_fiel`).

O que continua faltando é exatamente a matemática: 8 produtores (O1–O8), 5
pontes publicadas por formalizar (B3–B7) e 3 ligações por construir (L3–L5, sem base na Mathlib);
L1 e L2 estão construídas, falta a revisão humana. Em P vs NP a composição em tempo polinomial, P ⊆ NP,
as reduções de Karp e SAT já estão no kernel; falta Cook–Levin (B4) e SAT ∉ P (O4).

### Mineração de 14/10/2026

Todos os 250 repositórios do catálogo estão cobertos (224 com conteúdo, 26 vazios, nenhum sem
acesso; ver [`INVENTORY.md`](INVENTORY.md)). Desde a varredura de 13/10 só o M-Core recebeu
commits; ele foi varrido de novo em todos os 223 ramos: 38 declarações novas que concluem um alvo,
todas do próprio `atk-kernel` já em `main` (17 equivalências ou implicações, 21 condicionais com
hipóteses explícitas). Os 10 repositórios privados com arquivos de prova que antes estavam fora
de alcance foram reconferidos ramo a ramo: as 5 declarações Lean e as 6 em Coq/Isabelle que miram
um alvo têm `sorry`, `Axiom`, `Admitted` ou hipóteses. Os três repositórios com nome `.lean`
(`zeta-i-formal.lean`, `i-foundations.lean`, `collapse-lemma-rh.lean`) só têm licença e protocolo.
**Nenhum termo de prova novo** para qualquer das 25 lacunas.

## Ligação L2 construída — `ATK/ComposicaoTM2.lean` (26) + `ATK/ModeloPNP.lean` (22)

A peça que faltava na fundação de P vs NP, e que a Mathlib não tem, está provada: a **composição de
máquinas `FinTM2` em tempo polinomial** (`ATK.ComposicaoTM2.comp`). Com ela: `P ⊆ NP` sobre
`Turing.FinTM2` (`P_sub_NP`, via um decodificador de pares construído e verificado passo a passo),
reduções de Karp e P fechada por elas (`P_fechada_red`), SAT (CNF satisfatíveis em binário) e a
instância `modeloPNP : ComplexityModel` com `fiel : PneNP modeloPNP ↔ ATK.LigacaoPNP.PneNP`. O
modelo de portão `PNPModelo` está preenchido e compila sem axioma extra: no portão de P vs NP
faltam só a ponte B4 (Cook–Levin neste modelo) e o produtor O4 (SAT ∉ P). Detalhes em
[`LIGACOES.md`](LIGACOES.md). A ligação fica `CONSTRUIDA_NO_KERNEL` até a revisão humana.

## Rota RH: captura relativa acumulada — `ATK/CapturaRH.lean` (15 teoremas)

A obrigação proposta como "próxima" na rota de Riemann foi testada no kernel, sobre a família
genuína `D_N = inf_c ‖χ − Σ_{k≤N} c_k ρ_k‖²`, com `q_N = D_N − D_{N+1}` e `η_N = q_N / D_N`:

| teorema | enunciado | hipóteses |
|---|---|---|
| `passo` | `D_{N+1} = (1 − η_N) · D_N` | nenhuma |
| `produto` | `D_N = D_0 · ∏_{j<N} (1 − η_j)` | nenhuma |
| `telescopio` | `D_N = D_0 − Σ_{j<N} q_j` | nenhuma |
| `le_exp` | `D_N ≤ D_0 · exp(−Σ_{j<N} η_j)` | nenhuma |
| `captura_suficiente` | `Σ_{j<N} η_j ≥ log log(N+2) − C` ⇒ O1 (`D_N ≤ D_0 e^C / log(N+2)`) | a cota de captura |
| `captura_log_iff` | O1 ⟺ `Σ_{j<N} −log(1 − η_j) ≥ log log(N+2) − C` | `D_N > 0` |
| `riemann_de_captura` | `Σ_{j<N} η_j ≥ log log(N+2) − C` ⇒ **RH** (pontes todas no kernel: O1 ⇒ `D_N → 0` ⇒ RH) | a cota de captura |
| `positiva_de_piso` | piso BBLS ⇒ `D_N > 0` para todo `N` | `PisoLog` |
| `captura_teto` | piso BBLS ⇒ `Σ_{j<N} −log(1 − η_j) ≤ log log(N+2) + C` | `PisoLog` |

Conclusão verificada: a "cota inferior acumulada dos decrementos relativos", na forma exata
(logarítmica), **é a própria obrigação O1** (`captura_log_iff`), não uma redução dela; e a cota
implica RH com todas as pontes já certificadas (`riemann_de_captura`). Provar a cota é, portanto, pelo
menos tão difícil quanto RH. Sob o piso de
Báez-Duarte–Balazard–Landreau–Saias a captura acumulada fica presa em `log log N + O(1)`
(`captura_teto`): nenhuma rota pode capturar mais rápido, o que reconfirma `contracao_impossivel`.
A forma linear `Σ η_j` é só suficiente. A lacuna exata continua sendo
`∃ C, ∀ N, Σ_{j<N} −log(1 − η_j) ≥ log log(N+2) − C` para a família genuína, e nenhuma dedução
incondicional dela é conhecida.

## Auditoria dos pacotes ATK30 V3–V12 anexados (14/10/2026)

Oito ZIPs (`ATK30_audit_v3`, `ATK30_full_structure`, `ATK30_source_reconciled_v5`,
`ATK30_v6_source_matrix`, `ATK30_v7_connections`, `ATK30_v8_exact_inventory`,
`ATK30_v10_terminal_research`, `ATK_Omega_V12`) com 25 arquivos Lean distintos, declarados para
Lean 4.22.0 e nunca compilados (`BUILD_PENDING`). Compilados aqui com Lean 4.34.1 e a Mathlib
v4.34.1, cada teorema auditado com `#print axioms`:

* sem correção: **17/23 módulos** compilam; **60/69 teoremas** só com os axiomas padrão;
* três erros genuínos, de uma linha cada: `ATK30.equalityDefect_zero_iff` e
  `ATK30.squareDefect_zero_iff` (`simp` deixa `a − b = 0 ↔ a = b`; falta `sub_eq_zero`) e
  `ATKOmega.absorption_example_*` (`decide` não reduz aritmética de `ℚ`; `decide +kernel`
  resolve); com esses três ajustes, **22/23 módulos e 69/69 teoremas**;
* o agregador `ATK30.lean` não compila em versão nenhuma: `ATK30.Registry` e `ATK30.Candidates`
  declaram os mesmos nomes (`ATK30.proof_16`, …);
* conteúdo: lógica proposicional (contraposição, conjunção, exclusão prova/refutação), defeitos
  pontuais e aritmética de exemplos. Os teoremas de "fechamento" do V10 (`rh_closure`,
  `pnp_closure`, …) quantificam sobre proposições arbitrárias (`rh : Prop`), sem ligação com
  `RiemannHypothesis` ou com os outros enunciados. Nenhum toca uma das 25 lacunas.
* números: os valores de `VALORES_CALCULADOS.csv` que são exemplos batem com o kernel
  (`ModelosSete.D2_modelo` = 5/6, com `b = (1/2, 1/2)`; `absorcao_modelo`; `Hb_det` = 5); as
  observações `D_N·log N` são numéricas, não cotas.

Nada dos pacotes foi incorporado ao `atk-kernel`: o que é válido já está certificado aqui
(`ATK.Termos`, `ATK.AlgebraTerminal`, `ATK.ModelosSete`), e o restante não é matemática terminal.

## O ensaio — `scripts/ensaio_universal_green.py`

Uma rodada de ponta a ponta com enunciados de **brinquedo** (`AlvoRH := 2 + 2 = 4`, …), compilada de
verdade pelo Lean numa pasta temporária, com registro próprio. **10/10 cenários corretos**:

| cenário | resultado |
|---|---|
| todos os portões válidos | `UNIVERSAL_GREEN = true`, 7/7, `FINAL_ROOT = 635a8528…` |
| `sorry` | vermelho (`sorryAx`) |
| sombreamento (`def AlvoRH := True` no namespace do portão) | vermelho (tipo elaborado ≠ enunciado oficial) |
| hipótese no teorema terminal | vermelho (não é o enunciado literal sem hipóteses) |
| axioma próprio | vermelho |
| enunciado trocado (`True`) | vermelho |
| ligação aberta | vermelho |
| erro de compilação | vermelho |
| portão ausente | vermelho |
| sete linhas verdes sem o portão de `CLOSED_MATH` | `UNIVERSAL_GREEN = true`, `FINAL_ROOT = null` |

O ensaio não prova nenhuma conjectura: prova que a máquina acende quando — e só quando — há provas.

## O instalador — `scripts/instalar_portao.py LINHA`

Monta um portão real a partir de um arquivo `ATK/Terminal/<LINHA>.lean`: recusa se faltar o arquivo,
se restar marcador, `sorry`, `admit` ou `axiom`, se não compilar, se os axiomas saírem do padrão ou se
o tipo elaborado não for o enunciado oficial; se passar, registra o `import` e os teoremas. Rodado
hoje nas nove linhas: **9 recusas** ("não existe; nada instalado"), com a lista de peças de cada uma.
Testado com um portão de `sorry` (recusado) e com sombreamento de `RiemannHypothesis` (recusado).

## Brechas encontradas e fechadas nesta etapa

* **Sombreamento de nomes**: o auditor conferia o enunciado pelo texto da fonte; um portão podia
  definir `RiemannHypothesis := True` no próprio namespace e passar. Agora todo portão é checado pelo
  **tipo elaborado**: `example : _root_.<enunciado oficial> := <teorema>` precisa compilar.
* **Portão de `CLOSED_MATH`**: o `check_axioms.py` não olhava o enunciado do `closed_math` — um
  `theorem closed_math : True` teria acendido `CLOSED_MATH`. Agora ele exige o tipo
  `ATK.FinalRoot.Raiz ATK.ClosedMathGate.modelos`.
* **Obrigações**: o fechamento automático de uma obrigação (como B1) também passou a exigir o tipo
  elaborado, além do texto.
* **Auditoria de `ATK/Terminal/`**: o laço do CI só compilava `ATK/*.lean` e `ATK/Conditional/*.lean`;
  um portão em `ATK/Terminal/` nunca teria log. O laço agora inclui `ATK/Terminal/*.lean`.

## Por que não criei os portões nem um `FinalRoot` com `sorry`

Os arquivos `ATK/Terminal/*.lean` e `ATK/ClosedMathGate.lean` **não existem** de propósito: criar
qualquer um deles exigiria uma prova sem hipóteses de um problema aberto. Um esqueleto com `sorry`
ou um axioma com a conclusão seria um certificado falso — e o auditor o rejeitaria. A estrutura está
pronta para receber as provas; o verde universal depende delas.
