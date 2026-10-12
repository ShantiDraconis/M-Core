namespace ATK.Audit
/-- Auditoria: `SevenGates t` habitado ⟺ as sete metas (`t.all`, por definição). -/
theorem sevenGates_iff (t : ATK.SevenTargets) :
    Nonempty (ATK.SevenGates t) ↔ (t.RH ∧ t.NS ∧ t.YM ∧ t.BSD ∧ t.Hodge ∧ t.Beal ∧ t.PNP) :=
  ⟨fun ⟨g⟩ => g.close, fun ⟨h1, h2, h3, h4, h5, h6, h7⟩ =>
    ⟨⟨⟨True, True.intro, fun _ => h1⟩, ⟨True, True.intro, fun _ => h2⟩,
      ⟨True, True.intro, fun _ => h3⟩, ⟨True, True.intro, fun _ => h4⟩,
      ⟨True, True.intro, fun _ => h5⟩, ⟨True, True.intro, fun _ => h6⟩,
      ⟨True, True.intro, fun _ => h7⟩⟩⟩⟩
end ATK.Audit
