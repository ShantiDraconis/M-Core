; T28 (pontual): |F - P| <= E < L <= |P| exclui F = 0.
(set-logic QF_LRA)
(declare-const F Real) (declare-const P Real) (declare-const E Real) (declare-const L Real)
(define-fun absv ((v Real)) Real (ite (>= v 0.0) v (- v)))
(assert (<= (absv (- F P)) E))
(assert (<= L (absv P)))
(assert (< E L))
(assert (= F 0.0))
(check-sat)
