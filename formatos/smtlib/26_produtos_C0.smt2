; D_N log N abaixo de C0 = 2 + gamma - log 4 pi (ATK.ErrosGram.produtos_abaixo_C0), N = 256 e 8000,
; com log 4 pi = 2 log 2 + log pi e log 5 = 2 log 2 + d, 0,2231435 < d < 0,2231436.
(set-logic QF_LRA)
(declare-const g Real) (declare-const l2 Real) (declare-const lp Real) (declare-const d Real)
(assert (< 0.5772156 g)) (assert (< 0.6931471803 l2)) (assert (< l2 0.6931471808))
(assert (< lp 1.1447300)) (assert (< 0.2231435 d)) (assert (< d 0.2231436))
(define-fun C0 () Real (- (+ 2.0 g) (+ (* 2.0 l2) lp)))
(assert (not (and (< (* 0.0082337162772 (* 8.0 l2)) C0)
                  (< (* 0.0050691202 (+ (* 6.0 l2) (* 3.0 (+ (* 2.0 l2) d)))) C0))))
(check-sat)
