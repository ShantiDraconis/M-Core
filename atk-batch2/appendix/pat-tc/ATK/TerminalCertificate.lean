namespace ATK.Audit
/-- Auditoria: `ProofCertificate P` habitado ⟺ `P`. -/
theorem certificate_iff (P : Prop) : Nonempty (ATK.Certificate.ProofCertificate P) ↔ P :=
  ⟨fun ⟨c⟩ => ATK.Certificate.verify c, fun p => ⟨⟨True, True.intro, fun _ => p⟩⟩⟩
end ATK.Audit
