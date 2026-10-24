; Quarteto de zeros (ATK.ZeroClasses.card_quatro): para x != c e y != 0, os pontos
; (x, y), (x, -y), (2c - x, y), (2c - x, -y) sao dois a dois distintos. Os seis pares reduzem-se a
; x != 2c - x e y != -y. Nega-se: espera-se unsat.
(set-logic QF_LRA)
(declare-const x Real) (declare-const y Real) (declare-const c Real)
(assert (not (= x c))) (assert (not (= y 0.0)))
(assert (or (= x (- (* 2.0 c) x)) (= y (- y))))
(check-sat)
