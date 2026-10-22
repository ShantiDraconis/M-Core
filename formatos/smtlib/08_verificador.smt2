; Correção do verificador (1D): |x - m| <= r < |m| e x = 0 é impossível.
(set-logic QF_LRA)
(declare-const x Real) (declare-const m Real) (declare-const r Real)
(define-fun absv ((v Real)) Real (ite (>= v 0.0) v (- v)))
(assert (<= (absv (- x m)) r))
(assert (< r (absv m)))
(assert (= x 0.0))
(check-sat)
