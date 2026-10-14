# Millennium Conditional

> Neste branch do M-Core o código Lean está em `atk-kernel/` (raiz do repositório) e esta pasta
> `conditional/` guarda a documentação, o catálogo e a proveniência.

Pesquisa de Tiago Paschoalatto Fagliari (ORCID 0009-0006-6874-3910).

```
CONDITIONALS_CLOSED = 7/7    os 7 teoremas  hipótese → enunciado  estão provados no kernel
OPEN_MATH           = true   as 7 hipóteses abertas continuam sem prova
CLOSED_MATH         = false  nenhum dos 7 problemas foi resolvido
```

Cada problema do M-Core está escrito como um teorema condicional verificado no kernel do
Lean 4 + Mathlib:

```
PONTE (teoremas já publicados, ainda não formalizados)  →  HIPÓTESE ABERTA (o que falta)  →  ENUNCIADO
```

Pontes e hipóteses abertas entram como argumentos explícitos dos teoremas — nunca como
`axiom` —, então `#print axioms` deve mostrar só `propext`, `Classical.choice` e `Quot.sound`.
Um condicional verificado diz exatamente isto: *quem provar a hipótese aberta resolve o
problema*. Não diz que a hipótese é verdadeira.

## Os 7 condicionais

| Problema | Teorema Lean | Ponte (literatura) | Hipótese aberta | Enunciado |
|---|---|---|---|---|
| Riemann | `riemann_conditional` | Critério de Nyman–Beurling–Báez-Duarte: D_N → 0 ⇒ RH | ∃K, ∀N, D_N ≤ K/log(N+2) | OFICIAL (`RiemannHypothesis` da Mathlib) |
| Navier–Stokes | `ns_conditional` | Critério de explosão da enstrofia (Leray 1934) | Cota a priori da enstrofia em todo intervalo finito | PARAMÉTRICO |
| P vs NP | `pvsnp_conditional` | Cook–Levin: SAT é NP-completo | SAT ∉ P | PARAMÉTRICO |
| Hodge | `hodge_conditional` | Lefschetz (1,1) e Lefschetz difícil: p ≤ 1 ou p ≥ dim−1 | Codimensões 2 ≤ p ≤ dim−2 | PARAMÉTRICO |
| BSD | `bsd_conditional` | Gross–Zagier–Kolyvagin: posto analítico ≤ 1 | Posto analítico ≥ 2; fórmula refinada | PARAMÉTRICO |
| Yang–Mills | `ym_conditional` | Reconstrução de Osterwalder–Schrader | Construção 4D com axiomas OS e clustering exponencial | PARAMÉTRICO |
| Beal (não é do milênio) | `beal_conditional` | Último Teorema de Fermat (Wiles) | gcd(a,b,c) > 1 quando gcd(x,y,z) ≤ 2 | OFICIAL (elementar) |

Todos em `atk-kernel/ATK/Conditional/`, namespace `ATK.Conditional.<Problema>`.

**OFICIAL** — o enunciado usa só objetos da Mathlib e é o próprio problema.
**PARAMÉTRICO** — a Mathlib ainda não tem os objetos (soluções de NS, classe NP, cohomologia de
Hodge, função L de curvas elípticas, QFT construtiva). O enunciado é relativo a uma interface
(`NSModel`, `ComplexityModel`, …). O teorema vale para qualquer modelo; ele só fala do
problema real depois que os campos da interface forem ligados aos objetos verdadeiros.

### O que cada hipótese aberta significa

- **Riemann.** D_N = inf ‖χ − Σ_{k≤N} c_k ρ_k‖² em L²(0,∞), definido concretamente no arquivo.
  A cota K/log(N+2) é *mais forte* que RH. Evidência numérica (não prova):
  `numerics/dn_N1500_prec45.csv` dá D_N decrescente e D_N·log(N+2) ≤ 0,943 para N ≤ 1500
  (máximo em N = 1; 0,0457 em N = 1500).
- **P vs NP.** Também está certificado `pneNP_iff_sat_not_in_P`: dada a ponte, a hipótese aberta
  é *equivalente* ao problema. A condicional organiza, não encurta.
  No modelo do lane `m-core-p-vs-np`, SAT ∈ NP já está provado sem hipóteses (P01 fechado em 09/10,
  `PNPAfterP01.sat_in_np`); lá também só falta G2.1 = SAT ∉ P.
- **Beal.** Também certificado `beal_iff_gcdLowerBound`: a forma gcd do registro do M-Core é
  equivalente ao enunciado oficial. O ganho real é o corte por Fermat (gcd(x,y,z) ≥ 3 não tem solução).
