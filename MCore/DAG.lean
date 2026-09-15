import MCore.A2SelfRef

namespace MCore

/-- Explicit dependency fixture used only to prove that the audit gate catches
its forbidden G1/G4 feedback. -/
def forbiddenFixture : Graph :=
  [(.g1, .g4), (.g4, .g1), (.I, .coeffA), (.coeffA, .targetY), (.targetY, .I)]

/-- Obligation 15: the canonical I -> a -> Y -> I feedback is present. -/
theorem forbiddenFixture_hasCanonicalSelfRef :
    HasCanonicalSelfRef forbiddenFixture := by
  simp [forbiddenFixture, HasCanonicalSelfRef, HasEdge]

/-- Therefore the self-reference gate rejects the fixture. -/
theorem forbiddenFixture_rejected :
    ¬ PassesSelfRefGate forbiddenFixture := by
  simpa [PassesSelfRefGate] using forbiddenFixture_hasCanonicalSelfRef

/-- A clean downstream graph contains no target-to-coefficient feedback. -/
def downstreamFixture : Graph := [(.g1, .coeffA), (.coeffA, .g4)]

theorem downstreamFixture_passes : PassesSelfRefGate downstreamFixture := by
  simp [PassesSelfRefGate, HasCanonicalSelfRef, HasEdge, downstreamFixture]

end MCore
