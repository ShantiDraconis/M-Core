# atk-kernel

Pasta independente do restante do repositório (lakefile e Mathlib próprios).

Verificação no kernel do Lean 4 (Mathlib `v4.34.1`) dos lemas auxiliares do programa ATK,
com auditoria automática de axiomas no GitHub Actions.

## O que roda a cada push

**Job `kernel`**
1. Instala o Lean e baixa a Mathlib já compilada.
2. Roda `lake build`.
3. Compila cada arquivo `ATK/*.lean` separadamente e executa os `#print axioms` do final de cada um.
4. `scripts/check_axioms.py` marca cada teorema como **CERTIFIED** só se:
   * o arquivo compilou sem erro, e
   * os axiomas usados estão entre `propext`, `Classical.choice` e `Quot.sound`, e
   * a fonte não contém `sorry`, `admit` ou `axiom`.

   Um teorema com erro entra no ambiente com `sorryAx` e é reprovado automaticamente.
5. A tabela aparece no resumo da execução, e os logs ficam no artefato `atk-kernel-report`.

**Job `numerics`**
Reproduz o resíduo real D_N de Nyman–Beurling/Báez-Duarte para N ≤ 300, em 40 e 60 dígitos.
O arquivo `numerics/dn_N1500_prec45.csv` traz a tabela até N = 1500.

## Teoremas (51 = 19 lemas auxiliares + 14 condicionais + 14 de regimes + 4 de ClosedMath)

| Arquivo | Conteúdo | Observação |
|---|---|---|
| `NavierStokes` | absorção; δ > 0; comparação de Riccati; cota y(t) ≤ y₀/(1−2Cy₀t) | estimativa local, não regularidade global |
| `Riemann` | majorante ⇒ D_N → 0; passo de Schur; identidade e cota da Gram | o majorante uniforme implica RH e continua aberto |
| `YangMills` | Cauchy–Schwarz ponderado; inclinação da massa efetiva ≤ 0 | não constrói a teoria 4D nem o gap |
| `BSD` | det 2×2; regulador > 0; recuperação de #Ш **assumindo** a fórmula | não prova BSD |
| `Hodge` | realização linear única com matriz invertível | pressupõe que os ciclos existem |
| `Beal` | gcd(x,y,z) ≤ 2 **dado** Fermat (hipótese `hFLT`) | Fermat ainda não está todo formalizado na Mathlib |
| `PvsNP` | P⊆P/poly ∧ NP⊄P/poly ⇒ P≠NP; SAT∈NP ∧ SAT∉P ⇒ P≠NP | só a forma lógica, sem máquinas de Turing |
| `Geometry` | ∫R dV = 12π²a na S³ redonda | identidade algébrica |

### Condicionais (`ATK/Conditional/`)

Molde: PONTE (literatura, não formalizada) → HIPÓTESE ABERTA → ENUNCIADO. Ambas entram como
argumentos explícitos; detalhes em `scripts/conditionals.json`.

| Arquivo | Teorema principal | Enunciado |
|---|---|---|
| `Conditional/Riemann` | `riemann_conditional` (+ `DN_nonneg`, `DN_tendsto_zero`) | `RiemannHypothesis` da Mathlib |
| `Conditional/Beal` | `beal_conditional` (+ `beal_iff_gcdLowerBound`, `exponent_gcd_le_two`, `one_lt_gcd_iff`) | enunciado elementar completo |
| `Conditional/NavierStokes` | `ns_conditional` | relativo a `NSModel` |
| `Conditional/PvsNP` | `pvsnp_conditional` (+ `pneNP_iff_sat_not_in_P`) | relativo a `ComplexityModel` |
| `Conditional/Hodge` | `hodge_conditional` | relativo a `HodgeModel` |
| `Conditional/BSD` | `bsd_conditional` (+ `bsd_rank_conditional`) | relativo a `BSDModel` |
| `Conditional/YangMills` | `ym_conditional` | relativo a `YMModel` |

