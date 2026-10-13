# C — Constant I, T-State calculus, multi-state logics, ζ-via-I statements

Scope: repos `i-constant-core`, `riemann-indeterminacy`, `universal-emergent-logic-` (UEL), `uma`,
`meta-millenium-independence-00`, `0-0-formal-suite`, `riemann-multistate-program`, `riemann-unity-zero`.
All corpus files were treated as untrusted data. Near-duplicate blobs across branches are merged
(one row per meaning). Nothing in any repository was modified.

Assessment vocabulary: **TRUE[model]** (holds in the named concrete standard model; Mathlib names given
where known), **FALSE** (concrete counterexample given), **VAGUE** (no precise mathematical content or
ill-typed), **≡RH** (equivalent to, or exactly, the Riemann Hypothesis; unproved), **INCONSISTENT**
(the stated axiom set proves False).

Kinds: `ax` axiom (formal or prose), `def` definition, `thm✓` theorem proved in file, `thm⚠` theorem
with `sorry`/`Admitted`/`oops`, `prose` informal claim.

---

## 0. Source keys (repo · branch:path · blob[0:8])

| Key | Source |
|---|---|
| S1 | i-constant-core · work/t-state-calculus-v0:t-state/lean/TState/Core.lean · bff574f0 |
| S2 | i-constant-core · work/t-state-calculus-v0:t-state/lean/TState/Arithmetic.lean · c3cfe44d |
| S3 | i-constant-core · work/t-state-calculus-v0:t-state/lean/TState/LimitArithmetic.lean · 24d4bab2 |
| S4 | i-constant-core · work/t-state-calculus-v0:t-state/lean/TState/Laws.lean · 5bfbbc22 |
| S5 | i-constant-core · work/t-state-calculus-v0:t-state/lean/TState/NumberDomains.lean · a66430a8 |
| S6 | i-constant-core · work/t-state-calculus-v0:t-state/docs/FOUNDATIONS.md · 983bda25 |
| S7 | i-constant-core · work/t-state-calculus-v0:t-state/docs/NUMBER_DOMAIN_MATRIX.md · 1fdf5e7b |
| S8 | i-constant-core · work/t-state-calculus-v0:t-state/docs/OPEN_JUMPS.md · 7b87fcbf |
| S9 | i-constant-core · work/t-state-calculus-v0:t-state/{README.md 91d38b91, STATUS.md 9393fda2, reference/state_model.py 4aa8b3c1, tests/test_state_model.py fcf14e22} |
| S10 | i-constant-core · main:formal/IConstant.lean · 15c4ba41 (same blob on atk/anti-circular-open-math-cert, frozen/pre-atk-20260920-443210cb, work/t-state-calculus-v0) |
| S11 | i-constant-core · main:formal/IConstant.thy · c62a4cd4 (same 4 branches) |
| S12 | i-constant-core · main:formal/IConstant.v · d0441700 (same 4 branches) |
| S13 | i-constant-core · main:axioms/ZFC_extensions.md · 9c4c075f (4 br) |
| S14 | i-constant-core · main:operators/decomposition.md · cb4f1c7f (4 br) |
| S15 | i-constant-core · main:theory/delta_derivation.md · e7ac8ea2 (4 br) |
| S16 | i-constant-core · main:theory/limits_and_series.md · c32f7cb0 (4 br) |
| S17 | i-constant-core · main:proofs/formal_proofs.md · d71f0b5c (4 br) |
| S18 | i-constant-core · main:{theory/symbolic_collapse.md f484f27f, theory/ontology.md 358cff89, applications/physics.md 6f80204b, applications/consciousness_information.md 67546d14, diagrams/visual_representations.md e45efbb8, docs/examples_tutorials.md 6324c6b6, README.md d7844565} |
| R1 | riemann-indeterminacy · copilot/debate-tecnico-analise-critica:PHASE_STABILITY_THEOREM.md · 79d65208 (same text: TECHNICAL_ANALYSIS.md 4a78a475, riemann_singularity_phase_geometry.tex f70a821f) |
| R2 | riemann-indeterminacy · copilot/debate-tecnico-analise-critica:NOTATION_REFERENCE.md · 242f0c2d |
| R3 | riemann-indeterminacy · copilot/add-article-structure:docs/THEORY.md · a0c49e2d |
| R4 | riemann-indeterminacy · copilot/add-article-structure:formal/lean4/RiemannIndeterminacy.lean · 4a49f1f7 |
| R5 | riemann-indeterminacy · copilot/add-article-structure:formal/coq/RiemannZeta.v · 253009e9 ; formal/isabelle/RiemannZeta.thy · c22c07b1 |
| R7 | riemann-indeterminacy · copilot/add-article-structure:latex/sections/10-main-theorem.tex · a3b5e668 |
| R8 | riemann-indeterminacy · copilot/add-article-structure:latex/sections/04-singularities.tex · b9f1d341 |
| R9 | riemann-indeterminacy · copilot/add-article-structure:latex/sections/08-geometric-interpretation.tex · 0ec5d5c8 |
| R10 | riemann-indeterminacy · copilot/add-figures-and-improvements:riemann-indeterminacy_figures_deep.tex · 3d9e1ced |
| M1 | meta-millenium-independence-00 · main:src/lean/MetaMillennium/Core/ThreeStateLogic.lean · 94a61a1c (+copilot/consolidate-repository-structure) |
| M2 | meta-millenium-independence-00 · main:src/latex/chapters/ch10-three-state-logic.tex · 7d312715 |
| M3 | meta-millenium-independence-00 · copilot/add-transfinite-logical-states:src/LS6/Algebra.lean · ec908fb9 |
| M4 | meta-millenium-independence-00 · copilot/add-transfinite-logical-states:{src/LS6/Transitions.lean 6b41fcdf, src/LS6.lean 90d36b3f, docs/LS6_Formal.tex a0e16859} |
| M5 | meta-millenium-independence-00 · main:{docs/philosophy.md d22b9c28, src/python/models/dual_state_explorer.py 32ca13ff} |
| F1 | 0-0-formal-suite · atk/fundamental-i-model:src/FormalSuite/I/Universal/FundamentalIModel.lean · 31d234f6 |
| F2 | 0-0-formal-suite · atk/fundamental-i-model:src/FormalSuite/I/Foundations.lean · 29b58399 (comment-only variants 4cd5cfca, 2af06b9c; root i-foundations.lean 2de010e5, 6 br) |
| F3 | 0-0-formal-suite · atk/fundamental-i-model:src/FormalSuite/Geometry/Cone00.lean · 53b3d49a |
| F4 | 0-0-formal-suite · atk/fundamental-i-model:audit/I_BACKWARD_DENSE_SEMANTIC_AUDIT_001.md · 1b89e67a ; README.md · 84065601 |
| P1 | riemann-multistate-program · copilot/formalize-riemann-system:notes/01_mapping_0_div_0_and_I_to_Riemann.md · 0e22fe12 ; docs/01_overview_program.md · c9a74b1a |
| P2 | riemann-multistate-program · copilot/formalize-riemann-system:notes/03_symbolic_collapse_and_RH_status.md · 683ee4e8 |
| P3 | riemann-multistate-program · copilot/formalize-proofs-and-gaps:Hypotheses_and_Gaps_for_RH_Energy_Program.tex · 38645ec8 (≈ copilot/formalize-proof-hypotheses:hypotheses_and_gaps.tex ba070aa5) |
| P4 | riemann-multistate-program · copilot/advanced-math-techniques-rh:docs/areas/15-symbolic-translations/README.md · 362e380e |
| U1 | riemann-unity-zero · main:main.tex · d3878a2c (≈ copilot/calculate-high-precision-values:main.tex 5e34afc4) |
| U2 | riemann-unity-zero · main:MATHEMATICAL_STRUCTURE.md · 7b43a795 (+2 br) |
| U3 | riemann-unity-zero · copilot/calculate-rigidity-coefficient-yet-again:docs/rigidity_and_escape_mechanism.md · 415bc6b0 |
| U4 | riemann-unity-zero · copilot/add-rigididade-e-escape-no-eixo-z:ARQUITETURA_TRIDIMENSIONAL_DA_RIGIDEZ.md · 6f7f6ffa |
| U5 | riemann-unity-zero · copilot/detail-file-tree-for-theory:docs/article_pt.md · 812c12c3 ; copilot/document-absolute-unit-discovery:README.md · 281772d8 ; copilot/analyze-limits-with-lhospital:MATHEMATICAL_ANALYSIS.md · ad1e223f |
| U6 | riemann-unity-zero · copilot/anatomy-of-zetas-connection:papers/absolute_mirror_inversion.md · 82311c32 |
| E1 | UEL · copilot/add-lhospital-derivative-integral:WHITE_PAPER_00_REFUTATION_LA_2028.md · 9e574fd2 (+5 br) |
| E2 | UEL · main:laws/lre-limit-formalization.md · 76a68ef6 (+4 br) |
| E3 | UEL · copilot/refute-operator-0-0:formalization/lean/HEAU/OperatorZeroOverZero.lean · d0125b84 (+README.md 163ab205, coq dcf5ee4d, isabelle 57ec3b9e) |
| E4 | UEL · copilot/add-axioms-for-universal-unification:formalization/lean/Axioms/UnificationAxioms.lean · a42a0f4f |
| E5 | UEL · copilot/add-lhospital-derivative-integral:math/matriz_convergencia_universal.tex · 7ef4ce28 (+5 br) |
| E6 | UEL · copilot/add-axioms-for-universal-unification:problems/riemann_hypothesis/d1/{README.md b8438fb1, K_Bounds.md 7c7012af} (+5 br) |
| E7 | UEL · copilot/add-resonance-control-logic:src/critical_redundancy/grounding_logic.py · 116dd32d ; copilot/add-lhospital-derivative-integral:docs/LOGIC_B_DOCUMENTATION.md · 83d9b2e3 |
| E8 | UEL · copilot/add-lhospital-derivative-integral:universe00/README.md · 0f1238e2 (+5 br) |
| A1 | uma · main:formal_verification/lean/UNIVERSE_00_AXIOMS.lean · 191ed435 |
| A2 | uma · main:formal_verification/UMA_Foundation.lean · 25ed280e |
| A3 | uma · main:formal_proofs/lean/IndeterminacaoZeroDivZero.lean · 671c3b13 |
| A4 | uma · main:formal_proofs/lean/universe00_core.lean · 7cdd0d32 |
| A5 | uma · main:docs/AXIOMA_0_EQUATION.md · 4ceb9c2e |
| A6 | uma · main:core/system_logic.py · 951ed0bf ; main:docs/UNIVERSE_00_AXIOMATICS.md · e9ee5b9d |
| A7 | uma · main:{docs/MATHEMATICAL_FOUNDATIONS.md 52da0662, docs/MATH_SINGULARITY_00.md ce926706, core/logic/singularity_00.py a03c5417} |

