# Verde universal e raiz final — a estrutura completa do que falta

Esta é a árvore inteira do fechamento, montada no kernel e no auditor. Ela não prova nenhuma
conjectura. O que ela faz é tornar **exato** e **verificável por máquina** o que falta, e garantir
que `UNIVERSAL_GREEN` e `FINAL_ROOT` só mudem quando a matemática existir.

Estado calculado hoje: `UNIVERSAL_GREEN = false` · `FINAL_ROOT = null` · linhas verdes **0/7** ·
pontes no kernel **2/8** · produtores abertos **8/8** · ligações: **L1 e L2 fechadas** (titular,
14/10/2026), abertas **3/5** · fiação **21/21** · lacunas: **23 abertas e 2 preenchidas**,
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
| T1 | todos os teoremas esperados certificados; SHA das fontes registrado | ✅ calculado pelo CI a cada push (3084 esperados) |
| T2 | `audits/provenance.json` tem o mesmo SHA das fontes atuais | ✅ congelado (`scripts/congelar.py`) |
| T3 | projeto Lake independente (`atk-kernel/`, lakefile e toolchain próprios) | ✅ |
| T4 | compatibilidade Lean 4.19.0 (raiz `lean/MCore`) ↔ 4.34.1 (`atk-kernel`) | ✅ resolvida por isolamento |
| T5 | `lake build`: todo arquivo auditado compila | ✅ |
| T6 | `#print axioms` (fecho transitivo) só com axiomas padrão; nenhuma fonte com `sorry`/`admit`/`axiom` | ✅ |
| T7 | enunciados reais ligados | 🟡 4/7 (RH e Beal oficiais; L1 e L2 fechadas pelo titular; L3–L5 sem base na Mathlib) |
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
  **19 para 18**. Fechada (`CLOSED`) em 14/10/2026 pela revisão humana do titular; o contador de
  ligações abertas caiu para 4/5.
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
| pontes (literatura) | B2 Fermat, B3 Leray/BKM, B5 Lefschetz (1,1), B6 Gross–Zagier–Kolyvagin, B7 Osterwalder–Schrader, B8 Darmon–Merel (B1 Báez-Duarte e B4 Cook–Levin já provadas no kernel) | formalizar teoremas **publicados**; B2 está em andamento no projeto de Buzzard (FLT em Lean); B8 depende de modularidade |
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

O que continua faltando é exatamente a matemática: 8 produtores (O1–O8), 4
pontes publicadas por formalizar (B3, B5–B7) e 3 ligações por construir (L3–L5, sem base na Mathlib);
L1 e L2 estão fechadas (aprovação do titular). Em P vs NP a composição em tempo polinomial, P ⊆ NP,
as reduções de Karp, SAT e Cook–Levin (B4, `ATK.CookLevinNP.cookLevin`) já estão no kernel; falta
só SAT ∉ P (O4).

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

## Ligação L2 construída e fechada — `ATK/ComposicaoTM2.lean` (26) + `ATK/ModeloPNP.lean` (22)

A peça que faltava na fundação de P vs NP, e que a Mathlib não tem, está provada: a **composição de
máquinas `FinTM2` em tempo polinomial** (`ATK.ComposicaoTM2.comp`). Com ela: `P ⊆ NP` sobre
`Turing.FinTM2` (`P_sub_NP`, via um decodificador de pares construído e verificado passo a passo),
reduções de Karp e P fechada por elas (`P_fechada_red`), SAT (CNF satisfatíveis em binário) e a
instância `modeloPNP : ComplexityModel` com `fiel : PneNP modeloPNP ↔ ATK.LigacaoPNP.PneNP`. O
modelo de portão `PNPModelo` está preenchido e compila sem axioma extra: no portão de P vs NP
falta só o produtor O4 (SAT ∉ P): a ponte B4 (Cook–Levin neste modelo) está provada, ver abaixo. Detalhes em [`LIGACOES.md`](LIGACOES.md). Ligação fechada pelo titular em
14/10/2026.

## Ligação L4, parte do posto — `ATK/LigacaoBSD.lean` (4)

