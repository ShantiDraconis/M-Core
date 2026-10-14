# Termos terminais — ficha de 24 componentes

Gerado por `atk-kernel/scripts/termos.py --md` a partir de `atk-kernel/scripts/termos.json` (catálogo) e `atk-kernel/ATK/Termos.lean` (nomes e teoremas no kernel).

## Contagem reconciliada

- **25 lacunas** no catálogo, nos 21 modelos de portão: **23 abertas** e **2 preenchidas** (ligação construída no kernel).
- Rota da prova: **16** ocorrências abertas; rota da refutação: **10**; 3 ligações abertas são compartilhadas pelas duas rotas (16 + 10 − 3 = 23).
- Antes da construção da L2 eram 18 + 12 − 5 = 25; as contagens "18 + 12" e "25" mediam coisas diferentes e estavam certas.
- Tipos conferidos pelo kernel: **25/25** (cada lacuna aberta trocada por `(sorry : <tipo do catálogo>)` compila; cada lacuna preenchida compila com o termo real; trocar o tipo de B3 pelo de O3 faz a compilação falhar).
- Fechadas: **0/25**. Preencher uma lacuna de produtor ou de refutação é resolver o problema correspondente; preencher uma ligação é construir o modelo genuíno (falta ainda a revisão humana para `CLOSED`).

Fontes do kernel: SHA-256 `972898dd0b87f2779d2527329c00d3e527c726ff65884deef0f0a5ba5c98e142`.

## Os 24 componentes

Componentes 1–3, 8, 17–20, 23 e 24 são de cada termo; 4–7, 9–16, 21 e 22 são do domínio da linha e valem para todos os termos dela (não se inventam derivadas para objetos lógicos: onde não se aplica, está escrito).

## RH — Hipótese de Riemann

Enunciado oficial no portão: RiemannHypothesis (Mathlib). Ligação: nenhuma (enunciado da Mathlib). Mathlib: enunciado oficial já na Mathlib.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | ℂ; zeros não triviais de ζ (faixa 0 < Re s < 1) |
| 5 · Classes numéricas | ℂ, ℝ, ℕ |
| 6 · Parâmetros | nenhum |
| 7 · Operadores | ζ (continuação analítica), Re, conjugação, s ↦ 1 − s |
| 9 · Invariantes | simetria ρ ↦ 1 − ρ e conjugação (quarteto de zeros: ATK.ForaDaLinha.quarteto_fora) |
| 10 · Dimensão | 1 complexa (2 reais) |
| 11 · Geometria | faixa crítica; reta Re s = 1/2 |
| 12 · Coordenadas | s = σ + it |
| 13 · Métrica ou topologia | topologia de ℂ (métrica euclidiana) |
| 14 · Derivadas | ζ′ (holomorfia); usada na região sem zeros |
| 15 · Integrais | Mellin/Plancherel (critério de Báez-Duarte: ATK.MellinPlancherel, ATK.PlancherelL1L2) |
| 16 · Limites | D_N → 0 ⟺ RH (Báez-Duarte); numericamente D_N·log(N+2) ≈ 0,0457 |
| 21 · Exemplos (no kernel) | `ATK.ZetaLog.regiao_log`; `ATK.ContracaoDN.cert_Dinf_numerico_mem` |
| 22 · Contraexemplos (no kernel) | `ATK.FinalRoot.rota_contracao_morta`; `ATK.ContracaoDN.amostra_finita_nao_decide` |