---

## 1. Carriers, states, operators

**1.1 T-State calculus (S1–S9, branch work/t-state-calculus-v0 only).**
- `Phase = before | at | after`, `flip` swaps before/after. `Horizon = negInfinity | zero | posInfinity`, `neg` swaps ±∞.
- `IndeterminateForm = 0/0 | ∞/∞ | 0·∞ | ∞−∞ | 1^∞ | 0^0 | ∞^0 | custom String` (only tags; no power arithmetic defined).
- `State = finite (x:ℝ) | boundary (h:Horizon) (p:Phase) | indeterminate f`; 9 named boundary states (zeroBefore … negInfinityAfter).
- `Outcome α = exact a | family (S : StateSet α) | undefined` (Outcome.lean not in corpus; usage visible).
- Ops: `State.negate`; `StateArithmetic.{add,mul,div,analyticInv}` (conservative); `LimitArithmetic.{add,mul,div}` (ideal ±∞ "at" states); `poleFamily = {−∞at, +∞at}`.
- `NumericDomain` registry (18 + custom) and `CanonicalEmbedding` (7 injections).
- Referenced but **absent from the corpus**: Outcome, Boundary (`structuralNext/Prev`), Projective (`ProjectiveReal`, reciprocal), Operators (Π, Σ, Δ, Ω, Residual), Dynamics (StateSystem, Reachable, Kernel, FirstHit), Endpoint (Exhaustive/Exclusive/Gap/Overlap witnesses), Bridge (BridgeCertificate), ProblemInterfaces.
- Build hazards: Core.lean imports `Mathlib.Basic.Real.Basic` (non-existent; should be `Mathlib.Data.Real.Basic`); Laws.lean imports the missing modules. Pinned "Lean 4.34.0 / mathlib v4.34.0".
- Python reference model (S9) implements only 4 forms and the triplet/division/inverse rules.
- **Cleanest standard model:** germs = filters on `EReal`: `finite x ↦ 𝓝 x`, `boundary h before/at/after ↦ 𝓝[<] h / 𝓝 h (or pure h) / 𝓝[>] h` (so `posInfinity.after ↦ 𝓝[>] ⊤ = ⊥`, i.e. "beyond ∞" has no semantics, as the files intend); `family S ↦ ⨆ S`; `negate ↦ map Neg.neg`; `analyticInv ↦ map Inv.inv` on ℝ-germs.

**1.2 Number-domain matrix (S5, S7).** ℕ, ℤ, ℚ, algebraic, constructible, computable, ℝ, ℂ, extended reals, ℝP¹, Riemann sphere, p-adics, finite fields, hyperreals, surreals, ordinals, cardinals, "indeterminate states". Rule: a bridge needs map, domain, codomain, preservation, injectivity/surjectivity, boundary behaviour, behaviour of singular forms.

**1.3 IConstant (S10–S12).** Lean: `structure IConstant {value : Type u; is_indeterminate, is_total : value → Prop}`; axioms I_exists, I_duality, I_invariant, Delta_concept : ℝ (but theorems use undefined `Delta`), Delta_* ; ops `Pi` (application), `Sigma` (List fold +), `DeltaOp`, `Omega` (sorry), `I_add/I_mul` (sorry); `OntologicalLevel` (void<unity<duality<synthesis<totality); `Collapse` record with `conserves_info : True`. Isabelle: `typedecl IConstant`, constant I, Delta axioms. Coq: `Parameter I : Type`, `I_constant : I`. Prose constant **Δ = 0.∞19** and operator decomposition **I = Ω∘Δ∘Σ∘Π** (S13–S17).

**1.4 IField and Fundamental-I model (F1–F3).** `class IField α extends Field α` with `I*I = I`, `I ≠ 0` (instances ℝ, ℂ with I=1). `FundamentalIModel`: `IState := Bool × ℝ`, projection `.2`, traction = retraction = twist = Bool flip, stabilize = id, `state00 := (false,0)`. Cone00: `Cone n` (0 ∈ C, closed under λ≥0 scaling).

**1.5 Three-state logic (M1, M2, M5).** `ThreeState = true | false | neutral` ("0/0 = 3"); neg/and/or/implies tables = **strong Kleene K3** (and=min, or=max on F<N<T, a→b = ¬a∨b; verified by exhaustive check). Semantics `evaluate T φ` / `val_T φ ∈ {1,0,3}` by provability; Dual-State `DS(T,φ) = {(M⁺,M⁻) : M⁺⊨T+φ, M⁻⊨T+¬φ}`. (Imports `MetaMillennium.Core.ConsistencyAndIndependence`, not in corpus.)

**1.6 LS6 six-state logic (M3, M4).** States T, F, I (independence), P (prime-tail), Ω (trans-infinite), ∅ (finitist); neg (T↔F, P↔Ω, I,∅ fixed), meet, join, collapse, `Universe = HF | StandardZFC | NonStandard | LargeCardinal`, `transition`, `isStable`, `resolveTension`.
**No 7-state logic exists in these 8 repos**; the nearest are LS6 and the Riemann-system labels E₀…E₈ (P1, P2), which are names for expressions, not truth values.

**1.7 Other carriers.** UEL universe00 3 statuses PROVED/REFUTED/OPEN by error vectors (E8); UEL Θ̂ := "lim ε/ε" := `LinearMap.id` (E3); UEL "0/0 phase lock" = time average (E1); Logic A (threshold grounding) / Logic B (stochastic resonance) (E7). uma: `zeroOverZero : ℝ := 1` (A1), `IndeterminacaoContextual` (A3), `SingularityNumber` (A2), `PurePotential` (value = 1) (A4), singularity operator Ŝ (A6).

**Standard models used below.**
- **EReal/filters**: limits and germs (Mathlib `EReal`, `Filter.Tendsto`, `atTop`, `𝓝[<]`, `𝓝[≠]`).
- **Wheel K⊙** (Carlström, *Wheels – on division by zero*, 2004) for a field K: classes [a:b] of K² under scaling by K^×; [a:b]+[c:d]=[ad+bc:bd], [a:b]·[c:d]=[ac:bd], /[a:b]=[b:a]; 0=[0:1], 1=[1:1], ∞=/0=[1:0], **⊥=0/0=[0:0]**. Not in Mathlib.
- Transreals (Anderson; signed ±∞, nullity Φ) and common meadows (Bergstra–Ponse) only as comparison models.
- **K3** = ({F<N<T}, min, max, ¬).
- **ℝP¹** = `OnePoint ℝ` (or `Projectivization`).
- **Λ/ξ**: Mathlib `completedRiemannZeta`, `completedRiemannZeta₀`; ξ(s) := s(s−1)Λ(s)/2 = s(s−1)Λ₀(s)/2 + 1/2 (entire).

---

## 2. Catalogue of axioms, laws, rules, operators, theorems

