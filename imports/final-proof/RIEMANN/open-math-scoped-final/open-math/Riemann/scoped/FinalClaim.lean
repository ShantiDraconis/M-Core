import Riemann.frozen.vanishing_upper_bound_green_5c66f8dc

namespace Riemann.scoped

open MCore.RH.NB

/-- The only final scoped claim in this lane.
    It stops at DNLimit = 0 and does not claim RiemannHypothesis. -/
theorem FINAL_SCOPED_CLAIM
    (D : NBHilbertData)
    (rho : D.GeneratorFamily)
    (h : D.VanishingUpperBound rho) :
    D.DNLimit rho = 0 :=
  Riemann.frozen.vanishing_upper_bound_thm D rho h

#print axioms FINAL_SCOPED_CLAIM

end Riemann.scoped