### T01 — `RH:PROVA_DO_PRODUTOR`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T01 · `ATK.Termos.RH.produtor` · produtor O1 · rota prova |
| 2 · Definição formal | não existe zero não trivial de ζ com Re ≠ 1/2 (IsEmpty ZeroFora) — tipo Lean `ATK.Termos.RH.produtor` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.ForaDaLinha.riemann_iff_vazio`; `ATK.ForaDaLinha.nao_riemann_iff` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.RH.fecha`; `ATK.Termos.RH.exato` |
| 19 · Dependências | `ATK/Termos.lean`; nenhuma (enunciado da Mathlib) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.RH.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/RH.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T14 — `RHRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T14 · `ATK.Termos.RH.refutacao` · refutacao ¬RH · rota refutacao |
| 2 · Definição formal | um zero s de ζ, não trivial, s ≠ 1, com Re s ≠ 1/2 — tipo Lean `ATK.Termos.RH.refutacao` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.ForaDaLinha.riemann_iff_vazio`; `ATK.ForaDaLinha.nao_riemann_iff` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.RH.refutacao_iff`; `ATK.Termos.RH.refutacao_iff_zero_fora`; `ATK.Termos.RH.refutacao_nega_produtor` |
| 19 · Dependências | `ATK/Termos.lean`; nenhuma (enunciado da Mathlib) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.RHRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/RHRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

## Beal — Conjectura de Beal

Enunciado oficial no portão: ATK.Conditional.Beal.BealConjecture. Ligação: nenhuma (enunciado elementar em ℕ). Mathlib: FLT para n = 3, 4 na Mathlib; enunciado de Beal no ATK.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | ℕ⁶: bases a, b, c > 0; expoentes x, y, z > 2 |
| 5 · Classes numéricas | ℕ |
| 6 · Parâmetros | nenhum |
| 7 · Operadores | potência, mdc, divisibilidade, redução mod n |
| 9 · Invariantes | mdc(a, b, c); classes residuais mod 4 e mod 8; mdc dos expoentes |
| 10 · Dimensão | discreta (reticulado ℕ⁶) |
| 11 · Geometria | pontos inteiros em superfícies de Fermat generalizadas |
| 12 · Coordenadas | (a, b, c, x, y, z) |
| 13 · Métrica ou topologia | discreta |
| 14 · Derivadas | não se aplica |
| 15 · Integrais | não se aplica |
| 16 · Limites | não se aplica (enunciado finitário por instância) |
| 21 · Exemplos (no kernel) | `ATK.BealFourFourTwo.exemplos_442`; `ATK.BealFiltros.mod8_expoentes_pares` |
| 22 · Contraexemplos (no kernel) | `ATK.BealPartial.beal_exemplos_distintos` |

### T02 — `Beal:PROVA_DO_PRODUTOR`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T02 · `ATK.Termos.Beal.produtor` · produtor O2 · rota prova |
| 2 · Definição formal | nenhuma solução coprima de aˣ + bʸ = cᶻ no residual da descida (ExclusaoResidualDescida) — tipo Lean `ATK.Termos.Beal.produtor` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.BealCompleto.beal_incondicional`; `ATK.BealCompleto.beal_teorema_completo` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.Beal.fecha`; `ATK.Termos.Beal.exato` |
| 19 · Dependências | `ATK/Termos.lean`; nenhuma (enunciado elementar em ℕ) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.Beal.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/Beal.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T15 — `BealRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T15 · `ATK.Termos.Beal.refutacao` · refutacao ¬Beal · rota refutacao |
| 2 · Definição formal | aˣ + bʸ = cᶻ com x, y, z ≥ 3 e mdc(a, b, c) = 1 — basta procurar no residual com a, b coprimos — tipo Lean `ATK.Termos.Beal.refutacao` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.BealCompleto.beal_incondicional`; `ATK.BealCompleto.beal_teorema_completo` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.Beal.refutacao_iff`; `ATK.Termos.Beal.refutacao_iff_mdc`; `ATK.Termos.Beal.refutacao_iff_residual` |
| 19 · Dependências | `ATK/Termos.lean`; nenhuma (enunciado elementar em ℕ) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.BealRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/BealRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

## NS — Navier–Stokes 3D (Clay, caso A)