### 2A. T-State calculus

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C1 | `Phase.flip (flip p) = p`; `Horizon.neg (neg h) = h` | def+thm✓ | S1 | TRUE (finite cases). The file does not build because of its import path. |
| C2 | `negate`: finite x ↦ −x; boundary h p ↦ boundary (neg h)(flip p); indeterminate fixed; `negate ∘ negate = id` | def+thm✓ | S1 | TRUE. Filter model: map neg 𝓝[<]0 = 𝓝[>]0, map neg (𝓝[<]⊤) = 𝓝[>]⊥, map neg atTop = atBot. |
| C3 | Structural triplet: next(before)=at, next(at)=after, prev(after)=at for every horizon; next(after)=none | thm✓ (Boundary.lean missing) / tests | S4, S9 | TRUE by definition (trivial). |
| C4 | Conservative `add`, `mul`: exact on finite × finite, `undefined` otherwise; `add_finite`, `mul_finite` | def+thm✓ | S2 | TRUE (rfl). |
| C5 | `div (finite 0) (finite 0) = exact (indeterminate 0/0)` | def+thm✓ | S2, S4 | TRUE as a definition. Limit content: with f,g→0 (g≠0) every L∈EReal is a limit of f/g (f=cx, g=x; f=±\|x\|, g=x²) and non-convergence also occurs (f=x·sin(1/x), g=x). |
| C6 | `div (finite x) (finite 0) = family {−∞at, +∞at}` for x≠0; `div x y = x/y` for y≠0 | def+thm✓ | S2, S4 | TRUE read as a cluster set: f→x≠0, g→0, g≠0 ⇒ \|f/g\|→∞ (Mathlib `tendsto_inv₀_nhdsNE_zero` → cobounded; `Real.cocompact_eq`: atBot ⊔ atTop). FALSE read as "f/g tends to one of ±∞": g=(−1)ⁿ/n gives no limit. |
| C7 | 0/0 and 1/0 get different constructors (`zero_over_zero_classification`, `one_over_zero_classification`) | thm✓ | S4 | TRUE (constructors distinct). Also TRUE[K⊙]: 0/0=⊥ ≠ ∞=1/0. |
| C8 | `analyticInv`: 0⁻↦−∞(after), 0⁺↦+∞(before), +∞(before)↦0⁺, −∞(after)↦0⁻, ±∞(at)↦0(at), 0(at)↦family{±∞}, x≠0↦x⁻¹, beyond-∞ states undefined | def+4 thm✓ | S2, S9 | TRUE[filters]: Mathlib `tendsto_inv_zero_atTop`/`tendsto_inv_nhdsGT_zero`, `tendsto_inv_nhdsLT_zero`, `tendsto_inv_atTop_zero'`, `tendsto_inv_atBot_nhdsLT_zero`; map inv 𝓝[≠]0 = cobounded = atBot⊔atTop. The ±∞(at)↦0(at) rows drop the sign, so they are sound but lose information. |
| C9 | (implicit) analyticInv is involutive on the 4 directional germs but not on 0(at)/±∞(at) (inv(+∞at)=0at, inv(0at)=family) | consequence | S2 | TRUE (finite cases). |
| C10 | LimitArithmetic `add`: finite sums; (+∞at)+(−∞at) = (−∞)+(+∞) = indet ∞−∞; (+∞)+(+∞)=+∞; (−∞)+(−∞)=−∞; ±∞+finite=±∞; other cases undefined; `add_opposite_infinities` | def+thm✓ | S3 | TRUE[EReal]: `EReal.continuousAt_add` away from (⊤,⊥),(⊥,⊤); at (⊤,⊥) every c∈EReal is a limit (f=n+c, g=−n). |
| C11 | LimitArithmetic `mul`: sign rules for ±∞·x (x≠0) and ±∞·±∞; 0·(±∞) = indet 0·∞; `mul_zero_posInfinity` | def+thm✓ | S3 | TRUE[EReal] (`EReal.continuousAt_mul` off (0,±∞); `Filter.Tendsto.atTop_mul_const` etc.). With an unsigned 0, 0·∞ realizes every c∈EReal (f=c/n, g=n). |
| C12 | LimitArithmetic `div`: (±∞)/(±∞) = indet ∞/∞ (4 sign cases); finite/finite delegates to C5/C6; else undefined | def+thm✓ | S3 | TRUE (it is indeterminate). Sharper: same-sign ∞/∞ realizes exactly [0,+∞] and opposite signs [−∞,0], not all of EReal. |
| C13 | The seven classical indeterminate forms (plus custom) | def | S1, S6 | TRUE. Exact limit sets: 0/0, ∞−∞, 0·∞ give all of [−∞,+∞]; 1^∞, 0⁺^0, ∞^0 give all of [0,+∞] ((1+c/n)ⁿ→e^c, (e^{−n})^{−c/n}=e^c, (eⁿ)^{c/n}=e^c, plus the endpoints and oscillation). The Lean files contain no rule at all for the three power forms. |
| C14 | FOUNDATIONS: "reciprocal is involutive on the real projective line" (Projective.lean missing) | prose/thm (absent) | S6 | TRUE[ℝP¹]: [x:y]↦[y:x] is an involution swapping 0↔∞. |
| C15 | FOUNDATIONS: BridgeCertificate ⇒ ValidEndpoint; GapWitness contradicts Exhaustive; OverlapWitness contradicts Exclusive; FirstHit unique on a trajectory | thm✓ (S4) / prose | S4, S6 | TRUE by definition (Laws.lean shows the proof terms; FirstHit uniqueness is the uniqueness of `Nat.find`). The definitions themselves are not in the corpus. |
| C16 | "Not assumed: global associativity, distributivity, field structure, total order, completeness, continuity across horizons, universal information conservation" | prose | S6 | A correct caution. EReal (with the convention ⊤+⊥=⊥) gives a total associative +, but then ∞−∞ stops being "indeterminate". K⊙ is total but replaces distributivity by xz+yz=(x+y)z+0z. No field contains such an element (C40, C63; §5 #7). |
| C17 | CanonicalEmbedding ℕ→ℤ→ℚ→ℝ→ℂ, ℝ→EReal, ℝ→ℝP¹, ℝ→States | def | S5 | TRUE (each injective: `Nat.cast_injective`, `Int.cast_injective`, `Rat.cast_injective`, `Complex.ofReal_injective`, `EReal.coe_injective`, `OnePoint.coe_injective`, `State.finite.inj`). |
| C18 | Domain matrix roles ("ordinals/cardinals: do not treat as a field", "ℝP¹: reciprocity 0↔∞", "Riemann sphere: poles", …) | prose | S7 | TRUE as descriptions (ordinal + is not commutative: 1+ω=ω≠ω+1; cardinals have no additive inverses). |

### 2B. IConstant formal files

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C19 | `I_exists : ∃ i, is_indeterminate i.value ∧ is_total i.value` (Lean); Isabelle/Coq analogues | ax | S10–S12 | TRUE but trivial (take both predicates ≡ True). |
| C20 | `I_duality`: ∃ mult add : IConstant→α→IConstant with mult i x = i ∧ add i x = i | ax | S10 | TRUE but trivial (constant maps), so it need not be an axiom. |
| C21 | **`I_invariant`: ∀ f : IConstant→IConstant, f i = i → f = id** | ax | S10–S12 | **INCONSISTENT in Lean.** Take f := const i to get const i = id, so all IConstant are equal; but ⟨PUnit, fun _=>True, …⟩ ≠ ⟨PUnit, fun _=>False, …⟩. In Coq/Isabelle (abstract type) it is consistent only if the type is a singleton. |
| C22 | `I_absorption`: ∀x ∃op, op i x = i | thm⚠ (L) / ax (C,I) | S10–S12 | TRUE but trivial (op := fun i _ => i). |
| C23 | `I_decomposition`: ∃ π σ δ ω, i = ω(δ(σ(π i))) | thm⚠ / Admitted / ax | S10–S12 | TRUE but trivial (all = id). |
| C24 | `operator_completeness`: every T : IConstant→IConstant is a finite composite of Pi, Sigma, DeltaOp, Omega | thm⚠ (ill-typed) / Admitted / ax with "∨ True" | S10–S12 | The Lean version as intended is FALSE: finite words over 4 fixed maps are countable, while maps IConstant→IConstant are uncountable. The Coq and Isabelle versions are vacuously TRUE (ops := [T]). |
| C25 | `I_idempotent_add/mul`: i+i=i, i·i=i (I_add, I_mul are `sorry`) | thm⚠ / ax | S10, S11 | Unprovable as written (the operations are sorry). TRUE[K⊙]: ⊥+⊥=⊥, ⊥·⊥=⊥. |
| C26 | `I_nontrivial` (Lean: ¬∃r:ℝ, ∀x, i.value = r — Type vs ℝ; Coq: ¬∃r, ∀ctx : I→R, ctx I_constant = r) | thm⚠ / Admitted | S10–S12 | Lean: VAGUE (ill-typed). Coq: TRUE (use ctx := const 0 and const 1). |
| C27 | **Δ axioms**: Δ:ℝ, Δ>0, ∀n>0, Δ<1/n (Lean sorry; Coq Admitted; Isabelle axioms Delta_positive ∧ "∀ε>0 ∀N ∃n>N, Δ<1/n") | ax / thm⚠ | S10–S12, S17 | FALSE in ℝ (Archimedean: take n>1/Δ). **The Isabelle axiom pair is INCONSISTENT**, so Delta_bounds and Delta_very_small are "proved" from False (and their proof also cites a non-existent lemma `Delta_infinitesimal`). TRUE only in *ℝ (Mathlib `Hyperreal.epsilon_pos`, `Hyperreal.epsilon_lt_pos`). |
| C28 | `Delta_existence`: ∃! d, (∀ε>0, d<ε) ∧ ∃pattern, pattern k = 19/10^k | thm⚠ | S10 | FALSE (uniqueness fails: d=−1 and d=−2 both qualify). |
| C29 | `Delta_unique`: (∀ε>0, d<ε) ∧ (∃p, p 1 = 19/10) → d = Δ | thm⚠ / sorry / Admitted | S10–S12 | FALSE (d=−1 and d=−2 cannot both equal Δ). |
| C30 | `Delta_infinitesimal_property` (Lean): ∀ε>0 ∃N ∀n≥N, 1/n<ε; Coq: ∀ε>0 ∃n, Δ<1/INR n | ax | S10, S12 | Lean: TRUE (Archimedean; does not mention Δ). Coq: satisfiable (Δ=1/2, n=1). |
| C31 | `limit_with_I`: f x = x/(x−a) for x≠a ⇒ ∃L, lim_{x→a} f = L | thm⚠ | S10 | FALSE for a≠0 (a=1: x/(x−1)→±∞). TRUE for a=0. |
| C32 | **`I_resolves_indeterminate`**: f,g→0 at a ⇒ ∃L, eventually \|f/g−L\|<ε ∨ \|f/g−Δ\|<ε | thm⚠ / Admitted / **Isabelle ax** | S10–S12 | FALSE: f=x·sin(1/x), g=x, a=0 (sin(1/x) comes near every point of [−1,1]). The Isabelle axiom is therefore INCONSISTENT. |
| C33 | information_conservation: entropy(sup) = entropy(collapsed) + entropy(residual) | Isabelle ax (entropy := undefined) / Coq Admitted | S11, S12 | VAGUE (entropy unspecified; in Isabelle the axiom just forces `undefined::real = 0`). |
| C34 | `level_hierarchy`: level l1 < level l2 → l1 ≠ l2 | thm✓ | S10–S12 | TRUE (trivial). |
| C35 | `IOperatorCategory` (endomaps of IConstant with ∘) | def✓ | S10, S12 | TRUE (trivial). |
| C36 | `collapse_conserves`, `ZFC_compatible : True`, `consistency_equivalent_to_ZFC : True` | thm✓ / ax | S10–S12 | TRUE but vacuous. |
| C37 | Isabelle `I_from_limit`, `limit_x_over_x`: lim_{x→0} x/x = 1 | thm✓ | S11 | TRUE (x/x = 1 on 𝓝[≠]0). |
| C38 | Isabelle `Delta_series_decreasing`: 19/10^{n+1} < 19/10^n | thm✓ | S11 | TRUE. |

### 2C. i-constant-core prose theory

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C39 | Ax1: ∃I : I = 0/0 ∧ I is a well-defined object (not ⊥/undefined) | prose ax | S13, S17 | TRUE[K⊙] (⊥=[0:0] is a total element; the "≠⊥" is only a notation clash). |
| C40 | **Ax2 (duality): ∀x∈ℝ, I·x = I ∧ I+x = I**; also I×2=I, I/2=I, I×∞=I, I×0=I | prose ax | S13, S17, S18 (diagrams) | TRUE[K⊙] and TRUE[transreal Φ]. FALSE in any non-trivial ring (I+x=I ∀x forces x=0; I·0=I forces I=0). |
| C41 | "I is simultaneously identity and annihilator" | prose | S13 | FALSE unless the structure is trivial (identity gives I·x=x, absorption gives I·x=I, so x=I for all x). |
| C42 | Ax3 hierarchy H(ω+1); Ax4 collapse g(a)=I·Δ(f,a); Ax5 I = lim Σ Ψ_k; Ax6 H(S) ≤ H(S∪{I}) = H(I); Ax8 I = Π∘Σ∘Δ∘Ω | prose ax | S13 | VAGUE. |
| C43 | Ax7/MT1: Con(ZFC+Ax(I)) ⟺ Con(ZFC); "V ⊆ V[I] by forcing"; Thm 5 (forcing model M[I]) | prose | S13, S17 | The algebraic part (C39, C40) is TRUE as a definitional extension (K⊙ is constructible in ZFC). The forcing claims are VAGUE. Together with C21 it is FALSE. |
| C44 | MT2: ZFC cannot prove or refute the existence of I; "Fundamental theorem: ZFC+Ax(I) ⊢ I consistent and complete" | prose | S13 | FALSE: K⊙'s ⊥ provably exists in ZFC, and the completeness/consistency claim contradicts Gödel I/II. |
| C45 | Decomposition I = Ω∘Δ∘Σ∘Π unique; P3 minimality; P4 universality ("{Π,Σ,Δ,Ω} base for all transformations"); Thm 3 completeness; Cor 2 unique representation; Thm 10 irreducibility | prose thm | S14, S17 | Universality is FALSE (cardinality; and Ω constant destroys information). Uniqueness/minimality are VAGUE. |
| C46 | Π idempotent, Π†=Π, ker Π ⊕ im Π = U; Σ(A∪B)=ΣA+ΣB−Σ(A∩B); Ω∘f = Ω | prose | S14 | TRUE for orthogonal projections (Mathlib `orthogonalProjection`, `Submodule.isCompl_orthogonal`) and plain finite sums (`Finset.sum_union_inter`). Ω∘f=Ω iff Ω is constant. |
| C47 | Commutators [Σ,Δ] = ℏ·id, [Π,Σ] = ∂, [Ω,Π] = Ω, {Σ,Ω} = 2Ω | prose | S14 | FALSE for bounded or finite-dimensional operators: AB−BA = c·id with c≠0 is impossible (trace; Wintner–Wielandt). The rest is VAGUE. |
| C48 | **Δ = 0.∞19** definitions: (a) 0.1919… = 19/99; (b) code Σ_{k=1}^{10} 19/10^k "≈ 0.2111"; (c) Δ < 1/n ∀n; (d) Σ ∞^k·19/10^k | prose / code | S15, S18 (tutorial) | INCONSISTENT across files: (a) = 0.1919…, (b) actually computes 2.111… (→19/9) while its comment says 0.2111 (= 19/90), and (c) is infinitesimal. (a) and the true value of (b) are fine real numbers. |
| C49 | Δ algebra: Δ+Δ = 0.∞38; Δ² = 0.∞361; I = Δ/Δ; I·Δ = I; Δ = I − Ī; I = 1+Δ; I = Δ·ℵ₀·e^{iπ} | prose | S15 | Under (a): Δ+Δ = 38/99 TRUE; Δ² = 361/9801 ≈ 0.0368 ≠ 0.361… FALSE. I·Δ = I TRUE[K⊙]. I = 1+Δ FALSE for real Δ. The rest is VAGUE. |
| C50 | Thm 3 (Δ): lim_{x→0,n→∞} f(x)·n^19 = f(0)·Δ for analytic f | prose thm | S15 | FALSE (f≡1 diverges). |
| C51 | lim x ln x = −Δ; sin Δ = Δ; ∫₀^Δ f = f(0)Δ; Thm 2 (∃! Δ with aₙ(1/aₙ) = 1+Δεₙ) | prose | S15, S17 | FALSE: lim x ln x = 0 would force Δ=0; sin Δ = Δ only for Δ=0 in ℝ; aₙ(1/aₙ) = 1 exactly, so every Δ works (εₙ=0) and uniqueness fails. |
| C52 | I = lim_{x→0} x/x "is not 1"; 0/0-limits = I·lim f'/g'; **Iⁿ = I (n≥1), I⁰ = 1**; f(I) = a₀ + (Σ_{n≥1} aₙ)·I | prose | S16 | lim x/x = 1 is TRUE, which contradicts "not 1". Iⁿ = I and I⁰ = 1 are TRUE[K⊙]. The f(I) formula is TRUE[K⊙] for non-constant f (both sides ⊥) and FALSE for constant f (RHS = a₀+0·⊥ = ⊥ ≠ a₀). |
| C53 | Classical limits: sin x/x→1; (eˣ−1)/x→1; (tan x−sin x)/x³→1/2; (sin x−x)/x³→−1/6; x(√(x²+1)−x)→1/2; 1+2+3+… "= −1/12" | prose | S16, S18 | TRUE (the last as ζ(−1) = −1/12; Mathlib `riemannZeta_neg_nat_eq_bernoulli`). |
| C54 | Thm 4 (collapse conserves information): H(ψ) = H(ψⱼ) + H(Δ) + (−log\|cⱼ\|²) | prose thm | S17, S18 | FALSE: p=(½,¼,¼) collapsed on j=1 gives H=1.5 bits but RHS = 0+1+1 = 2. The correct grouping law H(p) = H_b(pⱼ) + (1−pⱼ)H(q) is TRUE (Shannon). |
| C55 | **Thm 8: I ≠ 0, I ≠ 1, I ≠ ∞** | prose thm | S17 | TRUE[K⊙] ([0:0] differs from [0:1], [1:1], [1:0]). |
| C56 | **Prop 1: conj(I) = I, 1/I = I** | prose | S17 | TRUE[ℂ⊙] (/[0:0] = [0:0]; conj fixes [0:0]). |
| C57 | Thm 11: {0,1,∞,I,Δ} with extended +,· forms a ("non-standard") field | prose thm | S17 | FALSE (absorbing I gives I·0 = I ≠ 0; also 1/0 exists). |
| C58 | Thm 6 universality: every object is reachable from I (0 = I·0 = Π(I), 1 = Δ(I)) | prose thm | S17 | FALSE[K⊙]: {⊥} is closed under +, ·, / and ⊥·0 = ⊥ ≠ 0. |
| C59 | Collapse operator C = Σ\|ψᵢ⟩⟨ψᵢ\| (complete), C² = C, C† = C, R = 1−C, RC = 0, Tr R = Δ | prose | S18 (symbolic_collapse) | C² = C, C† = C, RC = 0 are TRUE (orthogonal projections). Completeness gives C = 1, R = 0, Tr R = 0, contradicting Δ > 0, so FALSE. |
| C60 | Physics/consciousness/ontology claims (Δx·Δp → I·ℏ/2, ρ = ∞/0 = I, ∇·I = 0, ∇×I = Δ, Φ_max = I, "I ontologically complete", "x,y indistinguishable ⇒ x = y = I") | prose | S18 | VAGUE. |

### 2D. 0-0-formal-suite

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C61 | `IField α` = Field + I with I·I = I, I ≠ 0; instances ℝ, ℂ with I = 1 | def | F2 | TRUE (consistent; models given). |
| C62 | **`I_eq_one`**: in any IField, I = 1; `eq_one_of_idempotent_of_ne_zero`; `eq_I_of_idempotent_of_ne_zero`; `I_pow_eq_I`; `I_inv_eq_I` | thm✓ | F2 | TRUE (Mathlib `mul_eq_zero`; `IsIdempotentElem` in domains). Note it rules out a field model of an indeterminate I. |
| C63 | Audit: OPEN_BRIDGE_00_TO_IFIELD is not formalized; "Field is probably too strong: field laws force every idempotent to be 0 or 1" | prose | F4 | TRUE. Stronger: no non-trivial ring has an absorbing element (C40), so the right ambient structures are wheels, meadows or transreals. |
| C64 | Cone00: `Cone n`, vertex ∈ C, `distToVertex_smul` (λ≥0), `const_zero_collapses`, `I_scaled_eq`, `vertex_I_invariant` | def+thm✓ | F3 | TRUE (trivial; I-scaling is the identity because I = 1). Per the audit: Cone is not convex; `collapse_to_fixed_point` has unused hypotheses; `product_structure : True`. |
| C65 | FundamentalIModel: retraction∘traction = id = traction∘retraction; stabilize idempotent; projection preserved by traction/retraction/twist; ∃x≠y with equal projection; embedReal injective; `FundamentalITheorem` (∃S, π non-injective) | def+thm✓ | F1 | TRUE (trivial). Caveat: `state00 = embedReal 0` definitionally, so the "0/0 state" is indistinguishable from real 0. In `FundamentalIModelExistenceCertificate` the ∃M is vacuous (the property never mentions M). |

### 2E. Logics (three-state, LS6, multistate labels)

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C66 | ThreeState neg/and/or/implies tables | def | M1, M2, M5 | TRUE[K3]: exactly strong Kleene (and=min, or=max on F<N<T, implies = ¬a∨b, N→N = N); exhaustively verified. |
| C67 | `neg_neg`, `neg_neutral`, `de_morgan_and`, `de_morgan_or` | thm✓ | M1 | TRUE[K3] (`decide`). |
| C68 | ch10 Prop: ¬¬φ ≡ φ; φ∧¬φ "can be N"; φ∨¬φ "can be N"; "LEM fails for independent sentences" | prose | M2 | TRUE for the truth-functional K3 algebra. **FALSE under the stated provability semantics val_T**: a classical T proves ¬(φ∧¬φ) and φ∨¬φ, so val_T(φ∧¬φ) = F and val_T(φ∨¬φ) = T always. What fails is the disjunction property, not LEM. Hence val_T is not a K3-homomorphism for ∧ and ∨ (φ independent, ψ = ¬φ: or(N,N) = N ≠ T = val_T(φ∨ψ)). |
| C69 | `evaluate T φ` / val_T: T if T⊢φ, F if T⊢¬φ, N otherwise | def | M1, M2 | TRUE as a definition (well-defined for consistent T). Depends on missing `ConsistencyAndIndependence`. |
| C70 | **val_T(φ) = 3 ⟺ DS(T,φ) ≠ ∅** | prose thm | M2, M5 | TRUE (Gödel completeness for first-order T; immediate if ⊢ is replaced by ⊨). |
| C71 | "0/0 = 3" (`zero_div_zero_is_three := neutral`) | def/notation | M1, M2 | VAGUE (a label only). As arithmetic it conflicts with Lean's 0/0 = 0 and with uma's 0/0 = 1 (C84). |
| C72 | Millennium table (each problem T/F/N relative to ZFC); "truth is theory-relative"; "N if RH independent" | prose | M2, M5 | VAGUE. Caveat: RH is equivalent to a Π⁰₁ sentence (e.g. Lagarias: σ(n) ≤ H_n + e^{H_n} log H_n), so if ZFC is Σ₁-sound and RH is independent, then RH is true. N is not symmetric between T and F for RH. |
| C73 | LS6: neg involutive; meet/join commutative and idempotent | def+thm✓ | M3 | TRUE (exhaustively verified). |
| C74 | **LS6 `deMorgan1`, `deMorgan2`** "proved" by `cases a <;> cases b <;> rfl` | thm (claimed ✓) | M3 | **FALSE (10 failing pairs each), so the file cannot compile.** a=P, b=Ω: ¬(P∧Ω) = ¬I = I but ¬P∨¬Ω = Ω∨P = Ω. DM2 with a=∅, b=T: ¬(∅∨T) = F but ¬∅∧¬T = ∅∧F = ∅. |
| C75 | LS6 meet/join as lattice operations ("partial order structure") | implicit | M3, M4 | FALSE: meet is not associative ((P∧Ω)∧Ω = I∧Ω = Ω but P∧(Ω∧Ω) = I), and absorption fails (F∧(F∨∅) = ∅). join is associative (verified). |
| C76 | LS6 collapse/resolveTension: (T,F), (P,Ω) ↦ I; anything with ∅ ↦ ∅; `collapse_classical_symmetric` | def+thm✓ | M3, M4 | TRUE (definitional). "Critical tension T+F → I" is VAGUE. |
| C77 | LS6 `transition` table, `isStable`, `minimalStableUniverse`; "moving up, states become decidable; moving down, they collapse to ∅/I" | def / prose | M4 | The definitions are TRUE (trivial). The semantics ("P decidable in non-standard arithmetic", "Ω decidable with large cardinals", "T in HF becomes ∅") are VAGUE. |
| C78 | Universe chain "V_ω ⊂ V(ZFC) ⊂ N* ⊂ V_κ" | prose | M4 (LS6.lean doc) | FALSE as an inclusion chain (non-standard models of arithmetic do not contain V; for inaccessible κ, V_κ ⊂ V). |
| C79 | Riemann-system states E₀…E₈ (E₅ = zero s₀, E₆ = Re s₀, E₈ = σ=½, E₀ = 2s−2s); RH ⟺ ∀s₀∈E₅, E₆(s₀) = ½ ⟺ χ_RH = Π π_crit(Re s₀) = 1 | def / prose | P1, P2 | TRUE but a trivial reformulation of RH. |
| C80 | 0/0 outcomes ↔ RH scenarios (finite limit ↔ true, ∞ ↔ false, no limit ↔ independent) | prose | P1 | VAGUE analogy (Π⁰₁ caveat as in C72). |
| C81 | "If RH is independent: all collapses → ½ in some models, some ≠ ½ in others"; "for some zeros Re cannot be determined in ZFC" | prose | P2 | The first holds only via non-standard zeros in models of ZFC+¬RH; the standard model would satisfy RH. The second is VAGUE and likely FALSE for any explicit simple zero (a sign change of Z(t) certifies Re = ½; an off-line zero is certified by the argument principle). |
| C82 | universe00 statuses PROVED (E=0) / REFUTED (∃ε>0, E≥ε "structurally") / OPEN; "exactly one"; ax monotone_progress | prose / ax | E8 | VAGUE (epistemic; REFUTED and OPEN are neither disjoint nor exhaustive as stated). |
| C83 | Examples: lim sin x/x = 1, x²/x → 0, x/x² → ∞ | prose | P1 | TRUE (x/x² → ±∞ one-sided, → cobounded two-sided). |

### 2F. uma

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C84 | `zeroOverZero : ℝ := 1`, `zero_over_zero_is_one` (rfl); "0/0 = lim x/x = 1"; "0/0 = Unidade Absoluta" | def+thm✓ / prose | A1, A7 | TRUE as a separate constant and as lim x/x. FALSE as a law in any structure with (ab)/c = a(b/c): 1 = 0/0 = (2·0)/0 = 2·(0/0) = 2. |
| C85 | Competing values: "0/0 = ∞" (banner), 0/0 := Σ_{p≤47} 1/p ≈ 1.661647 (Ŝ), 0/0 → μ², 0/0 := context choice, `stabilize_division(≈0,≈0) = 1` | prose / code | A5, A6, A7 | INCONSISTENT with each other and with C84. Each is an arbitrary convention. |
| C86 | **AXIOMA 0: I/0 = 0/0 = I/I ≡ I** (with "I/I = 1") | prose ax | A5 | TRUE[K⊙] with I := ⊥ (⊥/0 = ⊥, 0/0 = ⊥, ⊥/⊥ = ⊥), but then "I/I = 1" is FALSE. With I = 1 as the text says it is FALSE (1/0 = ∞ ≠ ⊥ in K⊙, and C84 applies). |
| C87 | `lhopital_zero_form`: f differentiable, f 0 = 0, f'(0) ≠ 0 ⇒ ∃L, Tendsto (f x/x) (𝓝 0) (𝓝 L) | thm⚠ | A1 | **FALSE as stated** (unpunctured 𝓝 0: in Lean f 0/0 = 0, while the punctured limit is f'(0) ≠ 0; f = id). TRUE with 𝓝[≠] 0 and L = f'(0) (`hasDerivAt_iff_tendsto_slope_zero`). |
| C88 | `lhopital_rule_zero_over_zero`: f,g→0 on 𝓝[≠]a; DifferentiableAt f a and g a; deriv g a ≠ 0; deriv f/deriv g → L ⇒ f/g → L | thm⚠ | A2 | **FALSE because of `deriv` junk values**: f = x + x²·1_ℚ(x), g = x, a = 0 (deriv f = 0 off 0, so f'/g' → 0, but f/g → 1). TRUE versions: Mathlib `HasDerivAt.lhopital_zero_nhds` (derivatives on a punctured neighbourhood), or simply f/g → f'(a)/g'(a). |
| C89 | `sinc_removable_singularity`: sin x/x has a limit on 𝓝[≠] 0 | thm⚠ | A2 | TRUE (slope of sin at 0 = cos 0 = 1). |
| C90 | `SingularityNumber` (f, point, limit exists); ax `singularity_number_field` (sums/products realized); `real_embeds_in_singularity` | def / ax / thm⚠ | A2 | TRUE and provable (constant functions). It is a quotient onto ℝ, not a "field extension". |
| C91 | `IndeterminacaoContextual` (num = den = 0, context fn); `resolver_bem_definida` | def+thm✓ | A3 | TRUE (trivial: any value). |
| C92 | `transformacao_valor_zero`: valor_inicial = 0 ⇒ ∃c, d≠0 → valor_final = c | thm (proof wrong) | A3 | The statement is TRUE (witness 0). The in-file witness `energia_processo` leaves the goal 0 = energia_processo, which is false. |
| C93 | `autossuficiencia_minima`: gerada ≥ consumida etc. ⇒ index ≥ 1 | thm⚠ | A3 | FALSE (consumida = 0 gives x/0 = 0 and index 0; negative values also break it). |
| C94 | Ŝ: continuous including d = 0; never ∞; Ŝ(−n,d) = −Ŝ(n,d) | prose | A6 | FALSE: jump at \|d\| = ε (Ŝ(1,ε) = 10¹⁰ vs Ŝ(1,ε/2) = Σp ≈ 328); the code returns Σ(1/p)·sign(n+ε), so Ŝ(−n,d) = Ŝ(n,d) > 0 for small n. |
| C95 | Prime ratios p_{n+1}/p_n: Cesàro mean → 1 "but SD does not → 0" | prose | A7 | The first part is TRUE (p_{n+1}/p_n → 1 by PNT). The second is FALSE (ratios → 1 forces the SD → 0). |
| C96 | Axiom 00.3: lim(gh) = lim g·lim h·"rate correction"; lim_{e→0} ∫e/e = Δt; lim (de/dt)/e = −ω²; Ψ₀ = all states, \|Ψ₀\| = ℵ₀ | prose | A7 | VAGUE or FALSE (a product of existing limits needs no correction factor). |

