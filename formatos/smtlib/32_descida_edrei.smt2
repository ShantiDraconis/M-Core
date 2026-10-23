; Descida de Edrei (ATK.Edrei.passo / descida): com a0 = 1 e |w| = 2, cada passo tira um zero real com
; L_j >= 1/(a0*|w|) = 1/2 e baixa b1 de L_j*b0 = L_j; partindo de b1 = 1, tres passos dariam b1 < 0, mas
; b1 >= 0 (menor 1x1 de colunas iniciais). Logo no maximo a0*|w|*b1 = 2 passos: o sistema e insatisfazivel.
(set-logic QF_LRA)
(declare-const b0 Real) (declare-const b1 Real) (declare-const b2 Real) (declare-const b3 Real)
(declare-const L0 Real) (declare-const L1 Real) (declare-const L2 Real)
(assert (= b0 1.0))
(assert (>= L0 0.5)) (assert (>= L1 0.5)) (assert (>= L2 0.5))
(assert (= b1 (- b0 L0))) (assert (= b2 (- b1 L1))) (assert (= b3 (- b2 L2)))
(assert (>= b3 0.0))
(check-sat)
