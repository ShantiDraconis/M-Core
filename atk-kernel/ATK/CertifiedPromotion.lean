import ATK.StatusFinal

/-!
# Promotion gate for already certified bridge items

This module exposes the six existing kernel proof terms as a single certified
bridge registry. It does NOT promote any of the eight terminal obligations.

An item can only be promoted with a proof of its exact proposition, via
`ATK.StatusFinal.itemT`; the current terminal registry remains all `itemN`.
-/

namespace ATK.CertifiedPromotion

open ATK.StatusFinal

/-- The six exact bridge items already carry proofs. -/
theorem bridges_all_certified : ∀ i ∈ pontesProvadas, i.P :=
  pontesProvadas_validas

/-- The certified bridge registry is closed. -/
theorem bridge_registry_closed : closedMath pontesProvadas = true :=
  closed_pontes_true

/-- Closing the bridge registry does not change the terminal registry. -/
theorem terminal_registry_still_open
    (C : ATK.HodgeOficial.ConstrucoesHodge) :
    openMath (obrigacoes C) = true ∧ closedMath (obrigacoes C) = false :=
  ⟨open_math_true C, closed_math_false C⟩

end ATK.CertifiedPromotion

#print axioms ATK.CertifiedPromotion.bridges_all_certified
#print axioms ATK.CertifiedPromotion.bridge_registry_closed
#print axioms ATK.CertifiedPromotion.terminal_registry_still_open