Enunciado oficial no portão: ClayStatementA modeloGenuino ⟺ (A) do Clay (ATK.LigacaoNS.clayA_iff). Ligação: L1 FECHADA: ATK.LigacaoNS.modeloNS (revisão humana do titular em 14/10/2026; fidelidade ATK.LigacaoNS.clayA_iff). Mathlib: sem teoria de soluções de NS; L1 construída sobre Schwartz, fderiv e Lebesgue.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | ℝ³ × [0, ∞); velocidade u, pressão p; dado de Schwartz de divergência nula; ν > 0 |
| 5 · Classes numéricas | ℝ |
| 6 · Parâmetros | modelo M : NSModel (L1) |
| 7 · Operadores | ∂_t, ∂_j (fderiv), ∇, div, Δ, (u·∇)u |
| 9 · Invariantes | div u = 0; energia ½‖u‖²₂ não cresce; escala u_λ(x, t) = λ·u(λx, λ²t) |
| 10 · Dimensão | 3 espaciais + tempo; espaço de funções de dimensão infinita |
| 11 · Geometria | ℝ³ euclidiano; fluxo incompressível |
| 12 · Coordenadas | cartesianas (EuclideanSpace ℝ (Fin 3)) |
| 13 · Métrica ou topologia | L² (energia); enstrofia ‖∇u‖²₂ |
| 14 · Derivadas | ∂_t u + (u·∇)u = νΔu − ∇p (ATK.LigacaoNS.NSEq) |
| 15 · Integrais | energia ∫\|u\|², enstrofia ∫\|∇u\|² (ATK.LigacaoNS.gradSq) |
| 16 · Limites | explosão: enstrofia ilimitada quando t → T⁻ |
| 21 · Exemplos (no kernel) | `ATK.LigacaoNS.zero_global`; `ATK.LigacaoNS.global_nao_trivial`; `ATK.ModelosSete.absorcao_modelo` |
| 22 · Contraexemplos (no kernel) | `ATK.LigacaoNS.id_nao_admissivel`; `ATK.FinalRoot.ns_depende_do_modelo` |

