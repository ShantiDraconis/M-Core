import Theorems.Thm_fermat_last_theorem
import Mathlib.Data.Nat.Prime.Basic

/-!
# ATK — Beal sem hipóteses quando `mdc(x, y, z) ≥ 3`, pelo Último Teorema de Fermat

`anthropics/fermats-last-theorem` (commit `6e837e7`, Lean 4.33.1, Mathlib `v4.33.0`) prova
`fermat_last_theorem` só com os três axiomas padrão. Este subprojeto o compila **do código-fonte**
junto com as reduções de `atk-kernel/ATK/BealFermat.lean` (copiadas abaixo, com o mesmo texto de
`ATK.Conditional.Beal.BealConjecture`, porque o atk-kernel está em outra Mathlib):

* `fermat`: `FermatLastTheorem` da Mathlib, como teorema;
* `beal_de_mdc_ge_tres_incondicional`: Beal vale para todo triplo com `mdc(x, y, z) ≥ 3`;
* **`beal_iff_residual_incondicional`**: `BealConjecture ⟺ ResidualMdcAteDois`, sem hipóteses.

O resíduo (`mdc ∈ {1, 2}`) é a obrigação O2, aberta. **Nada aqui prova Beal.**

Custo: o projeto da Anthropic tem 60 474 módulos (≈ 530 h de CPU, até 36 GB de memória num só
módulo, ≈ 300 GB de disco durante o build). O workflow `atk-fermat.yml` é manual e pede uma
máquina própria (runner auto-hospedado); o CI hospedado do GitHub não comporta.
-/

/-- Enunciado oficial (mesmo texto de `ATK.Conditional.Beal.BealConjecture`). -/
def BealConjecture : Prop :=
  ∀ a b c x y z : ℕ, 0 < a → 0 < b → 0 < c → 2 < x → 2 < y → 2 < z →
    a ^ x + b ^ y = c ^ z → ∃ p : ℕ, p.Prime ∧ p ∣ a ∧ p ∣ b ∧ p ∣ c

namespace ATK.Fermat

/-- Beal para um triplo fixo de expoentes. -/
def BealFor (x y z : ℕ) : Prop :=
  ∀ a b c : ℕ, 0 < a → 0 < b → 0 < c →
    a ^ x + b ^ y = c ^ z → ∃ p : ℕ, p.Prime ∧ p ∣ a ∧ p ∣ b ∧ p ∣ c

/-- O resíduo de Beal depois de FLT: triplos com `mdc(x, y, z) ≤ 2`. -/
def ResidualMdcAteDois : Prop :=
  ∀ x y z : ℕ, 2 < x → 2 < y → 2 < z → Nat.gcd x (Nat.gcd y z) ≤ 2 → BealFor x y z

theorem beal_iff_forall_bealFor :
    BealConjecture ↔ ∀ x y z : ℕ, 2 < x → 2 < y → 2 < z → BealFor x y z :=
  ⟨fun h x y z hx hy hz a b c ha hb hc heq => h a b c x y z ha hb hc hx hy hz heq,
    fun h a b c x y z ha hb hc hx hy hz heq => h x y z hx hy hz a b c ha hb hc heq⟩