### Regimes do gateway (`ATK/Regimes.lean`)

Núcleo incondicional `W_strictMono` (W = W₀ + 10⁻⁶·t, independente de Seff — `W_ignores_Seff`),
classificação dos regimes vácuo/suave/crítico/explosão, histerese sem flapping, custo de
tunelamento, gatilhos H1 (RH) e H3 (BSD, forma correta) e ruído. Camada de simulação: não
toca `OPEN_MATH`.

### ClosedMath (`ATK/ClosedMath.lean`)

Teorema-mestre `closedMath_of_obligations : Bridges M → OpenObligations M → SevenStatements M`,
a versão oficial `closedMathFaithful_of_obligations` (RH ∧ Beal) e dois testes de firewall
(modelos de brinquedo). `CLOSED_MATH` é calculado pelo portão `ATK/ClosedMathGate.lean`
(regra em `scripts/obligations.json`); hoje o portão está ausente.

Nenhum destes teoremas prova uma conjectura do milênio: `OPEN_MATH = true`.

## ATK-Ω / ATK-I / ATK-RH (branch atk/rh-rho-independent)

| Arquivo | Conteúdo | O que NÃO é |
| --- | --- | --- |
| `ATK/RhoIndependente.lean` | ρ_m é função escada; independência linear de {ρ_m : m ≥ 2} em ℝ | não decide D_N → 0 |
| `ATK/OmegaEstados.lean` | álgebra de estados Todo/Nada/I, involução, idempotência, `detectarZero_iff`, indicadores GREEN/OPEN, "inversão não certifica" | não altera flags |
| `ATK/OmegaContracao.lean` | teorema de contração acoplada (norma ∞, versão perturbada), redução 8→7, contraexemplo diag(1,1/2), certificação condicional | A e a fidelidade são hipóteses |
| `ATK/OmegaClasses.lean` | classes R, P, N, Y, B, H, E, T: leis de fechamento e exemplos calculados | T é interface, não a prova de Perelman |
| `ATK/OmegaGramRho.lean` | Gram de ρ definida positiva, equações normais, completar o quadrado, erro mínimo, cota de truncamento | produto interno de L² entra como hipótese `DetectsSteps` |

