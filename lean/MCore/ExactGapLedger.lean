import MCore.ResolutionPredicate
import MCore.FinalFail.ExactGapLedger

namespace MCore.ExactGap

def status : String :=
  "8/8 pinned including Poincare positive control; seven unsolved prize endpoints remain OPEN_MATH"

def sourceOfTruth : String :=
  "MCore.FinalFail.exactGaps"

theorem seven_open_final_problems :
    MCore.FinalFail.openFinalProblems = 7 :=
  MCore.FinalFail.openFinalProblems_eq_seven

end MCore.ExactGap
