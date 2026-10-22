; G(1 - s) = G(s): com x = s - 1/2, 1 - s - 1/2 = -x; G depende de x^2 (componentes).
(set-logic QF_NRA)
(declare-const a Real) (declare-const b Real) (declare-const d Real) (declare-const g Real)
(define-fun sqr ((p Real) (q Real)) Real (- (* p p) (* q q)))
(define-fun sqi ((p Real) (q Real)) Real (* 2.0 p q))
(define-fun Gr ((a Real) (b Real)) Real
  (- (* (+ (sqr (- a d) b) (* g g)) (+ (sqr (+ a d) b) (* g g))) (* (sqi (- a d) b) (sqi (+ a d) b))))
(define-fun Gi ((a Real) (b Real)) Real
  (+ (* (+ (sqr (- a d) b) (* g g)) (sqi (+ a d) b)) (* (sqi (- a d) b) (+ (sqr (+ a d) b) (* g g)))))
(assert (not (and (= (Gr (- a) (- b)) (Gr a b)) (= (Gi (- a) (- b)) (Gi a b)))))
(check-sat)
