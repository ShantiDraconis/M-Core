# Terceiro Templo — formalização e catálogo de testes

Este catálogo cobre o documento `detalhe.odt`: a Cabala e os problemas do milênio, a álgebra
ATK-I de números relacionais e o zero, a seta e o infinitésimo. Cada afirmação **demonstrável**
do documento aponta para um teorema Lean conferido pelo kernel. As afirmações que **não** são
demonstráveis aparecem marcadas, com o motivo.

Legenda:

* **K-local**: compilado neste ambiente (Lean 4.34.1, Mathlib `v4.34.1`), sem `sorry`; usa só os
  axiomas `propext`, `Classical.choice` e `Quot.sound` (ou nenhum).
* **K-CI**: já estava na biblioteca certificada (`audits/axioms.txt`). O CI recompila tudo a cada push.
* **SYMBOLIC**: correspondência simbólica guardada como dado. Não é ponte nem prova.
* **OPEN_MATH**: obrigação matemática em aberto. Nenhum arquivo daqui a demonstra.

Módulo novo: `atk-kernel/ATK/TerceiroTemplo.lean`, com 49 teoremas, todos K-local.

## Como reproduzir

```bash
cd atk-kernel
lake exe cache get              # ou, sem cache: lake build ATK.TerceiroTemplo (compila a Mathlib necessária)
lake env lean ATK/TerceiroTemplo.lean   # imprime os 49 `#print axioms`
python3 scripts/check_axioms.py         # no CI: CERTIFIED só se compilar, sem sorry/admit/axiom e com axiomas padrão
```

Cada teste é um `theorem` seguido de `#print axioms`. Um teorema com erro entra no ambiente com
`sorryAx`, e o `check_axioms.py` o reprova automaticamente.

---

## 1. O alfabeto (Sefer Yetzirah)

| # | Afirmação do documento | Teorema | O que o kernel confere | Estado |
|---|---|---|---|---|
| 1.1 | São 22 letras | `card_letras` | `Fintype.card Letra = 22` | K-local |
| 1.2 | 3 mães: א מ ש | `card_maes` | o filtro `familia = mae` tem 3 elementos | K-local |
| 1.3 | 7 duplas: ב ג ד כ פ ר ת | `card_duplas` | 7 elementos | K-local |
| 1.4 | 12 simples | `card_simples` | 12 elementos | K-local |
| 1.5 | 22 = 3 + 7 + 12 | `familias_particionam` | a soma das três famílias é o total de letras | K-local |
| 1.6 | Gematria padrão | `gematria_injetiva` | letras diferentes têm valores diferentes (decisão finita sobre 22×22 pares) | K-local |
| 1.7 | Soma da gematria | `gematria_soma` | ∑ = 1495 (45 + 450 + 1000) | K-local |
| 1.8 | Mães: 1 + 40 + 300 | `gematria_maes` | = 341 (sem axiomas) | K-local |
| 1.9 | 231 portas = C(22, 2) | `portas_231`, `portas_eq_choose` | o número de subconjuntos de 2 letras é 231 | K-local |
| 1.10 | 32 caminhos = 10 + 22 | `caminhos_32` | 10 + 22 = 32, e ל + ב = 30 + 2 = 32 | K-local |

## 2. A Árvore da Vida como grafo

Os caminhos seguem a convenção de **Kircher (1652)**. Outras convenções (por exemplo a de Gra/Luria)
dão outro grafo e precisariam ser testadas de novo.

| # | Afirmação | Teorema | O que o kernel confere | Estado |
|---|---|---|---|---|
| 2.1 | 10 sefirot | `card_sefirot` | `Fintype.card Sefira = 10` | K-local |
| 2.2 | 22 caminhos, sem laços | `caminho_sem_laco` | nenhum caminho liga uma sefirá a si mesma | K-local |
| 2.3 | Caminhos distintos | `caminho_sem_repeticao` | nenhum par não ordenado aparece duas vezes, logo |E| = 22 | K-local |
| 2.4 | O grafo é conexo | `arvore_conexa` | 4 passos de alcance a partir de Keter cobrem as 10 sefirot | K-local |
| 2.5 | β₁ = 22 − 10 + 1 = 13 | `betti_um` | conta do número ciclomático, válida porque 2.3 e 2.4 valem | K-local |

