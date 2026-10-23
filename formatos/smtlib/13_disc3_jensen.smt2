; Discriminante de J3 = g3 X^3 + 3 g2 X^2 + 3 g1 X + g0:
; disc3 = 27 [4(g1^2 - g0 g2)(g2^2 - g1 g3) - (g1 g2 - g0 g3)^2]  (ATK.ClosedMath.Jensen.disc3_jensen)
(set-logic QF_NRA)
(declare-const g0 Real) (declare-const g1 Real) (declare-const g2 Real) (declare-const g3 Real)
(define-fun A () Real g3) (define-fun B () Real (* 3.0 g2))
(define-fun C () Real (* 3.0 g1)) (define-fun D () Real g0)
(define-fun disc3 () Real
  (+ (- (- (- (* B B C C) (* 4.0 A C C C)) (* 4.0 B B B D)) (* 27.0 A A D D)) (* 18.0 A B C D)))
(assert (not (= disc3 (* 27.0 (- (* 4.0 (- (* g1 g1) (* g0 g2)) (- (* g2 g2) (* g1 g3)))
                                  (* (- (* g1 g2) (* g0 g3)) (- (* g1 g2) (* g0 g3))))))))
(check-sat)
