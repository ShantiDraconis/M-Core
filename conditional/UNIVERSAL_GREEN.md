# Verde universal e raiz final — a estrutura completa do que falta

Esta é a árvore inteira do fechamento, montada no kernel e no auditor. Ela não prova nenhuma
conjectura. O que ela faz é tornar **exato** e **verificável por máquina** o que falta, e garantir
que `UNIVERSAL_GREEN` e `FINAL_ROOT` só mudem quando a matemática existir.

Estado calculado hoje: `UNIVERSAL_GREEN = false` · `FINAL_ROOT = null` · linhas verdes **0/7** ·
pontes no kernel **1/8** · produtores abertos **8/8** · ligações abertas **5/5** · fiação **21/21**
(rota da prova: faltam **18** termos) · ensaio do portão **12/12** · resolvidas **0/7**.

## As duas metas e o plano T1–T9 — `scripts/plano.py`

O verde universal tem duas metas diferentes, e o auditor agora calcula as duas separadamente a cada
push:

* **verde da biblioteca** (T1–T6 e T9): tudo compila, cada teorema usa só os axiomas padrão, as
  fontes estão congeladas, o projeto é isolado e o portão é fail-closed;
* **verde universal das conjecturas** (T7 e T8): os enunciados reais ligados e os produtores
  terminais provados.

| etapa | critério verificável | estado |
|---|---|---|
| T1 | todos os teoremas esperados certificados; SHA das fontes registrado | ✅ 839/839, `e8ed3b1b…` |
| T2 | `audits/provenance.json` tem o mesmo SHA das fontes atuais | ✅ congelado (`scripts/congelar.py`) |
| T3 | projeto Lake independente (`atk-kernel/`, lakefile e toolchain próprios) | ✅ |
| T4 | compatibilidade Lean 4.19.0 (raiz `lean/MCore`) ↔ 4.34.1 (`atk-kernel`) | ✅ resolvida por isolamento |
| T5 | `lake build`: todo arquivo auditado compila | ✅ |
| T6 | `#print axioms` (fecho transitivo) só com axiomas padrão; nenhuma fonte com `sorry`/`admit`/`axiom` | ✅ |
| T7 | enunciados reais ligados | 🟡 2/7 (RH e Beal oficiais; L1–L5 abertas) |
| T8 | produtores terminais incondicionais (os 7 portões) | ⬜ 0/7; faltam 19 termos |
| T9 | só o verde é certificado: ensaio do portão completo, nenhum terminal promovido | ✅ ensaio 10/10 |

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

## A última milha — `atk-kernel/terminal-templates/` e `scripts/verificar_fiacao.py`

Nove modelos de portão (`RH`, `Beal`, `NS`, `PNP`, `Hodge`, `BSD`, `YM`, `VerdeFiel`,
`ClosedMathGate`), cada um com a composição completa até o enunciado oficial e **marcadores** no
lugar do que falta (`PROVA_*`, `LIGACAO_*`). `verificar_fiacao.py` troca os marcadores por `sorry`,
compila os nove contra o build real e confere que o único axioma estranho é `sorryAx`.

Resultado (local e no CI): **9/9 modelos compilam; faltam exatamente 19 termos**:

| portão | termos que faltam |
|---|---|
| RH | `PROVA_DO_PRODUTOR` (`IsEmpty ZeroFora`) |
| Beal | `PROVA_DO_PRODUTOR` (`ExclusaoResidualDescida`, rota sem pontes) |
| NS | `LIGACAO_L1`, `PROVA_DA_PONTE_B3`, `PROVA_DO_PRODUTOR_O3` |
| P≠NP | `LIGACAO_L2`, `LIGACAO_L2_SAT`, `PROVA_DA_PONTE_B4`, `PROVA_DO_PRODUTOR_O4` |
| Hodge | `LIGACAO_L3`, `PROVA_DA_PONTE_B5`, `PROVA_DO_PRODUTOR_O5` |
| BSD | `LIGACAO_L4`, `PROVA_DA_PONTE_B6`, `PROVA_DO_PRODUTOR_O6`, `PROVA_DO_PRODUTOR_O7` |
| YM | `LIGACAO_L5`, `PROVA_DA_PONTE_B7`, `PROVA_DO_PRODUTOR_O8` |
| VerdeFiel, ClosedMathGate | nenhum: compilam assim que os sete portões existirem |

Ou seja: tudo o que não é matemática nova (ou fundação ausente da Mathlib) já está ligado e
verificado. Sobre L2: a Mathlib tem `Turing.TM2ComputableInPolyTime`, mas ainda não a composição de
máquinas de tempo polinomial, necessária para que P seja fechado por reduções.

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