- **Hodge.** O primeiro caso em aberto é uma variedade de dimensão 4 com p = 2.
- **Navier–Stokes.** A rota interna G5 do lane (S ≤ θνz + C·y², terminal `ActualNSToSignedGainCore`)
  foi refutada em 12/10 por escala (`ns_19_false`, M-Core `fix/ns-scaling-false`). A comparação de
  Riccati em `ATK.NavierStokes` também só dá cota local. A hipótese aberta segue aberta, sem rota ativa.

## Atualização de 13/10/2026 — estado dos seus repositórios

Conferido nas versões mais novas de hoje:

| Fonte | O que registra |
|---|---|
| M-Core `main` e os 4 branches mais recentes | `FinalProofRegistry`: 7 de 7 casos `openMath`, 0 `proved` |
| M-Core `fix/ns-scaling-false`, README de 12/10 | 8 enunciados mínimos abertos; "nenhuma conjectura do milênio foi provada" |
| M-Core `fix/ns-scaling-false`, `Correcao_20261012.lean` | rota G5 de Navier–Stokes refutada (`ns_19_false`) |
| `m-core-p-vs-np` `atk/p01-closure-audit-20261013-pnp-reduction` | SAT ∈ NP provado no modelo do lane; P ≠ NP reduzido a G2.1 (aberta) |

Os 8 enunciados abertos do seu README são as mesmas 8 obrigações O1–O8 daqui. Com o avanço do
P01, a ponte B4 passou a `PARCIAL_NO_MODELO_DO_LANE`: falta a NP-dificuldade e ligar o modelo do
lane (Lean 4.19) a este kernel (Lean 4.34.1).

## Busca de provas em todos os repositórios — `PROOF_SEARCH.md`

Varri 32 repositórios, 2.210 branches e 4.858 arquivos Lean atrás de qualquer prova que feche uma
obrigação. Das 688 declarações que concluem um alvo, 492 são condicionais, 108 são equivalências,
39 negações, 27 têm `sorry`/`exact ?_`, 12 dependem de `axiom` e 7 são auditorias de vacuidade.
As únicas 3 sem hipóteses são o P01 (SAT ∈ NP no modelo do lane). O `riemann_hypothesis` do
`millennium-riemann-I` depende dos axiomas `collapse_law` e `I_ne_one`, que juntos já são a própria RH.
Nenhuma das obrigações O1–O8 está fechada em nenhum lugar.

## Mapa de descarga de hipóteses — `HYPOTHESIS_MAP.md`

Das 334 hipóteses usadas pelos 491 teoremas condicionais limpos dos seus repositórios, só 6 já
estão provadas em algum branch. Cinco são da cadeia do P01 (SAT ∈ NP no modelo do lane P vs NP).
A sexta é nova: no lane Beal, `T59_allFourEliminator_proved` fecha o ramo do expoente 4 com o
FLT(4) da Mathlib, e Beal fica reduzido a **FLT para primos > 3** + **`T59ResidualEliminator`**.
Com isso a ponte B2 passou a `PARCIAL_NO_MODELO_DO_LANE`. Nenhuma obrigação aberta O1–O8 caiu.

## Inventário mestre de todos os repositórios — `INVENTORY.md`

Todos os branches de **224 repositórios** — todos os que têm algum commit; os 26 restantes do
catálogo estão vazios (tamanho 0 na API do GitHub). Nenhum ficou sem acesso: os 89 privados que faltavam
foram anexados (76 com commits, varridos; 13 vazios). São 4.086 branches e 65.049 arquivos distintos: 8.423 Lean, 791 Coq/Rocq,
253 Agda, 493 Isabelle, 6.963 Python, 2.300 LaTeX. Há 834 declarações Lean que concluem um alvo; as 135
sem hipótese explícita são 115 equivalências e 20 afirmações diretas, **cada uma lida**: firewalls, P01
(SAT ∈ NP no modelo), `RiemannHypothesis := True` local, ou provas que importam `axiom`s de outro
arquivo (`horizon-prime---framework`, `millennium-riemann-I`). Os 76 repositórios recém-varridos não
acrescentaram nenhuma: os achados Lean novos têm hipóteses (`harappan-universal-dictionary`, Yang–Mills,
arquivo com `sorry` e 7 `axiom`s) ou estão em arquivo com `sorry` (`universal`, `rh_equiv_xi`). Nos 552
enunciados de Coq/Agda/Isabelle, 453 estão em arquivos com `Admitted`/`Axiom`/`postulate`/`sorry`; os
outros são condicionais, equivalências ou `True`. As 32 alegações textuais de `CLOSED_MATH = true`
(14 repositórios; a nova é `clay_millennium_solved : p_equals_np → True` em `mishkan-iii-core`) não vêm
acompanhadas de termo que o kernel aceite.

## Os 2.440 teoremas auditados — `THEOREMS_2440.md`

