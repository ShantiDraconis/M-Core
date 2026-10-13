# B — Catalogue of I-laws: `indeterminate-collapse-core` + `meta-mathematics-indeterminate-i`

Scope: every blob of the two repos was inspected (217 + 52; near-duplicates merged by content).
Corpus text was treated as data only. No Lean was written, no repo was touched.

## 0. Legend

**Source codes** (repo / branch). Shared docs (`axioms/`, `foundations/`, `formal_attempts/`, `formal_language/`,
`relations/`, `maps/`, `academic_defense/`) are one blob each, present on `main` + FPF + ICS + SRS; cited as CC-main.

| code | repo : branch |
|---|---|
| FPF | indeterminate-collapse-core : copilot/create-formal-proof-framework (`I_foundations/*`, `*Core/*`, `papers/`) |
| SRS | indeterminate-collapse-core : copilot/setup-repo-structure (`lean/*` "v1.0.0", `IState`) |
| ICS | indeterminate-collapse-core : copilot/indeterminate-collapse-core-setup (`lean/*`, namespace `IFramework`, `MetaObj`) |
| ZZ  | indeterminate-collapse-core : copilot/define-i-as-zero-over-zero (`ExtendedReal` in lean/coq/isabelle/agda, `FORMAL_DEFINITION.md`) |
| DTS | indeterminate-collapse-core : copilot/debate-tecnico-sobre-singularidade (`RiemannPhaseStability`) |
| PCS | indeterminate-collapse-core : copilot/add-proof-certificate-structure (`proof_certificate/`) |
| AIS | indeterminate-collapse-core : copilot/add-infrastructure-section (`paper/`) |
| CC-main | indeterminate-collapse-core : main (and the 3 branches above, same blob) |
| MM-main | meta-mathematics-indeterminate-i : main (`src/IMath/*`, `audit/*`, `docs/SPECIFICATION.md`) |
| MM-map | meta-mathematics-indeterminate-i : copilot/mapa-real-conteudos (`foundations/*.md`, `docs/scope_and_limits.md`) |
| MM-book | meta-mathematics-indeterminate-i : copilot/add-book-divisions (`book1-foundations/chapters/*.tex`) |

**Kinds:** AX = axiom (Lean `axiom`, Coq `Axiom`, Isabelle `axiomatization`, Agda `postulate` of a principle);
DEF = definition; THM✓ = theorem with a complete proof in the file; THM-S = theorem with `sorry` / `Admitted` /
Isabelle `sorry` / Agda `postulate` or `{!!}`; PROSE = informal claim.

**Standard models used in the assessments**

| name | model |
|---|---|
| M_opt | `Option α`, I = `none`, Det/Known x = `some x`. Unary lift = `Option.map f`. Absorbing binary lift = `Option.map₂ op` (for `+` this is `WithTop α` with ⊤ absorbing; for `*` it is the "common meadow" ⊥) |
| M_ER | ExtendedReal = ℝ ⊔ {I}: `+` with I absorbing; `0·I = I·0 = 0`, `r·I = I` (r≠0), `I·I = I`; `r/0 = I` for all r, `I/x = x/I = I` |
| M_Φ | `Phi3 α = finite α \| infinity \| indeterminate (Expr α)`; modulo provenance it is Carlström's wheel ⊙ℝ (x/0 = ∞ for x≠0, 0/0 = ⊥, ∞/∞ = ⊥, x/∞ = 0) |
| M_K3 | strong Kleene 3-valued logic, F < I < T, ∧ = min, ∨ = max, p→q = max(¬p, q) |
| M_lim | "0/0 as the set of limit values": pairs/germs (f,g) with f,g → 0 at a point, value = lim f/g if it exists |
| M_ZFC | "I-status = ZFC-independence": K = {φ : ZFC ⊢ φ or ZFC ⊢ ¬φ}, U = the ZFC-independent sentences |
| M_term | free term algebra over ℝ ∪ {I} (no equations involving I) |

---

## 1. Carriers, definition(s) of I, states, operators, transformations

### 1.1 Carriers and definitions of I (five incompatible ones)
1. **`OpState α := Det α | Indet`**, `IState := Indet` (≅ `Option α`). Paths: FPF `I_foundations/Axioms.lean` f7568004. Same shape:
   SRS `lean/Axioms.lean` 4d81e0f0 (`IState α := Known α | Indeterminate`, `IState.I`, notation ♦);
   ICS `lean/Axioms.lean` ff43cc27 (`MetaObj α := Known α | I`);
   CC-main `formal_attempts/{lean,coq,isabelle,agda}` f480a0d8 / 0210e13b / cf65f0cf / a1ec238e (`MetaObject α := Known α | I`);
   SRS `python/utils/state_utils.py` 5613e618 (singleton `Indeterminate`, `I == I` is True).
2. **`ExtendedReal := real ℝ | indeterminate`, `I := indeterminate`, with I = 0/0 realised by `div`.** ZZ `lean/IndeterminateCollapse.lean` 470a9f7f,
   `coq/IndeterminateCollapse.v` e134c3e0, `isabelle/IndeterminateCollapse.thy` b9595ae9, `agda/IndeterminateCollapse.agda` 7edb11b8;
   prose ZZ `FORMAL_DEFINITION.md` 35ac6002, `QUICKSTART.md` 7d8d40e1.
3. **`Phi3 α := finite α | infinity | indeterminate (Expr α)`, `I := indeterminate (div (value 0) (value 0))`** (provenance retained).
   MM-main `src/IMath/Core/Phi3.lean` 1a37e5f4; spec MM-main `docs/SPECIFICATION.md` e32c2148.
4. **I as a meta-symbol ∉ ZFC universe**, "the collapse target of unsolved problems": CC-main `foundations/01_definition_of_I.md` 0281331d,
   `axioms/axiom_0_existence.md` 7b2d3300, `relations/to_ZFC.md` 92f6b10c; typed as `I : MetaSymbol` (singleton type) in
   `formal_language/typing_rules.md` a8bca951; meta repo MM-map `foundations/axioms_I.md` 14a96b67.
5. **I as a single-constructor type** `IndeterminateSymbol := I`: PCS `proof_certificate/computational/lean_stub/IndeterminatePlaceholder.lean` 240f8a6d.
   Plus DTS "compensated indeterminacy" `𝓘_{a,b} = lim a·f/(b·g)` (a 0/0 germ with a limit): DTS `lean4/RiemannPhaseStability/Basic.lean` 1471634f,
   `latex/riemann_phase_stability.tex` 141e5b00.

### 1.2 States
- Det/Known x (determinate) and Indet/I: all carriers above.
- FPF `States.lean` a61aa21d: `ClassicalState α = {s // IsDeterminate s}`, `TheIndetState`, `TransformedState T` (source, result, `T source = result`),
  `Step`, `iterT T n`. FPF `Definitions.lean` 4960d3a1: `Transition T`, `System` (State, initial, valid), `IsDeterminate`, `IsIndeterminate`.
- SRS `Definitions.lean` ddab58c5: `State α := IState α`, `IndeterminateState`, `DeterminateState`; SRS `States.lean` a9a1db30: named states
  `riemannHypothesisState = pVsNPState = yangMillsState = goldbachState := I`, `FiniteStateSpace = [K0,K1,K2,I]`.
- ICS `Definitions.lean`/`States.lean` f02f0391/014a22e3: `State α := (label : String, value : MetaObj α)`, `mkIndeterminate`, `StateSpace`,
  `StateTransition`, `reachable`, order `stateLE`.
- Phi3 states `finite | infinite | indeterminate` (MM-main Phi3.lean).
- Truth values `{tTrue, tFalse, tIndeterminate}` (ZZ, all four assistants).
- Problem domains K (Known) / U (Unknown): CC-main `axioms/axiom_1_duality.md` ef654cc6; Lean `Problem.isKnown` variants (SRS, ICS, formal_attempts);
  SRS `papers/main-paper.tex` 54f1b2cf: K = "decidable in ZFC".

### 1.3 Operators
- Absorbing lifts (I absorbing): FPF `Operators.lean` bef03fab `opAdd, opMul, opNeg`; SRS `Operators.lean` f634c4ee `meta_add/mul/sub/neg, meta_lift1/2`;
  ICS `Operators.lean` 1dbdc8ad `metaAdd/Sub/Mul/Div/Neg/Abs, metaOp2`; formal_attempts `meta_add, meta_mul`; MM-main `Algebra/Absorbing.lean` 341884a0 `absorbingAdd`.
- Zero-annihilating multiplication (0·I = 0): ZZ `ExtendedReal.mul`; ZZ `add`, `div` (r/0 = I).
- Phi3 division `idiv` (0/0 = I, a/0 = ∞, ∞/∞ = indeterminate with provenance): MM-main `Arithmetic/Division.lean` f035dde8.
- Equality-valued operators: ZZ `extEq` (≈), `evalEq` (3-valued), ICS `metaEq` (Kleene-strict, MetaObj Bool), formal_attempts `meta_equiv`.
- Logic: ZZ `tand, tor, timpl` (strong Kleene).
- Lifts of functions: SRS `liftTransformation`, ICS `liftMeta`, formal_attempts `Firewall`/`firewall`.

