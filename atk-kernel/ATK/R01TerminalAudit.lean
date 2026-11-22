import ATK.FinalRoot
import ATK.ClosedMathReal
import ATK.ProdutoresTN
import ATK.TeoremaGlobal
import ATK.ObrigacoesMinimas

/-!
R01 kernel probe. These commands inspect types and transitive axioms; they do not
create an inhabitant of RH, Produtores, PontesRestantes, Lacunas or FINAL_ROOT.
Execute from atk-kernel/: lake env lean ATK/R01TerminalAudit.lean
-/

#check @ATK.FinalRoot.raiz_de_produtores
#print axioms ATK.FinalRoot.raiz_de_produtores
#check @ATK.FinalRoot.verde_fiel_iff
#print axioms ATK.FinalRoot.verde_fiel_iff
#check @ATK.ClosedMathReal.closedMath_real
#print axioms ATK.ClosedMathReal.closedMath_real
#check @ATK.ProdTN.nonempty_iff_rh
#print axioms ATK.ProdTN.nonempty_iff_rh
#check @ATK.ProdTN.rh_of_kernel
#print axioms ATK.ProdTN.rh_of_kernel
#check @ATK.TeoremaGlobal.teorema_global
#print axioms ATK.TeoremaGlobal.teorema_global
#check @ATK.ObrigacoesMinimas.closedMath_minimo
#print axioms ATK.ObrigacoesMinimas.closedMath_minimo

/-!
A green probe establishes that these *specific declarations* elaborate and
their reported axiom sets are inspectable. No proof-status promotion is implied.
-/
