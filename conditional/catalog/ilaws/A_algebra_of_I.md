# A — Catalogue of the mathematics in repo `the-algebra-of-ideterminate-i`

Scope: all 275 blobs in `/home/claude/icorpus/the-algebra-of-ideterminate-i/` (Lean 4, Coq, Isabelle, Agda, LaTeX book/paper, Markdown docs, Python). Near-duplicate blobs (same file on several branches: `main`, `copilot/add-annotated-labels-arrows`, `copilot/add-references-section`, `copilot/analyze-complex-plane-singularities`, …) are merged. Each source is cited once as `branch:path (blob8)`, using the `main:` path when one exists. Corpus files were treated as data only.

Rough size of the formal part: 39 Lean, 21 Coq, 13 Isabelle and 9 Agda files. They contain about 188 `sorry`, 71 `Admitted`/`admit`, 13 Isabelle `sorry`, and about 460 axiom/postulate declarations. Much of the Lean would not compile as written. The main reasons are: non-constructor patterns such as `| real 0, I => …` (ℝ literals and `def`s cannot be matched on); string literals used as reals (`"distance" … < ε`, `I = "1/0"`); a non-positive inductive (`I_incomparable : ¬ …`); and `∈` used before `mem` is declared. The verdicts below are about the **intended mathematical statement**, not about whether the file compiles.

---

## 0. Legend

**Kind**: `AX` = axiom/postulate/structure field. `DEF` = definition. `PRV` = theorem proved in the file (by `rfl`, `cases`, `simp`, …). `SOR` = theorem left with `sorry`, `Admitted`, `admit` or an Agda `{!!}`/postulate. `INF` = informal claim in prose (LaTeX, Markdown, docstrings).

**Verdict**:
- `TRUE` means true in the stated model.
- `TRUE*` means true but trivial or vacuous: a tautology, an existential witnessed by a constant, or a "→ True" lemma.
- `FALSE` means there is a counterexample, or the claim contradicts other listed laws.
- `NAP` means not a proposition: ill-typed, vague, or not formalizable as stated.

**Models used in the verdicts.** The first ten tags (CARD through PAX) are models built in the corpus. The remaining tags (SET through ULTRA) are standard models brought in for comparison.

| Tag | Model (definition) | Where |
|---|---|---|
| **CARD** | `ℕ ∪ {I}`. `⊕`,`⊗` are ℕ-operations with `I` absorbing (also `0⊗I = I`). `n⊖n = I`; `n⊖m = n∸m` (truncated) for `n≠m`; `⊖` with `I` gives `I`. | lean/Indeterminate.lean |
| **KIJ** | `ℝ ∪ {I,J}`. `⊕`: `I` dominates, then `J`, else real `+`. `⊗`: `0⊗I = 0⊗J = 0`, `r⊗I = I`, `r⊗J = J` (r≠0), `I⊗J = I`, `I⊗I = I`, `J⊗J = J`. `⊖`: like `⊕` but `J⊖J = I`. `⊘`: `r⊘0 = I`, `r⊘I = r⊘J = 0`, `I⊘x = I`, `J⊘r = J` (r≠0), `J⊘0 = I`. | lean/IAlgebra.lean & clones |
| **WT** | The `{I}`-only fragment of KIJ, i.e. `ℝ ∪ {⊤}` with `⊤+x = ⊤`, `a·⊤ = ⊤` (a≠0), `0·⊤ = 0`. These operations coincide with Mathlib's `WithTop ℝ` `+` and its `MulZeroClass` multiplication. | — |
| **ABS** | "Common meadow" `ℚ⊥`/`ℝ⊥` = `Option ℝ` with `I = none` absorbing for `+` and `·` (so `0·I = I`), `x/0 = I`, `I/x = x/I = I`. | lean/consistency_proofs.lean, NexusField concrete model |
| **AEI** | `K ∪ {I}` (K a field). `+`: `I` absorbing. `·`: `a·I = I` (a≠0), `0·I = I·0 = 1`, `I·I = I`. `/`: `a/0 = I`, `0/a = I`, `I/x = x/I = I`. `I−I = I`. `I^n = I` (incl. n=0). | formalizations/lean/AlgebraIndeterminate/AEI.lean |
| **ZDIV** | `ℝ ∪ {I,J}`. `r⊕s = I` if `r+s=0`; `r⊗s = I` if `rs=0`; `r⊖s = I` if `r=s`; `r⊘s = I` if `s=0`; `I` absorbing; `J⊗J = 0`. | formalizations/lean/IAlgebra.lean |
| **IEA** | `ℝ ∪ ℂ ∪ {I, J, +∞, −∞, iI, −iI}` with the pattern tables of lean/IEA.lean (`0·I = 0`). | lean/IEA.lean |
| **FLEX** | `K_I = {a+bI} ≅ K²`. Componentwise `+`. `(a+bI)(c+dI) = ac+(ad+bc)I+bd·Ω(I)`; with `Ω(I)=I` this is the ring `K[I]/(I²−I) ≅ K×K`. | FlexibleResolution.lean |
| **MS** | Multistate: a value is a nonempty finset of states `{0,1,I,∞,?}`, plus a context-based `resolve`. | MultiStateI.lean |
| **PAX** | Abstract P1–P15: abelian group under `+`, monoid under `·`, distributivity, `x·0 = 0`, `I≠0,1`, `I²=I`, `I+I=I`, `¬∃x, I·x=1`. | lean/AlgebraI/Basic.lean |
| **SET** | Standard model I add: `I := Set.univ ⊆ ℝ` ("all possible values") with Mathlib pointwise operations on `Set ℝ`. Here `{x}+I = I`, `{x}·I = I` (x≠0), `{0}·I = {0}`, `I+I = I·I = I−I = I`, `0 ∈ I−I`, `1 ∈ I/I`. Only sub-distributive. | — |
| **LIM** | Standard: the value of an indeterminate form is the set of cluster points in `EReal` of `f_n/g_n` with `f_n, g_n → 0` (likewise for `∞−∞` etc.). | — |
| **WHEEL** | Carlström's wheel `⊙ℝ`: `1/0 = ∞`, `0/0 = ⊥`, `∞ ≠ ⊥`, `0·∞ = ⊥`, `⊥` absorbing. | — |
| **MEADOW** | `ℝ` with Mathlib's total division `x/0 = 0`. Consistent and nontrivial. | — |
| **RING** | `ℝ×ℝ` (≅ `ℝ[X]/(X²−X)`) with `I = (1,0)`. | — |
| **K3/LP** | Kleene and Priest 3-valued logics on `{T, I, F}`. Designated values are `{T}` in K3 and `{T, I}` in LP. | — |
| **ULTRA** | `ℝ^ℕ/U` with U a non-principal ultrafilter (Mathlib `Hyperreal`, `hyperfilter`). | — |

---

## 1. Carriers / definitions of I used in the corpus

The corpus has **no single definition of I**. There are at least nine mutually incompatible carriers:

1. **Extended cardinals, `ℕ ∪ {I}` (CARD)** with axiom I1 `κ⊖κ = I`. Sources: `main:lean/Indeterminate.lean (f0fd5a84)`, `main:coq/Indeterminate.v (fda5f348)`, `main:isabelle/Indeterminate.thy (643d7cb2)`. Abstract versions use `axiom Cardinal : Type` and `axiom I : Cardinal`: `main:formalizations/lean/AlgebraIndeterminate/Cardinals.lean (f3cf1b08)`, with Coq `566cd6a0`, Agda `73e64669`, Isabelle `8350085d`. Prose versions add I as a ZF urelement: `main:book/parts/part1/chapter02_axiom_I1.tex (4b018696)`, `main:latex/main.tex (26be2b27)`.
2. **`K_I = ℝ ∪ {I, J}` (KIJ)**: `inductive ExtendedReal | real : ℝ → _ | indet : {I,J} → _` with "15 postulates", `0⊗I = 0`, `r⊘0 = I`. Sources: `main:lean/IAlgebra.lean (f0e174df)`, `main:coq/IAlgebra.v (c184284c)`, `main:isabelle/IAlgebra.thy (a8616618)`, `main:agda/IAlgebra.agda (befe5e0c)`. Wheel clones: `main:lean/WheelOfFractions.lean (ec0987c9)`, Coq `3fa18784`, Isabelle `0404c9aa`, Agda `c126a51c`. Docs: `main:docs/MATHEMATICAL_FRAMEWORK.md (7b3ff63d)`, `main:BOTTLENECK_CONSTANT_SPECIFICATION.md (7a5d95da)`.
3. **Abstract "ring with an idempotent absorbing I" (PAX, P1–P15)**: `main:lean/AlgebraI/Basic.lean (c641179f)`, `main:coq/theories/Basic.v (9137d111)`, `main:docs/theory/axioms/core_postulates.md (43901456)`. This axiom set is **inconsistent** (see A62).
4. **Fully absorbing `Option`-type (ABS)**. Sources: `ModelElement := standard ℚ | indeterminate` in `main:lean/consistency_proofs.lean (2f1c53a0)`; `ConcreteNexusModel := Option ℝ` in `main:lean/NexusField.lean (be4be255)` and `main:lean/NexusFieldExamples.lean (43ca57a3)`; `structure Indeterminate (val : ℚ) (is_indeterminate : Bool)` in `main:lean/nexus_core.lean (4ea207db)`; `IComplex := ℂ ⊕ I` in `main:formalizations/lean/ITheory.lean (ce16cd1e)`. The Isabelle/Agda `CentralHypothesis` uses `Real r | Indeterminate` with `0⊗I = I` (`d947976c`, `d18e45ef`). The Lean `CentralHypothesis` uses `{v : Option ℝ // v = none}`, which has a single element (`ed29a88f`).
5. **Abstract `structure NexusField`** with axioms N1–N15, where I is defined by `0·inv 0 = I` (`be4be255`).
6. **AEI, "I = 1/0"**: `inductive KI (K) [Field K] | fromField | indeterminate` with `0·I = 1`. Sources: `main:formalizations/lean/AlgebraIndeterminate/AEI.lean (242da20d)`, ExtendedOperators `ba30ccd4`, Transitions `fa9b2687`, Examples `ecb9356b`; Coq `b219e6d2`/`04bf6527`/`6b1ee806`/`257afeeb`; Isabelle `087ff063`.
7. **IEA** with singularities {I, J=iI, ±∞, ±iI}: `copilot/analyze-complex-plane-singularities:lean/IEA.lean (503a118a)`, Coq `2407c988`, Isabelle `6ad50054`.
8. **ZDIV** ("I-structures", J = 1/I), where a zero sum or zero product becomes I: `main:formalizations/lean/IAlgebra.lean (258c41ea)`, Coq `ac245181`, Isabelle `f212d681`, Agda `e0a6d060`, Python `f09c6359`.
9. **FLEX `K_I = {a+bI}`** with corrective `Ω(I)`: `main:formalizations/lean/AlgebraIndeterminate/FlexibleResolution.lean (40a5384e)`, Coq `1dbec880`, Isabelle `7d9c4d78`, Agda `31f71680`.

There are also several minor carriers:
- ExtendedOperations `ℝ ∪ {I, J, 0_I, I_0}` (`copilot/add-annotated-labels-arrows:formalizations/lean/AlgebraIndeterminate/ExtendedOperationsI.lean (90970f1a)`).
- Multistate finsets (`5493bb58`, Coq `f1b69b3a`, Isabelle `a0e38ac6`).
- Wheel pairs `ℝ×ℝ` (`main:lean/WheelTheory.lean (c681d5cd)`).
- The hardware `ExtendedReal = Finite f64 | ±∞ | I | J` (`main:book/parts/part6/chapter33_extended_real_type.tex (55417d03)`).
- `HyperKI`, `ExtendedComplex (a+bI)`, `IValued (Σ aₙIⁿ)` (declared only, `ba30ccd4`).
- The extended ultrapower `ℝ^ℕ/U ∪ {I}` (`main:book/parts/part2/chapter17_ultrapowers_with_I.tex (6b1ad6b2)`).
- The 3-valued logic `{T, F, I}` (`main:book/parts/part1/chapter01_preliminary_logic.tex (fb45f2e2)`).
- In several files `I` is a **type** (`axiom I : Type`), not an element (AEI.lean, ITheory, FlexibleResolution). This is a category error.

