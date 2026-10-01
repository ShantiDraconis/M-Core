From Coq Require Import Arith Lia.

Module ATKClosure.

Inductive GateState : Type :=
| Open
| Closed.

Definition combine (a b : GateState) : GateState :=
  match a, b with
  | Closed, Closed => Closed
  | _, _ => Open
  end.

Theorem combine_closed_iff :
  forall a b,
    combine a b = Closed <->
    a = Closed /\ b = Closed.
Proof.
  intros a b; destruct a, b; simpl; split; intros H; try discriminate; auto.
Qed.

Record ReductionLane : Type := {
  State : Type;
  step : State -> State;
  defect : State -> nat;
  contract :
    forall x, 0 < defect x ->
      defect (step x) < defect x;
  freeze :
    forall x, defect x = 0 ->
      step x = x
}.

Record TerminalSpec (R : ReductionLane) : Type := {
  Inhabitant : Type;
  Certificate : Type;
  certify : Inhabitant -> Certificate
}.

Record ExactMaterializer
    (R : ReductionLane)
    (T : TerminalSpec R) : Type := {
  extract :
    forall x : State R,
      defect R x = 0 ->
      Inhabitant R T
}.

Record MaterialClosureWitness
    (R : ReductionLane)
    (T : TerminalSpec R) : Type := {
  terminal_state : State R;
  zero_defect : defect R terminal_state = 0;
  terminal_inhabitant : Inhabitant R T
}.

Definition close_with_exact_materializer
    (R : ReductionLane)
    (T : TerminalSpec R)
    (M : ExactMaterializer R T)
    (x : State R)
    (hz : defect R x = 0)
    : MaterialClosureWitness R T :=
  {| terminal_state := x;
     zero_defect := hz;
     terminal_inhabitant := extract R T M x hz |}.

Theorem zero_defect_not_arbitrary_terminal :
  ~ (forall (R : ReductionLane) (T : TerminalSpec R)
      (x : State R),
      defect R x = 0 ->
      exists y : Inhabitant R T, True).
Proof.
  intro H.
  refine (let R :=
    {| State := unit;
       step := fun x => x;
       defect := fun _ => 0;
       contract := _;
       freeze := _ |} in _).
  - intros x Hpos. lia.
  - intros x Hz. reflexivity.
  set (R := {|
    State := unit;
    step := fun x => x;
    defect := fun _ => 0;
    contract := fun x Hpos => ltac:(lia);
    freeze := fun x Hz => eq_refl
  |}).
  set (T := {|
    Inhabitant := Empty_set;
    Certificate := unit;
    certify := fun e => match e with end
  |} : TerminalSpec R).
  specialize (H R T tt eq_refl).
  destruct H as [e _].
  destruct e.
Qed.

Inductive OperatorKind : Type :=
| Traction
| Contraction
| Repression
| Torsion
| Excitation.

Record MaterialOperatorSystem : Type := {
  MState : Type;
  mdefect : MState -> nat;

  traction : MState -> MState;
  contraction : MState -> MState;
  repression : MState -> MState;
  torsion : MState -> MState;
  excitation : MState -> MState;

  traction_contract :
    forall x, 0 < mdefect x ->
      mdefect (traction x) < mdefect x;
  contraction_contract :
    forall x, 0 < mdefect x ->
      mdefect (contraction x) < mdefect x;
  repression_nonincrease :
    forall x, mdefect (repression x) <= mdefect x;
  torsion_preserves :
    forall x, mdefect (torsion x) = mdefect x;

  ExcitationCertified : MState -> Prop;
  excitation_contract :
    forall x,
      ExcitationCertified x ->
      0 < mdefect x ->
      mdefect (excitation x) < mdefect x
}.

Theorem torsion_cannot_strictly_close :
  forall (S : MaterialOperatorSystem) (x : MState S),
    0 < mdefect S x ->
    ~ mdefect S (torsion S x) < mdefect S x.
Proof.
  intros S x Hpos Hlt.
  rewrite (torsion_preserves S x) in Hlt.
  lia.
Qed.

End ATKClosure.