### T03 — `NS:PROVA_DA_PONTE_B3`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T03 · `ATK.Termos.NS.ponteB3` · ponte B3 · rota prova |
| 2 · Definição formal | sem solução global, a enstrofia explode em tempo finito (Leray 1934 + teoria local) — tipo Lean `ATK.Termos.NS.ponteB3 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.NavierStokes.ns_conditional`; `ATK.LigacaoNS.clayA_iff` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.NS.fecha`; `ATK.Termos.NS.colapso_de_refutacao` |
| 19 · Dependências | `ATK/Termos.lean`; L1 FECHADA: ATK.LigacaoNS.modeloNS (revisão humana do titular em 14/10/2026; fidelidade ATK.LigacaoNS.clayA_iff) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.NS.terminal` |
| 23 · Certificado Lean | teorema publicado; falta formalizar · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/NS.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T04 — `NS:PROVA_DO_PRODUTOR_O3`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T04 · `ATK.Termos.NS.produtorO3` · produtor O3 · rota prova |
| 2 · Definição formal | cota a priori da enstrofia enquanto a solução suave existe — tipo Lean `ATK.Termos.NS.produtorO3 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.NavierStokes.ns_conditional`; `ATK.LigacaoNS.clayA_iff` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.NS.fecha`; `ATK.Termos.NS.fecha_oficial` |
| 19 · Dependências | `ATK/Termos.lean`; L1 FECHADA: ATK.LigacaoNS.modeloNS (revisão humana do titular em 14/10/2026; fidelidade ATK.LigacaoNS.clayA_iff) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.NS.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/NS.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T16 — `NSRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T16 · `ATK.Termos.NS.refutacao` · refutacao ¬(A) · rota refutacao |
| 2 · Definição formal | ν > 0 e u₀ de Schwartz com div u₀ = 0 sem solução global suave de energia limitada (com B3: explosão da enstrofia — enunciado (C)) — tipo Lean `ATK.Termos.NS.refutacao modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.NavierStokes.ns_conditional`; `ATK.LigacaoNS.clayA_iff` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.NS.refutacao_iff`; `ATK.Termos.NS.colapso_de_refutacao`; `ATK.Termos.NS.refutacao_nega_produtor` |
| 19 · Dependências | `ATK/Termos.lean`; L1 FECHADA: ATK.LigacaoNS.modeloNS (revisão humana do titular em 14/10/2026; fidelidade ATK.LigacaoNS.clayA_iff) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.NSRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/NSRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

## PNP — P vs NP

Enunciado oficial no portão: PneNP modeloGenuino; enunciado fiel já no kernel: ATK.LigacaoPNP.PneNP (Turing.FinTM2). Ligação: L2 construída: ATK.ModeloPNP.modeloPNP e ATK.ModeloPNP.SAT (revisão humana pendente para CLOSED). Mathlib: tem TM2ComputableInPolyTime; a composição em tempo polinomial foi provada aqui (ATK.ComposicaoTM2.comp); faltam Cook–Levin e SAT ∉ P.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | linguagens L ⊆ {0,1}*; máquinas Turing.FinTM2 de tempo polinomial |
| 5 · Classes numéricas | ℕ (tamanhos e tempos), ℕ[X] |
| 6 · Parâmetros | modelo M : ComplexityModel (L2) e a linguagem SAT (L2_SAT) |
| 7 · Operadores | redução de Karp, composição de máquinas, par ⟨w, c⟩ |
| 9 · Invariantes | P ⊆ NP; P fechada por redução |
| 10 · Dimensão | discreta |
| 11 · Geometria | combinatória (circuitos, grafos de configuração) |
| 12 · Coordenadas | palavras List Bool |
| 13 · Métrica ou topologia | comprimento de palavra; tempo de execução |
| 14 · Derivadas | não se aplica |
| 15 · Integrais | não se aplica |
| 16 · Limites | assintótica polinomial T(n) = O(nᵏ) |
| 21 · Exemplos (no kernel) | `ATK.LigacaoPNP.vazio_em_P`; `ATK.LigacaoPNP.univ_em_NP`; `ATK.PvsNP.p_ne_np_of_sat` |
| 22 · Contraexemplos (no kernel) | `ATK.FinalRoot.pnp_depende_do_modelo` |

### T05 — `PNP:PROVA_DA_PONTE_B4`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T05 · `ATK.Termos.PNP.ponteB4` · ponte B4 · rota prova |
| 2 · Definição formal | Cook–Levin: SAT ∈ NP e toda L ∈ NP reduz a SAT — tipo Lean `ATK.Termos.PNP.ponteB4 modeloGenuino sat` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.PvsNP.pvsnp_conditional`; `ATK.Conditional.PvsNP.pneNP_iff_sat_not_in_P`; `ATK.ComposicaoTM2.comp`; `ATK.ModeloPNP.P_sub_NP`; `ATK.ModeloPNP.P_fechada_red` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.PNP.fecha`; `ATK.Termos.PNP.exato` |
| 19 · Dependências | `ATK/Termos.lean`; L2 construída: ATK.ModeloPNP.modeloPNP e ATK.ModeloPNP.SAT (revisão humana pendente para CLOSED) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.PNP.terminal` |
| 23 · Certificado Lean | teorema publicado; falta formalizar · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/PNP.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T06 — `PNP:PROVA_DO_PRODUTOR_O4`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T06 · `ATK.Termos.PNP.produtorO4` · produtor O4 · rota prova |
| 2 · Definição formal | SAT ∉ P — tipo Lean `ATK.Termos.PNP.produtorO4 modeloGenuino sat` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.PvsNP.pvsnp_conditional`; `ATK.Conditional.PvsNP.pneNP_iff_sat_not_in_P`; `ATK.ComposicaoTM2.comp`; `ATK.ModeloPNP.P_sub_NP`; `ATK.ModeloPNP.P_fechada_red` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.PNP.fecha`; `ATK.Termos.PNP.exato` |
| 19 · Dependências | `ATK/Termos.lean`; L2 construída: ATK.ModeloPNP.modeloPNP e ATK.ModeloPNP.SAT (revisão humana pendente para CLOSED) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.PNP.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/PNP.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T17 — `PNPRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T17 · `ATK.Termos.PNP.refutacao` · refutacao P = NP · rota refutacao |
| 2 · Definição formal | P = NP; com B4: SAT ∈ P (um algoritmo polinomial para SAT) — tipo Lean `ATK.Termos.PNP.refutacao modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.PvsNP.pvsnp_conditional`; `ATK.Conditional.PvsNP.pneNP_iff_sat_not_in_P`; `ATK.ComposicaoTM2.comp`; `ATK.ModeloPNP.P_sub_NP`; `ATK.ModeloPNP.P_fechada_red` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.PNP.refutacao_iff`; `ATK.Termos.PNP.refutacao_iff_sat` |
| 19 · Dependências | `ATK/Termos.lean`; L2 construída: ATK.ModeloPNP.modeloPNP e ATK.ModeloPNP.SAT (revisão humana pendente para CLOSED) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.PNPRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/PNPRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T21 — `PNPModelo:LIGACAO_L2`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T21 · `ATK.Termos.Ligacoes.L2` · ligacao L2 · rota prova+refutacao |
| 2 · Definição formal | modelo genuíno de P e NP; fidelidade exigida: FielL2 (classes = P, NP sobre Turing.FinTM2) — tipo Lean `ATK.Termos.Ligacoes.L2` |
| 3 · Tipo matemático | dado: estrutura ComplexityModel.{0} |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.PvsNP.pvsnp_conditional`; `ATK.Conditional.PvsNP.pneNP_iff_sat_not_in_P`; `ATK.ComposicaoTM2.comp`; `ATK.ModeloPNP.P_sub_NP`; `ATK.ModeloPNP.P_fechada_red` |
| 17 · Hipóteses | o modelo tem de satisfazer o critério de fidelidade da ligação |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.PNP.pneNP_de_fiel`; `ATK.Termos.PNP.finito_nao_fiel`; `ATK.ModeloPNP.P_sub_NP`; `ATK.ModeloPNP.P_fechada_red`; `ATK.ModeloPNP.fiel`; `ATK.ModeloPNP.fielL2`; `ATK.ComposicaoTM2.comp` |
| 19 · Dependências | `ATK/Termos.lean`; L2 construída: ATK.ModeloPNP.modeloPNP e ATK.ModeloPNP.SAT (revisão humana pendente para CLOSED) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.PNPModelo.modeloGenuino` |
| 23 · Certificado Lean | CONSTRUÍDA no kernel (ATK.ModeloPNP.modeloPNP; P ⊆ NP e fechamento por reduções provados); falta revisão humana para CLOSED · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/PNPModelo.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T22 — `PNPModelo:LIGACAO_L2_SAT`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T22 · `ATK.Termos.Ligacoes.L2SAT` · ligacao L2 · rota prova+refutacao |
| 2 · Definição formal | a linguagem SAT (fórmulas CNF satisfatíveis, codificadas em {0,1}*) — tipo Lean `ATK.Termos.Ligacoes.L2SAT modeloGenuino` |
| 3 · Tipo matemático | dado: linguagem do modelo L2 |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.PvsNP.pvsnp_conditional`; `ATK.Conditional.PvsNP.pneNP_iff_sat_not_in_P`; `ATK.ComposicaoTM2.comp`; `ATK.ModeloPNP.P_sub_NP`; `ATK.ModeloPNP.P_fechada_red` |
| 17 · Hipóteses | o modelo tem de satisfazer o critério de fidelidade da ligação |
| 18 · Lemas (certificados, do termo) | `ATK.ModeloPNP.sat_vazia`; `ATK.ModeloPNP.clausula_vazia_insat` |
| 19 · Dependências | `ATK/Termos.lean`; L2 construída: ATK.ModeloPNP.modeloPNP e ATK.ModeloPNP.SAT (revisão humana pendente para CLOSED) |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.PNPModelo.sat` |
| 23 · Certificado Lean | CONSTRUÍDA no kernel (ATK.ModeloPNP.SAT: codificação binária de CNF satisfatíveis); falta revisão humana para CLOSED · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/PNPModelo.lean.tpl` · `atk-kernel/scripts/termos.json` |

