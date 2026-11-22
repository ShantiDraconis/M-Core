import ATK.StatusFinal

/-!
# Exact-witness global closure gate

This file specifies the *necessary evidence* to change the terminal flags.
It does not claim that the evidence exists. The current registry stays open.
-/

namespace ATK.GlobalClosureGate

open ATK.StatusFinal ATK.Termos

/-- Exact witnesses for all eight registered terminal propositions. -/
structure TerminalWitnesses (C : ATK.HodgeOficial.ConstrucoesHodge) : Prop where
  o1 : RH.produtor
  o2 : Beal.produtor
  o3 : NS.produtorO3 ATK.LigacaoNS.modeloNS
  o4 : PNP.produtorO4 ATK.ModeloPNP.modeloPNP ATK.ModeloPNP.SAT
  o5 : Hodge.produtorO5 (ATK.HodgeOficial.modelo C)
  o6 : BSD.produtorO6 ATK.BSDRefinada.modeloCompleto
  o7 : BSD.produtorO7 ATK.BSDRefinada.modeloCompleto
  o8 : ATK.YMOficial.YMNucleo

/-- Build the proof-carrying registry, not a manually toggled boolean. -/
def certifiedObligations (C : ATK.HodgeOficial.ConstrucoesHodge)
    (h : TerminalWitnesses C) : List Item :=
  [ itemT "O1 Riemann" RH.produtor h.o1,
    itemT "O2 Beal" Beal.produtor h.o2,
    itemT "O3 Navier–Stokes" (NS.produtorO3 ATK.LigacaoNS.modeloNS) h.o3,
    itemT "O4 P ≠ NP" (PNP.produtorO4 ATK.ModeloPNP.modeloPNP ATK.ModeloPNP.SAT) h.o4,
    itemT "O5 Hodge" (Hodge.produtorO5 (ATK.HodgeOficial.modelo C)) h.o5,
    itemT "O6 BSD posto" (BSD.produtorO6 ATK.BSDRefinada.modeloCompleto) h.o6,
    itemT "O7 BSD refinada" (BSD.produtorO7 ATK.BSDRefinada.modeloCompleto) h.o7,
    itemT "O8 Yang–Mills" ATK.YMOficial.YMNucleo h.o8 ]

theorem closed_of_exact_witnesses
    (C : ATK.HodgeOficial.ConstrucoesHodge) (h : TerminalWitnesses C) :
    closedMath (certifiedObligations C h) = true := rfl

theorem not_open_of_exact_witnesses
    (C : ATK.HodgeOficial.ConstrucoesHodge) (h : TerminalWitnesses C) :
    openMath (certifiedObligations C h) = false := rfl

/-- The actual current registry is still open until witnesses are supplied. -/
theorem current_registry_not_closed
    (C : ATK.HodgeOficial.ConstrucoesHodge) :
    openMath (obrigacoes C) = true ∧ closedMath (obrigacoes C) = false :=
  ⟨open_math_true C, closed_math_false C⟩

end ATK.GlobalClosureGate

#print axioms ATK.GlobalClosureGate.closed_of_exact_witnesses
#print axioms ATK.GlobalClosureGate.not_open_of_exact_witnesses
#print axioms ATK.GlobalClosureGate.current_registry_not_closed
