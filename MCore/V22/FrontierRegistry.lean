import MCore.V22.Operators

namespace MCore.V22

inductive FrontierKind where
  | algebraicityWitnessConstructor
  | rankWitnessConstructor
  | commonPrimeWitnessConstructor
  | materialOrientation
  | classicalSemanticAdapter
  | concreteTheoryAdapter
  | uniformizationBridge
  | noneClosedControl
  deriving DecidableEq, Repr

inductive IntegrationStatus where
  | candidateBranch
  | integrated
  deriving DecidableEq, Repr

structure FrontierRecord where
  problem : ProblemId
  proofState : ProofState
  frontier : FrontierKind
  sourceRepo : String
  sourceRevision : String
  integration : IntegrationStatus
  deriving Repr

def primaryFrontiers : List FrontierRecord :=
  [
    { problem := .hodge
      proofState := .open
      frontier := .algebraicityWitnessConstructor
      sourceRepo := "ShantiDraconis/m-core-hodge"
      sourceRevision := "337ac80fa5e500029790c59ab501317fa10846c8"
      integration := .candidateBranch },
    { problem := .bsd
      proofState := .open
      frontier := .rankWitnessConstructor
      sourceRepo := "ShantiDraconis/m-core-bsd"
      sourceRevision := "f98be3a7f6dccdb01aa09fa83915cef97c85adfa"
      integration := .candidateBranch },
    { problem := .beal
      proofState := .open
      frontier := .commonPrimeWitnessConstructor
      sourceRepo := "ShantiDraconis/m-core-beal"
      sourceRevision := "ccf054d669b269b09f3b65f840ac2745daf4e821"
      integration := .candidateBranch },
    { problem := .pVsNP
      proofState := .open
      frontier := .materialOrientation
      sourceRepo := "ShantiDraconis/m-core-p-vs-np"
      sourceRevision := "969408f2d84121667319da04680893dd2978e9a6"
      integration := .candidateBranch },
    { problem := .riemann
      proofState := .open
      frontier := .classicalSemanticAdapter
      sourceRepo := "ShantiDraconis/m-core-riemann"
      sourceRevision := "21216ff1141f97921aeddb3708fee0bfea05fd14"
      integration := .candidateBranch },
    { problem := .yangMills
      proofState := .open
      frontier := .concreteTheoryAdapter
      sourceRepo := "ShantiDraconis/m-core-yang-mills"
      sourceRevision := "2b401f28942221beb36256b9d8ce9c44cc2b9c6d"
      integration := .candidateBranch },
    { problem := .navierStokes
      proofState := .open
      frontier := .uniformizationBridge
      sourceRepo := "ShantiDraconis/navier-stokes-critical-barrier-audit"
      sourceRevision := "b71bb67298daf0ff2c414a3b3812f780d01c18e5"
      integration := .candidateBranch },
    { problem := .poincare
      proofState := .provedTrue
      frontier := .noneClosedControl
      sourceRepo := "classical-reference"
      sourceRevision := "closed-control"
      integration := .integrated }
  ]

theorem primary_frontier_count :
    primaryFrontiers.length = 8 := by rfl

end MCore.V22