## Hodge — Conjectura de Hodge

Enunciado oficial no portão: HodgeConjecture modeloGenuino. Ligação: L3 aberta. Mathlib: sem cohomologia de Hodge de variedades projetivas.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | variedades projetivas complexas lisas X; classes em H^{2p}(X, ℚ) de tipo (p, p) |
| 5 · Classes numéricas | ℚ, ℂ |
| 6 · Parâmetros | modelo M : HodgeModel (L3) |
| 7 · Operadores | classe de ciclo cl : CH^p(X) ⊗ ℚ → H^{2p}(X, ℚ); decomposição de Hodge |
| 9 · Invariantes | tipo (p, p); racionalidade |
| 10 · Dimensão | dim_ℂ X = n; codimensão p |
| 11 · Geometria | geometria algébrica complexa; cohomologia |
| 12 · Coordenadas | coordenadas projetivas homogêneas |
| 13 · Métrica ou topologia | métrica de Kähler (Fubini–Study) |
| 14 · Derivadas | ∂, ∂̄ (formas diferenciais) |
| 15 · Integrais | integração de formas sobre ciclos (períodos) |
| 16 · Limites | não se aplica |
| 21 · Exemplos (no kernel) | `ATK.Hodge.linear_realization`; `ATK.ModelosSete.hodge_modelo`; `ATK.ModelosSete.posto_nulidade` |
| 22 · Contraexemplos (no kernel) | a versão integral é falsa (Atiyah–Hirzebruch): por isso o enunciado é racional |