O enunciado de BSD do Clay está no kernel sobre os objetos da Mathlib (`WeierstrassCurve.LSeries`,
`E(ℚ)`): `ClayBSD`. A ponte para o modelo paramétrico (`posto_iff`) usa modularidade e Mordell–Weil
como hipóteses explícitas. Falta a fórmula refinada, exigida pelo portão `BSDFull`; ver
[`LIGACOES.md`](LIGACOES.md).

## Ponte B4 provada: Cook–Levin no modelo genuíno — marcos M1 e M2

Resultado: **`ATK.CookLevinNP.cookLevin : CookLevin modeloPNP SAT`**, axiomas padrão, sobre o
modelo da ligação L2 (`Turing.FinTM2`, reduções de Karp). O auditor fecha a obrigação B4 pelo
teorema `ATK.ObligationsClosed.B4`, cujo enunciado é literalmente o campo `lean` de B4 em
`scripts/obligations.json`. Pontes no kernel: **2/8** (B1 e B4). Observação: o campo `lean` de B4
era o nome do predicado paramétrico `ATK.Conditional.PvsNP.CookLevin`, que sozinho não é uma
proposição; ele foi instanciado no modelo da ligação L2 —
`ATK.Conditional.PvsNP.CookLevin ATK.ModeloPNP.modeloPNP ATK.ModeloPNP.SAT` —, que é exatamente a
ponte usada pela linha de P vs NP. A regra de fechamento (enunciado literal + certificado +
verificação de tipo) não mudou. P vs NP continua aberto: falta O4 (SAT ∉ P).

### Marco M1: SAT ∈ NP no modelo genuíno — `ATK/SATemNP.lean` (77)

A primeira metade de Cook–Levin está provada no kernel, sobre as classes de `ATK.LigacaoPNP`
(máquinas `Turing.FinTM2` da Mathlib) e a linguagem `ATK.ModeloPNP.SAT` da ligação L2:
`sat_em_NP : SAT ∈ classeNP`, com um verificador construído e verificado passo a passo.

* O certificado é **esparso**: pares (bits do índice, valor) só para as variáveis que ocorrem na
  fórmula, com `|c| ≤ |w|`. Um vetor denso de atribuição não serviria, porque os índices vêm em
  binário e o vetor teria tamanho exponencial.
* A busca filtra o certificado bit a bit enquanto lê o índice do literal; o valor de `n` é uma
  função de `(c, n.bits)`, então a atribuição é consistente por construção.
* O analisador confere a canonicidade dos índices e só aceita codificações `codCNF φ` (`forma`);
  sobre elas aceita exatamente quando toda cláusula tem um literal satisfeito (`acc_cnf`).
* A máquina `satTM` (4 pilhas, 18 rótulos) roda em no máximo `2 (n + 4)²` passos
  (`verifComputavel`).

Com isso, `cookLevin_iff : CookLevin modeloPNP SAT ↔ ∀ L ∈ classeNP, Red L SAT`: a ponte B4
no modelo genuíno é exatamente a NP-dificuldade de SAT, provada no marco M2 (abaixo).

Marco M2a — `ATK/CookLevinBase.lean` (16): a base genérica do tableau. Um passo de `TM2` só lê o
topo de cada pilha (`stepAux_topo`: com `prof q ≤ d`, o passo sobre `S` é o passo sobre `take d`,
com `drop d` intacto), as pilhas crescem no máximo `emp q` por passo, os símbolos empurrados formam
um conjunto finito (a `FinTM2` da Mathlib só exige alfabeto finito na pilha de entrada) e a execução
acolchoada de `T ≥ n` passos termina na configuração de parada.

Marco M2b — `ATK/CookLevinTableau.lean` (46): **o tableau de Cook–Levin para qualquer máquina
`TM2`**. A CNF tem cinco famílias: (E) exatamente um valor por célula, rótulo e estado; (I) a
linha inicial com até `Q` células livres de certificado; (R) as transições, uma por padrão de
janela; (P) parada fica parada; (A) aceitação. `tableau_iff` prova as duas direções: a fórmula é
satisfatível exatamente quando algum certificado faz a execução acolchoada de `T` passos parar
aceitando (`completo`; `base_correto` + `passo_correto`). A sanidade numa máquina concreta dá
"satisfatível" e "insatisfatível" nos dois casos esperados.