### 2G. universal-emergent-logic (UEL)

| ID | Statement | Kind | Src | Assessment |
|---|---|---|---|---|
| C97 | "0/0 phase lock": lim_{T→∞}(1/T)∫₀ᵀ (ℝ + 𝕀e^{iωt}) dt = ℝ; Error = ℝ + i𝕀 | prose thm | E1 | TRUE for ω ≠ 0 (\|(e^{iωT}−1)/(iωT)\| ≤ 2/(\|ω\|T)). "0/0" is just a label here. |
| C98 | BSD "torsion phase": lim (1/π(X)) Σ_{p≤X} e^{iθ_p} = 0 via Sato–Tate | prose | E1 | FALSE (non-CM E/ℚ): Sato–Tate gives ∫₀^π e^{iθ}(2/π)sin²θ dθ = 8i/(3π) ≈ 0.849i. Only cos θ_p averages to 0. |
| C99 | Θ̂ = lim ε/ε := `LinearMap.id`; "Hermitian with eigenvalues {0,1}"; `spectral_decomposition` (ill-typed, sorry); Physical = ⊤, Gauge = ⊥ lemmas; `expectation_real` (sorry) | def / thm✓ / thm⚠ | E3 | Hermitian: TRUE (id). "Eigenvalues {0,1}": FALSE (the spectrum of id on H≠0 is {1}). The lemmas are vacuously TRUE. `expectation_real` is TRUE (`inner_self_im`). `feigenbaum_in_spectrum` is ill-formed. |
| C100 | LRE limit triad: L'Hôpital; x^α/x^β (x→0⁺) → 0, ∞, 1 for α>β, α<β, α=β; f = x^α−x^β ⇒ f'/x^{β−1} → −β; ∫₀¹(1−ε)^d dε = 1/(d+1); S_d = dV_d/dr, S_d/V_d = d/r; Riemann sums → ∫ | prose thm | E2 | TRUE (Mathlib rpow limits, `integral_pow`, `EuclideanSpace.volume_ball`). These make precise the slogan "0/0 encodes the order of vanishing". |
| C101 | LRE-3 "∄F: D→ℝ with R(u) ≤ F(π(u))" ⟺ "L'Hôpital cannot resolve uniformly" | prose | E2 | VAGUE. |
| C102 | Logic A grounding: \|num\|,\|den\| < τ ⇒ grounded constant; `nullify_error(1e−12) = 0`; `apply_to_riemann`: on_line ⟺ \|Re−½\| < 1e−10 | code | E7 | TRUE as code semantics but mathematically trivial (thresholding). The "refutation" claims are VAGUE. |
| C103 | UnificationAxioms: A1 (C self-adjoint) + **A5 (each zero height γ gives an eigenvector with eigenvalue ½+iγ) "validates RH by construction"**; A3 [L,P] = i·h·Id, h≠0; A2 "41"; A7 gap ≈ φ·g | ax | E4 | A1+A5 force γ = 0 (self-adjoint ⇒ real eigenvalues), which is FALSE for actual zeros (γ₁ ≈ 14.1347); Hilbert–Pólya needs eigenvalue γ, not ½+iγ. A3 is impossible for bounded or finite-dimensional operators. The rest is VAGUE. |

