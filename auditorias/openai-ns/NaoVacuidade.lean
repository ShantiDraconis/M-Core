import NavierStokes.ComparatorDefinitions

/-!
# Auditoria independente: o enunciado (C) não é vácuo

Com as definições do desafio (idênticas às da Formal Conjectures), o dado nulo `u₀ = 0`, `f = 0` é admissível
e tem solução global suave de energia limitada (`v = 0`, `p = 0`). Logo a classe de soluções não é vazia e
"não existe solução" é uma propriedade genuína de um dado específico, não um artefato das definições.
-/

open ContDiff Set InnerProductSpace MeasureTheory
open scoped Laplacian

namespace NavierStokes.Comparator

local notation "ℝ³" => EuclideanSpace ℝ (Fin 3)

theorem dado_nulo_admissivel :
    InitialVelocityConditionDecay (0 : ℝ³ → ℝ³) ∧ ForceConditionDecay (fun (_ : ℝ³) (_ : ℝ) => (0 : ℝ³)) := by
  refine ⟨⟨⟨fun x => by simp, contDiff_const⟩, fun m K => ⟨0, fun x => ?_⟩⟩,
    ⟨⟨contDiffOn_const⟩, fun m K => ⟨0, fun x t _ => ?_⟩⟩⟩
  · rw [show (0 : ℝ³ → ℝ³) = fun _ => 0 from rfl]
    rcases Nat.eq_zero_or_pos m with rfl | hm
    · simp
    · rw [iteratedFDeriv_const_of_ne (Nat.pos_iff_ne_zero.mp hm)]
      simp
  · have : (↿(fun (_ : ℝ³) (_ : ℝ) => (0 : ℝ³))) = fun _ => (0 : ℝ³) := rfl
    rw [this]
    rcases Nat.eq_zero_or_pos m with rfl | hm
    · simp
    · rw [iteratedFDerivWithin_const_of_ne (Nat.pos_iff_ne_zero.mp hm)]
      simp

theorem dado_nulo_tem_solucao (nu : ℝ) :
    ∃ v p, NavierStokesExistenceAndSmoothnessRn nu (0 : ℝ³ → ℝ³) (fun _ _ => 0) v p := by
  refine ⟨fun _ _ => 0, fun _ _ => 0, ⟨⟨?_, ?_, fun x => rfl, contDiffOn_const, contDiffOn_const⟩, ?_, ⟨1, ?_⟩⟩⟩
  · intro x t _
    have hl : Δ (fun _ : ℝ³ => (0 : ℝ³)) x = 0 := by rw [InnerProductSpace.laplacian_const]; rfl
    simp [hl, gradient]
  · intro x t _
    simp
  · intro t _
    simp
  · intro t _
    simp

end NavierStokes.Comparator

#print axioms NavierStokes.Comparator.dado_nulo_admissivel
#print axioms NavierStokes.Comparator.dado_nulo_tem_solucao