Marco M2c — `ATK/CookLevinReducao.lean` (23): **a redução como função pura** para toda
`L ∈ classeNP`. O tableau da `FinTM2` verificadora usa os símbolos alcançáveis, que formam um
conjunto finito. As variáveis viram números cujos bits são cadeias estruturadas (blocos unários),
e `reducao_iff : w ∈ L ⟺ reducao D T H w ∈ SAT`. Classicamente, toda linguagem se reduz a SAT por
alguma função não computável; o conteúdo aqui é a função explícita do tableau. O marco M2d prova
que ela é computável por uma `FinTM2` em tempo polinomial.

Marco M2d, parte 1 — `ATK/Fragmentos.lean` (10) + `ATK/Compilador.lean` (24): **um compilador
verificado de laços para `FinTM2`**. A linguagem tem registradores unários, emissão de bits,
somas, laços contados e laço sobre os bits da entrada. `comp_ok` prova que o código compilado
realiza a semântica em exatamente `custo` passos; `maq_run` cobre a máquina inteira, de `initList`
a `haltList`; e com `computavel`, custo polinomial dá `TM2ComputableInPolyTime`.

Marco M2d, parte 2 — `ATK/CookLevinLacos.lean` (71) + `ATK/CookLevinGerador.lean` (45) +
`ATK/CookLevinNP.lean` (51): **o gerador da redução e o fechamento de B4**.

* Fase aritmética (`arit`, `arit_spec`): `n = |w|`, `Q = q(n)`, `m = 2n+2+Q`, `T = p(m)` e as
  alturas do tableau, com ambiente final exato. `polyZ` soma `P(x)` a um registrador para qualquer
  `P : Polynomial ℕ`, por laços aninhados (`polyZ_spec`: semântica e custo).
* Emissão do tableau (`progE`, `progI`, `progR`, `progP`, `progA`): cada família da CNF impressa
  por laços contados; (I) lê a palavra de entrada por `forBits`; (R) percorre rótulos, estados e
  padrões de janela e imprime os consequentes com o resto das pilhas deslocado.
  `geraU_progTab`: a saída é exatamente `(formula …).flatMap cc`; `saida_gerador`: a saída do
  programa sobre `w` é `reducao D Tf Hf w`.
* Custo: programas de pura emissão custam e emitem no máximo `10·tam·(V+1)^(prof+1)` a partir de
  ambientes limitados por `V` (`cota_emis`); o bloco que lê a entrada é cotado à parte
  (`cota_progPre`); `Poli` (funções cotadas por polinômio, fechadas por soma, produto, potência e
  composição) dá `poli_custoTotal`.
* `maqRed`: o gerador compilado é `TM2ComputableInPolyTime cod cod`; `red_SAT`: toda
  `L ∈ classeNP` se reduz a SAT; **`cookLevin`**.

## Rodada de 15/10/2026 (noite, 2): FLT(19)

Continuação do pedido "prove tudo" (784 teoremas auditados, axiomas padrão).

* `ATK/FermatDezenoveBase.lean` (4): cota de Minkowski de `ℚ(ζ₁₉)` com parte inteira 105 933;
  `Φ₁₉`.
* `ATK/FermatDezenoveCertA.lean` … `CertE.lean` (558): um certificado por primo `p ≤ 105 933` com
  classe de norma `≤ 105 933` — 552 primos `≡ 1 (mód 19)`, `37, 113, 151, 227` (grau 2) e `7, 11`
  (grau 3). Cada certificado dá um gerador do ideal primo e as identidades do critério `pid6`,
  conferidas por reflexão em listas de inteiros (`ATK.PolyLista`) e `decide +kernel`. Os
  geradores foram achados fora do kernel por redução de reticulados (LLL exato).
* `ATK/FermatDezenove.lean` (218): `excecoes` — o kernel confere, em 106 blocos de mil, que todo
  `p ≤ 105 933` com potência `pⁱ ≤ 105 933`, `pⁱ ≡ 1 (mód 19)`, ou é certificado, ou é 1, ou tem
  divisor primo `≤ 325`; **`pid_dezenove`**: `𝓞(ℚ(ζ₁₉))` é principal; `regular_dezenove`;
  **`flt_dezenove`: FLT(19)**.
