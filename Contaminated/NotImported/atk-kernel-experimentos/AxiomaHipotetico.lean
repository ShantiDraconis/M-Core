import ATK.MundoHipotetico

/-!
# Experimento: o mundo hipotético como `axiom` e como `sorry`

Este arquivo **não** faz parte da biblioteca certificada (`lean_lib ATK` não o inclui e o CI
não o audita). Ele existe para registrar o que o kernel faz quando a hipótese é *postulada* em
vez de recebida como argumento. Saída registrada em `experimentos/AxiomaHipotetico.out`.

1. `axiom` fiel: o kernel aceita `RH ∧ Beal`, mas `#print axioms` mostra os axiomas novos.
2. `axiom` contraditório: o kernel aceita `RH ∧ ¬RH`.
3. `sorry`: o kernel aceita, e `#print axioms` mostra `sorryAx`.

Os três seriam **reprovados** por `scripts/check_axioms.py` (fonte com `axiom`/`sorry` e axiomas
fora de `propext`, `Classical.choice`, `Quot.sound`).
-/

namespace ATK.Experimento
open ATK.MundoHipotetico

/-! ## 1. Mundo fiel postulado -/
axiom S : Especificacao
axiom hS : Fiel S
axiom W : Mundo S

theorem rh_e_beal_postulados : RiemannHypothesis ∧ ATK.Conditional.Beal.BealConjecture :=
  fiel_fecha hS W

/-! ## 2. Mundo contraditório postulado -/
axiom Wc : Mundo especContraditoria

theorem rh_e_nao_rh : RiemannHypothesis ∧ ¬ RiemannHypothesis :=
  contraditorio_prova_rh_e_nao_rh Wc

theorem falso : False := (rh_e_nao_rh.2 rh_e_nao_rh.1)

/-! ## 3. Fechamento por `sorry` -/
theorem rh_por_sorry : RiemannHypothesis := sorry

end ATK.Experimento

#print axioms ATK.Experimento.rh_e_beal_postulados
#print axioms ATK.Experimento.rh_e_nao_rh
#print axioms ATK.Experimento.falso
#print axioms ATK.Experimento.rh_por_sorry
