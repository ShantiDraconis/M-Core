theory ATK_Closure
  imports Main
begin

datatype gate_state = Open | Closed

fun combine :: "gate_state => gate_state => gate_state" where
  "combine Closed Closed = Closed"
| "combine _ _ = Open"

theorem combine_closed_iff:
  "combine a b = Closed <-> a = Closed & b = Closed"
  by (cases a; cases b; simp)

locale reduction_lane =
  fixes step :: "'s => 's"
    and defect :: "'s => nat"
  assumes contract:
    "defect x > 0 ==> defect (step x) < defect x"
    and freeze:
    "defect x = 0 ==> step x = x"

locale exact_terminal =
  reduction_lane step defect
  for step :: "'s => 's"
    and defect :: "'s => nat" +
  fixes extract :: "'s => 'inh"
    and certify :: "'inh => 'cert"
  assumes extract_only_at_zero:
    "defect x = 0 ==> True"
begin

definition close_with_exact_materializer ::
  "'s => 'inh * 'cert" where
  "close_with_exact_materializer x =
     (extract x, certify (extract x))"

end

datatype operator_kind =
    Traction
  | Contraction
  | Repression
  | Torsion
  | Excitation

locale material_operator_system =
  fixes defect :: "'s => nat"
    and traction :: "'s => 's"
    and contraction :: "'s => 's"
    and repression :: "'s => 's"
    and torsion :: "'s => 's"
    and excitation :: "'s => 's"
    and excitation_certified :: "'s => bool"
  assumes traction_contract:
    "defect x > 0 ==> defect (traction x) < defect x"
    and contraction_contract:
    "defect x > 0 ==> defect (contraction x) < defect x"
    and repression_nonincrease:
    "defect (repression x) <= defect x"
    and torsion_preserves:
    "defect (torsion x) = defect x"
    and excitation_contract:
    "excitation_certified x ==> defect x > 0
      ==> defect (excitation x) < defect x"
begin

theorem torsion_cannot_strictly_close:
  assumes "defect x > 0"
  shows "~ defect (torsion x) < defect x"
  using torsion_preserves by simp

end

text "
Cross-prover semantic rule:
a zero structural defect is not itself a proof of an arbitrary terminal
mathematical proposition.  Each concrete lane must supply its own extract
function into the fixed terminal type.
"

end