* `FermatRegular`: `flt_dezenove`, `flt_tres_a_vinte_e_dois` (FLT(n) para `3 ≤ n ≤ 22`) e
  **`flt_iff_irregulares`: `FermatLastTheorem ⟺` FLT para os primos irregulares `p ≥ 23`**. 19 é o
  último primo com `𝓞(ℚ(ζₚ))` principal; para 23, 29 e 31 (números de classes 3, 8, 9) é preciso
  calcular o grupo de classes.
* `BealFermatRegular`: `19 ∣ mdc(x, y, z)` também é incondicional; cobertura dos expoentes em
  `3..200`: **887.152 (11,43%)**.

Nenhum estado mudou: pontes no kernel **2/8**, produtores abertos **8/8**, ligações abertas **3/5**.

## Rodada de 15/10/2026 (noite): Fermat para primos regulares, `n = 5, 7, 11, 13, 17`

Continuação do pedido "prove tudo" (179 teoremas auditados, axiomas padrão).

### `ATK/FltRegular/` — o teorema de Kummer (formalização pública flt-regular)

Cópia do projeto **flt-regular** (<https://github.com/leanprover-community/flt-regular>, commit
`faae830`, Apache 2.0; Riccardo Brasca, Ruben Van de Velde, Chris Birkbeck, Eric Rodriguez, Andrew
Yang, Alex J. Best e colaboradores): FLT para todo primo ímpar regular (casos I e II, com o lema de
Kummer e Hilbert 90/92/94), e `3, 5, 7` regulares. Mudanças: só os `import` (`ATK.FltRegular.…`) e
uma adaptação à Mathlib v4.34.1 em `Hilbert92.lean` (`MulEquiv.monoidEnd`), igual à da versão
posterior do próprio projeto. Sem `sorry`/`axiom`/`native_decide`; detalhes em
`ATK/FltRegular/ORIGEM.md`.

### `FermatOnze` (7), `FermatTreze` (11), `FermatDezessete` (126), `PolyLista` (9) — novos

* Cotas de Minkowski: parte inteira 58 para `ℚ(ζ₁₁)`, 306 para `ℚ(ζ₁₃)` e 13 254 para `ℚ(ζ₁₇)`
  (limites de `π` da Mathlib).
* Primos abaixo da cota com classe de norma pequena: `23` (`n = 11`); `3` (grau 3) e
  `53, 79, 131, 157` (`n = 13`); para `n = 17`, `2` (grau 8), `67`, `101` (grau 2) e os 100 primos
  `≡ 1 (mód 17)` até 13 254. Para cada um, `certificado_p` exibe um gerador do ideal primo e as
  identidades polinomiais em `ℤ[X]` do critério `pid6` de flt-regular. Os geradores foram achados
  fora do kernel (busca e redução de reticulados) e só conferidos dentro dele: por `ring` para 11 e
  13; para 17, por reflexão (`ATK.PolyLista`: `poly_soma`, `poly_produto`, `igual_de_listas`) e
  `decide +kernel` sobre listas de inteiros.
* `FermatDezessete.excecoes`: o kernel confere (por cálculo, em blocos de mil) que todo
  `p ≤ 13 254` com alguma potência `pⁱ ≤ 13 254`, `pⁱ ≡ 1 (mód 17)`, ou está entre os 103
  certificados, ou é 1, ou tem divisor primo `≤ 115`.
* **`pid_onze`, `pid_treze`, `pid_dezessete`**: `𝓞(ℚ(ζₚ))` principal; `regular_*`;
  **`flt_onze`, `flt_treze`, `flt_dezessete`: FLT(11), FLT(13) e FLT(17)**.

### `ATK/FermatRegular.lean` (15) — ponte B2

* `flt_primo_regular`, `flt_cinco`, `flt_sete`, `flt_onze`, `flt_treze`, `flt_dezessete`,
  `flt_tres_a_dezoito` (FLT(n) para `3 ≤ n ≤ 18`).
* **`flt_iff_irregulares`: `FermatLastTheorem ⟺ ∀ p primo, p ≥ 19, p irregular ⇒ FLT(p)`.** O
  primeiro primo irregular é 37. Para 19 o mesmo método serve (cota ≈ 105 933, ≈ 600
  certificados); de 23 em diante `𝓞(ℚ(ζₚ))` não é principal e é preciso calcular o número de
  classes.

