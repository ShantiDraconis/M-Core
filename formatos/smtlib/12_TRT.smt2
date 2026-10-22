; T R T (w) = conj(w) + i, com T(s) = i conj(s), R(s) = 1 - conj(s); fixo sse Im w = 1/2.
(set-logic QF_LRA)
(declare-const a Real) (declare-const b Real)
; T(a+bi) = i(a - bi) = b + a i
; R(b + a i) = 1 - (b - a i) = (1 - b) + a i
; T((1-b) + a i) = i((1-b) - a i) = a + (1-b) i
(define-fun re3 () Real a)
(define-fun im3 () Real (- 1.0 b))
(assert (not (and (= re3 a) (= im3 (+ (- b) 1.0))
                  (= (and (= re3 a) (= im3 b)) (= b 0.5)))))
(check-sat)