### T07 — `Hodge:PROVA_DA_PONTE_B5`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T07 · `ATK.Termos.Hodge.ponteB5` · ponte B5 · rota prova |
| 2 · Definição formal | casos conhecidos: p ≤ 1 (Lefschetz (1,1)) e p ≥ dim X − 1 — tipo Lean `ATK.Termos.Hodge.ponteB5 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.Hodge.hodge_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.Hodge.fecha`; `ATK.Termos.Hodge.decomposicao` |
| 19 · Dependências | `ATK/Termos.lean`; L3 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.Hodge.terminal` |
| 23 · Certificado Lean | teorema publicado; falta formalizar · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/Hodge.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T08 — `Hodge:PROVA_DO_PRODUTOR_O5`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T08 · `ATK.Termos.Hodge.produtorO5` · produtor O5 · rota prova |
| 2 · Definição formal | codimensões do meio 2 ≤ p ≤ dim X − 2 — tipo Lean `ATK.Termos.Hodge.produtorO5 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.Hodge.hodge_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.Hodge.fecha`; `ATK.Termos.Hodge.decomposicao` |
| 19 · Dependências | `ATK/Termos.lean`; L3 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.Hodge.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/Hodge.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T18 — `HodgeRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T18 · `ATK.Termos.Hodge.refutacao` · refutacao ¬Hodge · rota refutacao |
| 2 · Definição formal | uma classe de Hodge racional não algébrica; com B5, em codimensão do meio e dim X ≥ 4 — tipo Lean `ATK.Termos.Hodge.refutacao modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.Hodge.hodge_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.Hodge.refutacao_iff`; `ATK.Termos.Hodge.refutacao_meio`; `ATK.Termos.Hodge.refutacao_nega_produtor` |
| 19 · Dependências | `ATK/Termos.lean`; L3 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.HodgeRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/HodgeRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T23 — `HodgeModelo:LIGACAO_L3`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T23 · `ATK.Termos.Ligacoes.L3` · ligacao L3 · rota prova+refutacao |
| 2 · Definição formal | variedades projetivas complexas lisas, H^{2p}(X, ℚ), tipo (p, p) e classes de ciclos algébricos — tipo Lean `ATK.Termos.Ligacoes.L3` |
| 3 · Tipo matemático | dado: estrutura HodgeModel.{0,0} |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.Hodge.hodge_conditional` |
| 17 · Hipóteses | o modelo tem de satisfazer o critério de fidelidade da ligação |
| 18 · Lemas (certificados, do termo) | — (dado; critério na linha) |
| 19 · Dependências | `ATK/Termos.lean`; L3 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.HodgeModelo.modeloGenuino` |
| 23 · Certificado Lean | ABERTA — Mathlib sem cohomologia singular com decomposição de Hodge · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/HodgeModelo.lean.tpl` · `atk-kernel/scripts/termos.json` |

## BSD — Birch e Swinnerton-Dyer

Enunciado oficial no portão: BSDFull modeloGenuino. Ligação: L4 aberta. Mathlib: tem WeierstrassCurve; falta L(E, s) e o posto de Mordell–Weil.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | curvas elípticas E/ℚ; grupo de Mordell–Weil E(ℚ); L(E, s) |
| 5 · Classes numéricas | ℤ, ℚ, ℝ, ℂ |
| 6 · Parâmetros | modelo M : BSDModel (L4) |
| 7 · Operadores | posto, ord_{s=1}, altura de Néron–Tate, regulador (det), Ω_E, Ш, c_p |
| 9 · Invariantes | posto r; torção; condutor |
| 10 · Dimensão | curva (dimensão 1); E(ℚ) ≅ ℤ^r ⊕ T |
| 11 · Geometria | geometria aritmética; cúbicas de Weierstrass |
| 12 · Coordenadas | y² = x³ + ax + b (WeierstrassCurve) |
| 13 · Métrica ou topologia | pareamento de alturas ⟨P, Q⟩ |
| 14 · Derivadas | L^{(r)}(E, 1) |
| 15 · Integrais | período Ω_E = ∫_{E(ℝ)} \|dx/2y\| |
| 16 · Limites | lim_{s→1} L(E, s)/(s − 1)^r |
| 21 · Exemplos (no kernel) | `ATK.BSD.regulator_det_identity`; `ATK.ModelosSete.Hb_det`; `ATK.CongruentCurve.E_torsion_points` |
| 22 · Contraexemplos (no kernel) | `ATK.BSD.sha_recovery` isola #Ш só supondo a fórmula (não é prova) |

### T09 — `BSD:PROVA_DA_PONTE_B6`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T09 · `ATK.Termos.BSD.ponteB6` · ponte B6 · rota prova |
| 2 · Definição formal | Gross–Zagier–Kolyvagin: posto analítico ≤ 1 ⇒ posto = posto analítico — tipo Lean `ATK.Termos.BSD.ponteB6 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.BSD.bsd_rank_conditional`; `ATK.Conditional.BSD.bsd_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.BSD.fecha`; `ATK.Termos.BSD.decomposicao` |
| 19 · Dependências | `ATK/Termos.lean`; L4 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.BSD.terminal` |
| 23 · Certificado Lean | teorema publicado; falta formalizar · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/BSD.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T10 — `BSD:PROVA_DO_PRODUTOR_O6`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T10 · `ATK.Termos.BSD.produtorO6` · produtor O6 · rota prova |
| 2 · Definição formal | posto analítico ≥ 2 ⇒ posto = posto analítico — tipo Lean `ATK.Termos.BSD.produtorO6 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.BSD.bsd_rank_conditional`; `ATK.Conditional.BSD.bsd_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.BSD.fecha`; `ATK.Termos.BSD.decomposicao` |
| 19 · Dependências | `ATK/Termos.lean`; L4 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.BSD.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/BSD.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T11 — `BSD:PROVA_DO_PRODUTOR_O7`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T11 · `ATK.Termos.BSD.produtorO7` · produtor O7 · rota prova |
| 2 · Definição formal | Ш finito e fórmula do termo líder, para toda E/ℚ — tipo Lean `ATK.Termos.BSD.produtorO7 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.BSD.bsd_rank_conditional`; `ATK.Conditional.BSD.bsd_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.BSD.fecha`; `ATK.Termos.BSD.decomposicao` |
| 19 · Dependências | `ATK/Termos.lean`; L4 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.BSD.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/BSD.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T19 — `BSDRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T19 · `ATK.Termos.BSD.refutacao` · refutacao ¬BSD · rota refutacao |
| 2 · Definição formal | uma curva com posto ≠ posto analítico (com B6: posto analítico ≥ 2) ou em que a fórmula refinada falha — tipo Lean `ATK.Termos.BSD.refutacao modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.BSD.bsd_rank_conditional`; `ATK.Conditional.BSD.bsd_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.BSD.refutacao_iff`; `ATK.Termos.BSD.refutacao_posto` |
| 19 · Dependências | `ATK/Termos.lean`; L4 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.BSDRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/BSDRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T24 — `BSDModelo:LIGACAO_L4`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T24 · `ATK.Termos.Ligacoes.L4` · ligacao L4 · rota prova+refutacao |
| 2 · Definição formal | curvas elípticas sobre ℚ com posto de Mordell–Weil, L(E, s), regulador, Ш, c_p e torção — tipo Lean `ATK.Termos.Ligacoes.L4` |
| 3 · Tipo matemático | dado: estrutura BSDModel.{0} |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.BSD.bsd_rank_conditional`; `ATK.Conditional.BSD.bsd_conditional` |
| 17 · Hipóteses | o modelo tem de satisfazer o critério de fidelidade da ligação |
| 18 · Lemas (certificados, do termo) | — (dado; critério na linha) |
| 19 · Dependências | `ATK/Termos.lean`; L4 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.BSDModelo.modeloGenuino` |
| 23 · Certificado Lean | ABERTA — Mathlib sem L(E, s) e sem posto de Mordell–Weil · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/BSDModelo.lean.tpl` · `atk-kernel/scripts/termos.json` |