Os 2.440 teoremas do `FINAL_PROOF_STRUCTURE` (inventários do kernel, um por lane) foram localizados
um a um no commit exato que o CI verificou e classificados pela forma lógica. Todos são CLEAN no
kernel. Mas **653 (27%) são projeções de campos `Prop` de estruturas** — hipóteses empacotadas, não
provas —, 299 são refutações/firewalls, 235 são fatos de registro, 141 são equivalências e só
**19 são condicionais que concluem um alvo; nenhum deles tem as hipóteses provadas pelos outros
2.440**. Os enunciados finais aparecem no relatório de proposições do próprio kernel como
`NO_PROOF_IN_LIBRARY`. Usados juntos, os 2.440 entregam as pontes e a infraestrutura dos modelos;
não produzem nenhuma das obrigações O1–O8.

## Indeterminações como pontos de 3 estados — `ATK/Indeterminacy.lean` · `INDETERMINACY.md`

A proposta do autor (cada indeterminação é um ponto com 3 estados; interações são pontos; o estado
é medido por L'Hôpital e a medida é uma constante) está formalizada e **certificada: 50 teoremas**.
Ponto = germe `a·tᵐ`; estados `zero / finito / infinito` pela ordem `m`; produto, quociente e
inverso fecham; no estado finito o quociente mede a constante `a/b`; L'Hôpital mede `0/0` como
`f'(0)/g'(0)`; `0⁰` mede a multiplicidade como `e^(−mc)`; `0/0` sozinho tem os 3 estados e qualquer
valor real. A constante `I = 0 ⊘ 0` existe numa extensão de ℝ, é absorvente, sem cancelamento e
não forma anel. Lógica de 4 estados sem explosão; `ClosedMath P ↔ P`.

O mesmo arquivo prova os limites: `RH_I_iff` (RH na extensão com `I` é RH — `I` não move zeros) e
`monotona_nao_basta` (decrescer não dá `D_N → 0`). Por isso o módulo é infraestrutura e não muda o
portão.

## Ponte B1 provada: `D_N → 0 ⇒ RH` — `RIEMANN_BRIDGE.md`

`ATK.BaezDuarteBridge.baezDuarteCriterion : BaezDuarteCriterion` está **certificado** (axiomas
padrão). A implicação de Nyman–Beurling–Báez-Duarte deixou de ser hipótese: ζ na faixa crítica por
`∫_1^∞ {t} t^{-s-1} dt` e princípio da identidade (`ZetaStrip`), Mellin de `{1/(k t)}`
(`MellinRho`), estimativa de Cauchy–Schwarz e equação funcional (`BaezDuarteBridge`). O auditor
marca a obrigação B1 como `CLOSED` por cálculo. A rota de Riemann depende agora só de **O1**
(`inf_N D_N = 0`), que continua aberta e é equivalente à própria RH.

Também novos: `RiemannStates` (9 — `D_N` só pode estar nos estados `zero`/`finito`; limite em
`[0,1)`) e `BealResidual` (5 — Beal ⟺ excluir soluções dois a dois coprimas com `3 ∤ mdc(x,y,z)`
e `4 ∤ mdc(x,y,z)`).

## Sete estados, dissipação e resultados incondicionais novos (94 teoremas)

Detalhes em `INDETERMINACY.md` §7–§10. Todos certificados com axiomas padrão:

- `ATK/IndeterminacyStates.lean` (34): 7 estados (`zero`, `finito`, `+∞`, `−∞`, `oscila`,
  `indeterminado`, `foraDominio`), ordem de informação, tabelas de composição corretas e monótonas,
  `0/0` realiza 5 estados, L'Hôpital preserva estado, teorema de dissipação total.
- `ATK/RiemannConcrete.lean` (11) + `ATK/RiemannFaithful.lean` (25): para a família concreta de
  Báez-Duarte, `D_N` decresce, `D_0 = 1`, **`D_1 < 1`**, `D_N → inf D_N < 1`, e todo integrando é
  integrável (a definição formal é a distância verdadeira). O1 ⟺ `inf_N D_N = 0`.
- `ATK/BealReduction.lean` (12) + `ATK/BealPartial.lean` (12): **Beal ⟺ nenhuma solução dois a dois
  coprima**; caso `a = b`; Beal para todo triplo de expoentes com `3 ∣ mdc` ou `4 ∣ mdc`
  (FLT(3), FLT(4) da Mathlib), sem a ponte de Fermat geral.

Nenhuma obrigação O1–O8 foi fechada por esses resultados; `CLOSED_MATH` continua `false`.

## A teoria de `I` materializada — `I_THEORY.md` (186 teoremas)

Levantamento de **tudo** o que os repositórios propõem sobre `I` (4.922 arquivos em 79 repositórios,
586 leis/hipóteses deduplicadas em `catalog/ilaws/`, cada uma com fonte e veredito) e formalização
do que é verdadeiro:

- `ATK/IFormas.lean` (53): `I` como conjunto de valores das formas indeterminadas —
  `0/0`, `0·∞`, `∞−∞` valem **qualquer** ponto de `[−∞,+∞]`; `∞/∞`, `1^∞`, `0^0`, `∞^0` valem
  exatamente `[0,+∞]`; as sete oscilam; as determinadas (`∞+∞`, `a/∞`, `0^∞`…) têm valor único.
- `ATK/IAlgebra.lean` (34): quais álgebras de `I` são consistentes (meadow absorvente com
  distributividade total; modelo multiestado de conjuntos) e quais são **inconsistentes** (PAX/`K_I`,
  P1, `I_invariant`, o triângulo absorção + `0·I = 0` + distributividade); Δ só existe nos hiper-reais.
- `ATK/IGeometria.lean` (56): início fechado e fim fechado convergem ao **mesmo** neutro `1/2`,
  meio-abertos ao vazio; tensão, compressão, tração, torção, rigidez do neutro, o torque `𝕋` do
  acervo, lógica K3 com o neutro `N ↦ 1/2`.
- `ATK/ZetaSimetria.lean` (43): a mesma geometria nos zeros de ζ — extremos fechados `Re s ≥ 1` e
  `Re s ≤ 0` livres de zeros não triviais, **`ζ(σ) < 0` em `(0,1)`** (o neutro `1/2` não é zero),
  simetria por tensão/espelho/torção, quartetos, e **RH ⟺ o fim fechado chega ao meio ⟺ o início
  fechado chega ao meio ⟺ todo zero é fixo pela torção**. Os extremos provados são `a = 1`, `b = 0`;
  o limite `a ↓ 1/2` é a própria RH (O1), aberta.

## As lacunas, problema a problema — `LACUNAS.md` (64 teoremas)

Teoremas intermediários que empurram a fronteira certificada (nenhum fecha um problema):

- **Riemann** (`ATK/ZetaRetangulo.lean`, `ATK/ZetaRegiao.lean`): `ζ(s) ≠ 0` se `|s − 1| < 2·Re s`;
  **nenhum zero na faixa com `|Im s| < √3/2`** (RH até essa altura); e **região sem zeros em toda
  altura**: todo zero não trivial tem `c(t) < Re s < 1 − c(t)`, `c(t) = 1/(256(9+4|t|)⁴(3+3|t|))`.
- **Riemann, região logarítmica** (`ATK/ZetaParcial.lean`, `ATK/ZetaLog.lean`,
  `ATK/ValleePoussin.lean`, 54 teoremas, `VALLEE_POUSSIN.md`): somas parciais de ζ, cotas
  `|ζ| ≪ log|t|` perto de `Re s = 1` e **`c(t) < Re s < 1 − c(t)` com `c(t) ≥ 1/(10⁹ log⁹(3|t|))`**
  para `|t| ≥ 4`; supera a largura `|t|⁻⁵` a partir de `|t| = 2000` (numericamente desde ≈ 31) e dá
  piso explícito à condensação de `D_N`.
- **Beal** (`ATK/BealFLT.lean`): com o Último Teorema de Fermat, **Beal ⟺ excluir soluções dois a
  dois coprimas com `mdc(x,y,z) ∈ {1, 2}`**.
- **P vs NP** (`ATK/Shannon.lean`): contagem de Shannon — existe função de `n` bits sem circuito com
  `≤ 2^n/(8n)` portas e existe família fora de `P/poly`; falta exibir uma em NP.
- **Navier–Stokes** (`ATK/NSPequeno.lean`): da desigualdade de enstrofia, dados pequenos ⇒ sem
  explosão e decaimento a zero; falta o modelo e o caso de dados grandes.
- **Yang–Mills** (`ATK/YMToy.lean`): rede solúvel com gap `m(β) = log coth β > 0` que fecha quando
  `β → ∞` — a dificuldade do limite contínuo, em miniatura.
- **BSD**: `E(ℚ)` de `y² = x³ − x` tem exatamente 4 pontos (módulo paralelo `CongruentCurve`); o caso
  geral precisa de L-funções (L4). **Hodge**: sem fundações na Mathlib (L3).

## Provado, refutado, lacuna — e os zeros fora da linha — `FICHAS.md` (35 teoremas)

- `ATK/ForaDaLinha.lean`: **RH ⟺ não existe zero fora da linha**; um zero fora da linha evita a
  reta, o eixo real, `|Im| < √3/2` e as bordas `c(t)`, vem em **quarteto** de 4 zeros distintos e
  **condensa**: força `D_N ≥ m(ρ)² > 0` para todo `N` (estado `finito`).
- `ATK/Fichas.lean`: para cada conjectura, a parte **provada**, uma parte **refutada** (reforço
  falso, provado `¬`) e a **lacuna** (`Riemann ⟺ lacuna`, `Beal ⟺ lacuna`); anti-produtos
  completos; parâmetro de **explosão** (`T*` explícito para dados grandes na desigualdade de
  enstrofia), limiar crítico, e `FLT ⟺ FLT para primos ≥ 5`.

## Álgebra de terminais, modelos das sete linhas e álgebra triádica — `MODELOS_TERMINAIS.md` (171 teoremas)

- `ATK/AlgebraTerminal.lean`: intervalos racionais certificados (correção, imagem exata,
  comutatividade, **associatividade**, subdistributividade; a distributividade é **refutada**),
  estados `U < A < P` e certificados condicionais `Cert x H` — hipótese não vira teorema.
- `ATK/ContracaoDN.lean`: contração `D_{2N} ≤ q D_N` ⇒ RH, mas é **incompatível** com o piso
  `D_N ≥ c/log N`; nenhuma amostra finita decide o limite; fechar RH ⟺ certificado `D_∞ ∈ [0,0]`.
- `ATK/BealFiltros.lean`: **Beal ⟺ `g* = 2`**; exatamente uma base par; filtros mod 8 e mod 4.
- `ATK/ModelosSete.lean`: os cálculos dos modelos (Gram `D₂ = 5/6`, absorção `5/12`, gap `1`,
  `Z = 7/4`, `det 5`, posto/núcleo, composição `n^{kl}`) e volumes exatos das bolas em 4, 5 e 11D.
- `ATK/Triadico.lean`: decomposição espectral de todo `T` com `T³ = 1`; órbitas de tamanho 1 ou 3;
  `|X| ≡ |Fix σ| (mod 3)`; cadeias de Markov com simetria triádica têm estacionária uniforme.

## Verde universal e raiz final — `UNIVERSAL_GREEN.md` (12 teoremas + auditor)

- `ATK/FinalRoot.lean`: a árvore inteira do fechamento. `raiz_de_produtores` (pontes restantes +
  produtores ⇒ os sete enunciados), `produtores_fieis_de_raiz` (sem atalho), **`verde_fiel_iff`**
  (`RH ∧ Beal ⟺ IsEmpty ZeroFora ∧ ExclusaoResidualDescida`, sem hipóteses), e
  `ns_depende_do_modelo`/`pnp_depende_do_modelo` (as ligações L1–L5 são necessárias).
- `scripts/terminal_gates.json` + `scripts/universal_green.py`: os 7 portões terminais; o auditor
  calcula `UNIVERSAL_GREEN` e `FINAL_ROOT` a cada push, checando o **tipo elaborado** de cada portão.
  Hoje: `false`, `null`, 0/7.
- `terminal-templates/` + `scripts/verificar_fiacao.py`: a última milha ligada — 21/21 modelos de
  portão compilam com as peças ausentes; rota da prova: faltam **18** termos; rota da refutação: 12.
- `ATK/Termos.lean` + `scripts/termos.json` + `scripts/termos.py` (39 teoremas): as **25
  lacunas distintas**, cada uma com nome e tipo Lean; o auditor troca cada lacuna por
  `(sorry : <tipo>)` e o kernel confere **25/25** tipos (com teste de sensibilidade). Provado:
  `fecha`, `exato`/`decomposicao` (RH, Beal, Hodge, BSD, P≠NP dada a ponte), formas-testemunha
  das refutações e o critério de fidelidade da L2 (`PNP.pneNP_de_fiel`). Ficha de 24 componentes
  por termo em [`TERMOS.md`](TERMOS.md).
- `ATK/CapturaRH.lean` (15 teoremas): na família genuína, `D_{N+1} = (1 − η_N) D_N` e
  `D_N = D_0 ∏(1 − η_j)` sem hipóteses; a captura relativa acumulada (forma logarítmica) é
  **equivalente** à obrigação O1 (`captura_log_iff`) e, sob o piso BBLS, fica presa em
  `log log N + O(1)` (`captura_teto`).
- `scripts/ensaio_universal_green.py`: ensaio de ponta a ponta com enunciados de brinquedo — 12/12
  (acende com provas válidas; bloqueia `sorry`, sombreamento, hipóteses, axiomas, enunciado trocado).
- `scripts/instalar_portao.py`: instala um portão só se for prova genuína; hoje recusa as 9 linhas.
- `scripts/plano.py`: o plano **T1–T9** calculado a cada push — biblioteca **VERDE** (T1–T6, T9),
  conjecturas **ABERTAS** (T7 2/7, T8 0/7). `scripts/congelar.py` gera `atk-kernel/audits/`
  (proveniência, SHA por arquivo, axiomas por teorema, atestação do CI);
  `scripts/integrar_biblioteca.py` integra um pacote Lean externo (p.ex. ATK-T1) sob auditoria.

## Estrutura para CLOSED_MATH — `ATK/ClosedMath.lean`

`CLOSED_MATH` não é escrito à mão: o auditor o calcula. Ele só vira `true` se existir
`atk-kernel/ATK/ClosedMathGate.lean` com `theorem closed_math` **sem hipóteses**, compilado,
dependendo só de `propext`, `Classical.choice` e `Quot.sound`, sem `sorry`/`admit`/`axiom`, e
enunciado sobre os modelos genuínos (revisão humana das ligações L1–L5). Hoje esse arquivo não
existe, então `CLOSED_MATH = false`.

O caminho está pronto no teorema-mestre (verificado):

```
closedMath_of_obligations : Bridges M → OpenObligations M → SevenStatements M
```

Para fechar, faltam **20 obrigações** (lista completa em `atk-kernel/scripts/obligations.json`,
reproduzida em cada relatório do CI):

| Tipo | Quantas | O que é | Estado |
|---|---|---|---|
| PONTE (B1–B7) | 7 | teoremas publicados (Báez-Duarte, Fermat, Leray, Cook–Levin, Lefschetz, Gross–Zagier–Kolyvagin, Osterwalder–Schrader) | provados no papel, não formalizados (B2 e B4 parciais nos modelos dos lanes) |
| ABERTA (O1–O8) | 8 | as hipóteses abertas dos condicionais | `OPEN_MATH` |
| LIGAÇÃO (L1–L5) | 5 | construir na Mathlib os objetos reais de NS, P vs NP, Hodge, BSD e Yang–Mills | não existem na Mathlib |

**Firewall (verificado):**
- `ns_toy_model_vacuous` e `pnp_toy_model_vacuous` provam os enunciados de NS e P vs NP em
  modelos de brinquedo. Isso mostra que fechar um enunciado paramétrico sem a ligação L não vale nada.
- Teste fora do projeto: `axiom fake_rh : RiemannHypothesis` compila, mas `#print axioms` lista
  `fake_rh` e a auditoria reprova. Axioma não fecha problema.

## Camada de regimes do gateway (v5.1) — `ATK/Regimes.lean`

As 10 formas do gateway viraram teoremas: 1 núcleo incondicional, a classificação dos
regimes e as formas condicionais. **Esta camada não fecha nada de `OPEN_MATH`.**

O motivo está provado no próprio arquivo: `W(t) = W₀ + 10⁻⁶·t` não depende de `Seff`
(`W_ignores_Seff`, por `rfl`). Então o núcleo vale em todos os regimes automaticamente — e
por isso mesmo não diz nada sobre RH, BSD, Yang–Mills ou resistência a DoS.

| # | Forma | Condição | Teorema | O que prova |
|---|---|---|---|---|
| 0 | núcleo | — | `W_strictMono` | W cresce estritamente em t, para qualquer Seff |
| 1 | suave | 0 < Seff² < 1 | `regime_suave_iff` | classificação exata |
| 2 | explosão / cirurgia | Seff² > 1 | `regime_explosao_iff` | classificação exata |
| 3 | crítica | Seff² = 1 | `regime_critico_iff` | classificação exata (κ = 288,54 é parâmetro) |
| 4 | vácuo | Seff = 0 | `regime_vacuo_iff`, `vacuo_W_cresce` | W cresce mesmo sem tráfego |
| 5 | metaestável | Seff² na faixa [lo, hi] | `histerese_sem_flapping` | com histerese, o modo nunca troca dentro da faixa |
| 6 | tunelamento | Δ ≥ 0 | `custoTunel_antitone` | exp(−Δt) decresce (Δ = 0,032 é parâmetro) |
| 7 | falha H1 | \|Re s − ½\| > tol | `suspeitaH1_silenciosa`, `nao_RH_de_suspeita` | sob RH o gatilho não dispara em zero exato; zero exato que dispara refuta RH |
| 8 | falha H3 | posto ≠ posto analítico | `falhaH3_iff`, `L_zero_preve_posto_positivo` | L(E,1) = 0 **não** é falha: sob BSD força posto ≥ 1 |
| 9 | ruído | Seff qualquer sequência | `ruido_W_monotono` | W[n] < W[n+1] — por construção, não mede DoS |

Correções em relação ao rascunho v5.1: "AES-512" não é um padrão (AES tem chaves de 128, 192
e 256 bits), então os modos no Lean são só `Bool`, sem semântica criptográfica; e um valor
numérico de Re s fora de ½ marca *suspeita*, não refutação — só um zero exato refuta RH.

### Forma 10 — grade Harappan (legenda, só documentação)

| | |
|---|---|
| **[Origem]** t₀ — início da contagem de W | **[Cirurgia]** Seff² > 1 — modo de isolamento |
| **[Fluxo]** 10⁻⁶ — taxa de W | **[Valor]** condicional H1/H2/H3 — só vale se a hipótese for provada |

## Estrutura

```
README.md                    este arquivo
CATALOG.md                   os 251 repositórios agrupados por função e por problema
SOURCES.md                   de onde veio cada arquivo (repo + SHA)
PROOF_SEARCH.md              busca de provas em 32 repositórios e 2.210 branches
INVENTORY.md                 inventário mestre: 224 repositórios, todas as linguagens de prova
inventory.json               dados (por repositório; declarações sem hipótese; Coq/Agda/Isabelle)
THEOREMS_2440.md             os 2.440 teoremas auditados, um a um: forma, hipóteses, obrigação
theorems_2440.json           dados (lane, nome, arquivo, linha, conclusão, hipóteses, forma)
INDETERMINACY.md             a teoria dos pontos de 3 estados e o que o kernel provou dela
I_THEORY.md                  a teoria de I: levantamento (586 leis), o que foi certificado/refutado
LACUNAS.md                   cada problema: fronteira certificada, lemas de caminho, lacuna exata
FICHAS.md                    provado / refutado / lacuna, zeros fora da linha, parâmetros
VALLEE_POUSSIN.md            região sem zeros logarítmica, valores de c(t), piso de m(ρ)
MODELOS_TERMINAIS.md         álgebra de terminais, caudas de D_N, Beal g* = 2, modelos, triádico
UNIVERSAL_GREEN.md           árvore do fechamento, portões terminais, UNIVERSAL_GREEN e FINAL_ROOT
TERMOS.md                    as 25 lacunas dos portões: tipo Lean, teoremas, 24 componentes cada
proof_search.json            dados da busca (por repositório, categoria e problema)
HYPOTHESIS_MAP.md            quais hipóteses dos condicionais já estão provadas
hypothesis_map.json          dados do mapa
BACKWARD_ORACLE_PROTOCOL.md  política fail-closed (copiada do m-core-openai-ns-audit)
catalog/                     repos.txt (lista), repos.json (classificação)
catalog/ilaws/               catálogos A–D das leis de I propostas no acervo, com fonte e veredito
scripts/build_catalog.py     regera o catálogo
scripts/proof_scan.py        o scanner da busca de provas
scripts/hyp_map.py           o mapa de descarga de hipóteses
scripts/inventory_scan.py    varredura multilíngue de um repositório (todos os branches)
scripts/aggregate_inv.py     gera INVENTORY.md
scripts/i_scan.py            coleta os arquivos sobre I em todos os branches
scripts/thm2440.py           classifica os 2.440 teoremas no commit verificado pelo CI
scripts/valores_vp.py        avalia c_poly(t), c_log(t) e o piso de m(ρ) (ilustração numérica)
scripts/report2440.py        gera THEOREMS_2440.md
atk-kernel/                  projeto Lean independente (Lean 4.34.1, Mathlib v4.34.1)
  ATK/*.lean                 19 lemas auxiliares do M-Core (inalterados)
  ATK/Conditional/*.lean     7 condicionais (14 teoremas)
  ATK/Regimes.lean           10 formas do gateway (14 teoremas; não toca OPEN_MATH)
  ATK/ClosedMath.lean        teorema-mestre + firewall (4 teoremas)
  ATK/Indeterminacy.lean     pontos de 3 estados, L'Hôpital, I = 0⊘0, 4 estados (50 teoremas)
  ATK/IndeterminacyStates.lean  7 estados, composição, dissipação total (34 teoremas)
  ATK/RiemannConcrete.lean   D_N decrescente e convergente; O1 ⟺ inf D_N = 0 (11 teoremas)
  ATK/RiemannFaithful.lean   integrabilidade, D_0 = 1, D_1 < 1 (25 teoremas)
  ATK/BealReduction.lean     Beal ⟺ exclusão primitiva; caso a = b (12 teoremas)
  ATK/BealPartial.lean       Beal com 3 ou 4 dividindo os expoentes, via FLT3/FLT4 (12 teoremas)
  ATK/BealResidual.lean      Beal ⟺ domínio residual exato (5 teoremas)
  ATK/RiemannStates.lean     7 estados aplicados a D_N: só zero/finito (9 teoremas)
  ATK/ZetaStrip.lean         ∫_1^∞ {t} t^{-s-1} = 1/(s−1) − ζ(s)/s em Re s > 0 (14 teoremas)
  ATK/MellinRho.lean         Mellin de {1/(k t)} = −k^{−s} ζ(s)/s na faixa (10 teoremas)
  ATK/BaezDuarteBridge.lean  ponte B1: D_N → 0 ⇒ RiemannHypothesis da Mathlib (22 teoremas)
  ATK/ObligationsClosed.lean obrigações fechadas por teorema (B1) — lidas pelo auditor
  ATK/ZetaSimetria.lean      extremos fechados, ζ(σ)<0, simetrias, RH ⟺ processos ao meio (43)
  ATK/IFormas.lean           as 7 formas indeterminadas e seus conjuntos de valores (53)
  ATK/IAlgebra.lean          álgebras de I: impossibilidades e modelos consistentes (34)
  ATK/IGeometria.lean        neutro, tensão, compressão, torção, torque, K3 (56)
  ATK/ZetaRetangulo.lean     região sem zeros |s−1| < 2 Re s; RH até a altura √3/2 (16)
  ATK/ZetaRegiao.lean        3–4–1 ⇒ região sem zeros em toda altura: c(t) < Re s < 1 − c(t) (10)
  ATK/ForaDaLinha.lean       zeros fora da linha: evitam, quarteto, condensam D_N ≥ m(ρ)² (11)
  ATK/Fichas.lean            provado/refutado/lacuna; anti-produtos; explosão T*; FLT ⟺ primos ≥ 5 (24)
  ATK/ZetaParcial.lean       ζ por somas parciais: Σ_{n≤N} n^{-s} + N^{1-s}/(s−1) − s·H_N(s) (8)
  ATK/ZetaLog.lean           |ζ| ≪ log|t| perto de Re s = 1; região c(t) ≍ (log|t|)^{-9} (39)
  ATK/ValleePoussin.lean     região log vence a polinomial (|t| ≥ 2000); piso explícito de D_N (7)
  ATK/AlgebraTerminal.lean   intervalos certificados, estados U<A<P, Cert x H (63)
  ATK/ContracaoDN.lean       contração ⇒ RH; refutada pelo piso log; amostra finita não decide (13)
  ATK/BealFiltros.lean       Beal ⟺ g* = 2; paridade; filtros mod 8 e mod 4 (15)
  ATK/ModelosSete.lean       modelos finitos das 7 linhas; volumes de bolas 4/5/11D (55)
  ATK/Triadico.lean          T³ = 1: decomposição espectral; pontos fixos mod 3; Markov (25)
  ATK/FinalRoot.lean         raiz final: pontes restantes + produtores ⇒ 7 enunciados; verde fiel exato (12)
  ATK/BealFLT.lean           com FLT, Beal ⟺ caso mdc(x,y,z) ∈ {1,2} (10)
  ATK/Shannon.lean           contagem de Shannon; família fora de P/poly (9)
  ATK/NSPequeno.lean         enstrofia: dados pequenos ⇒ sem explosão, decaimento (3)
  ATK/YMToy.lean             rede solúvel: gap de massa e seu fechamento no contínuo (16)
  scripts/obligations.json   as 20 obrigações e a regra do portão de CLOSED_MATH
  scripts/check_axioms.py    auditoria: CERTIFIED só com axiomas padrão e sem sorry/admit/axiom
  scripts/terminal_gates.json os 7 portões terminais (enunciado literal sem hipóteses)
  scripts/universal_green.py calcula UNIVERSAL_GREEN e FINAL_ROOT (fail-closed, tipo elaborado)
  scripts/verificar_fiacao.py confere a fiação dos portões; lista os 19 termos que faltam
  scripts/ensaio_universal_green.py ensaio de ponta a ponta do portão (enunciados de brinquedo)
  scripts/instalar_portao.py instala um portão terminal só se for prova genuína
  terminal-templates/        os 9 modelos de portão (RH … YM, VerdeFiel, ClosedMathGate)
  scripts/plano.py           calcula o plano T1–T9 (biblioteca × conjecturas)
  scripts/congelar.py        congela as fontes: audits/provenance.json, audits/axioms.txt
  scripts/integrar_biblioteca.py integra uma biblioteca Lean externa sob auditoria
  audits/                    congelamento: SHA das fontes e por arquivo, axiomas, atestação do CI
  scripts/conditionals.json  ponte, hipótese aberta e fidelidade de cada condicional
  numerics/                  D_N de Báez-Duarte (N ≤ 1500)
.github/workflows/           CI: compila, roda #print axioms por arquivo e publica a tabela
```

## Como verificar

O CI (`.github/workflows/atk-kernel.yml`) baixa a Mathlib pré-compilada, compila tudo e
gera `reports/report.md` com o veredito de cada um dos 101 teoremas, a tabela dos condicionais, o estado das 20 obrigações e o portão de CLOSED_MATH.
Localmente:

```
cd atk-kernel
lake exe cache get
lake build
lake env lean ATK/Conditional/Riemann.lean   # imprime os axiomas
```

## Observação sobre o M-Core

No M-Core, `FinalFail/Semantic/Riemann.lean` usa a orientação de *refutação*
(`RiemannOffCriticalZero`, um zero fora da reta), enquanto o registro `FinalProofRegistry`
usa a orientação *positiva* (`FiniteSpanApproximatesChi`). Este monorepo segue a positiva.
Vale alinhar as duas no M-Core.
