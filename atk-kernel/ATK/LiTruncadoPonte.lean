import ATK.LiTruncado
import ATK.ZeroClasses.LiCompleto
import ATK.ZeroClasses.Expoente

/-!
# ATK — Ponte entre as truncagens de Li e o `λₙ` completo (rodada 108)

`ATK.LiTrunc.liT T n` soma `Re(1 − (1 − 1/ρ)ⁿ)` sobre os zeros não triviais com `‖ρ‖ ≤ T`, cada zero uma vez;
`ATK.ZeroClasses.LiCompleto.lam n` é o coeficiente de Li verdadeiro (rodada 68), com multiplicidades e a soma
inteira. Sob RH toda parcela é `≥ 0`, logo **cada truncagem é cota inferior de `λₙ`** (`liT_le_lam`).

Leitura: somar os primeiros zeros (na reta) dá números positivos e crescentes em `T` — é a Lei 1 aplicada a pontos
que já estão no círculo `|w| = 1`. Isso não é evidência de `λₙ ≥ 0`: é consequência de supor os zeros na reta.

Classificação: **consequência**. RH continua `OPEN_MATH`.
-/

namespace ATK.LiTrunc.Ponte

open ATK.ZeroClasses.LiCompleto ATK.ZeroClasses.Canonico ATK.ZeroClasses.LagariasHadamard

/-- Um zero não trivial (no sentido do Mathlib) está na faixa `Z` do ATK. -/
theorem mem_Z_of_naoTrivial {s : ℂ} (h : NaoTrivial s) : s ∈ ATK.ZetaSimetria.Z :=
  (ATK.ZetaSimetria.mem_Z_iff_nao_trivial s).mpr ⟨h.1, h.2.1⟩

/-- A primeira cópia `(ρ, 0)` de um zero da truncagem. -/
noncomputable def copia (T : ℝ) : {ρ // ρ ∈ zerosAte T} ↪ ZM where
  toFun x := ⟨⟨x.1, mem_Z_of_naoTrivial (mem_zerosAte.mp x.2).1⟩,
    ⟨0, ATK.ZeroClasses.Expoente.ordem_pos (mem_Z_of_naoTrivial (mem_zerosAte.mp x.2).1)⟩⟩
  inj' := by
    intro x y hxy
    have := congrArg (fun q : ZM => ((q.1 : ATK.ZetaSimetria.Z) : ℂ)) hxy
    exact Subtype.ext this

/-- **Sob RH, `λₙ^{(T)} ≤ λₙ`** para toda altura `T`. -/
theorem liT_le_lam (hRH : RiemannHypothesis) (T : ℝ) (n : ℕ) : liT T n ≤ lam n := by
  have hnn : ∀ q : ZM, 0 ≤ termo n q := fun q => ATK.Li.rh_parcelas hRH q.1.2
  have e : liT T n = ∑ q ∈ (zerosAte T).attach.map (copia T), termo n q := by
    rw [Finset.sum_map]
    unfold liT liS
    rw [← Finset.sum_attach]
    rfl
  rw [e]
  exact Summable.sum_le_tsum _ (fun q _ => hnn q) (summable_termo n)

end ATK.LiTrunc.Ponte

#print axioms ATK.LiTrunc.Ponte.mem_Z_of_naoTrivial
#print axioms ATK.LiTrunc.Ponte.liT_le_lam
