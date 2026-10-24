; Turan sob HR (ATK.JensenPolya.turan_de_rh): se J^{2,n}(X) = g0 + 2 g1 X + g2 X^2 com g2 > 0 tem uma raiz
; real x, entao g0 g2 <= g1^2 (pois (g2 x + g1)^2 = g1^2 - g0 g2). Nega-se: espera-se unsat.
(set-logic QF_NRA)
(declare-const g0 Real) (declare-const g1 Real) (declare-const g2 Real) (declare-const x Real)
(assert (> g2 0.0))
(assert (= (+ (* g2 x x) (* 2.0 g1 x) g0) 0.0))
(assert (> (* g0 g2) (* g1 g1)))
(check-sat)