## 3. Energia e laplaciano (Teoremas 1–3 do documento)

| # | Afirmação | Teorema | Hipóteses | Estado |
|---|---|---|---|---|
| 3.1 | E(f) ≥ 0 (Teorema 1) | `energia_nonneg` | pesos w ≥ 0, grafo finito qualquer | K-local |
| 3.2 | ⟨f, Lf⟩ = E(f) | `forma_laplaciano` | pesos simétricos; enunciado como 2⟨f, Lf⟩ = ∑ᵤ∑ᵥ (soma dupla) | K-local |
| 3.3 | L é positivo semidefinido | `lap_psd` | w simétrico e ≥ 0 | K-local |
| 3.4 | Energia da Árvore ≥ 0 | `energiaArvore_nonneg` | — | K-local |
| 3.5 | E(f) = 0 ⟺ f constante (Teorema 2) | `energiaArvore_zero_iff` | os 22 caminhos de Kircher; a ida usa uma árvore geradora explícita (arestas 0, 1, 2, 5, 7, 13, 14, 15, 21) | K-local |
| 3.6 | Existe λ₂ > 0 em todo grafo conexo (Teorema 3, caso geral) | — | **não formalizado**: exige o mínimo do quociente de Rayleigh na esfera (compacidade). O caso explícito C₁₀ está em 4.3 | pendente |

## 4. O ciclo de dez estados (Teorema 4 e cálculo explícito)

| # | Afirmação | Teorema | O que o kernel confere | Estado |
|---|---|---|---|---|
| 4.1 | λₖ = 2 − 2cos(2πk/10) | `ciclo_autovetor` | 2cos(θx) − cos(θ(x−1)) − cos(θ(x+1)) = (2 − 2cos θ)·cos(θx) | K-local |
| 4.2 | O autovetor fecha o ciclo | `ciclo_periodico` | com θ = 2πk/n, cos(θ(x+n)) = cos(θx) | K-local |
| 4.3 | λ₁ = (3 − √5)/2 ≈ 0,381966 | `lambda1_C10`, `lambda1_C10_pos` | valor exato via cos(π/5) = (1 + √5)/4, e λ₁ > 0 | K-local |
| 4.4 | μₖ = 1 − λₖ/4 = cos²(πk/10) | `mu_C10` | identidade trigonométrica | K-local |
| 4.5 | q = cos²(π/10) = (5 + √5)/8 ≈ 0,9045 | `q_C10`, `q_C10_pos`, `q_C10_lt_one` | valor exato, com 0 < q < 1 | K-local |

## 5. Invariância e contração

| # | Afirmação | Teorema | O que o kernel confere | Estado |
|---|---|---|---|---|
| 5.1 | A identidade preserva o invariante | `preserva_id` | sem axiomas | K-local |
| 5.2 | A composição preserva o invariante | `preserva_comp` | sem axiomas | K-local |
| 5.3 | ‖Tⁿf‖ ≤ qⁿ‖f‖ | `contracao_iterada` | por indução, em qualquer espaço seminormado | K-local |
| 5.4 | qⁿ‖f‖ → 0 | `contracao_tende_zero` | 0 ≤ q < 1 | K-local |
| 5.5 | Invariante **e** contraído implica zero | `invariante_contraido_zero` | d(Tx) = d(x) ≤ q·d(x), com q < 1, dá d(x) = 0: o mecanismo só **detecta** um zero, não o cria | K-local |

## 6. Zero, seta e infinitésimo (a tabela E_N / 0 / → / 10⁻ᴺ / 10⁻ᴴ)

