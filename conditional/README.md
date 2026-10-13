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

Todos os branches de **148 repositórios** (os demais: 13 vazios e 89 privados de arte, arquivo
pessoal/jurídico, arquitetura e cultura, não anexados) — 3.522 branches, 34.085 arquivos distintos:
7.842 Lean, 696 Coq/Rocq, 231 Agda, 457 Isabelle, 5.229 Python, 2.133 LaTeX. Há 829 declarações Lean
que concluem um alvo; as 135 sem hipótese explícita são 115 equivalências e 20 afirmações diretas,
**cada uma lida**: firewalls, P01 (SAT ∈ NP no modelo), `RiemannHypothesis := True` local, ou provas que
importam `axiom`s de outro arquivo (`horizon-prime---framework`, `millennium-riemann-I`). Nos 546
enunciados de Coq/Agda/Isabelle, 447 estão em arquivos com `Admitted`/`Axiom`/`postulate`/`sorry`; os
outros são condicionais, equivalências ou `True`. As 31 alegações textuais de `CLOSED_MATH = true`
(13 repositórios) não vêm acompanhadas de termo que o kernel aceite.

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
INVENTORY.md                 inventário mestre: 148 repositórios, todas as linguagens de prova
inventory.json               dados (por repositório; declarações sem hipótese; Coq/Agda/Isabelle)
THEOREMS_2440.md             os 2.440 teoremas auditados, um a um: forma, hipóteses, obrigação
theorems_2440.json           dados (lane, nome, arquivo, linha, conclusão, hipóteses, forma)
INDETERMINACY.md             a teoria dos pontos de 3 estados e o que o kernel provou dela
proof_search.json            dados da busca (por repositório, categoria e problema)
HYPOTHESIS_MAP.md            quais hipóteses dos condicionais já estão provadas
hypothesis_map.json          dados do mapa
BACKWARD_ORACLE_PROTOCOL.md  política fail-closed (copiada do m-core-openai-ns-audit)
catalog/                     repos.txt (lista), repos.json (classificação)
scripts/build_catalog.py     regera o catálogo
scripts/proof_scan.py        o scanner da busca de provas
scripts/hyp_map.py           o mapa de descarga de hipóteses
scripts/inventory_scan.py    varredura multilíngue de um repositório (todos os branches)
scripts/aggregate_inv.py     gera INVENTORY.md
scripts/thm2440.py           classifica os 2.440 teoremas no commit verificado pelo CI
scripts/report2440.py        gera THEOREMS_2440.md
atk-kernel/                  projeto Lean independente (Lean 4.34.1, Mathlib v4.34.1)
  ATK/*.lean                 19 lemas auxiliares do M-Core (inalterados)
  ATK/Conditional/*.lean     7 condicionais (14 teoremas)
  ATK/Regimes.lean           10 formas do gateway (14 teoremas; não toca OPEN_MATH)
  ATK/ClosedMath.lean        teorema-mestre + firewall (4 teoremas)
  ATK/Indeterminacy.lean     pontos de 3 estados, L'Hôpital, I = 0⊘0, 4 estados (50 teoremas)
  scripts/obligations.json   as 20 obrigações e a regra do portão de CLOSED_MATH
  scripts/check_axioms.py    auditoria: CERTIFIED só com axiomas padrão e sem sorry/admit/axiom
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