### 1.4 Transformations and the five named principles
- **Collapse**: (a) constant `Collapse s := Indet` (FPF Definitions.lean); (b) `collapse : Problem → IState Prop`, `if isKnown P then Known P.statement else I`
  (SRS Axioms.lean, ICS Axioms.lean, formal_attempts); (c) selective `collapse_op p` and `total_collapse` (SRS Operators.lean);
  (d) provenance-forgetting `Phi3.collapse` (MM-main `Arithmetic/Collapse.lean` b89c13a5); (e) prose φ : U → {I} (CC-main `axioms/axiom_2_collapse.md` e98c54df),
  rewrite rule φ(u) → I (CC-main `formal_language/rewriting_rules.md` 563b8ea7), C(0/0) = I (PCS `proof_object/collapse_mapping.md` afe31e65).
- **Propagation**: `Propagates T := T Indet = Indet` (FPF Definitions/Propagation 4d90ff2d), `IPropagating`/`Propagates` (SRS Definitions/Propagation 85be1cb6),
  `Transformation.isValid` (ICS Definitions/Propagation c95a0182), axiom P1/P2 (FPF Axioms.lean).
- **Stability**: `Stable sys T` (validity-preserving, FPF), `WellBehaved = PreservesIdentity ∧ Propagates` (FPF `Transformations.lean` 5f24c858, `Stability.lean` 5caabed4),
  `Stable = IPropagating ∧ IdentityPreserving'` and `ValidTransformation` structure (SRS Definitions/Transformations 7763f323/Stability 99a61d00),
  `locallyStable`, `globallyStable` (ICS `Stability.lean` 3d3a907b).
- **Duality** (K ⊕ U): CC-main axiom_1; `axiom_duality` (SRS), `ax_duality` (ICS), `duality` (formal_attempts).
- **Invariance** (one I for all unknowns): CC-main `axioms/axiom_3_invariance.md` 9fcd9071; `axiom_invariance` (SRS), `ax_invariance` (ICS), `invariance` (formal_attempts).
- **Non-interference / firewall**: `axiom_nonInterference` (SRS), `ax_non_interference` (ICS), `non_interference` (formal_attempts); prose "Axiom 4"
  (the file `axioms/axiom_4_non_interference.md` is referenced but absent from the corpus).
- Others: identity-preservation (two different definitions, see B14), `ax_identity_preservation` (ICS), composition `compT/meta_compose/compTransform/metaComp`,
  `iterT`, `chainTransformations` (foldl), `relabel`, `valueTransform`, `zeroCollapse`, `evenFilter`.

---

## 2. Deduplicated table of every axiom / law / rule / state / operator / theorem

### 2a. FPF `I_foundations` (OpState) — axioms

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B1 | `OpState α := Det α \| Indet`, I := Indet | DEF | FPF `I_foundations/Axioms.lean` f7568004 (≡ SRS 4d81e0f0, ICS ff43cc27, formal_attempts f480a0d8) | TRUE: M_opt (`Option α`). |
| B2 | C1: ∀x:α, Indet ≠ Det x | AX | FPF Axioms.lean f7568004 | TRUE in M_opt; provable by `OpState.noConfusion` — redundant axiom. |
| B3 | C2: ∀x, Det x ≠ Indet | AX | same | TRUE, redundant (= C1 symmetric). |
| B4 | C3 as coded: ∀f : OpState α → OpState α, f Indet = Indet ∨ ∃x, (f Indet = Det x → ∃y, (Det y = Indet → False)) | AX | same | TRUE but vacuous: provable by cases on `f Indet` (if Det x take that x, y := x). Does not express "irreducibility". |
| B5 | C3 as prose: "no f : OpState α → OpState α maps Indet to a determinate state" | PROSE | FPF `papers/main-paper.tex` a9153973; Axioms.lean doc | FALSE: f := const (Det a). |
| B6 | **P1: ∀ T : OpState α → OpState β, T Indet = Indet** | AX | FPF Axioms.lean f7568004; paper a9153973 | **FALSE — the axiom is inconsistent.** T := fun _ => Det () on Unit gives Det () = Indet, so False. Every `*Core` file imports it transitively (via `I_foundations.Stability`), so the whole FPF Lean environment proves everything. TRUE only when T is restricted to lifts `Option.map f` or to strict maps. |
| B7 | P2: Propagates T → Propagates U → Propagates (U∘T) | AX | same | TRUE (M_opt); also proved as `compT_preserves_indet`. Redundant. |
| B8 | I1: s = Indet → t = Indet → s = t | AX | same | TRUE, trivial (provable). |
| B9 | I2: Det x = Det y → x = y | AX | same | TRUE (constructor injectivity), redundant. |
| B10 | I3: Det x ≠ Indet | AX | same | TRUE, redundant (= C2). |