The key conflicts between carriers are the value of `0·I`, `I−I` and `I^0`:
- `0·I = 0` in KIJ, WT, IEA and PAX; `0·I = I` in CARD, ABS, NexusField and Isabelle/Agda CentralHypothesis; `0·I = 1` in AEI; `0·I = 0_I` in ExtendedOperations.
- `I−I = I` in KIJ, ABS, AEI and ZDIV; `I−I = 0` in PAX and Python `src`; `I−I ∈ {0, I, ?}` in MS.
- `I^0 = 1` in ExtendedOperations; `I^0 = I` in AEI.

---

## 2. Deduplicated table of all axioms, laws, rules and theorems

### 2.1 Cardinal-subtraction system (axioms I1–I7)

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A1 | **I1**: `∀κ, κ⊖κ = I` (one I for all κ, finite κ included) | AX (book, latex, Cardinals.lean/v/agda/thy); PRV in CARD | `main:book/…/chapter02_axiom_I1.tex (4b018696)`; `main:latex/main.tex (26be2b27)`; `main:formalizations/lean/AlgebraIndeterminate/Cardinals.lean (f3cf1b08)`; `main:lean/Indeterminate.lean (f0fd5a84)` | TRUE in CARD, by definition (it overrides `n−n = 0`). FALSE as a statement about real cardinal subtraction: in SET, `n−n = {0}`, `ℵ₀−ℵ₀ = [0,ℵ₀]`, `ℵ₁−ℵ₁ = [0,ℵ₁]`, so there is no single I. Consistent as an axiom about a fresh symbol. |
| A2 | Extended subtraction: `κ⊖λ = μ` if `κ = λ+μ`; `= I` if `κ = λ`; undefined if `κ<λ` | DEF | `4b018696` | NAP (not a function): `ℵ₀ = ℵ₀+5` gives `ℵ₀⊖ℵ₀ = 5` and also `= I`; for infinite κ the μ in `κ = λ+μ` is not unique. |
| A3 | **I2** (limited neutrality): `κ⊖λ = f(κ,λ)`, `λ⊖κ = g(κ,λ)`, with `f(κ,κ) = g(κ,κ) = I` | AX | Cardinals.lean `f3cf1b08` (+Coq `566cd6a0`, Agda `73e64669`) | TRUE* (vacuous: take `f := ⊖`, `g := flip ⊖`). The README version ("continuity at the diagonal", `843f5a7d`) is NAP: there is no topology on Card. |
| A4 | **I3a**: `(κ⊕λ)⊖(κ⊖λ) = I` for all κ, λ | AX; docs call it "Theorem 5.1 (proved)" | `f3cf1b08`, `26be2b27`, `566cd6a0`, `73e64669` | FALSE in CARD: κ=0, λ=1 gives `1⊖0 = 1`; κ=5, λ=2 gives `7⊖3 = 4`. Only satisfiable in degenerate models with `⊖ ≡ I`. |
| A5 | **I3b**: `(κ⊖λ)⊕(λ⊖κ) = I` | AX | same | FALSE in CARD: κ=2, λ=1 gives `1⊕0 = 1`. |
| A6 | **I4** absorption: `I⊕κ = I` and `I⊗κ = I` for all κ (κ = 0 included) | AX; PRV in CARD | `26be2b27`, `f0fd5a84` (+Coq `fda5f348`, Isabelle `643d7cb2`) | TRUE in CARD and ABS. Contradicts the `0⊗I = 0` postulate of KIJ, PAX and IEA (A30). |
| A7 | **I5**: `I⊖I = I`, `I⊕I = I` | AX; PRV | same | TRUE in CARD, ABS and SET (it follows from A1 with κ=I, and from A6). |
| A8 | **I7**: `I ≠ 0`; I7 is independent of I1–I6 | AX + INF | `main:book/…/chapter08_axiom_I7.tex (270d3fe4)` | TRUE. Independence is also TRUE: the one-point model satisfies I1–I6. |
| A9 | Uniqueness (Thm 3.1): `(∀κ, κ⊖κ = I₁) → (∀κ, κ⊖κ = I₂) → I₁ = I₂` | PRV (CARD); SOR (`I_unique`, Cardinals.lean) | `f0fd5a84`, `f3cf1b08` | TRUE* (instantiate any κ). |
| A10 | Every map preserving `⊖` (and `⊕`, `⊗`) fixes I | PRV | `f0fd5a84`, `fda5f348`, `643d7cb2`; `main:docs/MATHEMATICAL_GUIDE.md (6ea4e339)` | TRUE whenever `∀x, x⊖x = I`: `φI = φ(I⊖I) = φI⊖φI = I`. |
| A11 | Non-triviality: `I ≠ κ` for every cardinal κ | PRV (CARD); INF (latex) | `26be2b27`, `f0fd5a84` | TRUE. In CARD by constructors; also from I4 with real cardinal `+` (if `I = κ₀` then `κ₀+κ₀⁺ = κ₀⁺ ≠ κ₀`). The latex proof ("non-functional") is invalid. |
| A12 | Algebraic compatibility: `(κ⊕λ)⊖(κ⊕λ) = I` | PRV | `26be2b27`, `f0fd5a84` | TRUE* (an instance of I1). |
| A13 | `⊕`, `⊗` commutative and associative; `0⊕n = n`; `1⊗n = n`; closure | PRV | `f0fd5a84`, `fda5f348`, `643d7cb2` | TRUE in CARD. |
| A14 | `I ∈ xs → Σxs = I` and `Πxs = I` | PRV | `f0fd5a84` | TRUE in CARD and ABS. |
| A15 | `λ = μ → κ⊗(λ⊖μ) = (κ⊗λ)⊖(κ⊗μ)` | PRV | `f0fd5a84`, `fda5f348` | TRUE in CARD (both sides are I). |
| A16 | `κ⊗(λ⊖μ) = (κ⊗λ)⊖(κ⊗μ)` whenever the right side is defined | INF | `26be2b27` (appendix) | FALSE in CARD: κ=0, λ=2, μ=1 gives `0⊗1 = 0` but `0⊖0 = I`. |
| A17 | `κ ~ λ :⇔ κ⊖λ = I` is an equivalence and `Card/~` has well-defined operations | INF | `26be2b27`, `6ea4e339` | On Card alone ~ is equality: TRUE* (the quotient is Card itself). On `Card ∪ {I}`: FALSE (`1~I`, `I~2`, but not `1~2`). |
| A18 | Closure lemma: `z⊖y = (z⊖x)⊕(x⊖y)` | INF | `26be2b27` | FALSE in CARD: z=x=5, y=1 gives `I⊕4 = I ≠ 4`. |
| A19 | Triviality collapse: `I = 0` together with I4 and `0⊕x = x` forces all elements equal | INF (proof) | `fb45f2e2`, `270d3fe4` | TRUE: `x = 0⊕x = I⊕x = I`. In any monoid, an absorbing identity forces triviality. |
| A20 | "If `I = 1` a different trivialisation occurs" | INF (exercise) | `fb45f2e2`, `270d3fe4` | TRUE when `·` is totally absorbing (`x = 1·x = I·x = I`), or when ℝ embeds with I additively absorbing (`0 = 1+(−1) = I+(−1) = I = 1`). |
| A21 | `(Card ∪ {I}, ⊕, ⊗, 0, 1)` is a non-trivial ring | INF | `270d3fe4` | FALSE: there are no additive inverses (`I⊕x = I ≠ 0`; also `1⊕x ≠ 0` in Card). |
| A22 | `κ≠0 → I⊕κ ≠ 0` and `I⊗κ ≠ 0` | INF | `270d3fe4` | TRUE (CARD). |
| A23 | Every model of I1–I7 is infinite | INF (exercise) | `270d3fe4` | FALSE: `{0, I}` with `x⊖y := I` and `⊕`, `⊗` = "I unless both are 0" satisfies I1–I5 and I7. |
| A24 | Defining `κ⊖κ = κ` (instead of I) leads to contradiction or triviality | INF (exercise) | `4b018696` | FALSE: `⊖ := first projection` is consistent and non-trivial. |
| A25 | I1 is independent of ZF+AC (models where it holds and where it fails, forcing); ZF+AC+I1 is equiconsistent with ZF+AC; `independence_from_zf`, `zf_consistency_with_I`, `relative_consistency` | INF + SOR | `4b018696`; `main:lean/theory_independence.lean (8a1fbd6e)`; `main:formalizations/lean/AlgebraIndeterminate/Consistency.lean (289f4c7c)` | Relative consistency: TRUE* (I1 talks about fresh symbols, so the extension is conservative). "Independent like CH": NAP (I1 is not a statement of ZF's language). The Lean `independence_from_zf` contains the conjunct `(∃i, i = I) ∧ ¬(∃i, i = I)`, so it is FALSE. `arithmetic_preservation` (`std(a+b) = std a → False`) is FALSE at b=0. |
| A26 | Compactness holds for ZF+AC+I1–I5 | INF | `26be2b27` | TRUE (first-order compactness). |
| A27 | "Structural uniqueness": every extension of cardinal arithmetic with closure, non-triviality and consistency is isomorphic to the I-system | INF | `main:book/…/chapter37_ontology.tex (2fe91255)` | FALSE: CARD with `0⊗I = I` and CARD with `0⊗I = 0` both satisfy I1, I4(⊕), I5 and I7 and are not isomorphic; the corpus itself contains at least five non-isomorphic models. |
| A28 | (implicit "unique I") An absorbing element for `⊕` is unique | — | — | TRUE in any magma: `I = I⊕I' = I'`. |

### 2.2 `K_I = ℝ ∪ {I, J}`: postulates 1–15 and their theorems (KIJ)

Sources for this subsection: `main:lean/IAlgebra.lean (f0e174df)`, `main:coq/IAlgebra.v (c184284c)`, `main:isabelle/IAlgebra.thy (a8616618)`, `main:agda/IAlgebra.agda (befe5e0c)`, `main:docs/MATHEMATICAL_FRAMEWORK.md (7b3ff63d)`; the field-axiom files `main:lean/FieldAxiomVerification.lean (819fcccb)` and `main:coq/FieldAxiomVerification.v (d4d0c4d4)`; and `main:lean/ExtendedAnalysis.lean (929f0b8c)` / `main:coq/ExtendedAnalysis.v (1ce08858)`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A29 | Operation tables `⊕ ⊖ ⊗ ⊘` of KIJ (see legend) | DEF | f0e174df, c184284c, a8616618, befe5e0c | Definition. As written in Lean (non-constructor patterns) it does not compile; the semantics are clear. |
| A30 | **P4** `0⊗I = 0` (also `0⊗J = 0`; in WheelOfFractions this is the axiom `zero_times_I_undefined`) | AX (and DEF) | f0e174df, ec0987c9, 7b3ff63d, `7a5d95da` | TRUE in KIJ, WT and SET (`{0}·ℝ = {0}`). Contradicts A6 (I4), A84 (NexusField forces `0·I = I`), CentralHypothesis `0⊗I = I` (`d947976c`), and AEI `0·I = 1`. |
| A31 | **P1** `∃i, i = I`; **P2** `∀r∈ℝ, I ≠ r`; **P8** `∃j, j = J ∧ j ≠ I`; **P9** closure | AX | f0e174df, c184284c, a8616618, befe5e0c | TRUE* (constructor facts; provable, so need not be axioms). |
| A32 | **P3** `I⊕I = I ∧ I⊗I = I` | AX | same | TRUE (KIJ, ABS, SET). |
| A33 | **P5** `∀r, r⊘0 = I` (`0⊘0` included) | AX | same | TRUE in KIJ by definition. In LIM only `0/0` is "I-like": for r≠0 the cluster set of `r/g_n` is `{−∞,+∞}`. In WHEEL `1/0 = ∞ ≠ ⊥ = 0/0`. |
| A34 | **P6** `I⊘I = I`; **P7** `I⊖I = I` | AX | same | TRUE in KIJ, ABS and SET (`ℝ/ℝ* = ℝ`, `ℝ−ℝ = ℝ`). P7 contradicts PAX `I−I = 0` (A68) and the Python `src` rule `I−I = 0` (A190). |
| A35 | **P10–P14**: on reals `⊕ = +`, `⊗ = ·`, associativity, commutativity, `r⊕0 = r`, `r⊗1 = r` | AX | same | TRUE (inherited from ℝ). |
| A36 | **P15** `I≠0 ∧ I≠1` | AX | same | TRUE. |
| A37 | `assoc_add_fails_with_I`: `¬∀abc, (a⊕b)⊕c = a⊕(b⊕c)` | SOR | 819fcccb | FALSE: `⊕` and `⊗` are associative and commutative on all of KIJ (brute-force checked; levels real < J < I, and 0 is absorbing for `⊗`). |
| A38 | `distrib_fails_with_I`: `¬∀abc, a⊗(b⊕c) = a⊗b ⊕ a⊗c` (the file found no witness) | SOR | 819fcccb | TRUE: a=I, b=1, c=−1 gives `I⊗0 = 0` but `I⊕I = I`. The same holds in WT and SET (there only `⊆` holds). |
| A39 | `modified_distributivity`: distributivity holds unless one of a, b, c is I or J | SOR | f0e174df | TRUE (the all-real case). |
| A40 | `no_multiplicative_inverse` / `no_mul_inverse_I`: `¬∃x, I⊗x = 1` | SOR (Lean `f0e174df`; Coq Admitted `c184284c`); PRV (Coq Wheel `3fa18784`, Lean `819fcccb` except the 0 case) | — | TRUE in KIJ and WT (`I⊗x ∈ {I, 0}`). |
| A41 | `no_add_inverse_I`: `¬∃x, I⊕x = 0`; `not_a_ring`; `not_a_division_ring`; `not_a_field` (inverse form) | PRV/SOR | 819fcccb, d4d0c4d4, 929f0b8c, 1ce08858 | TRUE (KIJ). |
| A42 | `FieldAxiomVerification.not_a_field : ¬(∀ axiom ∈ ["field_axiom"], True)` | SOR | 819fcccb | FALSE as formalised: it negates a tautology. |
| A43 | `comm_mul_I : r⊗I = I⊗r`; `comm_add_mixed` | SOR/PRV | 819fcccb, d4d0c4d4 | TRUE. |
| A44 | `wheel_allows_zero_div` / `div_by_zero_is_I` / `singularities_accommodated`: `∀n, n⊘0 = I` | PRV (Coq/Isabelle); SOR (Lean) | c184284c, a8616618, ec0987c9, 3fa18784 | TRUE in KIJ. Agda has it as a postulate (`c126a51c`); there `isZeroReal = {!!}`. |
| A45 | `context_resolution : ∃ctx, resolve_context ctx I ≠ I` | PRV/SOR | f0e174df, c184284c, a8616618 | TRUE* (ctx=0 gives 0). |
| A46 | Vacuous existentials stated as axioms or theorems: `extended_is_ifield`, `j_symmetry_breaking (∃T, T I = J)`, `physical_ifield (∃ψ, ψ I ≠ 0)`, `nonstandard_connection (∃ predicate inf, inf ε → ε⊗I = I)`, `cardinal_connection`, `system_consistency (¬∃a b, a=b ∧ a≠b)`, `extended_algebra_representation`, `augmented_complex_plane (∃repr, repr I = (0,0))`, `extended_is_projective`, `discontinuities_eliminated (∃p:Prop, p)`, category, `I_measure_extension`, `I_manifold_generalization`, `I_variety_extension`, `add/mul_computable` | AX/SOR/PRV | f0e174df, c184284c, a8616618, ec0987c9, 929f0b8c, 1ce08858 | TRUE* (witnessed by a constant, an empty predicate, `True`, a zero measure or an empty type). No content. |
| A47 | `ultrapower_interpretation`: `I = 0⊘0` | AX | f0e174df, c184284c, a8616618 | TRUE* (holds by the definition of `⊘`; the `∃U` is unused). |
| A48 | `J⊕J = J`, `J⊗J = J`, `I⊕J = J⊕I = I`, `I⊗J = J⊗I = I` | SOR (Lean)/PRV (Coq) | 929f0b8c, 1ce08858 | TRUE (KIJ). |
| A49 | `symmetry_break` (swap I and J) is an involution | SOR/PRV | 929f0b8c, 1ce08858 | TRUE. It is not a homomorphism (`I⊕J = I ↦ J`, but `J⊕I` maps to `I`). |
| A50 | `I_unique_indet_fixed`: `x⊕x = x ∧ x⊗x = x ∧ x⊖x = x ∧ x⊘x = x → x = I ∨ x ∈ ℝ` | SOR | 929f0b8c | TRUE, and it can be strengthened to `x = I` (`J⊖J = I`; a real r needs `r−r = r`, i.e. r=0, but `0⊘0 = I`). |
| A51 | Wheel relation on KIJ pairs, `n₁⊗d₂ = n₂⊗d₁`, is transitive (`equiv_trans`, `wheel_equiv_trans`); `equiv_equivalence` | SOR (Lean, Coq admit); AX (Agda postulate) | ec0987c9, 929f0b8c, 3fa18784, 1ce08858, c126a51c | FALSE: `(1,1)~(0,0)~(2,1)` but `(1,1)≁(2,1)`. The Agda postulate makes that file inconsistent. Reflexivity and symmetry: TRUE. |
| A52 | **Postulate 73(a)** `∀x, x⊗I = I` (`absorption_property`) | SOR (Lean); "PRV" (Coq, Isabelle by auto); AX (Agda) | ec0987c9, 3fa18784, 0404c9aa, c126a51c; `main:src/python/ialgebra/wheel.py (7d28aefd)` | FALSE in the same files' model: x=0 gives `0⊗I = 0` (A30). The Agda postulate is inconsistent with the definition. |
| A53 | `neutrality_equivalence` (`n₁/0 ~ n₂/0`; `a/0 = b/0` for a, b ≠ 0); `all_zero_denom_equiv`; `singularities_collapse_to_locus`; `x⊕I = I` (`extended_closure`); `x≠0 → x⊗I = I`; `fundamental_properties_redefined`; `extended_forms_IEA`; `closure_with_I` | SOR/PRV | ec0987c9, 3fa18784, 0404c9aa | TRUE (KIJ). |
| A54 | `reciprocal_identity : 1⊘I = 0` ("1/I = 0 in limit sense") | AX | ec0987c9, 7a5d95da (`r⊘I = 0`) | TRUE* in KIJ (by definition). It differs elsewhere: `1/I = I` in ABS, AEI and ZDIV; `1/⊥ = ⊥` in WHEEL. |
| A55 | `I = 0 → 1 = 0` / `I = 0 → False` / `system_collapse : I = 0 → ∀xy, x = y` (Coq `I_zero_implies_one_zero`; argument "`1/0 = I = 0`, multiply by 0") | PRV (vacuous)/INF | 3fa18784; `main:docs/IMPLEMENTATION_COMPLETE.md (6789b4fe)`; `04835e7c`; `05a620f5` | TRUE* in KIJ (`I ≠ 0` by constructors). The argument is invalid in general: MEADOW (`x/0 = 0`, as in Mathlib) is consistent and non-trivial. Collapse needs additive absorption (A19). |
| A56 | Non-real sequences: `converges_to_I s :⇔ ∀ε>0 ∃N ∀n≥N, s_n = I ∨ (s_n ∈ ℝ ∧ abs s_n < ε)` | DEF | 929f0b8c, 1ce08858, 7b3ff63d | Definition. Note that it makes every null real sequence "converge to I", so limits are not unique (1/n → 0 and 1/n → I). |
| A57 | `const_I_converges` | SOR/PRV | 929f0b8c, 1ce08858 | TRUE. |
| A58 | `I_uncertainty_satisfied` (`I⊗I = I ∨ …`) | PRV | 929f0b8c, 1ce08858 | TRUE*. |
| A59 | `dark_matter_singular : ρ(0) = I` with `ρ(r) = 1/r²` | SOR/PRV | 929f0b8c, 1ce08858 | TRUE* (by definition). |
| A60 | `I_field_bounded : ∀ψ ∀r ∃M ∀s, abs s ≤ abs r → ψ(s)⊗ψ(s) ∈ {real M, I}` | SOR | 929f0b8c | FALSE: ψ = id on reals, r=1 (s=0 gives 0, s=1 gives 1, and one M cannot equal both). |
| A61 | `I_truth_value I := True ∧ False`; `I_paraconsistent : I_truth_value I` | SOR | 929f0b8c (Coq version `1ce08858`: `True`) | FALSE (its negation is provable). Coq version TRUE*. |

### 2.3 Abstract P1–P15 (PAX) and the "counterexamples to field axioms" CE1–CE9

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A62 | **Consistency of P1–P15** (P2 associativity, P4 `a+0 = a`, P5 `a+(−a) = 0`, P10 `I≠0`, P12 `I+I = I`, …); "verified" (README), "conjectured" (audits) | AX (Lean `c641179f`, Coq `9137d111`); INF | `43901456`; `main:audits/model_limitations.md (8323ec96)` | FALSE: `I = I+0 = I+(I+(−I)) = (I+I)+(−I) = I+(−I) = 0`, contradicting P10. The Lean `AlgebraI/Basic.lean` and Coq `theories/Basic.v` axiom sets prove False. |
| A63 | P1–P9 and P13: a ring with `+`-inverses, `·`-monoid, distributivity and `a·0 = 0` | AX | c641179f, 9137d111 | TRUE (standard ring axioms; P13 is derivable). |
| A64 | **P11** `I² = I` | AX | same | TRUE in RING, KIJ and ABS. |
| A65 | **P12** `I+I = I` | AX | same | TRUE in KIJ, ABS and SET. Incompatible with P5 (A62). |
| A66 | **P14** `¬∃x, I·x = 1` | AX | same | TRUE (it is derivable from P7, P8, P10 and P11; see A71), so it is not independent. |
| A67 | **P15** `I·0 = 0` | AX | same | TRUE in RING and WT (derivable from the ring axioms). |
| A68 | `i_minus_i : I − I = 0` (from P5) | PRV | c641179f, 9137d111 | TRUE in PAX and RING. It conflicts with P7 of KIJ (`I⊖I = I`). |
| A69 | P1–P11, P13–P15 without P12 are consistent | — (my observation) | — | TRUE: RING, `I = (1,0)` in `ℝ×ℝ`. |
| A70 | `Iⁿ = I` for n ≥ 1 (`i_power_eq_i`); CE9 "exponentiation doesn't grow" | SOR; INF | c641179f, 9137d111, `main:docs/theory/axioms/counterexamples.md (e70e7683)` | TRUE (induction from `I² = I`). |
| A71 | **CE1**: I has no inverse (`I = I·(I·I⁻¹) = (I·I)·I⁻¹ = I·I⁻¹ = 1`) | INF (proof) | e70e7683 | TRUE in any monoid: an idempotent `≠ 1` is not a unit. |
| A72 | **CE2**: cancellation fails (`I·I = I·1`, `I≠1`) | INF | e70e7683 | TRUE. |
| A73 | **CE3**: "`(I−I) = 0` but neither factor is 0"; audits: "idempotent `I² = I` that is **not** a zero divisor" | INF | e70e7683, 8323ec96 | CE3 is NAP. The audit claim is FALSE in any ring (`I(1−I) = 0` with `I ≠ 0, 1`); it is TRUE only in WT (`I·x = 0 ⇔ x = 0`). |
| A74 | **CE4**: additive cancellation fails (`I+I = I+0`, `I≠0`) | INF | e70e7683 | TRUE for structures with P12 and without P5. |
| A75 | **CE5**: "`2I² = I`, not `2I`" is a failure | INF | e70e7683 | FALSE as a "counterexample": `2I = I+I = I`, so `2I² = 2I = I` is consistent. |
| A76 | **CE6**: no total order compatible with `+` and `·` | INF (proof) | e70e7683 | TRUE: with strictly translation-invariant `<`, `0<I` gives `I = I+0 < I+I = I`, and `I<0` likewise, so I is incomparable with 0. |
| A77 | **CE7**: `x² = x` has 3 roots `{0, 1, I}`; `x+x = x` has 2 roots; this "violates the fundamental theorem of algebra" | INF | e70e7683 | Root counts: TRUE (RING has 4 idempotents). "Violates FTA": FALSE (the degree bound needs an integral domain). |
| A78 | **CE8**: `I−I = 0` and `I+I = I` both hold ("inverse takes priority") | INF | e70e7683 | FALSE (inconsistent; see A62). |
| A79 | "Abelian group under `+`, monoid under `·`, **not a ring because cancellation fails**" | INF | 43901456, 8323ec96 | FALSE: rings need no cancellation, and an abelian group plus a monoid plus distributivity is a ring. With P12 the system is inconsistent; KIJ is not a group under `⊕`. |
| A80 | Meta-axioms M2/M3: all 15 postulates are independent and minimal | INF | `main:docs/theory/axioms/README.md (ef759953)`, 43901456 | FALSE: P1, P6 and P9 (closure) are logically valid; P13 and P14 are derivable; and the whole set is inconsistent. |
| A81 | Uniqueness of I from `{I² = I, I+I = I, I≠0, I≠1, 0·I = 0}` (audits "✓ proven"; BOTTLENECK proof `I₁ = I₁·(I₂·I₂) = … = I₂`) | INF | 7a5d95da, 8323ec96 | FALSE: in KIJ, J satisfies all five hypotheses and `J ≠ I`. The proof is circular. |

### 2.4 Fully absorbing model, Tarski model, NexusField, Central Hypothesis, nexus_core (ABS)

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A82 | Tarski model `ℚ ∪ {I}`: `I≠0,1`; `I² = I`; `I+I = I`; `a/0 = I`; `0/0 = I`; `I/I = I`; `I+a = a+I = I`; `I·a = a·I = I`; ℚ operations preserved; `mutual_consistency`; `system_consistency`; `model_non_trivial` | DEF+PRV | `main:lean/consistency_proofs.lean (2f1c53a0)` | TRUE (genuinely proved: this is the common meadow ℚ⊥). Note this "15 postulates" list differs from P1–P15: it has `0·I = I` and no additive inverses. |
| A83 | `relative_consistency_zf : zf_consistent → ∃ model` | PRV | 2f1c53a0 | TRUE* (the hypothesis is unused). |
| A84 | **NexusField** structure fields N1–N15: N1 `0·inv 0 = I`; N2 `I≠0`; N3 `I≠1`; N4 `I+x = I`; N5 `x≠0 → I·x = I`; N6–N7 idempotence; N8–N9 `+` commutative and associative; N10 `a≠I → 0+a = a`; N11–N12 `·` commutative and associative; N13 `a≠I → 1·a = a`; N14 distributivity for a, b, c ≠ I; N15 `a≠I → 0·a = 0` | AX | `main:lean/NexusField.lean (be4be255)`, `main:lean/15_Axiomas_NexusField.md (cbf14c1d)` | Consistent: TRUE in ABS with `inv 0 = I` (`43ca57a3`). Derived consequence (not in the corpus): N1, N15 and N2 force `inv 0 = I` and `0·I = I`, which contradicts P4 (A30). |
| A85 | Lemmas 01–03 (`I·I = I`; `I≠1 ∧ I≠0`; `c≠0 → c·I = I`; `c+I = I`); absorption chains; `independence_from_base`; `singularity_stability`; general commutativity and associativity | PRV | be4be255 | TRUE (immediate from the fields). |
| A86 | `absorption_distributive : x,y ≠ 0 → I·(x+y) = I` (case `x+y = 0` left as sorry) | SOR | be4be255 | TRUE: the missing case is `I·0 = 0·I = I` (derived in A84). |
| A87 | `induction_base : I·1 = I` (sorry for `1≠0`) | SOR | be4be255 | TRUE (if `1 = 0` then `I·1 = I·0 = I` by A84). |
| A88 | `schwarzschild_connection : ∃metric, ∀r, r = 0 → metric r = I` | AX | be4be255 | TRUE* (take the constant I). |
| A89 | `nexusfield_consistency : ¬∃p, p ∧ ¬p` | PRV | be4be255 | TRUE* (a tautology; it says nothing about NexusField). |
| A90 | `concrete_model_valid : 0·inv(0) = I`; concrete examples (`0·I = I`, `inv I = I`, `inv(inv r) = r`, list sum/product with I equals I) | PRV | be4be255, `main:lean/NexusFieldExamples.lean (43ca57a3)` | TRUE (ABS). |
| A91 | CentralHypothesis H1–H3: `I := 0/0` exists; `k +ₙ I = I`; `k≠0 → k ⊗ₙ I = I`; Lean axiom `zero_mul_I : 0 ⊗ₙ I = ⟨some 0, _⟩` | AX | `main:formalizations/lean/AlgebraIndeterminate/CentralHypothesis.lean (ed29a88f)` | The Lean carrier `{v // v = none}` has one element. `zero_mul_I` is ill-typed and FALSE (`some 0 ≠ none`), and it contradicts the definition (`0⊗ₙI = I`). Isabelle (`d947976c`) and Agda (`d18e45ef`) prove `0⊗ₙI = I` instead: TRUE (ABS). |
| A92 | `consistency_of_I : ∀ data stream d, process d I = I` (by induction); `logic_absorption` | PRV | ed29a88f, d947976c, d18e45ef | TRUE* (`process` ignores d). |
| A93 | `singularity_is_I`, `physical_indeterminacy` (state = I at r=0 or the Planck scale) | AX/PRV | same | TRUE* (by definition). |
| A94 | nexus_core axiom `indeterminate_def : x.is_indeterminate = true → x.val = 0` | AX | `main:lean/nexus_core.lean (4ea207db)` | FALSE (`⟨1, true⟩` is a term), so the file is inconsistent. |
| A95 | nexus_core Lemmas 1–10, 26–35: I absorbs `+`, `·`, `/` on both sides; `I+I = I·I = I/I = I`; `x/0 = I` for standard x; nested absorption | PRV | 4ea207db | TRUE (ABS-like; note that many distinct `⟨q, true⟩` all behave as I). |
| A96 | `lemma_I_limit_absorption/interchange/sequence_limit : (∃n, f n = I) → ∀L, L = I` | SOR | 4ea207db | FALSE (L = standard 0). It would trivialise the type. |
| A97 | `lemma_I_homomorphism_preservation`: f preserves `+` and `·` → `f I = I` | SOR | 4ea207db | FALSE: f ≡ standard 0. (Compare A10, which uses `⊖`.) |
| A98 | `lemma_I_universal : ∀f x, f x = I → f(f x) = I` | SOR | 4ea207db | FALSE: `f x = I` if `x = 0` else 0; then `f 0 = I` but `f I = 0`. |
| A99 | Lemmas 11, 15–25, 36–50, 52, 54–55: integration, manifold, contour, Cauchy, ε-δ, continuity, compactness, chain/product/quotient rules, "Hausdorff" … all of the form `… → True` or `I = I` | PRV | 4ea207db | TRUE* (vacuous). |
| A100 | `IComplex = ℂ ⊕ I` with `inr` absorbing (incl. `0·I = I`); `I_absorbing`; `I_indeterminate : ∀x:ℂ, x/0 = inr default` | DEF/AX | ce16cd1e, `main:formalizations/agda/ITheory.agda (e80c38b4)` | `I_absorbing`: TRUE (ABS). `I_indeterminate`: NAP (ill-typed; in Mathlib `x/0 = 0` in ℂ). |

### 2.5 AEI ("I = 1/0") — `KI K`, ExtendedOperators, Transitions, Examples

Sources: `242da20d` (AEI.lean), `ba30ccd4` (ExtendedOperators), `fa9b2687` (Transitions), `ecb9356b` (Examples), Coq `b219e6d2`/`04bf6527`/`6b1ee806`/`257afeeb`, Isabelle `087ff063`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A101 | AEI tables: `+` I-absorbing; `a·I = I` (a≠0); `0·I = I·0 = 1`; `I·I = I`; `a/0 = I`; `0/a = I`; `I/x = x/I = I`; `I−I = I`; `I^n = I` for all n incl. 0; `I^(−n) = I`; `0^(−n) = I` | DEF | 242da20d, ba30ccd4, b219e6d2, 087ff063 | Definition. Note `0/1 = I` and `I^0 = I` (vs `I^0 = 1` in A120). |
| A102 | `I = "1/0"`; `I_as_limit` with `"distance"(1/x, I) < ε`; `axiom I : Type`; `I ≠ (any_k : K)` | AX | 242da20d, b219e6d2 | NAP (ill-typed). The Coq `I = 1/0` is TRUE* (KI_div). |
| A103 | `I_not_zero`, `I_not_field_element` | AX | 242da20d, b219e6d2, 087ff063 | TRUE* (constructors; redundant). |
| A104 | `a≠0 → a+I = I`; `a≠0 → a·I = I`; `I+I = I`; `I·I = I`; `I−I = I`; `I^n = I`; `2I = 3I = kI = I`; `a/0 = I`; `[I,a] = I`, `{I,a} = I` (commutator, anticommutator); `KI` closed under `+ · /` | PRV | 242da20d, ba30ccd4, ecb9356b, b219e6d2, 04bf6527 | TRUE (AEI). `two_I_eq_three_I` and `100·I = I` need `2,3,100 ≠ 0` in K: FALSE in characteristic 2 or 3 (char 2: `2·I = 0·I = 1 ≠ I = 3·I`); Isabelle proves it "by simp" for an arbitrary type. |
| A105 | `I·0 = 1`, `0·I = 1` "by convention" | PRV (Lean rfl); Coq `∀ zero one, … = fromField one` admitted | 242da20d, b219e6d2 | TRUE by definition in Lean. The Coq form with a quantified `one` is FALSE (take one := 0). |
| A106 | `I_no_inverse : ¬∃x, I·x = 1` (and Example 53, Isabelle) | SOR/admit | 242da20d, b219e6d2, 087ff063, ecb9356b | FALSE in AEI: x=0. |
| A107 | `inverse_implies_contradiction : (∃x, I·x = 1) → I = 1`; `no_solution_xI_eq_1` | SOR | same | FALSE (x = 0: the premise holds and the conclusion fails). |
| A108 | `KI_not_field : ¬∀x≠0, ∃y, x·y = 1` | PRV-by-sorry | 242da20d, b219e6d2, 087ff063 | FALSE in AEI: every nonzero element is invertible (`I⁻¹ := 0`). |
| A109 | `zero_I_eq_1_contradiction : 0·I = 1 → fromField 0 = fromField 1` | "PRV" (`exact h`, ill-typed) | 242da20d | FALSE (the premise holds, the conclusion fails). |
| A110 | `non_associativity : a≠0 → (I·a)·0 ≠ I·(a·0)` | SOR (Lean); **AX** (Coq) | 242da20d, b219e6d2 | FALSE: both sides are 1. The Coq axiom is inconsistent. `·` is still non-associative elsewhere: `(0·I)·I = I` but `0·(I·I) = 1`. |
| A111 | `suspended_distributivity : a,b,a+b ≠ 0 → I·(a+b) ≠ I·a + I·b` | SOR (Lean); **AX** (Coq) | 242da20d, b219e6d2 | FALSE: both sides are I. The Coq axiom is inconsistent for `abs K ≥ 3`. Distributivity does fail at `a+b = 0`: `I·(1+(−1)) = 1` but `I+I = I`. |
| A112 | `no_cancellation : ∃a≠b, I·a = I·b` | SOR/admit | 242da20d, b219e6d2 | TRUE iff K has at least two nonzero elements; FALSE for 𝔽₂. |
| A113 | `extended_equiv_fraction : 1/x ≡ᴵ 2/3 → x = 3/2 ∨ x = 0`; `div_by_zero_equiv_I` | SOR; PRV | 242da20d | TRUE (all characteristics). |
| A114 | `no_homomorphism_preserving_I : ¬∃f: KI K → K` preserving `+` and `·` with `f I = k` | SOR | 242da20d, b219e6d2, 087ff063 | FALSE: f ≡ 0. |
| A115 | `consistency_preserved : 1 ≠ 0`; `non_triviality` | SOR/PRV | 242da20d, b219e6d2 | TRUE. |
| A116 | `one_over_x_approximates_I` (n ↦ 1/(1/n) is unbounded) | SOR | 242da20d | NAP for a general field K (no absolute value); TRUE for K = ℝ. |
| A117 | Transitions: `embed` preserves `+`, `·`, `−`, 0, 1 and is injective; `project ∘ embed = some`; `lift (f∘g) = lift f ∘ lift g`; `x·0 = 1` has no solution in K but I solves it in KI | PRV | fa9b2687, 6b1ee806 | TRUE. |
| A118 | `compatibility_div : b≠0 → embed a / embed b = embed (a/b)` | PRV-attempt | fa9b2687 | FALSE at a=0: `0/b = I` (the 0/a rule). |
| A119 | Examples 48/49: `(a+b)·I = I`, `aⁿ·I = I` (sorry branches); Example 50 `a/0 + b = I`; 56; 57 | SOR/PRV | ecb9356b | 48/49: FALSE when `a+b = 0` or `aⁿ = 0` (the result is 1). 50, 56, 57: TRUE. |
| A120 | `KI.PartialOrder` with constructor `I_incomparable : ¬(…)`; `KI.beq` | DEF | ba30ccd4, 04bf6527 | NAP: a non-positive inductive, rejected by Lean and Coq. |
| A121 | Lifted functions: `log 0 = I`, `log I = exp I = sin I = cos I = √I = ⁿ√I = I`; limsup, liminf, series sums, infinite products, derivative, integral, measure, determinant, operator norm, probability, expectation, variance, entropy, gcd, lcm, Kolmogorov complexity "may be or are I"; `I_is_prime = I_is_composite = False` | DEF (stubs with sorry; the Coq versions are literally the constant I) | ba30ccd4, 04bf6527 | Definitions/NAP (no claim). |
| A122 | `I_is_root : ∃p, p(I) = 0`; `improper_integral_may_be_I` | SOR | ba30ccd4 | TRUE* (p = const 0; integral with an I bound is I by definition). |
| A123 | `operation_table` lists `0·I = 1`, `I·0 = 1` | DEF | ba30ccd4 | Consistent with A105. |
| A124 | Ternary logic `I_and`, `I_or`, `I_not` on `{true, false, indeterminate}` | DEF | ba30ccd4, 04bf6527 | This is Kleene's strong K3. De Morgan laws hold (TRUE); excluded middle fails at the third value. |

### 2.6 "Solutions 104.x" — ExtendedOperations `ℝ ∪ {I, J, 0_I, I_0}`

Sources: `copilot/add-annotated-labels-arrows:formalizations/lean/AlgebraIndeterminate/ExtendedOperationsI.lean (90970f1a)` (also lean/), `copilot/add-annotated-labels-arrows:docs/MULTISTATE_LOGIC.md (0b84bb74)`, `ialgebra/extended_operations.py (4c2a38a1)`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A125 | `I·J = J·I = 1`, `I·I = I`, `J·J = J`; `0·I = I·0 = 0_I`; `I+0 = 0+I = I_0`; `I+I = I`; `I_0` absorbing; J absorbing for `+`; `I^n = I` (n≥1), `I^0 = 1`, `J^0 = 1`, `0_I^0 = I`; `log I = J`, `log J = I` | DEF + PRV (rfl) | 90970f1a, 0b84bb74 | TRUE as definitions. |
| A126 | "J gives inverse-like behaviour **without contradiction**" | INF | 0b84bb74, 90970f1a | Only because associativity is dropped: `(I·I)·J = 1` but `I·(I·J) = I`. With associativity, `I·J = 1` and `I² = I` give `I = 1`. As a claim about an associative algebra: FALSE. |
| A127 | `J_inverse_behavior : x = I → ∃y, x·y = 1` | AX | 90970f1a | TRUE (y = J). |
| A128 | `cancellation_restricted : a ∈ ℝ*, a·b = a·c → b = c` | SOR | 90970f1a | TRUE (a nonzero real acts injectively on the carrier). |
| A129 | `I_distribute_nonzero : b, c not zero → I·(b+c) = I` ("Solution 104.2") | SOR | 90970f1a, 0b84bb74 | FALSE: b=1, c=−1 gives `I·0 = 0_I`. |
| A130 | `extended_zeros_coherent : ∀x, x·0_I = 0_I` | AX | 90970f1a | FALSE: x=0 gives `0·0_I = 0` by the `real 0, _` clause, so the axiom contradicts the definition. |
| A131 | `no_triviality_collapse : n ≠ 0 ∨ n = 0` | AX | 90970f1a | TRUE* (excluded middle). |
| A132 | `I + 0 = I_0 ≠ I` (0 is not an identity for I) | DEF | 90970f1a | Definition; it conflicts with every other model (`I+0 = I`). |

### 2.7 IEA (Indeterminate Extended Algebra)

Sources: `copilot/analyze-complex-plane-singularities:lean/IEA.lean (503a118a)`, `coq/IEA.v (2407c988)`, `isabelle/IEA.thy (6ad50054)`, `docs/IEA_COMPLETE_DOCUMENTATION.md (04835e7c)`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A133 | IEA tables: I-absorbing `+`; then J; `+∞ + −∞ = I`; `+∞ ⊕ x = +∞` but `x ⊕ +∞ = I`; `complex ⊕ real = I`; `0·I = I·0 = 0`, `0·J = 0`; `x/0 = I` | DEF | 503a118a, 2407c988, 6ad50054 | Definition. Defect: `⊕` is not commutative (`r ⊕ +∞ = I` but `+∞ ⊕ r = +∞`), and `complex 0 ≠ real 0`. |
| A134 | **A1** `r≠0 → r/0 = I` and `I≠0` | AX | same | TRUE (IEA). |
| A135 | **A2** `x⊕I = I`; `¬zero x → x⊗I = I`; `0⊗I = 0` | AX | same | TRUE (IEA, WT). |
| A136 | **A3** `∃λ∈ℝ ∀abc, a⊗(b⊕c) = (a⊗b)⊕(a⊗c)⊕(λ⊗J)` | AX (Lean, Coq) | 503a118a, 2407c988, 04835e7c | FALSE in IEA. With λ=0 and (I,1,−1): `I⊗0 = 0` but the right side is `I⊕I⊕0 = I`. With λ≠0 the right side is in {I, J} while a=b=c=1 gives 2. So the Lean and Coq IEA files are inconsistent. |
| A137 | **A4** `¬∃x, I⊗x = 1`; **A5** `I≠0`; `IEA_not_field`; `collapse_contradiction`; real `+`, `·` preserved; real distributivity | AX/PRV | same | TRUE (IEA). |
| A138 | `+∞ ⊖ +∞ = I`; `−∞ ⊖ −∞ = I`; `+∞ ⊕ −∞ = I` | PRV/INF | same | TRUE by definition. Matches LIM: `a_n − b_n` with `a, b → +∞` can tend to any L in `EReal` (TRUE). |
| A139 | `distributivity_fails` with witness `(2, +∞, −∞)` | SOR (Lean), Coq | 503a118a, 2407c988 | The witness fails (both sides are I). The statement is TRUE with witness `(I, 1, −1)`. |
| A140 | Doc: "If `I = 0` then `1/0 = 0`; multiplying by 0 gives `1 = 0`" | INF | 04835e7c | FALSE as a general argument: MEADOW is consistent (`(1/0)·0 = 0 ≠ 1` is not forced). |
| A141 | Doc: "IEA is consistent (proven), complete, formally verified"; "`1/0 = I` gives a continuous extension of division" | INF | 04835e7c | FALSE (A136 makes the Lean/Coq versions inconsistent; continuity: A167). |

### 2.8 Flexible resolution, `K_I = {a + bI}` (FLEX)

Sources: `main:formalizations/lean/AlgebraIndeterminate/FlexibleResolution.lean (40a5384e)`, Coq `1dbec880`, Isabelle `7d9c4d78`, Agda `31f71680`, `main:FLEXIBLE_RESOLUTION_README.md (05a620f5)`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A142 | `K_I = K×K`, componentwise `+`; `(a+bI)(c+dI) = ac+(ad+bc)I+bd·Ω(I)`, with `Ω(I) ∈ {I, kI, I+ε (ε²=0), 0, …}` | DEF | 40a5384e, 05a620f5 | Definition. With `Ω = I` it is the ring `K[I]/(I²−I) ≅ K×K` (RING); with `Ω = 0`, the dual numbers. |
| A143 | Axioms 23/24/26, `I_power`: "x/0 = I", "a+I = I", "a·I = I", "a(b+c) = ab+ac+λJ", "Iⁿ = I", formalised as `∃ result, result = (0,1)` | AX | 40a5384e, 1dbec880, 7d9c4d78 | As formalised: TRUE* (trivial existentials). As intended inside K²: FALSE. `(a,0)+(0,1) = (a,1) ≠ I` for a ≠ 0 (absorption contradicts componentwise `+`), and `a·I = aI ≠ I` for a ∉ {1}; the λJ correction is unnecessary because `·` is bilinear. |
| A144 | **Separation** `∀λ∈K, I ≠ λ` | AX | 40a5384e, 1dbec880, 7d9c4d78 | Lean/Coq: NAP (ill-typed: `I_elem : I`, `λ : K`). Isabelle: λ is inferred to have type `I_type`, so the axiom `∀λ, I_elem ≠ λ` is FALSE (λ := I_elem) and the file is inconsistent. The intended `(0,1) ≠ (λ,0)` is TRUE. |
| A145 | `I_add_idempotent` (linear): `I+I = 2I` | PRV | 40a5384e | TRUE (shows I+I ≠ I in K_I unless char 2, where I+I = 0). |
| A146 | `I_mul_idempotent`: `I·I` has I-coefficient 2 | PRV-attempt (linarith) | 40a5384e | FALSE: with `Ω = I`, `(0,1)(0,1) = (0,1)` (coefficient 1). |
| A147 | `add_with_absorption`, `mul_with_absorption` give `I+I = I` and `I·I = I` | PRV/SOR | 40a5384e, 1dbec880, 7d9c4d78 | TRUE* (by the if-then-else definition). |
| A148 | `global_zero_prohibited`, `system_consistent`, "Theorem 5: local resolution consistent for α ≠ 0" | PRV | 40a5384e, 7d9c4d78 | TRUE* (bookkeeping on a Boolean `is_consistent`). |
| A149 | "Theorem 3: `I = 0` globally → `1 = 0`" | INF | 05a620f5 | Depends on the model: TRUE under total additive absorption (A19); FALSE in linear K² (setting I := 0 just leaves K). |

### 2.9 ZDIV ("I-structures") and I-calculus axioms

Sources: `main:formalizations/lean/IAlgebra.lean (258c41ea)`, Coq `ac245181`, Isabelle `f212d681`, Agda `e0a6d060`, `main:formalizations/README.md (9e960ae8)`, `formalizations/DOCUMENTATION.md (7d349973)`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A150 | `r⊕s = I` if `r+s = 0`; `r⊖s = I` if `r = s`; `r⊗s = I` if `rs = 0`; `r⊘s = I` if `s = 0`; I absorbing; `J⊗J = 0`; mixed cases give I | DEF | 258c41ea, ac245181, f212d681, e0a6d060 | Definition. ℝ is not a substructure (`0⊕0 = I`, `2⊗0 = I`), and `⊕` is not associative: `(1⊕1)⊕(−1) = 1` but `1⊕(1⊕(−1)) = I`. |
| A151 | Thm 14.1 `x⊕I = I ∧ I⊗x = I ∧ x⊘I = I`; `x⊖x = I` (so `5⊖5 = I`); `eadd_comm`; `axiom_i2 I≠0`; `axiom_i3` | PRV/AX | same | TRUE (ZDIV). The Agda `self-sub` has a hole in the impossible case. |
| A152 | `j_property : J = 1⊘I` | AX | 258c41ea | FALSE: the definition gives `1⊘I = I ≠ J`, so the file is inconsistent. |
| A153 | Coq `ideriv f x := I`; axiom `ideriv_iexp : ideriv iexp x = iexp x` | DEF + AX | ac245181 | FALSE at x=0 (`I ≠ real 1`), so the Coq ICalculus module is inconsistent. The Agda version postulates `ideriv` abstractly and is consistent. |
| A154 | `ichain_rule`, `iproduct_rule` (with `ideriv ≡ I`) | AX | ac245181, e0a6d060 | TRUE* in Coq (`I = I⊗I`, `I⊕I = I`). |
| A155 | `a⊗b = I^(1−ab)·(ab)`, `a⊘b = I^(ab)·(a/b)`, `exp_I(x) = Σ x^⊗n/n! = I^(e^(−x))·e^x`, `df/dI = lim_{ε→I}(f(x⊕ε)⊖f(x))/ε` | INF | 9e960ae8, 7d349973, Python `f09c6359` | NAP (real exponents of I are undefined and inconsistent with the case definitions). |

### 2.10 Multistate I (MS)

Sources: `copilot/add-annotated-labels-arrows:formalizations/lean/AlgebraIndeterminate/MultiStateI.lean (5493bb58)` (also lean/), Coq `f1b69b3a`, Isabelle `a0e38ac6`, `docs/MULTISTATE_LOGIC.md (0b84bb74)`, `MULTISTATE_README.md (a6bef783)`.

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A156 | States `{0,1,I,∞,?}`; `I−I ↦ {0,I,?}`, `I/I ↦ {1,I,?}`, `I/0 ↦ {I,∞,?}`; contexts standard/limit/infinity/algebraic with priority lists | DEF | 5493bb58, f1b69b3a, a0e38ac6 | Definition. |
| A157 | The three results are not determinate (card ≠ 1); `I−I` contains 0; `I/I` contains I (and 1) | PRV | same | TRUE (by computation). Semantically, in SET: `0 ∈ ℝ−ℝ` and `1 ∈ ℝ/ℝ*` are TRUE. The exact 3-element sets are NAP. |
| A158 | Resolutions: `I−I` →limit 0; `I/I` →standard I; `I/0` →infinity ∞; table (algebraic: 0, 1, I) | PRV | same, 0b84bb74 | TRUE. |
| A159 | `resolve_valid : resolve r ctx ∈ r.states` | SOR (Lean); PRV (weaker Coq/Isabelle form) | same | TRUE (each branch returns a member). |
| A160 | `determinate_context_independent` | SOR | 5493bb58 | TRUE. |
| A161 | `equalSuperposition` normalised (`3·(1/√3)² = 1`) | SOR | 5493bb58 | TRUE. |
| A162 | `IDominated` `(0.2, 0.94, 0.27)` normalised | SOR | 5493bb58, f1b69b3a, 0b84bb74 | FALSE: `0.04 + 0.8836 + 0.0729 = 0.9965 ≠ 1`. The quoted measurement statistics (~4%, ~88%, ~7%) match the threshold code only roughly. |
| A163 | `beyond_binary_logic`, `singularity_interpretation` | AX | 5493bb58, f1b69b3a, a0e38ac6 | TRUE* (excluded middle; any state). |
| A164 | "`I/0 = (1/0)/0 = 1/(0·0) = 1/0 = I`" | INF | 0b84bb74 | The conclusion is TRUE in ABS and KIJ by definition. The derivation uses a field law that is invalid there. |

### 2.11 Analysis, limits, continuity, functions

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A165 | `limit_indeterminate_to_I`: f, g → 0 (not both 0) ⇒ `f/g` converges to I | SOR | 929f0b8c | FALSE: `f = g = 1/(n+1)` gives `f/g = 1`. |
| A166 | `lim_{x→0} x/x = I`; `lim_{ε→0} ε/ε = I` (and `lim_{x→∞} x/x = 1`) | INF | 7b3ff63d | FALSE (both limits are 1); the last one is TRUE. |
| A167 | `1/0 = I` is "continuous through the singularity"; "elimination of discontinuities" | INF | 04835e7c, `main:README.md (843f5a7d)` | FALSE for 2-variable `⊘`: in any T1 topology on ℝ∪{I}, `(x,y) ↦ x⊘y` is discontinuous at (0,0) (constant 1 along the diagonal). The 1-variable `y ↦ 1⊘y` can be made continuous by declaring I to be the point ∞ of `OnePoint ℝ`. |
| A168 | Python calculus: `lim x²/x = I`; `lim 1/x = I`; `d/dx(1/x)` at 0 = I; `∫_{−1}^{1} 1/x dx = I` | INF | `main:src/python/ialgebra/calculus.py (c73049cb)`, `6d583125` | `lim x²/x = 0`: FALSE. `lim 1/x`: no two-sided limit in `EReal`; it is ∞ in `OnePoint ℝ` (labelling it I is a convention). `∫ 1/x`: not Lebesgue integrable (principal value 0), so I is a label only. |
| A169 | Every 0/0 form "is" the same I | INF (throughout) | 4b018696, 7b3ff63d | LIM: TRUE that `0/0` has no determinate value (`∀L∈EReal ∃f,g→0, f/g→L`), but the different forms give different cluster sets (`x²/x → 0`, `sin x/x → 1`). |
| A170 | "∀ε ∃δ: abs x, abs y < δ ⇒ x/y converges to I" | INF | 7a5d95da | NAP/FALSE. |
| A171 | `limits_dont_determine_point_value` (f(x) = x for x≠0, f(0) = 1) | SOR (Lean, mis-scoped); Coq | `main:lean/ContinuityAnalysis.lean (78803781)`, `main:coq/ContinuityAnalysis.v (093ff3ff)` | TRUE (intended). |
| A172 | `limit_right_pos_infinity`, `limit_left_neg_infinity` (`1/x → ±∞`) | AX | 78803781, 093ff3ff | TRUE (standard; should be theorems). |
| A173 | `division_not_continuous_at_zero`: no continuous `f : ℝ² → ℝ` with `f(x,y) = x/y` for y≠0 | SOR (Lean); Coq with `True` placeholder | 78803781, 093ff3ff | Lean: TRUE. Coq form (`¬∃f, (…) ∧ True`): FALSE (f := x/y exists with Coq's total division). |
| A174 | `extended_division_piecewise_continuous`: uniform ε-δ for `x/y` over all `y ≠ 0` | SOR | 78803781, 093ff3ff | FALSE: `x₁ = x₂ = 1`, `y₁ = δ/3`, `y₂ = −δ/3`. |
| A175 | `division_has_jump_discontinuity` (formalised with `True` bodies) | SOR | 78803781 | FALSE as formalised (the inner `∃` holds trivially). The intended "no two-sided limit of a/y at 0" is TRUE. |
| A176 | `¬∃ topology τ` on ExtendedReal making `⊘` (or `x ↦ x⊘0`, `y ↦ r⊘y`) continuous (`algebraic_consistency_without_continuity`, `smooth_not_continuous`, `result2`, `fundamental_question`) | SOR | 78803781 | FALSE: the discrete topology makes every map continuous. (See A167 for the correct restricted statement.) |
| A177 | `I_not_comparable : ∀r, ¬(r < I) ∧ ¬(I < r)` | AX | 78803781 (Coq: `True`) | NAP (no order is defined). Intended: no order compatible with absorbing `+` exists, which is TRUE by A76. |
| A178 | `duality_claim I = 0⊘0`; `duality_established` (`r⊘0 = I`, `I⊘1 = I`); "I = 0/0 = ∞/∞" | AX/PRV/INF | 78803781, 093ff3ff | TRUE* by definition. The ∞/∞ part is NAP (in WHEEL, `1/0 = ∞ ≠ ⊥`). |
| A179 | `black_hole_no_infinite_curvature`, `big_bang_no_initial_singularity` (`I ≠ infinity_interpretation`, where `infinity_interpretation := I`) | SOR | 78803781 | FALSE (both sides are I). The Coq variants (`I ≠ 0`, `I ≠ real r`) are TRUE. |
| A180 | `result1/3`, `answer_valid_algebraic_structure` | SOR/PRV | 78803781, 093ff3ff | TRUE*. |
| A181 | Function atlas: `exp_I(I) = I`, `log I = I`, `sin, cos, tan, sinh, cosh, tanh(I) = I`, `Γ(I) = ζ(I) = J_α(I) = I`, `Γ` at poles = I, `ζ(1) = I`, `I^x = I` (x≠0), `x^I = I` (x ≠ 0,1); `0^0 = ∞^0 = 1^∞ = I` | DEF/INF | `main:book/parts/part7/appendix_A_function_atlas.tex (742ecc2b)` | Definitions (strict lift `f(I) := I`), consistent in ABS-style lifting. The derivations are invalid: "`log I = I` because `e^I = I`" needs injectivity, and `e^J = J` too. LIM: the forms `0^0`, `∞^0`, `1^∞` can take any value in `[0,∞]` (TRUE). |
| A182 | `sin I = (e^{iI} − e^{−iI})/2i = (I−I)/2i = I` | INF | 742ecc2b | Valid only where `I−I = I` (ABS); in PAX (`I−I = 0`) it would give 0. Model-dependent. |
| A183 | ch33 hardware `ExtendedReal`: `a/0 = ±∞` (a≠0), `0/0 = I`, `+∞ + −∞ = I`; `(a−a) → I` "explicitly" | DEF/INF | 55417d03 | Definitions; `a/0 = ±∞` conflicts with the corpus-wide `a/0 = I`. "`(a−a) → I`" is FALSE in its own code (`Finite(a) − Finite(a) = Finite(0)`). |
| A184 | "I represents the point at infinity in projective completions" | INF | 7b3ff63d | FALSE/NAP: the projective point ∞ is `1/0` and leaves `0·∞` undefined; WHEEL separates `∞` and `⊥ = 0/0`. |

### 2.12 Logic

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A185 | I-logic truth tables (`¬I = I`; Kleene `∧`, `∨`; `P→Q := ¬P∨Q`; `P° = F` iff `P = I`) | DEF | `fb45f2e2` | This is K3/LP. |
| A186 | "Controlled indeterminacy": `P = I` does not let you derive an arbitrary determinate Q (no explosion) | INF (thm) | fb45f2e2 | TRUE in LP (designated `{T,I}`: `P=I`, `Q=F` is a countermodel). FALSE in K3 (explosion holds vacuously). |
| A187 | `P∨¬P` can take value I; `∧`, `∨` are associative; if `P→Q = I` and `P = I` then Q is undetermined | INF (exercises) | fb45f2e2 | TRUE (K3/LP; `I→Q = I` iff `Q ∈ {I,F}`). |
| A188 | Guarded modus ponens, restricted universal instantiation (`x°` required) | DEF | fb45f2e2 | NAP (no semantics or soundness given). |
| A189 | `ZF + AC + I₁…I₁₅` is non-trivial | INF | fb45f2e2 | NAP for the undefined list `I₁₅`; TRUE* for the cardinal axioms (CARD); FALSE if the list includes P1–P15 (A62). |

### 2.13 Model theory, ultrapowers, set theory

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A190 | Python `src`: `I+0 = I`, `I+I = I`, `I−I = 0` ("restricted cancellation"), `0−I = I` (so `−I = I`), `I−r = I` | DEF (code) | `main:src/python/ialgebra/operations.py (2f0cbcd6)` | Inconsistent with `a−b = a+(−b)`: `I−I = I+(−I) = I+I = I ≠ 0`. FALSE as a coherent algebra. |
| A191 | Non-principal ultrafilters on ℕ exist under AC; "equivalent to a weak AC", not provable in ZF | INF | 6b1ad6b2 | TRUE ("equivalent" is loose: it follows from the Boolean prime ideal theorem). |
| A192 | Łoś's theorem (classical); `transfer_principle`; `los_theorem` as an axiom over an abstract `satisfies` | INF/AX | 6b1ad6b2, 26be2b27, `4f43bf33`, `99d9e84c` | TRUE as mathematics (Mathlib: `FirstOrder.Language.Ultraproduct`). As an axiom over an uninterpreted predicate it is contentless. |
| A193 | Extended ultrapower `M* = ℝ^ℕ/U ∪ {I}`; a sequence is identified with I when `{n : a_n − a_n undefined/divergent} ∈ U`; "indeterminate sequence: `[a]−[a] = I`" | DEF | 6b1ad6b2, 26be2b27 | TRUE* but vacuous: `a_n − a_n = 0`, so no sequence becomes I, and `[a]−[a] = 0` in `ℝ^ℕ/U`. |
| A194 | Example: the oscillating `[0,1,0,1,…]` is "indeterminate I" in `ℝ^ℕ/U` | INF | 6b1ad6b2 | FALSE: U contains the evens or the odds, so the class is 0 or 1. |
| A195 | Well-definedness of `M*`; "modified Łoś with I-logic"; "partial transfer for I" | INF | 6b1ad6b2 | Classical part TRUE; the I parts are NAP. |
| A196 | Preservation of I-axioms (I1, I4, I7, …) under ultrapowers | INF | 6b1ad6b2, 26be2b27 | TRUE (first-order sentences, by Łoś); trivial. |
| A197 | Saturation: `abs M < abs U` ⇒ `M^I/U` is `abs M⁺`-saturated | INF (thm) | 6b1ad6b2 | FALSE: M = ℝ, I = ℕ gives an ultrapower of size 𝔠, which cannot be 𝔠⁺-saturated (the type `{x ≠ a : a}` is not realised). |
| A198 | Consistency of ZF+AC+I1–I15 via the extended ultrapower; ZF+I consistency via "forcing adapted to ultrapowers" | INF/SOR | 6b1ad6b2, 26be2b27, 289f4c7c, 8a1fbd6e | The conclusion is TRUE* (conservative extension); the proofs are vacuous or invalid. |
| A199 | `I_as_infinitesimal_difference : ∀κ λ, (∃ infinitesimal x, y) ∧ κ⊖λ = I` | AX (with sorry terms) | 4f43bf33 | Forces `⊖ ≡ I`. FALSE in CARD (`2⊖1 = 1`). NAP as written (sorry ultrafilter). |
| A200 | `ultrapower_indeterminacy`, `I_preserves_consistency`, `hierarchy_preserved (rank S = n → S ∈ V_n)`, `no_contradictions`, `nonstandard_with_I`, `construct_extended_model`, `forcing_preserves_consistency` | SOR/AX | 4f43bf33, 289f4c7c | NAP (over uninterpreted placeholders). |
| A201 | Algebra.lean: `AbelianGroup Cardinal` with `inv = id` (`inv_left : κ+κ = 0`) | SOR | `8e0f6a4b`, `d629f086` | FALSE (`1+1 = 2 ≠ 0`). |
| A202 | `hom_preserves_indeterminacy`, `I_invariant_under_iso`, `IndeterminacyKernel` (relation defined by sorry) | SOR | 8e0f6a4b | NAP. |
| A203 | `cardinal_indeterminate_properties : κ⊖κ = I ∧ I⊕κ = I` | SOR (2nd part) | 8e0f6a4b | The second conjunct is independent of Cardinals.lean's axioms (model: ℤ/2 with `⊖ ≡ 0 =: I` satisfies I1–I3 and the ring axioms, but `0⊕1 = 1`). It is TRUE in CARD. |
| A204 | `near_ring_structure : (κ⊕λ)⊗μ = κμ ⊕ λμ` | PRV-attempt | 8e0f6a4b | TRUE (from the commutativity and left-distributivity axioms; the given proof term has the wrong shape). |
| A205 | `theory_independence`: `zf_consistency_with_I`, `relative_consistency`, `proper_extension`, `generic_meets_distinct`, `ch_analogy_structure`, `div_by_zero_yields_I : (a/0 : IndeterminateType) = I` | SOR/AX | 8a1fbd6e | NAP: `Prop` placeholders; the last is ill-typed (no division). `ch_analogy` is TRUE* (excluded middle). |

### 2.14 Wheel theory (ℝ×ℝ pairs), geometry, J, physics, miscellaneous

| ID | Statement | Kind | Source | Verdict |
|---|---|---|---|---|
| A206 | WheelTheory relation on `ℝ×ℝ`: `[a,b] ∼ [c,d] :⇔ ad = cb ∨ (b = 0 ∧ d = 0)`: reflexive, symmetric | PRV | `main:lean/WheelTheory.lean (c681d5cd)` | TRUE. |
| A207 | `wheel_equiv_trans`; `wheel_setoid` | SOR | c681d5cd | FALSE: `[1,1] ∼ [0,0] ∼ [2,1]` but `[1,1] ≁ [2,1]`. |
| A208 | `wheel_add_respects_equiv`, `wheel_mul_respects_equiv` | SOR | c681d5cd | TRUE (case analysis, brute-force checked), but moot because ∼ is not transitive. |
| A209 | Wheel "axioms" up to ∼ (`+` and `×` commutative and associative, `0ᵂ`, `1ᵂ` identities, `⁄⁄w ∼ w`, involution `⁄⁄w = w`), `wheel_distrib` for non-bottom elements | PRV | c681d5cd | TRUE (by `ring`). `wheel_distrib` even holds without the hypothesis, which shows ∼ is too coarse (it is not Carlström's wheel). |
| A210 | `wheel_to_extended` (denominator 0 ↦ I; otherwise a/b): `bottom_maps_to_I`, `wheel_div_zero_is_I`, `wheel_extends_fractions` | PRV | c681d5cd | TRUE. |
| A211 | "The I-wheel is Carlström's wheel; all `x/0` collapse to one I"; "Wheel `W(K_I, …)` is well-defined via equivalence classes"; BOTTLENECK "wheel axioms satisfied: distributivity; `a⊗(1⊘a) = 1` for a≠0" | INF | `main:docs/MATHEMATICAL_FRAMEWORK.md (7b3ff63d)`, `main:BOTTLENECK_CONSTANT_SPECIFICATION.md (7a5d95da)`, `main:src/python/ialgebra/wheel.py (7d28aefd)` | FALSE. In WHEEL `1/0 = ∞ ≠ ⊥ = 0/0`. The relation is not transitive (A207). For a = I: `I⊗(1⊘I) = I⊗0 = 0 ≠ 1`. Distributivity fails (A38). |
| A212 | Geometric locus: all `x/0` map to one point I, drawn at the origin (0,0) of the plane | DEF/INF | ec0987c9, 7d28aefd | NAP (I at the origin would clash with `I ≠ 0`). |
| A213 | **J = iI** (dual element from symmetry breaking) | DEF/INF | `main:book/main.tex (65be4134)`, `main:book/parts/part5/chapter28_field_theory.tex (8db7172b)`, IEA docs | FALSE against the KIJ table in both natural models. Under absorption over ℂ, `i·I = I`, so `J = I` (contradicts P8). In SET over ℂ, `J = iℝ ≠ ℝ`, but then `J⊗J = ℝ = I ≠ J` and `I⊕J = ℂ ≠ I`. |
| A214 | **J = 1/I** (reciprocal indeterminate) | DEF | 258c41ea, ac245181, `9e960ae8` | FALSE in every model given: `1⊘I = 0` (KIJ), `= I` (ABS, AEI, ZDIV). Conflicts with A213. |
| A215 | Physics: `ρ(0) = I`, `g₀₀(0) = I`, `ΔxΔp = I`, `friedmann_with_I`, Hawking `T = I`, `singularities_become_i`, `i_provides_consistency`, `vacuum_energy_indeterminate`, `planck_energy_indeterminate`, `quantum_foam_properties`, `information_in_i_regime`, `planck_scale_breakdown`, `singularity_regularization`; I-field Lagrangian/EOM; dark matter as a J-condensate; dark energy `= λv⁴/4`; LHC/GW predictions | DEF/PRV/AX/INF | `main:lean/PhysicalApplications.lean (ec97fde0)`, `main:lean/IAlgebra/Cosmology.lean (f1a8f976)`, `ae3f1b50`, `c130fde2`, `8db7172b`, `main:docs/PHYSICAL_INTERPRETATIONS.md (21e8de36)`, latex/sections/07_physics/* | The formal content is TRUE* ("quantity := I, therefore = I"). The physical hypotheses are NAP for this catalogue. |
| A216 | Physics math errors: (a) Cosmology axiom `continuity_equation : ∀ρ H t, HasDerivAt ρ (−3·H t·ρ t) t`; (b) Agda `sqrt-property : ∀x, sqrt x · sqrt x ≡ x`; (c) `energy_increases_with_momentum` (`p₁<p₂ ⇒ E(p₁)<E(p₂)`); (d) `gravitational_force_decreases` for arbitrary M; (e) ch28 "small oscillations around φ=0 have `m² = λv²`"; (f) `m_I = √(2λ)·v`; (g) `i_planck_length_relation`; (h) the Friedmann/Λ(t)/CEA positivity lemmas | AX/SOR/INF/PRV | f1a8f976, e80c38b4, `03066bb1`, ce16cd1e, 8db7172b | (a) FALSE (ρ ≡ 1, H ≡ 1 gives 0 = −3), so the file is inconsistent. (b) FALSE (x < 0). (c) FALSE (E depends on p², take p = −2, −1). (d) FALSE if `M·m_I ≤ 0`. (e) FALSE (`V''(0) = −λv²`, tachyonic). (f) TRUE. (g) TRUE. (h) TRUE. |
| A217 | Cryptography: "paired numbers reveal even-prime-like square roots"; keys "indecipherable without AEI theory"; I-flagged modular arithmetic | INF/DEF | `main:ialgebra/cryptography.py (3343efa9)` | NAP / FALSE: the key `(a XOR b)·ab` is a public function with no hardness. The modular structure `ℤ/n × ({0,1}, ∨)` is TRUE but trivial. |
| A218 | Ontology chapter: Quine–Putnam indispensability "theorem"; "explanatory indispensability"; "cost of omission"; "ontological thesis"; "realist explanation"; "epistemological limit"; "I as indeterminate abstract object" | INF | 2fe91255 | NAP. |
| A219 | "NaN comparisons are always false" | INF | 55417d03 | TRUE (IEEE 754 ordered comparisons; `≠` is true). |
| A220 | "`x+I = I` and `y+I = I` do not imply `x = y`" | INF | `main:lean/README.md`/docs | TRUE. |

---

## 3. Claims about the Millennium Prize problems

This repository makes almost no Millennium claims. None of the claims below is formalised, so none depends on an axiom or `sorry`. All are prose or code comments.

| ID | Problem | Claim | Source | Assessment |
|---|---|---|---|---|
| M1 | Riemann Hypothesis | `ζ_I(s) := ζ(s)` for s ≠ 1; `ζ_I(1) := I`; `ζ_I(I) := I`; "If `ζ(s) = I` has non-trivial zeros, they would lie on the critical line" | `main:book/parts/part7/appendix_A_function_atlas.tex (742ecc2b)` | NAP/vacuous. By the definition, `ζ_I(s) = I` only at s = 1 and s = I, neither of which is a zero, so the statement says nothing about RH. No proof is given and there is no formal counterpart. (`lemma_I_riemann_surface : ∀M, True` in nexus_core is vacuous.) |
| M2 | Navier–Stokes | Case-study code: `navier_stokes_extended` "continues through singularities" by marking `pressure == I` cells and interpolating from neighbours | `main:book/…/chapter33_extended_real_type.tex (55417d03)` | NAP: a numerical-engineering heuristic, not a statement about global existence or smoothness. |
| M3 | P vs NP | `inductive IComplexity \| O \| infinite \| indeterminate` ("undecidable complexity") | `ba30ccd4`, `04bf6527` | No claim (a datatype only). |
| M4 | Yang–Mills mass gap | ch28 "mass spectrum: `m_J = 0` (global symmetry) or `m_J > 0` (gauged)" for a scalar U(1) toy model | `8db7172b` | Not about Yang–Mills existence or the mass gap. Standard Goldstone/Higgs folklore (TRUE for the toy model). |
| M5 | Hodge, BSD, Poincaré | — | — | No mentions. ("Hodges" in `fafeccc9` is the model-theory author.) |

---

## 4. The most important laws that are TRUE, non-trivial, and worth proving in Lean 4 + Mathlib

The cleanest model is given for each law. Items 1–7 are model-free algebra and refute large parts of the corpus. Items 8–13 build the three useful concrete models. Items 14–21 are the analysis and model-theory content.

1. **The absorbing element is unique.** For any `Add`: if `∀x, a+x = a` and `∀x, b+x = b` then `a = b`. Abstract magma. (A28, A9)
2. **Absorbing identity ⇒ trivial.** In an `AddMonoid M`, `(∀x, I+x = I) → I = 0 → Subsingleton M`; the same for `Monoid` with `I = 1`. Abstract. (A19, A20)
3. **An absorbing element is incompatible with additive inverses.** In an `AddMonoid` (in particular an `AddGroup`), if `I+x = I` for all x and I has a right inverse, then `I = 0`. Hence P2+P4+P5+P12 ⊢ `I = 0`, so **PAX P1–P15 is inconsistent**. Abstract `AddGroup`. (A62, A78, A79)
4. **An idempotent unit equals 1.** In a `Monoid`, `IsIdempotentElem e → IsUnit e → e = 1`. Hence `I² = I`, `I ≠ 1` ⊢ `¬∃x, I·x = 1`, so P14 is derivable. Abstract `Monoid`. (A40, A66, A71)
5. **In a ring every idempotent `e ∉ {0,1}` is a zero divisor** (`e·(1−e) = 0`). Refutes the audit claim A73. Model `Ring`, witness `ℝ×ℝ`.
6. **Consistency of `{I² = I, I ≠ 0, I ≠ 1, ¬IsUnit I, I·0 = 0}` in a commutative ring.** Witness `I = (1,0) : ℝ×ℝ`; also: `x² = x` has exactly 4 solutions there. RING. (A69, A77)
7. **There is no linear order with strictly monotone `+` when a nonzero additive idempotent exists.** `LinearOrder` + `StrictMono (· + c)` ⇒ `I+I = I → I = 0`. Abstract. (A76, A177)
8. **ABS / common-meadow model.** Define `ℝ⊥ := Option ℝ` with `none` absorbing; `x/0 = none`. Prove: `AddCommMonoid`, `CommMonoid`, **both distributive laws for all elements**, `x − x = 0·x`, `0·⊥ = ⊥`, `x/0 = ⊥`, `⊥/x = x/⊥ = ⊥`. This is a consistent home for I4, I5, P3, P6, P7, the Tarski list A82, and the NexusField axioms (with `inv 0 = ⊥`). (A82, A84, A90, A95)
9. **NexusField forces `inv 0 = I` and `0·I = I`**, from N1, N2 and N15 alone. Consequently NexusField + P4 (`0·I = 0`) is inconsistent. Abstract structure. (A84, A86, A87)
10. **The WT model is Mathlib's `WithTop ℝ` arithmetic.** `⊤+x = ⊤`, `a≠0 → a·⊤ = ⊤`, `0·⊤ = 0`; `+` and `·` are associative and commutative; distributivity fails: `⊤·(1+(−1)) = 0 ≠ ⊤ = ⊤·1+⊤·(−1)`; `¬∃x, ⊤·x = 1`; `¬∃x, ⊤+x = 0`. This is the `{I}`-fragment of the 15-postulate K_I (P3, P4, P15, A37, A38, A40, A41). Mathlib `WithTop ℝ` with its `MulZeroClass` instance (or a custom inductive for the full KIJ with J).
11. **Characterisation in KIJ.** The unique x with `x⊕x = x ∧ x⊗x = x ∧ x⊖x = x ∧ x⊘x = x` is `x = I`. Custom inductive. (A50)
12. **SET model (`I := Set.univ : Set ℝ`, `open Pointwise`).** `{x}+I = I`; `x≠0 → {x}·I = I`; `{0}·I = {0}`; `I+I = I·I = I−I = I`; `0 ∈ I−I`; `1 ∈ I/I`; `I·({1}+{−1}) ⊊ I·{1}+I·{−1}` (only sub-distributivity, `Set.mul_add_subset`); `¬∃X, I·X = {1}`. One model satisfies P4 (`0·I = 0`), I4/I5 (for nonzero scalars), P6, P7 and the multistate claims at once, and it explains why distributivity must fail. (A30, A34, A157)
13. **CARD facts.** `⊕`, `⊗` are commutative and associative, `κ⊖κ = I`, and any `⊖`-homomorphism fixes I (already proved in Lean/Coq/Isabelle; port them). Plus the **refutations**: I3a fails at (κ,λ) = (0,1); "distributivity with I" fails at (0,2,1); `~_I` is not transitive on `ℕ∪{I}`. Custom inductive `ℕ ⊕ Unit`. (A4, A5, A10, A16, A17)
14. **0/0 is indeterminate (LIM).** `∀ L : EReal, ∃ f g : ℕ → ℝ, Tendsto f atTop (𝓝 0) ∧ Tendsto g atTop (𝓝 0) ∧ (∀n, g n ≠ 0) ∧ Tendsto (fun n ↦ ((f n / g n : ℝ) : EReal)) atTop (𝓝 L)`. This is the rigorous content of "I = 0/0" and refutes A165, A166, A168 and A169. Mathlib `EReal`, `Filter.Tendsto`.
15. **The other indeterminate forms are likewise indeterminate.** `∞ − ∞` can tend to any `L : EReal` (supports A138); `0·∞`, `1^∞`, `0^0` and `∞^0` can tend to any `L` in the appropriate range (`[0,∞]` for the power forms; A181). Mathlib `EReal`, `Real.rpow`.
16. (Harder, optional.) **Cluster sets.** Every nonempty closed subset of `EReal` is the cluster set of `f_n/g_n` for some `f, g → 0` with `g_n ≠ 0`. Mathlib `EReal` (compact), `MapClusterPt`.
17. **Continuity: the true version of A167/A176.** For any T1 topology on `ℝ ∪ {I}`, `(x,y) ↦ x⊘y` with `0⊘0 = I` is not continuous at (0,0). Yet `y ↦ 1⊘y` is continuous at 0 when I is identified with `∞ : OnePoint ℝ`. Also: the discrete topology makes every `⊘` continuous, so the corpus's "no topology" statements are false. Mathlib `OnePoint ℝ`, `T1Space`.
18. **Ultrapower facts refuting A193/A194.** In `Hyperreal = Germ (hyperfilter ℕ) ℝ`: `[a] − [a] = 0`, and the class of `(−1)^n`-type 0/1 oscillation is 0 or 1 (`Ultrafilter.em`). Mathlib `Hyperreal`, `Filter.Germ`.
19. **Łoś preservation of the I-axioms.** If a structure in the language `{⊕, ⊗, ⊖, I, 0}` satisfies the universal sentences I1, I4, I5, I7, so does every ultrapower (and every product, since they are universal Horn sentences). Mathlib `FirstOrder.Language.Ultraproduct` (`sentence_realize`). (A192, A196)
20. **AEI model facts (true statements refuting the file's claims).** `I·0 = 1`, so I is invertible and every nonzero element of `KI K` has a right inverse (KI_not_field is false); `·` is non-associative (`(0·I)·I = I ≠ 1 = 0·(I·I)`); f ≡ 0 is a `+`/`·`-homomorphism `KI K → K`. Custom inductive over a `Field K`. (A106–A111, A114)
21. **Meadow refutation of "I = 0 ⇒ 1 = 0".** Mathlib's `ℝ` satisfies `x/0 = 0` and `(0:ℝ) ≠ 1`; so "`1/0 = I` and `I = 0`" does not collapse anything without additive absorption. `div_zero`. (A55, A140)
22. **LP is non-explosive.** In `Fin 3` with K3 connectives and designated set `{T, I}`, the valuation `P ↦ I`, `Q ↦ F` makes `P ∧ ¬P` designated and Q not; under K3 designation `{T}`, explosion is valid. Small inductive. (A186)
23. **Uniqueness of I is false from the BOTTLENECK axioms.** In KIJ, J satisfies `J² = J`, `J+J = J`, `J ≠ 0,1`, `0·J = 0` but `J ≠ I`. Custom inductive (kernel decides it). (A81)

### Statements whose formalisation would make Lean prove `False` (do not import)

These are axioms that are false against their own file's definitions, or mutually inconsistent axiom sets:

- PAX P1–P15 (`lean/AlgebraI/Basic.lean`, `coq/theories/Basic.v`)
- IEA A3 (`lean/IEA.lean`, `coq/IEA.v`)
- `j_property` (`formalizations/lean/IAlgebra.lean`)
- Coq `ideriv_iexp`
- Coq AEI `non_associativity` and `suspended_distributivity`
- `extended_zeros_coherent` (ExtendedOperationsI)
- nexus_core `indeterminate_def`
- Lean CentralHypothesis `zero_mul_I`
- Isabelle FlexibleResolution `separation`
- Agda Wheel `absorption-property` and `wheel-equiv-trans` postulates
- Agda `sqrt-property`
- Lean Cosmology `continuity_equation`

---

## 5. Counts

There are 220 deduplicated rows (A1–A220). Each row is classified by the first verdict in its last column. About 15 rows have mixed sub-verdicts (for example "TRUE in model X, FALSE as a claim about Y"); the full text of those rows takes precedence over the count.

| Verdict | Rows |
|---|---|
| TRUE (substantive, in the stated model) | 95 |
| TRUE* (trivial or vacuous) | 32 |
| FALSE (counterexample or contradiction given) | 64 |
| NAP (ill-typed, vague, or not formalisable) | 18 |
| Pure definitions (no truth value: A29, A56, A101, A123, A132, A133, A142, A150, A156, A182, A185) | 11 |

Among the FALSE rows are 14 axioms or postulates that make their file inconsistent (see the list at the end of §4). There are also 5 Millennium items (M1–M5): none is a real claim and none is formalised.