## YM — Yang–Mills e gap de massa

Enunciado oficial no portão: ClayYM modeloGenuino. Ligação: L5 aberta. Mathlib: sem teoria quântica de campos construtiva.

| Componente (domínio da linha) | Conteúdo |
|---|---|
| 4 · Domínio e codomínio | grupos de Lie compactos simples G; teorias quânticas de Yang–Mills em ℝ⁴ |
| 5 · Classes numéricas | ℝ, ℂ |
| 6 · Parâmetros | modelo M : YMModel (L5) |
| 7 · Operadores | curvatura F = dA + A∧A, Hamiltoniano H, reconstrução de Osterwalder–Schrader |
| 9 · Invariantes | invariância de calibre; simetria euclidiana/Poincaré |
| 10 · Dimensão | 4 (espaço-tempo); Hilbert de dimensão infinita |
| 11 · Geometria | conexões em fibrados principais |
| 12 · Coordenadas | x ∈ ℝ⁴ (euclidiano) / Minkowski |
| 13 · Métrica ou topologia | espectro de H ⊆ {0} ∪ [Δ, ∞) |
| 14 · Derivadas | derivada covariante D_A |
| 15 · Integrais | medida euclidiana (integral funcional) |
| 16 · Limites | limite contínuo; decaimento e^{−m\|x\|} das correlações |
| 21 · Exemplos (no kernel) | `ATK.YMToy.massa_pos`; `ATK.ModelosSete.gap_toro` |
| 22 · Contraexemplos (no kernel) | `ATK.YMToy.massa_tende_zero` |

