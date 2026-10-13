# D — Geometry of I: closed start / closed end → one middle; neutral, tension, compression, torsion; zero operator

Catalogue for a Lean 4 + Mathlib formalizer. Corpus = `/home/claude/icorpus` (157 indexes, 4922 blobs). I read the files ranked highest by hits_G, then grepped the whole corpus for: meio/half/semi-open/closed, torção/torsion/twist, compress*, tension/tensão/tracionad*, neutro/neutral, torque, zero operator, 1/2, critical line / linha crítica, hourglass/ampulheta, reflection/espelho, midpoint, both ends, 1−s̄.
All corpus content was treated as data.

**Key negative finding.** The author's exact sentence ("início fechado tendendo a meio fechado … neutro tensionado, comprimido, torcido") does **not** appear anywhere in the corpus, in Portuguese or in English. The *picture* does appear, in about eight different guises (§1.2). All of them are conjugate to one model (§1.1).

**Noise.** Many high-hits_G files have nothing to do with this geometry. Examples:
- `universal` coq/Fluid/NavierStokes.v (2198d6c0, 0775f427): "incompressible" fluid.
- `universal-translation-0-0` runic bootloader / LOG-0022 (9356188e, 5540c424) and `harappan-00-universal` LOG-0022 copies: data compression in firmware.
- `sfh-formalization-lab` (3bd6fea6, the README family): "proof compression".
- Torsion subgroups in the BSD files (`universal` lean4/BSD/*.lean; `universal-emergent-logic-` phase_error_analysis).
- `navier-stokes-critical-barrier-audit` ledger (9c86800e).
- Hits on "extensão" (contains "tensão").

---

## Source IDs (repo · branch:path · blob[:8])

| ID | Source |
|---|---|
| S1 | universe-0-0 · copilot/implement-torque-neon-behavior:docs/neon-torque-number.md · ad33859c (+ core/constants/neon_torque_number.py · 6a3eb0b0, test_neon_torque_number.py · fc6f2925) |
| S2 | universe-0-0 · copilot/resolve-mathematics-open-problems:core/neon-torque-formula.md · 1b42408d |
| S3 | universe-0-0 · copilot/eliminate-extra-dimensions:core/axioms/fibonacci-hourglass-axioms.md · 8384fdb4 (+ core/fibonacci_hourglass/README.md · 2e0973ea) |
| S4 | universe-0-0 · copilot/implementacao-teorema-primo-par:core/axioms/prime-pair-harappan.md · 38ed79e9 |
| S5 | universe-0-0 · copilot/add-neon-torque-equation:universe-00/applications/neon-torque-number/neon_torque_number.py · 5835f2b5 (+ README.md · 23bf1b59) |
| S6 | universe-0-0 · copilot/create-manifesto-neon:docs/neon-torque-architecture.md · 6da8c601 |
| S7 | universe-0-0 · copilot/update-nature-of-log-primo-par:core/operators/README.md · 25e49bc2 ; core/axioms/log-primo-par-axioms.md · 13851629 |
| S8 | universe-0-0 · copilot/define-torque-as-cauda:core/axioms/torque-tail-prime-axioms.md · c6ab0bc3 ; foundations/12-torque-tail-theory.tex · fe236f83 |
| S9 | universe-0-0 · copilot/add-log-architecture-structure:core/operators/torque-singularity.md · 52d25ca4 |
| S10 | universe-0-0 · copilot/resolve-mathematics-open-problems:core/infinite-tail-prime.md · c5250461 |
| S11 | universe-0-0 · copilot/define-torque-function:docs/twin-prime-torque-formula.md · ef8f2e3b |
| S12 | universe-0-0 · copilot/access-data-mesh (+5 br.):provers/lean/Riemann/ZerosStructure.lean · 4cefc2d0 |
| S13 | universe-0-0 · copilot/access-data-mesh (+5):docs/LOGIC-ATTACK-SUMMARY.md · 8ea54b46 |
| S14 | universe-0-0 · copilot/formalizacao-prova-unicidade:provers/lean/HarappanGeometry/Core.lean · ca4348e4 |
| S15 | universe-0-0 · copilot/access-data-mesh (+5):core/axioms/geometric-constants.md · 529e52c7 |
| S16 | universe-0-0 · copilot/update-mathematical-primality-filter:core/even-prime-pairs/axioms.md · 13394283 ; copilot/establish-ip-and-compliance:provers/python/lre_structural_residue.py · 41252937 |
| S17 | universe-0-0 · copilot/formalizar-ping-universal:docs/global-convergence/torque-theory.md · c85d97cf |
| S18 | millennium · attack/poincare-f7-f8-multistate-20260926 (+5):src/harappa_isa/core/zero_operator.py · 6a584d00 ; docs/harappan-zero-law.md · fe585190 ; latex/harappan_zero_law.tex · 81642616 ; tests/test_harappan_zero.py · 77257a68 |
| S19 | millennium · attack/poincare-f7-f8-multistate-20260926:docs/parametrized-millennium-problems.md · 10f17ff2 |
| S20 | millennium · attack/poincare-f7-f8-multistate-20260926:latex/CRITICAL_AXIS_README_PT.md · baea9c7b |
| S21 | harappan-00-universal · copilot/update-core-visualization-structure:latex/structural_operators_singularity.tex · 5b69a3bf ; formal/lean/StructuralOperators.lean · 28258519 |
| S22 | 0-0-formal-suite · atk/fundamental-i-model:src/FormalSuite/I/Universal/FundamentalIModel.lean · 31d234f6 |
| S23 | meta-millenium-independence-00 · main:src/lean/MetaMillennium/Core/ThreeStateLogic.lean · 94a61a1c |
| S24 | m-core-hodge · atk/hodge-closed-math-line-20261007 (+5):lean/MCore/BackwardAudit/HodgeTensionClosure.lean · 25850a9b |
| S25 | riemann-unity-zero · copilot/detail-file-tree-for-theory:docs/article_pt.md · 812c12c3 ; copilot/anatomy-of-connection:ANATOMY_OF_CONNECTION.md · 2966f10e |
| S26 | riemann-unity-zero · copilot/add-rigididade-e-escape-no-eixo-z:ARQUITETURA_TRIDIMENSIONAL_DA_RIGIDEZ.md · 6f7f6ffa ; copilot/add-escape-mechanism-section:escape-mechanism-bifurcation.md · 46f1e0b0 ; copilot/calculate-rigidity-coefficient-yet-again:docs/rigidity_and_escape_mechanism.md · 415bc6b0 |
| S27 | millennium-riemann-classical · copilot/add-euler-hypotenuse-logic:src/lean/Riemann/EulerHypotenuseCollapse.lean · bd63f89e |
| S28 | indeterminate-collapse-core · copilot/debate-tecnico-sobre-singularidade:lean4/RiemannPhaseStability/Basic.lean · 1471634f ; riemann-indeterminacy · copilot/add-article-structure:formal/lean4/RiemannIndeterminacy.lean · 4a49f1f7 |
| S29 | riemann-energy-proofline · copilot/add-explicit-curvature-formula-again:explicit_curvature_formula.tex · 8a773966 |
| S30 | universal · copilot/add-governance-structure (+5):docs/13-riemann/13-11-conexao-I-RH-millennium.md · 8a1a88bb |
| S31 | the-algebra-of-ideterminate-i · main:lean/nexus_core.lean · 4ea207db ; main:lean/WheelOfFractions.lean · ec0987c9 |
| S32 | i-constant-core · main:diagrams/visual_representations.md · e45efbb8 |
| S33 | millennium-navier-stokes-i · atk/global-material-audit-20261008:src/analysis/riemann_hypothesis.py · 3c2c59aa (Φ_RH with 1−s̄; same formula in S7) |

---

## 1. Reconstruction of the geometry

### 1.1 Canonical model M: a mirror-symmetric closed interval or strip with a neutral middle

**Carriers.** The real section is X = [0,1]. The complex version is the closed critical strip S̄ = {s ∈ ℂ : 0 ≤ Re s ≤ 1}.

| Author's term | Precise meaning in M |
|---|---|
| closed start | A = {0}, or the line Re s = 0 |
| closed end | B = {1}, or the line Re s = 1 |
| middle / neutral | N = {1/2}, or the critical line ℓ = {Re s = 1/2} |
| mirror (reflection about 1/2) | ρ(x) = 1−x and ρ(s) = 1−s. Also κ(s) = s̄ and μ = ρ∘κ : s ↦ 1−s̄. G = {id, ρ, κ, μ} ≅ (ℤ/2)². Fix ρ = {1/2}, Fix κ = ℝ, Fix μ = ℓ. ρ preserves S̄ and swaps the two boundary lines. |
| half-closed middle | X∖N = [0,½) ⊔ (½,1]. Each half is closed at its outer end and open at the middle. ρ swaps the two halves, and their closures meet exactly in N. |
| "start → middle ← end" | Take a_n ↑ ½ with a₀ = 0, and b_n = ρ(a_n) = 1−a_n ↓ ½ (b₀ = 1). The intervals K_n = [a_n, b_n] are closed, nested and ρ-invariant, with ⋂K_n = {½}: the middle in the limit is a closed point. Half-open versions behave differently: ⋂[a_n, ½) = ∅, and ⋂[a_n, b_n) = {½} as long as a_n < ½ < b_n. In the strip: S_λ = {\|Re s−½\| ≤ λ/2}, with ⋂_{λ>0} S_λ = ℓ. |
| neutral | ½. It is the image of the additive neutral 0 and of the multiplicative neutral 1 under these conjugacies: x = σ(u) = 1/(1+e^{−u}) = y/(1+y), and w = 2x−1 = tanh(u/2) = (y−1)/(y+1). Under them ρ ↔ u↦−u ↔ y↦1/y ↔ w↦−w. A ↔ u = −∞ ↔ y = 0 ↔ w = −1, and B ↔ +∞ ↔ ∞ ↔ +1. (This matches S32's diagram, where 0 and ∞ are "tensão" polarities around 1.) |
| compression / tension | Scaling about the neutral. In u-coordinates u ↦ λu; in [0,1], T_λ(x) = σ(λ·logit x); in ℂ, D_λ(s) = ½ + λ(s−½). λ<1 is compression toward N; λ>1 is tension toward the ends. Properties: T_λ∘T_μ = T_{λμ}, T_λ fixes 0, ½ and 1, and T_λ commutes with ρ. For x ∈ (0,1), T_λ(x) → ½ as λ → 0⁺, while the closed ends stay fixed. D_λ maps ∂S̄ to ∂S_λ, which tends to ℓ. |
| torsion / twist | Rotation about the neutral: R_θ(s) = ½ + e^{iθ}(s−½). R_π = ρ is the corpus's "180° dual inversion" x ↦ −x + 2c with c = ½ (S6). The 45°/90°/180° "filters" (S1, S2, S6) are R_{π/4}, R_{π/2}, R_π, which generate C₈. D_λ (λ ∈ ℝ) preserves ℓ, but R_θ preserves ℓ only when θ ∈ πℤ. |
| "neutral tensioned, compressed, twisted" | N is the common fixed point of the spiral-similarity group {½ + a(z−½) : a ∈ ℂˣ} ≅ ℂˣ, with a = λe^{iθ} (λ = stretch, θ = twist). A holomorphic germ f with f(½) = ½ acts locally through the multiplier f′(½) = λe^{iθ}. **Rigidity of the neutral:** any map f with f∘ρ = ρ∘f must have f(½) = ½ (and f(½+z) − ½ is odd in z). An affine map z ↦ az+b commutes with ρ iff b = (1−a)/2, i.e. iff it is centred at ½. |
| ζ realisation | ξ(½+z) is even, and real on ℝ and on iℝ. Hence u_t(σ) = log\|ξ(σ+it)\| is even about ½. The transverse "force" F(½,t) = ∂_σ u_t(½) vanishes: "forces from both sides cancel" (S26, S27). The ζ-zero set in the strip is G-invariant, so off-line zeros come in quartets. Whether the force points outward everywhere, i.e. Re ξ′/ξ > 0 on Re s > ½, is **equivalent to RH** (Lagarias 1999; equivalently, Sondow–Dumitrescu 2010: \|ξ(σ+it)\| is strictly increasing for σ > ½). |

### 1.2 How the corpus states the picture (all conjugate to M)

- **V1 Hourglass** (S1, S2, S3, S5). There are two cones: the "Fibonacci head" (expansion) and the "infinite tail" (contraction, 0/0). The waist "X" is placed at 0.5 and identified with Re s = ½. The real Fibonacci waist is 1/φ: the ratios R(n) = F(n)/F(n+1) form nested closed intervals [R(2k), R(2k−1)] that shrink to 1/φ ≈ 0.618, not to ½ (G19).
- **V2 Torque gauge** (S4). 𝕋(x) = \|x−½\|/\|x+½\|. Both ends are at maximal torque (𝕋(0) = 1, 𝕋(∞) = 1) and the middle is balanced (𝕋(½) = 0). Exactly, 𝕋(x) = \|tanh(½ log 2x)\| = \|w\| for y = 2x. Hidden symmetry: x ↦ 1/(4x) swaps the ends and fixes ½. This is the Cayley picture: Re z > 0 maps onto the disc, ½ ↦ 0, 0 ↦ −1, ∞ ↦ +1.
- **V3 Logic** (S23, S24).
  - Kleene's K3 {F, N, T} embeds as {0, ½, 1} with ¬ = ρ.
  - "Hodge tension closure" has endpoints closedFalse0 and closedTrue0 with an open50 middle; it labels workflow states only.
- **V4 I-phase** (S7, S13, S16). I ∈ [0,1): I = 0 is "coherent" (closed start), 0 < I < 1 is "anomalous", and I = 1 ("collapse") is excluded by the axiom I ≠ 1. The carrier is half-open. The gauge I = t/(t+ε) maps [0,∞] onto [0,1] and never reaches 1 for finite t.
- **V5 Fibre model** (S22). On Bool×ℝ, traction, retraction and twist are all the same fibre involution, and each preserves the real projection. Tension, release and twist are therefore not distinguished.
- **V6 Harappan zero operator** (S18). Halving "bars" 2^{−n} → 0 compress toward the zero. This is the contraction h(x) = x/2 with fixed point 0, i.e. the dyadic version of the middle.
- **V7 Structural operators** (S21). Convergence (meet), elevation, divergence and channeling act around "Core = 0/0 = identity".
- **V8 Critical-line prose** (S25, S26, S20, S29). Examples: "0.5 ties both ends (1 and −2n)"; "the Z-axis is a stretched string (tracionado)"; the "valley" of log\|ξ\|; the canonical projection Π_{1/2}; a half-open partition of [0.1, 0.9] whose middle cell is I₃ = [0.42, 0.58).

---

## 2. Deduplicated laws and hypotheses (G1–G52)

Kind: AX axiom · DEF definition · PRV proved (Lean/Coq, as written) · SRY sorry/admit · PRO prose "theorem" · NUM numerics · CODE.
Assessment: TRUE (model; *std* = standard fact, *triv* = trivial) · EQ-RH (equivalent to or assumes RH) · FALSE (counterexample) · VAGUE.

### A. Critical line as the middle; reflection and symmetry

| # | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| G1 | The FE ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s) makes the nontrivial zeros symmetric about Re s = ½. | PRO | S25, S18, S28 | TRUE std (Mathlib `riemannZeta_one_sub`, `completedRiemannZeta_one_sub`). |
| G2 | Zeros come in quartets {s, s̄, 1−s, 1−s̄}. An off-line zero has 4 distinct members. | AX (FE, conj) + SRY (case s ∈ ℝ) | S12; also millennium-riemann-i docs/zeros-structure.md 60b6faa5, universal 13-03 4c243e49 | TRUE. The sorry is dischargeable because ζ(σ) < 0 on (0,1) (no real zeros in the strip). |
| G3 | Re s = ½ ⇒ s = 1 − s̄ ("self-conjugate"). | PRV (⇒ only) | S28 | TRUE triv. The converse also holds: Fix μ = ℓ. |
| G4 | xi(s) = xi(1−s); reflection_symmetry about ½. | SRY (xi defined with `sorry` for ζ) | S28 | TRUE std for Mathlib Λ = `completedRiemannZeta`. |
| G5 | Φ_RH(I,s) = \|ζ_I(s)\|² + α\|ζ_I(1−s̄)\|² + βR "enforces FE symmetry". | DEF | S7, S33 | For ζ itself, TRUE that in the strip ζ(s)=0 ⇔ ζ(1−s̄)=0. For the regularised ζ_I (no FE) the symmetry is lost. As a proof device: VAGUE. |
| G6 | F(σ,t) = ∂_σ log\|ξ(σ+it)\| satisfies F(½,t) = 0 for all t ("forces from both sides cancel"; tangentSlope_zero_at_half). | PRO; SRY in S27 | S26, S27, S20 | TRUE wherever ξ(½+it) ≠ 0, since \|ξ(σ+it)\| = \|ξ(1−σ+it)\|. |
| G7 | ξ(½+it) ∈ ℝ ("phase locked"). | SRY | S27 | TRUE std (FE + Schwarz reflection). |
| G8 | Rigidity C_R(t) = ∂²_σ log\|ξ\| at σ = ½ is ≥ 0 for all t, giving "no bifurcation/escape"; numerically R ≥ 0.106 on t ∈ [10, 80]. | PRO / hypothesis (HT) + NUM | S26 | RH ⇒ C_R(t) = Σ_ρ 1/(t−γ)² > 0: TRUE (Hadamard product). "C_R ≥ 0 ⇒ RH" is not a known theorem: OPEN. The docs honestly flag it as a postulate. |
| G9 | "RH ⇔ uniqueness of the transverse equilibrium"; a canonical projection Π_{1/2}(ω) = ½ exists for all ω. | PRO | S20 | Π_{1/2} is the constant map: TRUE but vacuous. The equivalence as stated is VAGUE. The precise forms (Lagarias Re ξ′/ξ > 0 on σ > ½; Sondow–Dumitrescu monotonicity) are EQ-RH. |
| G10 | Z = log\|ξ\| is a "valley" with minimum at σ = ½. Escape energy E(ε) → ∞ as ε → 0, yet E(ε) ~ ε² log\|t\|/2. "Corollary: ½ is the unique locus." | PRO | S26 (6f7f6ffa) | Self-contradictory, since the stated asymptotics give E(ε) → 0. log\|ξ\| is harmonic off zeros, so it has no 2-D minima. As a proof: FALSE. The uniqueness claim is EQ-RH. |
| G11 | E(σ) = ∫w(t)\|ξ(σ+it)\|²dt. Conjectures G1: E″(½) > 0 and G2: unique minimum at ½, described as "RH-type". | DEF + PRO | S29 | E(σ) = E(1−σ) holds pointwise. For w ≡ 1, E″ = C₁+C₂ with C₂ = C₁, so E″ = 4∫\|ξ′\|² > 0. Plancherel with Pólya's even kernel Φ > 0 gives E(½+a) = 2π∫Φ(u)² cosh(2au) du. So G1 and G2 are TRUE unconditionally (also for positive-definite even w) and do **not** imply RH. The "RH-strength" remark is FALSE. |
| G12 | Half-open partition I₁ = [0.1, 0.26), …, I₃ = [0.42, 0.58) (central), …, I₅ = [0.74, 0.9]. | DEF | S29 | TRUE (it is a partition). Note: ρ maps it onto the right-closed partition, and I₃ ↦ (0.42, 0.58]. A ρ-invariant middle cell must be closed or open: the "half-closed middle" is exactly where mirror symmetry fails. |
| G13 | \|e^{Bs}\| = e^{B/2} on the critical line ("Euler hypotenuse"). | PRV | S27 | TRUE triv. |
| G14 | rigidityMeasure e^{−10\|σ−½\|} equals 1 on the line and is < 1 off it. | PRV | S27 | TRUE triv (definitional). |
| G15 | "Force cancellation + E″(½) < 0 ⇒ no off-line zeros"; critical_line_has_wall; axiom absoluteRigidityIdentity. | SRY + AX | S27 | Non-sequitur. The `BalanceFunctional` module is not in the corpus. The sign E″ < 0 (a maximum) contradicts S29 (E″ > 0). VAGUE / EQ-RH. |
| G16 | Δ-collapse: an off-line zero forces I = 1, and the axiom I ≠ 1 then gives RH. | AX `collapse_axiom` (S12); `admit` (S30); "PROVEN" (S13) | S12, S30, S13 | Circular: collapse_axiom ∧ I ≠ 1 ⇔ RH (EQ-RH, assumed). In S30, ζ_I(s) = Σn^{−s}e^{−I(log n)²} has no functional equation. For I = 0 the series is not summable in the strip, so Lean's `tsum` gives 0 there; every strip point is then a "zero" and the theorem is FALSE in that model. |
| G17 | "Phase residue minimised at σ = 0.497980, so RH proven." | NUM | S13 | FALSE as a proof (numerics only). |
| G18 | Parametrised RH: the "torção ω(t) prevents off-line singularities"; α = ½ − σ. | PRO | S19 | VAGUE. |
| G19 | τ_RH(s) = Im(ζ′/ζ(s))·\|s − (½+it)\| = Im(ζ′/ζ)·\|σ−½\| vanishes on ℓ. "Every Millennium problem is solvable via torque." | DEF/PRO | S17 | First claim TRUE triv (undefined at zeros). Second claim VAGUE. |

### B. Hourglass, torque gauges and the 0.5 "lock"

| # | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| G20 | T_neon(s,φ) = I e^{iφ}\|s−½\|^{−1}Δ(s). NT-1: minimal energy on Re s = ½. NT-2: T(s, 90°) = T(1−s, 90°). | DEF/AX | S2 | \|s−½\| is G-invariant: TRUE. NT-1 FALSE: on the line the factor is 1/\|t\|, singular at ½; the code uses \|Re s−½\|^{−1} = ∞ on ℓ and patches it to I. NT-2 is FALSE with S7's Δ (Δ(z) = z gives s ≠ 1−s). |
| G21 | Hourglass: Fibonacci head and infinite tail meet at the 0.5 waist (the critical line). | PRO | S1, S2, S3, S5 | VAGUE. The true Fibonacci waist is 1/φ (G22). |
| G22 | FH Property 2: ∀ε ∃n \|F(n)/F(n+1) − ½\| < ε, and the ratios "oscillate around and cross 0.5". | PRO | S3 | Existence TRUE triv (n = 2 gives exactly ½). Oscillation FALSE: R(n) ≥ ½ for n ≥ 1 with equality only at n = 2; R(n) ∈ [3/5, 2/3] for n ≥ 3; R(n) alternates around 1/φ. |
| G23 | F(3) = 2, F(2)/F(3) = ½, F(3)/F(4) = 2/3; φ² = φ+1; 1/φ = φ−1; F(n+1)/F(n) → φ; Binet formula with ψ = (−φ)^{−1}. | PRO | S1, S3, S5 | TRUE std (Mathlib: `gold_sq`, `inv_gold`, `Real.coe_fib_eq`). |
| G24 | FH-3: the "normalised coordinate" equals 0.5 at θ ∈ {π/4, π/2, π, …}. FH-1: F(I) = I. | AX | S3 | VAGUE (undefined). Under the natural reading sin²θ = ½, it fails at π/2 and π. |
| G25 | PPH-3: 𝕋(x) = \|x−0.5\|/\|x+0.5\| : ℝ → [0,1], with 𝕋(½) = 0, 𝕋(0) = 1, 𝕋(∞) → 1. | DEF | S4 | TRUE on [0,∞): range [0,1), monotone on each side of ½, 𝕋(1/(4x)) = 𝕋(x); Cayley: \|z−½\| < \|z+½\| ⇔ Re z > 0. Codomain claim FALSE on ℝ: 𝕋(−1) = 3, and 𝕋 is undefined at −½. |
| G26 | PPH theorem: x·pair = √pair ⇒ x = 1/√pair; pair = 4 gives x = ½ "anchor". | PRO | S4 | TRUE triv. |
| G27 | 180° "dual inversion" x ↦ −x + 2c; rotations by 45°, 90°, 180°. | CODE/DEF | S6, S1 | TRUE: point reflection about c, which is ρ for c = ½. The rotations generate C₈. |
| G28 | Neon security lock: "prime" iff \|x−0.5\| < 0.1 and the even-root filter ∃i: F(i)F(i+1) is even and √ is an even integer (Thm NT-1). | DEF/PRO | S1 | Vacuous. i = 0 always passes (F₀F₁ = 0, as the code starts from [0,1]). For i ≥ 1 it never passes: F₁F₂ = 1 has an odd root, and for i ≥ 2 F_iF_{i+1} is not a square (coprime factors + Cohn: Fibonacci squares are 0, 1, 144). "Prime" is undefined. FALSE as a theorem. |
| G29 | Phantom compression of solar-system data into 1 bit; COMPRESSION_RATIO = ∞ (NT-4). | AX/CODE | S1 | FALSE (pigeonhole: 1 bit holds at most 2 states). |
| G30 | P_Neon = lim_{n→∞} F(n) ⋆ ∮_{0/0}^{0.5} ℙ_even(θ)dθ, with ℙ_even(θ) = 2+θ; root test √(2·P_Neon) ∈ ℤ. | DEF/CODE | S5 | The integral is 9/8, so P_Neon = lim (9/8)F(n) = ∞: FALSE as a constant. With finite n, (3/2)√F_n ∈ ℤ only for n ∈ {0, 12} (Cohn). |
| G31 | Torque security score \|sin θ\| is maximal at π/2. NT-3: "behaviour differs for θ ≠ θ′". | CODE/AX | S1 | TRUE triv / vacuous. |
| G32 | Q_lock = ½(φ−1) ≈ 0.309, versus "0.5 = midpoint between chaos 0 and order 1". | DEF | S6 | Arithmetic TRUE ((√5−1)/4 = cos 72°). The two "locks" are inconsistent with each other. |
| G33 | Twin-prime torque f = lim_{t→∞}(P₁/P₂)^t·Neon(λ) is "infinite rotation"; Ψ = √(P₁P₂) "deletes perfect squares". | DEF | S11 | The limit is 0 (TRUE; "infinite rotation" FALSE). p(p+2) = (p+1)²−1 is never a square, so nothing is deleted. 22/26 = 0.8461538… TRUE. |
| G34 | 0.5 "ties both ends" (1 and −2n) into a "closed circle"; arctan(½) ≈ 26.565°. | PRO | S25 (2966f10e) | Kernel TRUE: ℓ ∪ {∞} is a circle on Ĉ invariant under G, and ρ maps the pole 1 to 0. ρ does not pair 1 with −2n (−2n ↦ 2n+1). Otherwise VAGUE. |
| G35 | Teorema 1: lim_{x→0} √(x²+0.25)/x = 1 ("hypotenuse collapses to base"). | PRO | S25 (812c12c3) | FALSE: ±∞ (the document itself concedes this). TRUE replacement: the limit as x → ∞ is 1, and \|½+it\|/\|t\| → 1. |
| G36 | Teorema 4: trivial zeros are "necessary and sufficient" for the symmetry. Teorema 3: \|ζ(s_n)\|/\|ζ(s_{n−1})\| converges by "triangle geometry". | PRO | S25 | VAGUE. At zeros the ratio is literally 0/0. |
| G37 | Ψ_d = d/(d+1) = ∫₀¹ x^d dx, with "Ψ₁ = ½ structural". | DEF | S15 | FALSE for d ≠ 1 (the integral is 1/(d+1)). The two agree only at d = 1. |

### C. Neutral, zero operator, I-phase, states

| # | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| G38 | Kleene 3-state logic: ¬N = N, ¬¬s = s, de Morgan; "0/0 = 3" names N. | PRV | S23 | TRUE: K3 with ∧ = min, ∨ = max, → = max(1−a, b), ¬ = 1−x on {0, ½, 1}. N is the unique fixed point of ¬. |
| G39 | FundamentalIModel: traction∘retraction = id; traction and twist preserve the projection; stabilize is idempotent; non-collapse (∃x≠y, π x = π y); embedReal injective. | PRV | S22 | TRUE. Degenerate: twist = traction = retraction (one involution). |
| G40 | Hodge tension closure: open50 / closedTrue0 / closedFalse0; positive and negative certificates are incompatible; twist is involutive. | PRV | S24 | TRUE. These are labels, not mathematical content. |
| G41 | I-phase I(x) = ‖R‖/(‖R‖+ε) ∈ [0,1): 0 = coherent, (0,1) = anomalous, → 1 = collapsed. Axiom I ≠ 1. | DEF/AX | S16, S7, S13 | TRUE: t ↦ t/(t+ε) maps [0,∞) onto [0,1) strictly monotonically, so I ≠ 1 is automatic. |
| G42 | EPP-T2: for I ∈ [0,1) and any continuous f, I·f(p₁,p₂) ≠ 1. | PRO | S16 | FALSE (I = ½, f ≡ 2). |
| G43 | Collapse Δ: Δ∘Δ = Δ, Δ(I) = I, Δ(z) = z for regular z. Elsewhere "Δ(F(n)) → 0.5 at equilibrium". | AX | S7, S3 | The first set forces Δ = id. Jointly with "Δ(F(n)) → 0.5": FALSE (inconsistent specifications). |
| G44 | Closure 𝒞 = ι∘π with π∘ι = id ⇒ 𝒞² = 𝒞, Fix 𝒞 = im ι, R = x − 𝒞x ∈ ker π, R(𝒞x) = 0. | AX/PRO | S7 | TRUE std (section/retraction; additivity needed for R ∈ ker π). |
| G45 | Log primo par: L_I = log₂ I is idempotent; "2L = L ⇒ L = 0 or L idempotent", L_I ∉ ℂ. Neon scale: signature(log₂ λx) = signature(log₂ x). | AX | S7 | FALSE: in an additive group 2L = L ⇒ L = 0, so L_I = 0 (the additive neutral), contradicting L_I ∉ ℂ. Scale invariance: VAGUE, and FALSE if "signature" means fractional part (λ = √2). |
| G46 | nexus_core "I is the neutral element of indetermination": I + x = I·x = I/x = x/I = I. | PRV | S31 | TRUE in that model, but I is **absorbing** (a nullity), not neutral: a misnomer. |
| G47 | Wheel: x ⊗ I = I for all x (sorry), together with axiom zero ⊗ I = zero. | SRY + AX | S31 | Inconsistent: I = zero contradicts distinct constructors. FALSE. |
| G48 | Harappan Zero Law. z is a zero operator iff (i) adding z adds no information, (ii) nothing follows z, (iii) z has some of C1–C5 (code: C1 or C5). strength(z) = Σw_c with w = (.25, .15, .20, .15, .25). | DEF | S18 | Definitions are consistent in code and tests (DOT 0.55, bars M-342..345 0.55, FISH 0.45, CROSS 0.60). The md table lists DOT/bars 0.65, FISH 0.60, CROSS 0.85; the tex ranges are operational ∈ [0.60, 0.65] and non-trivial ∈ [0.60, 0.85]. Both are FALSE against the formula. The doc calls trivial zeros "direct poles": FALSE (ζ's only pole is s = 1). |
| G49 | HZL Thm 1: every inscription ends with a zero operator. Thm 2: hierarchy T < O < N. Thm 3: bars 2^{−n} → 0 ("compression"). | PRO | S18 | Thm 1 VAGUE (empirical). Thm 2 TRUE by definition. Thm 3 TRUE std (contraction x ↦ x/2, fixed point 0). |
| G50 | Structural operators (tex): Core = 0/0 is a two-sided identity for ∘; M165∘M359 = id and M359∘M165 = id_{Σ²}; M165∘M165 = M165; every operator fixes Core; M166(σ) ≻ σ; E∞ = Core; "consistency verified in Lean/Coq/Isabelle". | AX/PRO | S21 tex | FALSE. A two-sided inverse with symmetric meet forces \|Σ\| ≤ 1 ((a,b) and (b,a) have the same meet). "Fixes Core" contradicts M166(Core) ≻ Core. M165∘M165 is ill-typed. The Lean "consistency" theorem is `True`. |
| G51 | StructuralOperators.lean: M165_after_M359 (M165(M359 s) = s) and emergence_step_fixes_core. | PRV (claimed) | S21 lean | FALSE as stated: labels change. Counterexample s = Core: the result has label "0/0ₗ", resp. "∇(0/0⁺ₗ,0/0⁺ᵣ,0/0)". Only the `.stratum` versions hold. The file uses `push_neg` without importing Mathlib, so the "verified" claim is unsupported. The other laws (equal-pair idempotence, strict elevation, core absorption under hypothesis) are TRUE triv. |
| G52 | Torque-tail and related constructs. | DEF/AX/PRO | S8, S9, S10, S14 | See breakdown below. |

**G52 breakdown (S8, S9, S10, S14):**
- **P_even (S8).** P_even = {(p,q) : q = p·k prime, 2 ≤ k ≤ ⌊√p⌋}. FALSE/vacuous: p·k is composite, so P_even = ∅ and "stable prime" never holds. TT-A3: P(z) = c·z with \|c\| = e^{−I\|ζ\|²} < 1 cannot satisfy P² = P (that needs c ∈ {0,1}).
- **TT-T1 (S8).** "Critical line = tail manifold": EQ-RH / VAGUE.
- **T_u (S9).** T_u = P_e√P_p/(0/0): VAGUE.
- **Infinite tail prime (S10).** P_∞ = lim p_n e^{−In} is 0 for I > 0. "√P_∞ = P_∞" forces P_∞ ∈ {0,1}. There is no largest prime. All FALSE. ITP-RH: EQ-RH.
- **HarappanGeometry (S14).** Axiom `discrete_geometric_correction` is INCONSISTENT: n = 0, y = 1 gives ∀t, t = 0. `harappan_structure_uniqueness` (∃! Type) is FALSE: Empty and PUnit both qualify.

---

## 3. Statements that are TRUE, non-trivial enough and worth proving in Lean

The best model for each is given with its rough cost.

1. **Mirror geometry of the strip.** ρ s = 1−s, κ = `starRingEnd ℂ`, μ = ρ∘κ. Each is an involution, they commute, and ρ∘κ = μ (Klein four-group). Fix ρ = {½}, Fix μ = {s \| s.re = ½}, Fix κ = ℝ. ρ preserves `{s | 0 ≤ s.re ∧ s.re ≤ 1}` and swaps the lines re = 0 and re = 1. *(easy)*
2. **Rigidity of the neutral.** Any f with f∘ρ = ρ∘f has f(½) = ½. An affine z ↦ az+b commutes with ρ ⇔ b = (1−a)/2 (centre ½); also commuting with κ ⇔ a ∈ ℝ. The spiral similarities D_a = ½ + a(·−½) form a group ≅ ℂˣ. D_a preserves ℓ ⇔ a ∈ ℝˣ; the twist R_θ preserves ℓ ⇔ θ ∈ πℤ. *(easy)*
3. **Compression to the middle.** For \|λ\| < 1, D_λ^[n] s → ½. Nested ρ-invariant `Set.Icc (a n) (1 - a n)` with a_n ↑ ½ intersect to {½}. ⋂ `Set.Ico (a n) (1/2)` = ∅ (the half-open middle vanishes; the closed middle survives). ⋂_{λ>0} S_λ = ℓ. *(easy–medium)*
4. **Logistic conjugacy and the tension/compression group** on [0,1]. σ u = 1/(1+e^{−u}): σ(−u) = 1−σ u, σ 0 = ½, σ is an order isomorphism ℝ ≃ (0,1). T_λ = σ∘(λ·)∘logit fixes ½, commutes with ρ, and T_λ∘T_μ = T_{λμ}. T_λ x → ½ as λ → 0⁺ for x ∈ (0,1), and T_λ extends continuously fixing 0 and 1. This is the cleanest "closed ends fixed, interior tends to the neutral" model. *(medium)*
5. **Torque gauge** 𝕋 x = \|x−½\|/\|x+½\|. On [0,∞): 𝕋 ∈ [0,1), 𝕋 x = 0 ⇔ x = ½, 𝕋 0 = 1, 𝕋 → 1 at ∞, antitone on [0,½] and monotone on [½,∞), 𝕋(1/(4x)) = 𝕋 x. Complex: \|z−½\| < \|z+½\| ⇔ 0 < z.re. Counterexample 𝕋(−1) = 3. *(easy)*
6. **K3 = ({0,½,1}, min, max, 1−x).** The `ThreeState` map is a homomorphism for ¬, ∧, ∨, →; N is the unique fixed point of ¬; {N} is closed under all connectives, so K3 has no tautologies. *(easy; extends S23)*
7. **Fibonacci hourglass, corrected.** For R n = fib n / fib (n+1):
   - ½ ≤ R n for n ≥ 1, with equality ⇔ n = 2.
   - 3/5 ≤ R n ≤ 2/3 for n ≥ 3.
   - Even-index terms increase and odd-index terms decrease (Cassini), giving nested intervals with limit φ⁻¹ = φ−1.
   This refutes G22's "oscillates around 0.5". *(medium)*
8. **G-invariance of the ζ zero set in the strip.** For 0 < re s < 1: ζ s = 0 → ζ(1−s) = 0 via `riemannZeta_one_sub` (the hypotheses hold in the strip). Also ζ(conj s) = conj(ζ s), by the identity theorem from `zeta_eq_tsum_one_div_nat_cpow` on re > 1 plus analyticity on ℂ∖{1}; I did not check whether Mathlib already has this lemma. Hence ζ(1 − conj s) = 0. *(medium)*
9. **No real zeros in (0,1)**: ζ σ < 0 for σ ∈ (0,1). Cheapest route: the formalizer's own `ATK/ZetaStrip.lean` (m-core `conditional:atk-kernel/ATK/ZetaStrip.lean`, f35c76c8) has `H_eq_zeta`: H s = 1/(s−1) − ζ s/s with H(σ) = ∫₁^∞{t}t^{−σ−1} ≥ 0. This discharges the `sorry` in S12 `quartet_structure`: an off-line zero's G-orbit has exactly 4 elements. *(medium)*
10. **ξ / Λ symmetry consequences.** `completedRiemannZeta_one_sub` + conj symmetry give \|Λ(σ+it)\| = \|Λ(1−σ+it)\| and Λ(½+it) ∈ ℝ. The factor s(s−1) is ρ-invariant, so the same holds for ξ. With the generic lemma "g(½+x) = g(½−x) and g differentiable at ½ ⇒ g′(½) = 0" this gives F(½,t) = 0 where Λ(½+it) ≠ 0. *(medium)*
11. **Energy convexity, unconditional and not RH.** Abstract lemma: Φ ≥ 0, even, not a.e. 0, with Φ²e^{c\|u\|} integrable ⇒ a ↦ ∫Φ(u)² cosh(au) du is even, strictly convex on (−c,c), with unique minimum at 0. *(medium)* The full link E(σ) = ∫\|ξ(σ+it)\|²dt = 2π∫Φ²cosh(2(σ−½)u) needs Plancherel and Pólya's kernel *(hard, stretch)*. It shows S29's G1/G2 are true and not RH-strength.
12. **Torque-tail refutation.** `Nat.Prime p → 2 ≤ k → ¬ Nat.Prime (p*k)`, so P_even = ∅. Also (z ↦ c·z) idempotent ⇔ c = 0 ∨ c = 1. *(easy)*
13. **Structural-operator refutations.** If conv : Σ×Σ → Σ is symmetric, div : Σ → Σ×Σ, and div∘conv = id, then `Subsingleton Σ`. Concrete counterexample `M165_convergence (M359_divergence Core) ≠ Core` (by `decide`/`simp` on labels). The corrected `.stratum` versions hold. *(easy)*
14. **HarappanGeometry hazard.** `discrete_geometric_correction 0 1 (by decide)` ⊢ False, and ¬(∃! T : Type, …) via Empty ≠ PUnit. Flag before any build imports `Universe00.HarappanGeometry.Core`. *(easy)*
15. **Hypotenuse limits.** `Tendsto (fun x => √(x^2+1/4)/x) (𝓝[>] 0) atTop`; the same expression tends to 1 at `atTop`; \|½+it\|/\|t\| → 1. Refutes G35 and supplies the correct statement. *(easy)*
16. **Neon root filter is vacuous.** For i ≥ 1, IsSquare(fib i · fib (i+1)) ⇒ both factors are squares (`Nat.fib_coprime_fib_succ` + coprime-square lemma), and i = 0 is a trivial witness. The full "only i ≤ 1" result needs Cohn's theorem (not in Mathlib; optional). *(easy–medium)*
17. **Twin-prime torque.** ∀p ≥ 1, ¬IsSquare(p(p+2)) because p² < p(p+2) < (p+1)². Also (p/(p+2))^t → 0. *(easy)*
18. **I-phase gauge.** t ↦ t/(t+ε) is a strict order embedding [0,∞) → [0,1) with range [0,1), so "I ≠ 1" holds automatically. EPP-T2 counterexample: I = ½, f ≡ 2. *(easy)*

**Open, not to attempt (EQ-RH):**
- G9 in precise form: Lagarias, Re ξ′/ξ > 0 on σ > ½ ⇔ RH; Sondow–Dumitrescu monotonicity.
- G10 and G15 (uniqueness of the valley / wall).
- G16 (Δ-collapse).
- The S8 and S10 RH corollaries.
- G8's converse (C_R ≥ 0 ⇒ RH): open, and not even a known equivalence.