Rows **C104–C150 (statements about ζ, ξ, the critical strip and line, phase, mirror symmetry,
energy/valley "compression")** are catalogued once, in §4.

---

## 3. Open jumps / hypotheses the corpus itself declares open (near-verbatim, translated)

**T-State OPEN_JUMPS (S8)** — "an item listed is a research question, not a result" (140 items):
- **A. Boundary structure** (1–10): minimal topology for before/at/after; lateral germ vs ideal point; partial order of horizons; continuity across a horizon; compactification of a horizon; two ordered infinities vs one projective ∞; iteration after-∞ → next horizon; trans-horizon states without linear order; collapsing several horizons into equivalence classes; orientation and reversal by negation.
- **B. Singular arithmetic** (11–30): partial algebra with Outcome; multivalued algebra with family; **wheels for division by zero; meadows and totalized inverse; transreal arithmetic as a comparison model; projective arithmetic; extended-real arithmetic**; directional rules for poles; complete classification of the seven classical indeterminate forms; composite/nested forms; powers at horizons; log/exp on states; multivalued roots; branch cuts as state transitions; pole residues as extra information; compatibility of sum, product and collapse; conditional associativity; conditional distributivity; local identities; local and global inverses.
- **C. Infinitesimals/transfinite** (31–42): hyperreals and standard part; asymptotic germs; Hardy fields; Hahn fields; Puiseux series; transseries; surreals; ordinals as order states (no field arithmetic); cardinals as size states; points after infinity via ordinals; via surreals; formal comparison.
- **D. Geometry/analysis** (43–56): Alexandroff compactification; ℝP¹; Riemann sphere; blow-up; resolution of singularities; manifolds with corners; stratifications; sheaves of germs; stalks as local states; analytic continuation; monodromy; distributions/principal values; regularization; renormalization as a parametrized operator "without identifying it with proof".
- **E. State dynamics** (57–70): reachability, absorbing states, cycles, recurrence, bifurcations, attractors, repellers, SCCs, minimal kernels/separators, first passage, hitting probabilities, continuous flows, hybrid systems, trajectory invariants.
- **F. Endpoint logic** (71–84): exhaustiveness; exclusiveness; semantic adequacy; gap, overlap and semantic-mismatch witnesses; classical vs constructive; decidability of the classifier; partial-information states; object state vs proof state; refinement types; quotients of equivalent states; temporal modality; "multivalued logics only when the object requires them, not by default".
- **G. Computability/certification** (85–100): computable classifier; witness extraction; finite model checking; abstract interpretation; "SMT as auxiliary, never as substitute for the Lean theorem"; proof-carrying certificates; axiom, sorry/admit, quantifier and domain-restriction audits; reproducibility by SHA and toolchain; certificate reducers; falsification harnesses; counterexample search; property-based testing; differential testing.
- **H. Bridges to problems** (101–115): formalize the original ProblemSpec; admissible state without losing hypotheses; justified transitions; identify K; prove K indispensable; observing K preserves the endpoint; positive/negative independent of the conclusion; search gap; search overlap; prove adequacy; bridge sufficiency; bridge necessity; transfer to the official formulation; audit equivalence of reformulations; "only then discuss promotion to final proof".
- **I. Domain bridges** (116–128): ℕ→ℤ→ℚ→ℝ→ℂ; ℝ→extended reals; ℝ→ℝP¹; ℂ→Riemann sphere; ℝ→hyperreals; ℝ→surreals; local/global p-adic; archimedean vs p-adic; embeddings vs compactifications; partial functions vs totalizations; limits vs added points; quotients vs new elements; universal properties to choose the right extension.
- **J. Meta-theory** (129–140): category of ProblemSpec; endpoint-preserving morphisms; category of StateSystem; functors problem→state system; observation functors; naturality of certificates; composition of bridges; minimality of kernels; invariants under problem equivalence; theory of non-closure residues; "distance to closure without making it a truth value"; library of bridge patterns.