Estado: 0/8 produtores terminais. `OPEN_MATH=true`, `CLOSED_MATH=false`.
| `ATK/OmegaGramL2.lean` | **incondicional**: a matriz de Gram de ρ_{m_i} em L²(0,1) é definida positiva (`gramL2_posDef`); descarrega `DetectsSteps` no caso real | não decide D_N → 0 |
| `ATK/Orion.lean` | Orion/UCIF (κ, P_Ω, Hidden-State) corrigido e compilado; HREF Lei 5 (identidade de energia) como **teorema** num espaço de Hilbert real; Lei 7 e absorção; lacunas B3/B4/B5 e Leis 3/4/6 como hipóteses explícitas | não toca O1–O8 |
| `ATK/OrionAlcance.lean` | o alcance da análise Orion: teorema-mãe = Banach (Mathlib); **não-go** da regularização dual (C_ε⁻¹C_ε = 1, não ⊥); Re ρ = ½ ⇔ 1 − ρ̄ = ρ; lema de focalização HREF L2/L3 (Θ' ≤ −aΘ², Θ(t₀) < 0 ⇒ T ≤ t₀ + 1/(a|Θ(t₀)|)); classificação de defeitos | Lei 6 (a desigualdade vale para NS) segue OPEN |
| `ATK/GramBaezDuarte.lean` | **fórmula de Gram certificada para o D_N real**: Gram de ρ_k(t) = {1/(kt)} em L²(0,∞) é definida positiva (todo N); o ínfimo é atingido em c* = G⁻¹b, único; **D_N = 1 − b·G⁻¹b**; b_k = ∫₀¹ ρ_{k+1}; ponte {1/(kt)} = ρ^{NB}_k + (1/k){1/t} | O1 (D_N → 0) segue OPEN; valores numéricos de G (Vasyunin) e b (γ) não formalizados |
| `ATK/BaezDuarteVetorB.lean` | **vetor b em forma fechada**: ∫₀¹ {1/x} dx = 1 − γ (γ de Euler–Mascheroni da Mathlib); ∫₀¹ {1/(kt)} dt = (log k + 1 − γ)/k; b_j = (log(j+1) + 1 − γ)/(j+1) — a fórmula de `numerics/nb_gram.py`; b_j > 0 | entradas G_{jk} (Vasyunin) não formalizadas; O1 segue OPEN |
| `ATK/RelacionalI.lean` | **ATK-I — álgebra relacional** 𝔍(K) = (K², ⊕, ⊗, d, ≽, T, 𝒯): d R = 0 ⟺ R ∈ 𝒯; desigualdades de defeito; fechamento simultâneo de famílias finitas; Teorema de preservação e fechamento; classes 𝒫 (preservam verdade) e 𝒞 (contraem defeito) **independentes**; aproximação ≠ igualdade (T ∈ 𝒫∩𝒞_q, órbita falsa com d → 0); o limite certifica; **transporte de certificados** por morfismos isométricos (ℚ→ℝ, ℝ→ℂ) | linguagem; não fecha conjecturas |
| `ATK/RelacionalLeis.lean` | ATK-I Nível I completo: anel comutativo, 𝒯 subanel, d(Rⁿ) = d(R)·‖Σaʲbⁿ⁻¹⁻ʲ‖, R(−1,1)² verdadeira, pré-ordem não antissimétrica, ⊕ não passa ao quociente, transição T_t∘T_s = T_{s+t−st} e T_1 (normalização) ∉ 𝒫, três estados, **Σwᵢ(aᵢ−bᵢ)² = 0 ⟺ ∀i aᵢ = bᵢ** (7 relações) e fechamento artificial por T_1, defeito infinitesimal (hiper-reais) ≠ 0 | ALGEBRA_GREEN; aplicação OPEN |
| `ATK/RelacionalTransporte.lean` | transformações certificadas: fidelidade e transporte de provas, cinco classes (equivalência, suficiência, necessidade, contração, obstrução), não colapso c>0 e controle ω (com composição), cota uniforme, R(3,5) com T_n = escala 1/(n+1) sem cota uniforme, obstrução modular (2³+3³ ≢ 3³ mod 3), famílias: aplicar f é fiel ⟺ f injetiva | nenhuma família fecha uma conjectura |
| `ATK/RelacionalDN.lean` | **D_N > 0 para todo N (incondicional)**; etapas R(D_N,0) todas falsas; R(D_N,0) → R(D_∞,0) e **O1 ⟺ relação-limite verdadeira**; cota uniforme D_N ≥ c > 0 refutaria O1 | O1 segue OPEN |
| `ATK/CapturaIncondicional.lean` | descarrega `hpos` de `CapturaRH`: O1 ⟺ captura logarítmica acumulada **sem hipóteses**; η_N < 1 | O1 segue OPEN |
| `ATK/RefutacoesBeal.lean` | **variantes refutadas em volta de Beal**: as 10 soluções coprimas de Fermat–Catalan (todas com um expoente 2) ⇒ Beal com expoentes ≥ 2 é falso; o fator comum é necessário (2³+2³=2⁴, 3³+6³=3⁵, 7⁶+7⁷=98³, 2ⁿ+2ⁿ=2ⁿ⁺¹); conjectura de Euler das somas de potências falsa (Lander–Parkin, Frye) | nenhum exemplo refuta Beal |
| `ATK/BealPolinomial.lean` | **Beal para polinômios** (via Mason–Stothers/`Polynomial.flt_catalan` da Mathlib): fˣ+gʸ=hᶻ, f,g coprimos, x,y,z>2 ⇒ f,g,h constantes; contraste (7,3,2): polinômios sem solução, inteiros com 2⁷+17³=71² | Beal inteiro segue OPEN (falta o abc inteiro) |
| `ATK/YMSemGap.lean` | por que o grupo precisa ser simples: campo livre na rede — ondas planas autofunções com energia 4sin²(θ/2), **sem massa não há gap**; com massa, ⟨f,(Δ+m²)f⟩ ≥ m²‖f‖² uniforme em L | modelo de brinquedo; YM 4D segue OPEN |
| `ATK/BaseRiemannXi.lean` | **base (falta na Mathlib): a função ξ de Riemann** — ξ(s) = s(s−1)/2·Λ₀(s)+1/2 inteira; ξ(1−s)=ξ(s); **ξ(s̄)=conj ξ(s)** (via `completedRiemannZeta₀_conj`, novo); zeros de ξ = zeros não triviais de ζ, todos em 0<Re<1; **Ξ(t)=ξ(1/2+it) real**, par, contínua; ζ(1/2+it)=0 ⟺ Ξ(t)=0; critério de troca de sinal; **RH ⟺ todos os zeros de z ↦ ξ(1/2+iz) são reais** | base para Hardy e para certificar zeros; RH segue OPEN |
| `ATK/BaseGalerkinNS.lean` | **base (falta na Mathlib): Navier–Stokes de Galerkin em T³** em Fourier — termo convectivo truncado, **cancelamento exato Σ N(u)_k·conj û_k = 0** (truncamento simétrico, div. nula, realidade), Leray não altera o emparelhamento, identidade de energia estática e dinâmica, energia decrescente sem força | existência global do sistema de Galerkin e passagem ao limite: próximos passos; regularidade 3D OPEN |
| `ATK/BaseRedeCalibre.lean` | **base (falta na Mathlib): teoria de calibre na rede** — elos, transformações de calibre (ação de grupo), plaquetas com lei (g•U)_p = g U_p g⁻¹, **ação de Wilson invariante de calibre** para qualquer função de classe; Re tr é função de classe em U(N) | limite contínuo e gap de Yang–Mills OPEN |
| `ATK/BaseEDODissipativa.lean` | **base N2: existência e unicidade globais para EDOs dissipativas** — F localmente Lipschitz e ⟪F v, v⟫ ≤ 0 ⇒ solução em [0,T] para todo T, ‖u(t)‖ ≤ ‖u(0)‖; retração radial 2-Lipschitz; unicidade | instância Galerkin: `BaseGalerkinGlobal` |
| `ATK/BaseWilsonMedida.lean` | **base Y2: medida de Wilson** — medida produto (μ bi-invariante, ex. Haar de grupo compacto) preservada por toda transformação de calibre; esperanças com peso de Wilson exp(−βS) invariantes de calibre | positividade por reflexão e gap OPEN |
| `ATK/BaseGalerkinGlobal.lean` | **base N2b: soluções globais de Galerkin** — para K finito e simétrico, o subespaço admissível (divergência nula + realidade û(−k) = conj û(k)) é invariante pelo campo de Galerkin de Navier–Stokes; o campo é C¹ (logo localmente Lipschitz) e dissipativo (⟪F u, u⟫ = −ν Σ|k|²|û_k|² ≤ 0) ⇒ para todo T ≥ 0 existe solução em [0,T] com ‖u(t)‖ ≤ ‖u(0)‖ | compacidade (Aubin–Lions) e soluções fracas de Leray: N3–N5 |
| `ATK/BaseRiemannXiSinal.lean` | **base R2: sinal de ξ** — Γℝ(σ) real positiva para σ > 0; ξ(σ) real **positiva em toda a reta real** (ζ(σ) < 0 em (0,1) do kernel, ζ(σ) > 0 para σ > 1); ξ(1/2) = −Γℝ(1/2)ζ(1/2)/8; **Ξ(0) > 0**; Ξ(t) < 0 para algum t > 0 ⇒ zero de ζ na reta crítica com altura em (0,t) | Hardy (infinitas trocas de sinal) OPEN como base: R3–R4 |
| `ATK/BaseNagellLutzDois.lean` | **base B1b (parcial): Nagell–Lutz para a 2-torsão** — raiz racional de cúbica mônica inteira é inteira e divide o termo constante; todo ponto racional de ordem 2 de y² = x³ + a₂x² + a₄x + a₆ (aᵢ ∈ ℤ) tem y = 0 e x ∈ ℤ, x ∣ a₆; \|E[2]\| ≤ 4 sobre qualquer corpo de car ≠ 2 | Nagell–Lutz geral (filtração p-ádica) e redução mod p: próximos passos |
| `ATK/BaseRiemannTeta.lean` | **base R3: fórmula integral de Riemann para Ξ** — dobra de Mellin para FE-pairs (Λ₀(s) = M[cauda f](s) + ε·M[cauda g](k−s)); ψ(x) = (θ(x)−1)/2 = Σ_{n≥1} e^{−πn²x} > 0; Λ₀(s) = ∫₁^∞ ψ(x)(x^{s/2−1} + x^{(1−s)/2−1}) dx; **Ξ(t) = 1/2 − (t² + 1/4) ∫₁^∞ ψ(x) x^{−3/4} cos((t/2) log x) dx** | teorema de Hardy (R4) OPEN como base |
| `ATK/BaseHodgeLinear.lean` | **base H1: álgebra linear de Hodge (peso 1)** — com J² = −1: W = H^{1,0} ⊕ H^{0,1} (ker(J∓i)); uma conjugação σ que comuta com J troca as partes; h^{1,0} = h^{0,1}; dim W = 2h^{1,0} | Hodge em Kähler e Lefschetz (1,1): fora da Mathlib atual |
| `ATK/BaseGalerkinDecaimento.lean` | **base N3 (parte discreta): Poincaré em Fourier e decaimento** — decaimento exponencial abstrato (⟪F v, v⟫ ≤ −c‖v‖² ⇒ ‖u(t)‖ ≤ e^{−ct}‖u(0)‖); k ≠ 0 ⇒ λ_k ≥ 4π²; Parseval; em média nula, soluções globais de Galerkin com ‖u(t)‖ ≤ e^{−4π²νt}‖u(0)‖ | espaços L²_σ/H¹ contínuos, Aubin–Lions, Leray: N3–N5 |
| `ATK/BasePositividadeReflexao.lean` | **base Y3 (forma abstrata): positividade por reflexão (Osterwalder–Seiler)** — em Ω = X × X com μ ⊗ μ (μ finita) e θ(a,b) = (b,a): se −S(a,b) = B(a) + B(b) + Σᵢ cᵢCᵢ(a)Cᵢ(b) com cᵢ ≥ 0, então ∫ F(a)F(b)e^{−S} ≥ 0 para toda F limitada mensurável; expansão tensorial de Eⁿ, momentos (∫f)² ≥ 0, troca série–integral | decomposição da ação de Wilson nessa forma, gap em acoplamento forte: Y3'–Y4 |
| `ATK/BaseReducaoDois.lean` | **base B2 (parcial): redução mod p na 2-torsão** — Δ = 16d (d = discriminante da cúbica) para a₁ = a₃ = 0; com duas raízes inteiras distintas, d = ((x−y)(x−z)(y−z))²; p ∤ d ⇒ raízes distintas mod p; dois pontos racionais distintos de ordem 2 têm x inteiros distintos em ZMod p (redução injetiva em E(ℚ)[2]) | redução injetiva em toda a torsão (grupo formal): B2 |
| `ATK/BaseToroPoincare.lean` | **base N3 (contínua): Poincaré em L²(Tᵈ) e mergulho de Galerkin** — f̂₀ = média; H¹ lido em Fourier; **Poincaré**: média nula ⇒ ∫\|f\|² ≤ Σ\|k\|²\|f̂_k\|² = (2π)⁻²‖∇f‖²; polinômios trigonométricos (coeficientes e energia); um estado de Galerkin é um campo de L²(T³)³ com Σᵢ∫\|uᵢ\|² = ‖x‖²; energia contínua das soluções globais ≤ e^{−8π²νt}‖x₀‖² | L²_σ e Leray em L², Aubin–Lions: N3b–N5 |
| `ATK/BaseLerayL2.lean` | **base N3b: L²_σ(T³) e projeção de Leray em L²** — coeficiente de Fourier como funcional contínuo; L²_σ = ⋂ₖ ker(Σᵢ kᵢûᵢ(k)) fechado em L²(T³)³; Leray = projeção ortogonal (P u ∈ L²_σ, P u = u ⟺ u ∈ L²_σ, P² = P, ‖P u‖ ≤ ‖u‖); estados admissíveis de Galerkin estão em L²_σ e são fixados por P | fórmula de multiplicador, Aubin–Lions: N4 |
| `ATK/AtaqueBSD.lean` | **programa de ataque, frente 1: BSD (posto) para y² = x³ − x módulo duas pontes publicadas** — teta da curva como FE-pair de peso 2; Λ(1) = (1+ε)∫₁^∞ g pela dobra de Mellin; Λ(s) = Γ(s)c^{−s}L(E,s) em Re s > 2; toda continuação de L(E,s) é c^sΛ(s)/Γ(s); critério: sinal +1, \|aₙ\| ≤ n e N < (2π/log 2)² ⇒ L(E,1) ≠ 0; para y² = x³ − x: G(1) ≠ 0 e ordem 0 = posto | pontes P1 (modularidade com sinal) e P2 (\|aₙ\| ≤ n) explícitas; ver `ATAQUE.md` |
| `ATK/AtaqueRH.lean` | **frente RH** — infinitas trocas de sinal de Ξ ⇒ Hardy; Ξ(t) < 0 ⇒ zero na reta; certificados de sinal pela integral de Riemann; dois certificados opostos ⇒ zero entre eles | Hardy e o certificado numérico (F3.4–F3.5) OPEN como marcos |
| `ATK/AtaqueNS.lean` | **frente NS** — Explosão ⟺ ¬(enunciado A); dicotomia; com a ponte de Leray, explosão ⇒ enstrofia ilimitada antes de T; regularidade ⇐ cota a priori | perfil autossimilar e estabilidade certificada (F2.4–F2.5) |
| `ATK/AtaquePvsNP.lean` | **frente P vs NP** — fatias booleanas de linguagens, cotas inferiores de circuitos, P/poly; P ⊆ P/poly ∧ NP ⊄ P/poly ⇒ P ≠ NP; fronteira linear em NP monótona | ponte P ⊆ P/poly (Savage) explícita; O4 OPEN |
| `ATK/AtaqueYM.lean` | **frente YM** — FormaRefletida (−S = B(a) + B(b) + Σ cᵢCᵢ(a)Cᵢ(b)) ⇒ positividade por reflexão; estável por soma; ações de metades | FormaRefletida para Wilson (F5.3), gap (F5.4) |
| `ATK/BaseIntervalar.lean` | **base: aritmética intervalar certificada sobre ℚ** — soma, negação, diferença e produto corretos; sinal certificado; exp com resto de Lagrange; π ∈ [3,14; 3,15]; exemplo e^{−1} < 0,37 calculado em ℚ | infraestrutura das frentes NS e RH |
| `ATK/BaseHasseCurva32.lean` | **base: cota de Hasse para y² = x³ − x sobre corpos finitos (Gauss, Jacobsthal)** — S(k) = Σχ(x(x²+k)); S(kt²) = χ(t)S(k); Σ_k χ((k+a)(k+b)) = −1; Σ_k S(k)² = 2q(q−1); S(1)² + S(g)² = 4q; traço nulo se −1 não é quadrado; (Σχ(x³−x))² ≤ 4q; #afins = q + Σχ(x³−x) | núcleo aritmético da ponte P2 |
| `ATK/PonteCoefCurva32.lean` | **ponte P2 reduzida à ponte definicional P2a** — recursão de Hecke e invariante c_{k+1}² − a c_{k+1}c_k + p c_k² = p^{k+1}; (4p − a²)c_k² ≤ 4p^{k+1}; \|c_k(a_p, p)\| ≤ p^k para todo primo ímpar; a_p² ≠ 4p; FatoresPadrao ⇒ \|aₙ\| ≤ n (multiplicatividade); BSD (posto) para y² = x³ − x módulo P1 e P2a | P2a provada em `PonteFatoresCurva32` |
| `ATK/PonteFatoresCurva32.lean` | **ponte P2a provada: os fatores locais de L(E, s) da Mathlib para y² = x³ − x** — coeficientes de 1/(1 − aX + qX²) = recursão de Hecke; corpo residual de ℤ_v tem p elementos (ℤ_v ≅ ℤ_p); a_{p^k} = [X^k] da série local (produto de Euler, Northcott); em p ímpar o modelo minimal desce a ℤ_v e #Ẽ(𝔽_p) = p + 1 + Σχ(x³ − x); em 2 a redução é aditiva (2 uniformizador, paridade de v(Δ), c₄³ = 1728Δ); FatoresPadrao; **\|aₙ\| ≤ n incondicional**; BSD (posto) para y² = x³ − x módulo só P1 | P1 provada em `PonteModularCurva32` |
| `ATK/BaseGaussPrimario.lean` | **base: inteiros de Gauss primários (α ≡ 1 mod 2+2i)** — monoide; associado primário único de todo α de norma ímpar; Σ_{α primário, Nα = n} α multiplicativa (fatoração única em ℤ[i]); valores em 2^k (0), p ≡ 3 mod 4 (c_k(0, p)) e p = ππ̄ (c_k(2 re π, p)) | caráter de Hecke de ℚ(i) |
| `ATK/BaseGaussCurva32.lean` | **base: a_p = π + π̄ para y² = x³ − x (Gauss)** — 8 ∣ #E(𝔽_p) se i ∈ 𝔽_p (ponto (i, 1 − i) de ordem 4); a_p² + S(g)² = 4p; π = a_p/2 + (S(g)/2)i primário; a_p = 0 se p ≡ 3 mod 4; **aₙ = Σ_{α primário, Nα = n} α** para os coeficientes da Mathlib | CM de y² = x³ − x |
| `ATK/PonteModularCurva32.lean` | **ponte P1 provada: equação funcional modular de y² = x³ − x** — g(x) = Σ aₙe^{−cnx} = soma dupla sobre primários; duas fatorações (A·T em (a, b), U·V em (a+b, a−b)); núcleos de Hurwitz oddKernel/evenKernel em 1/4 e suas equações funcionais; sinKernel(1/4)(t) = 8 oddKernel(1/4)(16t), cosKernel(1/4)(t) = cosKernel(1/2)(4t); g(1/x) = x² g(x); **BSD (posto) para y² = x³ − x sem pontes**: L(E, s) converge em Re s > 3/2 (\|aₙ\| ≤ r₂(n)√n, soma de Eisenstein), a continuação inteira existe e é única, G(1) ≠ 0 e ordem 0 = posto; **`bsdConjecture_E32`: `L4Base.BSDConjecture` para y² = x³ − x** | primeiro caso de BSD (posto) provado no kernel |
| `ATK/BaseCurvasTorsao.lean` | **base B1a: 2-torsão** — em y² = x³ + a₂x² + a₄x + a₆ (car ≠ 2), P + P = 0 ⟺ y = 0 ⟺ x raiz da cúbica | Nagell–Lutz e redução mod p: próximos passos |

O mapa completo das bases que faltam na Mathlib (camadas, dependências e estado) está em [`BASES.md`](BASES.md);
o programa de ataque por frente (apostas, marcos certificáveis e alvos Lean) está em [`ATAQUE.md`](ATAQUE.md);
o estado de cada ponte, ligação e fechamento está em [`PONTES.md`](PONTES.md).