### T12 — `YM:PROVA_DA_PONTE_B7`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T12 · `ATK.Termos.YM.ponteB7` · ponte B7 · rota prova |
| 2 · Definição formal | reconstrução de Osterwalder–Schrader + teoria espectral — tipo Lean `ATK.Termos.YM.ponteB7 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.YangMills.ym_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.YM.fecha` |
| 19 · Dependências | `ATK/Termos.lean`; L5 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.YM.terminal` |
| 23 · Certificado Lean | teorema publicado; falta formalizar · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/YM.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T13 — `YM:PROVA_DO_PRODUTOR_O8`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T13 · `ATK.Termos.YM.produtorO8` · produtor O8 · rota prova |
| 2 · Definição formal | para todo G compacto simples, medida euclidiana de YM em ℝ⁴ com axiomas OS e clustering de taxa m > 0 — tipo Lean `ATK.Termos.YM.produtorO8 modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.YangMills.ym_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.YM.fecha` |
| 19 · Dependências | `ATK/Termos.lean`; L5 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.YM.terminal` |
| 23 · Certificado Lean | ABERTA — problema em aberto · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/YM.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T20 — `YMRefutacao:PROVA_DA_REFUTACAO`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T20 · `ATK.Termos.YM.refutacao` · refutacao ¬ClayYM · rota refutacao |
| 2 · Definição formal | um G compacto simples sem teoria quântica de YM com gap positivo — tipo Lean `ATK.Termos.YM.refutacao modeloGenuino` |
| 3 · Tipo matemático | Prop (proposição) |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.YangMills.ym_conditional` |
| 17 · Hipóteses | nenhuma: o portão exige um termo sem hipóteses |
| 18 · Lemas (certificados, do termo) | `ATK.Termos.YM.refutacao_iff`; `ATK.Termos.YM.refutacao_nega_produtor` |
| 19 · Dependências | `ATK/Termos.lean`; L5 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.YMRefutacao.refutacao` |
| 23 · Certificado Lean | ABERTA — nenhum contraexemplo conhecido · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/YMRefutacao.lean.tpl` · `atk-kernel/scripts/termos.json` |

### T25 — `YMModelo:LIGACAO_L5`

| Componente | Conteúdo |
|---|---|
| 1 · Identidade | T25 · `ATK.Termos.Ligacoes.L5` · ligacao L5 · rota prova+refutacao |
| 2 · Definição formal | teorias quânticas de campos em ℝ⁴ (axiomas de Wightman/Osterwalder–Schrader) e medidas euclidianas de YM — tipo Lean `ATK.Termos.Ligacoes.L5` |
| 3 · Tipo matemático | dado: estrutura YMModel.{0,0,0} |
| 8 · Leis (certificadas, da linha) | `ATK.Conditional.YangMills.ym_conditional` |
| 17 · Hipóteses | o modelo tem de satisfazer o critério de fidelidade da ligação |
| 18 · Lemas (certificados, do termo) | — (dado; critério na linha) |
| 19 · Dependências | `ATK/Termos.lean`; L5 aberta |
| 20 · Obrigação terminal | alimenta `ATK.Terminal.YMModelo.modeloGenuino` |
| 23 · Certificado Lean | ABERTA — Mathlib sem teoria quântica de campos construtiva · tipo conferido pelo kernel |
| 24 · Proveniência | `atk-kernel/terminal-templates/YMModelo.lean.tpl` · `atk-kernel/scripts/termos.json` |