**T-State FOUNDATIONS §6 / STATUS / README (S6, S9):** "No operation was defined for *after* +∞ or *before* −∞ as if they were numbers; this requires choosing a concrete mathematical extension." Not assumed: global associativity, distributivity, field structure, total order, completeness, continuity across horizons, universal conservation of information, solution of any Clay problem. Not promoted: no solution of an open problem; no after-infinity arithmetic; no universal completeness theorem for the operators; no relative-consistency claim; no concrete certificate for RH, P vs NP, NS, YM, Hodge, BSD or Beal. Promotion rule: a conjecture is closed only with a concrete adapter and a BridgeCertificate verified without sorry, admit or a new axiom containing the conclusion; promotion also needs green Lean CI and audits of sorry/admit, new axioms, quantifier match, domain match, semantic equivalence, gap/overlap witnesses.

**IConstant (S10–S12, S15, S17):** "Provas completas dos teoremas marcados com sorry"; integration with complex analysis; physical applications; computational consistency check. Isabelle `Delta_unique`, `I_nontrivial`, `collapse_preserves_info` (sorry, "requires additional axioms"). Δ conjectures: **C1** "Δ is irrational in an extended sense (not a ratio of ordinals)"; **C2** "Δ transcendental over ℚ(∞)"; **C3** "every trans-finite number is expressible via Δ (Δ generates the trans-finite field)"; Prop 2 "transcendence of Δ: complete proof remains open".

**0-0-formal-suite (F4):** `OPEN_BRIDGE_00_TO_IFIELD` "(not formalized)": "What is the formal object meant by 'indeterminate 0/0', and what theorem maps that object to the IField axioms I*I=I and I≠0 without assuming the desired value?" Gates G6 "0/0 ↔ cone vertex" (semantic only), G7 `product_structure : True` (placeholder), G8 mutual orthogonality in SpectralDecomposition (commented out). README: Zeta "STRUCTURAL / OPEN BRIDGE: the bridge to actual zeros of ζ is not proved"; Navier–Stokes and Geometry "placeholders present".

**riemann-indeterminacy (R3, R4, R7):** "What is postulated: the structural stability principle (A5); the exclusivity of stable phase equilibrium to the critical line; the impossibility of unbalanced compensated structures." "Translation to a classical proof remains an open challenge." Lean sorries: ζ inside `xi`, `xi_functional_equation`, `phase_stability_theorem`, `zeros_at_phase_quantization`, `zero_symmetry` (part), `compensated_at_origin`, `off_critical_unstable`, `hardyZ`, `hardy_zeros_correspond`, `verifiedZeros`, `generalized_phase_stability`.

**riemann-multistate-program (P3, P1):** H5 "Energy–Zero Bridge … currently a working hypothesis that requires rigorous formalization"; **G1** "prove E''(½) > 0 (Rigidity Conjecture)"; **G2** "prove ½ is the unique global minimum"; **G3** "prove zeros can only appear at the stable minimum"; **C→T** "If s₀ is a zero, Re s₀ is a stable critical point of E … the 'Clay step' … does not yet exist in the literature". Program phases 3–5: proof skeleton, refutation skeleton, independence investigation.

**riemann-unity-zero (U1, U3):** "Critical Convexity Conjecture" (rigorous proof is future work). Rigidity: "What remains to prove analytically: the global non-escape condition ∀t ≥ T: R(t) ≥ η(t) > 0"; "if one could establish R(t) ≥ c > 0 or R(t) ≥ c/log t … the Riemann Hypothesis follows" (that implication is itself unjustified; see C137).

**UEL (E6, E3, E4):** K_Bounds "H1 (R ≤ C₀ε^A uniformly) ⟺ RH; H2 (inf α(t) ≥ a* > 0) ⟺ RH; H3 (inf β(t) ≥ b* > ½) weaker; classical Titchmarsh bound insufficient"; "Proof of H1/H2/H3: ❌ Open (≡ RH)". HEAU sorries (spectral_decomposition, expectation_real, navier_stokes_imaginary_artifact, feigenbaum_in_spectrum); UnificationAxioms sorries (eigenvalues_real, spectrum_discrete, P_neq_NP, holographic_reduction).

**meta-millennium (M5):** "The central question is: could any Millennium Problem be formally independent of ZFC or its extensions?"

**uma (A1–A3):** sorries for `lhopital_zero_form`, `unique_prime_factorization`, `prime_event_collision_free`, `blockchain_unique_ids`, `autossuficiencia_minima`, `independencia_logistica_absoluta_alcancavel`, `independencia_logistica_absoluta_viavel`, `vantagem_longevidade`, `sinc_removable_singularity`, `lhopital_rule_zero_over_zero`, `real_embeds_in_singularity`.

---

## 4. ζ / critical strip / critical line / phase / reflection / "compression around ½" statements

Categories: **T&K** (true and known), **≡RH**, **FALSE**, **VAGUE**. No statement phrased as
"symmetric closed endpoints tending to a half-closed middle" or "torsion around a neutral point"
occurs in these 8 repos. The nearest analogues are the energy, barrier and valley claims (C134–C139),
the fixed point s = ½ of s ↦ 1−s (C146), and UEL's "phase torsion = vorticity" (VAGUE, UEL README variants).

