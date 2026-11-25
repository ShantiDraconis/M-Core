import ATK.Conditional

/-!
# ATK — Estrutura para CLOSED_MATH (teorema-mestre, obrigações e firewall)

`CLOSED_MATH` = os 7 enunciados provados. Este arquivo NÃO os prova; ele fixa exatamente o
que falta:

  `closedMath_of_obligations : Bridges M → OpenObligations M → SevenStatements M`

* `Bridges` — 7 leis-ponte: teoremas publicados, ainda não formalizados na Mathlib.
* `OpenObligations` — 8 obrigações abertas (`OPEN_MATH`).
* Para os 5 enunciados paramétricos (NS, P vs NP, Hodge, BSD, YM) existe ainda a obrigação de
  LIGAÇÃO: construir o modelo `M` a partir dos objetos reais. Sem ela, `SevenStatements M` não diz
  nada — `ns_toy_model_vacuous` e `pnp_toy_model_vacuous` provam o enunciado em modelos de
  brinquedo, exatamente para mostrar isso.

O portão: `CLOSED_MATH` só vira `true` no auditor se existir `ATK/ClosedMathGate.lean` com
`theorem closed_math` SEM hipóteses, certificado (axiomas padrão, sem `sorry`/`axiom`), sobre os
modelos genuínos. Hoje esse arquivo não existe.
-/

namespace ATK.ClosedMath

/-- Os modelos dos 5 enunciados paramétricos (universos fixados em `Type`). -/
structure Models where
  ns : ATK.Conditional.NavierStokes.NSModel.{0}
  cx : ATK.Conditional.PvsNP.ComplexityModel.{0}
  sat : cx.Lang
  hodge : ATK.Conditional.Hodge.HodgeModel.{0, 0}
  bsd : ATK.Conditional.BSD.BSDModel.{0}
  ym : ATK.Conditional.YangMills.YMModel.{0, 0, 0}

/-- CLOSED_MATH: os 7 enunciados juntos. -/
def SevenStatements (M : Models) : Prop :=
  RiemannHypothesis ∧
  ATK.Conditional.Beal.BealConjecture ∧
  ATK.Conditional.NavierStokes.ClayStatementA M.ns ∧
  ATK.Conditional.PvsNP.PneNP M.cx ∧
  ATK.Conditional.Hodge.HodgeConjecture M.hodge ∧
  ATK.Conditional.BSD.BSDFull M.bsd ∧
  ATK.Conditional.YangMills.ClayYM M.ym

/-- As 7 leis-ponte (literatura publicada; obrigação: formalizar). -/
structure Bridges (M : Models) : Prop where
  baezDuarte : ATK.Conditional.Riemann.BaezDuarteCriterion
  fermat : FermatLastTheorem
  leray : ATK.Conditional.NavierStokes.EnstrophyBlowupCriterion M.ns
  cookLevin : ATK.Conditional.PvsNP.CookLevin M.cx M.sat
  lefschetz : ATK.Conditional.Hodge.KnownCases M.hodge
  grossZagierKolyvagin : ATK.Conditional.BSD.GrossZagierKolyvagin M.bsd
  osterwalderSchrader : ATK.Conditional.YangMills.OSReconstruction M.ym

/-- As 8 obrigações abertas (`OPEN_MATH`). -/
structure OpenObligations (M : Models) : Prop where
  rh : ATK.Conditional.Riemann.UniformLogBound
  beal : ATK.Conditional.Beal.GCDLowerBoundSmallExponents
  ns : ATK.Conditional.NavierStokes.EnstrophyAPrioriBound M.ns
  pnp : ATK.Conditional.PvsNP.SATNotInP M.cx M.sat
  hodge : ATK.Conditional.Hodge.MiddleCodimension M.hodge
  bsdRank : ATK.Conditional.BSD.RankOpen M.bsd
  bsdRefined : ATK.Conditional.BSD.RefinedOpen M.bsd
  ym : ATK.Conditional.YangMills.ConstructiveYM4D M.ym

/-- **Teorema-mestre**: pontes + obrigações abertas ⇒ os 7 enunciados. -/
theorem closedMath_of_obligations {M : Models} (hB : Bridges M) (hO : OpenObligations M) :
    SevenStatements M :=
  ⟨ATK.Conditional.Riemann.riemann_conditional hB.baezDuarte hO.rh,
   ATK.Conditional.Beal.beal_conditional hB.fermat hO.beal,
   ATK.Conditional.NavierStokes.ns_conditional hB.leray hO.ns,
   ATK.Conditional.PvsNP.pvsnp_conditional hB.cookLevin hO.pnp,
   ATK.Conditional.Hodge.hodge_conditional hB.lefschetz hO.hodge,
   ATK.Conditional.BSD.bsd_conditional hB.grossZagierKolyvagin hO.bsdRank hO.bsdRefined,
   ATK.Conditional.YangMills.ym_conditional hB.osterwalderSchrader hO.ym⟩

