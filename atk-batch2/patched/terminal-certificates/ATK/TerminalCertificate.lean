import ATK.UniversalContracts
/-! Structural certificate: no claims about the seven open conjectures are discharged here. -/

namespace ATK.Certificate

structure ProofCertificate (target : Prop) where
  Material : Prop
  inhabitant : Material
  bridge : Material → target

theorem verify {target : Prop} (c : ProofCertificate target) : target :=
  c.bridge c.inhabitant

theorem seven_verify
    {R N Y B H E P : Prop}
    (r : ProofCertificate R) (n : ProofCertificate N)
    (y : ProofCertificate Y) (b : ProofCertificate B)
    (h : ProofCertificate H) (e : ProofCertificate E)
    (p : ProofCertificate P) :
    R ∧ N ∧ Y ∧ B ∧ H ∧ E ∧ P :=
  ⟨verify r, verify n, verify y, verify b, verify h, verify e, verify p⟩

-- This proves only the correctness of the certificate composition.
-- The seven concrete certificates must be provided independently.
#print axioms ATK.Certificate.verify
#print axioms ATK.Certificate.seven_verify
end ATK.Certificate