| ID | Statement (phrased via I / 0/0 / phase) | Src | Category and why |
|---|---|---|---|
| C104 | FE ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s) | R1, R2, R7, R8, U1, E5 | T&K (Mathlib `riemannZeta_one_sub`, equivalent form). |
| C105 | ζ(0) = −½, ζ(−1) = −1/12, ζ(2) = π²/6, ζ(4) = π⁴/90, Γ(½) = √π | R1, R2 | T&K (`riemannZeta_zero`, `riemannZeta_two`, `riemannZeta_four`, `riemannZeta_neg_nat_eq_bernoulli`, `Real.Gamma_one_half_eq`). |
| C106 | "Compensated 0/0 at s=0 = zero of sin(πs/2) × simple pole of Γ(1−s)"; "sin(πs/2)Γ(1−s) ~ (πs/2)(1/s) → π/2"; "Γ(1−s) ~ 1/s" | R1, R2, R10 (fig. T2) | FALSE: Γ(1−s) → Γ(1) = 1 (poles at s = 1, 2, …), so sin(πs/2)Γ(1−s) → 0. The correct mechanism (stated in R3, R8): the zero of sin cancels the pole of ζ(1−s) (~ −1/s), giving sin(πs/2)ζ(1−s) → −π/2 and ζ(0) = π⁻¹(−π/2) = −½. T&K (a 0·∞ form; Mathlib `riemannZeta_residue_one`). |
| C107 | "ζ(0) = (π/2)ζ(1)·(1/ζ(1)) = −½ after regularization" | R8 | FALSE (ζ(1) is a pole; the derivation reuses Γ(1−s) ~ 1/s). |
| C108 | Every trivial zero −2n is "a similar compensated structure" | R8, R7 | FALSE in the ζ-form (Γ(1+2n) and ζ(1+2n) are finite; a genuine simple zero of sin). TRUE in the ξ-form (the pole of Γ(s/2) cancels the zero of ζ). |
| C109 | Trivial zeros −2,−4,… come solely from sin(πs/2) | R1, R2 | T&K (`riemannZeta_neg_two_mul_nat_add_one`). |
| C110 | ζ(s) = 1/(s−1) + γ + O(s−1) | R8 | T&K (`tendsto_riemannZeta_sub_one_div`). |
| C111 | ξ = ½s(s−1)π^{−s/2}Γ(s/2)ζ entire, zeros = nontrivial zeros, ξ(s) = ξ(1−s) | R2, R7, U1, E5 | T&K (`completedRiemannZeta_one_sub`; ξ = s(s−1)Λ₀/2 + ½). |
| C112 | Lean `xi` (ζ := sorry). If filled naively with Mathlib `riemannZeta` and `Complex.Gamma`: xi 1 = 0 and xi(−2) = 0 (Γ(−1) = 0 junk) | R4 | Using that naive model: `xi_functional_equation` FALSE (xi(−2) = 0 ≠ xi(3) = 3ζ(3)/(2π) ≈ 0.574) and `phase_stability_theorem` FALSE (s=1 counts as a NonTrivialZero with Re = 1). Use `completedRiemannZeta₀`. |
| C113 | `xi_functional_equation` (Lean sorry; Coq/Isabelle axiom over an uninterpreted ζ); `reflection_symmetry` ✓ from it | R4, R5 | T&K for the true ξ. As an axiom on an uninterpreted ζ it is a consistent constraint (ζ ≡ 0 satisfies it). |
| C114 | `zero_symmetry`: NonTrivialZero s → NonTrivialZero (1−s) (part sorry/admit) | R4, R5 | TRUE for the true ξ (1−s = −2n ⇒ s = 1+2n, where ξ ≠ 0). FALSE in the naive model (s=1 ↦ 0 = TrivialZero 0). |
| C115 | Zeros come in ρ, ρ̄, 1−ρ, 1−ρ̄; an off-line zero has a reflected partner; zeros symmetric about the line and the real axis | R1, R2, R3, U5 Thm 2, E5 step 2 | T&K. |
| C116 | "Reflection property ζ(s̄) = ζ(s)" | R2 | FALSE (ζ(2−i) ≈ 1.1504+0.4375i = conj ζ(2+i) ≠ ζ(2+i)). T&K version: ζ(s̄) = conj ζ(s). |
| C117 | Geometric mirror symmetry \|ξ(σ+it)\| = \|ξ(1−σ+it)\| (U1 thm ✓ in prose); H3 \|ξ\|² symmetry; E(σ) = E(1−σ) | U1, P3 | T&K (ξ(1−s̄) = conj ξ(s)). |
| C118 | Stationary point E'(½) = 0 | P3 (thm, proof in prose) | TRUE (symmetry + C¹). |
| C119 | Hardy Z(t) = e^{iθ}ζ(½+it) real; Z zeros ⟺ zeros on the line (`hardy_zeros_correspond` sorry); Riemann–Siegel Z = 2Σ_{n≤√(t/2π)} n^{−½} cos(θ − t log n) + O(t^{−¼}) | R2, R4, R10 | T&K. |
| C120 | θ(t) = arg[π^{−it/2}Γ(¼+it/2)] − (t/2) log π | R1, R2 | FALSE (counts the π factor twice). Standard θ = Im logΓ(¼+it/2) − (t/2) log π; at t=30 the two differ by (t/2) log π mod 2π ≈ 4.60 (checked numerically). θ ~ (t/2) log(t/2πe) is T&K. |
| C121 | "ξ(½+it) = e^{iθ(t)} Z(t)" | R7 | FALSE (ξ(½+it) is real; ξ(½+it) = −½(t²+¼)π^{−¼}\|Γ(¼+it/2)\| Z(t)). |
| C122 | "Zero ⟺ arg ξ(½+it) ∈ πℤ" (R1, R2); "Z(t₀) = 0 ⟺ Θ = π/2 + nπ" (R7); Lean `zeros_at_phase_quantization`: NonTrivialZero s → ∃n, arg(xi s) = (2n+1)π/2 | R1, R2, R4, R7 | FALSE: ξ(½+it) ∈ ℝ for every t, so arg ∈ {0,π} wherever it is non-zero and the condition says nothing. In Mathlib arg 0 = 0, so the Lean statement implies "no nontrivial zeros", refuted by ρ₁ = ½+14.1347…i. |
| C123 | `PhaseStable s := ∃n, arg(xi s) = nπ ∧ Re s = ½` | R4 | With the true ξ it holds at every point of the critical line, so it carries no information about zeros. |
| C124 | "Zeros occur where the accumulated phase θ crosses multiples of π" (Gram's law) | R1, R3 | FALSE as an exact law (Gram's law fails; first Gram-block failure near g₁₂₆). Heuristic only. |
| C125 | "Θ(σ+it) = Θ(1−σ+it) by the FE" | R7 | FALSE. Correct: arg ξ(1−σ+it) = −arg ξ(σ+it) (mod 2π). |
| C126 | Θ = arg ξ "grows monotonically along vertical lines" | R3 | FALSE on σ = ½ (piecewise constant in {0,π}). VAGUE elsewhere. |
| C127 | `CompensatedIndeterminacy f s₀`: f = g·h near s₀ (including s₀), g s₀ = 0, h s₀ = 0 ∨ ¬analytic, f → L ≠ 0; `compensated_at_origin xi 0` | R4, R5 | FALSE: the predicate is unsatisfiable for every f (f s₀ = g s₀·h s₀ = 0, yet Tendsto f (𝓝 s₀) (𝓝 L) forces f s₀ = L ≠ 0). Correct notion: meromorphic orders of g and h add to 0 on 𝓝[≠] s₀ (see §5 #14). |
| C128 | **Phase-Stability Theorem**: nontrivial zeros sit exactly at quantized phase equilibria and are stable iff Re s = ½; (i) every zero with 0 < Re ρ < 1 has Re ρ = ½; (ii) off-line zeros give phase accumulation incompatible with reflection; (iii) the line is the unique locus where compensated indeterminacies stay stable; Lean/Coq/Isabelle `phase_stability`, `off_critical_unstable`; postulate A5 | R1, R3, R4, R5, R7 | ≡RH for (i) and the formal statements (true ξ), unproved. (ii), (iii) and A5 are VAGUE postulates that amount to RH; "stable iff on the line" is VAGUE (simple zeros are stable under perturbation anywhere, by Hurwitz). |
| C129 | "Phase contributions of Γ(s/2) and π^{−s/2} balance exactly on the line" | R1 | VAGUE. The true content is that ξ(½+it) is real (FE + conjugation). |
| C130 | Argument principle on [¼,¾]×[−T,T] equals N(T) | R9 | TRUE as the argument principle (zeros inside, with multiplicity, none on the boundary). Identifying it with N(T) is FALSE (it counts \|γ\| < T, so about 2N(T), and only ¼ < β < ¾). |
| C131 | 2π winding at each zero; Hilbert–Pólya (self-adjoint H with spectrum {tₙ} ⇒ RH); explicit formula as a trace formula; Weyl-type log density | R9 | T&K (winding number 1 per simple zero; a conditional implication). |
| C132 | N(T) = (T/2π) log(T/2π) − T/2π + O(log T); spacing ~ 2π/log T; infinitely many zeros on the line; no zeros on Re = 1 or Re = 0; zeros lie in 0 < Re < 1 | R2, P3 (H4), R7 (A4) | T&K (in Mathlib only `riemannZeta_ne_zero_of_one_le_re`). |
| C133 | "Distance to the line is phase, not metric"; "\|ζ\| explodes as Re → −∞"; off-line pair "at different distances" | R1, R3 | VAGUE. The last premise is FALSE: ρ and 1−ρ̄ are equidistant from σ = ½. |
| C134 | **Energy program**: E(σ) = ∫ w\|ξ(σ+it)\|² dt; G1 E''(½) > 0; G2 ½ is the unique global minimum; P4 "Energy Collapse Theorem" (unique minimizer ½, E'' > 0) | P3, P4 | **TRUE for w ≡ 1 and not RH-relevant**: Δ\|F\|² = 4\|F'\|² gives E''(σ) = 4∫\|ξ'(σ+it)\|² dt > 0, so E is strictly convex and symmetric with unique minimum ½ (numerically E(0.1) = 2.0249, E(0.3) = 2.0130, E(0.5) = 2.0091). For a general w > 0, E'' = 4∫w\|ξ'\|² − ∫w''\|ξ\|² has no automatic sign (VAGUE). |
| C135 | P4 "Energy barriers: E(σ) → +∞ as σ → 0⁺ or 1⁻ (pole of ζ at 1)" | P4 | FALSE (ξ is entire, ξ(0) = ξ(1) = ½, and E is continuous on ℝ). |
| C136 | **H5** (zero ⇒ Re s₀ is a critical point of E); G3; C→T conjecture; "energetic collapse pulls zeros to the line" | P3, P2 | ≡RH given G1/G2 (for w ≡ 1 the only critical point is ½, so H5 ⟺ RH), unproved. The "pull" talk is VAGUE. |
| C137 | Valley u = log\|ξ\| has a σ-minimum at ½; rigidity R(t) = ∂²_σ log\|ξ(½+it)\| > 0 (computed for t ∈ [10,80]); "R_ζ = Re[ζ''/ζ − (ζ'/ζ)²] stays finite and positive at zeros"; "R ≥ c > 0 ⇒ RH" | U3, U4 | "Finite at zeros" is FALSE ((log ξ)'' ~ −1/(s−ρ)² → +∞ on the line). R(t) > 0 for all t is **implied by RH** (Hadamard product: R(t) = Σ_γ (t−γ)⁻²); its unconditional status is open as far as I know. The converse "R > 0 ⇒ RH" is a non-sequitur (it is only local convexity at σ = ½). |
| C138 | Critical Convexity Conjecture: f_t(σ) = \|ξ(σ+it)\| has global minimum 0 exactly at ½ at zero heights ⟺ RH; K = ∂²_σ\|ξ\| > 0 "anchors" zeros | U1 | The ⟺ is tautologically TRUE. "K > 0 everywhere (off zeros)" plus symmetry gives \|ξ\| increasing for σ > ½, which implies RH. Known equivalences: RH ⟺ \|ξ(σ+it)\| strictly increasing in σ > ½ (Sondow–Dumitrescu 2010) ⟺ Re ξ'/ξ > 0 on Re s > ½ (Lagarias 1999). Open, RH-strength. |
| C139 | Geometric prison theorem (moving a zero by ε needs E(ε) → ∞ as ε → 0, yet E(ε) ~ ε² log\|t₀\|/2); corollary: ½ is the only locus | U4 | FALSE (self-contradictory: ε² log t → 0). The corollary is ≡RH. |
| C140 | Area-equilibrium: Area T_n(h) = (t_n/4)\|h−½\| | U2 | FALSE (shoelace gives (t_n/2)\|h−½\|). |
| C141 | **Thm 4.3**: RH ⟺ (avg_n \|A(T_n(h)) − A(T*_n(h))\| = 0 ⟺ h = ½); Cor: Δ(h) > 0 for h ≠ ½; Δ(h) = O(\|h−½\|) | U1, U2 | FALSE: Δ(h) ≡ 0 for every h (dual triangles always have equal area), and the triangles use only t_n, never Re ρ. The O-bound is vacuously TRUE. |
| C142 | √(4n²+h²) = 2n + h²/(4n) + O(n⁻³); lim_{x→∞} √(x²+¼)/x = 1 | U1, U5 | TRUE. |
| C143 | "Transubstanciação": lim_{x→0} √(x²+0.25)/x = 1 via L'Hôpital; "trivial zeros converge geometrically to unity" | U5 | FALSE (the limit is ±∞ and it is not a 0/0 form); the second claim is VAGUE. |
| C144 | **0/0 ≡ ∞/∞** ("extended working space W", conformal invariance; "Point X"; "0/0 = ∞/∞ on the Z axis") | U1, U2, U4, U5 | VAGUE as stated. TRUE[K⊙] (∞/∞ = [1:0]·[0:1] = [0:0] = 0/0), and TRUE for limit classes (f/g with f,g → ∞ equals (1/g)/(1/f) with both → 0, so the achievable limit sets coincide). |
| C145 | UEL "Thm Limite de Desvio": an off-line zero has \|σ−½\| ≥ 0.70 | E5 | ≡RH (nontrivial zeros have \|σ−½\| < ½ < 0.7, so it says no off-line zeros exist). No proof given. |
| C146 | E5 proof: "σ + (1−σ) = 1 ⇒ σ = ½"; "ψ(x) = x + O(x^{½+ε}) is a proved estimate"; P4 "s = ½ is the unique fixed point of s ↦ 1−s" | E5, P4 | The first is FALSE (an identity for every σ). The second is FALSE as "proved": it is equivalent to RH; unconditionally ψ = x + O(x·e^{−c√log x}). The third is TRUE (and s ↦ 1−s̄ fixes the whole line). |
| C147 | "lim_{σ→½} \|ζ(σ+it)\|/ξ(s) = 1 (phase synchronization)" | E5 | FALSE (at t=0: \|ζ(½)\|/ξ(½) = 1.46035/0.49712 ≈ 2.938). |
| C148 | RH ⟺ uniform convergence of the AFE error energy E^(1)(t) = ½∫₀¹R(ε;t)²/ε dε; von Koch RH ⟺ ψ(x) − x = O(√x log² x); ∫₀(log 1/ε)^{−2β} dε/ε < ∞ ⟺ β > ½ | E6 | The first equivalence is VAGUE (asserted, unproved). Von Koch is T&K. The integral lemma is TRUE. |
| C149 | Logic B: "20% phase noise pushes wandering zeros back; resonance exactly at σ = 0.5" (simulation) | E7 | VAGUE (no theorem; zeros of ζ are not dynamical objects). |
| C150 | UEL A5 eigenvalues ½+iγ of a self-adjoint C "validate RH" | E4 | FALSE as intended (see C103). |

---

## 5. TRUE, non-trivial laws most worth formalizing (with the cleanest model)

1. **Limit sets of the seven indeterminate forms** (EReal + filters). For f → a, g → b: the set of achievable limits of op(f,g) is all of EReal for 0/0, ∞−∞ and 0·∞ (unsigned 0), and exactly [0,⊤] for (+∞)/(+∞), 1^∞, 0⁺^0, ∞^0; in each case there are also non-convergent pairs. Justifies C5, C10–C13.
2. **Soundness of the T-State `LimitArithmetic` tables.** Whenever add/mul/div returns `exact v` on the determinate cells, every pair of germs in the input classes tends to class v. Model: germs as `EReal` filters; reuse `EReal.continuousAt_add` and `EReal.continuousAt_mul`.
3. **Directional reciprocal as a filter map:** map inv 𝓝[<]0 = atBot, map inv 𝓝[>]0 = atTop, map inv atTop = 𝓝[>]0, map inv atBot = 𝓝[<]0, and **map inv 𝓝[≠]0 = atBot ⊔ atTop**. This makes `family {±∞}` a filter supremum (C6, C8). Model: ℝ filters (Mathlib tendsto lemmas plus `Real.cocompact_eq`).
4. **Negation–inversion equivariance in T-State:** `analyticInv (negate s) = Outcome.map negate (analyticInv s)` for all s, and negate is an involution compatible with the filter model (map neg 𝓝[<]a = 𝓝[>](−a)). Model: the T-State inductive types (finite case split plus `neg_inv`).
5. **Wheel of fractions K⊙ of a field:** construction as a quotient of K² by K^× scaling, and Carlström's wheel axioms (//x = x, /(xy) = /x·/y, xz+yz = (x+y)z+0z, (x+yz)/y = x/y+z+0y, 0·0 = 0, (x+0y)z = xz+0y, /(x+0y) = /x+0y, 0/0+x = 0/0). This is the cleanest model of "I = 0/0".
6. **⊥-calculus in K⊙:** ⊥ := 0/0 is absorbing for + and ·; /⊥ = ⊥; ⊥ ∉ {0, 1, ∞}; 0·∞ = ∞/∞ = ∞+∞ = ∞−∞ = 0/0 = ⊥ while 1/0 = ∞ ≠ ⊥; ⊥ⁿ = ⊥; ⊥/0 = 0/0 = ⊥/⊥ = ⊥; {⊥} is closed under all operations; x/x = 1 iff x ∉ {0, ∞, ⊥}. Validates C39, C40, C52, C55, C56, C86 (with I = ⊥), C144 and refutes C57, C58.
7. **No-go theorems:** (a) in a non-trivial semiring or ring, no I satisfies ∀x, I+x = I, and none satisfies I·0 = I with I ≠ 0; (b) a non-zero idempotent in a field is 1 (already C62); (c) K⊙ is not a ring (0·∞ ≠ 0, ∞−∞ ≠ 0). Model: Mathlib `Ring`/`Field` plus the K⊙ above.
8. **Projective reciprocity:** on ℝP¹ (`OnePoint ℝ`), x ↦ 1/x with 0 ↔ ∞ is an involutive homeomorphism; restricted to ℝ\{0} it is inv. Model: `OnePoint ℝ` or `Projectivization` of K².
9. **K3 algebra:** ThreeState with min, max, ¬ is a bounded distributive lattice and a De Morgan/Kleene algebra (a∧¬a ≤ b∨¬b). N is the unique fixed point of ¬; implies = ¬a ∨ b; a ∨ ¬a = T fails only at a = N. Model: `ThreeState` (`decide`).
10. **K3 is sound but incomplete for the provability/semantic value.** For T consistent and closed under classical consequence (or semantically, T = a set of valuations): val_T(¬φ) = ¬val_T(φ) exactly; for ∘ ∈ {∧, ∨, →}, if K3(val φ, val ψ) ∈ {T, F} then val_T(φ∘ψ) equals it; strictness is witnessed by φ independent, ψ = ¬φ. This corrects C68. Model: propositional valuations, or Mathlib `FirstOrder.Language.Theory` with ⊨.
11. **Dual-State theorem:** val_T(φ) = N ⟺ both T ∪ {φ} and T ∪ {¬φ} are satisfiable (C70). Model: Mathlib `Theory.IsSatisfiable` and `Theory.models_iff_not_satisfiable`.
12. **LS6 refutations (decidable):** `¬ ∀ a b, neg (meet a b) = join (neg a) (neg b)`, the same for DM2, `¬` meet-associativity, and meet/join commutative with join associative (C73–C75). Model: `LS6State` (`decide`).
13. **ξ symmetries in Mathlib:** Λ(s̄) = conj Λ(s) (may need proving), together with `completedRiemannZeta_one_sub`. This gives ξ(½+it) ∈ ℝ, |ξ(σ+it)| = |ξ(1−σ+it)|, and a zero set invariant under s ↦ 1−s, s̄, 1−s̄ (C111, C115, C117, and the corrected C116, C121, C125). Model: `completedRiemannZeta₀` with ξ = s(s−1)Λ₀/2 + ½.
14. **"Compensated indeterminacy" done right:** if g has a zero of order m and h a pole of order m at s₀, then g·h extends analytically with a non-zero value (the meromorphic orders add). Instance: sin(πs/2)·ζ(1−s) → −π/2 at s = 0, hence ζ(0) = −½ from the FE (corrects C106, C107, C127). Model: Mathlib `MeromorphicAt` orders and `riemannZeta_residue_one`.
15. **Hardy Z / θ:** with θ(t) := Im logΓ(¼+it/2) − (t/2) log π, the quantity e^{iθ(t)}ζ(½+it) is real, and Z(t) = 0 ⟺ ζ(½+it) = 0 (C119, corrects C120). Model: Mathlib `Complex.Gamma`, conjugation symmetry, item 13.
16. **Energy convexity is unconditional and RH-neutral.** E(σ) = ∫_ℝ |ξ(σ+it)|² dt satisfies E(σ) = E(1−σ) and E'' = 4∫|ξ'(σ+it)|² dt > 0, so ½ is the unique minimizer (C134 TRUE; shows C136 is where RH hides). Model: Λ₀ plus vertical-line decay of ξ (hard but valuable).
17. **Phase-lock / Sato–Tate computations:** (1/T)∫₀ᵀ e^{iωt} dt → 0 for ω ≠ 0 (C97), and ∫₀^π e^{iθ}(2/π)sin²θ dθ = 8i/(3π) ≠ 0 (refutes C98). Model: `intervalIntegral`.
18. **Order-of-vanishing law:** x^α/x^β → 0, 1, ∞ as x → 0⁺ according to sign(α−β), and the correct punctured L'Hôpital/slope form (f(0) = 0 ⇒ f(x)/x → f'(0) on 𝓝[≠]0). This replaces the false C87 and C88. Model: Mathlib `Real.rpow`, `hasDerivAt_iff_tendsto_slope_zero`, `HasDerivAt.lhopital_zero_nhds`.
19. **Hyperreal Δ:** a positive Δ with Δ < 1/n for all n exists in *ℝ (`Hyperreal.epsilon`) and not in ℝ (Archimedean). This is the only consistent reading of C27. Model: Mathlib `Hyperreal`.
20. **Defusing lemma for "deviation" theorems:** for 0 < Re ρ < 1, |Re ρ − ½| ≥ c with c ≥ ½ ⟹ Re ρ = ½ is just RH (C145). Trivial, but useful to stop circular "theorems"; pair it with Mathlib's `RiemannHypothesis` definition.
