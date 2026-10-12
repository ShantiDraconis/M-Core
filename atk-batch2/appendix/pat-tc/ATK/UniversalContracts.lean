namespace ATK.Audit.Contracts
open ATK.Universal

/-- RH: com `Converges` abstrato, o contrato aceita `Converges := fun _ => True` e `DN` qualquer;
`Producer` sozinho não carrega conteúdo analítico. -/
theorem rh_producer_vacuous :
    Nonempty (RH.Producer (fun n : Nat => (0 : Rat) / ((n : Rat) + 1)) (fun _ => True)) :=
  ⟨⟨0, by first | decide | exact Rat.le_refl | exact Rat.le_refl _ | simp,
      fun _ => by first | exact Rat.le_refl | exact Rat.le_refl _ | simp,
      fun _ => True.intro⟩⟩

theorem ns_producer_iff (I S : Type) [Nonempty S] (Adm : I → Prop) (Sol : I → S → Prop)
    (Reg : S → Prop) :
    Nonempty (NS.Producer I S Adm Sol Reg) ↔ NS.Target I S Adm Sol Reg := by
  classical
  constructor
  · intro ⟨p⟩
    exact NS.terminal I S Adm Sol Reg p
  · intro h
    refine ⟨⟨fun u => if hu : Adm u then Classical.choose (h u hu) else Classical.arbitrary S,
      ?_, ?_⟩⟩
    · intro u hu
      simp only [dif_pos hu]
      exact (Classical.choose_spec (h u hu)).1
    · intro u hu
      simp only [dif_pos hu]
      exact (Classical.choose_spec (h u hu)).2

theorem ym_producer_iff (T : Type) (Phys Gap : T → Prop) :
    Nonempty (YM.Producer T Phys Gap) ↔ YM.Target T Phys Gap :=
  ⟨fun ⟨p⟩ => YM.terminal T Phys Gap p,
   fun h => Exists.elim h (fun t ht => ⟨⟨t, ht.1, ht.2⟩⟩)⟩

theorem bsd_producer_iff (C : Type) (Adm R F : C → Prop) :
    Nonempty (BSD.Producer C Adm R F) ↔ BSD.Target C Adm R F :=
  ⟨fun ⟨p⟩ => BSD.terminal C Adm R F p,
   fun h => ⟨⟨fun e he => (h e he).1, fun e he => (h e he).2⟩⟩⟩

theorem hodge_producer_iff (V Cl Cy : Type) [Nonempty Cy] (SP : V → Prop)
    (HC : V → Cl → Prop) (Rep : V → Cy → Cl → Prop) :
    Nonempty (Hodge.Producer V Cl Cy SP HC Rep) ↔ Hodge.Target V Cl Cy SP HC Rep := by
  classical
  constructor
  · intro ⟨p⟩
    exact Hodge.terminal V Cl Cy SP HC Rep p
  · intro h
    refine ⟨⟨fun x a => if hxa : SP x ∧ HC x a then Classical.choose (h x a hxa.1 hxa.2)
      else Classical.arbitrary Cy, ?_⟩⟩
    intro x a hx ha
    have hxa : SP x ∧ HC x a := ⟨hx, ha⟩
    simp only [dif_pos hxa]
    exact Classical.choose_spec (h x a hx ha)

theorem beal_producer_iff (T : Type) (Cx : T → Prop) :
    Nonempty (Beal.Producer T Cx) ↔ Beal.Target T Cx :=
  ⟨fun ⟨p⟩ => Beal.terminal T Cx p, fun h => ⟨⟨fun t ht => h t ht⟩⟩⟩

theorem pnp_producer_iff (M : Type) (D P : M → Prop) :
    Nonempty (PNP.Producer M D P) ↔ PNP.Target M D P :=
  ⟨fun ⟨p⟩ => PNP.terminal M D P p, fun h => ⟨⟨fun m hd hp => h m hd hp⟩⟩⟩

/-- O contrato não fixa a semântica: com `PolynomialTime := fun _ => False` o alvo é trivial. -/
theorem pnp_target_vacuous : PNP.Target Unit (fun _ => True) (fun _ => False) :=
  fun _ _ h => h

end ATK.Audit.Contracts