/-- Parte com enunciado OFICIAL (sem modelo): RH ∧ Beal. -/
def ClosedMathFaithful : Prop :=
  RiemannHypothesis ∧ ATK.Conditional.Beal.BealConjecture

/-- Os dois enunciados oficiais a partir de 2 pontes + 2 obrigações abertas. -/
theorem closedMathFaithful_of_obligations
    (hBD : ATK.Conditional.Riemann.BaezDuarteCriterion) (hFLT : FermatLastTheorem)
    (hRH : ATK.Conditional.Riemann.UniformLogBound)
    (hBeal : ATK.Conditional.Beal.GCDLowerBoundSmallExponents) :
    ClosedMathFaithful :=
  ⟨ATK.Conditional.Riemann.riemann_conditional hBD hRH,
   ATK.Conditional.Beal.beal_conditional hFLT hBeal⟩

/-! ## Firewall: por que modelos de brinquedo não fecham nada -/

/-- Num modelo de brinquedo (`GlobalSmooth := True`) o enunciado de NS vale trivialmente.
Isto NÃO é Navier–Stokes; mostra só que um "CLOSED" sobre modelo paramétrico sem a
obrigação de ligação é vazio. -/
theorem ns_toy_model_vacuous :
    ∃ M : ATK.Conditional.NavierStokes.NSModel.{0},
      ATK.Conditional.NavierStokes.ClayStatementA M :=
  ⟨{ Data := Unit, Admissible := fun _ => True, SmoothOn := fun _ _ => True,
     GlobalSmooth := fun _ => True, enstrophy := fun _ _ => 0 },
   fun _ _ => trivial⟩

/-- Num modelo de brinquedo (P = ∅, NP = tudo) "P ≠ NP" vale trivialmente. Isto NÃO é
P vs NP; mostra só que o enunciado paramétrico precisa do modelo genuíno. -/
theorem pnp_toy_model_vacuous :
    ∃ M : ATK.Conditional.PvsNP.ComplexityModel.{0}, ATK.Conditional.PvsNP.PneNP M :=
  ⟨{ Lang := Bool, P := ∅, NP := Set.univ, Red := fun _ _ => False,
     P_subset_NP := Set.empty_subset _,
     P_closed_under_red := fun h _ => False.elim h },
   Set.empty_ne_univ⟩

/-- Exact points for the eight original obligations, not replacement statements. -/
inductive ObligationPoint where
  | rh | beal | ns | pnp | hodge | bsdRank | bsdRefined | ym
  deriving DecidableEq

inductive PointStatus where
  | negative | undetermined | positive
  deriving DecidableEq

def pointStatement (M : Models) : ObligationPoint → Prop
  | .rh => ATK.Conditional.Riemann.UniformLogBound
  | .beal => ATK.Conditional.Beal.GCDLowerBoundSmallExponents
  | .ns => ATK.Conditional.NavierStokes.EnstrophyAPrioriBound M.ns
  | .pnp => ATK.Conditional.PvsNP.SATNotInP M.cx M.sat
  | .hodge => ATK.Conditional.Hodge.MiddleCodimension M.hodge
  | .bsdRank => ATK.Conditional.BSD.RankOpen M.bsd
  | .bsdRefined => ATK.Conditional.BSD.RefinedOpen M.bsd
  | .ym => ATK.Conditional.YangMills.ConstructiveYM4D M.ym

def pointEvidence (M : Models) (i : ObligationPoint) : PointStatus → Prop
  | .positive => pointStatement M i
  | .negative => ¬ pointStatement M i
  | .undetermined => True

theorem all_positive_iff_obligations (M : Models) :
    (∀ i, pointEvidence M i .positive) ↔ OpenObligations M := by
  constructor
  · intro h
    exact ⟨h .rh, h .beal, h .ns, h .pnp, h .hodge,
      h .bsdRank, h .bsdRefined, h .ym⟩
  · intro h i
    cases i
    · exact h.rh
    · exact h.beal
    · exact h.ns
    · exact h.pnp
    · exact h.hodge
    · exact h.bsdRank
    · exact h.bsdRefined
    · exact h.ym

theorem closedMath_of_positive_points {M : Models}
    (hB : Bridges M) (h : ∀ i, pointEvidence M i .positive) :
    SevenStatements M :=
  closedMath_of_obligations hB ((all_positive_iff_obligations M).mp h)

theorem negative_blocks_all_positive {M : Models} {i : ObligationPoint}
    (h : pointEvidence M i .negative) :
    ¬ (∀ j, pointEvidence M j .positive) :=
  fun hp => h (hp i)

end ATK.ClosedMath

#print axioms ATK.ClosedMath.all_positive_iff_obligations
#print axioms ATK.ClosedMath.closedMath_of_positive_points
#print axioms ATK.ClosedMath.negative_blocks_all_positive

#print axioms ATK.ClosedMath.closedMath_of_obligations
#print axioms ATK.ClosedMath.closedMathFaithful_of_obligations
#print axioms ATK.ClosedMath.ns_toy_model_vacuous
#print axioms ATK.ClosedMath.pnp_toy_model_vacuous