| # | Afirmação | Teorema | O que o kernel confere | Estado |
|---|---|---|---|---|
| 6.1 | E₁ = 1 − ln 2 ≈ 0,3068528194 | `E1_intervalo` | 0,3068528192 < E₁ < 0,3068528197 (cotas de ln 2 da Mathlib) | K-local |
| 6.2 | 10⁻ᴺ > 0 | `dez_pot_pos` | — | K-local |
| 6.3 | 10⁻ᴺ → 0 (a seta é um limite, não um número) | `dez_pot_tende_zero` | — | K-local |
| 6.4 | Positivo e decrescente **não** implica → 0 | `positivo_decrescente_nao_basta` | 1/5 + 1/(N+1) é > 0 e antítona, tende a 1/5, e **não** tende a 0 | K-local |
| 6.5 | 10⁻ᴴ > 0 com parte padrão 0 | `dezMenosH_infinitesimal` | nos hiper-reais da Mathlib, H = [n ↦ n] | K-local |
| 6.6 | 0 = 0 (zero real exato) | — | trivial (`rfl`) | — |
| 6.7 | e = 2,71828… é diferente do erro E_N | — | só distinção de notação, não há o que provar | — |

## 7. Álgebra ATK-I: números relacionais (já certificada)

| # | Afirmação | Teorema (módulo) | Estado |
|---|---|---|---|
| 7.1 | (0 = 1)·3 = (0 = 3) | `ATKINormal.Par.exemplo_escala` | K-CI |
| 7.2 | (2 = 1)³ = (8 = 1) | `ATKINormal.Par.exemplo_pot` | K-CI |
| 7.3 | Defeitos 3 e 7 | `defeito_0_3`, `defeito_8_1` | K-CI |
| 7.4 | (0=1)·3 ⪰ (2=1)³ **vale** pela proximidade | `exemplo_proximidade` | K-CI |
| 7.5 | Pela diferença (−3 ≥ 1): falsa | `pela_diferenca_falsa` | K-CI |
| 7.6 | Por componentes: falsa | `por_componentes_falsa` | K-CI |
| 7.7 | Com ε hiper-real (ε³ − 6ε² + 9ε − 8 ≥ 0): falsa | `infinitesimal_falsa` | K-CI |
| 7.8 | ⪰ é pré-ordem total, **não** antissimétrica | `maisProximo_refl/trans/total`, `nao_antissimetrica` | K-CI |
| 7.9 | T₀ = id; T₁ fecha; T₁∘T₁ = T₁; Tₜ fixa as igualdades verdadeiras | `T_zero`, `T_vale`, `T_idem`, `T_estavel`, `T_comp` | K-CI |
| 7.10 | d(Tₜ R) = (1 − t)·d(R); Tₜ preserva a ordem | `defeito_T`, `T_mono` | K-CI |
| 7.11 | A normalização **não** é prova | `normalizacao_nao_e_prova`, `vale_T_iff`, `normalizar_D` | K-CI |
| 7.12 | D_x(R) = d(R)/(1+x) → 0; x/(1+x) leva (0=1) a (1=1) | `Dx_tendsto`, `defeito_T_tx`, `T_tx_tendsto` | K-CI |
| 7.13 | (D∞ = 0) **valer** implica RH | `vale_D_infinito_RH` (ponte de Bagchi/Báez-Duarte) | K-CI |

## 8. Os problemas na linguagem de defeitos

