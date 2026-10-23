; D31(g) = g1^3 - 2 g0 g1 g2 + g0^2 g3: (1,3,3,1) -> 10 e (1,3,6,6) -> -3
; (ATK.ClosedMath.Jensen.tp_a_nao_passa_gamma: TP de a nao passa para gamma = n! a)
(set-logic QF_NRA)
(define-fun D31 ((g0 Real) (g1 Real) (g2 Real) (g3 Real)) Real
  (+ (- (* g1 g1 g1) (* 2.0 g0 g1 g2)) (* g0 g0 g3)))
(assert (not (and (= (D31 1.0 3.0 3.0 1.0) 10.0) (= (D31 1.0 3.0 6.0 6.0) (- 3.0)))))
(check-sat)