### `ATK/BealFermatRegular.lean` (11) — produtor O2, residual incondicional

* Beal sem pontes quando `d ∣ mdc(x, y, z)`, `d ∈ {5, 7, 11, 13, 17}` (`beal_mdc_regular`), e
  `BealConjecture ↔ ExclusaoResidualRegular` (`beal_iff_residual_regular`). Cobertura incondicional
  dos expoentes em `3..200`: 799.326 → **886.236** (10,30% → **11,42%**). Esses triplos têm
  `mdc ≥ 5`, fora do domínio de O2; sob B2 já estavam cobertos.

Nenhum estado mudou: pontes no kernel **2/8** (B2 parcial: faltam os primos irregulares),
produtores abertos **8/8**, ligações abertas **3/5**.

## Rodada de 15/10/2026 (tarde): posto `≥ 2` por 2-descida e `A⁶ + B⁶ ≠ C²`

Continuação do pedido "prove tudo" (39 teoremas, axiomas padrão).

### `ATK/PostoDois.lean` (28) — produtor O6, lado algébrico

`PostoDois` usa o
homomorfismo de descida `φ` de `MordellWeilDois` para dar **cotas inferiores** do posto de
Mordell–Weil (o lado algébrico do produtor O6):

* `dois_torcao`: `E(ℚ)[2] = {O, T₁, T₂, T₃}` (`Tᵢ = (eᵢ, 0)`);
* `phi_torsao_mem`: se `|φ(E[2])| = 4`, `φ` leva toda a torção em `φ(E[2])` — a torção é finita
  (`finite_torsion`, Mathlib) e `|φ(T)| ≤ |T/2T| = |T[2]| ≤ 4` (`card_quot_dois`);
* `independentes`, `posto_ge_dois`: se `φ(P₁)`, `φ(P₂)`, `φ(P₁) + φ(P₂)` estão fora de `φ(E[2])`,
  então `mP₁ + nP₂` de torção força `m = n = 0`, logo `postoMW E ≥ 2`; `posto_ge_um`, `nao_torsao`
  para um ponto; `card_imT`, `fora`: as condições reduzem-se a "não é quadrado em `ℤ`" para as
  classes `[x − e₁]`;
* **`posto_R30`: `y² = x(x + 30)(x + 2)` tem posto `≥ 2`** (`(−20, 60)` e `(−16, 56)`;
  classes `1, 15, −30, −2` para a 2-torção e `−5, −1, 5` para `P₁, P₂, P₁ + P₂`), e
  `infinito_R30`: `E(ℚ)` é infinito;
* `posto_R6`: `y² = x³ − 36x` (número congruente 6) tem posto `≥ 1`, com o ponto `(−3, 9)`.

O6 pede a igualdade posto = posto analítico para posto analítico `≥ 2`, o que exige a ordem de
anulação de `L(E, s)` em `s = 1` — fora de alcance.

### `ATK/DarmonMerelSeis.lean` (5) — ponte B8, expoente 6

* **`dmSq_seis`: `A⁶ + B⁶ ≠ C²`** para `A, B > 0` coprimos (Euler). Um dos dois é par (mód 4);
  `(A³, B³, C)` é uma tripla pitagórica primitiva (`coprime_classification'`, Mathlib):
  `A³ = M² − N²`, `B³ = 2MN`; `M ∓ N` coprimos de produto `A³` são cubos `s³`, `t³` (`cubo`) e o
  fator par de `MN = 4B₁³` é `4u³` (`par_cubo`); então `s³ + t³ = (2u)³` ou `s³ + (2u)³ = t³`,
  contra FLT(3) (`fermatLastTheoremThree`, Mathlib).
* `darmonMerel_iff_reduzido`: a ponte B8 equivale a `C²` com `n = 9` ou primo `≥ 5` e `C³` com
  `n = 4` ou primo `≥ 5` (antes: também `n = 6`). Os casos primos são Darmon–Merel (modularidade).

### `ATK/BealSeisSeisDois.lean` (6) — produtor O2, residual

