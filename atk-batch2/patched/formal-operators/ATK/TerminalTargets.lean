import ATK.KernelGates
/-!
These seven target predicates are EXTERNAL INPUTS, not the actual conjecture definitions.
Never certify a Millennium conjecture merely by inhabiting an arbitrary Prop.
The repository-specific semantic adapters must be installed and audited first.
-/
namespace ATK
structure SevenTargets where
  RH : Prop
  NS : Prop
  YM : Prop
  BSD : Prop
  Hodge : Prop
  Beal : Prop
  PNP : Prop

def SevenTargets.all (t : SevenTargets) : Prop :=
  t.RH ∧ t.NS ∧ t.YM ∧ t.BSD ∧ t.Hodge ∧ t.Beal ∧ t.PNP

structure SevenGates (t : SevenTargets) where
  rh : TerminalGate t.RH
  ns : TerminalGate t.NS
  ym : TerminalGate t.YM
  bsd : TerminalGate t.BSD
  hodge : TerminalGate t.Hodge
  beal : TerminalGate t.Beal
  pnp : TerminalGate t.PNP

def SevenGates.close {t : SevenTargets} (g : SevenGates t) : t.all :=
  close_seven g.rh g.ns g.ym g.bsd g.hodge g.beal g.pnp
end ATK
