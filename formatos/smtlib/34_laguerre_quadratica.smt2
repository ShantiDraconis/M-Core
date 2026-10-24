; Laguerre (ATK.Laguerre.realRooted_add_C_mul_derivative) no grau 2: p = x^2 - s x + P com discriminante
; s^2 - 4P >= 0 (raizes reais); q = p + c p' = x^2 + (2c - s)x + (P - cs) tem discriminante 4c^2 + (s^2 - 4P) >= 0.
; Nega-se: espera-se unsat.
(set-logic QF_NRA)
(declare-const s Real) (declare-const P Real) (declare-const c Real)
(assert (>= (- (* s s) (* 4.0 P)) 0.0))
(assert (< (- (* (- (* 2.0 c) s) (- (* 2.0 c) s)) (* 4.0 (- P (* c s)))) 0.0))
(check-sat)