* `sem_solucao_662`, **`beal_662`**: Beal vale incondicionalmente para todo triplo com `6 ∣ x`,
  `6 ∣ y`, `2 ∣ z` (de `dmSq_seis`; se `a, b` têm primo comum, ele divide `c`). Triplos com
  `mdc(x, y, z) = 2` fora das famílias já certificadas: `(6, 6, 4)`, `(6, 12, 10)`, `(18, 6, 14)`
  (`exemplos_662`, `exemplos_662_novos`).
* `beal_iff_residual_seis`: `BealConjecture ↔ ExclusaoResidualSeis`, sem pontes — o produtor O2
  (`ExclusaoResidualDescida`) equivale ao residual menor (`descida_iff_seis`). Cobertura
  incondicional dos triplos de expoentes em `3..200`: 762.844 → **799.326** (9,83% → **10,30%**).

Nenhum estado mudou: pontes no kernel **2/8**, produtores abertos **8/8**, ligações abertas **3/5**.

## Rodada de 15/10/2026 (manhã): Mordell–Weil e o primeiro caso de FLT para `p < 300`

Pedido do titular: provar tudo o que é provável. Os produtores O1–O8 continuam sem prova conhecida
(nenhum arquivo honesto pode fechá-los); estes são os dois maiores teoremas verdadeiros ao alcance,
170 teoremas novos, axiomas padrão:

* **`ATK/MordellWeilDois.lean` (37) — teorema de Mordell–Weil para `y² = (x − e₁)(x − e₂)(x − e₃)`**
  (`eᵢ ∈ ℤ` distintos; toda curva sobre `ℚ` com 2-torção racional completa é isomorfa a uma destas).
  2-descida completa sobre o grupo de pontos da Mathlib: o homomorfismo
  `φ : E(ℚ) → (ℚˣ/ℚˣ²)²`, `P ↦ ([x − e₁], [x − e₂])` (`phi`, via a identidade da reta de
  `addPolynomial_slope`), `ker φ ⊆ 2E(ℚ)` com a fórmula explícita de divisão por 2 (`metade`,
  `nucleo_le`), imagem finita pela paridade das valuações `p`-ádicas (`par_x_menos_e`,
  `finito_phi`); daí **Mordell–Weil fraco** (`mordellWeil_fraco`), **Mordell–Weil**
  (`mordellWeil`, pela descida da Mathlib) e `posto_finito`. Efeito na ligação L4: a hipótese
  `MordellWeil` deixa de ser necessária para essa família.
* **`ATK/GermainLegendre.lean` (133) — primeiro caso do último teorema de Fermat para todo primo
  ímpar `p < 300`** (`flt_caso_um_menor_300`): o critério de Germain–Legendre com um primo
  auxiliar `q = 2kp + 1` (`germain`), e para cada um dos 61 primos ímpares abaixo de 300 o
  kernel confere o seu `q` (até 9767) por `decide`. `flt_iff_caso_dois`: para esses `p`,
  FLT(p) ⟺ o segundo caso (`p ∣ xyz`). Efeito na ponte B2: o que falta para `p < 300` é só o
  segundo caso.

Nenhum estado mudou: pontes no kernel **2/8**, produtores abertos **8/8**, ligações abertas **3/5**.

## Rodada de 15/10/2026: avanço certificado em todos os itens abertos

Pedido do titular: tocar todos os itens que faltam. Cada item abaixo ganhou teoremas certificados
(axiomas padrão), em arquivos separados com testes de sanidade. **Nenhum estado mudou**: pontes no
kernel continuam **2/8**, produtores abertos **8/8**, ligações abertas **3/5** (estado das ligações
é decisão do titular). Total: 102 teoremas novos em 11 arquivos.

