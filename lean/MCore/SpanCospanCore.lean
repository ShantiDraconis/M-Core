import Mathlib.Data.Set.Basic

namespace MCore.Span

structure SpanCospan where
  F : Type
  M : Type
  I : Type
  R : Type
  kerC : M → M → Prop
  fib : M → Set M
  fixCR : M → M

def J_def : String :=
  "J = M_cl ∪ Indet; guarded expressions preserve syntax until collapse"

def firewall : String := "boundary crossing != collapse"

end MCore.Span
