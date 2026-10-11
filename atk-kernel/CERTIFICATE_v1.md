# Certificado ATK v1 — ShantiDraconis/M-Core

- Commit verificado: `97ddae72520d9f10a5472cf6d373a601c09f6ce4` (tag `atk-kernel-cert-v1`)
- Gerado em: 2026-10-11T23:51:07+00:00
- Teoremas aceitos pelo kernel: **41/42**

## ATK kernel check
- Execução: https://github.com/ShantiDraconis/M-Core/actions/runs/38185049186
- Lean (version 4.34.1, x86_64-unknown-linux-gnu, commit 5045d0056413266e57c625dcd7c365b10e377c52, Release)
- SHA-256 das fontes: `1a89b11b8964b727daf033238b49994680ddb52f484433ae9d7c17fbe3ccda75`
- Job “Lean 4 + Mathlib — compilação e auditoria de axiomas”: success
- Job “RH — D_N real (Nyman–Beurling / Báez-Duarte)”: success

## ATK legacy kernel check
- Execução: https://github.com/ShantiDraconis/M-Core/actions/runs/38185584477
- Job “Arquivos Lean originais (v4.21.0) — kernel e axiomas”: success

| Teorema | Veredito | Axiomas |
|---|---|---|
| `ATK.YangMills.weighted_cauchy_schwarz` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.YangMills.effective_mass_slope_nonpos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.residual_tendsto_zero` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.schur_step_monotone` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.gram_complete_square` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.gram_residual_le` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.abstract_bound_vacuous` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.bdDistSq_nonneg` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.bd_bound_tendsto` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.rh_of_bd_bound` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.PvsNP.p_ne_np_of_np_not_subset_ppoly` | ✅ CERTIFIED  | nenhum |
| `ATK.PvsNP.p_ne_np_of_sat` | ✅ CERTIFIED  | nenhum |
| `ATK.NavierStokes.absorption` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.absorption_margin_pos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.riccati_comparison` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.riccati_upper_bound` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.absorption_without_remainder_forces_decay` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Hodge.linear_realization` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Hodge.realization_unique` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Geometry.round_sphere_scalar_integral` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Beal.exponent_gcd_le_two` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.regulator_det_identity` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.regulator_two_pos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.sha_recovery` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.torsion_contains_zero` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.torsion_card_pos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.hodge_linear_realization` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATKExactValues.absorption` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.rh_finite_decrement` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.rh_ratio` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.rh_relative_reduction` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.rh_schur_nonnegative` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.rh_schur_antitone` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.ns_margin_example` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.ns_budget_example` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.ns_budget_identity` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.ns_margin_positive` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.ns_bulk_tail_bound` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.bsd_regulator_example` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.bsd_regulator_identity` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.bsd_recover_h22` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.VerifiedAuxiliary.hodge_linear_realization` | ❌ NOT_CERTIFIED sem saída de #print axioms (não elaborado) | — |

Lemas auxiliares e cálculos concretos. Nenhuma das sete conjecturas foi provada; OPEN_MATH=true.
