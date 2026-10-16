/-
Core definitions for Unified Millennium Invariants framework.
-/

import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.Matrix.Hermitian

-- Abstract Hilbert space for test functions
structure TestSpace where
  carrier : Type*
  [hilbert : InnerProductSpace ℝ carrier]
  scale : ℝ
  scale_pos : 0 < scale

-- Abstract linear operator
structure LinearOp (X : Type*) [InnerProductSpace ℝ X] where
  apply : X → X
  linear : ∀ (a b : ℝ) (x y : X), apply (a • x + b • y) = a • apply x + b • apply y

-- Projection operator
structure ProjectionOp (X : Type*) [InnerProductSpace ℝ X] extends LinearOp X where
  idempotent : ∀ x, apply (apply x) = apply x
  selfAdjoint : ∀ x y, ⟪apply x, y⟫_ℝ = ⟪x, apply y⟫_ℝ

-- Renormalized invariant as liminf of scale-dependent quantities
noncomputable def RenormalizedInvariant (scaleFn : ℝ → ℝ) : ℝ :=
  Filter.liminf scaleFn Filter.atTop

-- Admissibility axioms
structure AdmissibleSystem (X : Type*) [InnerProductSpace ℝ X] where
  testSpace : ℝ → TestSpace
  projection : ∀ T, ProjectionOp X
  kernel : ∀ T, LinearOp X
  positivity : ∀ T x, 0 ≤ ⟪kernel T |>.apply x, x⟫_ℝ
  stability : ∃ C, ∀ T₁ T₂, T₁ ≤ T₂ → 
    |RenormalizedInvariant (fun T => ⟪kernel T |>.apply x, x⟫_ℝ / ⟪x, x⟫_ℝ)| ≤ C