/-- Se `d` divide os três expoentes e vale FLT(d), **não há solução alguma**. -/
theorem sem_solucao_de_divisor {d a b c x y z : ℕ} (hF : FermatLastTheoremFor d)
    (hx : d ∣ x) (hy : d ∣ y) (hz : d ∣ z) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    a ^ x + b ^ y ≠ c ^ z := by
  obtain ⟨r, rfl⟩ := hx
  obtain ⟨s, rfl⟩ := hy
  obtain ⟨t, rfl⟩ := hz
  intro heq
  apply hF (a ^ r) (b ^ s) (c ^ t) (pow_ne_zero _ ha.ne') (pow_ne_zero _ hb.ne')
    (pow_ne_zero _ hc.ne')
  rw [← pow_mul, ← pow_mul, ← pow_mul, mul_comm r d, mul_comm s d, mul_comm t d]
  exact heq

/-- Forma via `mdc(x, y, z)`. -/
theorem sem_solucao_mdc {d a b c x y z : ℕ} (hF : FermatLastTheoremFor d)
    (h : d ∣ Nat.gcd x (Nat.gcd y z)) (ha : 0 < a) (hb : 0 < b) (hc : 0 < c) :
    a ^ x + b ^ y ≠ c ^ z :=
  sem_solucao_de_divisor hF (h.trans (Nat.gcd_dvd_left _ _))
    (h.trans ((Nat.gcd_dvd_right _ _).trans (Nat.gcd_dvd_left _ _)))
    (h.trans ((Nat.gcd_dvd_right _ _).trans (Nat.gcd_dvd_right _ _))) ha hb hc

/-- **Com FLT, Beal vale para todo triplo com `mdc(x, y, z) ≥ 3`** (não há soluções). -/
theorem beal_de_mdc_ge_tres (hF : FermatLastTheorem) {x y z : ℕ}
    (h : 3 ≤ Nat.gcd x (Nat.gcd y z)) : BealFor x y z :=
  fun _ _ _ ha hb hc heq => absurd heq (sem_solucao_mdc (hF _ h) dvd_rfl ha hb hc)

/-- **Com FLT, Beal ⟺ o resíduo `mdc(x, y, z) ≤ 2`.** -/
theorem beal_iff_residual (hF : FermatLastTheorem) :
    BealConjecture ↔ ResidualMdcAteDois := by
  rw [beal_iff_forall_bealFor]
  constructor
  · exact fun h x y z hx hy hz _ => h x y z hx hy hz
  · intro h x y z hx hy hz
    by_cases hd : Nat.gcd x (Nat.gcd y z) ≤ 2
    · exact h x y z hx hy hz hd
    · exact beal_de_mdc_ge_tres hF (by omega)

/-- O resíduo segue de Beal (a redução não pede mais do que Beal). -/
theorem residual_de_beal (h : BealConjecture) : ResidualMdcAteDois :=
  fun x y z hx hy hz _ => beal_iff_forall_bealFor.mp h x y z hx hy hz

/-- O `mdc` de expoentes maiores que 2 nunca é 0: o resíduo é `mdc ∈ {1, 2}`. -/
theorem mdc_pos {x y z : ℕ} (hx : 2 < x) : 0 < Nat.gcd x (Nat.gcd y z) :=
  Nat.gcd_pos_of_pos_left _ (by omega)


/-- **O Último Teorema de Fermat** (Anthropic), no enunciado da Mathlib. -/
theorem fermat : FermatLastTheorem := fun n hn a b c ha hb hc =>
  fermat_last_theorem n hn a b c (Nat.pos_of_ne_zero ha) (Nat.pos_of_ne_zero hb)
    (Nat.pos_of_ne_zero hc)

/-- **Beal vale para todo triplo com `mdc(x, y, z) ≥ 3`**, sem hipóteses. -/
theorem beal_de_mdc_ge_tres_incondicional {x y z : ℕ} (h : 3 ≤ Nat.gcd x (Nat.gcd y z)) :
    BealFor x y z :=
  beal_de_mdc_ge_tres fermat h

/-- **Beal ⟺ o resíduo `mdc(x, y, z) ≤ 2`**, sem hipóteses. -/
theorem beal_iff_residual_incondicional : BealConjecture ↔ ResidualMdcAteDois :=
  beal_iff_residual fermat

end ATK.Fermat

#print axioms fermat_last_theorem
#print axioms ATK.Fermat.fermat
#print axioms ATK.Fermat.sem_solucao_mdc
#print axioms ATK.Fermat.beal_de_mdc_ge_tres
#print axioms ATK.Fermat.beal_iff_residual
#print axioms ATK.Fermat.beal_de_mdc_ge_tres_incondicional
#print axioms ATK.Fermat.beal_iff_residual_incondicional
