From Coq Require Import Arith.
Require Import ATKClosure.

Module ATKSevenLanes.

Record SevenTerminalTypes : Type := {
  RH : Type;
  PNP : Type;
  YM : Type;
  NS : Type;
  BSD : Type;
  Hodge : Type;
  Beal : Type
}.

Record SevenInhabitants (T : SevenTerminalTypes) : Type := {
  rh : RH T;
  pnp : PNP T;
  yang_mills : YM T;
  navier_stokes : NS T;
  bsd : BSD T;
  hodge : Hodge T;
  beal : Beal T
}.

Theorem global_projects_rh :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    RH T.
Proof. intros T B; exact (rh T B). Qed.

Theorem global_projects_pnp :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    PNP T.
Proof. intros T B; exact (pnp T B). Qed.

Theorem global_projects_ym :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    YM T.
Proof. intros T B; exact (yang_mills T B). Qed.

Theorem global_projects_ns :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    NS T.
Proof. intros T B; exact (navier_stokes T B). Qed.

Theorem global_projects_bsd :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    BSD T.
Proof. intros T B; exact (bsd T B). Qed.

Theorem global_projects_hodge :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    Hodge T.
Proof. intros T B; exact (hodge T B). Qed.

Theorem global_projects_beal :
  forall (T : SevenTerminalTypes) (B : SevenInhabitants T),
    Beal T.
Proof. intros T B; exact (beal T B). Qed.

Definition build_seven
    (T : SevenTerminalTypes)
    (hRH : RH T)
    (hPNP : PNP T)
    (hYM : YM T)
    (hNS : NS T)
    (hBSD : BSD T)
    (hHodge : Hodge T)
    (hBeal : Beal T) :
    SevenInhabitants T :=
  {| rh := hRH;
     pnp := hPNP;
     yang_mills := hYM;
     navier_stokes := hNS;
     bsd := hBSD;
     hodge := hHodge;
     beal := hBeal |}.

Theorem global_iff_seven_inputs :
  forall (T : SevenTerminalTypes),
    (exists B : SevenInhabitants T, True) <->
    (exists hRH : RH T,
     exists hPNP : PNP T,
     exists hYM : YM T,
     exists hNS : NS T,
     exists hBSD : BSD T,
     exists hHodge : Hodge T,
     exists hBeal : Beal T, True).
Proof.
  intro T; split.
  - intros [B _].
    exists (rh T B), (pnp T B), (yang_mills T B),
      (navier_stokes T B), (bsd T B), (hodge T B), (beal T B).
    exact I.
  - intros [hRH [hPNP [hYM [hNS [hBSD [hHodge [hBeal _]]]]]]].
    exists (build_seven T hRH hPNP hYM hNS hBSD hHodge hBeal).
    exact I.
Qed.

End ATKSevenLanes.
