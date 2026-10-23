; Integral por pedacos (ATK.GramDois.contraexemplo_pedaco): com 0,4054651081081 < log(3/2) < 0,4054651081082,
; o valor correto 1/2 - 2 log(3/2) + 1/3 e > 0 e o do texto 1/2 - (5/2) log(3/2) + 1/3 e < 0.
(set-logic QF_LRA)
(declare-const L Real)
(assert (< 0.4054651081081 L)) (assert (< L 0.4054651081082))
(assert (not (and (> (+ 0.5 (* (- 2.0) L) (/ 1.0 3.0)) 0.0) (< (+ 0.5 (* (- 2.5) L) (/ 1.0 3.0)) 0.0))))
(check-sat)