### 2b. FPF `I_foundations` — definitions and theorems

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B11 | `Collapse s := Indet` (constant map) | DEF | FPF `Definitions.lean` 4960d3a1 | TRUE as a definition: const none. |
| B12 | collapse_invariant: Collapse (T s) = Collapse s; Collapse ∘ Collapse = Collapse; Collapse s ≠ Det x | THM✓ | FPF `Operators.lean` bef03fab, `Consistency.lean` 266b16d2, RiemannCore lemmas | TRUE (rfl / constructor disjointness). Trivial. |
| B13 | Propagates T :⇔ T Indet = Indet (= "IndetPreserving", "strict map") | DEF | FPF Definitions.lean, Axioms.lean | Strict maps on M_opt. |
| B14 | Identity-preservation, two definitions: (i) ∀x, T(Det x) ≠ Indet (Axioms.lean); (ii) ∀x ∃y, T(Det x) = Det y (Definitions/Transformations) | DEF | FPF f7568004, 4960d3a1, 5f24c858 | (i) ⇔ (ii) in M_opt, TRUE (unstated; easy). |
| B15 | compT_preserves_indet / seq_closure; idT_propagates; constIndet_propagates | THM✓ | FPF Operators.lean, `Propagation.lean` 4d90ff2d | TRUE (M_opt). |
| B16 | propagation_preserves_structure, closure_under_transformation, isIndet_invariant_of_propagating, transformedIndet, indet_is_fixed_point | THM✓ | FPF Propagation.lean, Operators.lean, `States.lean` a61aa21d, Stability.lean 5caabed4 | TRUE; restatements of the definition of Propagates. |
| B17 | propagation_no_collapse: Propagates T → T Indet ≠ Det x | THM✓ | FPF Propagation.lean | TRUE. |
| B18 | indet_unique: {s // IsIndeterminate s} is a subsingleton | THM✓ | FPF States.lean | TRUE. |
| B19 | iterT_propagates, iter_closure, indet_stable_under_iter: T^[n] Indet = Indet | THM✓ | FPF States.lean, Stability.lean | TRUE (induction). |
| B20 | opAdd/opMul: Det x ⊕ Det y = Det(x⊕y), otherwise Indet; opAdd_propagates_left/right, opMul_propagates_left; opNeg Indet = Indet | DEF+THM✓ | FPF Operators.lean, Propagation.lean | TRUE: M_opt with `Option.map₂` (I absorbing). |
| B21 | idT_preserves_identity, comp_preserves_identity, idT_wellBehaved, comp_wellBehaved | THM✓ | FPF Transformations.lean 5f24c858 | TRUE. |
| B22 | valid_preserves_consistency; identity_preserved_under_valid_transition; stable_transition_exists | THM✓ | FPF Transformations.lean, Stability.lean | TRUE. |
| B23 | stability_under_iter: valid T → valid s → valid (T^[n] s) | THM✓ (proof broken) | FPF Stability.lean | Statement TRUE; the given proof does not typecheck (`ih` is about `iterT T n s`, goal about `iterT T n (T s)`; `hV` unused). Needs `induction n generalizing s`. |
| B24 | consistency_of_I_system, no_immediate_contradiction, det_indet_disjoint, det_initial_is_consistent, collapse_is_consistent | THM✓ | FPF Consistency.lean 266b16d2 | TRUE (from C1/I3, which are provable anyway). |
| B25 | "The I-framework does not derive ⊥ from its axioms" | PROSE | FPF Consistency.lean notes; paper a9153973 | FALSE: P1 (B6) derives ⊥. |
| B26 | "Transformations form a monoid under compT with unit idT" | PROSE | FPF Operators.lean notes | TRUE (function composition), unproved there; proved in ICS (B63). |

### 2c. SRS `lean/` (IState, v1.0.0)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B27 | axiom_existence: I ≠ Known x | AX | SRS `lean/Axioms.lean` 4d81e0f0 | TRUE, redundant (constructors). |
| B28 | isKnown P :⇔ ∃ b : Bool, (b = true ↔ P.statement); isUnknown := ¬isKnown | DEF | same | Classically isKnown P holds for every P (b := decide P), so isUnknown P ↔ False and U = ∅. |
| B29 | axiom_duality: isKnown P ⊕ isUnknown P | AX | same | Ill-typed as written (`Sum` on Props, needs `PSum`/`Or`); classically TRUE (LEM). |
| B30 | axiom_collapse: isUnknown P → (I : IState Prop) = I | AX | same | TRUE trivially (says I = I). |
| B31 | collapse P := if isKnown P then Known P.statement else I | DEF | same | With B28: collapse P = Known P.statement for all P, so collapse P ≠ I is provable. "RH collapses to I" is **refutable** in this file's own semantics. File has no imports, so the `if` lacks a `Decidable` instance (compile risk). |
| B32 | axiom_invariance: isUnknown P → isUnknown Q → collapse P = collapse Q | AX | same | TRUE (both sides I by definition), and vacuous by B28. |
| B33 | axiom_nonInterference: lift f I = I, lift f := Option.map f | AX | same | TRUE by rfl, redundant. |
| B34 | I_ne_known, known_ne_I, lift_preserves_I | THM✓ | same | TRUE. |
| B35 | IdentityPreserving T (uses partial `extract` with `sorry`); IdentityPreserving' : ∀x ∃y, T(Known x) = Known y; Consistent T; IPropagating; Stable := IPropagating ∧ IdentityPreserving'; CollapseMap structure; Propagates | DEF (one with sorry) | SRS `lean/Definitions.lean` ddab58c5 | Definitions. The first `IdentityPreserving` contains `sorry` in its body. |
| B36 | liftTransformation_propagates / _identityPreserving / _stable / _propagatesI | THM✓ | same | TRUE (M_opt). |
| B37 | meta_add/mul/sub/neg/lift1/lift2 absorbing; meta_add_I_left/right, meta_mul_I_left/right, meta_lift2_I_left, meta_lift1_I, meta_compose_preserves_I | DEF+THM✓ | SRS `lean/Operators.lean` f634c4ee | TRUE: M_opt `Option.map₂`. |
| B38 | collapse_op p: I ↦ I; Known x ↦ (p x ? I : Known x); collapse_op_preserves_I | DEF+THM✓ | same | TRUE. (Also idempotent, not stated, TRUE.) |
| B39 | total_collapse : IState α → IState (IState α) := Known I | DEF | same | Odd: returns `Known I` one level up, not I. VAGUE as a "total collapse". |
| B40 | ipropagating_propagates, lift_propagates_I, valid_propagates, compose_propagates, propagation_does_not_create_known, global_propagation_theorem, I_is_fixpoint_of_ipropagating | THM✓ | SRS `lean/Propagation.lean` 85be1cb6 | TRUE. |
| B41 | chain_propagates; propagation_chain_stays_indeterminate; I_absorbing (foldl-chain of IPropagating maps fixes I) | THM-S | same | TRUE (induction on the list, generalising the accumulator). |
| B42 | propagation_not_determinising (disjunction, right disjunct = IPropagating) | THM✓ (aux def has sorry) | same | TRUE, trivial. |
| B43 | ValidTransformation {fn, prop : IPropagating, ident : IdentityPreserving'}; validLift; identityTransformation; composeValid (ident field `sorry`) | DEF / THM-S | SRS `lean/Transformations.lean` 7763f323 | composeValid's missing obligation is TRUE (composition of identity-preserving maps). |
| B44 | stable_maps_known_to_known, stable_maps_I_to_I, stable_known_not_I, valid_compose_stable, stable_preserves_determinate/_indeterminate, system_stability_theorem, valid_does_not_indeterminate, valid_does_not_resolve, global_stability | THM✓ | SRS `lean/Stability.lean` 99a61d00 | TRUE. Underlying unstated fact: Stable T ⇔ ∃f, T = Option.map f (TRUE). |
| B45 | collapse_known_not_I, collapse_unknown_is_I, collapse_known_ne_unknown, consistent_preserves_known, consistent_compose | THM✓ | SRS `lean/Consistency.lean` de5e2521 | TRUE (collapse_unknown_is_I is vacuous by B28). |
| B46 | IState_has_two_distinct_elements; system_not_trivially_inconsistent: ¬∀α s, s = I; identity_witnesses_non_triviality | THM✓ | same | TRUE. |
| B47 | axioms_consistent: ¬∃P, P ∧ ¬P | THM✓ | same | TRUE tautology; says nothing about the axioms (misnamed). |
| B48 | apply_I_propagating, chain_nil, chain_singleton, id_compose_left, compose_id_right; zeroCollapse (Known 0 ↦ I), evenFilter, both IPropagating | DEF+THM✓ | SRS Transformations.lean | TRUE. zeroCollapse/evenFilter are not identity-preserving. |
| B49 | riemannHypothesisState = pVsNPState = yangMillsState = goldbachState := I; I_in_FiniteStateSpace; length = 4; isIndeterminate/isKnown/extractWithDefault lemmas | DEF+THM✓ | SRS `lean/States.lean` a9a1db30, `Examples.lean` 61d77a5e | TRUE by definition. Note the clash with B31 (collapse ⟨RH⟩ = Known RH). `rfl` examples over `State Prop` need `DecidableEq Prop` (compile risk). |

### 2d. ICS `lean/` (IFramework, MetaObj, labelled states)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B50 | ax_existence: indeterminate ≠ Known x | AX | ICS `lean/Axioms.lean` ff43cc27 | TRUE, redundant. |
| B51 | isKnown p := Decidable p.statement; ax_duality: isKnown p ∨ ¬isKnown p | DEF+AX | same | `Decidable` is a Type, so ill-typed as a Prop. Read as `Nonempty (Decidable p)`, it is classically true for every p. Then U = ∅ and duality is TRUE (LEM). |
| B52 | ax_collapse: ¬isKnown p → collapse p = I; ax_invariance | AX | same | TRUE (by definition of `collapse`), and vacuous. |
| B53 | ax_non_interference: liftMeta f I = I | AX | same | TRUE (rfl), redundant. |
| B54 | ax_identity_preservation (A5): T I = I → ∀x, x = I → T x = I | AX | same | TRUE, trivial (substitution). |
| B55 | State := (label, value); isValid T :⇔ ∀s, s.value = I → (T s).value = I; propagation_single_step, propagation_finite, non_collapse, propagation_concat | DEF+THM✓ | ICS `lean/Definitions.lean` f02f0391, `Propagation.lean` c95a0182 | TRUE. |
| B56 | propagation_transition: t.transform valid ∧ t.source indet → t.target indet | THM✓ (proof ill-typed) | ICS Propagation.lean | FALSE: `StateTransition` does not require target = transform source. Counterexample: source = I-state, target = (l, Known 0), transform = id. |
| B57 | locallyStable, valid_implies_locally_stable, I_globally_stable, stability_under_extension, stability_summary | THM✓ | ICS `lean/Stability.lean` 3d3a907b | TRUE. |
| B58 | isIdentityPreserving T :⇔ T mkIndeterminate = mkIndeterminate; I_fixed_point_id; I_fixed_point_of_identity_preserving | DEF+THM✓ | ICS Definitions.lean, Stability.lean | TRUE by definition. Type error: `mkIndeterminate : State String` is used at `State α`. |
| B59 | stateLE s t :⇔ (s indet → t indet), "state lattice"; I_state_is_top | DEF+THM✓ | ICS `lean/States.lean` 014a22e3 | Preorder TRUE, and I is top (TRUE). "Lattice / ordering" is FALSE: not antisymmetric (two I-states with different labels). |
| B60 | I_state_not_determinate; partition / indeterminateCount | THM✓/DEF | same | TRUE. |
| B61 | idTransform valid; compTransform_isValid; relabel_isValid; valueTransform_isValid (f I = I ⇒ valid) | THM✓ | ICS `lean/Transformations.lean` d5ab99fa | TRUE. |
| B62 | metaEq: (Known x, Known y) ↦ Known (x == y); any I ↦ I | DEF | ICS `lean/Operators.lean` 1dbdc8ad | Kleene-strict equality on M_opt. TRUE as definition; monotone in the information order. |
| B63 | canonicalMonoid: (Transformation α, ∘, id) is a monoid | THM✓ | ICS Transformations.lean | TRUE (rfl). |
| B64 | Model = MetaObj Unit; framework_consistency (I ≠ Known (), liftMeta id I = I, metaAdd I I = I, metaAdd Known I = I); paper Thm "A0–A5 consistent" | THM✓ | ICS `lean/Consistency.lean` 7b322b7f; ICS `paper/main.tex` 7f2224e4 | TRUE: all ICS axioms hold in `Option Unit`. Unlike FPF, the ICS axiom set is consistent. |
| B65 | metaAdd/Sub/Mul/Div/Neg/Abs absorbing, metaAdd_I_left/right, metaMul_I_left/right, metaNeg_I | DEF+THM✓ | ICS Operators.lean | TRUE (M_opt). |

### 2e. ZZ `ExtendedReal` (lean/coq/isabelle/agda) and FORMAL_DEFINITION.md

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B66 | ExtendedReal := real ℝ \| indeterminate; I := indeterminate | DEF | ZZ `lean/IndeterminateCollapse.lean` 470a9f7f; coq e134c3e0; isabelle b9595ae9; agda 7edb11b8 | M_ER. Lean `deriving DecidableEq` over ℝ (noncomputable) is a compile risk. Agda imports a non-existent `Data.Real`. |
| B67 | add: real+real = real; I + x = x + I = I; indeterminate_add_propagation | DEF+THM✓ | same (all four) | TRUE in M_ER (= M_opt `map₂ (+)`, ≅ `WithTop ℝ` additively). |
| B68 | **mul: I·r = r·I = (r = 0 ? 0 : I); I·I = I.** zero_times_indeterminate 0·I = 0, indeterminate_times_zero I·0 = 0, indeterminate_self_composition I·I = I | DEF+THM✓ (Agda: 0·I, I·0 postulated) | same; FORMAL_DEFINITION 35ac6002 props 1–3; QUICKSTART 7d8d40e1; README 05e7b1cd | TRUE in M_ER. **Contradicts** B20/B37/B65 (I absorbing for ·, so 0·I = I), B141(3) (I·c = I for all c), and B115 ("no reduction"). |
| B69 | div: r/s classical (s≠0); r/0 = I for every r; I/x = x/I = I. zero_div_zero 0/0 = I, nonzero_div_zero r/0 = I | DEF+THM✓ (Agda: postulated) | same | TRUE in M_ER (definitional). |
| B70 | add_comm, add_assoc, mul_comm (w.r.t. ≈) | THM✓ (Agda: postulated real laws) | same | TRUE in M_ER. (mul_assoc also TRUE, not stated; see §4.) |
| B71 | extEq: real r₁ ≈ real r₂ ⇔ r₁ = r₂; I ≈ I; else False | DEF | same | extEq x y ⇔ x = y (TRUE, provable by cases), so ≈ is plain equality. |
| B72 | classical_consistency_add/mul/div (s≠0); add_zero_r; mul_one_r | THM✓ (Agda: some postulated) | same | TRUE: `real` is a homomorphism wherever defined. |
| B73 | indeterminate_unique (x ≈ I → x = I); real_not_indeterminate | THM✓ | same | TRUE. |
| B74 | Property 4: ∀x ≠ 0, x/0 = I·x | PROSE | ZZ FORMAL_DEFINITION 35ac6002 | TRUE in M_ER (both sides are I). FALSE if extended to x = 0 (0/0 = I but I·0 = 0). |
| B75 | Implicit distributivity / "wheel algebra structures are models" | PROSE | FORMAL_DEFINITION §4.4 | FALSE. I·(1 + (−1)) = I·0 = 0, but I·1 + I·(−1) = I + I = I. Carlström's wheel axiom (x+y)z + 0z = xz + yz fails at x=1, y=−1, z=I (0 vs I). Also in any wheel 0·(0/0) = 0/0, not 0. M_ER is not a semiring and not a wheel. |
| B76 | "Axioms consistent relative to ZFC + one inaccessible cardinal" | PROSE | FORMAL_DEFINITION §4.4 | MISLEADING / FALSE requirement: M_ER is a ZFC set, so Con(ZFC) (indeed much less) suffices. |
| B77 | "Indeterminate closure: operations on I may yield I or collapse to determinate values" | PROSE | FORMAL_DEFINITION prop 5 | VAGUE. In M_ER the only collapse is I·0 = 0. |
| B78 | Inference rules: ⊢ 0/0 : I; Collapse rule; Propagation rule ("op(e₁,e₂) undefined classically ⇒ I") | PROSE | FORMAL_DEFINITION §2.2 | VAGUE (conflates type and value). |
| B79 | Truth tables tand/tor/timpl over {T,F,I} | DEF | ZZ all four files; FORMAL_DEFINITION §2.3 | TRUE: exactly strong Kleene K3 (M_K3); I→I = I (not Łukasiewicz). |
| B80 | evalEq: reals ↦ T/F; (I,I) ↦ I; (real, I) ↦ F; QUICKSTART "I = I is neither true nor false" | DEF+PROSE | ZZ all four; QUICKSTART 7d8d40e1 | Definition is consistent but **not** a Kleene-monotone extension of =: evalEq(r, I) = F, yet refining I to r gives T (strong Kleene would give I). Not reflexive (NaN-like). As a claim about Lean `=`, FALSE (I = I by rfl). Contradicts B71 (I ≈ I True), B62 (metaEq (Known,I) = I) and B114 (rewrite I = I → TRUE). |
| B81 | "Decidability: whether an expression collapses is generally undecidable" | PROSE | FORMAL_DEFINITION §3.3 | VAGUE. TRUE for term languages with sin/exp/abs (Richardson 1968: zero-equivalence undecidable); decidable for polynomial or rational expressions (Tarski). |
| B82 | Embedding φ(x) = x preserves operations; "ZFC ⊢ T ⇒ IC ⊢ φ(T)" for T free of division by zero | PROSE | FORMAL_DEFINITION §4.2 | TRUE in M_ER (definitional extension); VAGUE as stated. |

### 2f. formal_attempts skeletons (Lean/Coq/Isabelle/Agda) and notes

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B83 | existence: ∀x, I ≠ Known x | AX | CC-main `formal_attempts/lean` f480a0d8, coq 0210e13b, isabelle cf65f0cf, agda a1ec238e | TRUE, redundant. |
| B84 | Known_domain P: Lean ∃x, x = P ∧ Decidable x (ill-typed); Coq/Isabelle ∃x, x = statement P ∧ (x ∨ ¬x); Agda (x ⊎ ¬x) | DEF | same | Coq (with `Classical`) and Isabelle/HOL prove Known_domain P for every P. In Agda ¬¬KnownDomain P is provable, so UnknownDomain P → ⊥. Either way U = ∅. |
| B85 | duality: Known ∨ Unknown (Lean uses `⊕` on Prop) | AX | same | TRUE (LEM); the Lean version is ill-typed. |
| B86 | collapse P := if Known_domain P then Known (statement P) else I; collapse_unknown; invariance | DEF+AX | same (Agda: collapse postulated) | TRUE and vacuous (Coq/Isabelle/Lean). In Agda, a consistent postulate about an opaque function. |
| B87 | non_interference: ∀f, Firewall f (lifted f maps I to I); Isabelle firewall_composition (sorry) | AX / THM-S | same | TRUE (provable; Lean lacks the `Functor` instance it needs). firewall_composition TRUE, trivial. |
| B88 | **riemann_collapses: collapse RH = I; pvsnp_collapses: collapse PvsNP = I** | THM-S (sorry / Admitted / sorry / postulate) | same | **FALSE** in Lean/Coq/Isabelle semantics: by B84 collapse = Known _ ≠ I. So the Admitted/sorry adds a refutable statement and the file is inconsistent. Coq's "RH" placeholder is ∀s, Z s → True (a tautology). Agda: consistent but contentless. |
| B89 | I_idempotent: collapse ⟨I = I⟩ = I | THM-S | same | FALSE (Coq/Isabelle: Known (I=I) ≠ I). Lean version ill-typed (2 args to a 1-field structure). |
| B90 | collapse_idempotent: collapse ⟨collapse P = collapse P⟩ = collapse P | THM-S | same | FALSE: P := ⟨False⟩ gives Known True vs Known False (propext). |
| B91 | Lean indeterminate_form f g x := I if f x = 0 ∧ g x = 0, else Known (lim f/g) if it exists, else I; example x/x at 0 = I | DEF + THM-S | formal_attempts/lean f480a0d8 | The example is TRUE (unfold and `if_pos`). The semantics assigns I even when the limit exists (x/x → 1), contradicting B120 ("calculus 0/0 ∈ K"). |
| B92 | Coq indeterminate_form: lim f = lim g ⇒ I, else Known (lim f); Isabelle (Some 0, Some 0) ⇒ I \| (Some l, _) ⇒ Known l; Agda analogous | DEF | coq 0210e13b, isabelle cf65f0cf, agda a1ec238e | FALSE as limit semantics. Coq: f = g = x+3 at 0 gives I though f/g → 1. Coq/Isabelle: f→2, g→4 return 2, not 1/2. The Agda non-linear pattern is ill-formed. |
| B93 | meta_add_preserves_I, meta_mul_preserves_I; meta_equiv refl/sym (proved), trans (Isabelle sorry, Agda postulate); known-injective; I-contradiction | THM✓ / THM-S | same | All TRUE (case analysis). |
| B94 | "∀ f ∈ ZFC-Functions: f(I) = I"; "for any ring homomorphism f, f(I) = I"; "collapse I = I" | PROSE | CC-main `formal_attempts/notes.md` 0f295593 | FALSE if f ranges over all maps on a carrier containing I (const 0). TRUE only for lifts `Option.map f`. "Ring hom on I" is VAGUE (I is in no ring). collapse I = I is TRUE in M_Φ (B127). |

### 2g. Prose axioms 0–4, foundations, formal language, relations (CC-main)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B95 | Axiom 0: ∃ I ∈ M, I ∉ ZFC-universe, I atomic, "represents 0/0"; "I ∉ V_α for all α, I ∉ V"; "ZFC cannot create an object representing undefinedness" | PROSE | CC-main `axioms/axiom_0_existence.md` 7b2d3300; `foundations/00_overview.md` aa01e039; `03_meta_mathematics.md` 88e8f907; `relations/to_ZFC.md` 92f6b10c | VAGUE / FALSE. Every carrier above is a ZFC set (Option ℝ, the flat domain ℝ_⊥, wheels, meadows); a fresh point is adjoined routinely (e.g. I := ℝ ∉ ℝ). "I ∉ V" is incoherent for any formal model. TRUE reading: I is a fresh constant outside the base carrier. |
| B96 | Axiom 1 (Duality): every problem P = K ⊕ U, K ∩ U = ∅, collapse(U) = I. K = "∃ ZFC definition/proof", U = "no solution in the current framework"; SRS paper: K = "decidable in ZFC" | PROSE | CC-main `axioms/axiom_1_duality.md` ef654cc6; SRS `papers/main-paper.tex` 54f1b2cf | VAGUE: mixes static ZFC-decidability with epistemic, time-dependent status. Precise model M_ZFC: the partition is TRUE by definition. |
| B97 | Within M_ZFC: "RH ∈ U", "Goldbach ∈ U", "P vs NP ∈ U" (so they collapse to I) | PROSE | axiom_1, axiom_2, axiom_3, maps/general_pattern 0cfedff2, relations/* | UNKNOWN / unsupported. For Π⁰₁ sentences (Goldbach; RH via the Davis–Matiyasevich–Robinson / Lagarias criteria), ZFC-independence implies truth (a false Π⁰₁ sentence has a checkable counterexample, so ZFC ⊢ ¬φ). So "collapse(RH) = I" would entail RH. |
| B98 | Invariance under reformulation: P₁ ≡ P₂ ⇒ same K/U and same collapse ("invariant under logical equivalence") | PROSE | axiom_1 ef654cc6; axiom_3 9fcd9071 | TRUE in M_ZFC if ≡ means ZFC-provable equivalence. FALSE for material/semantic equivalence: all true sentences are materially equivalent to 0 = 0 ∈ K. |
| B99 | Axiom 2: φ : U → {I} constant, total, non-injective, surjective onto {I}, irreversible; "collapse(I) = I (fixed point)" | PROSE | CC-main `axioms/axiom_2_collapse.md` e98c54df | TRUE trivially: a constant map to a singleton is non-injective iff \|U\| ≥ 2 and surjective iff U ≠ ∅. "Fixed point" is ill-typed (I ∉ U) unless I ∈ U. |
| B100 | Axiom 2: "collapse is well-defined but not computable: u ∈ U cannot be decided algorithmically" | PROSE | same | TRUE in M_ZFC (assuming Con(ZFC)). If {φ : ZFC decides φ} were recursive, ZFC-provability would be decidable. |
| B101 | Axiom 3 (Invariance): ∀u₁,u₂ ∈ U, φ(u₁) = φ(u₂) = I; "one I, not I₁, I₂, …" | PROSE | axiom_3 9fcd9071; `foundations/01_definition_of_I.md` 0281331d | TRUE, redundant (follows from Axiom 2's constant map). Contradicts B135 (context-dependent I), the Phi3 provenance design (B126, B128), and general_pattern "I₁, I₂, Relationship(I₁, I₂)" (0cfedff2). |
| B102 | Axiom 4 (Firewall): "I does not appear in any theorem provable in ZFC alone" | PROSE | 0281331d; `foundations/02_scope_and_limits.md` a21ec877; `academic_defense/common_objections.md` 78cb8e62 | TRUE trivially (I is not in the language of ZFC). It is not a conservativity proof (see B106). |
| B103 | "I + x, I×x do not reduce; no ordering; no evaluation; no substitution; lim f(I) undefined"; symbols.md "✗ I + 0 = I, ✗ I×1 = I, ✗ I − I = 0, ✗ I² = 0, I/I ≠ 1" | PROSE | 0281331d; CC-main `formal_language/symbols.md` ff43f9af; rewriting_rules 563b8ea7 | TRUE in M_term. **Contradicts** B20/B37/B67 (I + 0 = I, I×1 = I proved in Lean), B68 (I·I = I, I·0 = 0) and MM-map B136. |
| B104 | "I is not a number / extended number / hyperreal / surreal; does not provide a value for 0/0" | PROSE | a21ec877 | VAGUE. Contradicts ZZ (0/0 ↦ I as a defined value of M_ER) and MM-main (I ∈ Phi3 ℂ). "0/0 is undefined in *ℝ and No" is TRUE. |
| B105 | Con(ZFC) ⇒ Con(ZFC + M) ("proof sketch: case 2, M's axioms are minimal and don't interact") | PROSE | to_ZFC 92f6b10c | Conclusion TRUE for any fresh-constant / Option reading (interpret I as a fixed set outside the carrier); the argument is invalid. FALSE for the FPF Lean axiom set (B6). |
| B106 | Conservativity: "ZFC+M ⊢ φ (φ I-free) ⇒ ZFC ⊢ φ, because I is not in φ so the proof cannot use M axioms" | PROSE | to_ZFC 92f6b10c; a21ec877 | Conclusion TRUE for definitional/Option models (by interpretation). The argument is invalid: new axioms can yield new I-free theorems. |
| B107 | "Semantic and syntactic conservativity coincide for first-order theories (by completeness)" | PROSE | to_ZFC 92f6b10c | FALSE. Semantic ⇒ syntactic only. E.g. CT⁻ over PA is syntactically conservative, but models that are not recursively saturated do not expand (Lachlan; Kotlarski–Krajewski–Lachlan). |
| B108 | "The proof-theoretic ordinal of ZFC is beyond the recursive ordinals" | PROSE | to_ZFC 92f6b10c | FALSE: the Π¹₁ ordinal of any r.e. (sound) theory is < ω₁^CK (Σ¹₁ bounding). |
| B109 | "Every model of ZFC extends to a model of ZFC+M by an external I, like extending a ZF model to ZF+AC by adding choice functions" | PROSE | to_ZFC 92f6b10c | First part TRUE (expand by a new sort/constant). The analogy is FALSE: models of ZF + ¬AC are not made into ZFC models by adding sets; Con(ZF) ⇒ Con(ZFC) goes through the inner model L. |
| B110 | "No element in any ZFC-constructible field, ring or algebraic structure can consistently represent 0/0" | PROSE | to_ZFC 92f6b10c; 03_meta 88e8f907 | FALSE for "algebraic structure": wheels (Carlström 2004), common meadows (Bergstra–Ponse: 0/0 = ⊥, absorbing), M_ER, M_Φ. TRUE for fields/rings (B111, B164). |
| B111 | "ℝ ∪ {I} cannot be a field" | PROSE | to_ZFC 92f6b10c | TRUE with ℝ as subfield: a proper extension field of ℝ has dimension ≥ 2, so it has more than one new element; and 0·I = 0 is forced, so I is not a quotient 0/0. |
| B112 | Rewriting system: collapse rule φ(u) → I (u ∈ U); "φ(u) = I → TRUE", "x = I → FALSE (x ∈ K)"; congruence; non-expansion; normal forms; "confluent" and "terminating" | PROSE | CC-main `formal_language/rewriting_rules.md` 563b8ea7 | TRUE for the TRS {φ(u) → I \| u ∈ U} ∪ ground arithmetic on I-free terms (orthogonal, size-decreasing, so terminating and confluent). The equality rule contradicts B80. |
| B113 | Typing: I : MetaSymbol (singleton type), φ : Unknown → MetaSymbol, classical operators reject MetaSymbol; "Type Safety Theorem" | PROSE | CC-main typing_rules a8bca951 | TRUE for a simply-typed system with disjoint base types (standard progress/preservation). But it makes "I + 5" ill-typed, contradicting rewriting_rules ("I + 5 is a normal form") and the Lean `opAdd`. |
| B114 | Rewriting: "φ(u) = φ(v) ⟶ I = I ⟶ TRUE" | PROSE | rewriting_rules 563b8ea7 | TRUE for propositional equality. Contradicts B80 (evalEq I I = I). |
| B115 | "Forbidden: arithmetic on I does not reduce" (rewriting non-rules) | PROSE | rewriting_rules 563b8ea7 | Same as B103. |
| B116 | h(x) = x² if RH else x³: "continuity at 0 cannot be proved by ε–δ" | PROSE | CC-main `relations/to_analysis.md` 0415a2f8 | FALSE: δ = min(1, √ε) works for both branches, and by LEM h is provably continuous at 0 (indeed everywhere). |
| B117 | "0/0 has no universal value: sin x/x → 1, x²/x → 0, x/x² diverges; the limit depends on f, g" | PROSE | to_analysis 0415a2f8; 0281331d; to_ZFC (0 = 0·c for all c) | TRUE in M_lim: every c ∈ ℝ is lim (c·x)/x; ±∞ and "no limit" (x·sin(1/x)/x) also occur. The solution set of 0·c = 0 is all of ℝ. |
| B118 | "Δm = I", "inf σ(H) = I", "χ[P=NP] = I", "NS smoothness = I", "Γ_decay = I", "m_DM = I", "χ[multiverse] = I", "BB(n) for large n = I" | PROSE | to_analysis 0415a2f8; `relations/to_computation.md` 270e0716; `relations/to_physics.md` ed56bb11 | VAGUE (category error: a meta-symbol equated to a real number or a Boolean). Precise version "ZFC does not determine the value": TRUE for BB(n) at explicit n (Yedidia–Aaronson 2016, later lowered to ≈745), unknown for the others. Same doc also says "BB(n) has determinate values" (internal clash). |
| B119 | "Oracles move from I to determinate values: χ[P^A = NP^A] = 1, χ[P^B = NP^B] = 0" | PROSE | to_computation 270e0716 | Baker–Gill–Solovay facts TRUE; the "I" reading is VAGUE. |
| B120 | "Calculus 0/0 ∈ K (pseudo-indeterminate); I only for structural unknowns; lim f ≠ I" | PROSE | to_analysis 0415a2f8 | Coherent with M_ZFC. Contradicts B91 (I at every 0/0 point) and MM-book B141(4) (I projects to limits). |
| B121 | Problem ↦ K_P ⊕ I, "P[U_P ↦ I] = K_P ⊕ I"; indexed I₁, I₂ | PROSE | CC-main `maps/general_pattern.md` 0cfedff2 | VAGUE; the indexing contradicts B101. |

### 2h. Proof certificate / stubs (PCS, AIS)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B122 | C(0/0) = I; uniqueness/determinism; invariance under rewriting ((0)/(0), 0 ÷ 0 ↦ I); non-bijective; "irreversible: I cannot be mapped back to 0/0"; Type-II "I + I, I × 0 may yield other symbols or I" | PROSE | PCS `proof_certificate/proof_object/collapse_mapping.md` afe31e65; `proof_object/formal_statement.md` fa767480 | Determinism TRUE trivially. "Irreversible" is VAGUE (C is injective on {0/0}) and is contradicted by M_Φ, where `toExpr I = 0/0` recovers provenance. Type-II is VAGUE. |
| B123 | CORE-1..5 axioms, rules R1–R4, ops Collapse/Representation/Verification, "V('I is consistent') = true" | PROSE | PCS `proof_certificate/dependencies/core_axioms.md` eac70326 | VAGUE (procedural, not mathematical). |
| B124 | lean_stub: axiom indeterminate_nature : ∀x, x = I → True | AX | PCS 240f8a6d | TRUE (tautology). |
| B125 | Projection operators Proj : 𝓘 → X "preserving essential structure" | PROSE | AIS `paper/chapters/ch00_foundations_I/sec_projections.tex` c1aba6a9 | VAGUE. |

### 2i. meta-mathematics-indeterminate-i (MM-main Lean core + MM-map/MM-book prose)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B126 | Phi3, state, toExpr, I := indeterminate (0/0 expr); C01 state I = indeterminate; C02 I ≠ ∞; C03 I ≠ finite z; finite_injective | DEF+THM✓ | MM-main `src/IMath/Core/Phi3.lean` 1a37e5f4; `Certificates/Core.lean` 8bb83bfd | TRUE (M_Φ); genuine kernel proofs. |
| B127 | collapse: finite ↦ finite, ∞ ↦ ∞, indeterminate e ↦ I; collapse_finite/_infinity/_indeterminate/_I; C08 collapse idempotent | DEF+THM✓ | MM-main `Arithmetic/Collapse.lean` b89c13a5 | TRUE. |
| B128 | idiv: a/b = a/b (b≠0); 0/0 = I; a/0 = ∞ (a≠0); finite/∞ = 0; ∞/finite = ∞ (incl. ∞/0); ∞/∞ = indeterminate(∞/∞); indeterminate e / y, x / indeterminate e = indeterminate(div …). C06 zero_idiv_zero, finite_ne_zero_idiv_zero, finite_idiv_finite_ne_zero, C07 infinity_idiv_infinity, finite_idiv_infinity, infinity_idiv_finite | DEF+THM✓ | MM-main `Arithmetic/Division.lean` f035dde8 | TRUE. Modulo provenance it agrees with Carlström's wheel ⊙ℝ. Note I / I = indeterminate((0/0)/(0/0)) ≠ I until collapsed. |
| B129 | absorbingAdd (I absorbs everything, incl. ∞; ∞ absorbs finite); absorbingAdd_I_left/right; C09 not right-cancellative (x + I = y + I, x ≠ y) | DEF+THM✓ | MM-main `Algebra/Absorbing.lean` 341884a0 | TRUE (M_Φ; cf. M_opt / `WithTop`). absorbingAdd forgets provenance. |
| B130 | C04/C05 ofReal/ofComplex injective; C10 refinement transitive; C11 germs x/x ≠ x²/x; C12 x/x resolves to 1; C13 x²/x resolves to 0; C14 both; C15 determinedPoint injective | THM✓ (per ledger) | MM-main Certificates/Core.lean 8bb83bfd; `audit/THEOREM_LEDGER.md` 0630892f | Statements TRUE (M_lim / standard). The supporting sources (`Core/Expr`, `Core/Embeddings`, `Refinement/Realization`, `Analysis/Germ`, `Geometry/Point`) are **not in the corpus**, so the proofs cannot be checked here. |
| B131 | "Core does not install Field (Phi3 α); laws tested one by one; failed laws kept as counterexamples"; "zero project axioms" | PROSE | MM-main `docs/SPECIFICATION.md` e32c2148; `README.md` 878464e6 | TRUE for the five visible files: no `axiom`/`sorry`. Phi3 cannot be a field (absorbing I has no inverse). |
| B132 | IField: in a field, x·x = x ∧ x ≠ 0 ⇒ x = 1 | THM (historical, cited) | MM-main `audit/PROVENANCE_MANIFEST.md` 8d93dc48 | TRUE (x(x−1) = 0). Consequence: "I·I = I" (B68, B136) plus I ≠ 0 inside any field forces I = 1, contradicting "I ≠ every classical number". |
| B133 | Axiom 1 Existence (I = 0/0 symbol); Axiom 4 Unification; Axiom 5 "no computable numeric value" | PROSE | MM-map `foundations/axioms_I.md` 14a96b67 | VAGUE (fresh-constant reading consistent). Axiom 5: I has no numeric value at all. |
| B134 | Axiom 2: "I is not in ℝ, ℂ or any standard number system" | PROSE | same | VAGUE; consistent with Option-type carriers. Clashes with MM-main's "three-state numerical domain" containing I. |
| B135 | Axiom 3 / Principle 3: "interpretation of I is context dependent; different problems may give different indeterminacies" | PROSE | 14a96b67; MM-map `foundations/meta_logic.md` 456a867f; MM-map `docs/scope_and_limits.md` b2b653d8 | VAGUE. TRUE in M_Φ before collapse (indeterminate e ≠ indeterminate e′). **Contradicts** CC Axiom 3 Invariance (B101); reconciled only by "invariance = after collapse". |
| B136 | Ops: I + I = I; I + x = I (x ∈ ℝ); I·I = I; I·x = I (x ≠ 0); "ξ = I ∧ δ = I ⇒ ξ + δ = I (not 2I)" | PROSE | 14a96b67 | TRUE in M_opt with map₂ and in M_ER (I·0 left unspecified, so consistent with both). |
| B137 | "ξ = δ = E_crit = c = I (meta-equality)" | PROSE | meta_logic 456a867f | FALSE if = is equality: transitivity forces ξ = δ = c. TRUE only reading "x = I" as a unary predicate Ind(x). Also conflicts with B135. |
| B138 | "Within ZFC: CH = I"; "AC independent of ZF" | PROSE | meta_logic 456a867f; MM-map `foundations/relation_to_ZFC.md` 1091a94c | TRUE in M_ZFC (Gödel 1940, Cohen 1963). |
| B139 | Gödel I ("any consistent formal system containing arithmetic has true unprovable statements"); Gödel II ("no consistent system can prove its own consistency"); "ZFC is consistent if large cardinals exist" | PROSE | meta_logic 456a867f | TRUE with the missing hypotheses (recursively axiomatised, interprets Q/PA). As stated, overgeneral. Inaccessible κ ⇒ V_κ ⊨ ZFC is TRUE. |
| B140 | Def ("the indeterminate"): Form I = 0/0; Domain I ∈ 𝓘; Universality (in any structure with zero and division, I manifests as collapse of 0/0); Non-uniqueness (not determined by any single limit) | PROSE | MM-book `chapters/03-indeterminate-definition.tex` 6104e87b | VAGUE. Non-uniqueness TRUE in M_lim. |
| B141 | Thm "Indeterminate properties": (1) I ≠ c for classical c; (2) I cannot be compared with <, >, =; (3) I + c = I and I·c = I for all c; (4) I admits projections to classical values via limits | THM (sketch) | same | (1) TRUE (M_opt). (2) Self-contradictory with (1) and (3), which use =; "unordered" TRUE. (3) TRUE in M_opt, but FALSE in M_ER at c = 0 (cross-source clash with B68). (4) TRUE in M_lim; contradicts CC "I is not a limit" (B104, axioms_I "distinction from limits"). |
| B142 | Indeterminate space 𝓘 with collapse 𝓒 : S → 𝓘, projection 𝓟 : 𝓘 → S, ∼ identifying indeterminates that project identically | PROSE | same | VAGUE. Concrete model: germs (f,g) with f,g → 0 modulo equal limit (M_lim). |
| B143 | "Fundamental Collapse Theorem: every consistent system admits a collapse structure" (proof: Lindenbaum quotient, "limit") | THM (sketch) | MM-book `chapters/04-foundations.tex` 09e99ba9 | VAGUE (trivially satisfiable by a constant collapse; the sketch proves nothing specific). |
| B144 | Meta-completeness definition; "Meta-incompleteness: no sufficiently expressive system is meta-complete, generalising Gödel" | THM (no proof) | same | VAGUE (not formally defined). |
| B145 | "Projection Theorem: every classical theorem remains valid when projected"; "Lifting Theorem: some classical theorems admit multiple inequivalent liftings"; "framework is conservative and more expressive" | THM (no proof) | same | VAGUE. |
| B146 | Collapse 𝓒 : S₁ × S₂ → I; "limit of the difference quotient is a collapse"; meta-axioms Separation / Projection / Indeterminacy / Collapse ("collapse preserves essential structural information while eliminating classical distinctions") | PROSE | MM-book `chapters/02-meta-mathematical-framework.tex` 655c08de | VAGUE. "Preserves essential information" contradicts CC Axiom 2 ("preserves no information beyond indeterminate", B99). |
| B147 | Modal / 3-valued / type-theoretic / categorical ("I terminal or initial object") options | PROSE | MM-map relation_to_ZFC 1091a94c | VAGUE (programmatic). The 3-valued option = M_K3 (B79). |

### 2j. Millennium encodings (constants used by the bridges)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B148 | X_state := Indet; X_known_state := Det True (RH: Det RH_Known); X_collapse := Collapse (Det False) (RH: Collapse (Det RH_Unknown)); X_unknown_collapses_to_I; X_unknown_is_indet; X_known_consistent; X_decomposition_nontrivial; X_collapse_idempotent; X_I_bridge (X ∈ {RH, BSDCore, ComplexityCore, HodgeCore, NavierStokesCore, YangMillsCore}) | DEF+THM✓ | FPF `*Core/IReformulation.lean`, `IntermediateLemmas.lean`, `MainBridge.lean`, `ComputationalChecks.lean` (see §3) | TRUE by rfl/cases; content-free (see §3). |
| B149 | ComplexityCore: axioms InP, InNP : (ℕ → Bool) → Prop; P_subset_NP; P_equals_NP := ∀L, InNP L → InP L | AX+DEF | FPF `ComplexityCore/ClassicalFormulation.lean` a829cd59 | Consistent (InP = InNP = const True). P_equals_NP is independent of these axioms (InNP = True with InP = True vs InP = False). |
| B150 | RiemannCore: Float-based `Complex`; riemannZeta := sorry; axioms zeta_functional_equation (riemannZeta s = sorry), zeta_euler_product, infinitely_many_on_critical_line; RH_Known := ∃ _ : Complex → Complex, True | AX+DEF (sorry) | FPF `RiemannCore/ClassicalFormulation.lean` 9c9b48b8 | Placeholder, not about the real ζ. zeta_euler_product is trivial (prod := ζ s). The "infinitely many" axiom only asserts one zero (lists may repeat). RH_Known ⇔ True. |
| B151 | BSD/Hodge/NS/YM ClassicalFormulation: X_KnownStructure := True; X_UnknownParameter := sorry | DEF (sorry) | FPF `{BSD,Hodge,NavierStokes,YangMills}Core/ClassicalFormulation.lean` df82485e / 7815417d / 136d1a7c / 36bfff76 | Placeholder; never imported by the IReformulation files. |

### 2k. DTS Riemann "phase-stability" (compensated 0/0 indeterminacy)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B152 | Compensated indeterminacy at s = 0: lim_{s→0} sin(πs/2) / (Γ(1−s))⁻¹ = π/2 ("𝓘^ζ_{0,0} = π/2") | THM-S (Lean sorry; tex "Theorem"; Isabelle sorry; python limit_value) | DTS `lean4/RiemannPhaseStability/Basic.lean` 1471634f; `latex/riemann_phase_stability.tex` 141e5b00; `isabelle/RiemannPhaseStability.thy` e80f1626; `python/riemann_phase_stability.py` 1c9dd05a | **FALSE**: (Γ(1−s))⁻¹ → 1, so the quotient sin(πs/2)Γ(1−s) → 0 (numerically 1.6·10⁻⁴ at s = 10⁻⁴). The corrected law is TRUE: lim_{s→0} sin(πs/2)·Γ(s) = π/2 (since sΓ(s) → 1). |
| B153 | CompensatedIndeterminacy fields: ∃z₀, num z₀ = 0; ∃z₀, den z₀ = 0 (separately); limit at 0 exists. zeta instance: ∃z₀, (Γ(1−z₀))⁻¹ = 0 | DEF + THM-S | DTS Basic.lean 1471634f | Structure is mis-specified (zeros need not be at the anchor). The den witness is TRUE at z₀ = 1, 2, … (Γ poles; in Mathlib Γ 0 = 0 and 0⁻¹ = 0). It is not 0/0 at s = 0. |
| B154 | Expansions: Γ(1−s) = 1 + γs + O(s²); ζ(1−s) = 1/s + γ + O(s) | PROSE | DTS tex 141e5b00 | First TRUE. Second FALSE (sign): ζ(1−s) = −1/s + γ + O(s). |
| B155 | TopologicalAnchor.finite_residue: Tendsto (z ↦ (z−p)⁻¹(z−p)) (𝓝 p) (𝓝 r), r ≠ 0; zero_is_anchor | DEF + THM-S | DTS Basic.lean; Isabelle; Agda a30fe875 | FALSE as coded: the value at p is 0, so the limit along 𝓝 p must be 0 ≠ r. Along 𝓝[≠] p the limit is 1 (TRUE). |
| B156 | isStructurallyStable s :⇔ ∃ε>0, ∀ perturbation with sup ‖·‖ < ε, ∃ s′ ∈ B(s,ε), perturbation s′ = 0; criticalLine_zeros_stable; phaseStabilityTheorem (stable ↔ on line) | DEF + THM-S | DTS Lean/Isabelle/Agda | FALSE for every s (constant perturbation ε/2). Hence criticalLine_zeros_stable is FALSE (ζ(1/2 + 14.1347…i) = 0), and phaseStabilityTheorem is FALSE (it would forbid zeros on the line). riemannHypothesis_from_stability is TRUE only vacuously. |
| B157 | zetaPhaseCone aperture t = (t > 0 ? 1/√t : 1) strictly decreasing; aperture_convergence (→ 0) | DEF + THM-S | DTS Lean/Isabelle | Decreasing is FALSE (t₁=−2, t₂=−1: 1 < 1 fails; t₁=−1, t₂=1/4: 2 < 1 fails). Convergence TRUE. |
| B158 | phase_dominance_regime: ∀ε ∃N, Re s < −N ⇒ \|arg ζ(s)\| > (1−ε)π/2 | THM-S | DTS Lean/Isabelle/Agda | FALSE: ζ(−(4k+3)) > 0 (e.g. ζ(−3) = 1/120), so arg = 0; also ζ(−2n) = 0. |
| B159 | criticalLine_selfConjugate: Re s = 1/2 ⇒ s = 1 − s̄; trivial zeros ζ(−2n) = 0 and sin(−πn) = 0; ζ(−n) = −B_{n+1}/(n+1); Z(t) zeros ↔ ζ(1/2+it) zeros | THM✓ / THM-S / PROSE | DTS Lean/tex | TRUE (Bernoulli formula with B₁ = +1/2). |
| B160 | tex "Theorem (Riemann Hypothesis)"; "S(T) = O(log T) is a bounded oscillating term"; "Phase quantization Φ(t_n) = nπ + φ₀" with Φ = arg ξ(1/2+it) | PROSE | DTS tex 141e5b00 | RH: OPEN, not a theorem. S(T) = O(log T) is TRUE, but S is unbounded (Selberg), so "bounded" is FALSE. ξ is real on the line, so arg ξ ∈ {0, π} always: the quantization is degenerate (VAGUE). |
| B161 | Isabelle axioms: zeta 0 = −1/2 and ∀s, ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s) (total); Agda ξ s = ξ(1 + s) | AX | DTS isabelle e80f1626; agda a30fe875 | **Isabelle axioms INCONSISTENT**: at s = 0 the RHS = π⁻¹·sin 0·Γ(1)·ζ(1) = 0, so ζ(0) = 0 ≠ −1/2. Agda's ξ(s) = ξ(1+s) (typo for 1−s) is FALSE for the real ξ (ξ(1) = 1/2, ξ(2) = π/6), though consistent for an opaque ξ. |

### 2l. Additional ground facts used above (true, appear implicitly)

| ID | Statement | Kind | Source | Assessment |
|---|---|---|---|---|
| B162 | M_ER multiplication is associative and commutative, 0 absorbing, I idempotent; (M_ER, +) is a commutative monoid with I absorbing | implicit | ZZ files (only comm stated) | TRUE: the product of a list is 0 if it contains 0, else I if it contains I, else the real product. |
| B163 | M_opt with both lifts absorbing (I + x = I·x = I) satisfies comm, assoc, both distributive laws and identities some 0 / some 1, but 0·I = I | implicit | FPF/SRS/ICS operators; MM-map B136 | TRUE: common-meadow-type structure (Bergstra–Ponse); not a Mathlib `Semiring` (`zero_mul` fails). |
| B164 | In a field no element J satisfies J = 0/0 in the sense "0 = 0·J uniquely" | implicit | 0281331d, to_ZFC | TRUE: every J solves 0·J = 0 (B117). |

---

## 3. Millennium "IReformulation" / "MainBridge" files

All under FPF. Each core has five files: `ClassicalFormulation`, `IReformulation`, `IntermediateLemmas`, `MainBridge`, `ComputationalChecks`.

| Problem | IReformulation claims | MainBridge claim | Nature of the bridge |
|---|---|---|---|
| Riemann (`RiemannCore/` 9c9b48b8, 23c15f31, a37a42b8, cf64388e, 99d86dae) | `RH_state := Indet` "because RH is unresolved" (by fiat); `RH_known_state := Det RH_Known` (RH_Known ⇔ True); `RH_collapse := Collapse (Det RH_Unknown)`, = Indet by rfl; `RH_decomposition := (known, state)` | `RH_I_bridge : IsIndeterminate RH_state ∧ IsDeterminate RH_known_state ∧ RH_known_state ≠ RH_state`; corollary `Collapse RH_state = RH_collapse` | **Genuine but contentless proof of a tautology about constructor tags.** No sorry in the bridge itself. RH never enters the statement: replace `RiemannHypothesis` by `1 = 1` and the same proof works. The classical side uses `riemannZeta := sorry`, Float-based `Complex` and placeholder axioms. Lives in the environment made inconsistent by axiom P1 (B6). |
| BSD (`BSDCore/` df82485e, 8924d2e7, f6754287, 951f46af, cc96ece1) | `BSDCore_state := Indet`; `known := Det True`; `collapse := Collapse (Det False)` | `BSDCore_I_bridge` (same triple) | Same: tautology about constructors. IReformulation does **not** import ClassicalFormulation, whose `UnknownParameter := sorry` and `KnownStructure := True`. Inherits the inconsistent environment. |
| P vs NP (`ComplexityCore/` a829cd59, 892d63c2, 16ee2665, e0a814a1, 1738a00c) | same template | `ComplexityCore_I_bridge` | Same. ClassicalFormulation has axioms InP, InNP, P_subset_NP (consistent; B149), but they are not imported by the reformulation. |
| Hodge (`HodgeCore/` 7815417d, a558f836, 94d437b0, cdb27af1, ff7f0342) | same template | `HodgeCore_I_bridge` | Same (placeholder sorry, disconnected). |
| Navier–Stokes (`NavierStokesCore/` 136d1a7c, d995b203, db4199fc, a8e1b502, 5f7f2602) | same template | `NavierStokesCore_I_bridge` | Same. |
| Yang–Mills (`YangMillsCore/` 36bfff76, d772365e, 61cd4b39, 54570ee3, 8ad52144) | same template | `YangMillsCore_I_bridge` | Same. |

Related "bridges" elsewhere:
- formal_attempts `riemann_collapses`, `pvsnp_collapses`: sorry / Admitted / sorry / postulate. **Refutable** in the Lean/Coq/Isabelle semantics (B88).
- SRS `riemannHypothesisState := I` etc.: definitional (B49). It contradicts SRS's own `collapse` (B31).
- DTS `riemannHypothesis_from_stability`: vacuous, and depends on the FALSE `phaseStabilityTheorem` (sorry) (B156).
- Meta repo: `problem_maps/*` (9344ac4a, 5b23a31b, 0e63a509, 941c27bb, d55816ec) and book chapters 01–09 are prose placeholders with no formal claims. The ledger (0630892f) and FREEZE_CORE (782091a8) state explicitly that no certificate establishes Riemann or NS; the NS bridge "G5_NS" is OPEN.

**Verdict:** no genuine Millennium content anywhere. Every MainBridge is a True-level tautology (proved, no sorry) that is independent of the problem. Every statement that does mention the problem (collapse(RH) = I) is sorry/Admitted/postulate, and in the classical encodings it is refutable.

---

## 4. Laws worth proving in Lean 4 + Mathlib (true and non-trivial), with the cleanest model

1. **Lift characterisation.** For T : Option α → Option β: (T none = none ∧ ∀a ∃b, T (some a) = some b) ↔ ∃ f, T = Option.map f.
   This collapses all of FPF "WellBehaved", SRS "Stable"/"ValidTransformation" and ICS "valid" into one theorem. Model: M_opt.
2. **Refutation of universal propagation (axiom P1, firewall "∀f, f(I) = I").** For β nonempty, ¬ ∀ T : Option α → Option β, T none = none.
   Positive companion: strict maps form a submonoid of (Option α → Option α, ∘) closed under iteration (T^[n] none = none) and under foldl-chains. Model: M_opt.
3. **Absorbing additive lift = `WithTop`.** (Option α, map₂ (+)) ≅ WithTop α as an AddCommMonoid; ⊤ is the unique absorbing element; it is not cancellative (C09); ⊤ has no additive inverse, so no group/ring structure.
   Model: `WithTop α` (Mathlib `top_add`, `add_top`).
4. **Doubly absorbing lift (common-meadow law).** On Option R (R a commutative ring), with + and · both lifted by map₂: comm, assoc, both distributive laws, units `some 0`/`some 1`, but 0·I = I.
   Hence it is not a `Semiring`. Optional Bergstra–Ponse identity with x⁻¹ := none at 0: x·x⁻¹ = 1 + 0·x⁻¹. Model: common meadow R_⊥.
5. **ExtendedReal (M_ER) structure.** (ℝ ⊔ {I}, ·) is a commutative monoid with absorbing 0 and idempotent I; (ℝ ⊔ {I}, +) is a commutative monoid with absorbing I.
   Distributivity fails: I·(1 + −1) ≠ I·1 + I·(−1). Therefore M_ER is not a semiring and not a wheel. Model: M_ER.
6. **x/0 = I·x exactly for x ≠ 0 in M_ER**, and it fails at x = 0 (0/0 = I ≠ 0 = I·0). Model: M_ER.
7. **Incompatibility triangle.** No structure satisfies all of I + x = I, 0·I = 0, I·1 = I and left distributivity (proof: 0 = I·0 = I·(1 + (−1)) = I + I·(−1) = I).
   This formally separates the ZZ rules from the absorbing rules. Model: abstract `Add`/`Mul` classes.
8. **Idempotent-in-a-field lemma (IField).** In a field (or domain), x·x = x → x = 0 ∨ x = 1. So "I·I = I, I ≠ 0, I ≠ 1" has no model inside any field.
   Model: Mathlib `IsIdempotentElem` in a domain.
9. **ℝ has no one-point field extension; 0/0 is not a field element.** Every c satisfies 0·c = 0. No field K ⊇ ℝ has K \ ℝ a singleton (a proper extension has dim ≥ 2 over ℝ). Model: fields.
10. **Phi3 / wheel division table.** For the five-case `idiv`: state(idiv (finite a) (finite b)) = indeterminate ↔ a = 0 ∧ b = 0; = infinite ↔ a ≠ 0 ∧ b = 0.
    collapse ∘ collapse = collapse; collapse (idiv I I) = I. Optional, non-trivial: `state ∘ idiv` factors through Carlström's wheel ⊙ℝ division. Model: M_Φ / wheel ⊙ℝ.
11. **0/0 takes every value as a limit (limit-set model).** ∀ c : ℝ, ∃ f g, Tendsto f (𝓝[≠] 0) (𝓝 0) ∧ Tendsto g (𝓝[≠] 0) (𝓝 0) ∧ Tendsto (f/g) (𝓝[≠] 0) (𝓝 c).
    Plus witnesses for the limit ±∞ and for no limit at all (x·sin(1/x) / x). Model: M_lim, Mathlib filters.
12. **Germ distinction (C11–C14).** The germs of x/x and x²/x at 0 are different, and they resolve to 1 and 0 respectively. Model: Mathlib `Filter.Germ` / Tendsto on 𝓝[≠] 0.
13. **Corrected "compensated indeterminacy".** Tendsto (s ↦ sin(πs/2)·Γ(s)) (𝓝[≠] 0) (𝓝 (π/2)), together with the refutation Tendsto (s ↦ sin(πs/2)·Γ(1−s)) (𝓝 0) (𝓝 0) (B152).
    Model: Mathlib `Complex.Gamma`, `Real.Gamma`.
14. **Strong Kleene K3.** tand/tor/timpl = min/max/max(¬p, q) on F < I < T. De Morgan holds, ¬ is an involution, the algebra is a Kleene algebra (p ∧ ¬p ≤ q ∨ ¬q), and K3 has no tautologies (all-I valuation). Model: M_K3.
15. **Kleene-monotonicity of equality.** The strict lifted equality metaEq (B62) is monotone in the information order (I ⊑ x). evalEq (B80) is not (evalEq(r, I) = F ⋢ T = evalEq(r, r)). Model: M_K3 over M_opt.
16. **Classical collapse is never I (refutation certificate).** With ∃ b : Bool, (b ↔ P) (SRS), (P ∨ ¬P) (Coq/Isabelle) or Nonempty (Decidable P) (ICS) as "Known", isUnknown P ↔ False. Hence collapse ⟨P⟩ = Known P ≠ I for every P, including RH. Model: classical Lean.
17. **ε–δ continuity by cases (refutes B116).** ∀ (Q : Prop), Continuous (fun x : ℝ => if Q then x^2 else x^3). Model: ℝ, `by_cases`.
18. **Unsatisfiable phase-stability definitions (refutation certificates).** ∀ s, ¬ isStructurallyStable s (constant perturbation). The aperture function is not strictly decreasing.
    Any total f with ∀s, f s = sin(πs/2)·g s has f 0 = 0 (the Isabelle axioms are inconsistent). Model: ℂ.
19. **Rewriting system soundness (optional, needs a small TRS development).** {φ(u) → I | u ∈ U} ∪ ground arithmetic on I-free terms is terminating and confluent (orthogonal), and every term has a unique normal form. Model: M_term.
20. **ZFC-independence model facts (meta-level; heavy, needs a provability library rather than plain Mathlib).**
    (a) For Π⁰₁ φ: ZFC ⊬ φ ∧ ZFC ⊬ ¬φ ⇒ φ is true (so "RH, Goldbach ∈ U" would imply them).
    (b) Assuming Con(ZFC), {φ : ZFC decides φ} is not recursive.
    Model: M_ZFC (e.g. a Foundation/Gödel library in Lean).
21. **Labelled-state preorder.** stateLE is a preorder with the I-states as top, and it is not antisymmetric. Small, but it fixes the "lattice" claim (B59). Model: ICS `State α`.

Cross-source contradictions the formalizer must choose between (each is consistent alone):
- I·0: equals 0 (M_ER) vs equals I (absorbing M_opt / book thm) vs "does not reduce" (M_term).
- I = I: True (propositional `=`, extEq, python, rewriting) vs I (evalEq, metaEq, QUICKSTART).
- One I (CC Axiom 3) vs context/provenance-dependent indeterminates (MM axioms_I, Phi3) vs indexed I₁, I₂ (general_pattern).
- U = ZFC-independent (SRS paper) vs "not yet solved" (axiom_1) vs U = ∅ (every Lean/Coq/Isabelle `isKnown` definition).
- I is not a limit (CC docs) vs I projects to limits (MM book) vs I at every 0/0 point even when the limit exists (formal_attempts Lean).