| item | arquivo (teoremas) | o que foi provado | o que continua faltando |
|---|---|---|---|
| L4 | `BSDInvariantes` (23) + `BSDRefinada` (16) + `BSDTamagawaE32` (5) | todos os invariantes da fórmula refinada sobre a Mathlib: `L^{(r)}(E,1)/r!`, Ω no modelo minimal global, torção (`ordemTorsao_E32 = 4`), altura de Néron–Tate com limite provado, paralelogramo exato, `ĥ(P) = 0 ⟺ P de torção`, emparelhamento bilinear, regulador (`regulador_E32 = 1`), Tamagawa pela redução da Mathlib (redução boa ⇒ `c_v = 1`), Ш por cohomologia de Galois contínua em todas as places; `FormulaRefinada`, `modeloCompleto`, `bsdFull_iff`; em `y² = x³ − x`, `c_p = 1` para todo `p ≠ 2` (`tamagawa_E32`) | a decisão do titular sobre a ligação; as hipóteses publicadas `Modularidade` e Mordell–Weil fraco |
| L3 | `HodgeToro` (10) | estrutura de Hodge de peso 1 de `H¹(ℂ/(ℤ + τℤ), ℚ)`, `H^{1,0} = ℂ·dz`, `h^{1,0} = 1` | cohomologia singular de variedades projetivas na Mathlib |
| L5 | `L5Lacuna` (4) | `GapAtLeast` com definição genuína sobre `Wightman` (energia `≥ Δ` em `Ω^⊥`), coerente com a condição espectral; a teoria trivial tem lacuna | `IsQuantumYM` (campos de calibre) |
| B2 | `SophieGermain` (12) | teorema de Sophie Germain; primeiro caso de FLT(5); FLT(5) ⟺ segundo caso | segundo caso; primos que não são de Sophie Germain |
| B3 | `NSExplosao.taxa_leray` | taxa de Leray: explosão em `T` ⇒ `y(t)² ≥ 1/(2b(T − t))` | existência local e continuação (não estão na Mathlib) |
| B5 | `HodgeFiltracao` (5) | classe de Hodge ⟺ vetor racional em `F^p` (Deligne); para `p = 1`, a parte linear de Lefschetz (1,1); `p_g = 0` ⇒ todo `H²` é de Hodge | a classe vir de um divisor (sequência exponencial) |
| B6 | `BSDRefinada.pontes_E32_iff`, `bsdFull_iff_fraco` | em `y² = x³ − x`, B6 ∧ O6 ⟺ posto analítico 0; Mordell–Weil fraco basta para a fidelidade | Gross–Zagier–Kolyvagin |
| B7 | `YMReconstrucao` (6) | reconstrução OS no modelo de rede: positividade de reflexão, vácuo único, lacuna do hamiltoniano = taxa de decaimento | o teorema para medidas em `ℝ⁴` |
| B8 | `DarmonMerelReducao` (9) | a ponte se reduz aos expoentes primos (mais 6, 9 em `C²` e 4 em `C³`); o resto está provado com a Mathlib | os casos primos (modularidade) |
| O3 | `NSExplosao.explosao_comparacao` | com `b·y₀² > a`, a comparação de Riccati explode em tempo finito: a desigualdade sozinha não dá O3 | informação estrutural de NS |
| O4 | `CircuitoExplicito` (10) | cota inferior explícita linear `n ≤ 2s + 1` (ex.: `OUₙ`), contra a cota de Shannon não construtiva | cota superpolinomial para uma família em NP |
| O5 | `HodgeFiltracao` | `Hdg^p = V_ℚ ∩ F^p` em toda codimensão | algebricidade |
| O6 | `BSDRefinada.pontes_E32_iff` | instância em `y² = x³ − x` | posto analítico ≥ 2 |
| O7 | `BSDRefinada`, `BSDTamagawaE32` | O7 no modelo completo é literalmente a fórmula refinada; em `y² = x³ − x` se reduz a `L(E,1) = Ω·c₂·#Ш/16` (o produto de Tamagawa é só o fator em 2) | a fórmula |
| O8 | `YMReconstrucao` | na rede: positividade de reflexão e clustering com taxa `m(β) > 0` | limite contínuo 4D não abeliano |
| O1 | — | nenhum teorema novo nesta rodada (o upstream integrou `ATKIBagchi`: `D∞ = 0` da família do texto ⇒ RH) | `D∞ = 0` |
| O2 | — | nenhuma família incondicional nova (reduções com a Mathlib esgotadas); a redução condicional por B8 ficou mais estreita | O2 |

**Estado calculado: UNIVERSAL_GREEN = false, linhas verdes 0/7, CLOSED_MATH = false.**

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