| # | Problema | Afirmação | Teorema | Estado |
|---|---|---|---|---|
| 8.1 | RH | Identidade telescópica ∑δ_N = D₁ − D∞ | `ATKIAplicacoes.telescopica`, `rh_de_telescopica` | K-CI |
| 8.2 | RH | D_N ≤ K/log(N+2) implica D_N → 0 | `cota_log_fecha` | K-local |
| 8.3 | RH | D_N ≤ C·qᴺ (aproximação geométrica) implica D_N → 0 | `cota_geometrica_fecha` | K-local |
| 8.4 | RH | Existe **de fato** essa cota para o D_N de Nyman–Beurling | — | **OPEN_MATH** (equivale a RH) |
| 8.5 | YM | d_δ(Δ) = max(0, δ − Δ) = 0 ⟺ Δ ≥ δ | `defeito_gap_zero_iff`, `defeito_gap_exemplo` | K-local |
| 8.6 | YM | O espectro {1/(n+1)} não tem gap | `espectro_sem_gap` | K-local |
| 8.7 | YM | Gaps positivos Δₐ = a podem sumir no limite | `ATKIAplicacoes.gaps_positivos_somem` | K-CI |
| 8.8 | YM | H ≥ δ(I − P) implica gap ≥ δ | `ATKIAplicacoes.gap_de_coercividade` | K-CI |
| 8.9 | YM | Teoria quântica 4D e gap físico | — | **OPEN_MATH** |
| 8.10 | NS | y = (1 − 2t)^(−1/2) resolve y′ = y³ | `riccati_solucao` | K-local |
| 8.11 | NS | Essa solução explode em t → 1/2⁻ | `riccati_explode` | K-local |
| 8.12 | NS | Absorção c_B + c_T < 1 com Grönwall dá cota finita | `ATKIAplicacoes.absorcao`, `gronwall_simples`, `ns_condicional` | K-CI |
| 8.13 | NS | δ = 1 − 1/4 − 1/3 = 5/12 | `ATKIAplicacoes.margem_exemplo` | K-CI |
| 8.14 | NS | A absorção vale para todas as soluções 3D | — | **OPEN_MATH** |
| 8.15 | BSD | Defeito inteiro < 1 fecha a igualdade (ℕ e ℤ) | `ATKIAplicacoes.fechamento_inteiro`, `fechamento_inteiro_int` | K-CI / K-local |
| 8.16 | BSD | Cotas 2 ≤ r ≤ 2 fecham o posto | `ATKIAplicacoes.cotas_fecham` | K-CI |
| 8.17 | BSD | det [[2,1],[1,3]] = 5; h₂₂ = 3 | `regulador_exemplo`, `regulador_h22` | K-CI |
| 8.18 | BSD | Posto = ordem de anulação, para toda curva | — | **OPEN_MATH** |
| 8.19 | Hodge | 2z₁ + 3z₂ = α (certificado racional do exemplo) | `ATKIAplicacoes.hodge_certificado`, `hodge_transicao` | K-CI |
| 8.20 | Hodge | Toda classe de Hodge racional é algébrica | — | **OPEN_MATH** |
| 8.21 | Todos | Defeito total ∑wᵢdᵢ = 0 ⟹ cada dᵢ = 0 | `ATKIAlgebra.fechamento_simultaneo`, `universal_sete` | K-CI |
| 8.22 | Todos | Mundo hipotético: pontes + obrigações ⟹ enunciados | `ClosedMath.closedMath_of_obligations` | K-CI (condicional: as obrigações entram como hipóteses) |

## 9. Atribuição simbólica letra → problema

| # | Afirmação | Teorema | Estado |
|---|---|---|---|
| 9.1 | A tabela 8 × 22 do documento | `letrasDe` (definição) | SYMBOLIC |
| 9.2 | Toda letra está em algum problema | `letras_cobertas` | K-local (sobre o **dado**) |
| 9.3 | ת aparece nos oito problemas | `tav_em_todos` | K-local (sobre o **dado**) |
| 9.4 | A letra X "fornece" uma prova do problema Y | — | **não é afirmação matemática**: nenhum teorema usa `letrasDe` como hipótese |

## Resumo

| Camada | Testes | Estado |
|---|---|---|
| Alfabeto, Árvore, energia, ciclo C₁₀, contração, infinitésimos, defeitos (módulo novo) | 49 | 49/49 K-local |
| ATK-I e defeitos dos problemas (módulos existentes, citados acima) | 40+ | K-CI |
| Gap geral do grafo conexo (Teorema 3, caso geral) | 1 | pendente de formalização |
| Pontes para RH, YM, NS, BSD, Hodge, P≠NP e Beal | 7 | **OPEN_MATH** |
| Correspondências cabalísticas | tabela | SYMBOLIC |

Nenhum teste deste catálogo prova um problema do milênio. O que a formalização mostra é que a
estrutura combinatória da Cabala (22 letras, 231 portas, Árvore com 10 sefirot e 22 caminhos)
produz objetos com propriedades verificáveis: energia, laplaciano, gap no ciclo e contração.
A passagem desses objetos finitos para os objetos infinitos dos problemas é exatamente a parte
que continua aberta.
