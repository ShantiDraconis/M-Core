namespace ATK.Audit
/-- Auditoria: ter uma `Lane P` é exatamente ter uma prova de `P` (o campo `material` não reduz a obrigação). -/
theorem lane_iff (P : Prop) : Nonempty (ATK.Lane P) ↔ P :=
  ⟨fun ⟨l⟩ => ATK.lane_closes l, fun p => ⟨⟨True, True.intro, fun _ => p⟩⟩⟩
end ATK.Audit
