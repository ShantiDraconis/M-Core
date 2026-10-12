# Certificado ATK v2 — ShantiDraconis/M-Core

- Commit verificado: `cfa675c8239340f38bafb11eab2bcc292ffe4195` (tag `atk-kernel-cert-v2`)
- Gerado em: 2026-10-12T00:46:12+00:00
- Teoremas aceitos pelo kernel: **63/64**

## ATK kernel check
- Execução: https://github.com/ShantiDraconis/M-Core/actions/runs/38188849574
- Lean (version 4.34.1, x86_64-unknown-linux-gnu, commit 5045d0056413266e57c625dcd7c365b10e377c52, Release)
- SHA-256 das fontes: `7da370de725a98729488e0ac7ce9cc2b38b1b7c32807b94f1f5aacaae331fadd`
- Job “RH — D_N real (Nyman–Beurling / Báez-Duarte)”: success
- Job “Lean 4 + Mathlib — compilação e auditoria de axiomas”: success

## ATK legacy kernel check
- Execução: https://github.com/ShantiDraconis/M-Core/actions/runs/38185584477
- Job “Arquivos Lean originais (v4.21.0) — kernel e axiomas”: success

| Teorema | Veredito | Axiomas |
|---|---|---|
| `ATK.PvsNP.p_ne_np_of_np_not_subset_ppoly` | ✅ CERTIFIED  | nenhum |
| `ATK.PvsNP.p_ne_np_of_sat` | ✅ CERTIFIED  | nenhum |
| `ATK.NavierStokes.absorption` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.absorption_margin_pos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.riccati_comparison` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.riccati_upper_bound` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NavierStokes.absorption_without_remainder_forces_decay` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.NSControl.weighted_energy_control` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.LogicAudit.rh_material_vacuous` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.LogicAudit.pnp_material_vacuous` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.pnp_separation_schema_true` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.pnp_separation_schema_false` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.beal_descent_without_wellfoundedness` | ✅ CERTIFIED  | propext, Quot.sound |
| `ATK.LogicAudit.ym_material_vacuous` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.bsd_material_vacuous` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.bsd_rank_target_true_instance` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.bsd_rank_target_false_instance` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.hodge_material_vacuous` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.hodge_schema_true_instance` | ✅ CERTIFIED  | nenhum |
| `ATK.LogicAudit.hodge_schema_false_instance` | ✅ CERTIFIED  | nenhum |
| `ATK.Hodge.linear_realization` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Hodge.realization_unique` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Geometry.round_sphere_scalar_integral` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BealDescent.no_primitive_of_descent` | ✅ CERTIFIED  | propext |
| `ATK.BealDescent.beal_of_descent` | ✅ CERTIFIED  | propext, Quot.sound |
| `ATK.BealDescent.descent_of_beal` | ✅ CERTIFIED  | propext, Quot.sound |
| `ATK.BealDescent.descent_iff_beal` | ✅ CERTIFIED  | propext, Quot.sound |
| `ATK.YangMills.weighted_cauchy_schwarz` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.YangMills.effective_mass_slope_nonpos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Beal.exponent_gcd_le_two` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.residual_tendsto_zero` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.schur_step_monotone` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.gram_complete_square` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.gram_residual_le` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.abstract_bound_vacuous` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.bdDistSq_nonneg` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.bd_bound_tendsto` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.Riemann.rh_of_bd_bound` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.regulator_det_identity` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.regulator_two_pos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.sha_recovery` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.torsion_contains_zero` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.BSD.torsion_card_pos` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.RHConvergence.bdDistSq_succ_le` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.RHConvergence.bdDistSq_antitone` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.RHConvergence.bdDistSq_converges` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.RHConvergence.bdDistSq_limit_nonneg` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
| `ATK.RHConvergence.rh_iff_limit_zero_of_criterion` | ✅ CERTIFIED  | propext, Classical.choice, Quot.sound |
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
