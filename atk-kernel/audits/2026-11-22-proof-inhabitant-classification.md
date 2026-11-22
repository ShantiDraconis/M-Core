# Audit of proof inhabitants, terminal roots and misclassified obligations (2026-11-22)

**Scope:** source inspection of `atk-kernel/ATK/FinalRoot.lean`, `ClosedMathReal.lean`, `StatusFinal.lean` and `ClosedMathCEZ.lean` on M-Core main. This is **not** a successful Lean build or a transitive axiom audit. Keep OPEN_MATH=true, CLOSED_MATH=false.

## Source-level findings

| Declaration | Actual source type / premises | Correct classification | Promotion |
|---|---|---|---|
| `ATK.FinalRoot.verde_fiel_iff` | `VerdeFiel ↔ IsEmpty ZeroFora ∧ ExclusaoResidualDescida`; no theorem parameters | **Unconditional equivalence**; neither side inhabited | Publish as equivalence only |
| `ATK.FinalRoot.rotas_RH` | Tuple of implications to RH and `RiemannHypothesis ↔ IsEmpty ZeroFora` | **Unconditional proof of implications/equivalence**, not RH | Publish with exact types |
| `ATK.FinalRoot.raiz_de_produtores` | `(hP : PontesRestantes M) (hO : Produtores M) : Raiz M` | **Conditional** terminal assembly; `hP` and `hO` are required inhabitants | Do not promote to final root |
| `ATK.FinalRoot.pontes_de_restantes` | `(hP : PontesRestantes M) : Bridges M` | Conditional bridge packaging; B1 supplied, remaining bridges assumed | Do not promote to terminal |
| `ATK.FinalRoot.verde_fiel_iff_final` | `(hFLT : FermatLastTheorem) (hDM : DarmonMerel) : ... ↔ ...` | Conditional equivalence | Require proof terms for both |
| `ATK.FinalRoot.ns_depende_do_modelo`, `pnp_depende_do_modelo` | Existence of toy models making parametric statements true and false | **Unconditional counterexamples to model-independent promotion** | Preserve as scope guard |
| `ATK.ClosedMathReal.closedMath_real` | `(L : Lacunas H Y) : ClosedMathRealAlvo H Y` | Conditional proof; `L` contains the target obligations | Do not promote |
| `ATK.ClosedMathReal.lacuna_rh_iff` | `RH.produtor ↔ RiemannHypothesis` | Unconditional equivalence, not a proof of either side | Preserve as circularity guard |
| `ATK.ClosedMathReal.lacuna_pnp_iff` | PNP producer iff real P≠NP | Unconditional equivalence, not P≠NP | Preserve |
| `ATK.CEZ.simetria_nao_basta` | Exists a symmetric function with off-line zero | Unconditional counterexample to symmetry-only strategy | Promote as negative result only |
| `ATK.CEZ.rh_iff_externa_vazia` | RH iff external zeta zero class empty | Unconditional equivalence | Not RH |
| `ATK.StatusFinal.open_math_true`, `closed_math_false` | Boolean inventory flags for `itemN` entries | Unconditional **status** results, not mathematical nonexistence of proofs | Preserve fail-closed |

## Terminal inhabitants and gaps

- `PontesRestantes M` is a **Prop structure**, not an inhabitant of itself. Its fields are unproved obligations until a concrete `hP : PontesRestantes M` is constructed.
- `Produtores M` similarly requires `hO : Produtores M`, including `hO.rh : IsEmpty ZeroFora`, itself equivalent to RH. No term of that type was found in the inspected `FinalRoot.lean`.
- `raiz_de_produtores` is a **function** from those two structures to `Raiz M`, not a closed term `Raiz M`.
- `Lacunas H Y` in `ClosedMathReal.lean` includes `rh : RH.produtor` and `pnp : PNP.produtorO4 ...`; the same file proves these equivalent to RH and P≠NP respectively. It would be circular to call an inhabitant of `Lacunas` a new unconditional proof without inspecting its construction.
- `StatusFinal.pontesProvadas` **does** contain explicit proof-bearing `itemT` entries for B1, B4, SAT∈NP, restricted FLT, finite zero count and a restricted Littlewood input. These are legitimate candidates for targeted build/axiom audit, **not seven final proofs**.
- `StatusFinal.obrigacoes` contains `itemN` for O1–O8; a separately found proof of a matching exact proposition should be inserted as `itemT` only after checking the *actual proof term*, transitive axioms and canonical type.
- `StatusFinal` explicitly marks O8 as a **shadow** of Yang–Mills, not a Clay-equivalent statement. Never promote this shadow to a Millennium result.

## Verification queue (not executed yet)

1. Run pinned `lake build ATK` on the correct nested project.
2. In a temporary audit module importing `ATK.FinalRoot`, `ATK.ClosedMathReal`, `ATK.StatusFinal`, `ATK.ClosedMathCEZ`, run `#check @...` and `#print axioms ...` for every candidate above.
3. Search all branches for actual *definitions* of inhabitants, not names: `def/theorem/instance ... : PontesRestantes M`, `... : Produtores M`, `... : Raiz M`, `... : Lacunas H Y`, `... : IsEmpty ZeroFora`, `... : RiemannHypothesis`. Review elaborated types and transitive imports.
4. Verify R01 `hwitness` and `htransfer` **separately**; no inspected term supplies them.
5. For any truly new unconditional inhabitant, create a separate minimal PR with full proof source, precise Mathlib statement, pinned toolchain, build logs and axiom footprint.

**Audit conclusion:** there are genuine unconditional **equivalences, implications, counterexamples and bookkeeping proofs** currently present, but **no verified unconditional final root** in the inspected modules. Do not conflate theorem closure with conclusion closure.
