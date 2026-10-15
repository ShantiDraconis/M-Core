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
